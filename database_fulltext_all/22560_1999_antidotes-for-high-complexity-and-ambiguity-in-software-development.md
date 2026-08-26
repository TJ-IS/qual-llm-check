---
otero_id: 22560
otero_key: "6F6S8MBW"
title: "Antidotes for high complexity and ambiguity in software development"
authors: "Stephanie Watts Sussman; P.J Guinan"
year: "1999"
journal: "Information & Management"
doi: "10.1016/s0378-7206(99)00005-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Antidotes for high complexity and ambiguity in software development $^{1}$

Stephanie Watts Sussman $^{a,*}$ , P.J. Guinan $^{2,b}$

$^{a}$ Weatherhead School of Management – MIDS, Case Western Reserve University, 10900 Euclid Ave., Cleveland, OH 44106-7235, USA $^{b}$ Babson College – Information Systems, Babson Park, Wellesley, MA 02157-0310, USA

Received 18 February 1998; accepted 8 November 1998

## Abstract

In a longitudinal study of 47 software development teams, we investigate interactions between team and technology factors and the degree of complexity and ambiguity of the projects themselves. From the literature, we propose a theoretical model that identifies a characteristic of the technology (modularity) and a characteristic of the team process (conflict resolution) used during system development, as effective for minimizing the adverse effects of high task-based complexity and ambiguity (those tasks for which multiple acceptable solutions exist). We hypothesize that modularity and conflict-resolution techniques will account for a significant amount of the variance in user satisfaction for highly complex and ambiguous projects, but that this will not be the case for simple and unambiguous projects. Our findings confirm this hypothesis, indicating that effective conflict resolution and modularity are associated with significantly higher client satisfaction six months after implementation for all projects. An explanation for these findings is offered, followed by implications for theorists and practitioners. © 1999 Elsevier Science B.V. All rights reserved.

Keywords: Complexity; Ambiguity; Conflict resolution; Modularity; Task–technology fit; Software development; Teams; Survey research; Moderation analysis

## 1. Introduction

The team tasks of software design and development are intrinsically complex and often exacerbated by incomplete user requirements, changing environmental demands, and high levels of interdependence within teams [12]. Many large-scale software development projects do not function as intended or fulfil their potential [11, 12]. Clearly, research into improving the software development process is still warranted [15].

Managing development teams is a non-routine task characterized by high levels of complexity $[30]$ , especially when these teams are medium or large. Task complexity or uncertainty has been studied for its effects on various types of systems, such as expert systems $[55]$ , decision-support systems $[23, 45]$ , end-user computing $[9]$ , and project management in general $[35]$ . What can be done to mitigate the negative impact of high task complexity on the software development process? The structural contingency perspective of organizational design [48, 52] prescribes an appropriate fit between organizational structure and environmental uncertainty for reducing task complexity and uncertainty. According to the information processing perspective, more routine, less complex environments process information most efficiently with hierarchical control structures [20], while complex and uncertain environments benefit from organismic organizational forms [7] and rich information channels [13].

In addition to high complexity, theorists also identify ambiguous or equivocal task environments as a threat to effective information processing. Such task environments are those in which no single correct outcome is inherently correct, and potentially acceptable multiple solutions exist $[14]$ . The creation of shared systems of symbols can help reduce task ambiguity $[53]$ , and provide a horizontal coordination mechanism $[35]$ by forcing stakeholders to undertake an explicit process of convergence on diverse desired outcomes.

From an information processing perspective, the impact of task complexity has been widely documented $[18, 54]$ , but less research has been conducted on the role of task ambiguity in the context of software development. Nor has there been any recent empirical work relating to influences of task complexity and task ambiguity on software development teams.

Although theoretical prescriptions for mitigating the adverse effects of task complexity and ambiguity are helpful, they are very general in nature, and do little to guide practitioners in selecting particular technologies and processes for software development from the myriad of options available. It is important to investigate which specific technologies and processes are most effective under conditions of high complexity and ambiguity, since it is under these conditions that traditional methods of coordination and control are least effective $[20]$ . Successful identification of such factors contributes to our theoretical understanding of these two organizational problems at a higher level of granularity than has been achieved thus far, and can benefit practitioners faced with real task uncertainty and ambiguity.

Section 2 presents past research on task-based complexity and ambiguity and develops hypotheses around specific team and technology characteristics identified as having the capacity to absorb the negative effects of complexity and ambiguity. Section 3 describes the method used to analyze these hypotheses, based on a survey of 47 medium-sized software development teams. The resultant findings and discussion are presented in Section 4. Conclusions and implications of these results are discussed in Section 5.

## 2. Background

Organization design research posits that organizational forms can be fitted to characteristics of tasks in order to optimize organizations' ability to deal with external forces [21, 49]. Team problem-solving processes are clearly affected by the type of task involved [32, 8]. These task characteristics are distinct from the technologies employed to transform inputs into outputs, most frequently described on a continuum of routine/non-routine [40].

Two major forces external to organizational subunits influence the ability of their members to process information: uncertainty and equivocality $[13]$ . Uncertainty is defined as the absence of information $[2]$ , and is reduced by new task-related information $[50]$ . Ambiguous task environments are those where multiple and conflicting interpretations of existing information occur, such that they are resolved through enactment of shared interpretations of the task at hand $[53]$ .

## 2.1. Task complexity

Work-related uncertainty can be viewed as an objective characteristic of the task $[8]$ that imposes behavioral requirements on individuals facing it. Task complexity is one widely accepted source of work-unit uncertainty $[50]$ . Task uncertainty has been associated with lower levels of software project performance and higher levels of software performance risk $[35]$ .

Perceived complexity is widely acknowledged to be an important factor affecting the software development process $[42]$ . Software development project teams are often faced with high levels of complexity, since it is not unusual to build a system which has multiple interfacing components and is measured in millions of lines of code $[6]$ . Theory states that task complexity can be reduced by the acquisition and use of additional new information $[2]$ , thus organizational forms and processes that promote maximum information processing capacity should be most beneficial in highly complex tasks [20], such as software development.

