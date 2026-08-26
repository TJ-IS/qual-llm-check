---
otero_id: 17971
otero_key: "NPNKFYA8"
title: "Group decision support systems: Factors in a software implementation"
authors: "David Sutherland; Robert Crosslin"
year: "1989"
journal: "Information & Management"
doi: "10.1016/0378-7206(81)90075-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Group Decision Support Systems: Factors in a Software Implementation

David Sutherland and Robert Crosslin
The University of Maryland, Baltimore County, Information Systems Management Department, Catonsville, MD 21228, USA

The implementation of a Group Decision Support System (GDSS) is a major consideration of “networked” organizations. This article presents the results of a study that focused on an interactive software implementation of the Analytic Hierarchy Process (AHP) as a GDSS. State policy makers used the AHP to ascertain factors critical to their success. Four different implementations were used; the results of these indicate that varied inconsistency levels will be experienced, based on how it is implemented. Recommendations for future implementation of GDSS are given.

Keywords: Decision Support Systems, Group Decision Support Systems, Networks, Systems Implementation, Human Factors.

![](/api/attachments/NPNKFYA8/fulltext/images/b2e731219a11fe393a3e52bfb05484cde49704fef8667dc58b3fb5d7d4c77991.jpg)

David Sutherland is an an Assistant Professor in the Information Systems Department of the University of Maryland, Baltimore County. His Ph.D. is from the University of Virginia. He has been working with computers in both industry and education for the past twelve years. He currently teaches systems analysis and design techniques, information systems utilization and operations analysis. Dr. Sutherland is currently conducting research on software productivity as well as organizational structure's relationship to IS at the International Center for Information Technologies (ICIT) in Washington, D.C. He was a co-editor of ICIT's recently released book, Measuring the Business Value of Information Technologies.

## 1. Introduction

Implementations of systems to aid in group decision making process often have led to difficulty [1,12]. This seems to arise when the process is confounded by the multiple differences represented in a group: their context and particular decision process. A group of researchers at the Carnegie Institute of Technology between 1957 and 1964, developed a theory of organizational decision making [24]. This worked toward a science of decisions in management situations and led to what became “the most well-established ‘behavioral’ perspective in MIS and Management Science” [13]. The research presented here combines the behavioral perspective with the organizational perspective, while addressing a specific implementation of a facilitated group decision system.

Early work, including that of Licklider, alluded to “interactive” computer systems that would facilitate organizational communication and decision making. As new technology emerged, the

![](/api/attachments/NPNKFYA8/fulltext/images/f278d9746873bbe296714a1f80621e4384ed722d46d80b1798c809e901ee97d3.jpg)

Robert Crosslin is an economist with extensive teaching, research and consulting experience in state and federal government automated information systems on mainframe, mini, and microcomputers. His Ph.D. is from the University of Missouri. Particularly relevant to this research is his experience in managing the design of MIS and DSS systems for the U.S. Departments of Labor, Education and Defense. He has also performed several economic evaluations of existing and

proposed MIS systems for these same federal agencies and state agencies and institutions with whom they interact. He also has research and teaching experience in the areas of economic and simulation modeling. In addition, Dr. Crosslin is a Certified Public Accountant.

interactive aspects of the technology were refined and applications of those were implemented [10]. As this development took place, few researchers continued the empirical development of models for decision making in complex organizations. Much of the research centered on the individual supported by a computer based decision tool [14,8,5,4], and much research was conducted in the organizational context and DSS use [25,26,7]. While the individual and the organization are obvious considerations, little research has been conducted in the area of group decision making, yet the ability of computer technology to support it continues to increase.

The need for GDSS is highlighted by the identification of a phenomenon in organizational behavior: Networked Organizations. By allowing individuals within and across organizations to share tasks through communications links, new networked organizations are being established. Miles and Snow [15] address the concept of the dynamic network. The authors present the concept of new organizational form as a combination of strategy, structure, and management processes; many of these are based on information technologies (IT). Such systems allow participants to hook into a predefined and negotiated general structure for a working relationship based on the information shared and manipulated, including that used in the GDSS.

Currently, a group user of a computer system not only interacts with a single machine, but also with multiple machines and their users through telecommunications links. Managers are looking for guidance in defining group decision making, as well as decisions on which implementations of technology will best support group decision making. To guide them, two aspects of GDSS must be considered: first, the context in which decision making takes place; and second, in light of the context, the vehicle that is incorporated in the decision making.

