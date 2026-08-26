---
otero_id: 21614
otero_key: "96ZKND8E"
title: "Contributors to quality during software maintenance"
authors: "Mehdi Ghods; Kay M Nelson"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00051-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Contributors to quality during software maintenance <sup>1</sup>

Mehdi Ghods <sup>a,)</sup>, Kay M. Nelson <sup>b,2</sup>

Boeing, P.O. Box 24346, Seattle, WA 98124, USA

<sup>b</sup> DiÕision of Accounting and Information Systems, The UniÕersity of Kansas, Summerfield 350B, Lawrence, KS 66045, USA

## Abstract

Software maintenance is a costly, yet often neglected part of the development life-cycle. This study evaluates factors that contribute to quality during maintenance. Quality is measured as quality of application maintenance, overall application quality during maintenance, and quality of maintenance changes. Quality is also measured objectively as number of failures and defects per month. The findings of this study indicate that design for maintainability in software development positively impacts quality during the maintenance phase of the life-cycle. The relationship and coordination between maintainers and users is also a key quality factor. Reuse within an application and from other applications also positively impacts quality, as do the structured design techniques of independence and consistency of data elements. The use of a structured methodology was found to reduce code and design defects in large applications. CASE tools, however, showed no significant impacts on any of the quality metrics in this study. Surprisingly, the technical expertise of the software maintenance team and the business expertise of the users showed a negative quality impact, possibly due to the respondents of the study incorrectly identifying experts or fully understanding expertise. User controlled data tables also showed a negative impact on overall maintenance quality. These results indicate that a well designed application combined with a strong maintainer–user bond can result in quality software maintenance. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Software quality; Software maintenance; Reusable software; Structured methods

## 1. Introduction

Quality is one of the most sought after dimensions of the business software applications that organizations depend on today. Despite this high demand for quality, very few studies have been done that evaluate the ongoing quality of software applications during the maintenance portion of the system life-cycle. This study seeks to understand the practices and techniques that lead to high quality software maintenance.

Studies that take the application development view of software seem to address maintenance as an afterthought of development rather than a critical and expensive part of the total system life-cycle. For example, Dekleva 4 evaluates how the choice of <sup>w</sup> <sup>x</sup> development approach will influence maintenance. Perry 13 addresses maintenance quality in the con- <sup>w</sup> <sup>x</sup> text of development quality. The maintenance phase of the life-cycle is a natural and necessary part of the system operation 2 . A number of studies show that <sup>w</sup> <sup>x</sup> this phase is highly costly and consumes most of the resources needed for a software application 6,8 . It<sup>w</sup> <sup>x</sup> is clear that maintenance must be given specific consideration when business objectives for information systems include improvements in cost, quality and productivity.

Table 1  
Age of systems by organization

<table><tr><td>ORG</td><td>No. of systems</td><td>No. &lt; 1 year</td><td>No. 1–3 years</td><td>No. &gt; 3–5 years</td><td>No. &gt; 5–10 years</td><td>No. &gt; 10 years</td></tr><tr><td>101</td><td>35</td><td>5</td><td>6</td><td>8</td><td>6</td><td>10</td></tr><tr><td>102</td><td>5</td><td>0</td><td>1</td><td>2</td><td>2</td><td>0</td></tr><tr><td>103</td><td>5</td><td>0</td><td>3</td><td>0</td><td>1</td><td>1</td></tr><tr><td>104</td><td>14</td><td>2</td><td>1</td><td>0</td><td>3</td><td>8</td></tr><tr><td>105</td><td>9</td><td>0</td><td>0</td><td>3</td><td>1</td><td>5</td></tr><tr><td>106</td><td>5</td><td>1</td><td>2</td><td>2</td><td>0</td><td>0</td></tr><tr><td>107</td><td>3</td><td>0</td><td>0</td><td>2</td><td>0</td><td>1</td></tr><tr><td>108</td><td>5</td><td>0</td><td>1</td><td>2</td><td>2</td><td>0</td></tr><tr><td>109</td><td>4</td><td>0</td><td>0</td><td>2</td><td>2</td><td>0</td></tr><tr><td>110</td><td>8</td><td>1</td><td>1</td><td>1</td><td>4</td><td>1</td></tr><tr><td>111</td><td>18</td><td>1</td><td>3</td><td>4</td><td>6</td><td>4</td></tr><tr><td>112</td><td>5</td><td>1</td><td>1</td><td>3</td><td>0</td><td>0</td></tr><tr><td>Total</td><td>116</td><td>11</td><td>19</td><td>29</td><td>27</td><td>30</td></tr><tr><td>%</td><td></td><td>9.48%</td><td>16.38%</td><td>25.00%</td><td>23.28%</td><td>25.86%</td></tr></table>