## 2.2. Task ambiguity

Unlike task complexity, task ambiguity refers to those tasks for which multiple acceptable solutions exist, as perceived by those with different frames of reference $[2]$ . Task information that is clear and directed leads to similar interpretations, while task information that is ambiguous leads to multiple interpretations which must be resolved in order to develop a shared understanding of how to perform the task. At the team level, the team leader must work to integrate the separate perceptions, frames and knowledge bases of team members $[51]$ , who are often working on different development tasks, especially in the case of large projects $[56]$ . A system development project in which different stakeholders have divergent goals and views of the final system presents an ambiguous task to its developers $[5]$ . Typical ambiguous systems are those spanning different functional areas, such that managers from the different functions have particular and divergent needs for the system. Such conflicts create task ambiguity when they are not identified and resolved.

Organizational forms which promote the exchange of rich information have been prescribed as most effective for reducing task ambiguity, since this type of information increases the capacity of the information exchanged to move individual perceptions toward a shared perception [13]. Alternatively, we can view the problem from the perspective of social cognition: Externalized knowledge is less ambiguous than tacit knowledge, since it is explicit and codified. Externalization of tacit knowledge held by team members occurs through social processes which make use of metaphors, analogies and models [36], and by the use of explicit models of the system-to-be. Cognitive maps, prototypes and scripts are used to represent individuals' tacit cognitions [26] by cognitive scientists. In the same way, technologies which enable physical depiction of the future computer system – such as application module management systems – enable the articulation of shared team perceptions of the system-to-be; articulations that then become manifestations of shared, externalized knowledge. The process of building these models reduces task ambiguity by requiring that the divergent perspectives of the various individuals involved become enmeshed as their tacit knowledge becomes public and represented. Thus, rather than information richness, we look to another prescription for the reduction of task ambiguity – the creation of systems of symbols which embody shared perceptions of an unambiguous task outcome.

The concept of task-technology fit is widely applied to system utilization theory [22] at the individual level. We build a related contingency model at the group level to hypothesize an appropriate fit between these two characteristics of the task, complexity and ambiguity, and a group process factor - team conflict resolution - and a technology factor - modularity - during the software development process, as described below.

## 2.3. Team conflict resolution

A substantial body of research has investigated the impact of conflict resolution across team boundaries, especially in interaction with users participating in development $[43]$ . This research has focused primarily on medium-sized teams consisting of 8–15 members. Less work has been done in the area of within-team conflict resolution. Team-member conflict-resolution behaviors during system development have been directly associated with project success $[44]$ . For this reason, and as a consequence of the theoretical argument presented below, we have selected conflict resolution as the key group-process variable to include in our model.

Although many definitions of conflict exist, it is generally agreed that conflict occurs around incompatible goals or interests among members $[5]$ . Since goal interference represses information processing capacity, conflict resolution can enhance information processing capacity by facilitating goal congruence. Networked communication environments enable the “adjustment and continual re-definition of individual tasks through interaction with others” $[7]$ that is necessary for high levels of information processing. As a mechanism for encouraging differentiation and integration of diverse views of the various team members, horizontal coordination requires that team members resolve conflicts effectively through generation of agreement and consensus [43]. Conflict resolution is one highly effective coordination mechanism that can increase communication within the team and so mitigate the adverse effects of complexity by increasing the quantity of information available to the team [52, 56].

In these ways, conflict-resolution behaviors can increase the information processing capacity of a team $[47]$ . Since teams facing high levels of task complexity need to process greater quantities of information than those facing lower levels of task complexity, teams with effective conflict resolution behaviors should be able to handle high levels of task complexity $[50]$ more successfully than those without effective conflict resolution behaviors. And since conflict resolution capabilities are also mechanisms that teams can use to generate shared perceptions of the desired outcome, conflict resolution skills can be helpful for resolving the inconsistent views of ambiguous projects. Thus, conflict resolution may mitigate the impacts of both task complexity and ambiguity. $^{3}$

## 2.4. Modularity

Where organizations reach the limits of their capacity to manage complexity, information technologies can be used to reduce and manage this complexity $[28]$ . Technologies include the programs and routines generated from tool use, as well as the actual physical tools. Systems development methodologies and the production of necessary artifacts require that the development team articulate its shared perceptions of the system-to-be. We have argued above that ambiguity can be reduced through the creation and use of shared systems of symbols $[53]$ , so technologies that require the team to make explicit its tacit perceptions of the system through generation of modules or other physical artifacts should be most effective for complex and ambiguous processes.

Explicit shared perceptions of the system under development include the whole system, its parts, and the relationships of these parts to the whole [51]. Under the guise of reuse, many systems are developed in parts or modules, a system characteristic we refer to here as ‘Modularity’. When teams design modules, they are sharing their views of the system parts. Therefore, we consider the extent to which modularization technology is utilized during system development to be a measure of the degree to which a team makes its tacit knowledge explicit – through module creation and selection. The benefits of modularity are well documented in the literature [37, 19, 39], especially in the context of objected-oriented technologies [38, 16] but not fully theoretically grounded [1, 4]; we offer a theoretical explanation for these benefits: The process of deciding and resolving multiple views about which modules to build and to include in the final system externalizes individuals’ tacit knowledge so that a group knowledge convergence can occur and be made explicit. In this view, the greater the degree of modularity used by the team, the greater the likelihood that task ambiguity will be reduced in the process. In addition, by committing to include certain modules and not others in the final system, modularity also mitigates task ambiguity by reducing the number of future possible options available to the team. And by making explicit the relationship of parts to the whole, modularity generates additional information which may be helpful in reducing task-based uncertainty.

## 2.5. Information system success

Client satisfaction or client information satisfaction is the most widely used single measure of IS success $[17]$ . As DeLone and McLean state: “It is hard to deny the success of a system which its users say that they like.” The clients’ perceptions of the value, appropriateness, and timeliness of the information that the system produces is an extremely important determinant of overall system success $[27]$ , and is used in this study to measure system success six months after installation.

## 2.6. Model development

