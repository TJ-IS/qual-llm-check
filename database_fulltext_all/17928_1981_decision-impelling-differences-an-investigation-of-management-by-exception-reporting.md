---
otero_id: 17928
otero_key: "X6NVDQ6D"
title: "Decision impelling differences: An investigation of management by exception reporting"
authors: "Phillip Judd; Charles Paddock; James Wetherbe"
year: "1981"
journal: "Information & Management"
doi: "10.1016/0378-7206(81)90032-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision Impelling Differences: An Investigation of Management by Exception Reporting

Phillip Judd

College of Business Administration, University of Houston, Houston, TX 77004, USA

Charles Paddock

College of Business Administration, Arizona State University, Tempe, AZ 85281, USA

and

James Wetherbe

Management Information Systems Research Center, School of Management, University of Minnesota, 93 Blegen Hall, 269 19th Avenua South, Minneapolis, MN 55455, USA

An investigation of management by exception reporting is conducted using practicing managers as subjects. A comparison of exception reporting using absolute variations, percentage variations, and a combination of both indicates that managers should not use exception reports that provide only absolute or percentage criteria. Apparently, a combination of absolute and percentage criteria are required to help managers to make decisions based on variations from norms. The explanation of this behavior is labeled as decision impelling differences.

## 1. Introduction

Keywords: Management by Exception Reporting, Decision Making, Information Requirements Analysis, Information Retrieval, Programmed Decision Making.

![](/api/attachments/X6NVDQ6D/fulltext/images/e90b84bd96e9ae34bd3e6547a8cacae9f6c6b4ac63324dc8c75a45eda2050414.jpg)

Philip Judd is the Director of the Research and Instructional Computing Service at the University of Houston. He is on the faculty in the Executive Development Program and the Executive M.B.A. Program at the University of Houston.

© North-Holland Publishing Company Information & Management 4 (1981) 259–267

One of the useful contributions of computing technology to processing information for decision making is in providing exception reporting. Such reporting is supposed to cause corrective responses on significant variations from the norm while eliminating time consuming review of insignificant variations [3]. Exception reporting allows managers to predefine criteria by which specific exceptions are selected from detailed information. This is usually based upon some type of variation from accepted performance (e.g., a list of out-of-stock items).

A major danger of exception reporting is that only those items meeting selection criteria are included in the report. This assumes that the decision maker defining the selection criteria has properly defined the items to be monitored. If the decision maker fails

![](/api/attachments/X6NVDQ6D/fulltext/images/0669509c41b195131a8443ac164f0b43a44529ad2bd57e0afb87d63d496f4460.jpg)

Charles Paddock is an Assistant Professor in Computer Information Systems at Arizona State University. At present, he is actively engaged in research activities in the area of office automation. He has conducted research in decision support systems for the aerospace, aircraft, and law enforcement sectors.

![](/api/attachments/X6NVDQ6D/fulltext/images/523221407da4ad20268630a8bfe9c691f3f97ea88770d9efedf60e51cab7fbcf.jpg)

Dr. James C. Wetherbe is Director of the Management Information Systems (MIS) Research Center and an Associate Professor of MIS in the School of Management at the University of Minnesota. He has held MIS management and technical positions with several major U.S. corporations. He has directed computer centers and been on the faculty at several universities. He is widely published in MIS journals and is the author of texts on systems analysis and design and MIS management. His primary research interests are in MIS management and systems design.

to consider all pertinent circumstances that might occur, important matters will not be included in the exception report and will likely be overlooked; this compromises the decision making process. On the other hand, if a manager does not discriminate enough, he or she will have to sift through too much detail; this creates additional work and can also compromise the process.

There is evidence that managers have difficulty defining their information needs [1,2,4,8, and 9]. For example, Chervany and Dickson [4] found managers tended to be more comfortable with detail information, even though their decision making performance was better with summary information. Benbasat and Schroeder [2] found that managers unfamiliar with their job tended to ask for irrelevant information. Psychological studies into the nature of human information processing indicate the limitations of humans as information processors and their inability to recognize those limitations [5,12,15–18].

