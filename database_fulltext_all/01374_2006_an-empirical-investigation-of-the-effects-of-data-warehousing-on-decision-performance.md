---
otero_id: 1374
otero_key: "956QGENX"
title: "An empirical investigation of the effects of data warehousing on decision performance"
authors: "Yong-Tae Park"
year: "2006"
journal: "Information & Management"
doi: "10.1016/j.im.2005.03.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An empirical investigation of the effects of data warehousing on decision performance

Yong-Tae Park <sup>\*</sup>

California State University, P.O. Box 6848 LH-552, Fullerton, CA 92834-6848, USA

Received 27 January 2004; received in revised form 16 December 2004; accepted 5 March 2005 Available online 22 April 2005

## Abstract

Organizations implement data warehouses to overcome the limitations of DSS by adding this database component and thereby improve decision performance. However, no empirical evidence is available to show the effects of a data warehouse (DW) on decision quality and performance. To examine this, a laboratory experiment was conducted. The data warehouse variables considered were the time horizon of the data and its level of aggregation.

It was found that using a full data warehouse resulted in significantly better performance and that using it resulted in better performance than using a partial data warehouse (long-time history with no aggregated data). However, using a partial data warehouse was not significantly better than not using a data warehouse at all. <sup>#</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Data warehouse; Decision support systems; IS success; Database management; Decision performance

## 1. Introduction

Improved decision making is a major concern of business managers and DSS users in the organization. To make a quality decision, decision-makers must have quality information pertinent to the decision at hand. Several studies have shown [26,37] that information and system quality affect an individual’s performance. Thus, improving system quality should lead to enhanced decision quality.

Because organizations frequently process uncertain information and thus decision makers must accept the ‘‘bounded rationality’’ [38], they should reduce their uncertainty by obtaining as much reliable and consistent information as possible. Due to the potential benefits of a data warehouse (DW) as well as internal and/or external pressure for creating a competitive advantage, many organizations have launched DW projects with the expectations of acquiring a consistent and reliable source of data for their DSS. However, the success rate in realizing benefits of DW has been lower than expected [29,58,64,68]. Prior studies on DWs have focused mainly on the success of their implementation, rather than their effects on the performance of DSS users. Thus, little empirical evidence of the effectiveness of DW has been reported [39]. This calls for empirical studies to help organizations understand the benefits of DW. The research question of the study was: how does the presence of a DW (including data aggregation and time horizon) change a DSS user’s decision performance?

## 2. Previous research

Research on DW has been mainly descriptive or conceptual [49,50,66]. Only a few studies [56,67] were empirical. Watson and Haley [65] found that DW was used throughout the organization and also supported executive information systems (EIS). Haley [28] viewed the DW as an IT infrastructure that provides appropriate data and tools to support decision makers and contended that DW provided a unique opportunity to improve the IT infrastructure. Her study showed that project factors, organizational factors, and infrastructure factors had significant impact on successful implementation of a DW project. Little and Gibson [36] conducted an exploratory factor analysis to identify factors affecting the successful implementation of DWs. They found that understanding the organization’s external environment and prototyping to demonstrate data warehousing were critical for successful implementation.

## 2.1. DW research on conceptual framework and empirical studies

Based on an analysis of successful DW implementations for strategic use, Park [42,43] proposed frameworks for assessing a DW for suitability and justifying a DW project from a standpoint of strategic advantage. Chen and Soliman [11] examined the underlying factors of end-user satisfaction with DW, especially the roles of the information center. They found that most of the items in classic end-user satisfaction measurements were valid in DW environments and that satisfaction with DW depended on the roles and performance of information centers. Shin [53] also found that user satisfaction was affected by system quality factors such as data quality and its locatability. In a study of the factors affecting DW success, Wixom and Watson found that a high level of data and system quality was associated with a high level of perceived net benefits. Rudra and Yeo [48] found that the data quality of DW is influenced by its data captured, the degree of heterogeneity of system integration, and the level of policy and planning from management.

## 2.2. Previous empirical studies of DSS performance

DSS performance research has focused on two main topics: DSS availability and evaluation of its features [7]. Studies investigated the change in decision performance when using a DSS over decisions made without a DSS [2,5,10,12,40,61,62] and the effects of DSS components on decision quality [4].

Ghani and Lusk [21] measured the impact of presentation format and amount of information on decision performance and found that after an increase in the volume of information (with or without a change in presentation format), the initial performance deteriorated. In a similar study, Dickson et al. [16] showed that generalized claims of superiority of graphic presentation were not supported, at least for decision-related activities. Benbasat et al. [6] investigated the effect of color-enhanced and other presentation modes on user perception and decision making. Their results suggested that the benefits are task-dependent and that the effect is not pervasive. Jarvenpaa [34] investigated the effect of task demand and graphical format on decision time and evaluation strategy and found that presentation format influenced the decision time and information acquisition strategy. Tan and Benbasat [59] conducted laboratory experiments to assess the relative strength and weakness of a variety of graphs for information extraction tasks. They found that data extraction accuracy was not significant affected by presentation format.

