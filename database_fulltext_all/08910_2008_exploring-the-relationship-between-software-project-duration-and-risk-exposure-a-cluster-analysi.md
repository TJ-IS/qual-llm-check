---
otero_id: 8910
otero_key: "VUUH7AWS"
title: "Exploring the relationship between software project duration and risk exposure: A cluster analysis"
authors: "Sun-Jen Huang; Wen-Ming Han"
year: "2008"
journal: "Information & Management"
doi: "10.1016/j.im.2008.02.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Exploring the relationship between software project duration and risk exposure: A cluster analysis

Sun-Jen Huang <sup>\*</sup>, Wen-Ming Han

Department of Information Management, National Taiwan University of Science and Technology, 43 Sec. 4, Keelung Road, Taipei, Taiwan Received 5 September 2006; received in revised form 4 October 2007; accepted 5 February 2008 Available online 24 March 2008

## Abstract

Software projects often fail. Thus it is important to find ways to ensure a successful outcome. One significant area is a better understanding of the relationship between the software project duration and risk exposure, as this helps project managers with pertinent information to be effective in managing risky projects. We addressed this need by adopting a cluster analysis technique to provide managers with insight into effective planning and control of their projects. The results not only revealed that risk exposures associated with user, requirement, planning & control and team risk dimensions were affected by project duration, but also showed how to manage software risks effectively through observing trends in the risk components. Based on our findings, project managers can adopt appropriate attitudes, skills, and practices to dea with risky areas more effectively rather than just identifying those software risks with which project managers should be concerned. Published by Elsevier B.V.

Keywords: Software project management; Software risk management; Risk exposure; Project duration; Risk component

## 1. Introduction

Rapid development of new software products to meet customers’ needs is essential today. Despite the fact that many organizations have invested money, time and effort to develop their software, the failure of many software projects is still frequent [8,27].

A software risk (an uncertain event or condition with negative consequences on a software project) can increase the failure rate of a project if it is ignored [9,15]. Thus, the main purpose of software risk management is to identify managerial and technical problems before they occur so that actions can be taken to eliminate or mitigate their impact [11]. Software risk management entails: quantifying the importance of a risk (assessing its probability of occurring and its impact on the project performance) and developing strategies to control it. Thus, understanding the nature of the various software risks and their effect on project success has become increasingly important (e.g., [12]).

Many studies have discussed software risks in two ways: identifying risks and examining the relationship between threats and risks. The former provides a framework as a checklist for project managers (e.g., [1,2,14]), while the latter creates patterns that show how software risks are affected by project characteristics and thus allows managers to develop an appropriate risk management strategy (e.g., [13,20]). We concentrated on the latter in our work.

Knowledge about the effects of project duration on software risk has not been previously investigated in depth. Though software projects have been plagued by schedule slips [6], the effectiveness of a risk management strategy could be improved by understanding the effect of project duration on risky areas. However, most studies have focused either on the types of uncertainties (e.g., [18,19,21,30]) or environmental contingencies [25]. Fewer have discussed the relationship between project duration and risk exposure [33], and they did not provide a systematic way to design a risk management plan based on their findings.

Table 1  
Summary of previously related studies

<table><tr><td></td><td>Boehm (1991)</td><td>Barki et al. (1993)</td><td>Schmidt et al. (2001)</td><td>Wallace et al. (2004)</td></tr><tr><td>Project type</td><td>General</td><td>General</td><td>General</td><td>General</td></tr><tr><td>Scope</td><td>TRW</td><td>Quebec</td><td>Hong Kong, Finland, and the United States</td><td>Across Countries</td></tr><tr><td>Participant</td><td>Project Manager</td><td>Project Leader and User representative</td><td>Project Manager</td><td>PMI member</td></tr><tr><td>Participant numbers</td><td>Unknown</td><td>120</td><td>43</td><td>507</td></tr><tr><td>Research Method</td><td>Unknown</td><td>CFA</td><td>Delphi</td><td>SEM</td></tr><tr><td>Dimensions</td><td>0</td><td>5</td><td>14</td><td>6</td></tr><tr><td>Risks</td><td>10</td><td>23</td><td>53</td><td>27</td></tr></table>

An appropriate skill for managing significant risks can be based on understanding the trends of risk components [10]. Studies have concentrated on the effect of project characteristics on risk exposure, which is not separated by risk components (e.g., [4,24]). Therefore, very little guidance is available on developing a good risk management strategy.