In this research, the aspects of context and vehicle were considered in the implementation of a computer based GDSS – the process as well as the product. We feel that researchers have not paid enough attention to the process of GDSS, having focused their attention on the product. The GDSS under investigation between May and July 1987 utilized an interactive software implementation of the Analytic Hierarchy Process (AHP).

The decision process was conducted with individuals in an organization located throughout the United States and Puerto Rico.

## The Analytic Hierarchy Process

For over a decade, the AHP has been used to facilitate group decision making in various fields. AHP is a structured tool for setting priorities among competing alternatives in group decision making settings $[17,19,20,21,9,23,22,16,11,2,3]$ . The process involves a group of individuals developing lists of items that are of importance to a specified topic, ranking those items, and then conducting pairwise comparisons of those items, weighting each item as it is compared to each other item. The weightings of these items are then compared to the weightings that each other member of the group has assigned. The outcome is a ranked list of items. AHP allows multiple levels of factor influences (i.e., a hierarchy), with factors at a lower level influencing a factor at a higher level which, in turn, influences factors at the next level until the decision is reached.

Saaty asserts that a hierarchy is an abstraction of the structure of a system [18]. A decision that has more than one factor affecting the outcome is also a system. Therefore, the Analytic Hierarchy Process can be used to model decisions about the structure of a system. However: Which elements make up the system's structure? and What is the relative importance or strength of each element in that structure? Ultimately these sub-decisions on a system's structure yield the final, overall decision. The process by which a group arrives at these decisions, including the technology involved, can have a significant impact on the final outcome and on the group members' satisfaction with the decision.

The AHP works computationally by defining the structure of a hierarchy and comparing the factors at each level for their influence on the factor (or, ultimately, the goal) at the next higher level. For each pairwise factor comparison, a number representing the judgement of the participants on the relative strengths of the two factors is inserted into the upper half of a square matrix. The eigenvector with the largest eigenvalue is found. This represents the priority ordering of the factors; each element being its relative strength, and the eigenvalue is a measure of the consistency of the pairwise judgements.

## 2. Current Research

Our research used AHP to help U.S. state policy makers and program administrators decide which factors would be most important in securing the future of state and local Labor Market Information (LMI). The effort took five months to prepare and involved the participation of the directors of state LMI from each of the fifty states. Each was asked to take part in a process that used AHP. A software implementation of AHP was used; it provides accuracy in the process, as well as quick turnaround. Results were presented to the LMI directors at their annual conference in July 1987, one month after the actual LMI AHP process was initiated.

LMI directors are part of each state's employment security (i.e., labor) department and are in charge of employment research and statistics on the supply of and demand for categories of workers in the labor markets within their state. These are used for state policymaking and by the employer community for economic development. Much LMI data is transmitted to the federal level, with the majority of the funding for these activities coming from the Department of Labor; the directors share many common statistical methodologies as well as problems. They come together each year to discuss current and future LMI policies and programs. The theme for their 1987 conference focused on improving state and local labor market information.

## Purpose of the Research

DeSanctis and Gallupe [6] have presented a taxonomy for GDSS research. They refer to an information exchange view of the GDSS process that is based on three levels of systems. Level 1 provides “technical features for removing common communication barriers.” Level 2 provides “decision modeling and group decision techniques aimed at reducing uncertainty and ‘noise.’” Level 3 “are characterized by machine-induced group communication patterns.”

The GDSS under study is at both Levels 1 and 2. The software implementation of the AHP, along with the use of existing communications features, provided a means for facilitating communication. It also provided a means of reducing “noise” in the decision process, although we show there is variance in its levels of “noise” or there is inconsistency, depending on various factors in the GDSS implementation.

Our purpose was to establish the effectiveness of alternative ways of deciding the factors to be ranked and to determine the effectiveness of the software implementation of the AHP. A secondary objective was to determine necessary features that an automated GDSS should contain in order to improve group satisfaction.

When AHP is used, it is generally during a meeting, dynamically, with attendees generating factors, discussing, ranking, and comparing them. Similar processes occur when using other group decision processes, such as the Delphi Technique. A process such as this requires quick interaction and effective group leadership. To determine the effectiveness of alternative means of factor determination, our current research used a modified Delphi technique implemented in four groups:

(1) The respondents determined and ranked factors using an electronic network.

(2) They determined and ranked the factors using the U.S. mail system.

(3) The respondents reviewed the set of factors determined by the above groups prior to arriving at the national conference and then ranked those factors in a one hour meeting.

(4) They determined and ranked the factors while at the conference, using the common implementation of the AHP.

Group 1 consisted of LMI directors who use a form of Electronic Mail. They used two distinct E-Mail systems, and though these systems differed, the main concern of the research was that the process for factor surfacing and eventual feedback could be conducted on an E-Mail network. It was thought that these people would also use the E-Mail functions to communicate with others in Group 1 about the factors and process.

Group 2 worked in parallel with Group 1, but did not have E-Mail for factor surfacing or information communication. They were given a list of names and addresses of their fellow team members and were encouraged to communicate either through the mails or by phone. The group was drawn randomly and represented various regions of the U.S.

Group 3 members received a list of the factors surfaced by Groups 1 and 2 a week before the national conference. They were asked to read it and add others they felt were necessary. They were told that they would spend an hour at the national conference discussing and ranking the factors and then conducting a pairwise comparison of them. This meant that Group 3 members had some time to think and to discern new factors. They were also given a list of others in their group but were not encouraged to contact them.

Group 4 members were told only that they would meet at the conference for an hour. They were not told the reason, but were told that it was very important. At the conference, the team developed a list of factors critical to LMI success, ranked them, and then compared each to every other.

## 3. Methodology

Other than the group using Electronic Mail for factor rounds, the groups were randomly assigned. The software implementation of AHP, Expert Choice, was used to determine the hierarchy of factors within each group. Data on the level of factor ranking consistency between and within groups were calculated, and analysis was conducted on the consistency. Data on affective variables were gathered through the use of a questionnaire and interviews after the sessions: this included such areas as concordance with the overall treatment, agreement on the ranked factors of their group, acceptability of time allotted, and interest of each participant in using a similar process in the future.

Among the research questions established at the outset were:

(1) Would use of automated GDSS lead to inconsistency in the decision process?

(2) What would be the overall effect on inconsistency of extra time to consider the factors?

(3) Would groups with more time to conduct the process have a higher approval level for their ranked factors?

(4) Would groups with more time to conduct the process have a higher concordance level with the overall process?

(5) Would groups with more time to conduct the process have a higher stake in their outcome?

(6) Would groups with more time to conduct the process be more comfortable with the time they had for working with factors?

## 4. Outcomes

The group outcomes were factors that the members of each group felt would improve the future of state and local labor market information. For example, the seven factors of one group were:

\- increased funding for LMI activities

\- increased Federal assistance and guidance

\- improved data series

\- expansion of the occupational employment statistics program

\- improved state marketing of LMI resources and products

\- increased quantity and quality of wage surveys

\- standard LMI definitions across the states

Figure 1 shows the final ranking of these by the group. The relative weights of the factors sum to one. Figure 1 is a copy of the GDSS screen produced by the software, as viewed by participants.

## Quantitative Findings

The inconsistency of individual and group judgements in the pairwise comparisons of factors is one objective measure of the quality of a decision. The software implementation provide the traditional measure of transitivity of preferences between factors and the cardinal consistency in the strength of factor preferences. “It is not whether (decisionmakers) are inconsistent on particular (factor) comparisons that matters, but how strongly consistency is violated in the numerical sense for the overall problem under study” [19].

The software-produced Inconsistency Ratios for the groups are shown in Table 1. Studies have shown that inconsistent judgements in multi-factor comparisons occur randomly with a 10 percent frequency. Inconsistent judgements greater than 10 percent are therefore classified as nonrandom and a cause for concern. Groups 1 and 2 had the lowest group inconsistency ratios, while Groups 3 and 4 were higher. This addresses our second question. Furthermore, the mean standard deviation of priority weights was lower for Groups 1 and 2, lending additional support to the hypothesis. The fact that the group inconsistency ratios were all low addresses our question about automated group decision support systems leading to judgement decisions that are well within objectively established critical limits for consistency.