Cats-Baril and Huber [9] found that use of heuristics and increased interaction had positive effects on decision quality, user productivity, and user attitude. Dos Santos and Bariff [17] found that more structured manipulation of model variables and the display of incremental changes improved performance. Liang [35] found that the quality of the IS was the most critical factor investigated. Goslar et al. [24] investigated whether or not information overload (data level) affected performance when the subjects could select data they wished to use from the available database. Their study showed that data level affected the number of alternatives considered during the decision making process but it did not show any significant influence on the time expended to complete the task.

## 3. Research framework and research hypotheses

The use of IT can impact organizational design, intelligence, and decision making [30]; accessing and transforming good transaction data make DW an excellent component of a DSS. Therefore, a DSS with DW should improve the performance of users by improving information accessibility which positively affects the quality of decision making.

DeLone and McLean’s IS success model [14] postulated that system and consequent information quality affect both the system use and user satisfaction, which have an impact on user performance. However, Seddon’s IS success model [51] inferred that improved system quality can positively affect systems use and user satisfaction; this concurs with the argument of the reformulated IS success model by DeLone and McLean [15]. Based on these, several studies empirically investigated the association between system quality and individual impact [19,60] and between information quality and individual impact [52]. Applying this argument to data warehousing suggests that the adoption and use of a DW in a DSS can improve decision performance.

For an IT to impact on individual’s performance, it must be utilized and there must be a good fit between the user’s tasks and the system [22]. The effectiveness of an information system can be achieved when system capabilities reduce ambiguity and uncertainty [13].

The characteristics of decision tasks in DSS are typically semi-structured or unstructured [57]. The function of information is to reduce uncertainty by decreasing the randomness of events [1]. One of the characteristics that make DW valuable is the time window of clean data it provides; by providing more relevant transaction data pertinent to the task, a decision maker can lower the uncertainty level and this should lead to improved performance.

One of the major difficulties for decision makers is that there is not enough historical data stored in the applications to meet their needs [25]. A 60–90-day time horizon is normal for operational systems, while a multi-year horizon is normal for a data warehouse. Furthermore, since most of DSS processing is performed against aggregated data [32], the characteristics of DW can reduce data processing time as compared to a traditional database, and thus allow decision makers more time to analyze the decision task, leading to better results. Thus, the hypotheses of this study were:

H1. DSS users’ performance on marketing decision task based on trend-analysis will be different for groups using a DSS database with different characteristics, in terms of time window and data aggregation.

H1a. DSS users using DW-enhanced DSS with longtime history and aggregated data will perform better on marketing tasks based on trend-analysis than those using a traditional DSS database.

H1b. DSS users using DW-enhanced DSS with longtime history and aggregated data will perform better on marketing tasks based on trend-analysis than those using DW-enhanced DSS with long-time history only.

H1c. DSS users using DW-enhanced DSS with longtime history only will perform better on marketing decisions based on trend-analysis than those using a DSS with a traditional DSS database.

H2. DSS users’ performance on marketing tasks will differ, depending on the level of task complexity.

## 4. Research methodology

A laboratory experiment was conducted to test the research hypotheses, since the key intent was to investigate a causal relationship. Strong internal validity of an experimental method provides the best way to determine whether or not causal relationships exist between independent and dependent variables [20,33].

Table 1  
The independent variables

<table><tr><td>Independent variable</td><td>Operationalization</td></tr><tr><td>Characteristics of DSS database component</td><td>Difference in time horizon on the data in the DSS databasePresence or absence of aggregated data in the DSS database</td></tr><tr><td>Tack complexity</td><td>Difference in the number of variables considered in decision making</td></tr></table>

## 4.1. Dependent and independent variables

The dependent variable was decision performance, which involved the accuracy of identifying and prioritizing four market districts that would probably accomplish revenue maximization for a fictitious company, Aroma Food Company, by deploying four sales force teams. The unit of analysis was the individual user.

The independent variables were the DSS database with different characteristics (traditional versus data warehousing components) and decision tasks with different levels of complexity (see Table 1). Two unique characteristics of a DW approach are the length of the time horizon of the data it contains and aggregated data.

The DSS database component used in this study was the database component of the Red Brick Data Warehouse (a product of Red Brick Systems, Inc., a wholly-owned subsidiary of Informix Software Inc.) that supports the BrioQuery Explorer DSS tool version 5.0 in solving decision tasks. This tool was developed by Brio Technology, Inc.; the Explorer incorporates core query, analysis, and reporting features, and has data modeling functionality. The data set was sales transaction data organized by subject. In most cases DSS users ask for aggregated or calculated data to meet their needs; therefore, the DSS databases used in the study included both time and aggregation data. They were:

 Traditional DSS database:

\- With a short-time history of 3 months without aggregated data.

 DSS Database with long-time history (Partial DW)

\- With a long-time history (2 years of data).

 DSS database with long-time history and aggregated data (Full DW)

\- With a long-time history and aggregated data.

This study utilized the sample data from the Red Brick Data Warehouse version 5.1. It contained 69,776 records, but the data used for decision tasks were 33,786 records (2-year time period) for the DW and 4195 records (3-month time period) for the traditional DSS database.

The decision task in this experiment involved sales force deployment for the marketing department of Aroma Food Company. By analyzing various trend analyses, subjects were required to identify the four out of eight market districts to which sales force teams should be dispatched in order to maximize sales revenue.

Among the ways of classifying decision tasks [23,46,63], task complexity was used in this study. It was manipulated at two levels in terms of the number of criteria to be considered. Task complexity entails the degree of cognitive load (mental effort) required to identify and/or solve a problem [44]. Simon [54] had conceptualized complexity as a function of the number of elements in a system and the degree and nature of the interactions among them. I therefore postulated that the level of task complexity was a function of the number of decision criteria considered in the task and the degree of interaction between them. By the same token, in solving a semi-structured decision task, the more the decision criteria and uncertainty involved, the greater the cognitive load imposed on the decision maker. However, it is difficult, if not impossible, to determine the number of interactions among decision criteria that a decision maker considers in solving a task. Thus, only the number of decision criteria was used as the determinant of task complexity in this study.

For convenience in operationalizing task complexity, subjects must take into account five criteria in making a sales force deployment decision for a less complex task. On the other hand, they must take into consideration these same five criteria and two additional pieces of information for a more complex task. The two levels of task complexity and the three levels of DSS database components yielded a 2  3 factorial design.

## 4.2. The measurement approach in evaluating performance

Decision tasks handled by DSS users are usually semi-structured or unstructured and a decision maker must exercise his or her judgment at some point in the process. Therefore, a certain degree of subjectivity is inevitable.

To ensure reliable measurement of the decision performance in the study, a panel of judges was employed; they were four MBA students and one economics Ph.D. student who had industrial experience in decision making. There was some disagreement in a few criteria. For these, a majority vote was taken after the panel had discussed them.

The panel used a seven point scoring scale and sorted the respondents into those who only correctly identify the four most promising market districts and those who also prioritize them correctly. Furthermore, the panel gave partial credit to those who do not correctly identify the four most promising market districts but performed well in prioritizing those selected. Thus a subject received seven points when he/she correctly identified and prioritized the four market districts that could most probably help achieve the marketing objective. When he/she correctly identified the four market districts but not the order, he/she was given four points. If a subject incorrectly identified market districts, he/she lost one point for each wrong market district. If a subject identified all four market districts but prioritized them incorrectly, he/she lost one, two, or three points depending on the extent of the error.

## 4.3. Subjects and laboratory experiment

Twelve MBA and graduate IS students then participated in two pilot studies to test the scope of the task and validate the instruments. Later, a convenience sample of ninety volunteers (mostly MBA or MIS students who had taken MBA or IS classes) participated in the study. The participants wanted to have hands-on experiences with DSS tools and DW software. No incentives were given. Most of the subjects were familiar with decision analysis techniques and/or market forecasting.

BrioQuery provides a managed query environment that allows subjects to perform most of their own queries. Since its graphic functionality was not effective in a trend analysis when more than two trends had to be presented, the Microsoft Excel spreadsheet program was used as a supplementary tool.

A time constraint or time pressure can have significant impact on decision performance of DSS users [8] in the areas of crisis [55] and emergency management [31]. However, the time constraints faced by the users of typical DSS applications in business organizations are seldom critical. Moreover, in the experiment, the two rounds of pilot studies had shown that most subjects completed the task within 40 min. Furthermore, since a moderate level of time pressure can result in more goal commitment [3] subjects were given a time limit of 40 min for the task.

Descriptive statistics for decision performance

<table><tr><td>DSS database characteristics</td><td>Task difficulty</td><td>Mean</td><td>S.D.</td><td>N</td></tr><tr><td rowspan="3">Traditional DSS database</td><td>Less complex task</td><td>4.13</td><td>1.96</td><td>15</td></tr><tr><td>More complex task</td><td>3.73</td><td>1.67</td><td>15</td></tr><tr><td>Total</td><td>3.93</td><td>1.80</td><td>30</td></tr><tr><td rowspan="3">DSS database with long-history</td><td>Less complex task</td><td>5.20</td><td>1.82</td><td>15</td></tr><tr><td>More complex task</td><td>4.60</td><td>1.55</td><td>15</td></tr><tr><td>Total</td><td>4.90</td><td>1.69</td><td>30</td></tr><tr><td rowspan="3">DSS database with long-history and aggregated data</td><td>Less complex task</td><td>5.87</td><td>1.30</td><td>15</td></tr><tr><td>More complex task</td><td>5.07</td><td>1.44</td><td>15</td></tr><tr><td>Total</td><td>5.47</td><td>1.41</td><td>30</td></tr><tr><td rowspan="3">Total</td><td>Less complex task</td><td>5.07</td><td>1.83</td><td>45</td></tr><tr><td>More complex task</td><td>4.47</td><td>1.62</td><td>45</td></tr><tr><td>Total</td><td>4.77</td><td>1.74</td><td>90</td></tr></table>