## 2. Related work

Several previous studies have helped in identifying, assessing, and prioritizing software risks. For example, Boehm [5] proposed a software risk management framework that included risk assessment and risk control, and identified a list of the top-ten software risks based on his experience at TRW. However, two problems were identified in several later studies (e.g., [16]). Firstly, the list of top-ten risks was not produced through any formal model-building procedure; thus it lacked a theoretical foundation. Secondly, it reflected the risks of a software development environment in 1991. But since then the complexity, scale and diversity of software have increased and thus, the list has become inadequate unless it is calibrated.

After reviewing IS uncertainty and software risk literature, Barki et al. [3] conducted a survey in Quebec to develop a list which included 23 software risks, classified into five groups using factor analysis. Although the list provided a comprehensible instrument, Wallace et al. [32] pointed out that the assessment scale of each risk was excessively complex. To reduce the bias of a single-culture viewpoint, Schmidt et al. conducted a Delphi survey to integrate the options of experts from Hong Kong, Finland, and the United States. They identified 53 risk items, which were grouped into 14 types, and asserted that cultural difference could affect the list, and that only 11 software risks were applicable from a cross-cultural perspective [26]. Recently, Wallace et al. collected the opinions of 507 members in the Project Management Institute (PMI) and identified 27 software risks, which were classified into six dimensions: User, Requirement, Project Complexity, Planning & Control, Team and Organizational Environment using Structural Equation Model. A summary of related studies on software risks is given in Table 1.

In our study, the six risk dimensions of Wallace’s work were adopted. Firstly, her work was conducted in 2004, and thus it was relatively up-to-date and reflected the consensus of 507 PMI members from various countries. Secondly, SEM was used in her work to examine and prove the composite reliability, convergent validity and adequacy of the proposed framework of software risks. Therefore, the six risk dimensions and their associated software risks, as shown in Table 2, were considered appropriate for our study.

## 3. Data collection and analysis technique

## 3.1. Data collection

To maximize the response rate, a Web-based survey was conducted. We collected data from recently completed software projects in 2005. The survey was made up of three sections. The first introduced the study and encouraged respondents to respond to the survey. The second asked respondents to provide seven project characteristics that described the background of the software project described: process model, project duration, team size, average experience of project members, ratio of staff turnover, number of external suppliers and number of project manager replacements.

The final part listed 27 software risks, and asked the respondents to give in the probability of their occurrence and their impact on the project schedule. Based on Boehm’s original work, the risk exposure was defined here as the probability of occurrence of a risk factor multiplied by the impact on the project schedule. In order to ensure the consistency, the degree of probability of occurrence of software risks and their degree of impact on the project schedule were measured using the 5-scale criteria of the DoD Risk Assessment Method as shown in Table 3 [31]. For example, assuming that the probability of occurrence of a specific software risk was unlikely and would affect a major slip in key milestones, the probability of occurrence of that risk and its impact were rated as 2 and 4, respectively, based on the risk assessment criteria. Hence, the risk exposure of that software risk is equal to 8 (2 - 4).

A pretest was conducted to improve content validity through personal interviews with domain experts after completing the draft of the survey. Based on their feedback, the initial questionnaire was modified to improve its consistency and responder understanding. The questionnaire is shown as Appendix A.

Table 2  
Software risks adopted in this study

<table><tr><td>Risk dimension</td><td>Software risk</td></tr><tr><td>User</td><td>Users resistant to changeConflict between usersUsers with negative attitudes toward the projectUsers not committed to the projectLack of cooperation from users</td></tr><tr><td>Requirement</td><td>Continually changing system requirementsSystem requirements not adequately identifiedUnclear system requirementsIncorrect system requirements</td></tr><tr><td>Project complexity</td><td>Project involved the use of new technologyHigh level of technical complexityImmature technologyProject involves the use of technology that has not been used in prior projects</td></tr><tr><td>Planning and control</td><td>Lack of an effective project management methodologyProject progress not monitored closely enoughInadequate estimation of required resourcesPoor project planningProject milestones not clearly definedInexperienced project managerIneffective communication</td></tr><tr><td>Team</td><td>Inexperienced team membersInadequately trained development team membersTeam members lack specialized skills required by the project</td></tr><tr><td>Organizational environment</td><td>Change in organizational management during the projectCorporate politics with negative effect on the projectUnstable organizational environmentOrganization undergoing restructuring during the project</td></tr></table>