Fig. 1 illustrates a model derived from the literature, reflecting the relationships between the two task factors, the two process factors, and the dependent measure of user information satisfaction.

![](/api/attachments/6F6S8MBW/fulltext/images/8c153868b0b4711f2a445f059df6044b655dcd8cbce5cc1b5f124329e74f04c3.jpg)  
Fig. 1. The model: moderation of complexity and ambiguity factors.

From this model we hypothesize that modularity and conflict resolution moderate the negative impacts of complexity and ambiguity on user information satisfaction:

Hypothesis 1: Taken together, effective conflict resolution and high levels of modularity will result in high user information satisfaction (six months after project implementation) in highly complex projects, but not in less complex projects.

Hypothesis 2: Taken together, effective conflict resolution and high levels of modularity will result in high user information satisfaction (six months after project implementation) in highly ambiguous projects, but not in less ambiguous projects.

By investigating both process factors together, we can compare the extent to which they moderate the task variables, to see if one is more salient than the other under the different task conditions. Since we have no theoretical basis on which to judge the relative impacts of the moderating variables under the two task conditions, this aspect of the analysis is data driven and, thus, exploratory.

## 3. Research method

This study investigated 47 software development teams from 15 organizations. The research design is based on a cross-sectional field study. These teams consisted of eight-to-fifteen members each, so can be considered ‘medium-sized’. The unit of analysis is the IS design team.

For each software development project, two sets of questionnaires were distributed. The first questionnaire was distributed to team members and completed during the design and code phase of software development. It contained items on the degree of conflict resolution and modularity, as well as perceived task complexity and ambiguity. The second questionnaire was distributed to actual users of the developed systems, six months after implementation.

In the first questionnaire, data on the independent and moderating variables were collected directly from members of each team. Wherever possible, all team members were surveyed. When it was not possible to reach all team members, teams provided a representative sample of key informants from the team. Using key informant techniques for data collection has been found to be effective for survey research in organizations $[41]$ . In the second questionnaire, a minimum of two users per project were asked the dependent measure – to what extent the information provided them by the system meets their precise information needs. By surveying both team members and users six months apart, we prevent self-report and recall bias in the dependent measure.

Only projects estimated to have twelve-to-fifteen-month development schedules were selected, from organizations representing a range of industries: insurance, financial services, high technology, heavy industry, transportation, and petroleum. Table 1 presents demographic information.

## 3.1. Measures and procedures

Excerpts from standard indicators were used to measure the constructs of this study. All indicators and constructs are in the form of seven-point Likert-type scales, and are listed in Appendix A. Question order was randomized and items were reverse-scored in the actual instrument to reduce response order effects. Client information-satisfaction items were taken from Ives et al. [27]. Indicators for conflict resolution were drawn from Hackman [24], while those for modularity were taken from Henderson and Cooprider [25]. Task ambiguity was operationalized using Daft and Macintosh's [14] measure of work-unit information equivocality. Task complexity items were drawn from Van de Ven, Delbecq and Koenig [52].

Table 1  
Description of study sample

<table><tr><td>Industry</td><td># Cos</td><td># Teams</td><td># Respondents</td></tr><tr><td>Insurance</td><td>4</td><td>11</td><td>41</td></tr><tr><td>Transportation</td><td>2</td><td>12</td><td>79</td></tr><tr><td>High technology</td><td>1</td><td>7</td><td>64</td></tr><tr><td>Financial services</td><td>4</td><td>11</td><td>58</td></tr><tr><td>Petroleum</td><td>2</td><td>3</td><td>18</td></tr><tr><td>Heavy industry</td><td>1</td><td>3</td><td>31</td></tr><tr><td>Total</td><td>15</td><td>47</td><td>291</td></tr></table>

## 4. Results and discussion

The unit of analysis is the team, so values for each construct reported represent the average value of that construct for the team. Table 2 presents descriptive statistics, and the Cronbach $\alpha$ s indicate acceptable levels of reliability for all constructs.

Univariate analyses confirm acceptable levels of skewness and kurtosis for all variables. Pearson correlation matrices indicate no significant correlations between independent constructs (see Table 3), except between ambiguity and complexity. Thus, the two hypothesized moderators are not entirely independent or strictly orthogonal. However, their correlation of

0.34 is of medium magnitude and within acceptable parameters for a weak form test of orthogonality. And based on the sample size, analysis of the effects of the two moderators is performed independently, so this correlation does not impact it. To investigate convergent validity, confirmatory factor analysis with varimax rotation and Kaiser normalization was used. All items loaded onto their respective constructs with no overlap (see Table 4).

In order to assess both, the form and the strength of the hypothesized moderators, it is necessary to employ two types of analysis – moderated regression analysis performed on the full sample, and the split-sample analysis of subgroups divided by the moderator [46]. These two types of analyses are presented in the following.

## 4.1. Moderated regression analysis

Moderated regression analysis (MRA) avoids the loss of information resulting from the artificial transformation of a continuous variable into a qualitative one. It enables the identification of all types of moderators, except homologizers which operate through the error term to affect the strength rather than the form of the predictor-criterion relationship. Subgroup analysis in Section 4.2 will be used to determine if the hypothesized task moderators are homologizers.

Table 2  
Descriptive statistics

<table><tr><td>Factor</td><td>Mean/median</td><td>S.D.</td><td>No. indicators</td><td>α</td></tr><tr><td>Ambiguity</td><td>3.96/4.08</td><td>0.79</td><td>3</td><td>(0.8117)</td></tr><tr><td>Complexity</td><td>4.97/5.00</td><td>0.85</td><td>2</td><td>(0.8398)</td></tr><tr><td>System success</td><td>5.17/5.67</td><td>1.44</td><td>3</td><td>(0.9472)</td></tr><tr><td>Modularity</td><td>2.12/2.00</td><td>1.57</td><td>3</td><td>(0.8640)</td></tr><tr><td>Conflict resolution</td><td>5.12/5.17</td><td>0.81</td><td>2</td><td>(0.8839)</td></tr></table>

Table 3  
Correlation matrices using whole sample