## 5. Data analysis

Two-way ANOVA test was conducted using SPSS 11.5 for Windows at a 95% confidence level. The descriptive statistics are summarized in Table 2. The Levene’s test for homogeneity of variances (significance level $0 . 1 5 5 > 0 . 0 5 )$ shows (Table 3) that the variance in decision performance scores is not significant across the experimental groups, assuring that the homogeneity of variance assumption was not violated [41].

The results of ANOVA test on dependent variable show (Table 4) that there is a significant difference among groups with different DSS database characteristics on decision performance $( F = 6 . 7 , ~ p < 0 . 0 1 )$ . However, there was no significant difference between groups with different levels of task complexity on decision performance at the significance level of 0.05, although the effect size (0.035) indicated a potential effect when using a larger sample.

Table 3  
Levene’s test for homogeneity of variances on decision performance

<table><tr><td>F</td><td>1.65</td></tr><tr><td>d.f.1</td><td>5</td></tr><tr><td>d.f.2</td><td>84</td></tr><tr><td>Significance</td><td>0.16</td></tr></table>

The ANOVA tests found no interaction effects between DSS database component and task difficulty, indicating that these variables do not jointly affect the performance of DSS users.

Table 4  
ANOVA tests of between-subjects effects on decision performance

<table><tr><td>Source</td><td>Type III sum of squares</td><td>d.f.</td><td>Mean square</td><td>F</td><td>Significance</td><td>Partial  $\eta^2$ </td><td>Noncent. parameter</td><td>Observed powera</td></tr><tr><td>Corrected model</td><td> $44.767^b$ </td><td>5</td><td>8.95</td><td>3.34</td><td>0.00</td><td>0.17</td><td>16.69</td><td>0.88</td></tr><tr><td>Intercept</td><td>2044.900</td><td>1</td><td>2044.90</td><td>762.30</td><td>0.00</td><td>0.90</td><td>762.30</td><td>1.00</td></tr><tr><td>Database</td><td>36.067</td><td>2</td><td>18.03</td><td>6.72</td><td>0.00</td><td>0.14</td><td>13.45</td><td>0.90</td></tr><tr><td>Task</td><td>8.100</td><td>1</td><td>8.10</td><td>3.02</td><td>0.09</td><td>0.04</td><td>3.02</td><td>0.40</td></tr><tr><td>Database* task</td><td>0.600</td><td>2</td><td>0.30</td><td>0.11</td><td>0.89</td><td>0.00</td><td>0.22</td><td>0.06</td></tr><tr><td>Error</td><td>225.333</td><td>84</td><td>2.68</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total</td><td>2315.000</td><td>90</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Corrected total</td><td>270.100</td><td>89</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

(<sup>\*</sup>) Signifies the interaction effect between Database and Task. The ANOVA test was conducted at the significance level of 0.05.  
<sup>a</sup> Computed using $\alpha = 0 . 0 5 .$  
<sup>b</sup> R<sup>2</sup> = 0.166 (adjusted $R ^ { 2 } = 0 . 1 1 6 )$

Table 5  
Post hoc tests for DSS database characteristics on decision performance (the Scheffe´ method)

<table><tr><td rowspan="2">(I) DSS database characteristics</td><td rowspan="2">(J) DSS database characteristics</td><td rowspan="2">Mean difference (I-J)</td><td rowspan="2">S.E.</td><td rowspan="2">Significance</td><td colspan="2">95% Confidence interval</td></tr><tr><td>Lower Bound</td><td>Upper Bound</td></tr><tr><td rowspan="2">Traditional DSS database</td><td>DSS database with long-history</td><td>-0.97</td><td>0.42</td><td>0.08</td><td>-2.02</td><td>0.09</td></tr><tr><td>DSS database with long-history and aggregated data</td><td> $-1.53^a$ </td><td>0.42</td><td>0.00</td><td>-2.59</td><td>-0.48</td></tr><tr><td rowspan="2">DSS database with long-history</td><td>Traditional DSS Database</td><td>0.97</td><td>0.42</td><td>0.08</td><td>-0.09</td><td>2.02</td></tr><tr><td>DSS database with long-history and aggregated data</td><td>-0.57</td><td>0.42</td><td>0.41</td><td>-1.62</td><td>0.49</td></tr><tr><td rowspan="2">DSS database with long-history and aggregated data</td><td>Traditional DSS database</td><td> $1.53^a$ </td><td>0.42</td><td>0.00</td><td>0.48</td><td>2.59</td></tr><tr><td>DSS database with long-history</td><td>0.57</td><td>0.42</td><td>0.41</td><td>-0.49</td><td>1.62</td></tr></table>

