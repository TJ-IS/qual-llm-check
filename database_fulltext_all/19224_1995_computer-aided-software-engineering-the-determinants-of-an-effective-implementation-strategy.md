---
otero_id: 19224
otero_key: "YUZY5WVS"
title: "Computer-aided software engineering: The determinants of an effective implementation strategy"
authors: "Robert Urwiler; Narender K. Ramarapu; Ronald B. Wilkes; Mark N. Frolick"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(95)00025-r"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Applications

# Computer-aided software engineering: The determinants of an effective implementation strategy

Robert Urwiler ${}^{a}$ , Narender K. Ramarapu ${}^{b,*}$ , Ronald B. Wilkes ${}^{c}$ , Mark N. Frolick ${}^{c}$

$^{a}$ Price Waterhouse, LLP, Atlanta, GA, USA

$^{b}$ School of Business Administration, The University of Tennessee at Martin, Martin, TN 38238-5015, USA

$^{c}$ Fogelman College of Business and Economics, The University of Memphis, Memphis, TN 38152, USA

## Abstract

This report investigates the determinants of a successful Computer-Aided Software Engineering (CASE) tool implementation. Success was defined as a perceived increase in both the quality of software produced and the productivity of the software developers as a result of the introduction of technology. To investigate the effects of certain environmental conditions on the relative success, a survey was mailed to two hundred members of a specific CASE tool user group. Approximately thirty-five percent responded. The findings indicate that an environment which includes the enforcement of a development methodology and use of metrics contribute to perceived improvements in quality when using CASE. Also, use of metrics, use of consultants, and formal training contribute to perceived improvements in developer productivity. Apparently, the presence of each of these environmental conditions significantly contributes to a successful CASE implementation and is, therefore, a ‘determinant’ of a successful implementation strategy.

Keywords: CASE implementation; Metrics; Productivity; Quality; Software engineering; Systems development

## 1. Introduction

Over the past 30 years, the software development process has been slowly evolving from an art form to a structured discipline. Brooks [2] describes the effect of many of the undisciplined software development practices common during mid-1960s. Since that time, much attention has been given to refining the tools and methodologies necessary for efficient and effective system development [17]. One of the most promising developments in recent years has been the introduction of computer-aided software engineering (CASE) as a vehicle to increase the effectiveness of the overall software development life cycle. It is a software technology that brings an engineering discipline to systems development, maintenance, and project management through the use of automated tools. CASE is attractive because the automation effort helps to reduce the cost of software development by minimizing the labor content of software [13]. It has been estimated that thousands of organizations have turned to CASE as part of their quest towards improved productivity and system quality, and that it will revolutionize software development in the same manner that CAD/CAM has revolutionized many engineering disciplines in the past 25 years [21,29].

CASE is currently having a profound effect on corporate America. According to a recent nation-wide survey of systems analysts, about two-thirds indicated that they are involved to some extent in its use [12].

Unfortunately, not all organizations that have made significant investments in the technology consider the outcome successful, but many have experienced frustration because the claims of vendors have not been realized. In fact, according to Case Research Corporation's Second Annual Report, less than $25\%$ of all the tools purchased were actually being used at the time of the study [25].

There are many perceptions as to why the transition from the traditional method of software development to a CASE based approach has been so difficult. One suggestion is that the implications of preparing for and instituting a relatively radical cultural change is not being adequately addressed in the implementation strategy [26].

Many studies indicate that the technology alone is not sufficient for improvement. These focus on the need to address motivational issues, education, and management within a carefully planned introduction program $[4,5,16,18,20,27]$ . Consequently, many organizations fail to realize that the cost of implementing CASE effectively goes well beyond the purchase of the software. Environmental factors may help determine success.

## 2. Related literature

When an organization makes the decision to explore CASE as a means of improving the software development process, a major change in design philosophy is assumed [1]. Factors identified as being necessary for an effective implementation include adequate planning, preparation, training, capitalization, and executive involvement. Common causes of an ineffective implementation have been identified as management short-sightedness, inadequate infrastructure, under capitalization, inability to share a vision at all levels of the organization, and a failure to match methods and tools to the organization's current level of maturity [6].

Norman and Nunamaker [21] conducted an experimental study of 91 software engineers from 47 organizations using a common CASE tool to test claims of productivity increases from the use of the technology. The study indicated a perception of productivity increase. The participants thought that the productivity increase could be attributed to adherence to the organization's pre-defined development methodology.

Other experimental studies indicate that no significant quality or productivity gains could be attributed to CASE technology $[3,14]$ . According to one expert, for productivity improvement to be realized, the tool must serve as a methodology companion and not simply a stand-alone technology $[16]$ . As software development becomes increasingly complex, a formal methodology can help to organize the process. This is accomplished by applying a pre-defined methodical approach to the software development process $[23]$ . In support of this position, it has been suggested that CASE tools should provide methodology adherence enforcement $[28]$ .