The quality of software product maintenance can be measured from several different perspectives. Previously, emphasis has been placed primarily on the use of exclusively technical metrics to evaluate software quality 7,15 . An example of these technical<sup>w</sup> <sup>x</sup> metrics is the combination of defects, size, readability, and complexity metrics, and some process attributes in a measure of maintainability 7 .

Reuse and reusability can also be used as quality factors for software development and maintenance. Reuse has been shown to increase productivity and improve quality while reducing effort and time 10 .<sup>w</sup> <sup>x</sup> Davis and Williams 3 consider reuse as an ‘en- <sup>w</sup> <sup>x</sup> abling technology’ for improving quality and reducing cost. In the same spirit, adherence to structured methods and analysis 6 and management of the<sup>w</sup> <sup>x</sup> change request process 9 have also been shown as<sup>w</sup> <sup>x</sup> ways of measuring quality during software maintenance.

From the user’s perspective, four quality factors: reliability, maintainability, reusability and extendibility, are assumed to strongly contribute to the quality of the software product 11 . These factors are con-<sup>w</sup> <sup>x</sup> sidered as application independent and, therefore, applicable to all types of software applications. However, building these factors into a software application can be costly. The effort and cost of adding these types of factors to the software application must be justified by benefits such as maintenance productivity.

Coordination between the users of software applications and the maintainers who support these applications is critical to ongoing quality 5 . Barriers to<sup>w</sup> <sup>x</sup> quality can arise when changes to the technology are not agreed upon or mutually understood 1 . Stan-<sup>w</sup> <sup>x</sup> dards agreed to and used by both groups can enhance the coordination between these groups 14 .<sup>w</sup> <sup>x</sup>

Table 2  
System Language by Organization systems may be written in Ž more than one language.

<table><tr><td>ORG</td><td>No. of systems</td><td>Cobol</td><td>Fortran</td><td>C</td><td>Object oriented</td><td>Other</td></tr><tr><td>101</td><td>35</td><td>16</td><td>4</td><td>5</td><td>5</td><td>19</td></tr><tr><td>102</td><td>5</td><td>0</td><td>2</td><td>0</td><td>0</td><td>3</td></tr><tr><td>103</td><td>5</td><td>2</td><td>0</td><td>0</td><td>2</td><td>3</td></tr><tr><td>104</td><td>14</td><td>11</td><td>0</td><td>0</td><td>0</td><td>3</td></tr><tr><td>105</td><td>9</td><td>9</td><td>0</td><td>0</td><td>0</td><td>3</td></tr><tr><td>106</td><td>5</td><td>3</td><td>0</td><td>0</td><td>1</td><td>2</td></tr><tr><td>107</td><td>3</td><td>2</td><td>0</td><td>0</td><td>0</td><td>3</td></tr><tr><td>108</td><td>5</td><td>3</td><td>0</td><td>0</td><td>0</td><td>2</td></tr><tr><td>109</td><td>4</td><td>0</td><td>3</td><td>0</td><td>0</td><td>1</td></tr><tr><td>110</td><td>8</td><td>1</td><td>4</td><td>4</td><td>0</td><td>4</td></tr><tr><td>111</td><td>18</td><td>10</td><td>0</td><td>0</td><td>1</td><td>8</td></tr><tr><td>112</td><td>5</td><td>0</td><td>0</td><td>0</td><td>1</td><td>5</td></tr><tr><td>Total</td><td>116</td><td>57</td><td>9</td><td>9</td><td>10</td><td>58</td></tr><tr><td>%</td><td></td><td>49.14%</td><td>11.21%</td><td>7.76%</td><td>8.62%</td><td>48.28%</td></tr></table>