These and other studies indicate that it is incumbent upon the systems designer to work with managers in defining their information requirements. It is usually unwise to simply provide what is requested.

This article explores the analysis and design of exception reporting systems.

## 2. Decision Impelling Difference

In theoretical terms, for information to have economic value it must improve decision making. For a decision to be improved, it (of necessity) must be changed from what it was. Therefore, information must impel the decision maker to change the decision. Some scholars argue that information has value if it reduces uncertainty or increases knowledge, though it does not improve a decision. We acknowledge this argument, but we are defining economic value of information to organizational performance. If one organization takes the same course of action with information as it does without it, the economic consequences are unchanged by the information.

For example, suppose a company is predisposed not to introduce a new product. However the marketing research group is asked to conduct research to assess its market potential. The study reveals that the product should be a success. Management alters its decision and introduces the product. Therefore, the information made a difference. The product is successful with net profits of \$500,000. The value of the information could be argued to be worth \$500,000 less the cost of obtaining the information. If the information from the study did not cause management to alter its decision the information had no economic value.

Of course, it is difficult to know in advance whether or not additional information will improve (by altering) a decision. But, it can be argued that additional information should be acquired if it is likely or at least possible to alter (improve) the current decision posture.

## 2.1. Just Noticeable Difference

An important question is: "At what point will information alter a decision and therefore potentially have value?" Dickhaut and Eggleton [7] and later Davis [6] explored the concept of information altering decisions by applying Weber's Law of just noticeable difference [20]. This is a psychologic law developed to explain person's judgments of physical stimuli, such as the loudness of sounds, heaviness of weights, and brightness of lights. Weber's Law says that the difference or increment that is noticeable is a constant proportion of the physical dimensions of the original stimulus. Thus, if $C$ denotes a criterion and $C$ is the just-noticeable-difference, then:

$$
\frac {\Delta C}{C} = k \text {   for   all   } C.
$$

Essentially, this means a larger difference is required to distinguish between heavier objects, brighter lights, or louder sounds, but the relation is the same. That is, as C changes, $\Delta C$ changes in order to hold k constant.

The application of just noticeable difference to information provides insight into human information processing. However, we are interested not only in noticeable differences in information but in whether or not the difference is significant enough to impel a decision maker to make a new decision. We have coined the term decision impelling difference (DID) to describe the concept under investigation. A DID is defined as a sufficiently significant change to modify a decision.

## 3. Management by Exception Reporting

Management by exception (MBE) reporting makes an excellent application for investigating the DID. Ideally, information included in an exception report should impel a decision maker to take action. Information not included that would have caused action is an error of omission. Information included that would not invoke action is extraneous. The exceptions in an MBE report should be consistent with those that the decision maker would choose from a detailed report. Thus, the selection criteria for an MBE report should approximate as closely as possible those of the decision makers. Though it is unrealistic to develop perfect exception reporting systems, minimizing omission errors and minimizing extraneous information is an important design objective.

Most MBE systems are developed using one of two criteria — percentage variance or absolute variance. Using percentage variance, the decision maker asks for all items that exceed a percentage threshold e.g., a list of all customer accounts that have exceeded their credit limit by more than 10 percent. Using absolute variance, the decision maker asks for all items that exceed a quantity threshold; e.g., a list of all customers whose accounts are 60 days past due.

Evidence indicates that humans are not generally good intuitive statisticians [6]. This leads to the questions:

Do decision makers really get the information they need using either a percentage or absolute selection criteria?

Are decision makers as concerned about a 20 percent variance on £2,000 as they are a 20 percent variance on £200,000?

Are absolute variances of £5,000 the same for a base figure of £50,000 as they are for a base figure of £100,000?

## 4. Research Design

With the preceding questions in mind we conducted an investigation into MBE using a DID framework. Specific research questions formulated were as follows:

• Is percentage variance a reliable criteria for developing MBE systems?

\- Is absolute variance a reliable criteria for developing MBE systems?

\- If either percentage or absolute variance criteria are not reliable criteria for developing MBE Systems what approach should be used?

The use of accounting or financial information has proven effective for a number of information utilization studies $[8,9,13,14]$ ; it was selected as a good, universal application for the purposes of this study. In particular, budget exception reporting was isolated as suitable.