Hughes and Clark [7] conducted a study among senior information systems managers to determine why organizations have been unsuccessful in their attempts to implement CASE. They proposed a five stage model to explain the phases that organizations should follow during a CASE implementation: disenchantment, resignation, commitment, implementation, and maturity. Disenchantment is triggered by the realization that the current development method is inadequate. This leads to the initial acquisition of CASE tools without proper analysis or training. During the resignation phase, ad hoc experimentation continues until the organization realizes that the tool requires the adoption and enforcement of a development method. The commitment phase involves more rigorous evaluation of tools that meet the requirements. In addition, allocation of resources, training, and consulting to support a pilot project is needed. Implementation involves the installation and use of specific tools and methods for specific individual projects. Finally, maturity is characterized by the realization that one methodology may not serve all requirements.

The Software Engineering Institute (SEI), has identified the principle costs in a CASE adoption budget [8]. Items to consider include identifying the scope of the projects to be undertaken, the degree of environmental complexity within the target organization(s), the level of resistance to change, current technology being employed, current development practices, current skill level of developers, knowledge of CASE, and – based on past experience – the speed of technological advance within the targeted organizations. These factors can also be considered indicators of organizational readiness, which have been identified as one of the main determinants of an effective CASE implementation [24].

Organizational readiness can be characterized by maturity level. The SEI's Software Process Capability Maturity Model (CMM) is a five-level indicator of software process maturity. Level 1 (Initial) is characterized by crisis-driven, ad hoc development. Level 2 (Repeatable) is dominated by good management so that certain software tasks are repeated rather than recreated. Level 3 (Defined) is characterized by the use of standard processes in the development of software. Level 4 (Managed) includes the measurement and control of development activities. Finally, level 5 (Optimizing) involves the refinement of the development process via analysis of data collected about the process [9]. In 1990, at least 74% of surveyed organizations were still in the “initial” phase of evolution [19].

The SEI states that metrics (or applied software measurement) should be employed at each level of the maturity model in order to assess the effects of various tools and methods. According to Jones [11], applied software measurement is “the emerging discipline associated with the accurate and meaningful collection of information which has practical value to software management and staffs.” Its goal is to give software developers and professionals a set of useful, tangible data points for sizing, estimating, managing, and controlling software projects. Many different approaches can be tailored to the specific environment, but all focus on gathering relevant data to assist the organization in the decision making process [10,22].

Many organizations are becoming dissatisfied with CASE because they believed that the technology alone could solve their development problems. However, organizations should first study their development environment and understand where efforts should be made to make the best use of a development automation tool $[15]$ .

## 3. Research hypothesis

The literature suggests that certain environmental components of a CASE implementation plan will result in a more effective outcome. The following hypotheses characterize an environment conductive to success:

1. H1: IS organizations adhering to at least one structured development methodology have a greater likelihood of success with CASE technology than do IS organizations that do not adhere to it.

2. H2: IS organizations that implement CASE technology by first testing and refining the process via pilot projects have a greater likelihood of success with CASE technology than do IS organizations that do not.

3. H3: IS organizations that provide formal training on CASE supported development techniques have a greater likelihood of success with CASE technology than do IS organizations that provide either no formal training or formal training on tool usage alone.

4. H4: IS organizations that retain CASE consultants to guide the organization in the use of CASE technology have a greater likelihood of success with CASE technology than do IS organizations that do not.

5. H5: IS organizations that use some form of metrics to measure and refine the software development process have a greater likelihood of success with CASE technology than do IS organizations that do not.

## 4. Methodology

## 4.1. Subjects

Participants in this study were software development professionals currently utilizing a common integrated CASE tool in North American-based IS organizations. Individuals were drawn from the membership of a specific “user group” which requested anonymity as a condition of participation. Two hundred contacts of user group affiliate organizations were randomly selected from the membership list. Selected individuals were asked to participate in the study via an anonymous survey instrument.

## 4.2. Survey instrument

No available instrument adequately covered the information required for the CASE tool context. Therefore, a questionnaire was prepared to collect data (see Appendix A). The questionnaire measured the perceived level of increase in software quality and developer productivity as a result of using the CASE tool and the degree to which hypothesized environmental conditions were present. Open-ended comments were also solicited to gather anecdotes and to provide insight into the conditions of specific organizational implementations.

The questionnaire has three sections. Section 1 gathers demographic information and the functional characteristics of the development environment; Section 2 gathers information regarding perceived success with CASE; and Section 3 gathers information regarding conditions present in the environment. Demographic information and the functional characteristics of the development environment of a particular organization was gathered using six different multiple-choice questions.

