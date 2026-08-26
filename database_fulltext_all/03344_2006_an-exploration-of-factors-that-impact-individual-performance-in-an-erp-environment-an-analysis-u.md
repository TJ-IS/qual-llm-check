---
otero_id: 3344
otero_key: "ST5JDSGP"
title: "An exploration of factors that impact individual performance in an ERP environment: an analysis using multiple analytical techniques"
authors: "Boontaree Kositanurit; Ojelanki Ngwenyama; Kweku-Muata Osei-Bryson"
year: "2006"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000654"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An exploration of factors that impact individual performance in an ERP environment: an analysis using multiple analytical techniques

Boontaree Kositanurit<sup>1</sup>, Ojelanki Ngwenyama<sup>2</sup> and Kweku-Muata Osei-Bryson<sup>3</sup>

<sup>1</sup>Fiscal Policy Office, Information and Communication Technology Center, Ministry of Finance, Thailand; <sup>2</sup>Research Institute for Tfechnology Management and Organizational Learning, School of Information Technology Management, Ryerson University, Toronto, Canada; <sup>3</sup>Department of Information Systems and The Information Systems Research Institute, Virginia Commonwealth University, Richmond, VA, U.S.A.

## Correspondence:

Ojelanki Ngwenyama, Research Institute for Technology Management and Organizational Learning, School of Information Technology Management, Ryerson University, 350 Victoria Street, Toronto, Canada M5B 2K3. Tel: þ 1 416 979 5000 ext. 4203; E-mail: ojelanki@ryerson.ca

## Abstract

This study explores the factors that can impact individual performance when using enterprise resource planning (ERP) systems. Starting from the proposition that organizational performance depends on individuals’ task accomplishments, we test a structural model of task–technology fit, ERP user satisfaction, and individual performance in ERP environments. This research utilizes a survey method to examine the perceptions of ERP users. We performed factor and reliability analyses to assess the validity of the survey instrument. Six factors were identified as having an impact on individual performance: System Quality, Documentation, Ease of use, Reliability, Authorization, and Utilization. To explore the relationships among these factors, we conducted regression and multivariate adaptive regression splines analysis, and compared the findings from these two analytical techniques. The study provides evidence that System Quality, Utilization, and Ease of Use are the most important factors bearing on individual performance in ERP environments. Our findings also provide IT managers and researchers with knowledge of how these factors can be manipulated to improve individual performance when using ERP systems. European Journal of Information Systems (2006) 15, 556–568. doi:10.1057/palgrave.ejis.3000654

Keywords: ERP; user performance; task–technology fit; regression splines

## Introduction