![](/api/attachments/NPNKFYA8/fulltext/images/30cea4f17330cdf8730c2edaef09d056cf571a8f1bda6455ff0f33eeb65a4670.jpg)  
Fig. 1. Judgements with Respect to Goal of Improving Localized LMI.

Individual inconsistency ratios varied widely within each group, many of them being two to three times the ratio for random occurrence. This implies that the averaging process of combining priority weights reduced the level of group inconsistent judgements. It also suggests that individuals may alter their internal judgement as they go through the decision process. The important implication here is that GDSS should provide for reconsideration by individuals prior to calculating final decisions.

State Labor Market Information (LMI) Directors: AHP Group Inconsistency Ratios in Comparing Factors to Secure the Future of LMI Programs.

<table><tr><td>Subject Group</td><td>Inconsistency Ratio</td></tr><tr><td>1</td><td>0.036</td></tr><tr><td>2</td><td>0.031</td></tr><tr><td>3</td><td>0.078</td></tr><tr><td>4</td><td>0.053</td></tr></table>

Individuals will often strongly disagree on the relative importance of factors affecting the group's decision. Although each of the four groups surfaced "increased funding" as a factor and ranked it at or near the top, there was wide variation in the numerical weightings given to this. The wide variation in pairwise rankings occurred for all factors and within each group. People attempt to reduce this variation, whether or not numerically measured, in the communication process while reaching a group decision. Automated GDSS, to be effective, should provide a means for calculating and displaying these variations, so group users might efficiently address the underlying reasons for the disagreement, as in the traditional consensus methodologies. The AHP software unfortunately did not have this feature; however, we used a separate spreadsheet package as an interface to enter individual pairwise factor weightings and to calculate and display within-group variation, before progressing to the group-input (i.e., one pairwise weighting per group) procedures allowed by the GDSS software. This was illuminating and highlighted the otherwise masked within group variation of individual decisions.

As we expected, the two groups that had more time to reflect on the factors and their relative importance to the group's decision had significantly smaller deviations than the other two groups; there was more initial agreement on factor weightings. GDSS should incorporate this type of "individual input, initial variances in agreement" feature to facilitate group discussions and final decisions.

The individual Inconsistency Ratios varied widely within each group as well across groups, as can be seen in Table 2. In fact only 2 of 39 individual Inconsistency Ratios were less than the expected random cut-off of 0.10. This implies that the averaging process of combining individual priority weights reduced the level of group-inconsistent judgements. The amount of variability in individual Inconsistency Ratios for each group is graphically depicted in the boxplots in Figure 2. Note that Group 4, which had the least amount of time to reflect and consider their judgments, had by far the widest range of individual Inconsistency Ratios.

Table 3 presents the results of t-tests for significance of differences between the various group means. Groups 1 and 2 had significantly lower means for individual Inconsistency Ratios. Since they had several days to consider the relative strengths for each factor, this may imply that individuals often alter their judgements as they progress temporally through the group decision process. This result has important implications for the design of automated GDSS. First, it should provide for reconsideration of judgements prior to calculating final decisions (Expert Choice provides this.) Second, such software should provide for input of individual sub-decisions (e.g., pairwise factor comparisons in the AHP) that are subsequently combined in generating group decisions; these sub-decisions and their associated internal consistency should be provided to facilitate reconsideration before calculating a group result. If only group sub-decisions are input, then much of the technological and processing power and value will be missed.

Group inconsistency is partly a result of disagreement within the group and, we assume, consequently results in less individual satisfaction with the group decision. We tested this assumption by

Table 2  
State Labor Market Information (LMI) Directors: AHP Individual Inconsistency Ratios in Comparing Factors to Secure the Future of LMI Programs.