<table><tr><td></td><td>Ambiguity</td><td>Complexity</td><td>Modularity</td><td>Conflict resolution</td><td>UIS</td></tr><tr><td>Ambiguity</td><td>1.00</td><td>0.34**</td><td>-0.08</td><td>-0.12</td><td>-0.19</td></tr><tr><td>Complexity</td><td></td><td>1.00</td><td>-0.05</td><td>-0.004</td><td>-0.10</td></tr><tr><td>Modularity</td><td></td><td></td><td>1.00</td><td>-0.06</td><td>0.22</td></tr><tr><td>Conflict resolution</td><td></td><td></td><td></td><td>1.00</td><td>0.37**</td></tr></table>

Table 4  
Factor analyses using whole sample

<table><tr><td></td><td></td><td>Factor 1</td><td>Factor 2</td></tr><tr><td colspan="4">Rotated factor matrix from factor analysis of independent variables</td></tr><tr><td rowspan="3">Ambiguity</td><td>P4S5Q4</td><td>0.87630</td><td></td></tr><tr><td>P4S5Q18</td><td>0.87607</td><td></td></tr><tr><td>P4S5Q20</td><td>0.81088</td><td></td></tr><tr><td rowspan="2">Complexity</td><td>P4S5Q14</td><td></td><td>0.93321</td></tr><tr><td>P4S5Q10</td><td></td><td>0.93071</td></tr><tr><td colspan="4">Rotated factor matrix from factor analysis of the moderator variables</td></tr><tr><td rowspan="3">Modularity</td><td>P2S1Q4</td><td>0.94558</td><td></td></tr><tr><td>P2S1Q8</td><td>0.92372</td><td></td></tr><tr><td>P2S1Q12</td><td>0.91714</td><td></td></tr><tr><td rowspan="3">Conflict resolution</td><td>S3Q8</td><td></td><td>0.92876</td></tr><tr><td>S3Q26</td><td></td><td>0.88392</td></tr><tr><td>S3Q16</td><td></td><td>0.86345</td></tr></table>

MRA involves comparing three regression equations for equality of the regression coefficients [46]. The first of these compares regressions that contain the independent variables and the moderator with one containing these and an additional interaction term.

To create interactions terms between conflict resolution and modularity, and complexity and ambiguity, task complexity and ambiguity were coded as dummy variables, with ‘zero’ representing below-average complexity and ambiguity, and ‘one’ representing above-average complexity and ambiguity. These dummy variables were then multiplied by the respective independent factors in each model to create cross-product terms, and regressions were performed on the entire sample $n = 47$ using these interaction terms, the hypothesized moderators, and the independent variables. This technique was used to determine the extent to which the independent constructs vary in a linear fashion with the continuous variables of complexity and then ambiguity. Significant outcomes generated in this way may allow us to say, for example, that not only does modularity significantly impact client satisfaction under conditions of high ambiguity, but also that the more the ambiguity present, the greater impact of modularity on client satisfaction, and vice versa.

A regression (Table 5(a)) was performed using the two independent factors of conflict resolution and the extent of modularity, the interaction terms of these two factors with the complexity dummy variable, and complexity. The overall model was significant $F(5,41)=2.83, p<0.05$ with an adjusted $r^{2}$ of 0.17.

No interaction factors were significant. The hypothesized moderators of conflict resolution and modularity were significant, while complexity is not, although its impact is negative, as predicted from theory. The $\beta$ coefficients of both the interaction terms are positive, however.

Table 5(b) presents results of the same analysis for ambiguity. The overall model was significant $(F(5,41)=3.24,\ p=0.0149)$ with an adjusted $r^{2}$ of 0.20. The negative impact of ambiguity is greater than that of complexity, but is not significant. The only significant individual factor is conflict resolution, although the modularity–ambiguity interaction term has a strong positive $\beta$ .

Table 5  
Whole sample regression analysis

<table><tr><td></td><td> $\beta$ </td><td>T</td><td>Significance of T</td></tr><tr><td colspan="4">(a) A complexity dummy in interaction with other  $variables^a$ </td></tr><tr><td>Complexity</td><td>-0.07</td><td>-0.30</td><td>0.7639</td></tr><tr><td>Modularity</td><td>0.31</td><td>1.89</td><td>0.0656</td></tr><tr><td>Modularity × complex</td><td>0.02</td><td>0.10</td><td>0.9176</td></tr><tr><td>Conflict resolution</td><td>0.44</td><td>2.96</td><td>0.0051</td></tr><tr><td>Conflict resolution × complex</td><td>0.11</td><td>0.34</td><td>0.7377</td></tr><tr><td colspan="4">(b) An ambiguity dummy in interaction with other  $variables^b$ </td></tr><tr><td>Ambiguity</td><td>-0.12</td><td>-0.50</td><td>0.6188</td></tr><tr><td>Modularity</td><td>0.18</td><td>1.05</td><td>0.2991</td></tr><tr><td>Modularity × ambiguity</td><td>0.27</td><td>1.11</td><td>0.2736</td></tr><tr><td>Conflict resolution</td><td>0.48</td><td>3.31</td><td>0.0020</td></tr><tr><td>Conflict resolution × ambiguity</td><td>-0.18</td><td>-0.67</td><td>0.5086</td></tr></table>

$^{a}$ Adjusted $r^{2}$ of 0.17, $F(5,41)=2.83$ , p=0.028.  
$^{b}$ Adjusted $r^{2}$ of 0.20, $F(5,41)=3.24$ , p=0.0149.

<table><tr><td></td><td> $\beta$ </td><td> $T$ </td><td>Significance of  $T$ </td></tr><tr><td colspan="4">(a) Complexity and the independent variablesa</td></tr><tr><td>Complexity</td><td>0.03</td><td>0.19</td><td>0.8493</td></tr><tr><td>Modularity</td><td>0.30</td><td>2.20</td><td>0.0330</td></tr><tr><td>Conflict resolution</td><td>0.46</td><td>3.43</td><td>0.0014</td></tr><tr><td colspan="4">(b) Ambiguity and the independent variablesb</td></tr><tr><td>Ambiguity</td><td>-0.11</td><td>-0.85</td><td>0.4023</td></tr><tr><td>Modularity</td><td>0.29</td><td>2.20</td><td>0.0336</td></tr><tr><td>Conflict resolution</td><td>0.43</td><td>3.16</td><td>0.0029</td></tr></table>