## 5.1. Post hoc tests

Since the overall mean differences of decision performance among the groups (traditional versus DW) were statistically significant, a post hoc test was carried out to identify which differences contributed. The Scheffe´ method was used, since it is the most conservative with respect to Type I error [27]. The results of the tests are summarized in Table 5.

The results of these tests show, at the significance level of 0.05, that only the mean difference between traditional and database with long-time history and aggregation was statistically significant. Although improvement was expected for decision performance by adding long-term data, the increase was not statistically significant; improvement was achieved only when both long-time history and aggregated data were available.

## 5.2. Discussion of the findings

The major finding was that the adoption and use of a fully capable data warehouse (including both long history and aggregated data) improved DSS users decision performance (see Table 6). This result was consistent with the fundamental idea of the IS success model: improving system and/or information quality will improve individual performance. It also demonstrated that Huber’s conceptual theory was valid in data warehousing and DSS contexts.

Support for Hypothesis 1 indicated that improving system quality did indeed enhance decision maker performance. The result of testing Hypothesis 1a indicated that for the decision task employed, availability and aggregated data significantly improved the performance of DSS analysts. Peterson and Beach [45] argued that man is an ‘‘intuitive statistician’’ who seeks to behave optimally. When given a long sequence of data elements, decision makers usually made more accurate estimates and predictions of future events than when given summarized data [18]. Peterson and Beach also argued that larger samples tend to permit decision makers a better sense of the population.

Table 6  
Summary of hypotheses testing

<table><tr><td>Hypothesis</td><td>Significance</td><td>Evaluation</td></tr><tr><td>H1</td><td>0.00</td><td>Supported $^{a}$ </td></tr><tr><td>H1a</td><td>0.00</td><td>Supported $^{a}$ </td></tr><tr><td>H1b</td><td>0.41</td><td>Rejected</td></tr><tr><td>H1c</td><td>0.08</td><td>Rejected</td></tr><tr><td>H2</td><td>0.09</td><td>Rejected</td></tr></table>

<sup>a</sup> Supported at the 0.05 level.

The results of testing Hypothesis 1b and 1c suggested that, for the decision task, providing longtime data alone did not significantly improve the performance of decision makers. Time was not a variable of interest in this study and data analysis showed no statistically significant difference in the time among the three treatment groups (Table 7). Those decision makers provided with the DSS database with long-history only spent about 10% more time (35 min) in solving the task than those subjects provided with both long-history and aggregated data (31.5 min) (Table 8). Thus, it can be inferred that the difference in decision performance could not be attributable to the time constraints.

## 5.3. Implications of the research findings

Previous research on data warehousing has not shown their effectiveness in an application areas. Findings of this study showed that data warehousing can have a positive impact on decision making. Relatively little attention has been paid to the effects of individual DSS components on decision performance. The study found that improving the quality of the DSS by adding a DW can improve information availability and quality and enhance DSS users decision performance.

ANOVA tests of between-subjects effects on time required in completing decision task

<table><tr><td></td><td>Sum of squares</td><td>d.f.</td><td>Mean square</td><td>F</td><td>Significance</td></tr><tr><td>Between groups</td><td>174.82</td><td>2</td><td>87.41</td><td>1.97</td><td>0.15</td></tr><tr><td>Within groups</td><td>3888.30</td><td>87</td><td>44.69</td><td></td><td></td></tr><tr><td>Total</td><td>4063.12</td><td>89</td><td></td><td></td><td></td></tr></table>

Table 8  
Descriptive statistics for time in completing decision task

<table><tr><td rowspan="2"></td><td rowspan="2">N</td><td rowspan="2">Mean</td><td rowspan="2">S.D.</td><td rowspan="2">S.E.</td><td colspan="2">95% Confidence interval for mean</td><td rowspan="2">Minimum</td><td rowspan="2">Maximum</td></tr><tr><td>Lower bound</td><td>Upper bound</td></tr><tr><td>Traditional DSS database</td><td>30</td><td>33.43</td><td>8.66</td><td>1.58</td><td>30.20</td><td>36.67</td><td>10.00</td><td>40.00</td></tr><tr><td>DSS database with long-history</td><td>30</td><td>34.87</td><td>5.70</td><td>1.04</td><td>32.74</td><td>36.99</td><td>17.00</td><td>40.00</td></tr><tr><td>DSS database with Long-history and aggregated data</td><td>30</td><td>31.47</td><td>5.16</td><td>0.94</td><td>29.54</td><td>33.39</td><td>19.00</td><td>40.00</td></tr><tr><td>Total</td><td>90</td><td>33.26</td><td>6.76</td><td>0.71</td><td>31.84</td><td>34.67</td><td>10.00</td><td>40.00</td></tr></table>