<table><tr><td>Group i</td><td>State k</td><td>Inconsistency ratio (in percent)</td></tr><tr><td>1</td><td>1</td><td>5.9</td></tr><tr><td>1</td><td>2</td><td>9.8</td></tr><tr><td>1</td><td>3</td><td>12.7</td></tr><tr><td>1</td><td>4</td><td>16.6</td></tr><tr><td>1</td><td>5</td><td>19.5</td></tr><tr><td>1</td><td>6</td><td>21.1</td></tr><tr><td>1</td><td>7</td><td>22.2</td></tr><tr><td>1</td><td>8</td><td>22.7</td></tr><tr><td>1</td><td>9</td><td>27.9</td></tr><tr><td>1</td><td>10</td><td>27.9</td></tr><tr><td>1</td><td>11</td><td>30.1</td></tr><tr><td>1</td><td>12</td><td>38.4</td></tr><tr><td>2</td><td>13</td><td>7.3</td></tr><tr><td>2</td><td>14</td><td>7.9</td></tr><tr><td>2</td><td>15</td><td>14.7</td></tr><tr><td>2</td><td>16</td><td>15.0</td></tr><tr><td>2</td><td>17</td><td>19.8</td></tr><tr><td>2</td><td>18</td><td>21.0</td></tr><tr><td>2</td><td>19</td><td>22.2</td></tr><tr><td>2</td><td>20</td><td>22.4</td></tr><tr><td>2</td><td>21</td><td>58.5</td></tr><tr><td>3</td><td>22</td><td>18.5</td></tr><tr><td>3</td><td>23</td><td>23.3</td></tr><tr><td>3</td><td>24</td><td>27.5</td></tr><tr><td>3</td><td>25</td><td>34.7</td></tr><tr><td>3</td><td>26</td><td>35.1</td></tr><tr><td>3</td><td>27</td><td>35.3</td></tr><tr><td>3</td><td>28</td><td>35.3</td></tr><tr><td>4</td><td>29</td><td>7.6</td></tr><tr><td>4</td><td>30</td><td>9.4</td></tr><tr><td>4</td><td>31</td><td>10.1</td></tr><tr><td>4</td><td>32</td><td>12.5</td></tr><tr><td>4</td><td>33</td><td>13.4</td></tr><tr><td>4</td><td>34</td><td>15.7</td></tr><tr><td>4</td><td>35</td><td>15.9</td></tr><tr><td>4</td><td>36</td><td>22.1</td></tr><tr><td>4</td><td>37</td><td>78.5</td></tr><tr><td>4</td><td>38</td><td>82.8</td></tr><tr><td>4</td><td>39</td><td>99.9</td></tr><tr><td colspan="2">Mean, All Participants</td><td>26.18</td></tr><tr><td colspan="2">Standard Deviation</td><td>20.60</td></tr><tr><td colspan="2">Mean, Group 1</td><td>21.23</td></tr><tr><td colspan="2">Standard Deviation</td><td>8.80</td></tr><tr><td colspan="2">Mean, Group 2</td><td>20.98</td></tr><tr><td colspan="2">Standard Deviation</td><td>14.32</td></tr><tr><td colspan="2">Mean, Group 3</td><td>29.96</td></tr><tr><td colspan="2">Standard Deviation</td><td>6.41</td></tr><tr><td colspan="2">Mean, Group 4</td><td>33.45</td></tr><tr><td colspan="2">Standard Deviation</td><td>33.39</td></tr></table>

Fig. 2. Box-Plots of Variability in Group Inconsistency Ratios.

performing a loglinear regression, using individual agreement/disagreement with the group's final decision as the dichotomous dependent variable and the group's Inconsistency Ratio as the predictor variable. The model obtained an overall good fit to the data, with a Chi-square goodness-of-fit value of 148. As the predictor variable coefficient of 6.9 indicates, the probability of individual agreement with the final decision is inversely related to function of the group Inconsistency Ratio. Once again, automated versions of GDSS techniques should take into account these methods of analyzing and improving individual and group consistency and agreement. Otherwise, users of automated GDSS may distrust and disdain their use in favor of the less precise, but more perceptually comforting, techniques of the past; then both users and IS professionals will not gain the potential of such techniques.

State Labor Market Information (LMI) Directors: Significance of Difference Between Group Means of AHP Individual Inconsistency Ratios in Comparing Factors to Secure the Future of LMI Programs.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="4">Comparison with Group *</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Mean, All Participants</td><td>26.18</td><td></td><td></td><td></td><td></td></tr><tr><td>Standard Deviation</td><td>26.60</td><td></td><td></td><td></td><td></td></tr><tr><td>Mean, Group 1</td><td>21.23</td><td></td><td>0.04</td><td>2.34</td><td>1.12</td></tr><tr><td>Standard Deviation</td><td>8.80</td><td></td><td>(0.48)</td><td>(0.02)</td><td>(0.14)</td></tr><tr><td>Mean, Group 2</td><td>20.98</td><td></td><td></td><td>1.58</td><td>1.06</td></tr><tr><td>Standard Deviation</td><td>14.32</td><td></td><td></td><td>(0.07)</td><td>(0.15)</td></tr><tr><td>Mean, Group 3</td><td>29.96</td><td></td><td></td><td></td><td>0.32</td></tr><tr><td>Standard Deviation</td><td>6.41</td><td></td><td></td><td></td><td>(0.38)</td></tr><tr><td>Mean, Group 4</td><td>33.34</td><td></td><td></td><td></td><td></td></tr><tr><td>Standard Deviation</td><td>33.39</td><td></td><td></td><td></td><td></td></tr></table>