The perceived success of CASE was measured by responses to two different statements regarding the perception of quality and productivity improvements as a result of using the CASE tool. Using a six-item Likert scale ranging from “strongly disagree” to “strongly agree,” the degree of participants opinion toward success was captured.

The presence of hypothesized environmental conditions was also measured by responses to statements on the same six-item Likert scale. Participants indicated the degree to which each of the conditions was present in their respective environment.

The questionnaire was validated by CASE user group officials and senior IS professors, and modified appropriately. Each official and professor reviewed the questionnaire to clarify any confusing terms or concepts, to minimize ambiguity before the final version of the questionnaire was distributed. An endorsement by CASE users group officials was also included in the cover letter to motivate participants to take part in the survey.

## 4.3. Correlational design

The correlational design was chosen in order to show the relationship between the level of quality and productivity improvement as a result of CASE and the degree to which each of the hypothesized conditions was present.

For the purposes of this study, success was defined as a perceived increase in productivity among software developers using CASE and a perceived increase in quality of software produced using CASE. Therefore, the two dependent variables measured were “productivity” and “quality.”

The independent variables measured were the conditional factors hypothesized: “use of a formal methodology,” “introduction via pilot projects,” “formal training in development techniques,” “the use of CASE consultants,” and “the use of metrics.”

## 4.4. Procedure

The President of the Atlanta chapter of a specific CASE user group was contacted and asked to review and consider a proposal for possible user group participation – After review by them, the proposal was referred to the National President who brought the proposal before the National Board of Directors. After deliberation, the Board agreed to national participation with the stipulation that the actual mailing list not be made available to the researcher due to the proprietary nature of the membership. In addition, the officials requested that the user group not to be explicitly named in the final document.

Survey packages were created, that included a cover page with instructions and an endorsement from user group officials, the survey, and a self-addressed, stamped envelope for return reply. The packages were sent to the user group headquarters for labeling and mailing. Two hundred individuals were randomly chosen from the membership list to participate in the study.

Seventy responses were received. Of these, one was returned with only demographic information and comments. In addition, three surveys were returned as ‘undeliverable.’

## 5. Research findings

## 5.1. The sample

The majority of the respondents were IS managers, analysts and consultants. Over 62% of the respondents' organization used 1 to 5 CASE tools, and over 73% had used CASE tools for over 3 years. (See Appendix B for descriptive statistics of the survey sample.)

Table 1  
Group means and standard deviation

<table><tr><td>Variable</td><td>Mean</td><td>Std Dev</td><td>Variance</td></tr><tr><td>QUALITY</td><td>4.6</td><td>1.6</td><td>2.5</td></tr><tr><td>PRODUCTIVITY</td><td>4.1</td><td>1.3</td><td>1.8</td></tr><tr><td>METHODOLOGY USE</td><td>4.6</td><td>1.4</td><td>1.9</td></tr><tr><td>PILOT PROJECT USE</td><td>4.9</td><td>1.6</td><td>2.4</td></tr><tr><td>TRAINING</td><td>5.1</td><td>1.2</td><td>1.5</td></tr><tr><td>CONSULTANT USE</td><td>4.0</td><td>1.6</td><td>2.5</td></tr><tr><td>MEASUREMENT USE</td><td>2.9</td><td>1.7</td><td>2.9</td></tr></table>

Number of Cases = 70.

## 5.2. Analysis

Multiple regression analysis was used to determine whether a relationship existed between dependent (criterion) and independent (predictor) variables – The “stepwise” method was used for entry of the predictor variables into the regression equation.

The analysis proved useful in determining which of the five variables predicted success of CASE via the perception of quality and productivity improvement. We conducted two regression analyses. In the first, the criterion variable was quality and in the second, the criterion variable was productivity. The predictor list was specified at five based on the independent variables. Table 1 summarizes the group means and standard deviations across each dependent and independent variable.

The first regression analysis performed was for the criterion variable quality. At the first step, use of methodology emerged as the predictor variable with an R value (for regression) of .46 and an R-squared value (the coefficient of determination) of .21. In step two, use of metrics was added to the regression equation and resulted in an R of .50 and an R-squared of .25 (see Table 2 (a)). Adding metrics to the regression equation increased the variability of quality by .04. The final regression equation for the criterion variable quality after stepwise elimination is (also see Table 2 (b)),

$$
\text { Quality } = 1. 9 + 0. 4 (\mathrm{X} 1) + 0. 2 (\mathrm{X} 2) + \mathrm{ei}\tag{1}
$$

where,

$$
\begin{array}{l l} \mathrm{X1=} & \text {Methodology Use} \\ \mathrm{X2=} & \text {Metrics or Measurement Use} \\ \mathrm{ei=} & \text {Error} \end{array}
$$