The instrument used in conducting the study consisted of three parts: a scenario, two variance reports, and ranking sheets (see the appendix). The scenario requested the participant to assume the role of a decision maker and to decide which variances listed on the reports were important to investigate. As will be seen, each variance report contained 24 hypothetical cases where actual expenditures exceeded budgeted amounts; the reports presented, in tabular form, budget size, actual expenditure, amount of dollar difference, and percentage difference; budget sizes ranged from \$5,000 to \$175,000; percentage differences ranged from 1% to 11% on one report, and from 1% to 25% on the other. The use of two different reports with different percentage variance ranges were used to see if DID's were range sensitive. Variance amounts were evenly distributed throughout the reports. A column was provided for respondents to indicate which variances were important enough to investigate. Budgets were randomly ordered on each variance report. The ranking sheets were provided so that participants could prioritize those variances which they choose to investigate. There were two ranking sheets — one for each variance report.

Participants in the study consisted of 116 practicing managers holding a variety of positions in diverse industries. They were parttime students in the MBA program at the University of Houston (1979–80).

The study was administered in two parts: discrepancy selection and discrepancy ranking. During discrepancy selection, respondents did not know that they would be asked to rank choices. This approach was taken to minimize consideration of relative importance during the selection process. Once selection was made, participants were asked to rank order the budget discrepancies they had selected.

## 5. Analysis

Subjects were asked to select those budgets they would investigate. By doing so, they were indicating the type of variance they considered critical and thus which should be included in an MBE system for the data in question. This allows for an analysis of their use of percent and absolute variance.

## 5.1. Percent Variance

If percentage variance is a reliable criteria for developing an MBE system, then responses should have met the following criteria:

1. All discrepancies selected for further investigation should have higher percentage differences than those not selected.

2. Discrepancies selected should be ranked in descending order based upon percentage difference.

Failure to meet the first criterion resulted when a subject chose to investigate a variance that had a lower percentage difference than one that was not chosen. This indicated that the subject was using a method other than pure percentages to determine which discrepancies to investigate. Failure to meet the second criterion indicated that the order in which discrepancies would be investigated was determined in some fashion other than on a pure percentage basis.

Of the 116 responses, 102 did not meet one or both of the criteria. At a 1 percent level of significance, a confidence level of the proportion of respondents who chose discrepancies on the basis of percentage (0.12 ± 0.09) indicates that percentage criteria are not likely to approximate a decision maker's actual behavior.

## 5.2. Absolute Variance

The same method used to analyze the percentage variance question was used to analyze the absolute variance question. The two criteria used were:

1. All discrepancies selected for further investigation should have higher absolute values than those not selected.

2. Discrepancies selected should be ranked in descending order based upon absolute values.

As with the percentage variance, failure to meet either criterion indicated that the variances were not chosen purely on the basis of absolute values.

Of the 116 responses, 103 did not meet one or both of the criteria. At the 1 percent level of significance, a confidence interval on the proportion of respondents who chose discrepancies on the basis of absolute value $(0.11 \pm 0.09)$ indicates that absolute value criteria are not likely to approximate decision makers' actual behavior.

## 3.3. DID

Given that neither a single criterion - percentage or absolute - adequately explained decision making behavior, the third research question was addressed: If either percentage of absolute variance are not reliable for developing MBE systems, what approach should be used?

From the evidence of the first two analyses, there is interaction between percentage variance and absolute variance. Close analysis indicated that as the base figures went up, subjects were more sensitive to smaller percentages and as the base figures went down, a larger percentage was required to invoke action. This indicates an inverse relation between the size of the base amount and the size of the percentage required to cause a DID.

In an effort to define actual DIDs for the responses unexplained by percentage or absolute values, a multi-criteria approach using both percentage and absolute criteria was explored. The simplest combination of these parameters, their arithmetic product, resulted in the closest approximation of the participants' DID. That is, $DID = P * A$ , where P = percentage variance and A = absolute variance.