A recent survey by Robbins-Gioia LLC, finds that more than 50% of organizations implementing enterprise resource planning (ERP) systems were not satisfied with their performance (http://www.robbinsgioia.com/ news\_events/012802\_erp.aspx). Various prescriptions for improving organizational performance from ERP implementations have been put forward, including the following three: (1) standardize business practices to fit with the ERP software (Summer, 1999; Kremers & Dissel, 2000; Markus & Tanis, 2000; Palaniswamy & Frank, 2000); (2) avoid customizing the software (Parr & Shanks, 2000; Mabert et al., 2001; Murray & Coffin, 2001); and (3) provide appropriate training in the use of the system (Bingi et al., 1999; Summer, 1999; Al-Mudimigh et al., 2001). Although there has been much discussion and conjecture about what leads to good performance of ERP systems in organizations, further research is needed to understand the factors affecting individual performance in the use of ERP systems in organizations.

Many have investigated end-user performance with information systems, as can be seen from Table 1.

Table 1 Studies relating to end-user performance

<table><tr><td>Focus of the study</td><td>Method of data collection</td><td>Method of data analysis</td><td>Citations</td></tr><tr><td>TTF: the effect of task demands and graphical format on information processing strategies</td><td>Experiment</td><td>ANOVA</td><td>Jarvenpaa (1989)</td></tr><tr><td>TTF: the fit between job and PC capabilities</td><td>Surveys (questionnaires)</td><td>Partial least-square analysis</td><td>Thompson et al. (1991)</td></tr><tr><td>TTF: computer graphs and fit with question types and question complexity levels</td><td>Laboratory experiment</td><td>Two-way analysis of variance and Wilcoxon matched pairs signed-ranks test</td><td>Wilson &amp; Addo (1994)</td></tr><tr><td>TTF</td><td>Surveys (questionnaires)</td><td>Regression analysis</td><td>Goodhue (1995)</td></tr><tr><td>TTF: model validation</td><td>Surveys (questionnaires)</td><td>Regression analysis</td><td>Goodhue &amp; Thompson (1995)</td></tr><tr><td>TTF</td><td>Surveys (questionnaires)</td><td>Establishing instrument validity</td><td>Goodhue (1998)</td></tr><tr><td>TTF</td><td>Laboratory experiment</td><td>Regression analysis</td><td>Mathieson &amp; Keil (1998)</td></tr><tr><td>TTF and fitness-for-use (FFU)</td><td>Surveys (questionnaires)</td><td>Regression analysis and path analysis</td><td>Dishaw &amp; Strong (1998)</td></tr><tr><td>TTF and TAM</td><td>Surveys (questionnaires)</td><td>Path analytic technique</td><td>Dishaw &amp; Strong (1999)</td></tr><tr><td>TTF</td><td>Experiment and questionnaire</td><td>Regression analysis and logistic regression</td><td>Goodhue et al. (2000)</td></tr><tr><td>TTF: CASE-task fit and software developer&#x27;s performance</td><td>Surveys (questionnaires)</td><td>Hierarchical regression analysis</td><td>Lai (1999)</td></tr><tr><td>User satisfaction</td><td>Surveys (questionnaires)</td><td>Measurement development</td><td>Bailey &amp; Pearson (1983)</td></tr><tr><td>User satisfaction</td><td>Surveys (questionnaires)</td><td>Measurement development</td><td>Ives et al. (1983)</td></tr><tr><td>User satisfaction</td><td>Surveys (questionnaires)</td><td>Measurement development</td><td>Doll &amp; Torkzadeh (1988)</td></tr><tr><td>User satisfaction</td><td>Surveys (questionnaires)</td><td>Establishing instrument validity</td><td>Torkzadeh &amp; Doll (1991)</td></tr><tr><td>User satisfaction</td><td>Surveys (questionnaires)</td><td>Establishing instrument validity</td><td>Doll et al. (1994)</td></tr><tr><td>User satisfaction</td><td>Surveys (questionnaires)</td><td>Establishing instrument validity</td><td>Hendrickson et al. (1994)</td></tr><tr><td>User satisfaction</td><td>Surveys (questionnaires)</td><td>Establishing instrument validity, structural equation model, regression analysis</td><td>Etezadi-Amoli &amp; Farhoo-mand (1996)</td></tr><tr><td>User satisfaction</td><td>Surveys (questionnaires)</td><td>Partial least-square testing</td><td>Igbaria &amp; Tan (1997)</td></tr><tr><td>User satisfaction</td><td>Surveys (questionnaires)</td><td>Structural equation based on partial least square</td><td>Blili &amp; Rivard (1998)</td></tr><tr><td>User satisfaction and TAM</td><td>Surveys (questionnaires)</td><td>Structural equation model using LISREL</td><td>Al-Gahtani &amp; King (1999)</td></tr><tr><td>User satisfaction</td><td>Surveys (questionnaires) and observation through meta-monitoring system analysis that automatically, tracked and recorded users&#x27; activities</td><td>Z-tests</td><td>Downing (1999)</td></tr></table>

This body of literature can be divided into two types of inquiry: (1) task–technology fit (TTF) studies and (2) user satisfaction studies. Each category approaches the problem of end-user performance from a different perspective. The TTF approach postulates that when the user’s task and the technology are congruent, user performance will be high (Goodhue, 1995; Goodhue & Thompson, 1995; Dishaw & Strong, 1998; Mathieson & Keil, 1998). Consequently, studies falling under this approach try to define task and technology characteristics, and what is ‘goodness of fit’ between specific technologies and enduser tasks (Dishaw & Strong, 1998; Mathieson & Keil, 1998; Goodhue et al., 2000). In contrast, user satisfaction studies investigate the extent to which certain information systems properties, such as system quality, information quality, system use, and user satisfaction influence user performance (Bailey & Pearson, 1983; Doll & Torkzadeh, 1988). Numerous user satisfaction studies have been conducted in the last decade that attempt to identify factors of information systems that lead to high user performance (Torkzadeh & Doll, 1991; DeLone & McLean, 1992; Doll et al., 1994; Hendrickson et al., 1994).

Starting from the proposition that organizational performance depends on tasks accomplished by individuals, we investigate a structural model of TTF, ERP user satisfaction, and individual performance in ERP environments. We start from the two well-known research streams of TTF and User Satisfaction to explore factors that might influence individual performance when using ERP systems.

## Task–technology fit

Several researchers have used the TTF model to explain the impact of IS and task characteristics on individual performance (Goodhue & Thompson, 1995; Dishaw & Strong, 1998; Ferratt & Vlahos, 1998). This model supports the argument that when there is a fit between user task characteristics and characteristics of the IS, utilization of the system will be high and user performance will be high. Goodhue & Thompson (1995) find support for the relationships TTF and Performance, and Utilization and Performance. They find moderate support for the relationships Task Characteristics and TTF, and Technology Characteristics and TTF, and no support for the relationship TTF and Utilization, as can be seen from Figure 1. The specific IS properties/technology characteristics they tested for were, Information Quality, Locatability, Authorization, System Reliability, and Ease of Use. Although the TTF model does not answer the question of what characteristics of IS lead to the highest levels of user performance, it suggests some constructs that are relevant to investigation.

![](/api/attachments/ST5JDSGP/fulltext/images/71f90e6110534b9e5728e971d8bfa77a11ff83fbd2886a408778f9da05208185.jpg)  
Figure 1 The TTF model proposed and tested by Goodhue & Thompson (1995). Note: the relationships in the dotted lines are moderately ( ) or not ( ) supported.

## User satisfaction and performance

The second category of studies, User Satisfaction, focuses on identifying the conditions under which users are satisfied with the systems they use. Doll & Torkzadeh (1988) define User Satisfaction as the user’s opinion of a particular computer application that s/he uses. The fundamental argument of this approach is that high levels of user satisfaction lead to high levels of user performance. In an earlier study, Bailey & Pearson (1983) conducted a literature review to identify influencing factors and developed a questionnaire for investigating User Satisfaction. Ives et al. (1983) replicated and extended Bailey & Pearson’s (1983) study to provide evidence of the validity of the instrument. Reliability, content validity, predictive validity, and construct validity were tested. Doll & Torkzadeh (1988) also developed an instrument that would measure end-user computing satisfaction. This instrument included several constructs relating to IS properties such as information content, format, accuracy, and ease of use.

These early works paved the way for other studies that linked the constructs of user satisfaction, system characteristics, and user performance. Some of this research has also focused specifically on clarifying and confirming the relationship between user satisfaction and end-user performance (DeLone & McLean, 1992). This argument is also the central point of the nomological net model of Igbaria & Tan (1997). In another important study, DeLone & McLean (1992) validate the constructs, system quality, information quality, use, user satisfaction, and individual and organizational performance. Later, Etezadi-Amoli & Farhoomand (1996) develop a questionnaire instrument and tested the relationship between end-user satisfaction and user performance, also validating the three constructs of System Documentation, Functionality, and Ease of Use.

## Theoretical foundation and research hypotheses

The literature on TTF, user satisfaction, and performance offers a rich set of validated constructs for gathering data relating to IS properties and user performance. Put forward in this paper is the first attempt to utilize these studies to explain individual performance in an ERP environment. We use these prior studies and their inventory of validated constructs as a starting point for this investigation. The research question below places this study at the intersection of TTF and User Performance studies, because both areas of research theorize the constructs common to both, namely, ‘IS characteristics’ and, ‘user performance’, as can be seen from the review of the literature presented earlier in this paper. We began with the hypothesis that an integrated model (see Figure 2) of TTF and ERP User Satisfaction can be used to explain individual performance in an ERP environment.

However, after exploratory factor analysis showed that there were overlaps between the theoretical constructs of the TTF and User satisfaction, we revised our research hypothesis (we discuss the exploratory factor analysis later) in order to explore factors that might influence individual performance in ERP environments. There are now two hypotheses. One, each of the six factors (System Quality, Documentation, Ease of Use, System Reliability, Authorization, and Utilization) is a predictor of individual performance in the User Satisfaction ERP environment. Two, each of the five factors (System Quality, Documentation, Ease of Use, System Reliability, and Authorization) is a predictor of system utilization in the User Satisfaction ERP environment.

## Research methodology

A survey instrument<sup>1</sup> was developed and responses were gathered by way of an on-line survey. Details of these are described below. To analyze the data, we used (a) factor analysis; (b) regression analysis; (c) regression splines (RS) analysis; and (d) comparison of results of regression analysis and RS analysis. Recently, Bauer & Kohavi (1999) demonstrated that, for some data sets, a combination of predictive models can offer better explanations than any of the individual models. On this account, we use two analytical techniques: regression and multivariate adaptive RS (MARS), to test the model. It should be noted that although RS analysis has been used only recently in mainstream information systems research (Ko & Osei-Bryson, 2004), it has been successfully applied in various fields including software engineering (e.g. Briand et al., 2002), electrochemistry (e.g. Carey & Yee, 1992), geography (e.g. Abraham & Steinberg, 2001), communication (e.g. Ekman & Kubin, 1999), chemical studies (e.g. Nguyen-Cong et al., 1996), cancer research (e.g. Mallick et al., 1997), genetics (York & Eaves, 2001), engineering (e.g. Jin et al., 2001), geochemistry (e.g. Griffin et al., 1997), epidemiology (e.g. Kuhnert et al., 2000), and finance (e.g. Abraham, 2002).

## Development of the survey instrument

The three well-known measurement instruments were integrated and refined to measure different aspects of factors that have impacts on individual performance in an ERP environment. They are (1) the TTF instrument of Goodhue & Thompson (1995); (2) the user satisfaction instrument of Etezadi-Amoli & Farhoomand (1996); and (3) the user satisfaction instrument of Doll & Torkzadeh (1988). Demographic and support information items (e.g. types of industry, education level of users, and users’ familiarity with the systems they use) were also added to the questionnaire. Three panels of experts reviewed the resulting questionnaire. Comprising two Ph.D. students and two practitioners, the first panel reviewed the first draft of the questionnaire. The second panel included two practitioners who, together with a researcher, separately analyzed each of the questions in the shortened version to determine the validity for the TTF instrument of Goodhue and Thompson. The third panel comprised five professors, two Ph.D. students, and two practitioners who conducted the final review of the questionnaire. After the final review, a pilot study was conducted on a small focus group of 10 participants who were working in an ERP environment. The feedback from the pilot study was then incorporated into the final questionnaire instrument. The questionnaire items are provided in Appendix A.

## Data collection

The authors conducted an on-line survey during the period April–August 2003. We obtained 349 respondents, which is 78.96% of the users who visited the website.

![](/api/attachments/ST5JDSGP/fulltext/images/da74d606ec74b6cb2f8fdfca8fb9e1bbcc209ea83ec37d25ac89fad3edf5e269.jpg)  
Figure 2 A structural model of TTF, ERP User Satisfaction, and Individual Performance Impact.

Of these, 255 respondents are ERP users with 85% response rate and 94 respondents are non-ERP users with 66.19% response rate. The participants were from 15 U.S. organizations: 12 who responded to the ERP survey; two who responded to both the ERP and non-ERP surveys; and one who responded to the non-ERP survey. Responses classified by industry type and by managerial level are presented in Tables 2 and 3, respectively. It should be noted that while respondents to our survey consisted of both ERP users and non-ERP users, the explanatory models presented later in this paper are based on the analysis of responses from ERP users only (Appendix B).

## Analysis and results

## Factor analysis

In order to identify interpretable groupings of questionnaire items, we conducted factor analysis (separately) for the independent and dependent variables. We conducted several iterations of factor analyses; Appendix C provides a detailed description of the analysis and results and Table 4 provides a summary of the results of our factor analysis. Both Utilization and Individual Performance are dependent variables in this study. However, Utilization is also an independent variable for Individual Performance. Thus, we performed factor analyses separately for Individual Performance items and Utilization items. Items from Individual Performance (i.e., PERFO1, PERFO2, PERFO3) were loaded together into one factor with 81.79% total variance explained. Items from Utilization were loaded together into one factor with 28% total variance explained. Table 4 below shows the reliability measures for the various questionnaire items.

Table 2 Responses classified by industry type

<table><tr><td rowspan="2">Industry</td><td colspan="3">Number of responses</td></tr><tr><td>ERP</td><td>Non-ERP</td><td>Total</td></tr><tr><td>Financial service provider</td><td>13</td><td>16</td><td>29</td></tr><tr><td>Health care</td><td>15</td><td>0</td><td>15</td></tr><tr><td>Higher education and research</td><td>101</td><td>67</td><td>168</td></tr><tr><td>Insurance</td><td>6</td><td>0</td><td>6</td></tr><tr><td>Manufacturing</td><td>9</td><td>0</td><td>9</td></tr><tr><td>Oil and gas</td><td>12</td><td>0</td><td>12</td></tr><tr><td>Public sector</td><td>23</td><td>0</td><td>23</td></tr><tr><td>Retail</td><td>28</td><td>11</td><td>39</td></tr><tr><td>Telecommunication</td><td>1</td><td>0</td><td>1</td></tr><tr><td>Utilities</td><td>47</td><td>0</td><td>47</td></tr><tr><td>Total responses</td><td>255</td><td>94</td><td>349</td></tr></table>

Note: In those cases that an enterprise conducts business in many areas, the business can be assigned to more than one industry.

Table 3 Responses of ERP users classified by managerial level

<table><tr><td>Managerial level</td><td>Number of responses</td></tr><tr><td>Operations</td><td>116</td></tr><tr><td>First-line supervisor or manager</td><td>57</td></tr><tr><td>Mid-level manager (supervising other managers)</td><td>33</td></tr><tr><td>Executive (top) level manager (Vice president, President, Chairman of the Board of Directors, etc.)</td><td>5</td></tr><tr><td>Others</td><td>36</td></tr><tr><td>Missing values</td><td>8</td></tr><tr><td>Total responses</td><td>255</td></tr></table>

## Regression analysis

After validating the questionnaire items, we conducted stepwise regression analyses (separately) on Individual Performance and Utilization as dependent variables. Here we find that System Quality, Ease of Use, and Utilization are positive predictors of individual performance with an Adjusted $R ^ { 2 }$ of 0.733, and System Quality, Documentation and Ease of Use are positive predictors of Utilization with an adjusted $R ^ { 2 }$ of 0.405 (see Table 5). However, since Utilization works as the mediator between the independent (variables) factors and Individual Performance, the mediation testing recommended by Baron & Kenny (1986) was also performed to confirm that Utilization is a mediator.

According to Baron & Kenny (1986), mediation can be tested by estimating the regression equations. The following conditions should be present if mediation exists between an independent variable and the dependent variable:

1. The given independent variable (i.e., System Quality, Ease of Use, Documentation) has a statistically significant effect on Utilization, the mediator.

Table 4 Summary results of factor analysis on independent variables

<table><tr><td rowspan="2">Construct</td><td colspan="2">Questionnaire items</td><td rowspan="2">Reliability (alpha)</td></tr><tr><td>Original instrument</td><td>Item</td></tr><tr><td rowspan="3">System quality</td><td>TTF</td><td>Currency (CURR)Right Level of Detail (RDETAIL)Meaning (MEAN)</td><td>0.9603</td></tr><tr><td>UIS (Doll &amp; Torkzadeh)</td><td>Content (CONT1, CONT2, CONT3, CONT4)Accuracy (ACCU1, ACCU2)Format (FOR1, FOR2)Timeliness (TIME)</td><td></td></tr><tr><td>UIS (Etizadi &amp; Torkzadeh)</td><td>Functionality (FUNC1)</td><td></td></tr><tr><td>Documentation</td><td>UIS (Etizadi &amp; Torkzadeh)</td><td>(DOC1, DOC2, DOC3, DOC4, DOC5)</td><td>0.9337</td></tr><tr><td rowspan="2">Ease of use</td><td>TTF</td><td>Ease of Use (EQU1T, EQU2T)</td><td>0.9226</td></tr><tr><td>UIS (Etizadi &amp; Torkzadeh)</td><td>Ease of Use (EQU1U, EQU2U)</td><td></td></tr><tr><td>System reliability</td><td>TTF</td><td>Reliability (RELIA1, RELIA2)</td><td>0.8660</td></tr><tr><td>Authorization</td><td>TTF</td><td>Authorization (AUTH1, AUTH2)</td><td>0.7618</td></tr></table>

Table 5 Results of stepwise regression analysis

<table><tr><td>Model</td><td>Dependent variable (Y)</td><td>Independent variable</td><td>Tentatively selected as a predictor</td><td>Beta coefficient ( $\beta$ )</td><td>adjusted  $R^{2}$ </td></tr><tr><td rowspan="7">1</td><td rowspan="7">Performance</td><td></td><td>Constant</td><td>0.303</td><td>0.733</td></tr><tr><td>System quality</td><td>Yes (Positive)</td><td>0.517</td><td></td></tr><tr><td>Documentation</td><td></td><td></td><td></td></tr><tr><td>Ease of use</td><td>Yes (Positive)</td><td>0.146</td><td></td></tr><tr><td>System reliability</td><td></td><td></td><td></td></tr><tr><td>Authorization</td><td></td><td></td><td></td></tr><tr><td>Utilization</td><td>Yes (Positive)</td><td>0.344</td><td></td></tr><tr><td rowspan="6">2</td><td rowspan="6">Utilization</td><td></td><td>Constant</td><td>2.217</td><td>0.405</td></tr><tr><td>System quality</td><td>Yes (Positive)</td><td>0.494</td><td></td></tr><tr><td>Documentation</td><td>Yes (Negative)</td><td>-0.156</td><td></td></tr><tr><td>Ease of use</td><td>Yes (Positive)</td><td>0.250</td><td></td></tr><tr><td>System reliability</td><td></td><td></td><td></td></tr><tr><td>Authorization</td><td></td><td></td><td></td></tr></table>

2. The given independent variable (i.e., System Quality, Ease of Use, Documentation) has a statistically significant effect on Individual Performance, the dependent variable.

3. The mediator Utilization should have a statistically significant effect on Individual Performance the dependent variable.

The results of the mediation testing in Table 6 confirm that Utilization is the mediator between the two independent variables – System Quality and Ease of Use – and the dependent variable – Individual Performance. However, the evidence of Utilization as the mediator between Documentation and Individual Performance is not established, as Documentation has no statistically significant effect.

From the results of the regression analysis and the mediation testing presented above, we conclude that System Quality and Ease of Use have both direct and indirect impacts on Individual Performance. The resultant model of the determinants of the individual performance of the ERP users is graphically displayed in Figure 3.

## RS analysis

In order to examine the main effect and two-way interaction, we conducted RS analyses for both Performance (PERFORM) and Utilization (UTIL). With regard to main effect, we found that System Quality has a positive, statistically significant rate of impact on Performance, but this rate of impact is not uniform as it is decreases when the value of System Quality is above 2 (adjusted $R ^ { 2 } { = } 0 . 7 4 1 )$ . Further, both Ease of Use and Utilization have a positive statistically significant rate of impact (adjusted $R ^ { 2 } { = } 0 . 7 4 1 )$ ). Also, System Quality has a positive statistically significant rate of impact on Utilization; and while Ease of Use has a positive statistically significant rate of impact on Utilization only when Ease of Use has a value greater than 1.25 (adjusted $R ^ { 2 } { = } 0 . 3 9 5 )$ . With regard to two-way interaction, we found that both System Quality and Ease of Use have a direct statistically significant impact on Performance. Additional statistically significant impacts are influential through interactions with other factors (adjusted $R ^ { 2 } = 0 . 8 2 4 )$ . Utilization, Authorization, and Documentation each have their statistically significant impact on Performance, but only through interactions (adjusted $R ^ { 2 } = 0 . 8 2 4 )$ . Finally, while System Quality has a direct statistically significant impact on Utilization, Ease of Use, Reliability, Authorization, and Documentation, each have their statistically significant impact on Utilization only through interactions (adjusted $R ^ { \dot { 2 } } { = } 0 . 4 4 8 )$ .