In summary, the success in methodology use itself accounted for roughly 21% success for the criterion variable quality. Adding metrics to the equation significantly increased the predictability of the equation. Together the two predictor variables accounted for 25% of the success of CASE for the criterion variable quality.

The second regression analysis performed was for the criterion variable productivity. In the first step, use of metrics emerged as the predictor variable with an R value of .47 and an R-squared value of .22. In step two, use of consultants was added to the regression equation and resulted in an R of .56 and an R-squared of .31. In step three, training was added to the regression equation and resulted in an R of .60 and an R-squared of .36. After the third variable was added to the equation, it increased the variability of productivity by .14 (see Table 3 (a)). The final regression equation for the criterion variable productivity after stepwise elimination is (also see Table 3 (b)),

Table 2  
(a) Multiple regression analysis. $^{a}$  
Dependent (criterion) variable = Quality

<table><tr><td>Criterion Variable</td><td>Predictor Variable</td><td>Step</td><td>Multiple R</td><td>R-Square Change</td><td>Bivariate Correlation</td></tr><tr><td rowspan="2">Quality</td><td>Methodology Use</td><td>1</td><td>.46</td><td>.21</td><td>.44</td></tr><tr><td>Measurement Use</td><td>2</td><td>.50</td><td>.25</td><td>.20</td></tr><tr><td colspan="6">(b) Regression model for Quality.  $^b$  Estimated model (Quality = 1.9 + 0.4(X1) + 0.2(X2) + ei)</td></tr><tr><td>Variable</td><td>Estimate</td><td>T-Statistic</td><td>Sig T</td><td></td><td></td></tr><tr><td>Methodology Use</td><td>0.4</td><td>3.6</td><td>.000</td><td></td><td></td></tr><tr><td>Measurement Use</td><td>0.2</td><td>2.0</td><td>.049</td><td></td><td></td></tr><tr><td>(Constant)</td><td>1.9</td><td>3.3</td><td>.001</td><td></td><td></td></tr></table>

$^{b}$ F(2,67 df) = 11.40.  
$^{a}$ Method: Stepwise Criteria PIN .05 POUT .10.

Productivity

$$
= 1. 1 + 0. 3 1 (\mathrm{Y} 1) + 0. 2 0 (\mathrm{Y} 2) + 0. 2 6 (\mathrm{Y} 3) + \mathrm{ei} \tag {2}\tag{2}
$$

where

$$
\begin{array}{l l} \text {Y1 =} & \text {Use of Metrics} \\ \text {Y2 =} & \text {Use of Consultants} \\ \text {Y3 =} & \text {Training} \\ \text {ei =} & \text {Error} \end{array}
$$

Use of metrics alone accounted for approximately 22% of the success of CASE for the criterion variable productivity. Adding consultants and training to the equation significantly increased the predictability of the equation and accounted for roughly 36% of the success of CASE for the criterion variable productivity.

For both the multiple regression equations, the coefficient for the predictors were significant at the .05 level.

## 5.3. Hypotheses testing

Hypothesis H1 was supported as a predictor of quality but not as a predictor of productivity. Hypothesis H2 was neither supported as a predictor of quality nor productivity. Hypothesis H3 was not supported as a predictor of quality but was supported as the number three predictor of productivity. Hypothesis H4 was not supported as a predictor of quality but was supported as the number two predictor of productivity. Hypothesis H5 was highly supported for both the dependent variables. It was supported as the number two predictor of quality and as the number one predictor of productivity.

In summary, the hypothesis related to “use of a development methodology” and “use of metrics” was supported as predictors of quality in a CASE environment. Additionally, the hypotheses related to “use of metrics,” “use of consultants” and “formal training” were supported as predictors of productivity in a CASE environment. Together, these supported hypotheses are “determinants of a successful computer-aided software engineering implementation strategy.”

Table 3  
(a) Multiple regression analysis. $^{a}$  
Dependent (criterion) variable = Productivity

<table><tr><td>Criterion Variable</td><td>Predictor Variable</td><td>Step</td><td>Multiple R</td><td>R-Square Change</td><td>Bivariate Correlation</td></tr><tr><td rowspan="3">Productivity</td><td>Measurement Use</td><td>1</td><td>.47</td><td>.22</td><td>.31</td></tr><tr><td>Consultant Use</td><td>2</td><td>.56</td><td>.31</td><td>.20</td></tr><tr><td>Training</td><td>3</td><td>.60</td><td>.36</td><td>.26</td></tr></table>

(b) Regression model for Productivity. $^{b}$

Estimated model (Productivity = 1.1 + 0.31 (Y1) + 0.20(Y2) + 0.26(Y3) + ei)