To establish the accuracy of this DID selection criteria (as opposed to percentages or absolute values alone), the 89 responses which represented alternative selection strategies were analyzed. $^{1}$ A separate analysis using percent, absolute, and DID criteria was performed for each of the two variance reports. The first step of the analysis was to obtain the average ranking for the discrepancies chosen for the included responses: Consecutive integers were assigned to the discrepancies listed on each respondent's ranking sheets (by order listed) and then the mean rank for each discrepancy was computed for all respondents. The mean value for a given discrepancy was determined by summing the integers assigned to that discrepancy and divided by the number of respondents who included that discrepancy on their ranking sheet. The average ranking was determined on the basis of these mean values. The second step of the analysis involved plotting this average ranking against the percentage difference, the absolute dollar difference, and the DID. The graphs of the three plots for the 1–11% data are displayed in Figures 1–3, and the three plots for the 1–25% data are displayed in Figures 4–6.

An analysis of these curves was then performed using a least squares curve fit to six different curve types. In all cases, an exponential function $[Y = A(\exp(BX))]$ provided the best approximation. Table 1 presents the index of determination for these curves.

For both variance reports, the closest fit to the exponential function was obtained by using the DID. Absolute variance provides the next best fit and percent variance provides the least. The degree to which the function matches the DID curve indicates the validity of using the DID to represent the selection strategy of those managers who do not base their choice of discrepancies solely on percentages or dollar differences.

![](/api/attachments/X6NVDQ6D/fulltext/images/1573b392ea88a74ce2e8845f9e2d60f0b9457c6220604e20a230a9bab898d8c8.jpg)  
Fig. 1. Plot Using Percent Variance Ranking for 1–11% Report.

![](/api/attachments/X6NVDQ6D/fulltext/images/5b0dc878856d0beadb7ab4286ef9623f3bc72ce88f2145efdb0e7f5f9a792528.jpg)  
Fig. 2. Plot Using Absolute Variance Ranking for 1–11% Report.

![](/api/attachments/X6NVDQ6D/fulltext/images/9c23dd9c9a698f85a8c3dff6d050672185b5cd23001399169f2a3bdaa6b6f6a9.jpg)  
Fig. 3. Plot Using DID Ranking for 1–11% Report.

![](/api/attachments/X6NVDQ6D/fulltext/images/2a4936fb6b3dc82b4b9be631f41804ea8e529b42d0c1df3dd2cdc3f468778e34.jpg)  
Fig. 4. Plot Using Percent Variance Ranking for 1–25% Report.

![](/api/attachments/X6NVDQ6D/fulltext/images/200e8dba12c54429f770941094fff018cd3fd5cf61b5ff901cc9dbf0f662ad4d.jpg)  
Fig. 5. Plot Using Absolute Variance Ranking for 1–25% Report.

![](/api/attachments/X6NVDQ6D/fulltext/images/96949ca91e5ac42c3f1dfa72fc5d49701053745f6a053e875767b078eaa6b787.jpg)  
Fig. 6. Plot Using DID Ranking for 1–25% Report.

Table 1: Index of determination

<table><tr><td rowspan="2"></td><td colspan="2">Index of determination</td></tr><tr><td>1%-11% Report</td><td>1%-25% Report</td></tr><tr><td>Average by Rank vs. Average by Percentage</td><td>0.362</td><td>0.324</td></tr><tr><td>Average Rank vs. Rank by Absolute Value</td><td>0.890</td><td>0.844</td></tr><tr><td>Average Rank vs. Rank by DID</td><td>0.979</td><td>0.974</td></tr></table>

## 6. Discussion of the Findings

The results of this study indicate a need to reexamine the current method of designing exception reporting. Although this study was limited in scope and cannot realistically be applied to all areas of exception reporting, it does demonstrate that in certain situations the majority of decision makers will tend to judge the importance of a variance, not just on its percentage or absolute difference, but rather on a combination of the two via some weighting scheme.

The impact of these findings on management by exception reporting is significant in two ways. First, no single method of determining exceptions will be suitable for all managers. Second, exception reports should include more information than simply a percentage deviation or an absolute value deviation.

For the system designer, these results point out the necessity to exercise judgment in the development of exception reporting systems. Since all managers do not use the same criteria for selecting exceptions, a strong argument can be made for designing a personalized system based on the examination of a decision makers' selection criteria.