Table 6  
Whole sample regression analysis  
$^{a}$ Adjusted $r^{2}$ of 0.20, $F(3,43)=3.51$ , p<0.01.  
$^{b}$ Adjusted $r^{2}$ of 0.21, $F(3,43)=5.07$ , p<0.01.

Under MRA, for complexity or ambiguity to be pure moderators, significant differences must be apparent between the regression coefficients of the regressions above that include the interaction terms, and those below (Table 6(a and b)), that do not include them. No significance was found, so we can conclude that task complexity and ambiguity are not pure moderators in this model.

A final comparison in MRA is of regression coefficients between regressions without the moderator and those that include the moderator. Table 7 depicts the regression without moderators, and was significant overall $F(2,44)=7.30, p<0.01$ , with an adjusted $r^{2}$ of 0.21. Conflict resolution and modularity were individually significant (for conflict, T=3.47, p=0.0012, and for modularity, T=2.22, p<0.05). However, the model was not significantly different from those that included the moderators. We can conclude that while complexity and ambiguity have no significant relationship to the criterion or dependent variable, they do not interact with the independent or predictor variables in a way that moderates the form of these relationships.

Whole sample regression analysis $^{a}$ of model

<table><tr><td></td><td> $\beta$ </td><td> $T$ </td><td>Significance of  $T$ </td></tr><tr><td>Conflict resolution</td><td>0.46</td><td>3.47</td><td>0.0012</td></tr><tr><td>Modularity</td><td>0.30</td><td>2.22</td><td>0.0317</td></tr></table>

$^{a}$ Adjusted $r^{2}$ of 0.21, $F(2,44)=7.30$ , p=0.0018.

## 4.2. Subgroup analysis

In the split-sample analysis, median values for complexity and ambiguity were used to divide the sample into high and low complexity and ambiguity, as is typical for split sample analysis $[33, 29, 31]$ . For complexity, the median reported value was 5.0, but since seven cases reported exactly this value, these seven were eliminated, leaving 19 teams with above-the-median complexity value of 5.0, and 21 teams reporting below this average. For ambiguity, the reported value of median was 4.0, but one case reported exactly this value, so this team was eliminated, leaving 24 teams above this median value and 22 below it.

Following standard practice [34], Chow tests [10] were performed to determine whether the models based on the split samples were significantly different from one another. Regressions were performed on the four subsamples defined by the model – high and low task complexity, and high and low task ambiguity.

To investigate Hypothesis 1, conflict resolution and modularity were regressed in separate regressions onto the dependent variable of client satisfaction, first using only high complexity teams, and then using only low complexity teams (H1). For Hypothesis 2, this process was repeated using only high ambiguity teams, and then using only low ambiguity teams (H2).

Hypothesis 1 was then investigated, and for teams reporting above the median in task complexity, the model is highly significant $(F(2,15)=11.44, p<0.001)$ , with an adjusted $r^{2}$ of .55, as is the individual conflict factor $(T=4.43, p<0.001)$ . Modularity is also significant $(T=2.19, p<0.05)$ , but not substantially different from that revealed in the whole sample analysis. For those teams reporting below average complexity, neither the model nor either individual indicator are significant.

Moderation is difficult to confirm with small sample sizes, but results of the Chow test confirmed that the regression coefficients of the high and low complexity subsamples were significantly different (F = 3.083, p = 0.05). Thus, split-sample analyses confirm

Table 8  
Split sample regression analysis

<table><tr><td></td><td> $\beta$ </td><td> $T$ </td><td>Significance of  $T$ </td></tr><tr><td colspan="4">(a) Model using teams with above-median complexitya</td></tr><tr><td>Conflict resolution</td><td>0.72</td><td>4.43</td><td>0.0005</td></tr><tr><td>Modularity</td><td>0.36</td><td>2.19</td><td>0.045</td></tr><tr><td colspan="4">(b) Model using teams with below-median complexityb</td></tr><tr><td>Conflict resolution</td><td>0.10</td><td>0.46</td><td>0.6499</td></tr><tr><td>Modularity</td><td>0.25</td><td>1.13</td><td>0.2731</td></tr></table>

$^{a}$ Adjusted $r^{2}$ of 0.55, $F(2,15)=11.44$ , p<0.001.  
$^{b}$ Adjusted $r^{2}$ of -0.03, $F(2,19)=0.695$ , p=0.511.

Hypothesis 1 to the extent that the model is highly significant under conditions of high task complexity, and insignificant under conditions of low task complexity. However, this effect is due to the impact of conflict resolution (which is almost ten times more significant than in the whole-sample analysis), and not the effect of modularity. Thus, Hypothesis 1 is true for conflict resolution, but not for modularity. [See Table 8(a and b).]