<table><tr><td>Variable</td><td>Estimate</td><td>T-Statistic</td><td>Sig T</td></tr><tr><td>Measurement Use</td><td>.31</td><td>3.9</td><td>.00</td></tr><tr><td>Consultant Use</td><td>.20</td><td>2.3</td><td>.02</td></tr><tr><td>Training</td><td>.26</td><td>2.3</td><td>.02</td></tr><tr><td>(Constant)</td><td>1.1</td><td>1.8</td><td>.07</td></tr></table>

$^{a}$ Method: Stepwise, Criteria PIN .05, POUT .10.  
$^{h}$ F(3,66 df) = 12.56.

## 6. Discussion

This study supports hypotheses that a CASE implementation strategy can be more successful with the presence of certain environmental conditions. The use and enforcement of a formal software development methodology and metrics have been supported as a determinant of a CASE implementation resulting in improved quality of software developed.

In an integrated CASE environment, all of the components of a model must fit together cohesively in order to generate a high-quality application. Fully integrated CASE tools often require that each layer of a work product be built upon the prior layer across all phases of the development life cycle. A formal development methodology adds the rigid processes and procedures necessary to ensure that this cohesion is enforced throughout the software development effort. Although the use of formal methods generally results in more time being expended due to the necessary inspections and supporting documentation inherent in such an approach, this research supports that the results will be a higher quality application. One notable benefit of following a formal methodology is that the resulting higher quality application generally requires less maintenance effort due to a reduced number of flaws initially built into the system. This may result in the recovery of a significant portion of the additional time expended and, more importantly, help to reduce the chance of a software flaw having a negative impact on the business process being supported.

The use of metrics in an integrated CASE environment is also important in terms of monitoring and improving the quality of software developed. As is widely agreed within the Total Quality Management (TQM) literature, in order to improve the quality of a process or product, one must first define the attributes or characteristics of quality in terms of indicators which can be continuously monitored. Without quantifiable measures, it may be difficult to monitor subtle improvements or declines in quality and take appropriate actions. As these metrics and the progress against them are communicated to developers, they provide a set of common goals to work towards and can contribute to a focus on quality that may not be as likely in an environment where quality is a subjective goal.

Just as the use of a formal development methodology and quality metrics have been supported as determinants of CASE implementation resulting in improved software quality, the use of productivity metrics and consultants with formal training in CASE development methods are supported as determinants of improved productivity of software developers.

As part of sound project management practices, a set of productivity metrics with close ties to a detailed project plan offer all resources a clear path towards the goal of completing the set of interim deliverables which make up a project phase. One could argue that the planning necessary to implement effective metrics may be more closely tied to improved productivity than the metrics themselves. Regardless, the metrics do provide a means to quantify the characteristics of productivity and to communicate progress to developers and management. It should be noted that blindly implementing metrics without regard to proper project planning and management can have a detrimental effect on the project rather than improving productivity.

Consultants can be retained to assist in project planning and management and to “coach and mentor” resources on effective CASE use. One of the key objectives of using consultants is to decrease the amount of time necessary to become sufficiently productive using the tool and in educating management on “best practices” regarding formulating and carrying out an effective project plan. Consultants can bring a wide variety of external experiences to a project and can directly impact the probability of success. A good consultant or group of consultants can have a positive impact on productivity by “jump starting” the development team with knowledge and experience.

Another way to avoid unnecessary delays in becoming a fully productive development team is to ensure that all resources have been sufficiently trained. This training should include not only tool training, but methodology training as well. It is important to recognize that there is much more to learning CASE than learning how to operate the tool. Just as learning to effectively operate a wrench does not make one a good auto mechanic, strictly learning to operate the CASE tool will not make one an effective CASE developer. The developer must understand what tasks will be undertaken, how those tasks fit into the larger picture, and what methods will be used to accomplish the tasks. A training program which includes methodology and tool training is desirable to achieve the goal of a well-prepared development team.

From a management perspective, all of the factors discussed should only be implemented as outlined by a carefully developed project strategy. This strategy should include a clear set of goals and objectives for the project and provisions for the proper assembly of appropriate tools, techniques, and resources which support the stated objectives.

This study focused on opinions of individuals who were involved in software development across many organizations throughout North America and which were found to be consistent with most previous findings. The results can be generalized to all development organizations in this geographical region.

## Appendix A. Survey

## A.1. Section I - Demographic information

G1 - The number of employees in my entire organization is: (circle only one)

(a) less than 500

(b) 500–999

(c) 1,000-4,999

(d) 5,000–9,999

(e) 10,000 +

G2 - The primary function of my department is: (circle only one)

(a) Software Development

(b) Data Administration