A straightforward strategy for designing an MBE for a manager is as follows:

1. Provide the decision maker with a detail report for that data for which an MBE report is to be designed.

2. Ask the decision maker to indicate which detail items to include in the report.

3. Analyze both relationships between the base amount, the absolute variance, and the percentage variance to determine the decision maker's DID for the data in question.

4. Present findings to the decision maker, make modifications if necessary, and

5. Proceed with developing the system.

6. Reevaluate the DID for an MBE report periodically, particularly when a new decision maker is involved.

## 7. Further Research

The lack of published information on the design and implementation of the MBE concept suggests that there is much room for both theoretical and practical research in this area. The study presented in this paper raises a number of questions.

How does MBE inhibit or promote accomplishment of the decision maker's objectives? Assuming that the decision maker's goals are in line with those of the organization (a sometimes tenous assumption), then the fact that he or she may choose different exceptions – or choose the same ones differently – than those provided by some other system is only important if the manner in which MBE is implemented prevents attainment of those goals. If MBE affects the decision making ability of a number of decision makers in the organization, then the performance of the organization itself might be significantly affected.

To answer the above questions, research is needed on how MBE is currently designed and used – both within and across industries, and inside individual organizations. That is, how heavily is it relied upon, and for what purposes?

A second area of investigation is one of devising a framework or methodology for examining MBE application, design, and implementation.

A third question concerns the advisibility and practicality of designing MBE systems, for the individual decision makers versus designing a more general system for use by a group. Is it possible, for instance, to use the same DID criteria for all managers examining budgets in the organization without affecting the quality of individual decision maker's decisions?

Fourth, the emergence of an exponential distribution in the exception selection process may prove an interesting pursuit, especially if it appears to apply in other areas of exception selection (inventory, sales performance, quality control, etc.). In particular, is the DID = P \* A model found relevant to the reports studied in this research, representative of behavior in other applications?

Finally, the deepest research question is why the DID phenomenon functions as it does. This requires protocol analysis of the decision makers as they are selecting and ranking data.

## 8. Conclusion

Decision impelling differences (DID) is a useful concept for describing information as it relates to decision making behavior. It overcomes deficiencies of percent and absolute variance criteria for designing management by exception reporting systems. Further investigation into the characteristics of DID's and decision making can potentially improve decision making in a variety of applications.

## Appendix

## Exception Report Questionnaire

As an executive of a large organization, you requested a report of the managers who exceeded their budget. This report is summarized on the following pages.

Please indicate which (if any) of these budget discrepancies you would want to check into.

Circumstances may prevent you from checking into each discrepancy selected. Therefore, indicate below the order in which you would investigate your choices. Use case numbers and list the cases in descending order (i.e., the first case you would investigate should appear first).

## References

[1] R.L. Ackoff, "Management Misinformation Systems," Management Sciences, December 1967, pp. B147–56.

[2] I. Benbasat and R.G. Schroeder., "An Experimental Investigation of Some MIS Design Variables," MIS Quarterly, Vol. 1, No. 1, March 1977.

Instructions: Place an × in the LAST column next to the discrepancies you would check into.