\* t-values with significance level in parenthesis. A one-way analysis of variance on the individual Inconsistency Ratios was first performed; the ANOVA produced an F-ratio of 61.4 (1.38 d.f.) corresponding to a chance probability of less than 0.001. This confirmed that the Inconsistency Ratios of the four groups are from different distributions and allowed the six pairs of group mean t-tests.

## Qualitative Findings

The use of a questionnaire and subsequent interviews afforded us information on the affective elements of the AHP factor surfacing processes. Twenty-seven of forty-seven questionnaires were returned for a response rate of 56%. Although the n and response rate are not as high as one would hope, the information may be taken as anecdotal and offer a second dimension to the researchers' findings.

The questionnaire was constructed with the assistance of the Interstate Conference of Employment Security Agencies' LMI Coordinator. Ten questions were presented to the Directors using a five point Likert type for measures during a conference session, where all the findings were presented to the entire group. The questionnaires were analyzed by determining the average and standard deviation of the response.

Each group felt the factors they identified represented the most important factors. This is interesting, in light of the variance in their findings. As a matter of fact, Group 4, who met only during the national conference, focused their discussion and therefore their factors on reactions to a speaker who had just made a presentation before the group met with the researchers.

Group 4's agreement with the importance of their factors says something about the temporal effect of the level of importance. In a group decision supported process, time to reflect may be an important factor; e.g., we often need to “sleep on” a potential decision.

All groups felt their personal views were represented in the group decision. This is important because stake holding in a decision will be strengthened if members feel comfortable with the result. One individual using the E-Mail function strongly felt that his personal views were not represented because he was away from his terminal during part of the process time, and because the computer which housed his E-Mail function was shut down part of the time. This anecdote points out the importance of links in a networked decision process. If individuals do not have access to the link, they will not have a stake in the decision.

When asked about the time they had to consider the factors and clarify issues before ranking them, Group 4 felt they were given inadequate time, while Group 3 were most comfortable with it. Group 4 completed the entire process in a little over an hour. An AHP is often conducted in group decision making in this way. Individuals in Group 3, on the other hand, were given factors determined by Group 2 and asked to reflect on them before going to the conference. Group 3 did not feel constrained by the time and could reflect on the factors.

Groups 1 and 2 spent much of their time discerning factors as well as determining rankings. Their level of concordance with the time taken was higher than Group 4, but not as high as Group 3. This would indicate that the factor surfacing process, regardless of the medium on which it is performed, is thought-intensive and warrants time.

The level of rigor each group brought to their consideration reflected the amount of time the individuals had before comparing. Groups 1 and 2 indicated that their consideration of factors was rigorous while Groups 3 and 4 did not. Again, this shows that credibility of the results of a group decision making process may be dependent on the time to reflect on the factors before comparison.

Reflection time played a role in the actual pair-wise comparison process. Whereas Groups 1 and 2 felt this comparison process allowed them to think through the importance of their factors, Groups 3 and 4 were constrained for time and therefore indicated less concordance with the thought process. This indicates that the credibility of the ultimate decision will be weighted by the time to reflect on the factors. Also, Groups 1 and 2 showed a higher level of concordance than Groups 3 and 4. All agreed that they would like to use the AHP process again, with Groups 1 and 2 showing a higher level of agreement. All Groups indicated they would like more information on GDSS.

It was interesting to note the actual time participants spent. Group 2 reported an average of two hours, while the other groups reported times averaging around one hour. Of course, Groups 3 and 4 were limited in their reflection time, although Group 3 did have time before the process.