A total of 300 project managers were invited to aid in our investigation, and 135 questionnaires were returned, representing a response rate of 45 percent. However, 20 responses were eliminated due to missing values of risk and 18 were eliminated due to missing values of the estimated duration. Thus a sample of 97 software projects remained, representing a final response rate of 32.3%. Each software project in the sample included the estimated and actual durations and 27 values on the probability of occurrence and the impact on the schedule of all software risks. By comparing the gap between estimated and actual durations, the results showed that 71.1% of the 97 software projects were over schedule, which approximated the statistics of published reports (e.g., [17,23]).

## 3.2. Data analysis technique

In our study, the Two-Step cluster analysis method [29] available in SPSS was chosen for classifying the collected software projects according to project duration because: (1) it provides an auto-clustering mechanism [22]; (2) it is designed to handle large datasets efficiently [34].

The Two-Step cluster analysis method provides ways to automatically test multiple cluster solutions and then choose the best from them. It consists of pre-clustering followed by clustering. At first, all observations are read and processed to decide whether the current observation should be combined with a previous precluster, or whether a new precluster should be created, based on a Log-likelihood distance measure [7]. Then, the preclusters are grouped using an agglomerative clustering algorithm to produce a range of solutions. Since the number of preclusters is normally far less than the total number of observations, this clustering is an efficient way to derive the best solution.

Table 3  
Risk assessment scale and representative meaning

<table><tr><td>Level</td><td>Probability of occurrence</td><td>Level</td><td>Impact on project schedule</td></tr><tr><td>1</td><td>Remote</td><td>1</td><td>Minimal or no impact</td></tr><tr><td>2</td><td>Unlikely</td><td>2</td><td>Additional resources required. Able to meet due date</td></tr><tr><td>3</td><td>Likely</td><td>3</td><td>Minor slip in key milestone. Not able to meet due date</td></tr><tr><td>4</td><td>Highly likely</td><td>4</td><td>Major slip in key milestone or critical path impacted</td></tr><tr><td>5</td><td>Near certainty</td><td>5</td><td>Cannot achieve key team or major program milestone</td></tr></table>

Table 4  
Results of the auto-clustering process

<table><tr><td>Number of clusters</td><td>BIC</td><td> $BIC\ change^a$ </td><td>Ratio of  $BIC\ changes^b$ </td><td>Ratio of distance  $measures^c$ </td></tr><tr><td>1</td><td>75.9</td><td></td><td></td><td></td></tr><tr><td>2</td><td>45.3</td><td>-30.6</td><td>1.0</td><td>2.7</td></tr><tr><td>3</td><td>39.7</td><td>-5.6</td><td>0.2</td><td>2.2</td></tr><tr><td>4</td><td>42.1</td><td>2.4</td><td>-0.1</td><td>3.2</td></tr><tr><td>5</td><td>49.2</td><td>7.1</td><td>-0.2</td><td>1.4</td></tr><tr><td>6</td><td>56.8</td><td>7.6</td><td>-0.2</td><td>2.8</td></tr><tr><td>7</td><td>65.4</td><td>8.6</td><td>-0.3</td><td>1.3</td></tr><tr><td>8</td><td>74.1</td><td>8.7</td><td>-0.3</td><td>1.1</td></tr><tr><td>9</td><td>82.9</td><td>8.8</td><td>-0.3</td><td>2.5</td></tr><tr><td>10</td><td>91.9</td><td>9.0</td><td>-0.3</td><td>1.1</td></tr><tr><td>11</td><td>100.9</td><td>9.0</td><td>-0.3</td><td>2.0</td></tr><tr><td>12</td><td>110.0</td><td>9.1</td><td>-0.3</td><td>1.1</td></tr><tr><td>13</td><td>119.1</td><td>9.1</td><td>-0.3</td><td>1.7</td></tr><tr><td>14</td><td>128.2</td><td>9.1</td><td>-0.3</td><td>1.1</td></tr><tr><td>15</td><td>137.4</td><td>9.1</td><td>-0.3</td><td>1.2</td></tr></table>

<sup>a</sup> Changes are from the previous number of clusters in the table.  
<sup>b</sup> Ratios of changes are relative to the changes of the two cluster solutions.  
<sup>c</sup> Ratios of distance measures are based on the current number of clusters against the previous number of clusters.