<table><tr><td>Case number</td><td>Budget</td><td>Actual</td><td>Difference</td><td>Percent difference</td><td>Check into (X)</td></tr><tr><td>1.</td><td>145,000</td><td>155,152</td><td>10,152</td><td>7</td><td>( )</td></tr><tr><td>2.</td><td>110,000</td><td>111,107</td><td>1,107</td><td>1</td><td>( )</td></tr><tr><td>3.</td><td>47,000</td><td>49,356</td><td>2,356</td><td>5</td><td>( )</td></tr><tr><td>4.</td><td>54,000</td><td>58,859</td><td>4,859</td><td>9</td><td>( )</td></tr><tr><td>5.</td><td>159,000</td><td>176,487</td><td>17,487</td><td>11</td><td>( )</td></tr><tr><td>6.</td><td>89,000</td><td>93,450</td><td>4,450</td><td>5</td><td>( )</td></tr><tr><td>7.</td><td>152,000</td><td>153,521</td><td>1,521</td><td>1</td><td>( )</td></tr><tr><td>8.</td><td>68,000</td><td>68,685</td><td>685</td><td>1</td><td>( )</td></tr><tr><td>9.</td><td>103,000</td><td>110,211</td><td>7,211</td><td>7</td><td>( )</td></tr><tr><td>10.</td><td>75,000</td><td>83,244</td><td>8,244</td><td>11</td><td>( )</td></tr><tr><td>11.</td><td>12,000</td><td>13,086</td><td>1,086</td><td>9</td><td>( )</td></tr><tr><td>12.</td><td>5,000</td><td>5,252</td><td>252</td><td>5</td><td>( )</td></tr><tr><td>13.</td><td>124,000</td><td>127,729</td><td>3,729</td><td>3</td><td>( )</td></tr><tr><td>14.</td><td>82,000</td><td>84,454</td><td>2,454</td><td>3</td><td>( )</td></tr><tr><td>15.</td><td>138,000</td><td>150,427</td><td>12,427</td><td>9</td><td>( )</td></tr><tr><td>16.</td><td>26,000</td><td>26,260</td><td>260</td><td>1</td><td>( )</td></tr><tr><td>17.</td><td>33,000</td><td>36,638</td><td>3,638</td><td>11</td><td>( )</td></tr><tr><td>18.</td><td>131,000</td><td>137,547</td><td>6,547</td><td>5</td><td>( )</td></tr><tr><td>19.</td><td>19,000</td><td>20,335</td><td>1,355</td><td>7</td><td>( )</td></tr><tr><td>20.</td><td>117,000</td><td>129,870</td><td>12,870</td><td>11</td><td>( )</td></tr><tr><td>21.</td><td>116,000</td><td>120,982</td><td>4,982</td><td>3</td><td>( )</td></tr><tr><td>22.</td><td>96,000</td><td>104,645</td><td>8,645</td><td>9</td><td>( )</td></tr><tr><td>23.</td><td>61,000</td><td>65,271</td><td>4,271</td><td>7</td><td>( )</td></tr><tr><td>24.</td><td>40,000</td><td>41,191</td><td>1,191</td><td>3</td><td>( )</td></tr></table>

Instructions: Place an x in the LAST column next to the discrepancies you would check into.

<table><tr><td>Case number</td><td>Budget</td><td>Actual</td><td>Difference</td><td>Percent difference</td><td>Check into (×)</td></tr><tr><td>1.</td><td>5,000</td><td>6,257</td><td>1,257</td><td>25</td><td>( )</td></tr><tr><td>2.</td><td>152,000</td><td>167,222</td><td>15,222</td><td>10</td><td>( )</td></tr><tr><td>3.</td><td>103,000</td><td>118,459</td><td>15,459</td><td>15</td><td>( )</td></tr><tr><td>4.</td><td>12,000</td><td>14,460</td><td>2,460</td><td>20</td><td>( )</td></tr><tr><td>5.</td><td>19,000</td><td>21,851</td><td>2,851</td><td>15</td><td>( )</td></tr><tr><td>6.</td><td>68,000</td><td>74,814</td><td>6,814</td><td>10</td><td>( )</td></tr><tr><td>7.</td><td>159,000</td><td>166,954</td><td>7,954</td><td>5</td><td>( )</td></tr><tr><td>8.</td><td>40,000</td><td>40,400</td><td>400</td><td>1</td><td>( )</td></tr><tr><td>9.</td><td>47,000</td><td>58,752</td><td>11,752</td><td>25</td><td>( )</td></tr><tr><td>10.</td><td>54,000</td><td>64,891</td><td>10,891</td><td>20</td><td>( )</td></tr><tr><td>11.</td><td>26,000</td><td>28,626</td><td>2,626</td><td>10</td><td>( )</td></tr><tr><td>12.</td><td>33,000</td><td>34,651</td><td>1,651</td><td>5</td><td>( )</td></tr><tr><td>13.</td><td>82,000</td><td>82,820</td><td>820</td><td>1</td><td>( )</td></tr><tr><td>14.</td><td>117,000</td><td>122,853</td><td>5,853</td><td>5</td><td>( )</td></tr><tr><td>15.</td><td>110,000</td><td>121,012</td><td>11,012</td><td>10</td><td>( )</td></tr><tr><td>16.</td><td>131,000</td><td>163,752</td><td>32,752</td><td>25</td><td>( )</td></tr><tr><td>17.</td><td>89,000</td><td>111,257</td><td>22,257</td><td>25</td><td>( )</td></tr><tr><td>18.</td><td>61,000</td><td>70,156</td><td>9,156</td><td>15</td><td>( )</td></tr><tr><td>19.</td><td>166,000</td><td>167,662</td><td>1,662</td><td>1</td><td>( )</td></tr><tr><td>20.</td><td>96,000</td><td>115,213</td><td>19,213</td><td>20</td><td>( )</td></tr><tr><td>21.</td><td>124,000</td><td>125,246</td><td>1,246</td><td>1</td><td>( )</td></tr><tr><td>22.</td><td>145,000</td><td>166,752</td><td>21,752</td><td>15</td><td>( )</td></tr><tr><td>23.</td><td>138,000</td><td>165,638</td><td>27,638</td><td>20</td><td>( )</td></tr><tr><td>24.</td><td>75,000</td><td>78,752</td><td>3,752</td><td>5</td><td>( )</td></tr></table>