Hypothesis 2 was then investigated, and for teams reporting above the median in task ambiguity, the model is highly significant $(F(2,21)=9.48, p=0.0012)$ , with an adjusted $r^{2}$ of 0.42. Both, conflict resolution and modularity are individually significant (for conflict, T=3.47, p<0.01, and for modularity, T=3.07, p<0.01). For those teams reporting below average ambiguity, neither the model nor the indicator is significant. However, the Chow test comparing regression coefficients was not significant $(F=1.003, p=0.37)$ . Despite the fact that the model is significant under conditions of high ambiguity, but not low ambiguity, we cannot confirm Hypothesis 2. [See Table 9(a and b).

Table 10(a and b) illustrate the effects of conflict resolution and modularity on user information satisfaction for those teams with high and low average levels of both, complexity and ambiguity, respectively. As in the foregoing, the model was significant for the high complexity and ambiguity sample $(F(2,8)=5.72, p<0.05)$ , with an adjusted $r^{2}$ of 0.49, but not significant for the low ambiguity and complexity sample. Again, conflict resolution explained a larger portion of the variance than did ambiguity. The Chow test did confirm that the two regression coefficients are significantly different $(F=3.34, p=0.05)$ .

Table 9  
Split sample regression analysis

<table><tr><td></td><td> $\beta$ </td><td> $T$ </td><td>Sinificance of  $T$ </td></tr><tr><td colspan="4">(a) Model using teams with above-median ambiguitya</td></tr><tr><td>Conflict resolution</td><td>0.55</td><td>3.47</td><td>0.0023</td></tr><tr><td>Modularity</td><td>0.49</td><td>3.07</td><td>0.0058</td></tr><tr><td colspan="4">(b) Model using teams with below-median ambiguityb</td></tr><tr><td>Conflict resolution</td><td>0.26</td><td>1.14</td><td>0.2680</td></tr><tr><td>Modularity</td><td>0.14</td><td>0.64</td><td>0.5307</td></tr></table>

$^{a}$ Adjusted $r^{2}$ of 0.42, $F(2,21)=9.48$ , p=0.0012.  
$^{b}$ Adjusted $r^{2}$ of -0.03, $F(2,20)=0.70$ , p=0.51.

## 4.3. Discussion

This study utilizes a parsimonious, theoretically grounded model derived from the organizational design and software development literatures. Its contribution lies in its simplicity, and also in its combined investigation of the two important task variables, both of which can sabotage effective software development. It operationalizes theoretical prescriptions for managing complexity and ambiguity in its selection of two critical process factors – conflict resolution and modularity. These factors together do not explain any of the variance in client information satisfaction six months subsequent to installation for unambiguous, low-complexity projects. But they explain 55% of the variance in client satisfaction for projects with above-average complexity, and 42% of the variance in client satisfaction for projects with above-average ambiguity. As compared to their impact across all projects, conflict resolution plays a greater role than modularity in apparently mitigating the effects of complexity, and modularity positively impacts highly ambiguous projects. The converse is not true – conflict resolution does not strongly interact with ambiguity to counteract its negative effects, nor does modularity interact strongly with complexity to mitigate its effects.

Table 10  
Split sample regression

<table><tr><td></td><td> $\beta$ </td><td> $T$ </td><td>Significance of  $T$ </td></tr><tr><td>(a) Using teams with both,  $ambiguity^a$ </td><td>both,</td><td>above-median</td><td>complexity and</td></tr><tr><td>Conflict resolution</td><td>0.60</td><td>2.65</td><td>0.0292</td></tr><tr><td>Modularity</td><td>0.42</td><td>1.83</td><td>0.1043</td></tr><tr><td>(b) Using teams with both,  $ambiguity^b$ </td><td>both,</td><td>below-median</td><td>complexity and</td></tr><tr><td>Conflict resolution</td><td>0.11</td><td>0.39</td><td>0.7059</td></tr><tr><td>Modularity</td><td>0.16</td><td>0.55</td><td>0.5951</td></tr></table>

$^{a}$ Adjusted $r^{2}$ of 0.49, $F(2,8)=5.72$ , p<0.05.  
$^{b}$ Adjusted $r^{2}$ of -0.13, $F(2,12)=0.30$ , p=0.82.

The whole-sample MRA analysis indicates that this effect operates through the error terms, by affecting the strength rather than the form of the relationship of the independent variables to client information satisfaction. Conflict resolution and, to a lesser extent, modularity, are homologizer moderators with no direct relationship to either the independent or dependent constructs.

For practitioners, the lesson is clear. First, take time to identify those projects that are high in complexity and ambiguity. Team members and leaders are often aware of these conditions and are a good source for this information. Users also may well understand the potential complexities and ambiguities of a software development effort. Such identification processes should become a routine aspect of application portfolio development. Once these projects have been identified, corrective action can be taken, as suggested by this research. Foster conflict resolution capabilities in project teams faced with highly complex projects. This could include formal training, tacit learning, and modifications to incentive systems. Many human resource departments provide training in this area, as do many consulting organizations. Team members should be made aware of the purpose for the trainings and the importance of conflict resolution, particularly for projects high in complexity.

Practitioners should also work to ensure that modularity is being utilized in highly ambiguous software development projects. It is widely acknowledged that modularity can save time and, therefore, money during development. This study shows that modularity can increase system effectiveness also, for reasons consistent with current organizational theory. There are a number of CASE (computer-aided software engineering) tools available in the market that have features that promote modularity of design and development. Team members in these teams should be instructed regarding the meaning of ambiguity, its potential deleterious effects on software development success, and the role that modularity can play in mitigating these negative effects.

## 4.4. Limitations

This study does not confirm that feedback and conflict resolution behaviors actually reduce complexity, nor that modularity reduces ambiguity; only that, in the presence of high complexity, conflict-resolution behaviors have a positive impact on subsequent client satisfaction, and that, in the presence of high ambiguity, modularity also has a positive impact on information satisfaction. A theoretical argument has been presented which associates these positive impacts with their capacity to mitigate or absorb the negative effects of task complexity and ambiguity, but the evidence does not go so far. Future research in this direction could confirm these theoretical propositions through controlled experimental manipulations.

Client satisfaction is critical for systems success, and information satisfaction is especially important in this era of knowledge work and organizational learning. However, another path for future research would be the addition of non-perceptual dependent measures and metrics to identify impacts of this model on technical success.

This study does not investigate mechanisms for complexity and ambiguity reduction at the boundary of the team. It seems likely that much effective ambiguity reduction occurs in interaction with those outside the team. Thus, the impacts of these behaviors by boundary spanners (externally-oriented team members) is another potentially fruitful direction for future research. Nor does it investigate small or large teams, focusing as it does on medium-sized teams. While we have no reason to believe that these results cannot be generalized to larger or smaller software development teams, our results cannot speak on this issue.

## 5. Conclusion

Organizational theorists have long looked to organizational design for ways to improve the effectiveness of organizational information processing. The present study builds on this theory base to take an empirical look at information-processing behaviors at the team level of analysis. An important contribution is the combined examination of both, task complexity and ambiguity, confirming theory that identifies them as distinct constructs, each posing their own challenges. That which moderates complexity does not moderate ambiguity and vice versa. By operationalizing conflict resolution and modularity as an information processing behavior and a technology, respectively, this research confirms theoretical organizational design prescriptions in a model that is parsimonious, yet highly significant under the task conditions specified.

Communication via rich information channels has been cited as a way to reduce task ambiguity. Within teams, much interaction occurs face-to-face and is thus already rich, so it is important to investigate alternative mechanisms for reducing task-related ambiguity. We do this by looking to the modules produced with process technologies as external manifestations of shared perceptions of desired outcomes. This conceptualization of modularity provides a theoretical rationale for the widely acclaimed benefits of modularity technologies and contributes to the growing body of research that ties tools and techniques to theoretical reasons for their effectiveness. The growing popularity of object-oriented technologies motivates our continued theoretical interest in the phenomenon of modularity.

For practitioners, we present support for a contingency model which states that under conditions of high task complexity, conflict resolution is an effective team capability, while under conditions of high task ambiguity, modularity technologies are beneficial, especially in conjunction with conflict resolution. While further research is needed to confirm these prescriptions, this study paves the path for practitioners to enhance system development effectiveness by providing modularity capabilities to teams facing ambiguous projects, and by enabling conflict-resolution behaviors within those teams facing highly complex projects.

## Appendix A

## Survey items (all seven-point Likert scales)

Ambiguity: (α = 0.8117)

Please characterize the extent to which your project has the following characteristics:

1. To what extent do multiple views exist of how the final system should look?

2. During system development, to what extent can information be interpreted in different ways, which can lead to different but acceptable solutions?

3. To what extent do multiple views exist of how the final system should be developed?

Not at all – very small extent – some extent – very great extent

Complexity: (α = 0.8398)

Please characterize the extent to which your project has the following characteristics:

1. How technically complex is the system being developed?

2. To what extent are the technical problems for this system particularly complicated?

Not at all – very small extent – some extent – very great extent

System success: $(\alpha = 0.9472)$

Please provide your impressions of how the present system satisfies your needs:

1. The system provides the precise information that I need.

2. The information content meets my needs.

3. I get the information I need on time.

N/A – strongly disagree – neither agree nor disagree – strongly agree

Modularity: (α = 0.8640)

How often does your project team perform this activity on the current project:

1. Develop modular, component-oriented application parts?

2. Maintain an inventory of reusable application components?

3. Create application system units from individual components?

Not at all – very small extent – some extent – very great extent

Conflict resolution:

Please evaluate to what degree you feel the following statements describe your project team:

1. In general, we get along very well.

2. This team resolves conflicts that exist among team members in a timely manner.

3. This team finds ways to minimize tensions between members.

N/A – strongly disagree – neither agree nor disagree – strongly agree

## References

[1] U. Apte, C.S. Sankar, M. Thakur, J. Turner, Reusability strategy for development of information systems: implementation experience of a bank, Management Information Systems Quarterly 14(4), 1990, pp. 421–431.

[2] L. Argote, Input uncertainty and organizational coordination in hospital emergency units, Administrative Science Quarterly 27, 1982, pp. 420–434.

[4] R.D. Banker, R.J. Kauffman, Reuse and productivity in integrated computer-aided software engineering – an empirical study, Management Information Systems Quarterly 15(3), 1991, pp. 375–401.

[5] H. Barki, J. Hartwick, User participation, conflict, and conflict resolution: the mediating role of influence, Information Systems Research 5(4), 1994, pp. 422–438.

[6] B. Boehm, Software Engineering Economics, Prentice-Hall, New York, NY, 1981.

[7] T. Burns, G.M. Stalker, The Management of Innovation, Quadrangle Books, Chicago, IL, 1961.

[8] D.J. Campbell, Task complexity: a review and analysis, Academy of Management Review 13(1), 1988, pp. 40–52.

[9] P.H. Cheney, R.I. Mann, D.L. Amoroso, Organizational factors affecting the success of end-user computing, Journal of Management Information Systems 3(1), 1986, pp. 65–80.

[10] G.C. Chow, Tests of equality between sets of coefficients in two linear regressions, Econometrika 28, 1960, pp. 591-605.

[11] P. Constance, Don't slip into the swamp; navy and air force guides help software managers avoid common traps, Government Computer News 14, 1995, pp. 23.

[12] B. Curtis, H. Krasner, N. Iscoe, A field study of the software design process for large systems, Communications of the ACM 31(11), 1988, pp. 1268–1287.

[13] R.L. Daft, R.H. Lengel, Organizational information requirements, media richness and structural design, Management Science 32(5), 1986, pp. 554–571.

[14] R.L. Daft, N.B. Macintosh, A tentative exploration into the amount and equivocality of information processing in organizational work units, Administrative Science Quarterly 26, 1981, pp. 207–224.

[15] C. Deephouse, T. Mukhopadhyay, D.R. Goldenson, M.I. Kellner, Software Processes and Project Performance, Journal of Management Information Systems, 12(3) (1995–1996) 187–205.

[16] E.X. DeJesus, Big oop, no oops, Byte 20(8), 1995, pp. 74.

[17] W.H. Delone, E.R. McLean, Information systems success: the quest for the dependent variable, Information Systems Research 3(1), 1992, pp. 60–95.

[18] R.E. Duncan, Characteristics of organizational environments and perceived environmental uncertainty, Administrative Science Quarterly 17, 1972, pp. 313–327.

[19] G. Edmondson, One Electronic SOS clinched the deal, Business Week 3464 (1996) 83.

[20] J.R. Galbraith, Organizational Design, Addison-Wesley, Reading, MA, 1977.

[21] D. Gerwin, Relationships between structure and technology, in: P. Nystrom, W. Starbuck (Eds.), Handbook of Organizational Design, Oxford University Press, 1981, pp. 3–38.

[22] D.L. Goodhue, R.L. Thompson, Task–technology fit and individual performance, Management Information Systems Quarterly 19(2), 1995, pp. 213–233.

[23] T. Guimaraes, M. Igbaria, M. Lu, Determinants of DSS success: an integrated model, Decision Sciences 23(2), 1992, pp. 409–430.

[24] J.R. Hackman, M.D. Lee, Redesigning work: a strategy for change, Work in America Institute, Scarsdale, NY, 1979.

[25] J.C. Henderson, J.G. Cooprider, Dimensions of IS planning and design aids: a functional model of CASE technology, Information Systems Research 1(3), 1990, pp. 227–254.

[26] L.A. Isabella, Evolving interpretations as a change unfolds: how managers construe key organizational events, Academy of Management Journal 33(1), 1990, pp. 7–41.

[27] B. Ives, M.H. Olsen, J.J. Baroudi, The measurement of user information satisfaction, Communications of the ACM 26(10), 1983, pp. 785–793.

[28] P. Keen, Shaping The Future: Business Design Through Information Technology, Harvard Business School Press, Boston, MA, 1991.

[29] D.J. Ketchen, J.B. Thomas, R.R. McDaniel, Process, content and context: synergistic effects on organizational performance, Journal of Management 22(2), 1996, pp. 231–352.

[30] M.V. Koushik, V.S. Mookerjee, Modeling coordination in software construction: an analytical approach, Information Systems Research 6(3), 1995, pp. 220–244.

[31] R. Madhavan, J.E. Prescott, Market value impact of joint ventures: the effect of industry information processing load, Academy of Management Journal 38(3), 1995, pp. 900–912.

[32] J.E. McGrath, Groups: Interaction and Performance, Prentice-Hall, Englewood Cliffs, NJ, 1984.

[33] J.D. McKeen, T. Guimaraes, J.C. Wetherbe, The relationship between user participation and user satisfaction: an investigation of four contingency factors, Management Information Systems Quarterly 18(4), 1994, pp. 427–438.

[34] D. Miller, M.F.R. Kets de Vries, J. Toulouse, Top executive locus of control and its relationship to strategy-making structure, and environment, Academy of Management Journal 25, 1982, pp. 237–253.

[35] S. Nidumolo, The effect of coordination and uncertainty on software project performance: residual performance risks as an intervening variable, Information Systems Research 6(3), 1995, pp. 191–219.

[36] I. Nonaka, A dynamic theory of organizational knowledge creation, Organization Science 5(1), 1994, pp. 14–37.

[37] R. Pakath, H.R. Rao, Module-based design for a portfolio of institutional decision support systems, Information and Management 20(4), 1991, pp. 265–278.

[38] C.M. Pancake, The promise and cost of object technology: a five-year forecast, Communications of the ACM 38(10), 1995, pp. 33–49.

[39] PC Week, The toughest challenged, Re:sources, 12(15) (1995) 18.

[40] C.A. Perrow, Framework for comparative organizational analysis, American Sociological Review 16, 1967, pp. 444–469.

[41] L.W. Phillips, R.P. Bagozzi, On measuring organizational properties: methodological use of key informants, Working Paper, Stanford University, Graduate School of Business, 1981.

[42] H.R. Rao, J.M. An, The effect of team composition on decision scheme, information search, and perceived complexity, Journal of Organizational Computing 5(1), 1995, pp. 1–20.

[43] D. Robey, D.L. Farrow, C.R. Franz, Group process and conflict in system development, Management Science 35(10), 1989, pp. 1172–1191.

[44] D. Robey, L.A. Smith, L.J. Vijayasarathy, Perceptions of conflict and success in informations systems development projects, Journal of Management Informations Systems 10(1), 1993, pp. 123–139.

[45] G.I. Sanders, J.F. Courtney, A field study of organizational factors influencing DSS success, Management Information Systems Quarterly 9(1), 1985, pp. 77–93.

[46] S. Sharma, R.M. Durand, O. an Gur-Arie, Identification and analysis of moderator variables, Journal of Marketing Research 18, 1981, pp. 291–300.

[47] H.A. Smith, J.D. McKeen, Computerization and management: a study of conflict and change, Information and Management 22, 1992, pp. 53–64.

[48] James D. Thompson, Organizations in Action, McGraw-Hill, New York, NY, 1967.

[49] M.L. Tushman, Work unit characteristics and subunit communication structure: a contingency analysis, Administrative Science Quarterly 24, 1979, pp. 84–98.

[50] M.L. Tushman, D.A. Nadler, Information processing as an integrating concept in organizational design, Academy of Management Review 3, 1978, pp. 613–624.

[51] D.B. Walz, J.J. Elam, B. Curtis, Inside a software design team: knowledge acquisition, sharing and integration, Communications of the ACM 36(10), 1993, pp. 63–77.

[52] A.H. Van De Ven, A. Delbecq, R. Koenig, Determinants of coordination modes within organizations, American Sociological Review 41, 1976, pp. 322–338.

[53] K.E. Weick, Technology as Equivoque, in Goodman and Sproull (Eds.), Technology and Organizations, Chap. 1, Jossey-Bass, San Francisco, CA, 1990.

[54] R.E. Wood, Task complexity: definition of the construct, Organizational Behavior and Human Decision Processes 37, 1986, pp. 60–82.

[55] Y. Yoon, T. Guimaraes, Selecting expert system development techniques, Information and Management 24(4), 1993, pp. 209–223.

[56] R.W. Zmud, Management of large software development efforts, Management Information Systems Quarterly 4(2), 1980, pp. 45–55.

![](/api/attachments/6F6S8MBW/fulltext/images/e7e2b67a6f5f2cd79a6d83c9631d90706215211d7b9e8068488c978855ac6deb.jpg)  
Stephanie Watts Sussman is an Assistant Professor of Information Systems at the Weatherhead School of Management at Case Western Reserve University. She received her doctorate from Boston University, where the research for this paper was performed. Her research interests include systems development, technologies for knowledge transfer, and computer-mediated communication.