The optimal number of clusters is determined by the Bayesian inference criterion (BIC), a model selection criterion proposed by Schwarz [28]. It is calculated using the formula:

$$
\mathrm{BIC} _ {i} = - 2 \ln (L _ {i}) + k _ {i} \ln (n)
$$

where n is the sample size; $k _ { i }$ is the number of parameters in model i; and ln(L ) is the maximized value of the likelihood function for the estimated model i. The results of the autoclustering process, as shown in Table 4; indicated that the solution with two clusters was the best, since it had reasonably large ratios of both BIC changes and distance measures. Cluster 1 represented the group containing 15 long-duration software projects, while cluster 2 represented the other group containing 82 short-duration ones. Table 5 summarizes the profile of all the projects and each cluster of software projects.

## 4. Data analysis and results

## 4.1. The relationship between project duration and risk exposure

The first question was whether: does a relationship exists between risk exposures and project duration? Based on the results of the Two-Step cluster analysis, the means of risk exposure for the six risk dimensions within the long-duration and short-duration projects are shown in Table 6. The greater the mean of risk exposure within the project duration cluster, the greater the importance of that project duration cluster.

The risk exposure of all risk dimensions within the longduration projects was higher than for the short-duration projects, though the differences in some are not obvious (such as the ‘‘project complex’’ risk dimension). To confirm this, a t-test method was performed to verify whether significant differences existed on the exposure of the six risk dimensions between the long-duration and short-duration projects. Interestingly, the results revealed that the risk exposures of the four risk dimensions (user, requirement, planning & control and team), between the long-duration and short-duration projects were significantly different. However the risk exposures of the project complexity and organization environment risk dimensions between the two project duration clusters did not.

Another interesting finding was that the orderings of the six risk dimensions within the long-duration and shortduration projects were inconsistent. To confirm this finding, a Kendall’s W rank test was adopted to verify whether these two orderings were significantly different. The result $( p = 0 . 1 0 3 )$ showed that there was no significant association among the six risk dimensions between the long- and shortduration projects. This indicated that the importance of a specific risk dimension was affected by the project duration and hence, was a crucial consideration for project managers when deciding on the suitable risk management strategy.

A more detailed analysis on the nature of risk exposure in the six risk dimensions was required to develop a better risk management strategy. Hence, the patterns between the project duration and each of the two risk components were explored in more detail.

## 4.2. The relationship between project duration and risk component

The effects of project duration on risk components, which included the probability of occurrence and the impact on the

Table 6  
Profiles of each cluster of software projects

<table><tr><td>Project characteristics</td><td>Total (n = 97)</td><td>Cluster1 (n = 15)</td><td>Cluster2 (n = 82)</td></tr><tr><td colspan="4">Process model</td></tr><tr><td>Waterfall</td><td>47</td><td>10</td><td>37</td></tr><tr><td>Incremental</td><td>25</td><td>3</td><td>22</td></tr><tr><td>Evolutionary</td><td>19</td><td>1</td><td>18</td></tr><tr><td>Other</td><td>6</td><td>1</td><td>5</td></tr><tr><td colspan="4">Project duration (months)</td></tr><tr><td>&lt;6</td><td>31</td><td>0</td><td>31</td></tr><tr><td>7–12</td><td>37</td><td>0</td><td>37</td></tr><tr><td>13–18</td><td>14</td><td>0</td><td>14</td></tr><tr><td>19–24</td><td>8</td><td>8</td><td>0</td></tr><tr><td>&gt;25</td><td>7</td><td>7</td><td>0</td></tr><tr><td colspan="4">Team size</td></tr><tr><td>&lt;10</td><td>67</td><td>6</td><td>61</td></tr><tr><td>11–20</td><td>13</td><td>2</td><td>11</td></tr><tr><td>21–40</td><td>12</td><td>5</td><td>7</td></tr><tr><td>41–60</td><td>3</td><td>1</td><td>2</td></tr><tr><td>&gt;60</td><td>2</td><td>1</td><td>1</td></tr><tr><td colspan="4">Average experience of project members (years)</td></tr><tr><td>&lt;1</td><td>3</td><td>0</td><td>3</td></tr><tr><td>1–3</td><td>48</td><td>8</td><td>40</td></tr><tr><td>4–6</td><td>39</td><td>5</td><td>34</td></tr><tr><td>7–9</td><td>6</td><td>1</td><td>5</td></tr><tr><td>&gt;9</td><td>1</td><td>1</td><td>0</td></tr><tr><td colspan="4">Ratio of staff turnover (percentages)</td></tr><tr><td>0</td><td>39</td><td>2</td><td>37</td></tr><tr><td>1–10</td><td>21</td><td>2</td><td>19</td></tr><tr><td>11–20</td><td>24</td><td>7</td><td>17</td></tr><tr><td>21–30</td><td>4</td><td>2</td><td>2</td></tr><tr><td>&gt;30</td><td>9</td><td>2</td><td>7</td></tr><tr><td colspan="4">Number of external suppliers</td></tr><tr><td>0</td><td>42</td><td>5</td><td>37</td></tr><tr><td>1</td><td>26</td><td>2</td><td>24</td></tr><tr><td>2</td><td>10</td><td>4</td><td>6</td></tr><tr><td>3</td><td>9</td><td>0</td><td>9</td></tr><tr><td>&gt;4</td><td>10</td><td>4</td><td>6</td></tr><tr><td colspan="4">Number of project manager replacements</td></tr><tr><td>0</td><td>79</td><td>7</td><td>70</td></tr><tr><td>1</td><td>6</td><td>3</td><td>3</td></tr><tr><td>2</td><td>5</td><td>2</td><td>3</td></tr><tr><td>3</td><td>6</td><td>2</td><td>4</td></tr><tr><td>&gt;4</td><td>1</td><td>1</td><td>0</td></tr></table>