Table 6 Mediation testing for ERP data set

<table><tr><td>Regression equation</td><td>Target variable</td><td>Input variables</td><td>Beta coeffi-cient (β)</td><td>Sig. (P-value)</td></tr><tr><td rowspan="3">1</td><td rowspan="3">Utilization</td><td>System quality</td><td>0.494</td><td>0.000</td></tr><tr><td>Ease of use</td><td>0.250</td><td>0.001</td></tr><tr><td>Documentation</td><td>-0.156</td><td>0.020</td></tr><tr><td rowspan="3">2</td><td rowspan="3">Performance</td><td>System quality</td><td>0.680</td><td>0.000</td></tr><tr><td>Ease of use</td><td>0.218</td><td>0.000</td></tr><tr><td>Documentation</td><td>-0.015</td><td>0.764*</td></tr><tr><td rowspan="4">3</td><td rowspan="4">Performance</td><td>System quality</td><td>0.507</td><td>0.000</td></tr><tr><td>Ease of use</td><td>0.131</td><td>0.011</td></tr><tr><td>Documentation</td><td>0.039</td><td>0.408*</td></tr><tr><td>Utilization</td><td>0.349</td><td>0.000</td></tr></table>

Note: \* There is no statistically significant effect).

![](/api/attachments/ST5JDSGP/fulltext/images/af425f59fd98148073a7b29f55aef7707919a3d083bf3c08f5ff10ab3c8ab7c6.jpg)  
Figure 3 Individual performance model for ERP users.