Table 3  
System Platform by Organization systems may run on than one Ž platform.

<table><tr><td>ORG</td><td>No. of systems</td><td>Mainframe</td><td>Work station</td><td>Client server</td><td>PC</td></tr><tr><td>101</td><td>35</td><td>20</td><td>3</td><td>12</td><td>3</td></tr><tr><td>102</td><td>5</td><td>4</td><td>1</td><td>2</td><td>0</td></tr><tr><td>103</td><td>5</td><td>3</td><td>0</td><td>2</td><td>0</td></tr><tr><td>104</td><td>14</td><td>13</td><td>0</td><td>0</td><td>1</td></tr><tr><td>105</td><td>9</td><td>9</td><td>0</td><td>4</td><td>0</td></tr><tr><td>106</td><td>5</td><td>4</td><td>0</td><td>1</td><td>0</td></tr><tr><td>107</td><td>3</td><td>1</td><td>2</td><td>1</td><td>2</td></tr><tr><td>108</td><td>5</td><td>4</td><td>0</td><td>0</td><td>1</td></tr><tr><td>109</td><td>4</td><td>1</td><td>0</td><td>2</td><td>1</td></tr><tr><td>110</td><td>8</td><td>4</td><td>4</td><td>2</td><td>4</td></tr><tr><td>111</td><td>18</td><td>14</td><td>0</td><td>0</td><td>4</td></tr><tr><td>112</td><td>3</td><td>3</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Total</td><td>116</td><td>80</td><td>10</td><td>27</td><td>17</td></tr><tr><td>%</td><td></td><td>68.97%</td><td>8.62%</td><td>23.28%</td><td>14.66%</td></tr></table>

This study takes a maintenance view of quality including development for maintainability as a factor that contributes to maintenance quality. Among the contributing quality factors investigated in this research are data consistency and independence, design for change and reuse, as well as maintenance practices such as tool and method use and coordination with users.

## 2. Research method

To test software maintenance quality, data was collected from both users and maintainers of software systems, as well as from I<sup>r</sup>S managers and the user managers supported by the software. In this study, we considered a global definition for user<sup>r</sup> customer as set forth by Xenos and Christodoulakis <sup>w</sup> <sup>x</sup> 16 . User<sup>r</sup>customer, in this fashion, is defined to include team members in the successive phases of application life-cycle, in addition to the end-user. The maintainer of an application, for example, is the receiver of the deliverables from the development and implementation teams, and, therefore, a user<sup>r</sup>customer for those team members. Our method, therefore, included the measurement of the maintenance factors from the perception of the maintainer, as well as the end-user. Quality performance data was collected from I<sup>r</sup>S managers and user managers as ‘stakeholders’ of the systems studied. The questions used to collect this data can be found in Appendix A of this paper.

Altogether, 236 maintainer, 236 user, 118 I<sup>r</sup>S manager, 118 user manager, and 118 metrics questionnaires were distributed. The final number of projects responding was 116, which is the n for the study. Regression analysis and analysis of variance Ž . ANOVA are used to analyze the data obtained.

Three different perceptual indicators of quality were used to assess I<sup>r</sup>S team performance; quality of application maintenance, overall application quality, and quality of maintenance changes. In addition, objective defect and failure data was taken from actual number of defects and failures per month, collected by the maintenance teams.

The indicators were derived from the quality factors of reliability and maintainability as proposed by Kitchenham 11 and Khoshgoftaar, Szabo and<sup>w</sup> <sup>x</sup> Woodcock 9 . Design for change is also measured<sup>w</sup> <sup>x</sup> as an independent variable as a potential contributor to maintainability. Reuse, as proposed as a quality factor by Kitchenham 11 , is measured as an inde- <sup>w</sup> <sup>x</sup> pendent indicator of quality, as are the use of tools and structured methods 6 . Structured methods tech-<sup>w</sup> <sup>x</sup> niques measured included such items as the independence of data from code and consistency of data elements, use of CASE tools, and use of libraries.