project schedule, were investigated. Two radar charts were used to examine this. Figs. 1 and 2 show the variation of the probability of occurrence and the impact on the project schedule, respectively, on the six risk dimensions within the long-duration and short-duration projects. Fig. 1 shows that the probability of occurrence in all risk dimensions within the long-duration projects is higher than those within the short-duration projects Moreover, Fig. 2 showed the same observations. Hence, a t-test was conducted to examine whether the six risk dimensions between the long-duration and short-duration projects were different in terms of both risk components. Table 7 shows that no significant difference existed on the probability of occurrence in the requirement, project complexity, and organization environment risk dimensions between the long- and short-duration projects. For the risk component of the impact on the project schedule, the project complexity, team and organization environment risk dimensions did not show any significant difference between the long- and short-duration projects.

![](/api/attachments/VUUH7AWS/fulltext/images/2569913b33c15708e56e4d4ad4b90fa4239ae6f3f5d7a0f6d7c992e3b24d8524.jpg)  
Fig. 1. Radar chart for the probability of occurrence.

Further analysis of the data showed that both the probability of occurrence and the impact on the project schedule of the two risk dimensions was found to be significantly affected by the project duration $( p < 0 . 0 5 )$ These were the user and planning & control risk dimensions. This result not only indicated that the long-duration projects had higher frequencies on these two risk dimensions compared to the short-duration projects, but it also implied that project managers who underestimated the factor of project duration may have easily ignored these two risk dimensions. On the other hand, there was no positive pattern on both the probability of occurrence and the impact on the project schedule of the project complexity and organization environment risk dimensions between the long- and shortduration projects $( p > 0 . 0 5 )$ . This indicated that both risk components of these two risk dimensions were not affected by the project duration.

Risk exposures within long-duration and short-duration projects

<table><tr><td>Risk dimension</td><td>Number of risks</td><td>Long-duration project</td><td>Short-duration project</td><td>Sig.</td></tr><tr><td>User</td><td>5</td><td>7.73</td><td>5.31</td><td>0.00</td></tr><tr><td>Requirement</td><td>4</td><td>11.25</td><td>8.08</td><td>0.03</td></tr><tr><td>Project complexity</td><td>4</td><td>6.97</td><td>5.80</td><td>0.33</td></tr><tr><td>Planning and control</td><td>7</td><td>10.31</td><td>5.94</td><td>0.00</td></tr><tr><td>Team</td><td>3</td><td>9.07</td><td>5.69</td><td>0.00</td></tr><tr><td>Organization environment</td><td>4</td><td>6.64</td><td>5.22</td><td>0.23</td></tr></table>

Table 8  
Table 7  
Differences of risk components within long-duration and short-duration software projects