(c) Consulting Services

(d) Training Services

(e) Business Unit

(f) Other

G3 - My primary job function is: (circle only one)

(a) Analyst

(b) Consultant

(c) Trainer/Educator

(d) Management

(e) Other

G4 - The number of CASE tools currently in use by my entire organization is: (circle only one)

(a) 1-5

## A.2. Section II - Relative level of success

(b) 6-20

(c) 21-50

(d) 51-100

(e) 100- +

G5 - CASE tools are used in the following functional areas within my organization: (circle all that apply)

(a) Strategic Planning

(b) Project Management

(c) Data Analysis

(d) Process Analysis

(e) Code Generation

G6 - The number of years that my organization has been using CASE tools is: (circle only one)

(a) Less than 1

(b) 1-2

(c) 3-5

(d) 6 +

D1 - The organization with which I am associated is experiencing improved quality of software produced as a result of the implementation of Computer-Aided Software Engineering (CASE) tools. (circle only one)

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Strongly</td><td>Moderately</td><td>Mildly</td><td>Mildly</td><td>Moderately</td><td>Strongly</td></tr><tr><td>Disagree</td><td>Disagree</td><td>Disagree</td><td>Agree</td><td>Agree</td><td>Agree</td></tr></table>

Comments regarding software quality in your CASE environment:

D2 - The organization with which I am associated is experiencing improved productivity within the software development process as a result of the implementation of Computer-Aided Software Engineering (CASE) tools. (circle only one)

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Strongly</td><td>Moderately</td><td>Mildly</td><td>Mildly</td><td>Moderately</td><td>Strongly</td></tr><tr><td>Disagree</td><td>Disagree</td><td>Disagree</td><td>Agree</td><td>Agree</td><td>Agree</td></tr></table>

Comments regarding software quality in your CASE environment:

## A.3. Section III - Success factors

I1 - The organization with which I am associated enforces the use of at least one structured software development methodology. (circle only one)

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Strongly</td><td>Moderately</td><td>Mildly</td><td>Mildly</td><td>Moderately</td><td>Strongly</td></tr><tr><td>Disagree</td><td>Disagree</td><td>Disagree</td><td>Agree</td><td>Agree</td><td>Agree</td></tr></table>

Comments regarding software quality in your CASE environment:

I2 - The organization with which I am associated introduced CASE technology via at least one pilot project. (circle only one)

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Strongly</td><td>Moderately</td><td>Mildly</td><td>Mildly</td><td>Moderately</td><td>Strongly</td></tr><tr><td>Disagree</td><td>Disagree</td><td>Disagree</td><td>Agree</td><td>Agree</td><td>Agree</td></tr></table>

Comments regarding software quality in your CASE environment:

I3 - The organization with which I am associated provided formal training on software development techniques required to use CASE effectively. (circle only one)

<table><tr><td>1Strongly Disagree</td><td>2Moderately Disagree</td><td>3Mildly Disagree</td><td>4Mildly Agree</td><td>5Moderately Agree</td><td>6Strongly Agree</td></tr></table>

## Comments regarding software quality in your CASE environment:

I4 - The organization with which I am associated retains experienced CASE consultants to guide projects using CASE. (circle only one)

<table><tr><td>1Strongly Disagree</td><td>2Moderately Disagree</td><td>3Mildly Disagree</td><td>4Mildly Agree</td><td>5Moderately Agree</td><td>6Strongly Agree</td></tr></table>

Comments regarding software quality in your CASE environment:

I5 - The organization with which I am associated makes use of standard measurements to improve the effectiveness of the software development process. (circle only one)

<table><tr><td>1StronglyDisagree</td><td>2ModeratelyDisagree</td><td>3MildlyDisagree</td><td>4MildlyAgree</td><td>5ModeratelyAgree</td><td>6StronglyAgree</td></tr></table>

Comments regarding software quality in your CASE environment:

## Appendix B. Sample demographics

Number of employees in participant's entire organization:

<table><tr><td>category</td><td>respondents</td><td>percentage</td></tr><tr><td>0–499</td><td>12</td><td>17%</td></tr><tr><td>500–999</td><td>5</td><td>7%</td></tr><tr><td>1000–4999</td><td>15</td><td>21%</td></tr><tr><td>5000–9999</td><td>12</td><td>17%</td></tr><tr><td>10000 +</td><td>26</td><td>37%</td></tr></table>

## 70 Total Respondents

Primary function of participant's department:

<table><tr><td>category</td><td>respondents</td><td>percentage</td></tr><tr><td>Software Development</td><td>42</td><td>59%</td></tr><tr><td>Data Administration</td><td>10</td><td>14%</td></tr><tr><td>Consulting Services</td><td>12</td><td>17%</td></tr><tr><td>Training Services</td><td>0</td><td>0%</td></tr><tr><td>Business Unit</td><td>2</td><td>3%</td></tr><tr><td>Other</td><td>8</td><td>11%</td></tr></table>