## 5.4. Implications for IS practitioners

Considering the investments made by organizations in DW projects, this technology has become a major user of scarce resources. However, many organizations committed themselves to DW projects with little evidence of a benefit. The findings of this study serve as empirical proof of the effectiveness of DW in business decision making and thus can help organizations determine whether data warehousing is an effective database component in improving decision performance of DSS users.

The findings provide a useful guideline for IT investment in data warehousing and an appropriate implementation strategy: to minimize resource consumption, organizations must identify their needs for different decision tasks and prepare aggregated data.

## 6. Contributions and limitations

This study made two contributions:

1. It is one of the first empirical studies that examined the effects of data warehousing on decision performance. Previous research has provided no empirical evidence of its effectiveness in DSS contexts. My findings are empirical evidence that can provide an understanding of the impact of data warehousing on decision performance.

2. It applied the fundamental ideas of two well established concepts: the conceptual theory of the effects of advanced IT and the IS success model. The results showed that the basic ideas of these models and theory are still valid in data warehousing and DSS.

This study employed a laboratory experiment. However, levels of the independent variables manipulated for the experiment were arbitrary. Hence the findings may apply only to the specific task used.

A second limitation is that this study used only a small convenience sample of ninety graduate students. Although Remus [47] showed that MBA students are suitable surrogates for managers in an experimental setting, their characteristics may not be the same as real decision makers in marketing.

Also, the volume of data used for the decision tasks was relatively small. Therefore, the findings should not be generalized outside marketing or similar decisions, or to tasks that require an analysis of more transaction data for a longer time period.

A final limitation is that this study used specific tools. Red Brick Data Warehouse is fast in data extraction and manipulation and its interface is userfriendly. Other DSS tools and DW products may not have these characteristics.

IS utilization is a necessary condition for it to have a positive impact on individual performance. Furthermore, user satisfaction is one of the most commonly acknowledged measurements for the success of IS and thus DSS users will not utilize a DW unless they perceive its usefulness in decision making.

## 7. Conclusion

Organizations implement data warehousing as a database component to provide decision makers with a source of more reliable and consistent data for business decision making. The findings reported here indicate that DSS users can improve decision performance by implementing a data warehouse. Providing long-term history of transaction data alone does not add as much value as a full DW.

The findings provide empirical evidence to support the basic concepts of the IS success model that postulates positive impacts of system quality and/or information quality on decision performance through system use. Practitioners can expect to improve the decision performance of DSS users by implementing a data warehouse as a component of DSS. In addition, DSS users can expect to improve their decision performance by enhancing individual components of a DSS, without having to improve all its aspects.

## References

[1] N. Ahituv, S. Neumann, H.N. Riley, Principles of Information Systems for Management, fourth ed., Business and Educational Technologies, 1994 p. 217.

[2] R.J. Aldag, D.J. Power, An empirical assessment of computerassisted decision analysis, Decision Sciences 1986, pp. 572– 589.

[3] F.M. Andrews, G.F. Farris, Time pressure and performance of scientists and engineers: a five-year panel study, Organizational Behavior & Human Performance 8(2), 1971, pp. 185– 200.

[4] I. Benbasat, A.S. Dexter, An experimental study of the human/ computer interface, Communications of the ACM 24(11), 1981, pp. 752–762.

[5] I. Benbasat, A.S. Dexter, Individual differences in the use of decision support aids, Journal of Accounting Research 20(1), 1982, pp. 1–11.

[6] I. Benbasat, A.S. Dexter, P. Todd, An experimental program investigation color-enhanced and graphical information presentation: an integration of the findings, Communications of the ACM 29(11), 1986, pp. 1094–1105.

[7] I. Benbasat, B.R. Nault, An evaluation of empirical research in managerial support systems, Decision Support Systems 6(3), 1990, pp. 203–226.

[8] G.H. Bruggen, A. Smidts, B. Vierenga, Improving decision making by means of a marketing decision support, Management Science 44(5), 1998, pp. 645–658.

[9] W.L. Cats-Baril, G.P. Huber, Decision support systems for illstructured problems: an empirical study, Decision Sciences 18(3), 1987, pp. 350–372.

[10] D. Chakravarti, A. Mitchell, R. Staelin, Judgment-based marketing decision models: an experimental investigation of the decision calculus approach, Management Science 25(3), 1979, pp. 251–263.

[11] L. Chen, K.S. Soliman, Exploring information center’s roles in the use of data warehouses, in: Proceedings of the Fourth Americas Conference on Information Systems, Baltimore, Maryland, August 14–16, 1998, pp. 3–5.

[12] P.C. Chu, J.J. Elam, Decision Process, Task Complexity, and Decision Support System Effectiveness, Ohio State University Working Paper, July 1988.

[13] R.L. Daft, R.H. Lengel, A proposed integration among organizational information requirements, media richness, and structural design, Management Science 32(5), 1986, pp. 554–571.