<table><tr><td rowspan="2">Risk dimension</td><td colspan="3">Probability of occurrence</td><td colspan="3">Impact on project schedule</td></tr><tr><td>Long-duration project</td><td>Short-duration project</td><td>Sig.</td><td>Long-duration project</td><td>Short-duration project</td><td>Sig.</td></tr><tr><td>User</td><td>2.63</td><td>2.19</td><td>0.01</td><td>2.87</td><td>2.30</td><td>0.01</td></tr><tr><td>Requirement</td><td>3.05</td><td>2.64</td><td>0.12</td><td>3.45</td><td>2.81</td><td>0.03</td></tr><tr><td>Project complexity</td><td>2.58</td><td>2.29</td><td>0.25</td><td>2.52</td><td>2.27</td><td>0.34</td></tr><tr><td>Planning and control</td><td>2.92</td><td>2.20</td><td>0.00</td><td>3.30</td><td>2.48</td><td>0.01</td></tr><tr><td>Team</td><td>2.89</td><td>2.23</td><td>0.01</td><td>2.84</td><td>2.33</td><td>0.07</td></tr><tr><td>Organization environment</td><td>2.18</td><td>2.01</td><td>0.47</td><td>2.68</td><td>2.38</td><td>0.31</td></tr></table>

Summarization of risk components and exposure of six risk dimensions affected by project duration

<table><tr><td rowspan="2">Risk dimensions</td><td colspan="2">Risk components</td><td rowspan="2">Risk exposure</td></tr><tr><td>Probability of occurrence</td><td>Impact on schedule</td></tr><tr><td>User</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Requirement</td><td></td><td>X</td><td>X</td></tr><tr><td>Project complexity</td><td></td><td></td><td></td></tr><tr><td>Planning and control</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Team</td><td>X</td><td></td><td>X</td></tr><tr><td>Organization environment</td><td></td><td></td><td></td></tr></table>

For the risk component of the impact on the project schedule, the requirement risk dimension was significantly different between the long- and short-duration projects $( p = 0 . 0 3 )$ , but the significance did not exist from the viewpoint of the probability of occurrence $( p = 0 . 1 2 )$ . This indicated that the requirement risk dimension frequently occurred regardless of the scale of the project duration, but its distractive impact on the project schedule within the longduration projects was higher than those within the short duration projects. In contrast to this, the team risk dimension was the reverse. It frequently occurred within the longduration projects as opposed to the short-duration projects $( p = 0 . 0 1 )$ , but its distractive impact on the project schedule was not significantly affected by the project duration $( p = 0 . 0 7 )$ . Thus, to maximize the synergy effect on the limited project/organization resources, an appropriate risk management strategy must undertake the actions to eliminate the frequent risks or to mitigate the high consequences to which risks will lead.

![](/api/attachments/VUUH7AWS/fulltext/images/922267e4b03901580ffc886eabfbd363243ec16890dea28ec2172772d6f57365.jpg)  
Fig. 2. Radar chart for the impact on the project schedule.

## 4.3. A comparison of significant results

The t-test results were summarized in Table 8 which revealed the relationship between the risk exposure and the software project duration. The marks there indicate the existence of the observed significant difference.

Interestingly, although the project duration has significant effect on the user, requirement, planning & control and team risk dimensions in terms of risk exposure, their correlations were different. Project managers can define strategic objectives of risk management and examine the various possible alternative plans to meet their objectives. They will know not only which risk components or exposures in a particular risk dimension will be affected by the project duration, but also how to avoid or mitigate each significant risk by analyzing the trend in the probability of occurrence and the impact on the project schedule.

## 5. Conclusion

The greater the understanding of software risk, the better the risk management planning activity and project outcome. The purpose of our study was to examine the effects of project duration on risk exposure. In particular, we extended the relationship to risk components in order to assist project managers design suitable risk management activities in the early stages. Since the effect of project duration on risk exposure and risk component will be well understood before the implementation, an active risk management plan could then be developed.

The findings in this study indicated that risk exposures associated with the user, requirement, planning & control and team risk dimensions were affected by project duration, although the tacit knowledge was different. It not only indicated that these four risk areas had to be controlled well, but it also showed that a project manager must learn to adopt to the different attitudes, skills, and practices that will be used to address them. If these four risk areas are well managed, the failure ratio of long-duration software projects could be reduced. On the other hand, risk exposures of the project complexity and organization environment risk dimensions were not significantly affected by the project duration because their probability of occurrence and their impact on the project schedule were not significantly different between the long- and short-duration projects. Such knowledge could help the project managers decide how to mitigate or eliminate significant risks which would lead to higher success rates.

## Acknowledgements