[3] F. Collins, "Cost Exception Alerting Techniques," Journal of Systems Management, November 1977, pp. 31–33.

[4] N.L. Chervany and G.W. Dickson, "An experimental Evaluation of Information Overload in a Production Environment," Management Sciences, June 1974, pp. 1355–44.

[5] R. Conrad, "Errors of Immediate Memory," The British Journal of Psychology, November 1959, pp. 349–359.

[6] G.B. Davis, Management Information Systems: Conceptual Foundations, Structure and Development, New York: McGraw Hill, 1974.

[7] J. Dickhaut and V. Eggleton, "An Application of Weber's Law in an Accounting Setting," Proceedings of the 4th Annual Midwest AIDS Regional Conference, April 1972, pp. 515–518.

[8] J.D. Dermer, "Cognitive Characteristics and the Perceived Importance of Information," The Accounting Review, July 1973, pp. 511–19.

[9] M.J. Driver and T.J. Mock, "Human Information Processing Decision Style Theory, and Accounting Information Systems," The Accounting Review, July 1975, pp. 490–507.

[10] A.M. Jenkins, "A Framework for MIS Research," Proceedings of the Ninth Annual Conference American Institute for Decision Sciences, Chicago, October 1977, p. 573.

[11] E. McClean, "Find Users as Application Developers," MIS Quarterly, Vol. 3, No. 4, December 1979, pp. 37–45.

[12] G.A. Miller, "The Magic Number Seven Plus or Minus Two: Some Limits on Our Capacity for Processing Information," Psychological Review, 1956, pp. 81–97.

[13] H. Miller, "Environmental Complexity and Financial Reports," The Accounting Review, January 1972, pp. 31–7.

[14] T.J. Mock., "The Value of Budget Information," The Accounting Review, July 1973, pp. 520–34.

[15] A. Newell and H.A. Simon, Human Problem Solving, Prentice Hall, Inc., Englewood Cliffs, New Jersey, 1972.

[16] H.A. Simon and A. Newell, "Human Problem Solving: The State of the Art in 1970," American Psychologist, Vol. 26, February 1971, pp. 145-149.

[17] S. Streufert, P. Swedfeld and M.J. Driver, "Conceptual Structure, Information Search and Information Utilization," Journal of Applied Psychology and Social Psychology, 1965, pp. 736–40.

[18] A. Tuersky and Kahneman, "The Belief in the Law of Small Numbers," Psychological Bulletin, Vol. 76, 1971, pp. 105–110.

[19] James C. Wetherbe, System Analysis for Computer-Based Information Systems, St. Paul: West Publishing, 1979.

[20] R.S. Woodworth and Schlosberg, Experimental Psychology, Rev. Ed., Henry Holt and Company, Inc., New York, 1955, pp. 192–233.