[14] W.H. DeLone, E.R. McLean, Information systems success: the quest for the dependent variable, Information Systems Research 3(1), 1992, pp. 60–95.

[15] W.H. DeLone, E.R. McLean, DeLone and McLean model of information systems success: a ten-year update, Journal of Management Information Systems 19(4), 2003, pp. 9–30.

[16] G.W. Dickson, G. DeSanctis, D.J. McBride, Understanding the effectiveness of computer graphics for decision support: a cumulative experimental approach, Communications of the ACM 29(1), 1986, pp. 40–47.

[17] B.L. Dos Santos, M.L. Bariff, A study of user interface aids for model-oriented decision support systems, Management Science 34(4), 1988, pp. 461–468.

[18] D.E. Erlick, Absolute judgments of discrete quantities randomly distributed over time, Journal of Experimental Psychology (67) 1964, pp. 475–482.

[19] J. Etezadi-Amoli, A.F. Farhoomand, A structural model of end user computing satisfaction and user performance, Information & Management (30) 1996, pp. 65–73.

[20] C.D. Fisher, Laboratory experiments, in: S.B. Thomas, R. Gerald Ferris (Eds.), Method & Analysis in Organizational Research, Reston Publishing Company, Inc, Reston, Virginia, 1984, pp. 169–185.

[21] J. Ghani, E.J. Lusk, The impact of a change in information representation and a change in the amount of information on decision performance, Human Systems Management 3(4), 1982, pp. 270–278.

[22] D.L. Goodhue, R.L. Thompson, Task-technology fit and individual performance, MIS Quarterly 19(2), 1995, pp. 213–236.

[23] G.A. Gorry, M.S.A. Scott Morton, Framework for management information systems, Sloan Management Review 13(1), 1971, pp. 55–70.

[24] M.D. Goslar, G.I. Green, T.H. Hughes, Decision support systems: an empirical assessment for decision making, Decision Sciences 17(1), 1986, pp. 79–91.

[25] P. Gray, H.J. Watson, Decision Support in the Data Warehouse, Prentice Hall, Upper Saddle River, New Jersey, 1998.

[26] T. Guimaraes, M. Igbaria, Client/server system success: exploring the human side, Decision Sciences 28(4), 1997, pp. 851–875.

[27] J.F. Hair, R.E. Anderson, R.L. Tatham, L. Ronald, W.C. Black, Multivariate Data Analysis, fifth ed., Prentice-Hall International, Inc, 1998.

[28] B.J. Haley, Implementing the Decision Support Infrastructure: Key Success Factors in Data Warehousing, Doctoral dissertation, University of Georgia, 1997.

[29] C. Horrocks, Commentary: making the warehouse work, Computerworld 30(26), 1996, p. DW3.

[30] G.P. Huber, A theory of the effects of advanced information technologies on organizational design, intelligence, and decision making, Academy of Management Review 15(1), 1990, pp. 47–71.

[31] A.M. Hunter, State and local government liability for failing to use reasonably available information and technology in emergency management, Information Society (3) 1985, pp. 313– 326.

[32] W.H. Inmon, Building the Data Warehouse, second ed., John Wiley & Sons, New York, 1996.

[33] S. Isaac, W.B. Michael, Handbook in Research and Evaluation for Education and the Behavioral Sciences, third ed., Educational and Industrial Testing Services, San Diego, CA, 1995.

[34] S.L. Jarvenpaa, The effect of task demands and graphical format on information processing strategies, Management Science 35(3), 1989, pp. 285–303.

[35] T.P. Liang, Critical success factors of decision support systems: an experimental study, Data Base 17(2), 1986, pp. 3–16.

[36] R.G. Little Jr., M.L. Gibson, Identification of factors affecting the implementation of data warehousing, in: Proceedings of the Thirty-Second Annual Hawaii International Conference on System Sciences, Maui, Hawaii, January 5–9, 1999.

[37] H. Lucas, An experimental investigation of the use of computer-based graphics in decision making, Management Science 27(7), 1981, pp. 757–768.

[38] G.J. March, H.A. Simon, Organization, Wiley, New York, 1958.

[39] F.R. McFadden, H.J. Watson, The world of data warehousing: issues and opportunities, Journal of Data Warehousing (1) 1996, pp. 61–71.

[40] S.H. McIntyre, An experimental study of the impact of judgment-based marketing models, Management Science 28(1), 1982, pp. 17–33.

[41] J. Pallant, SPSS Survival Manual, Open University Press, U.K., 2001.

[42] Y.T. Park, Strategic uses of data warehouse: an organization’s suitability for data warehousing, Journal of Data Warehousing 2(1), 1997, pp. 24–33.

[43] Y.T. Park, Justification of data warehousing for dss: a competitive advantage point of view, in: Proceedings of the Fourth Americas Conference on Information Systems, Baltimore, Maryland, August 14–16, 1998, pp. 39–41.