Table 4  
System size by organization

<table><tr><td>ORG</td><td>No. of systems</td><td>Small (&lt; 300 FP)</td><td>Medium (300–2000 FP)</td><td>Large (&gt; 2000 FP)</td></tr><tr><td>101</td><td>35</td><td>4</td><td>20</td><td>11</td></tr><tr><td>102</td><td>5</td><td>0</td><td>3</td><td>2</td></tr><tr><td>103</td><td>5</td><td>1</td><td>3</td><td>1</td></tr><tr><td>104</td><td>14</td><td>2</td><td>7</td><td>5</td></tr><tr><td>105</td><td>9</td><td>0</td><td>5</td><td>4</td></tr><tr><td>106</td><td>5</td><td>0</td><td>2</td><td>3</td></tr><tr><td>107</td><td>3</td><td>1</td><td>1</td><td>1</td></tr><tr><td>108</td><td>5</td><td>1</td><td>2</td><td>2</td></tr><tr><td>110</td><td>8</td><td>1</td><td>4</td><td>3</td></tr><tr><td>111</td><td>18</td><td>2</td><td>6</td><td>10</td></tr><tr><td>112</td><td>3</td><td>1</td><td>3</td><td>1</td></tr><tr><td>113</td><td>4</td><td>2</td><td>1</td><td>1</td></tr><tr><td rowspan="2">Total %</td><td>116</td><td>15</td><td>57</td><td>44</td></tr><tr><td></td><td>12.93%</td><td>49.14%</td><td>37.93%</td></tr></table>

Table 5  
Quality factors all size systems regression analysis

<table><tr><td>Independent variable(s)</td><td>Dependent variable</td><td> $R^{2}$ </td><td> $F$  value</td><td>Significance</td></tr><tr><td>Reuse within the application</td><td>Overall quality</td><td>0.053</td><td>6.74</td><td>0.05</td></tr><tr><td>Reuse from other applications and independent data elements</td><td>Overall quality</td><td>0.087</td><td>5.94</td><td>0.01</td></tr><tr><td>User controlled data tables (-) and independent data elements</td><td>Overall quality</td><td>0.112</td><td>7.44</td><td>0.01</td></tr><tr><td>Consistency of data across application</td><td>Overall quality</td><td>0.151</td><td>12.2</td><td>0.01</td></tr><tr><td>Consistency of data across application and coordination and expertise (-)</td><td>Quality of changes</td><td>0.090</td><td>2.22</td><td>0.10</td></tr></table>

Whether a formal structured methodology was used during maintenance was also considered. In addition, the level of coordination between users and maintainers is also measured as a potential contributor to maintenance quality. All variables are rated on a 1–7 Likert rating scale. The respondents for the independent variables were I<sup>r</sup>S maintainers and users while the dependent quality performance variables were rated by I<sup>r</sup>S and user managers acting as stakeholders.

For each represented software system, information was collected from expert respondents: one or two maintainers and one or two users of the system. Two maintainer questionnaires were provided by 46.6% of the organizations and two user questionnaires were provided by 41.3% of the organizations. These expert informants each provided knowledge of the nature and role of the software system in use and the purpose and nature of the business process. Indicators of software maintenance performance are tested for validity using respondents from both the I<sup>r</sup>S and user sides of the system. Performance criteria measures are taken from a survey given to I<sup>r</sup>S manager and user manager stakeholders Appendix Ž A ..

The basic design of this research is a cross-sectional field study. The sample was drawn from twelve organizations. These organizations were chosen for industry diversity, ease of data collection, and availability of metrics information, making this a convenience sample. The software systems included in the study represent a wide variety of ages, sizes, programming languages, and hardware platforms. The ages of the systems in the study vary from six months to thirty years old. The sizes range from 130 function points to over 10 000 function points. The programming languages range from mainframe IMS and DB2 to PC Oracle and FoxPro. The hardware platforms the software systems are running on include mainframes, workstations, client<sup>r</sup>server installations, personal computers, and radio frequency installations. Tables 1–4 list the age, language, platform, and size of the software systems by organization.