## Comparison of results of regression & RS analyses

In general, both regression analysis and RS provide similar results for those factors that have a significant impact on individual performance. For example, the RS models indicate that, in some cases, the rate of impact of an independent variable on the dependent variable is conditional and may depend on the value of the given independent variable and other variables. In addition, we generated a consensus result by applying a majority vote rule to the results of the regression and RS analyses (See Table 7). This result is consistent with Figure 3. It is important to note here that, from our mediation testing (Table $^ { 6 ) , }$ Utilization is not a mediator between Documentation and Performance. When we do not consider Documentation in the regression model for Utilization, the adjusted $\mathrm { R } ^ { 2 }$ of the model is 0.394.

We approached the exploratory analysis task with the two data analysis techniques, regression analysis and RS analysis. The results from the two data analysis techniques complement each other. This is not unexpected as both techniques are based on the same foundation of least-squares estimation. The purpose of using and comparing the two techniques was not to put forward evidence that one was better or more appropriate than the other; instead, they are different. However, we would like to point out the following. While regression analysis is a more theory-driven approach, RS is a more datadriven approach. RS utilizes a dynamic/heuristic search for BFs and interactions between BFs. While regression analysis is a deductive approach to scientific inquiry, RS is an inductive approach. Both can be used in research in IS or any other discipline.

## Contribution to research and practice

Taken from the literature in TTF and User Satisfaction, six factors were investigated in order to determine which might better predict individual performance in an ERP environment. These six factors were: system quality; documentation; ease of use; system reliability; authorization; and utilization. Analysis shows that although the impact of other factors on Individual Performance is significant, System Quality, Utilization, and Ease of Use are the most important factors that can impact Individual Performance in an ERP environment, as can be seen from Figure 4.

Table 7 Comparison of regression and RS analyses results

<table><tr><td>Dependent variable</td><td>Regression</td><td>RS with no interaction</td><td>RS with two-way interaction</td><td>Consensus</td></tr><tr><td>Utilization</td><td>System quality, ease of use</td><td>System quality ease of use</td><td>System quality ease of use, documentation, authorization, reliability</td><td>System quality, ease of use</td></tr><tr><td>Adj  $R^{2}$ </td><td>0.405</td><td>0.395</td><td>0.448</td><td></td></tr><tr><td>Performance</td><td>System quality, utilization, ease of use</td><td>System quality, utilization, ease of use</td><td>System quality, ease of use, documentation, authorization, utilization</td><td>System quality, utilization, ease of use</td></tr><tr><td>Adj  $R^{2}$ </td><td>0.733</td><td>0.741</td><td>0.824</td><td></td></tr></table>

As well as making its contribution to the literature in the information systems management field, practitioners may benefit. The formulas associated with the constructs and equations associated with the regression and RS could be programmed in a spreadsheet used by managers to estimate the impacts of different ERP system configuration on individual performance. To illustrate this, we will use the equations of the main effects regression models. It should be noted that the formulas associated with the constructs were obtained as a result of factor analysis:

1. Given the questionnaire items that are associated with the Performance construct (i.e., PERFO1, PERF02, PERF03), a determination could be made of the minimum rating for each of these items that would be considered to be high individual Performance. Using these ratings, the threshold value (Performance ) for the Performance construct could be calculated.

2. An assessment of a given ERP system configuration could be done that would involve the questionnaire items that are associated with the independent variables (i.e., System Quality, Ease of Use).

3. Given the set of items associated with each construct, the corresponding construct score can be calculated as the average rating of the set of items.

4. Given the System Quality and Ease of Use construct scores, the regression equation for which Utilization is the target variable (see Table 8) can be used to estimate the corresponding construct score Utilization<sub>Estimate</sub>.

5. Given the System Quality and Ease of Use construct scores and Utilization<sub>Estimate</sub>, the regression equation for which Performance is the target variable (see Table 8) and can be used to estimate the corresponding construct score Performance<sub>Estimate</sub>.

6. If Performance<sub>Estimate</sub> o Performance<sub>Threshold</sub> then the manager could explore the impact of increasing the ratings of selected items in the System Quality and Ease of Use constructs in order to increase the value of Performance<sub>Estimate</sub>. Assuming that there are different costs for improving the levels of different items in these constructs, the configuration associated with the smallest increase in total cost could be selected.