Again, the time factor could indicate the time individuals spent thinking about the factors; if one looks at the variance of factors within and between groups, one sees the inverse correlation between total time spent on the process and group inconsistency in decision making.

## 5. Conclusions and Recommendations

Our findings relate to the process as well as the product. As we began to work with the data, a number of considerations began to emerge.

1 Would use of automated GDSS lead to inconsistency in the decision process?

Our results suggest no. Relatively high group consistency was achieved while maintaining both individual and group satisfaction. This was true in spite of relatively high inconsistencies for individuals.

2 What would be the overall effect on inconsistency of extra time to consider the factors?

Apparently, individuals given more time to reflect in the GDSS showed higher individual and within-group consistency. Here, group inconsistency ratios were all less than 10%, but this is not necessarily due to the automated GDSS. Even though the inconsistency levels were within acceptable limits, one might argue that these levels would have been attained with or without the use of an automated GDSS and might be attributable to the use of the AHP. But it would have been nearly impossible to conduct the AHP decision process in this study without the use of Expert Choice. Results of the overall process and across group comparisons were presented two hours after the final group met, and post-hoc analysis of the data maintained was made possible by the software.

3 Would groups with more time to conduct the process have a higher approval level for their ranked factors?

All groups had a high approval level for their ranked factors. This may be due to the process, which allowed for individual involvement. But this should be considered in light of the inconsistency ratios; this leads one to speculate that though the decision participant may feel comfortable with the final decision, the decision may be sub-optimal.

4 Would groups with more time to conduct the process have a higher concordance level with the overall process?

Although all groups stated they would like to use the process again, Groups 1 and 2 showed a higher level of concordance. Groups 1 and 2 stated they were more rigorous in their consideration and ranking of factors. This might be a basis for comfort with the process and be considered a factor of the time given the group. Further study is needed to clarify this point.

5 Would groups with more time to conduct the process have a higher stake in their outcome?

All group members felt they had a stake in the decision. The process and use of an automated GDSS allowed for objective analysis of the factors, and the decision was therefore considered egalitarian. Again, this finding should be considered in light of the inconsistency ratios, and implementors of GDSS should consider the effects of such implementation.

Although the participants felt they held a stake in the final decisions, the decisions varied between groups, and, as stated above, Group 4's factors related closely to a conference discussion just prior to their meeting to determine important factors: the temporal effect must be considered.

6 Would groups with more time to conduct the process be more comfortable with the time they had for working with factors?

Group 4, with the least time to contemplate the factors, had the lowest concordance with time given to conduct the process. Group 3 had the highest; it was given the factors surfaced by Groups 1 and 2 before attending the conference. This finding is interesting, in light of the fact that Groups 1 and 2 had the most time to conduct the process. Perhaps Groups 1 and 2 did not feel comfortable because they were asked to brainstorm factors, a time consuming effort. But, in this effort, GDSS users will decide its strengths. Again, the concept of networked organizations requires such effort, and anything less than full group participation may lead to less than optimal decisions.

## 6. Recommendations

In light of the findings, a number of recommendations for GDSS consideration surface.

\- Study the current process for decision making in the organization and introduce GDSS by facilitating that process.

It is important that the users not confuse a new decision process with the introduction of a GDSS. To eliminate this confusion, it should be introduced as support for a well understood decision process.

\- Identify stake-holders and introduce the GDSS to them.

The individuals with insight should be made a part of the GDSS. The outcome is only as good as its participant base, and exclusion of key stakeholders may lead to political failure.

\- Introduce the GDSS in several less-than-critical decisions before making a critical one.

The effect of a new GDSS might blur the intent of the decision process. Using it in several less-than-critical decision situations will allow the user to become comfortable with the system and to question the process while considering the product.

\- Ensure that the GDSS has individual input with an interface to group calculations and to final decisions.

Allowing the GDSS users to have an interface forces them to question their intentions. This will allow for higher levels of rigor in the decision process.

\- Include a multi-stage approach to allow/force adequate time for accurate factor surfacing, internal variance-disagreement reduction and accurate factor weightings: give time for consideration and reconsideration.

Allowing individuals to cycle through several iterations will allow for consensus in the results.

The iterations allow time for reconsideration. A GDSS may not compress the time, but proper implementation can increase the quality and ultimate acceptance of the results. Decisions are still in the realm of human endeavor.