## 3. Results

## 3.1. Quality factors all size systems ( )

Reuse within the application contributes to overall quality of the application being maintained Table 5 .Ž .

Additionally, reuse from other applications and independence of data elements have a positive impact on overall quality. User controlled data tables negatively impact overall quality, while the independence of data elements from the code and the consistency of those data elements positively impact overall quality and the quality of system maintenance.

Table 6  
Quality factors small and medium systems regression analysis

<table><tr><td>Independent variable(s)</td><td>Dependent variable</td><td> $R^{2}$ </td><td>F value</td><td>Significance</td></tr><tr><td>Consistency of data across application</td><td>Quality of system maintenance</td><td>0.161</td><td>15.6</td><td>0.00</td></tr><tr><td>Design for maintainability and structured design</td><td>Quality of changes</td><td>0.299</td><td>14.23</td><td>0.00</td></tr></table>

Table 7  
Quality factors large systems regression analysis

<table><tr><td>Independent variable(s)</td><td>Dependent variable</td><td> $R^{2}$ </td><td>F value</td><td>Significance</td></tr><tr><td>Consistency of data across application</td><td>Quality of system maintenance</td><td>0.080</td><td>4.38</td><td>0.05</td></tr><tr><td>Design for maintainability</td><td>Overall quality</td><td>0.174</td><td>9.43</td><td>0.01</td></tr></table>

Coordination between users and maintainers positively contributes to the quality of changes, while the expertise of maintainers and users negatiÕely relates to quality of maintenance changes. This model, however, is not statistically significant at the 0.05 level, therefore this result needs more empirical investigation in future studies.

## 3.2. Quality factors systems( ) <sup>-</sup> 2000 fps

In small and medium size systems, development factors appear to be the key to the quality of changes and quality of systems maintenance. The indepen dence and consistency of data elements in a software application positively impact the quality of system maintenance Table 6 .Ž .

The design for maintainability measures of design for change and the use of structured design positively impact the quality of changes made to small and medium sized applications.

## 3.3. Quality Factors systems( ) <sup>)</sup> 2000 fps

Independence and consistency of data elements positively contribute to the quality of systems maintenance in large software applications Table 7 .Ž .

Design for maintainability and change during the application development process also has a positive relationship to the overall quality of these large applications.

## 4. Defect and failure analysis

The use of a structured methodology was the only factor in this study that had an impact on the objective measures of software quality: defects and failures Table 8 . In these areas, significant differencesŽ . were found between number of design defects found per month in the structured methods large size projects compared to those systems not maintained with structured methods.

Table 8  
Failure and defect analysis ANOVA one way Ž .

<table><tr><td>Variable</td><td>F</td><td>Sig.</td></tr><tr><td>Failures per month &lt; 300 function points</td><td>0.64</td><td>0.44</td></tr><tr><td>Failures per month 300–2000 function points</td><td>0.13</td><td>0.72</td></tr><tr><td>Failures per month &gt; 2000 function points</td><td>1.97</td><td>0.17</td></tr><tr><td>Code defects discovered per month &lt; 300 function points</td><td>0.31</td><td>0.59</td></tr><tr><td>Code defects discovered per month 300–2000 function points</td><td>0.74</td><td>0.39</td></tr><tr><td>Code defects discovered per month &gt; 2000 function points</td><td>4.92</td><td>0.03</td></tr><tr><td>Design defects discovered per month &lt; 300 function points</td><td>0.06</td><td>0.82</td></tr><tr><td>Design defects discovered per month 300–2000 function points</td><td>1.17</td><td>0.28</td></tr><tr><td>Design defects discovered per month &gt; 2000 function points</td><td>2.41</td><td>0.10</td></tr><tr><td>Other defects discovered per month &lt; 300 function points</td><td>0.53</td><td>0.48</td></tr><tr><td>Other defects discovered per month 300–2000 function points</td><td>1.96</td><td>0.17</td></tr><tr><td>Other defects discovered per month &gt; 2000 function points</td><td>2.61</td><td>0.11</td></tr></table>