![](/api/attachments/ST5JDSGP/fulltext/images/57cf7d4cb7acaaa69535514ee3ac553d494973f049ed44191081bbe0764186de.jpg)  
Figure 4 Factors impacting on individual performance in ERP environment.

Table 9 describes our illustrative example. The managers decided that the threshold for Performance is approximately 6.00 (i.e., Performance<sub>Threshold</sub>D6.0). The current system configuration (see status quo column of Table 9) results in Performance<sub>Estimate</sub> ¼ 5.29 which is below Performance<sub>Threshold</sub>. They therefore decided to explore the impact of a few sample ERP System Improvements Options. The value of Performance<sub>Estimate</sub> for Option 5 and Option 6 exceeds Performance<sub>Threshold</sub> while that for Option 3 is very close to exceeding the Performance<sub>Threshold</sub>. The manager would therefore attempt to estimate the additional cost of improving the system configuration from the status quo to that of each of these options, and select the one with the lowest cost.

## Concluding comments

This study contributes to the research community and IS management practice. The paper presents empirical evidence that prior theoretical models of individual performance of traditional IS can be applied and extended to develop our understanding of individual performance of ERP systems usage. Although ERP systems are different from traditional IS, there are dimensions of these systems that can be analyzed using existing models to understand and manage individual performance in the use of these systems. Furthermore, through our use of RS analysis, we were able to provide more detail regarding the specific factors that impact individual performance when using ERP system (e.g. changes in the rate of impact over different regions).

Table 8 Regression equations of main effect regression splines models

<table><tr><td>Target</td><td>Equation</td></tr><tr><td>Utilization</td><td> $2.702+0.463 \times \text{Max}(0, \text{SYSQUAL}-1.00)+0.201 \times \text{Max}(0, \text{EOU}-1.25)$ </td></tr><tr><td>Performance</td><td> $2.804+0.431 \times \text{Max}(0, \text{SYSQUAL}-2.00)-1.576 \times \text{Max}(0,$  $2.00-\text{SYSQUAL})+0.156 \times \text{Max}(0,\text{EOU}-1.00)+0.347 \times \text{Max}(\text{UTIL}-1.00)$ </td></tr></table>

Table 9 Illustrative example

<table><tr><td rowspan="2">Item</td><td rowspan="2">Status quo</td><td colspan="5">Sample ERP system improvements options</td></tr><tr><td>Option 1</td><td>Option 2</td><td>Option 3</td><td>Option 4</td><td>Option 5</td></tr><tr><td>MEAN</td><td>4</td><td>4</td><td>6</td><td>4</td><td>4</td><td>7</td></tr><tr><td>CONT1</td><td>5</td><td>5</td><td>6</td><td>5</td><td>5</td><td>7</td></tr><tr><td>CONT2</td><td>3</td><td>3</td><td>6</td><td>3</td><td>4</td><td>7</td></tr><tr><td>CONT3</td><td>5</td><td>5</td><td>6</td><td>5</td><td>5</td><td>7</td></tr><tr><td>CONT4</td><td>4</td><td>4</td><td>6</td><td>4</td><td>4</td><td>7</td></tr><tr><td>ACCU1</td><td>5</td><td>5</td><td>5</td><td>6</td><td>5</td><td>5</td></tr><tr><td>ACCU2</td><td>4</td><td>4</td><td>4</td><td>6</td><td>4</td><td>4</td></tr><tr><td>FOR1</td><td>4</td><td>4</td><td>4</td><td>6</td><td>4</td><td>4</td></tr><tr><td>FOR2</td><td>4</td><td>4</td><td>4</td><td>6</td><td>4</td><td>4</td></tr><tr><td>TIME</td><td>4</td><td>4</td><td>4</td><td>6</td><td>4</td><td>4</td></tr><tr><td>FUNC1</td><td>4</td><td>4</td><td>4</td><td>6</td><td>4</td><td>4</td></tr><tr><td>System quality</td><td>4.18</td><td>4.18</td><td>5.00</td><td>5.18</td><td>4.27</td><td>5.45</td></tr><tr><td>EQU1T</td><td>3</td><td>6</td><td>3</td><td>3</td><td>7</td><td>3</td></tr><tr><td>EQU2T</td><td>4</td><td>6</td><td>4</td><td>4</td><td>7</td><td>4</td></tr><tr><td>EQU1U</td><td>5</td><td>6</td><td>5</td><td>5</td><td>7</td><td>5</td></tr><tr><td>EQ2U</td><td>4</td><td>6</td><td>4</td><td>4</td><td>7</td><td>4</td></tr><tr><td>Ease of use</td><td>4.00</td><td>6.00</td><td>4.00</td><td>4.00</td><td>7.00</td><td>4.00</td></tr><tr><td>Utilization_Est</td><td>4.10</td><td>4.50</td><td>4.48</td><td>4.56</td><td>4.74</td><td>4.69</td></tr><tr><td>Performance_Est</td><td>5.29</td><td>5.74</td><td>5.77</td><td>5.88</td><td>6.02</td><td>6.04</td></tr></table>

Future research could use MARS to explore the significant impact of variables including levels of system integration, social norms, and organizational cultures on individual performance. Levels of system integration can be operationalized by categorizing the level of integration using the number of modules implemented in organizations. Social norms and organizational cultures can be operationalized based on organization types recommended by Morgan (1986). In an attempt to gain the maximum benefit from the MARS explanatory power, a different measurement (i.e., a true continuous scale) may be used. Another possibility for future research would be to test the causality between independent and dependent variables by conducting an experimental design, as crosssectional data cannot infer causality.

From an information systems management perspective, the results of the study point to specific factors and system features that managers can leverage to improve the performance of individuals who use ERP systems. Our findings suggest that it is necessary for ERP implementation managers to spend time and effort to make sure that users are satisfied with system quality and ease of use, as these two are identified as the most important factors that contribute to individual performance when using ERP systems. To be useful to organizations, ERP systems must provide data and information that is accurate, current, and sufficient to meet users’ needs. Information should provide the right level of detail and be presented in a useful format. In addition, the ERP system should be easy to use for users. These qualities can be confirmed through ERP software selection and through ERP implementation, including business process re-design and system configuration. Without this interface between users and systems, frustration and resistance to the systems by the users can become a constant problem.

## Acknowledgements

This research was supported in part by a grant from the 2004 Summer Research Program of the School of Business of Virginia Commonwealth University, Richmond, VA, U.S.A.

## About the authors

Boontaree Kositanurit, is an economist at Fiscal Policy Office, Ministry of Finance, Thailand, where she is involved in implementation of economic management systems. She earned her Ph.D. in Information Systems (2003) and MBA (1998) at the Virginia Commonwealth University and her B.S., in Mathematics and Computer Science from Chulalongkorn University, Thailand in 1995. Her research areas include: Information Technology and Productivity, and Data Mining.

Ojelanki K. Ngwenyama is Professor of Information Technology Management and Director of the Institute for Research on Technology Management and Organizational Learning, at Ryerson University, Toronto, Canada;

## References

ABRAHAM A (2002) Analysis of hybrid soft and hard computing techniques for Forex monitoring systems. World Congress on Computational Intelligence, pp 1616–1622.

ABRAHAM A and STEINBERG D (2001) Is neural network a reliable forecaster on earth? A MARS query! In International Work – Conference on Artificial and Natural Neural Network (MIRA J and PRIETO A, Eds), pp 679–686, Springer-Verlag, Grenada, Spain.