70 Total Respondents (some chose more than one category)

Primary job function of participant:

<table><tr><td>category</td><td>respondents</td><td>percentage</td></tr><tr><td>Analyst</td><td>19</td><td>27%</td></tr><tr><td>Consultant</td><td>11</td><td>16%</td></tr><tr><td>Trainer/Educator</td><td>3</td><td>4%</td></tr><tr><td>Management</td><td>37</td><td>52%</td></tr><tr><td>Other</td><td>1</td><td>1%</td></tr></table>

70 Total Respondents (some chose more than one category)

Number of CASE tools currently in use throughout organization:

<table><tr><td>category</td><td>respondents</td><td>percentage</td></tr><tr><td>1–5</td><td>44</td><td>63%</td></tr><tr><td>6–20</td><td>12</td><td>17%</td></tr><tr><td>21–50</td><td>5</td><td>7%</td></tr><tr><td>51–99</td><td>3</td><td>4%</td></tr><tr><td>100–+</td><td>8</td><td>11%</td></tr></table>

70 Total Respondents (some chose more than one category)

Functional use of CASE tools throughout organization:

<table><tr><td>category</td><td>respondents</td><td>percentage</td></tr><tr><td>Strategic Planning</td><td>42</td><td>59%</td></tr><tr><td>Project Management</td><td>26</td><td>37%</td></tr><tr><td>Data Analysis</td><td>69</td><td>97%</td></tr><tr><td>Process Analysis</td><td>66</td><td>93%</td></tr><tr><td>Code Generation</td><td>64</td><td>90%</td></tr></table>

70 Total Respondents (most chose more than one category)

Number of years organization has been using CASE:

<table><tr><td>category</td><td>respondents</td><td>percentage</td></tr><tr><td>less than 1</td><td>0</td><td>0%</td></tr><tr><td>1–2</td><td>18</td><td>25%</td></tr><tr><td>3–5</td><td>41</td><td>58%</td></tr><tr><td>6–+</td><td>12</td><td>17%</td></tr></table>

70 Total Respondents

## References

[1] Brisebois, R. and Dion, P. “Implementing CASE: Six critical factors,” Computing Canada, 16, 11, May 24, 1990, pp. 21–22.

[2] Brooks, F.P., Jr. The Mythical Man-month. Addison-Wesley, Massachusetts, 1975.

[3] Card, D.N., McGarry, F.E. and Page, G.T. “Evaluating software engineering technologies,” IEEE Transactions – Software Engineering, 13, 7, July, 1987, pp. 845–851.

[4] Corbitt, G.F., Norman, R.J. and Butler, M.C. “Assessing proximity to fruition: A case study of phases in CASE technology transfer,” International Journal of Software Engineering, 1, 2, June, 1991, pp. 189–201.

[5] Du Plessis, A.L. "A method for CASE tool evaluation," Information & Management, 25, 2, August 1993, pp. 93–102.

[6] Forte, G. and Norman, R.J. “A self-assessment of the software engineering community,” Communications of the ACM, 35, 4, April, 1992, pp. 28–32.

[7] Hughes, C. and Clark, J.D. “The stages of CASE usage,” Datamation, 36, 3, February 1, 1990, pp. 41–44.

[8] Huff, C.C. “Elements of a realistic CASE tool adoption budget,” Communications of the ACM, 35, 4, April, 1992, pp. 45–54.

[9] Humphrey, W. “Characterizing the software process: A maturity framework,” IEEE Software, March, 1988, pp. 73–79.

[10] Humphrey, W., Snyder, T.R. and Willis, R.R. “Software process improvement at hughes aircraft,” IEEE Software, July, 1991, pp. 11–23.

[11] Jones, C. Applied Software Measurement: Assuring Productivity and Quality. McGraw-Hill, Inc, New York, 1991.

[12] Jones, M.C. and Arnett, K.P. “CASE use is growing, but in surprising ways: Most mature IS organizations still use case tools to help with administrative dirty work and not for full-blown applications design,” Datamation, 38, 10, May 1, 1992, pp. 108–109.

[13] Jones, C. “CASE’s missing elements: key functions must be added to computer-aided software engineering tools, and thorough training is needed in their use,” IEEE Spectrum, 29, 6, June, 1992, pp. 38–41.

[14] Lemmp, P. and Lauber, R. “What productivity increases to expect from a CASE environment: Results of a user survey,” In Productivity: Progress, Prospects, and Payoff, Proceedings of 27th Annual Technical Symposium, June 9, 1988, pp. 13-19.