## 5. Summary and conclusions

This study finds that structured design, independence and consistency of data elements, and design for change during the development process are positively related to software maintenance quality. Reuse was also found to positively impact quality when exercised within the application or from other applications. The case of designing and maintaining for others to reuse code modules or objects from one’s own application showed no significant impacts on quality. This result is somewhat surprising. It appears that having to maintain for reuse by several outside applications may result in compromises, resulting in this type of reuse having no relationship to quality. It is possible that the generic nature of code, modules or objects designed for multiple reuse may result in a slightly overall lower quality level than reuse within only one system.

The results of this study also indicate that the existing findings on software quality during the development process can legitimately be extended to ongoing maintenance. Maintainer–user coordination is key to achieving quality goals during maintenance. CASE tools, however, showed no significant impacts on any of the quality metrics in this study. This indicates that the use of these tools needs to be examined for appropriateness to the maintenance task and need to be evaluated for real contributions to the quality of the maintenance process. It is possible that these tools may pay off in different performance areas.

The use of a structured methodology is only shown to have a significant impact in large projects in the areas of code and design defects. This may indicate that structured methods are more appropriate for projects of this size. Since the structured methodology studied had only been in use for less than two years, it is possible that a learning curve exists based on the size of application maintained, and that small projects will see reduced failures and defects sometime in the future.

Surprisingly, the technical expertise of the software maintenance team and the business expertise of the users was found to have a negative quality impact in this study. This indicates a need to reevaluate the impact and measurement of expertise. Following the analysis of the data in this study, a feedback session was held with maintainers and users of the systems studied. These subjects indicated that these negative results may stem from expertise being rated by peers as longevity and tenure in the job rather than as true technical or business skills. When asked what I<sup>r</sup>S maintenance expertise looked like, the respondents were unable to give clear answers. It was their consensus that only the experts themselves could articulate the characteristics of maintainer expertise. These discussions have led to an in depth qualitative investigation of maintainer expertise 12 .<sup>w</sup> <sup>x</sup>

User controlled data tables also showed a negative impact on overall quality. It is possible that this negative relationship stems from users being inadequately trained in making data table changes. Poorly or erroneously made data changes could readily result in quality problems in the system.

The use of a structured methodology is only having a significant impact in large projects in the areas of code and design defects. This may indicate that structured methods are more appropriate for this size of projects. Since the structured methodology used in the analysis was in operation for less than two years, it is also possible that a learning curve exists based on the size of application maintained, and that small and medium projects will see reduced failures and defects sometime in the future.

This study has demonstrated that the techniques used in both software development and software maintenance significantly impact quality during the maintenance phase of the life-cycle. The relationship and coordination between maintainers and users is also a key quality factor. It appears that a well designed application combined with a strong maintainer–user bond can result in quality software maintenance.

## Appendix A. Questions

## A.1. Questions rated by users and maintainers

Please rate each of these statements on the scale proÕided. Read each question individually before answering. Refer to the same software application and business process<sup>r</sup>task throughout this questionnaire.

Thank You

<table><tr><td colspan="2">Scale</td></tr><tr><td>N/A</td><td>Not Applicable</td></tr><tr><td>1</td><td>Non-Existent</td></tr><tr><td>2</td><td>Very Weak</td></tr><tr><td>3</td><td>Weak</td></tr><tr><td>4</td><td>About Average</td></tr><tr><td>5</td><td>Strong</td></tr><tr><td>6</td><td>Very Strong</td></tr><tr><td>7</td><td>Extremely Strong</td></tr></table>

Communication between the I<sup>r</sup>S and user organization in making changes to this application is:

The modularity of this application is:

The way that data elements are represented the same in this application and related software applications is:

The user’s level of knowledge about their business is:

The design of this application into logical subsystems, modules, or functions is:

The degree to which this application can be modified is:

The ease with which programming changes can be made to this application is:

The way that a data item such as ‘customer’ is consistently represented in this application is:

The independence of subsystems, modules, or functions in this application is:

The degree to which modifications can be readily made to this application is:

The built-in capacity of this application to be changed is:

Cooperation between the I<sup>r</sup>S and user organization in making changes to this application is:

The consistency of data across this application is:

The degree to which the I<sup>r</sup>S support group and users of this software application work as a team in making changes to this application is:

The break down of this application into subsystems, modules, or functions is:

The uniformity in the way data is represented across this software application is:

The degree to which the design of this application has the potential to be changed is:

The ability to add, change, or delete data elements in this application is:

The I<sup>r</sup>S support group’s knowledge about this software application is:

The way that the I<sup>r</sup>S support group and users of this application communicate on changes to the system is:

The degree to which data elements are consistent across this application is:

The organization of this software application into identifiable subsystems, modules, or functions is:

The degree to which this software application can be modified is:

The degree to which data is stored independent of programs in this application is:

Coordination between the I<sup>r</sup>S and user organization in making changes to this application is:

The degree to which the design of this application can be readily changed is:

The way that information in this application is divided into subsystems, modules, or functions is:

The division of this application into subsystems, modules, or functions is:

A.2. Questions rated by ‘stakeholder’ I<sup>r</sup>S managers and user managers

Performance Characteristics: Please rate the performance of the following characteristics of the software application you support:

<table><tr><td>not applicable</td><td colspan="4">low</td><td colspan="3">moderate</td><td>high</td></tr><tr><td>N/A</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td></td></tr></table>

Overall quality\_\_\_

Quality of changes performed by the I<sup>r</sup>S staff\_

Response Characteristics: Please rate your I<sup>r</sup>S maintenance group on the following characteristics.

<table><tr><td>not applicable</td><td colspan="4">low</td><td colspan="3">moderate</td><td>high</td></tr><tr><td>N/A</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td></td></tr></table>

Quality of system maintenance

Delivery of quality systems<sup>r</sup>maintenance

Objective Measures of Defects and Failures:

INSTRUCTIONS: Defect and Cycle Time Collection

Defect Collection Instructions:

A software defect is a bug which if not removed will cause a program or system to fail or produce incorrect results. This study tracks several types of defects:

<sup>Ø</sup> Software failures

<sup>Ø</sup> Design defects

<sup>Ø</sup> Code defects

<sup>Ø</sup> Other defects

If you are not currently tracking these defects, please use the following procedures to track them for a period of one month.

Failures: Please keep a log Appendix A of howŽ . many failures are reported by users and operators of this system on a daily basis.

Design Defects: Design defects are defects attributable to design errors such as mistakes in algorithms. These defects are normally found during initial tests of changes or enhancements to an application. Please keep a log Appendix B of design Ž . defects found by both programmer<sup>r</sup>analysts and testers for a period of one month.

Code Defects: Code defects are defects attributable to coding errors such as branching to a wrong location. These defects are found throughout the coding process as well as in final test of changes and enhancements to an application. Please keep a log Appendix C of code defects found by bothŽ . programmer<sup>r</sup>analysts and testers for a period of one month.

Other Defects: Other defects include specification, installation, environmental support, vendor supplied, and documentation defects. Definitions of these defects can be found in the definition of terms ( ) Appendix E . Please keep a log Appendix D ofŽ . other defects by type found by both programmer<sup>r</sup> analysts, testers, and users for a period of one month.

Section 5: The following questions are about the quality characteristics of the software application you are supporting. If you do not know the answer to a particular question or do not have access to the information requested, please fill in the question with N<sup>r</sup>A Ž . not available .

1. Do you track defects in this software application? yes\_\_\_ no\_\_\_

If the answer to this question is no, please see the attached Defect Collection Instructions sheet.

2. Do you track failures for this software application? yes\_\_\_ no\_\_

3. On average, how many failures per month occur in this software application?

0 1–5 6–10

11–20

more than 20\_\_\_

4. On average, how many defects<sup>r</sup>month in this software application are attributable to coding errors?