This research was supported by the National Science Council (NSC) of Taiwan under the contract 96-2416-H-011-009. The authors also wish to thank anonymous reviewers for their constructive comments and the chief editor Prof. Edgar H Sibley for his editorial effort on the manuscript of this paper.

## Appendix A. Selected parts of the questionnaire

To what degree do you believe the probability of occurrence and the impact on the project schedule is affected by the Organizational Environment risks in your most recently completed software project? Please circle the response that best represents your judgment on the following scales based on the DoD Risk Management Assessment Method which is provided in the attached sheet.

<table><tr><td colspan="8">Project involved the use of new technology</td></tr><tr><td>Probability of occurrence</td><td>Remote</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>Near certainty</td></tr><tr><td>Schedule</td><td>Minimal or no impact</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>Cannot achieve key team or major program milestone</td></tr><tr><td colspan="8">Corporate politics with negative effect on project</td></tr><tr><td>Probability of occurrence</td><td>Remote</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>Near certainty</td></tr><tr><td>Schedule</td><td>Minimal or no impact</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>Cannot achieve key team or major program milestone</td></tr><tr><td colspan="8">Unstable organizational environment</td></tr><tr><td>Probability of occurrence</td><td>Remote</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>Near certainty</td></tr><tr><td>Schedule</td><td>Minimal or no impact</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>Cannot achieve key team or major program milestone</td></tr><tr><td colspan="8">Organization undergoing restructuring during the project</td></tr><tr><td>Probability of occurrence</td><td>Remote</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>Near certainty</td></tr><tr><td>Schedule</td><td>Minimal or no impact</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>Cannot achieve key team or major program milestone</td></tr></table>

## References

[1] T. Addison, E-commerce project development risks: Evidence from a Delphi survey, International Journal of Information Management 23 (1), 2003, pp. 25–40.

[2] D. Aloini, et al., Risk management in ERP project introduction: review of the literature, Information & Management 44 (6), 2007, pp. 547–567.

[3] H. Barki, S. Rivard, J. Talbot, Toward an assessment of software development risk, Journal of Management Information Systems 10 (2), 1993, pp. 203–225.

[4] H. Barki, S. Rivard, T. Talbot, An Integrative Contingency Model of Software Project Risk Management, Journal of Management Information Systems 17 (4), 1998, pp. 37–69.

[5] B.W. Boehm, Software risk management: Principles and practices, IEEE Software 8 (1), 1991, pp. 32–41.

[6] R. Charette, Why software fails, IEEE Spectrum 42 (9), 2005, pp. 42– 49.

[7] T. Chiu, et al., A Robust and Scalable Clustering Algorithm for Mixed Type Attributes in Large Database Environment, in: Proceedings of the 7th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2001, pp. 263–268.

[8] S. Chris, C. Christine, The State of IT Project Management in the UK 2002–2003, University of Oxford, Templeton College, 2003 .

[9] T. DeMarco, T. Lister, Waltzing With Bears: Managing Risk on Software Projects, Dorset House Publishing Company, 2003.

[10] W.M. Han, S.J. Huang, An empirical analysis of risk components and performance on software projects, Journal of Systems and Software 80 (1), 2007, pp. 42–50.

[11] F. Heemstra, J. Kusters, Dealing with risk: a practical approach, Journal of Information Technology 11 (4), 1996, pp. 333–346.

[12] J.J. Jiang, G. Klein, Risks to different aspects of system success, Information & Management 36 (5), 1999, pp. 263–272.

[13] J.J. Jiang, G. Klein, Software development risks to project effectiveness, The Journal of Systems and Software 52 (1), 2000, pp. 3–10.

[14] M. Keil, et al., A framework for identifying software project risks, Communications of the ACM 41 (11), 1998, pp. 76–83.

[15] R.L. Kumar, Managing risks in IT projects: an options perspective, Information & Management 40 (1), 2002, pp. 63–74.

[16] K. Lyytinen, L. Mathiassen, J. Ropponen, Attention shaping and software risk—A categorical analysis of four classical risk management approaches, Information Systems Research 9 (3), 1998, pp. 233– 255.

[17] KPMG, Runaway projects—cause and effect, Software World 26 (3), 1995, pp. 3–5.

[18] K.S. Na, et al., Software development risk and project performance measurement: evidence in Korea, Journal of Systems and Software 80 (4), 2007, pp. 596–605.