## References

[1] C. Argyris and D. Schon. Organizational Learning: A Theory in Action Perspective. San Francisco: Jossey-Bass, 1978.

[2] A. Arbel. "A university budget problem: A priority based approach," Socio-Economic Planning Sciences, Volume 17, Number 4, 1983, pp. 181–189.

[3] C.F. Arrington, W. Hillison and R. Jensen. "An application of analytical hierarchy process to model expert judgements on analytical review procedures," Journal of Accounting Research, Volume 22, Number 1, Spring 1984, pp. 298–312.

[4] M.L. Bariff and E.J. Lusk. "Cognitive and personality tests for the design of management information systems," Management Science, Volume 23, Number 8, 1977, pp. 820-829.

[5] I. Bensabat and A.S. Dexter. "Individual differences in the use of decision support aids," The Accounting Review, Volume 20, Number 1, Spring 1982, pp. 1–11.

[6] G. DeSanctis and R.B. Gallupe. "A foundation for the study of group decision support systems," Management Science, Volume 33, Number 5, May 1987, pp. 589–609.

[7] G.W. Dickson and J.K. Simmons. "The behavioral side of MIS," Business Horizons, August 1970, pp. 59–71.

[8] R.H. Doktor and W.F. Hamilton. "Cognitive style and the acceptance of management science recommendations," Management Science, Volume 19, Number 8, April 1973 pp. 884–894.

[9] B.J. Epstein and W.R. King. "An experimental study of the value of information," Omega, Volume 10, Number 3, 1982 pp. 249–258.

[10] T.P. Gerrity, Jr. "The design of man-machine decision systems," Ph.D. dissertation, M.I.T., 1970.

[11] P. Harker. “An analytical hierarchy approach for the determination of interregional migration patterns,” paper presented at the Association of American Geographers annual meeting, Washington D.C., April 22-25, 1984.

[12] D.R. Kingdon. Matrix Organization. New York: Harper and Row, 1973.

[13] P.G.W. Keen and M.S. Scott Morton. Decision support systems: An organizational perspective. Reading, Massachusetts: Addison-Wesley, 1978.

[14] J.L. McKenney and P.G.W. Keen. "How managers' minds work," Harvard Business Review, Volume 52, Number 3, May-June 1974, pp. 79–90.

[15] R.W. Miles and C.C. Snow. “Networked organizations: New concepts for new forms,” The McKinsey Quarterly, Autumn 1986, pp. 53–66.

[16] G. Rabinowitz. “Some aspects of measuring world influence,” Journal of Peace Science, Volume 2, Number 1, Spring 1976, pp. 49–55.

[17] T.L. Satty. “Modeling unstructured decision problems: The theory of analytical hierarchies,” Mathematics and Computers in Simulation, Volume 20, Number 3, 1978, pp. 147–157.

[18] T.L. Satty. The Analytic Hierarchy Process. New York: McGraw-Hill, 1980.

[19] T.L. Satty and J.P. Bennett. "A theory of analytical hierarchies applied to political candidacy," Behavioral Science, Volume 22, Number 4, July 1977, pp. 237–245.

[20] T.L. Satty and M.W. Khouja. "A measure of world influence," Journal of Peace Science, Volume 2, Number 1, Spring 1976, pp. 31–48.

[21] T.L. Satty and P.C. Rogers. “Higher Education in the United States (1985-2000)-Scenario construction using a hierarchical framework with eigenvector weighting.” So

cio-Economic Planning Sciences, Volume 10, Number 6, 1976, pp. 251–263.

[22] P.J.H. Schoemaker and C.C. Waid. "An experimental comparison of different approaches to determining weights in additive utility models," Management Science, Volume 28, Number 2, February 1982, pp. 182–196.

[23] A. Seidmann and A. Arbel. "An analytic approach for planning computerized office systems," Omega, Volume 11, Number 6, 1983 pp. 607–617.

[24] H.A. Simon. "A behavioral model of rational choice," in Models of Man. New York: Wiley, 1957, pp. 241-260.

[25] H.L. Wilensky. Organizational Intelligence. New York: Basic Books, 1967.

[26] W.M. Zani. 1970. "Blueprint for MIS," Harvard Business Review, Vol. 48, No. 6, pp. 95–100.