11–20

more than 20\_\_\_

5. On average, how many defects<sup>r</sup>month in this software application are attributable to design errors?

more than 20\_\_\_

6. On average, how many defects<sup>r</sup>month in this software application are attributable to other errors?

0 1–5 6–10 11–20 more than 20

## References

<sup>w</sup> <sup>x</sup>1 J.G. Cooprider, K.M. Victor, The Contributions of Shared Knowledge to I<sup>r</sup>S Group Performance, Proceedings of the Fourteenth ICIS, Orlando, FL, December 15–18, 1993.

<sup>w</sup> <sup>x</sup> 2 M.A. Cusamano, C.F. Kemerer, A quantitative analysis of U.S. and Japanese practice and performance in software development, Management Science 36 11 1990 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 M.J. Davis, R.B. Williams, Software architecture characterization, Software Engineering Notes 22 3 1997 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 S.M. Dekleva, The influence of the information systems development approach on maintenance, MIS Quarterly 16 3Ž . Ž . 1992 .

<sup>w</sup> <sup>x</sup> 5 S.H. Haeckel, R.L. Nolan, Managing by wire, Harvard Business Review 71 5 1993 .Ž . Ž .

6 T.R. Hopkins, Restructuring software: a case study, Software —Practice and Experience 26 8 1996 .Ž . Ž .

7 C. Jones, Programming Productivity, McGraw-Hill, New York, 1986.

<sup>w</sup> <sup>x</sup> 8 K.C. Keene, S.J. Keene, Consideration of maintenance objectives in the design and development of software, Quality and Reliability Engineering International 9 5 1993 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 T.M. Khoshgoftaar, R.M. Szabo, T.G. Woodcock, An empir-

ical study of program quality during testing and maintenance, Software Quality Journal 3 3 1994 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 Y. Kim, E.A. Stohr, Software reuse: survey and research directions, Journal of Management Information Systems, forthcoming, 1998.

<sup>w</sup> <sup>x</sup> 11 B.A. Kitchenham, Metrics In Practice, IEEE Colloquium Ž . Digest , n 1985<sup>r</sup>21, 1985.

<sup>w</sup> <sup>x</sup> 12 K.M. Nelson, S. Nadkarni, V.K. Narayanan, M. Ghods, Understanding Software Maintainer Expertise: A Causal Mapping Approach, working paper, The University of Kansas, Ernst and Young CARAT Working Paper Series, 1997.

<sup>w</sup> <sup>x</sup> 13 W.E. Perry, Quality concerns in software development: the challenge is consistency, Information Systems Management 9 Ž . Ž .2 1992 .

<sup>w</sup> <sup>x</sup>14 R.E. Quinn, J. Rohrbaugh, A spatial model of effectiveness criteria: towards a competing values approach to organizational analysis, Management Science 29 1983 .Ž .

<sup>w</sup> <sup>x</sup> 15 A. Topper, D. Ouellete, P. Jorgensen, Structured Methods: Merging Models, Techniques, and CASE, McGraw-Hill, New York, 1994.

<sup>w</sup> <sup>x</sup> 16 M. Xenos, D. Christodoulakis, Applicable methodology to

automate software quality measurements, Proceedings of the 1st International Conference on Software Testing, Reliability and Quality Assurance, New Delhi, India, 1994.

Dr. Mehdi Ghods is an Associate Technical Fellow with Boeing. He earned his graduate degrees in physics, computer science and measurement, and prior to joining Boeing, he was a faculty member in radiology department at Michigan State University. His current research interests and work include operations research, management information system, technology transfer, and in particular, measurement and research in information technology.

Dr. Kay Nelson has both national and international experience in the fields of information systems and engineering management. She is currently an Assistant Professor at the University of Kansas. Dr. Nelson earned her PhD from the University of Texas at Austin in Management Information System. Her current research interests include the measurement of software maintenance quality and maintenance effectiveness, the role of tools and methods in software maintenance, and the use of information systems for strategic communication and coordination. Dr. Nelson has previously published in MIS Quarterly.