[19] S.R. Nidumolu, The effect of coordination and uncertainty on software project performance, Information System Research 6 (3), 1995, pp. 191–219.

[20] S.R. Nidumolu, Standardization, requirements uncertainty and software project performance, Information & Management 31 (3), 1996, pp. 135–150.

[21] S.R. Nidumolu, A comparison of the structural contingency and riskbased perspectives on coordination in software development projects, Journal of Management Information Systems 13 (2), 1996, pp. 77– 113.

[22] M.J. Norusis, SPSS 12.0 Statistical Procedures Companion, Prentice-Hall, Upper Saddle River, NJ, 2003.

[23] D. Phan, D. Vogel, J. Nunamaker, The search for perfect project management, Computer world 22, 1998, pp. 95–100.

[24] J. Ropponen, K. Lyytinen, Components of Software Development Risk: How to Address Them? A Project Manager Survey IEEE Transactions on software engineering 26 (2), 2000, pp. 98– 112.

[25] J. Ropponen, K. Lyytinen, Can software risk management improve system development: an exploratory study, European Journal of Information Systems 6 (1), 1997, pp. 41–50.

[26] R. Schmidt, et al., Identifying software project risks: an international Delphi study, Journal of Management Information Systems 17 (4), 2001, pp. 5–36.

[27] Standish Group. Chaos Chronicles Version 3.0, 2003, West Yarmouth.

[28] G. Schwartz, Estimating the dimension of a model, Annals of Statistics 6 (2), 1978, pp. 497–511.

[29] SPSS Inc. The SPSS two-step cluster component: A scalable component to segment your customers more effectively. White paper–technical report, Chicago, 2001, pp. 1–9.

[30] A. Tiwana, M. Keil, Functionality risk in information systems development: an empirical investigation, IEEE Transactions on Engineering Management 53 (3), 2006, pp. 412–425.

[31] US Department of Defense, Risk Management Guide for DOD Acquisition, fifth edition, Defense Acquisition University, Defense Systems Management College, 2003 pp. 1–188.

[32] L. Wallace, M. Keil, A. Rai, How software project risk affects project performance: an investigation of the dimensions of risk and an exploratory model, Decision Sciences 35 (2), 2004, pp. 289–321.

[33] L. Wallace, M. Keil, A. Rai, Understanding software project risk: a cluster analysis, Information & Management 42 (1), 2004, pp. 115– 125.

[34] T. Zhang, et al., BIRCH: an efficient data clustering method for very large databases, in: Proceedings of the ACM SIGMOD Conference on Management of Data, 1996, pp. 103–114.

![](/api/attachments/VUUH7AWS/fulltext/images/6a699cbfe6c878ea6e5b89ed0906226ae5f04d99e15df602bc4722d186c8a973.jpg)

Sun-Jen Huang received his BA in Industrial Management in 1988, and his MS in engineering and technology in 1991, both from the National Taiwan University of Science and Technology, Taiwan, and his PhD degree from the School of Computer Science and Computer Engineering, La Trobe University, Melbourne, Australia, in 1999. He is currently an associate professor in the Department of Information Management, National Taiwan University of Science and Tech

nology, Taipei, Taiwan. He is also the head of the Software Engineering and Management Laboratory at NTUST, which hosts research projects every year from National Science Council and software industry in Taiwan. Dr. Huang is also a chairman of Software Quality Promotion Committee at the Chinese Society for Quality. His research interests include software engineering and project management, software process improvement, software measurement and analysis, and software quality management. Dr. Huang has published more than 20 papers in journals including Information & Management, IEEE Transactions on Software Engineering, Software Practice & Experience, Journal of Systems and Software, Informal and Software Technology, European Journal of Operational Research, Applied Intelligence, and Journal of Software Engineering Studies.

![](/api/attachments/VUUH7AWS/fulltext/images/e48d3110de6ab81392df8fc1f727b4e29ac49c7b1af1184ba33637ec4f0c38ce.jpg)

Wen-Ming Han is currently a doctoral candidate in the Department of Information Management at National Taiwan University of Science and Technology (NTUST), and is also a member of the Software Engineering and Management Laboratory at NTUST, Taiwan. He received his Bachelor degree in Information Management from St. John’s & St. Mary’s Institute of Technology in 2001, and Master degree in Information Management from NTUST in 2003, Taiwan. His current

research interests include software risk management, software proces improvement, functional size measurement and value-based engineering.