AL-GAHTANI SS and KING M (1999) Attitudes, satisfaction and usage: factors contributing to each in the acceptance of information technology. Behaviour & Information Technology 18(4), 277–297.

AL-MUDIMIGH A, ZAIRI M and AL-MASHARI M (2001) ERP software implementation: an integrative framework. European Journal of Information System 10, 216–226.

BAILEY JE and PEARSON SW (1983) Development of a tool for measuring and analyzing computer user satisfaction. Management Science 29(5), 530–545.

BARON R and KENNY DA (1986) The moderator-mediator variable distinction in social psychological research: conceptual, strategic, and statistical considerations. Journal of Personality and Social Psychology 51(6), 1173–1182.

BAUER E and KOHAVI R (1999) An empirical comparison of voting classification algorithms: bagging, boosting, and variants. Machine Learning 36, 105–139.

BINGI P, SHARMA M and GODLA J (1999) Critical issues affecting an ERP implementation. Information Systems Management 16(3), 7–14.

BLILI SRL and RIVARD S (1998) Impact of task uncertainty, end-user involvement, and competence on the success of end-user computing. Information and Management 33(3), 137–153.

BRIAND LC, MELO WL and WUST J (2002) Assessing the applicability of fault-proneness models across object-oriented software projects. IEEE Transactions on Software Engineering 28(7), 706–720.

CAREY WP and YEE SS (1992) Calibration of nonlinear solid-state sensor arrays using multivariate regression techniques. Sensors and Actuators 9, 113–122.

CHEN L (1997) Multivariate regression splines. Computational Statistics & Data Analysis 26, 71–82.

DELONE WH and MCLEAN ER (1992) Information systems success: the quest for the dependent variable. Information Systems Research 3(1), 60–95.

DISHAW MT and STRONG DM (1998) Assessing software maintenance tool utilization using task–technology fit and fitness-for use models. Journal of Software Maintenance Research and Practice 10(3), 151–179.

DISHAW MT and STRONG DM (1999) Extending the technology acceptance model with task–technology fit constructs. Information and Management 36(1), 9–21.

DOLL WJ and TORKZADEH G (1988) The measurement of end-user computing satisfaction. MIS Quarterly 12(1), 259–274.

Visiting Research Professor at Aarhus Business School and Aalborg University, Denmark; and Docent at University of Jyva¨skyla¨, Finland. His research focuses on social and organizational implications of information technology. Kweku-Muata Osei-Bryson is Professor of Information Systems at Virginia Commonwealth University, where he was also Coordinator of its Information Systems Ph.D. programme. He has also been an Information Systems practitioner in both industry and government. His research areas include: Data Mining, Expert Systems, Decision Support Systems, Information Technology and Productivity, Information Systems Outsourcing, Multi-Criteria Decision Analysis.

DOLL WJ, XIA W and TORKZADEH G (1994) A confirmatory factor analysis of the end-user computing satisfaction instrument. MIS Quarterly 18(4), 453–461.

DOWNING CE (1999) System usage behavior as a proxy for user satisfaction: an empirical investigation. Information and Management 35(4), 203–216.

EKMAN T and KUBIN G (1999) Nonlinear prediction of mobile radio channels: measurements and MARS model designs. IEEE International Conference on Acoustics, Speech and Signal Processing, pp 2667–2670, Phoenix, Arizona.

ETEZADI-AMOLI J and FARHOOMAND AF (1996) A Structural model of end user computing satisfaction and user performance. Information and Management 30(2), 65–73.

FERRATT TW and VLAHOS GE (1998) An investigation of task–technology fit for managers in Greece and the US. European Journal of Information Systems: An Official Journal of the Operational Research Society 7(2), 123–136.

FRIEDMAN JH (1991) Multivariate adaptive regression splines. The Annals of Statistics 19(1), 1–67.

GOODHUE DL (1995) Understanding user evaluations of information systems. Management Science 41(12), 1827–1844.

GOODHUE DL (1998) Development and measurement validity of a task– technology fit instrument for user evaluations of information systems. Decision Sciences 29(1), 105–138.

GOODHUE DL, KLEIN B and MARCH ST (2000) User evaluations of IS as surrogates for object performance. Information and Management 38(2), 87–101.

GOODHUE DL and THOMPSON RL (1995) Task–technology fit and individual performance. MIS Quarterly 19(2), 213–236.

GRIFFIN W, FISHER N, FRIEDMAN J and RYAN C (1997) Statistical technique for the classification of chromites in diamond exploration samples. Journal of Geochemical Exploration 59, 233–249.

HASTIE TJ and TIBSHIRANI R (1990) Generalized Additive Model. Chapman & Hall, London.

HASTIE TH, TIBSHIRANI R and FRIEDMAN J (2001) The Elements of Statistical Learning: Datamining, Inference, and Prediction. Springer-Verlag, New York.

HENDRICKSON AR, GLORFELD K and CRONAN TP (1994) On the repeated test-retest reliability of the end-user computing satisfaction instrument: a comment. Decision Science 25(4), 655–667.

IGBARIA M and TAN M (1997) The consequence of information technology acceptance on subsequent individual performance. Information and Management 32(3), 113–121.

IVES B, OLSON MH and BAROUDI JJ (1983) The measurement of user information satisfaction. Communications of the ACM 26(10), 785–793.

JARVENPAA SL (1989) The effect of task demands and graphical format on information processing strategies. Management Science 35(3), 285–303.

JIN R, CHEN W and SIMPSON T (2001) Comparative studies of metamodelling techniques under multiple modelling criteria. Journal of Structural and Multidisciplinary Optimization 23(1), 1–13.

KO M and OSEI-BRYSON K-M (2004) Using Regression Splines to Assess the Impact of Information Technology Investments on Productivity in the Health Care Industry. Information Systems Journal 14(1), 43–63.

KREMERS M and DISSEL HV (2000) ERP system migrations. Communications of the ACM 43(4), 53–56.

KUHNERT P, KIM-ANH D and MCCLURE R (2000) Combining non-parametric models with logistic regression: an application to motor vehicle injury data. Computational Statistics & Data Analysis 34, 371–386.

LAI VS (1999) A contingency examination of CASE-task fit on software developer’s performance. European Journal of Information Systems 8(1), 27–39.

MABERT V, SONI A and VENKATARAMAN MA (2001) Enterprise resource planning: measuring value. Production and Inventory Management Journal, Summer-Fall 44(3–4), 46–52.

MALLICK BK, DENISON DGT and SMITH AFM (1997) Bayesian survival analysis using a MARS model. Technical report, Imperial College, London.

MARKUS LM and TANIS C (2000) The enterprise systems experience – from adoption to success. In Framing the domains of it research: glimpsing the future through the past (ZMUD RW, Ed), Pinnaflex educational resources, Cincinnati, Ohio.

MATHIESON K and KEIL M (1998) Beyond the interface: ease of use and task–technology fit. Information and Management 34(4), 221–230.

MORGAN G (1986) Images of Organization. Sage Publications, Beverly Hills, CA.

MURRAY MG and COFFIN GW (2001) A case study analysis of factors for success in ERP system implementations. Proceedings of the Seventh American Conference on Information Systems, pp 1012–1018.

NGUYEN-CONG V, VAN DANG G and RODE DBM (1996) Using multivariate adaptive regression splines to OSAR studies of dihydroartemisinin derivatives. European Journal of Medical Chemistry 31, 797–803.

PALANISWAMY R and FRANK T (2000) Enhancing manufacturing performance with ERP systems. Information Systems Management 17(3), 43–55.

PARR A and SHANKS G (2000) A model of ERP project implementation. Journal of Information Technology 15, 289–303.