[15] Major, M.J. “The unresolved case: CASE promises great productivity, but users still are awaiting the evidence,” Midrange Systems, 5, 8, April 28, 1992, pp. 25–28.

[16] McLure, C. “The CASE for structured development,” PC Technology Journal, August, 1988, pp. 51–67.

[17] McNurlin, B.C. and Sprague, R.H., Jr. Information Systems in Practice (2nd ed.). Prentice Hall, New Jersey, 1989.

[18] Merritt, P. "CASE and culture – Observations on technology transfer," CASE '88 Advance Working Papers, International Workshop on CASE, July, 1988, pp. 14–16.

[19] Moad, J. “The software revolution,” Datamation, 36, 4, February 15, 1990, pp. 22–28.

[20] Norman, R.J., Corbitt, G.F., Butler, M.C. and McElroy, D.D. "CASE technology transfer: A case study of unsuccessful change," Journal of Systems Management, May, 1989, pp. 33–37.

[21] Norman, R.J. and Nunamaker Jr., J.F. “CASE productivity perceptions of software engineering professionals,” Communications of the ACM, 32, 9, September, 1989, pp. 1102–1108.

[22] Pfleeger, S.L. and McGowan, C. "Software metrics in the process maturity framework," Journal of Systems Software, 12, 1991, pp. 255–261.

[23] Pressman, R.S. Software Engineering: A Practitioner's Approach. Prentice Hall, New Jersey, 1982.

[24] Rubin, H. “How to become a software engineering ‘Bigfoot’,” American Programmer, January, 1990.

[25] Second Annual Report on CASE. CASE Research Corporation, Bellevue, Washington, 1991.

[26] Sorensen, K. “Despite of a slow start, CASE goes the distance,” Digital Review, October 2, 1989.

[27] Tate, G., Verner, G. and Jeffery, R. “CASE: A testbed for modeling, measurement and management,” Communications of the ACM, 35, 4, April, 1992, pp. 65–72.

[28] Vessey, I., Jarvenpaa, S. and Tractinski, N. “Evaluation of vendor products: CASE tools as methodology companions,” Communications of the ACM, 35, 4, April, 1992, pp. 90–105.

[29] Yourdon, E. “What ever happened to structured analysis?,” Datamation, June 1, 1986, pp. 133–138.

![](/api/attachments/YUZY5WVS/fulltext/images/e43747b40f660ca54ca56420dd9f1cf5f358228d69191985ad875b0bc96dcae3.jpg)

Robert Urwiler is a Management Consultant with Price Waterhouse, LLP in Atlanta, Georgia, an adjunct instructor of Business Administration at Brenau University, and a doctoral candidate at Nova Southeastern University. He has been involved in custom software development using CASE and structured techniques for over ten years and has published in the Journal of Strategic Information Systems, the Journal of Systems Management, and others. He can

be reached via email at Urwiler@lib.brenau.edu.

![](/api/attachments/YUZY5WVS/fulltext/images/9b5fe0b1738cd33bcb0906d45378742b4b8958dac334965920d6a9588b538c8f.jpg)

Narender K. Ramarapu is an Assistant Professor of Management Information Systems in the Department of Management at The University of Tennessee at Martin. He received his Ph.D. in MIS from The University of Memphis. His current research is in the areas of Human Information Processing, Hypertext/Hypermedia, Integrated CASE and Global Information Systems. He has published in the Journal of Information Systems Management, Journal of Sys-

tems Management, International Journal of Operations and Production Management, Journal of Information Technology and others.

![](/api/attachments/YUZY5WVS/fulltext/images/defd193ee2602fa4a927899ff19815c4125d5a4c36e964570c4b8537f2393015.jpg)

Ronald B. Wilkes is an Associate Professor of Management Information Systems in the Fogelman College of Business and Economics at The University of Memphis. He received his Ph.D. in Management Information Systems from The University of Minnesota. His primary research interests are in management of the information technology resource. Prior to entering academia, Ronnie was Vice President of Systems for Data Communications Corporation,

Memphis and Vice President of Development for Cylix Communications, Memphis.

![](/api/attachments/YUZY5WVS/fulltext/images/7072f5efb7e523d9b01d63da15099b51bd87146e835ada4df12e5b17ce47f48d.jpg)

Mark N. Frolick, Ph.D. is an Associate Professor of Management Information Systems and the Associate Director of the FedEx Center for Cycle Time Research at The University of Memphis. His research interest include executive information systems, cycle time reduction, systems development, and telecommuting. He has published in MIS Quarterly, Journal of Management Information Systems, Journal of Information Systems Management, and the Journal

of Strategic Information Systems, among other journals. He also helped establish a new journal entitled Cycle Time Research.