[44] J.W. Payne, Task complexity and contingent processing in decision making: an information search and protocol analysis, Organizational Behavior and Human Performance (16) 1976, pp. 366–387.

[45] C.R. Peterson, L.R. Beach, Man as an intuitive statistician, Psychological Bulletin (68) 1967, pp. 29–46.

[46] D.R. Pieptea, E. Anderson, Price and value of decision support systems, MIS Quarterly 11(4), 1987, pp. 515–528.

[47] W.E. Remus, An empirical test of the use of graduate students as surrogates for mangers in experiments on business decision making, Journal of Business Research 14(1), 1986, pp. 19–25.

[48] A. Rudra, E. Yeo, Key issues in achieving data quality and consistency in data warehousing among large organisations in Australia, in: Proceedings of the Thirty-Second Annual Hawaii International Conference on System Sciences, Maui, Hawaii, January 5–9, 1999.

[49] T. Sakaguchi, M.M. Frolick, A review of the data warehousing literature, Journal of Data Warehousing 2(1), 1997, pp. 34–54.

[50] J.A. Schardt, The enterprise intersection model: a unifying framework for data warehouse development, Journal of Data Warehousing 2(2), 1997, pp. 51–61.

[51] P.B. Seddon, A respecification and extension of the DeLone and McLean model of IS success, Information Systems Research 8(3), 1997, pp. 240–253.

[52] P. Seddon, M.Y. Kiew, A partial test and development of the DeLone and McLean model of IS success, in: Proceedings of the International Conference on Information Systems, Vancouver, Canada (ICIS 94), 1994, pp. 99–110.

[53] B. Shin, An exploratory investigation of system success factors in data warehousing, Journal of the Association for Information Systems (4) 2003, pp. 141–170.

[54] H.A. Simon, The architecture of complexity, General Systems Yearbook (10) 1964, pp. 63–76.

[55] C. Smith, S. Hayne, A distributed system for crisis management, Hawaii International Conference on System Sciences (3) 1991, pp. 72–81.

[56] C. Speier, J.W. Palmer, D. Bergman, Applying business framework analysis to the analysis and design of a data warehouse at Corporate Express, Inc, Journal of Data Warehousing 3(3), 1998, pp. 52–59.

[57] R.H. Sprague, M.J. Watson, Bit by bit: toward decision support systems, California Management Review 22(1), 1974, pp. 60– 67.

[58] B. Stackowiak, Why bad data warehouses happen to good people, Journal of Data Warehouse 2(2), 1997, pp. 33–36.

[59] J.K.H. Tan, I. Benbasat, The effectiveness of graphical presentation for information extraction: a cumulative experimental approach, Decision Sciences 24(1), 1993, pp. 167–191.

[60] S.T. Teo, P.K. Wong, An empirical study of the performance impact of computerized in the retail industry, Omega International Journal of Management Science (26) 1998, pp. 611–621.

[61] P. Todd, I. Benbasat, The use of information in decision making: an experimental investigation of the impact of computer-based decision aids, MIS Quarterly 16(3), 1992, pp. 373– 393.

[62] P. Todd, I. Benbasat, An experimental investigation of the relationship between decision makers, decision aids and decision making effort, Infor 31(2), 1993, pp. 80–100.

[63] R.K. Vierck, Decision support systems: an MIS manager’s perspective, MIS Quarterly 5(4), 1981, pp. 35–48.

[64] H.J. Watson, D. Goodhue, B.H. Wixom, The benefits of data warehousing: why some organizations realize exceptional payoffs, Information & Management 2001, pp. 1–12.

[65] H.J. Watson, B.J. Haley, Data warehousing: a framework and survey of current practices, Journal of Data Warehousing 2(1), 1997, pp. 10–17.

[66] J.F. Weilbach, H.L. Viktor, A data warehouse for policy making: a case study, in: Proceedings of the Thirty-Second Annual Hawaii International Conference on System Sciences, Maui, Hawaii, January 5–9, 1999.

[67] B.H. Wixom, H.J. Watson, Am empirical investigation of the factors affecting data warehousing success, MIS Quarterly 25(1), 2001, pp. 17–41.

[68] H. Zimmer, Data Warehousing: Are You on a Path to Success or Failure? http://www.tekptnr.com/tdwi/lessons/rghtpath.html.

![](/api/attachments/956QGENX/fulltext/images/808d9b4e5a67c7fb764b00dba0c4f1e539db37b69fcdd2076a3a1f9523b5be16.jpg)

Yong-Tae Park is Associate Professor of Information Systems and Decision Sciences at the California State University, Fullerton (CSUF). His current research interests include web-based GDSS, data warehousing, e-commerce strategies, and strategic uses of information systems. Dr. Park teaches systems analysis and design, database, data warehousing, and GIS. He received his Ph.D. from Claremont Graduate University. He was on the faculty at the University of Illinois, Springfield before coming to the CSUF.