SUMMER M (1999) Critical success factors in enterprise wide information management systems projects. Proceedings of the 1999 ACM SIGCPR Conference on Computer Personnel Research, pp 297–303.

THOMPSON RL, HIGGINS CA and HOWELL JM (1991) Personal computing: toward a conceptual model of utilization. MIS Quarterly 15(1), 125– 143.

TORKZADEH G and DOLL WJ (1991) Test-retest reliability of the end-user computing satisfaction instrument. Decision Science 22(1), 26–37.

WILSON EV and ADDO TBA (1994) An investigation of the relative presentation efficiency of computer-displayed graphs. Information and Management 26(2), 105–115.

YORK TP and EAVES LJ (2001) Common disease analysis using multivariate adaptive regression splines (MARS): genetic analysis workshop 12 simulated sequence data. Genetic Epidemiology 21, 649–654.

## Appendix A

# Questionnaire Items and Acronyms Used

The final questionnaire items used in the survey are listed together with acronyms used to represent the items. Each item is presented in the format of ‘acronym – the questionnaire item’.

Questionnaire items relating to measurements of logical concepts, that is, factors (1) CURR – The data provide by the ERP system is up-to-date enough for my purposes. (2) RDATA – The ERP system available to me is missing critical data that are very useful to me in my job. (3) RDETAIL – The ERP system maintains data at an appropriate level of detail for my group’s tasks.) (4) MEAN – The exact definition of data fields relating to my tasks is easy to find out. (5) AUTH1 – Data that would be useful to me are unavailable because I don’t have the right authorization. (6) AUTH2 – Getting authorization to access data that would be useful in my job is time consuming and difficult. (7) RELIA1 – The ERP system I use is subjected to unexpected or inconvenient down times which makes it harder to do my wo (8) RELIA2 – The ERP system I use is subject to frequent system problems and crashes. (9) EOU1T – It is easy to learn how to use the ERP system. (10) EOU2T – The ERP system I use is convenient and easy to use. (11) TRAIN – There is not enough training for me or my staff on how to find, understand, access or use the ERP system. (12) CONT1 – The ERP system provides the precise information I need. (13) CONT2 – The information contents provided by the ERP system meet my needs. (14) CONT3 – The ERP system provides reports that seem to be exactly what I need. (15) CONT4 – The ERP system provides sufficient information to my needs. (16) ACCU1 – The system is accurate (17) ACCU2 – I am satisfied with the accuracy of the system (18) FOR1 – The output is presented in a useful format. (19) FOR2 – The information is clear. (20) TIME – The ERP system provides me the information I need in a timely manner. (21) DOC1 – The content of the user manual is useful. (22) DOC2 – The index of the user manual is useful. (23) DOC3 – The user manual is current (up-to-date) (24) DOC4 – The user manual is complete. (25) DOC5 – The user manual is easy to understand and follow. (26) EOU1U – The description of the functions/ commands displayed on screen is clear to me. (27) EOU2U – The function/command names of the ERP are easy to remember (28) FUNC1 – The ERP system provides complete features I need. (29) FUNC2 – I am satisfied with the speed of interacting with the system.

## Appendix A Continued

(30) FUNC3 – It is easy to detect possible errors in the ERP systems.

(31) FUNC4 – It is easy to correct errors that happen in the ERP systems.

(32) FUNC5 – It is easy to change the output format.

(33) SUPP1 – I am satisfied with the amount of support provided by vendor or other sources.

(34) SUPP2 – I am satisfied with the availability of information systems staff for consultation.

(35) UTIL1 – Currently, I cannot accomplish my tasks without the ERP systems.

(36) UTIL2 – If I have a choice to use any systems to perform my tasks, I still prefer to use the current system I use.

(37) PERFO1 – The ERP system helps me be more effective.

(38) PERFO2 – The ERP system has a positive impact on my productivity in my job.

(39) PERFO3 – The ERP is an important aid to me in the performance of my job.

For these 39 questionnaire items, the scale used is the 7-point likert scale.

<table><tr><td>1Strongly disagree</td><td>2Moderately disagree</td><td>3Slightly disagree</td><td>4Neither agree Nor disagree</td><td>5Slightly agree</td><td>6Moderately agree</td><td>7Strongly Agree</td></tr></table>

## Questionnaire items relating to demographic and support information

(40) INDUS – What industry is your company in? (1) Aerospace and defence 12) Manufacturing (2) Automotive 13) Oil and Gas (3) Banking 14) Pharmaceuticals (4) Chemicals 15) Public Sector

(41) EDUC – Education: Please check highest degree attained: (1) High school graduate or less (2) Baccalaureate Degree (3) Masters Degree (4) Doctorate

(42) LWCOMP (Years working in the company) – How long have you worked with the company?

(43) LWJOB (Years working in the current job) – How long have you worked in your current job?

(44) LWSYS (Years working with the system in consideration either ERP or non-ERP) – How long have you worked with the ERP/non-ERP system that you identified?

(45) TIMESYS (Average hours spent with the ERP/non-ERP system per day) – Please estimate how much time you spend each day on the ERP/non-ERP system that you identified?

(3) Mid-level manager (Supervising other managers)

(4) Executive (Top) level manager (Vice president. President. Chairman of the Board of Directors, etc.)

## Appendix B: Overview of RS

RS is a method for flexible regression modeling (Friedman, 1991). While traditional regression analysis uses a single slope to represent the relationship between a dependent and an independent variable, RS allows more than one slope, thus it provides a more flexible model than regression analysis. The RS method uses a set of piecewise polynomials to describe the relationships between the independent variables and the dependent variable (Chen, 1997). Each piecewise polynomial, called a basis function (BF), represents a sub-region of the domain of the spline. Basis functions are used by RS to implement the concepts of knots and piecewise linear RS (Briand et al., 2002).

MARS is a computer-assisted approach to RS analysis that allows for automatic selection of the knots (Hastie & Tibshirani, 1990; Friedman, 1991). MARS builds the RS model in a two-phase process, using a forward-stepwise regression selection and backward-stepwise deletion strategy. In the first phase, an overfitted model is built by adding basis functions. In the second phase, basis functions that have the least contribution to the model are deleted where removal causes the smallest increase in residual squared error. The MARS model is optimized based on the Generalized Cross Validation measure (Hastie et $a l . ,$ 2001). A MARS model can be generated that allows no interaction between the input variables, or

## Appendix C: Details of factor analysis

## Independent variables:

We conducted several iterations of factor analyses in order to find a meaningful or interpretable grouping of the questionnaire items. Based on the results of the initial iteration, RDATA, TRAIN, FUNC2, FUNC3, FUNC4, FUNC5, SUPP1, and SUPP2 variables were omitted from further consideration because they have cross loadings (i.e., the load was very close on more than one factors and the difference in the loadings was less than 0.1) and low communalities. Although the difference in the loadings of MEAN on the System Quality factor (i.e., factor 1) and the Ease of Use factor (i.e., factor 3) was less than 0.1 (i.e., to permit interactions between two or more variables. In MARS, analysis interactions between variables have a hierarchical, tree-like structure, with parent and child relationships between basis functions. A MARS model that does not involve interaction between the variables (or factors) can be expressed as a linear combination of nonlinear functions $( \mathrm { i } . \mathrm { e } . , \mathrm { B F } _ { j k } )$ of the independent variables such that $\gamma = b _ { 0 } + \Sigma _ { j } \ f _ { j } ( x _ { j } )$ . Equivalently, it can be expressed as a linear combination of basis functions $\mathrm { B F } _ { j k }$ such that $\gamma = \beta _ { 0 } + \Sigma _ { j } ~ \Sigma _ { k \in K j } ~ \beta _ { j k } \mathrm { { B F } } _ { j k }$ where $f _ { j } ( x _ { j } ) = \Sigma _ { k \in K j }$ $\beta _ { j k } \mathrm { B F } _ { j k } , \ \beta _ { 0 }$ is a constant that is equivalent to the intercept in the regression model, $\mathrm { B F } _ { j k }$ is a basis function of the independent variable (or factor) that has one of the following forms: max(0, $X _ { j } - c _ { j k } )$ , or max(0, $c _ { j k } { - } X _ { j } )$ , and $\beta _ { j k }$ is a coefficient of the basis function $B F _ { j k } .$ . MARS must both identify the most relevant knots $( \mathrm { e } . \mathrm { g } . \ c _ { j k } )$ as well as the coefficients. The coefficients are the coefficients $\beta _ { j k }$ and are estimated by minimizing the sum of square errors. RS performs a polynomial fit in each region with constraints at the knots using the least squares criterion.

loading on factor 1 and 3 were 0.607 and 0.519, respectively), it was retained for the following reasons: (1) the loading on the System Quality factor was 0.088 higher than the loading on the Ease of Use factor; (2) the alpha of System Quality with MEAN was as high as 0.9603; and (3) the reliability analysis of the System Quality factor did not suggest that MEAN should be deleted.

In our second iteration, factor analysis and reliability analysis were re-performed on the other 26 items (cf. Table C1). The five factors produced by the factor analysis explained 70.996% of the total variance. Reliability analysis was then performed on each of the factors suggested by the factor analysis. Although the reliability analysis recommended that RDETAIL should be dropped, the item was maintained because the alpha of System Quality is quite high (0.9603) and if the item is deleted, the increase in the alpha is not significant (0.0002).

Table C1 Factor analysis and reliability analysis of TTF and user satisfaction items

<table><tr><td>Original instrument</td><td>Items</td><td>System quality</td><td>Documentation</td><td>Ease of use</td><td>System reliability</td><td>Authorization</td></tr><tr><td colspan="7">TTF</td></tr><tr><td>Currency</td><td>CURR</td><td>0.705</td><td></td><td></td><td></td><td></td></tr><tr><td>Right data</td><td>RDATA</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Right level of detail</td><td>RDETAIL</td><td>0.621</td><td></td><td></td><td></td><td></td></tr><tr><td>Meaning</td><td>MEAN</td><td>0.607</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">Ease of use</td><td>EOU1T</td><td></td><td></td><td>0.645</td><td></td><td></td></tr><tr><td>EOU2T</td><td></td><td></td><td>0.704</td><td></td><td></td></tr><tr><td>Training</td><td>TRAIN</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">Authorization</td><td>AUTH1</td><td></td><td></td><td></td><td></td><td>0.672</td></tr><tr><td>AUTH2</td><td></td><td></td><td></td><td></td><td>0.831</td></tr><tr><td rowspan="2">System reliability</td><td>RELIA1</td><td></td><td></td><td></td><td>0.735</td><td></td></tr><tr><td>RELIA2</td><td></td><td></td><td></td><td>0.904</td><td></td></tr><tr><td colspan="7">UIS of Doll and Torkzadeh</td></tr><tr><td rowspan="4">Content</td><td>CONT1</td><td>0.838</td><td></td><td></td><td></td><td></td></tr><tr><td>CONT2</td><td>0.894</td><td></td><td></td><td></td><td></td></tr><tr><td>CONT3</td><td>0.629</td><td></td><td></td><td></td><td></td></tr><tr><td>CONT4</td><td>0.862</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">Accuracy</td><td>ACCU1</td><td>0.670</td><td></td><td></td><td></td><td></td></tr><tr><td>ACCU2</td><td>0.745</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">Format</td><td>FOR1</td><td>0.643</td><td></td><td></td><td></td><td></td></tr><tr><td>FOR2</td><td>0.721</td><td></td><td></td><td></td><td></td></tr><tr><td>Timeliness</td><td>TIME</td><td>0.730</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="7">UIS of Etizadi and Farhoomand</td></tr><tr><td rowspan="5">Documentation</td><td>DOC1</td><td></td><td>0.801</td><td></td><td></td><td></td></tr><tr><td>DOC2</td><td></td><td>0.799</td><td></td><td></td><td></td></tr><tr><td>DOC3</td><td></td><td>0.808</td><td></td><td></td><td></td></tr><tr><td>DOC4</td><td></td><td>0.829</td><td></td><td></td><td></td></tr><tr><td>DOC5</td><td></td><td>0.810</td><td></td><td></td><td></td></tr><tr><td rowspan="2">Ease of use</td><td>EOU1U</td><td></td><td></td><td>0.712</td><td></td><td></td></tr><tr><td>EOU2U</td><td></td><td></td><td>0.690</td><td></td><td></td></tr><tr><td rowspan="5">Functionality</td><td>FUNC1</td><td>0.746</td><td></td><td></td><td></td><td></td></tr><tr><td>FUNC2</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>FUNC3</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>FUNC4</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>FUNC5</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">Support</td><td>SUPP1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SUPP2</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reliability (alpha)</td><td></td><td>0.9603*</td><td>0.9337</td><td>0.9266</td><td>0.8860</td><td>0.7618</td></tr></table>

Note: (1)\* alpha will increase to 0.9605 if item Rdetail is deleted. (2) Extraction method – principal axis factoring. Rotation method – Varimax with Kaiser normalization.

The exploratory factor analysis confirmed the overlap of the instruments, as described by Goodhue (1998). The questionnaire items regarding Ease of Use from the TTF instrument and from the user satisfaction instrument of Etezadi-Amoli and Farhoomand were loaded together into one factor (Ease of Use). In addition, the currency item from the TTF instrument and the timeliness item from the user satisfaction instrument of Etezadi-Amoli and Farhoomand were loaded on the System Quality factor.

## Dependent Variables:

Utilization and Individual Performance are dependent variables in this study. However, Utilization is also an independent variable for Individual Performance. Thus, factor analyses were performed separately on Individual Performance items and Utilization items.

Items from Individual Performance (i.e., PERFO1, PERFO2, PERFO3) were loaded together into one factor with 81.79% total variance explained. The reliability analysis recommended the item PERFO3 to be deleted.

Table C2 Factor analysis and reliability analysis of individual performance items

<table><tr><td>Original instrument</td><td>Items</td><td>Factor</td><td>Alpha if item deleted</td></tr><tr><td colspan="4">Individual performance</td></tr><tr><td></td><td>PERFO1</td><td>0.884</td><td>0.865</td></tr><tr><td>Extraction method</td><td>PERFO2</td><td>0.914</td><td>0.861</td></tr><tr><td>Principal axis factoring</td><td>PERFO3</td><td>0.665</td><td>0.946</td></tr><tr><td>Alpha</td><td></td><td>0.927</td><td></td></tr></table>

Table C3 Factor analysis and reliability analysis of utilization items

<table><tr><td>Original instrument</td><td>Items</td><td>Factor</td></tr><tr><td colspan="3">Utilization</td></tr><tr><td>Extraction method</td><td>UTIL1</td><td>0.529</td></tr><tr><td>Principal axis factoring</td><td>UTIL2</td><td>0.529</td></tr><tr><td>Alpha</td><td></td><td>0.438</td></tr></table>

However, it was maintained since the alpha with the three items was as high as 0.927, and the alpha would be increased by only 0.02, if PERFO3 is deleted. Items from Utilization were loaded together into one factor with 28% total variance explained. Results of factor analysis and reliability analysis are presented in Tables C2 and C3.
