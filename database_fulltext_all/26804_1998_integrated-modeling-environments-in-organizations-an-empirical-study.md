---
otero_id: 26804
otero_key: "V2K7G8B6"
title: "Integrated Modeling Environments in Organizations: An Empirical Study"
authors: "Gordon P. Wright; Alok R. Chaturvedi; Radha V. Mookerjee; Susan Garrod"
year: "1998"
journal: "Information Systems Research"
doi: "10.1287/isre.9.1.64"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/V2K7G8B6/fulltext/images/4554adde4b4cca3107ad4e62c9a0f9adb556dde325382206642b08075d76ba58.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Integrated Modeling Environments in Organizations: An Empirical Study

Gordon P. Wright, Alok R. Chaturvedi, Radha V. Mookerjee, Susan Garrod,

To cite this article:

Gordon P. Wright, Alok R. Chaturvedi, Radha V. Mookerjee, Susan Garrod, (1998) Integrated Modeling Environments in Organizations: An Empirical Study. Information Systems Research 9(1):64-84. http://dx.doi.org/10.1287/isre.9.1.64

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1998 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/V2K7G8B6/fulltext/images/731eeaee9498f275d3421c9a3266e973feec36d56ffa630eb74ee8f3b0912c57.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Integrated Modeling Environments in Organizations: An Empirical Study

Gordon P. Wright • Alok R. Chaturvedi • Radha V. Mookerjee • Susan Garrod Krannert Graduate School of Management, Purdue University, West Lafayette, Indiana 47907 gordy@mgmt.purdue.edu

Krannert Graduate School of Management, Purdue University, West Lafayette, Indiana 47907 alok@mgmt.purdue.edu

Information Systems Architecture, Boeing Commercial Group, Seattle, Washington 98124 radha.v.mookerjee@boeing.com

School of Technology, Purdue University, West Lafayette, Indiana 47907 sgarrod@purdue.edu

on siderable attention in the information systems and management science literature has focused on computer-based modeling environments, sometimes called integrated modeling environments or model management systems. This research has been primarily concerned with suggesting features/components of modeling environments such as improved executable modeling languages for model creation, integration, and data representation; specialized database systems for managing model data; and customized model-solver software. However, there has been little (if any) empirical guidance offered in the literature about the specific needs of business and industry for computer-based integrated modeling environments. Using a data set compiled from a national survey of modelers (analysts) and model users (decision makers), we empirically investigate the validity of several of the key assump tions of modeling environment research reported in the literature, and examine the relationships between the modeling factors: data complexity, model complexity, modeling intensity, modeler/user requirements, and need for computer-based integrated modeling environments in organizations.

Our empirical analysis of the data set shows that practitioners rank automated access to model data and automated error checking (e.g., model syntax and semantics checking) high as desirable components in modeling environments. We find that users prefer to have modeling environments linked to their current modeling and modeling-support software systems. Our findings further suggest that a high percentage of modelers and users are dissatisfied with the software systems they are currently using to support their modeling activities. Finally, a covariance structure analysis of the modeling environment factors clearly shows that: (a) model complexity has a direct positive effect on modeling intensity; (b) data complexity has an insignificant direct effect on modeling intensity, but has a negative effect on modeler/user requirements; and (c) modeler/user requirements have a direct positive effect on need for computer-based integrated modeling environments in organizations.

(Model Management Systems; Integrated Modeling Environments; Structured Modeling; Decision Support Systems)

## 1. Introduction

An active area in information systems research is the development of computer-based modeling environments, sometimes called integrated modeling environments or model management systems (e.g., see Geoffrion 1989a, 1991, and 1994; Blanning 1993; and Wright et al. 1997). By an integrated modeling environment we mean a software system with facilities for model creation and data representation, and the capability for interfacing with database systems and model-solving tools.

A key factor motivating most of the published research on modeling environments is the assumption that models, like data, are an important organizational resource and need to be managed well.<sup>1</sup> Further, much of the published research can be characterized as proposing components of modeling environments such as: improved executable modeling languages for model creation and data representation; specialized database management systems for managing model data; and customized model-solver software. However, the literature offers little empirical guidance as to the needs in business and industry for integrated modeling environments.

Using a data set compiled from a national survey of modelers and users, this study focuses on empirically describing several of the key assumptions of modeling environment research reported in the literature. In addition, we attempt to empirically describe and compare the important factors and trends that are relevant to organizations evaluating their need for (and use of) modeling environments, as suggested by the data, to those features of modeling environments suggested in the literature. This study also examines the relationships between the modeling constructs: data complexity, model complexity, modeling intensity, modeler/user requirements, and the need for integrated modeling environments in organizations.

<sup>1</sup>For the purpose of this research, the term “model” refers to a representation (idealized) that uses variables and equations or constraints to describe a business problem/system. Examples include statistical (e.g., econometric, time series, decision analysis, simulation), optimization/mathematical programming, spreadsheet, and network (e.g., scheduling, distribution, production planning, PERT) representations of business problems that can be manipulated using solver software systems.

## Research Assumptions—Integrated Modeling Environments

Most of the published research on modeling environments is theoretical in content and based on assumptions RA1-RA4 as follows.

RA1: MODEL USAGE. Models are widely used by firms for the planning and control of business functions; usage is increasing due to improved user-friendly hardware, modeling languages, and solver software (Will 1975; Dolk and Konsynski 1984; Applegate et al. 1985, 1986; Geoffrion 1987, 1989a, 1989b, 1994).

RA2: MODEL COMPLEXITY. Models used in organizations differ widely in complexity, application domain, and modeling paradigm (Elam et al. 1980; Geoffrion 1987; Chang et al. 1993; Lenard 1993).

RA3: MODELING ACTIVITIES. There exists considerable interaction of models in organizations; as a result, there exists a need for formal methods to manage models from different modeling paradigms and application domains (Dolk and Konsynski 1984, 1985; Bradley and Clemence 1988; Geoffrion 1989b; Krishnan 1993; Dolk and Kottermann 1993, 1994).

RA4: MODEL-DATA ACTIVITIES. Organizations need capable and versatile database management systems to support their modeling efforts (Dolk and Konsynski 1984, 1985; Wright et al. 1997; Kang et al. 1997).

Desirable Features of Modeling Environments The following is a comprehensive list of the desired features of computer-based modeling environments suggested in the literature.

DF1. Have facilities for model formulation, model representation, model verification, data management, model integration, model selection, and model solution (Dolk and Konsynski 1984; Shaw et al. 1988; Ramirez et al. 1993; Geoffrion 1987, 1991; Neustadter et al. 1992; Krishnan 1993).

DF2. Serve as a buffer between models and data, enabling users from many functional areas to use a single modeling paradigm (to perform task-specific analysis) and a common database (Dolk 1988; Geoffrion, 1987, 1989; Neustadter et al. 1992).

DF3. Support the entire life-cycle of the model (formulation, documentation, software development, evaluation, validation, training, installation, implementation and maintenance) (Will 1975; Dolk 1988; Fourier et al. 1990, Gass 1983, 1987; Ramirez et al. 1993; Geoffrion 1991).

DF4. Be hospitable to users of models as well as modeling professionals (Gass 1983, 1987; Geoffrion 1987, 1989a, 1991).

DF5. Support a single easily understood language for multiple users of the system (Geoffrion 1987, 1989c, 1992a, 1992b; Krishnan 1993; Wright et al. 1997).

Examples of computer-based modeling systems for optimization that have some of the features given previously are AMPL (Fourier et al. 1990), GAMS (Brooke et al. 1988), SASt-OR (1989) and LINGO (Cunningham and Schrage 1991). Some of the features can also be found in SASt (1989) and SPSSt (Norusis 1993), two popular computer-based systems for data analysis and econometric modeling, and SIMSCRIPTt (1983), a well-known simulation system.

An excellent survey of the model management literature is given in Blanning (1993). Two notable prototype implementations of modeling environments that possess most of the preceding features are FW/SM developed at UCLA (Geoffrion 1991) and OR/SM developed at Purdue (Wright et al. 1997, Kang et al. 1997). FW/SM and OR/SM are built on Framework IIIt (FW) (1991) and ORACLEt Tools and Database (OR) (ORACLE 1989), respectively. Both use Structured Modeling (SM) (Geoffrion 1987) as their conceptual framework and the Structured Modeling Language (Geoffrion 1992a and 1992b) as their executable modeling language. Briefly stated, the advantages of Structured Modeling as a conceptual framework for integrated modeling environments are: (1) applicability across several problem domains; (2) an executable, functional, and mathematically rigorous language for model and data representation; (3) the ability to manage different versions and families of models; and (4) a natural capability for interfacing with database systems and model-solving tools. The work of Geoffrion and his colleagues (e.g., see Geoffrion 1987, 1989c, 1991, 1992a, 1992b; Neustadter et al. 1992) on FW/SM strongly influenced the design and implementation of OR/SM.

Since this study is believed to be the first attempt to gather and analyze empirical data from practitioners regarding their use of integrated modeling environments, we chose to investigate the data set from an exploratory perspective. This was done by analyzing several summary statistics on modeling and modelrelated activities in organizations, and raising questions (hypotheses) and testing relationships that are related to several of the key assumptions of the modeling environment research reported in the literature. Therefore, this paper proceeds as follows. The next section describes the data set collected from a national survey of modeling professionals and users of models. This is followed by a somewhat detailed empirical description of several modeling-related activity variables that are directly related to the research assumptions RA1–RA4 given previously. We then empirically describe several of the desired features of modeling environments suggested by the data. This is followed by more exploratory analysis where we use covariance structure analysis (Jo¨reskog and So¨rborn 1986) to examine the relationships between the modeling constructs: data complexity, model complexity, modeling intensity, modeler/user requirements, and the need for modeling environments (labeled “modeling environmentneed” in this study) in organizations. We conclude with some brief comments of what we believe are the contributions of this study to the literature.

## 2. Data

## Data Collection

Our empirical analysis uses a data set obtained from a national survey of modeling practitioners in business and industry. Coded surveys were mailed to modelers and users of models in several areas of organizations including: market research, financial planning, production and operations planning, strategic management, human resource management, and management information systems. Sent along with each questionnaire was a cover letter from the researchers explaining the coding systems, the purpose of the study, and the confidentiality of the responses. Informants were also offered a brief statement describing the importance of the survey to encourage their participation. Questionnaires were returned directly to the researchers in preaddressed and postage-paid envelopes to emphasize the academic control of the information. One followup mailing with a duplicate survey and cover letters were sent to nonrespondents; also, one follow-up telephone call was made to randomly selected nonrespondents to encourage them to complete and return the questionnaire.<sup>2</sup>

## Respondents (Modelers and Users) and Key Terms

The Purdue Technical Practitioners’ Database was used to select the informants for the questionnaires. This database contains information on several modeling professionals and users of models including: (a) name, address, and job description; (b) type of industry employed; (c) years employed; and (d) education. Questionnaires were mailed to 825 randomly selected members of the database. Questionnaires were returned by 192 of the potential 825 respondents covering 90 different organizations. This gives a response rate of 23% that is above average for such surveys and suggests that the results are probably robust and somewhat generalizable (Dillman 1978). The respondents are a diverse group in terms of position and experience. For example, over 75% of the respondents belong to Fortune 500 companies; approximately 60% spend at least 20% of their time on modeling activities; and 67% have over 5 years of modeling experience. Table 1 gives some additional characteristics of the respondents.

The first page of the questionnaire gives the definition of several key terms and phrases frequently used in the survey, which are reported in Table 2. This is followed by 15 pages containing 71 questions on modeling and modeling-related activities. Since several questions have multiple parts (i.e., variables), the resulting data set has 192 responses on 153 variables. Nearly all the variables are categorical on a five-point scale. A few responses are observations on continuous variables such as percentages, while other responses indicate choices such as types of software systems being used to support modeling activities.

The questions in the survey were: (a) designed using the research assumptions and desirable features of

Table 1 Characteristics of the Respondents—Modelers and Users

<table><tr><td></td><td>Frequency</td><td>Percentage</td></tr><tr><td colspan="3">Industry</td></tr><tr><td>Manufacturing</td><td>109</td><td>54.8</td></tr><tr><td>Finance, Banking, and Insurance</td><td>30</td><td>15.1</td></tr><tr><td>Wholesale and Retail Trade</td><td>19</td><td>9.5</td></tr><tr><td>Transportation, Communication, and Utilities</td><td>12</td><td>6.0</td></tr><tr><td>Other</td><td>29</td><td>14.6</td></tr><tr><td colspan="3">Position</td></tr><tr><td>Senior Management</td><td>30</td><td>15.1</td></tr><tr><td>Middle Management</td><td>83</td><td>41.7</td></tr><tr><td>Professional/Staff</td><td>70</td><td>35.1</td></tr><tr><td>Other</td><td>16</td><td>8.1</td></tr><tr><td colspan="3">Modeling and Model-Use</td></tr><tr><td colspan="3">Experience</td></tr><tr><td>&lt;5 years</td><td>64</td><td>32.2</td></tr><tr><td>5–10 years</td><td>66</td><td>33.2</td></tr><tr><td>10–15 years</td><td>22</td><td>11.1</td></tr><tr><td>&gt;15 years</td><td>47</td><td>23.6</td></tr></table>

## Table 2 Definitions of Key Terms/Phrases in the Questionnaire

## Model\*

A model is a statement of a problem, characterized by a set of inputs, a set of outputs and the relations between them. A model may contain one or more of the following: an objective function, a set of constraints, or a set of assumptions.

## Solver

A procedure (e.g., a statistical estimation method or an algorithm) used to execute or solve a model; it is assumed to be independent from the form of model representation.

## Model Integration

The process of combining two or more models to form one composite model.

## Model-Data Interface

A computer-based link between a model and the data needed for mode solution.

## Model-Solver Interface

A computer-based link between a model and a procedure needed to solve the model.

## Solver Selection

The selection of a solver (assuming more than one solver is available for a particular model) best suited for the problem (i.e., model instance) at hand.

modeling environments discussed earlier (in the introduction); and (b) stated in simple, concrete terms using terminology understood and employed by modelers and model users. Some field interviews were used to pretest and improve the wording of questions. Also, exploratory factor analysis and an examination of the question intercorrelations, means, and standard deviations were used to refine the scales. A few questions were not considered because of low variance in responses and the possibility of multiple interpretations. The questions are organized into six distinct sections: Models, Data, Solvers, Software Systems, Model Complexity, and User Characteristics. These sections are briefly described as follows.

Models Section. Seventeen questions were used to assess model usage within and across departments. The questions address the multiple facets of modeling incorporated in our definitions of model, model integration, and model-solver interface, as listed in Table 2 including: (a) time spent creating models, (b) functional areas using models, (c) future use (planned for) versus present use of models, (d) frequency of model usage in direct support of decision making in the firm, (d) interaction of models within and across application domains, and (e) how firms manage models.

Data Section. This section contains eight questions that focus on measures of the complexity of modeldata, including data accuracy and data volatility, and how data (e.g., databases) needed to manipulate (e.g., solve) models are managed (e.g., located, stored, retrieved, and reused) in organizations.

Solver Section. Types and satisfaction levels of computer-based solvers were assessed with three questions, including a question asking the respondent to list the reasons, if any, why he/she is dissatisfied with his/her current solver software systems.

Software Systems. Thirty-three questions were used to assess the need for: (a) automated support for model creation, selection, and integration; (b) automated support for solver selection; and (c) model-data interfaces. Several of the questions also were used to assess the necessity for a computer-based integrated modeling environment in the respondent’s department.

Model Complexity. The complexity of the models in each respondent’s department or organization was assessed by six questions. For example, each respondent was asked to identify the factors that best indicate (i.e., measure) the complexity of the models being used in their department. Examples of factors measuring model complexity include: (a) number of variables, (b) number of constraints, and (c) expected computing time.

User Characteristics. The last section of the survey gives some descriptive information about each respondent including statistics concerning his/her work experience and level of computer literacy. In addition, each respondent is asked to list the computer hardware most frequently used to support his/her modeling efforts.

Table 3 summarizes the content of the questionnaire in more detail.

## 3. Some Empirical Results

First, we describe several key summary statistics (Tables 4–7) from our analysis of the practitioners’ data set that are directly related to the research assumptions RA1–RA4, as shown in Figure 1. This is followed by a discussion (Table 8) of the need for modeling environments in business, organized around the desired features DF1–DF4 (given in the introduction) of integrated modeling environments suggested in the literature.

## RA1: Model Usage—Descriptive Findings

Tables 4A and 4B—Model Hardware and Software. High-end PCs and mainframes are the most common computers being used in organizations to support modeling and modeling-related activities. Workstations and Low-end PCs rank last and are only marginally different from each other in frequency of use. On the average, the data indicates that modelers use three to four different software systems (e.g., solvers, database management systems) to support their modeling efforts.

Tables 4C and 4D—Model Solvers. Not surprising, statistical methods and spreadsheet-based procedures/algorithms are the most frequently used solvers in business applications. SAS ranks first as the most frequently used solver, followed by spreadsheets and project management software ranking second and

## WRIGHT, CHATURVEDI, MOOKERJEE, AND GARROD Integrated Modeling Environments in Organizations

Table 3 Survey Design

<table><tr><td>Section</td><td>Variables Measured</td><td>Related to Assumptions/Features</td></tr><tr><td rowspan="5">Models(17 questions)</td><td>Time spent on model-related activities, size and variability of model library, and level of computerization</td><td>RA1, RA2</td></tr><tr><td>Application domains, types of problems solved using models, and frequency of use of different model types</td><td>RA1, RA2/DF1</td></tr><tr><td>Model interactions: within and across departments by type of model</td><td>RA1-RA4/DF1</td></tr><tr><td>How/why models are stored</td><td>DF1</td></tr><tr><td>Demand for models to support decision making: within and across depart-ments</td><td>RA1-RA3/DF1</td></tr><tr><td rowspan="8">Data(8 questions)</td><td>Source of data</td><td>RA4/DF1, DF2, DF4</td></tr><tr><td>Data location—centralized or decentralize</td><td>RA3, RA4/DF1, DF2, DF4</td></tr><tr><td>Data availability—hard copy, automated</td><td>RA4/DF1, DF2, DF4</td></tr><tr><td>Data volatility—(ranking)</td><td>RA4/DF1, DF2, DF4</td></tr><tr><td>Data accuracy—(ranking)</td><td>RA4/DF, DF2, DF4</td></tr><tr><td>Ease of data measurement</td><td>RA4/DF1, DF2, DF4</td></tr><tr><td>Ease of acquiring data</td><td>RA4/DF1, DF2, DF4</td></tr><tr><td>Proportion of models using real-time data</td><td>RA3, RA4/DF1, DF2</td></tr><tr><td rowspan="4">Solvers(3 questions)</td><td>Names of solvers being used for each of eleven different model types</td><td>RA1, RA2/DF1, DF2, DF4</td></tr><tr><td>Satisfaction levels for the five most frequently used solvers</td><td>RA1/DF1, DF2, DF4</td></tr><tr><td></td><td>RA1-RA2/DF1, DF2, DF4</td></tr><tr><td>Reasons for dissatisfaction with current solvers</td><td></td></tr><tr><td rowspan="13">Software Systems(33 questions)</td><td>Number of software systems for model-related activities</td><td>RA1, RA2/DF1</td></tr><tr><td>Names of software systems for model-related activities</td><td>RA1, RA2/DF1, DF4</td></tr><tr><td>Need for model formulation languages/software</td><td>RA1-RA3/DF1, DF3, DF5</td></tr><tr><td></td><td>RA1, RA2/DF1, DF3, DF4, DF5</td></tr><tr><td>Satisfaction levels—model formulation software</td><td>RA1, RA2/DF1, DF3, DF4, DF5</td></tr><tr><td>Need for model selection software</td><td>RA1, RA2/DF1, DF3, DF4</td></tr><tr><td>Similarity of variables across models</td><td>RA2, RA3/DF1</td></tr><tr><td></td><td>RA2, RA3/DF1, DF3, DF4</td></tr><tr><td>Need for model integration software</td><td>RA1, RA2/DF1, DF3, DF4</td></tr><tr><td>Need for solver selection software</td><td>RA3, RA4/DF1-DF5</td></tr><tr><td>Need for automated model-data interfaces</td><td>RA1-RA4/DF1-DF5</td></tr><tr><td>Need for computer-based modeling environment systems</td><td>RA1-RA4/DF1-DF5</td></tr><tr><td>Desired characteristics of computer-based modeling environments</td><td>RA1-RA4/DF1-DF5</td></tr><tr><td rowspan="5">Model Complexity(6 questions)</td><td>Indicators of model complexity</td><td>RA1, RA3/DF1, DF3-DF5</td></tr><tr><td>Measuring model complexity</td><td>RA1, RA3/DF1, DF3-DF5</td></tr><tr><td>Proportion of complex models in use</td><td>RA1, RA3/DF1, DF3-DF5</td></tr><tr><td></td><td>RA1, RA4/DF1, DF3-DF5</td></tr><tr><td>Adequacy of current software to manage complex models</td><td>CF5</td></tr><tr><td rowspan="4">User Characteristics(4 questions)</td><td>Years of modeling experience</td><td>RA1, RA2</td></tr><tr><td>Job title</td><td>RA1</td></tr><tr><td>Computer literacy</td><td>RA1, RA2</td></tr><tr><td>Hardware systems being used</td><td></td></tr></table>

Information Systems Research Vol. 9, No. 1, March 1998

Figure 1 Research Assumptions and Summary Statistics  
![](/api/attachments/V2K7G8B6/fulltext/images/833d34732e1dd44da2f9f130c89c8ccf1641089c71bf3c391e7b62cd83d3603b.jpg)

third, respectively. The data further suggest that simulation and optimization solvers (e.g., MPS and SIM-SCRIPT) rank the lowest in frequency of use. A total of 150 different systems were named by the respondents as frequently used solvers; however, only nine were mentioned as frequently used solvers by five or more respondents, which probably suggests that many commercial solver software products are either similar in terms of purpose or performance, or they are highly specialized and meet the requirements of only a small number of modelers.

Tables 4E and 4F—Application Domains and Model Usage. As shown in Table 4E, manufacturing, finance, strategy, and accounting are the functional areas where models are used most frequently in organizations. Human resource management ranks noticeably the lowest in model usage. Statistical models (e.g., regression, forecasting) are the most frequently used types of models in organizations, followed by scheduling and project management models. The least used models are mathematical programming models.

Other Statistics on Model Usage. The data indicate that the average number of models used across departments within an organization is approximately equal to twenty. Further, the average number of models across organizations is estimated to be about 200. The data also indicate that models are used to support approximately 50% of departmental decisions. Sixty percent of the practitioners indicated that they use models primarily for solving unstructured problems. Finally, less than 5% indicated that the modeling software they use is developed in-house. The later supports the claim that most modeling software systems are: (a) purchased from software vendors; and (b) standard across organizations.

Table 4 Model Usage  
(A) Hardware Used to Support Modeling Environments

<table><tr><td>Type</td><td>Frequency</td><td>Percentage</td></tr><tr><td>High-End PCs</td><td>167</td><td>87.0</td></tr><tr><td>Mainframes</td><td>115</td><td>59.9</td></tr><tr><td>Workstations</td><td>48</td><td>25.0</td></tr><tr><td>Low-End PCs</td><td>40</td><td>20.8</td></tr></table>

(B) Number of Software Systems Used to Support Modeling Environments

<table><tr><td>Range</td><td>Frequency</td><td>Percentage</td></tr><tr><td>0–5</td><td>159</td><td>82.8</td></tr><tr><td>6–10</td><td>13</td><td>6.8</td></tr><tr><td>11–15</td><td>11</td><td>5.8</td></tr><tr><td>&gt;15</td><td>9</td><td>4.7</td></tr></table>

(C) Most Frequently Used Solvers

<table><tr><td>Solver Software</td><td>Frequency</td><td>Percentage</td></tr><tr><td>SAS</td><td>116</td><td>60.4</td></tr><tr><td>Spreadsheets</td><td>78</td><td>40.6</td></tr><tr><td>Project Management</td><td>23</td><td>12.0</td></tr><tr><td>SIMAN</td><td>15</td><td>7.8</td></tr><tr><td>MPS</td><td>15</td><td>7.8</td></tr><tr><td>SPSS</td><td>10</td><td>5.2</td></tr><tr><td>LINDO</td><td>9</td><td>4.7</td></tr><tr><td>SIMSCRIPT</td><td>7</td><td>3.7</td></tr><tr><td>SLAM</td><td>6</td><td>3.1</td></tr></table>

(D) Solver Software Used by Model Type

<table><tr><td>Solver Software</td><td>Model Type</td></tr><tr><td>SAS</td><td>Statistical, Forecasting, Math, Programming</td></tr><tr><td>Spreadsheets</td><td>Statistical, Forecasting, Project Management Forecasting, Scheduling, Project Manage-ment</td></tr><tr><td>Project Management</td><td></td></tr><tr><td>SIMAN</td><td>Simulation</td></tr><tr><td>MPS</td><td>Scheduling, Distribution, Math, Programming</td></tr><tr><td>SPSS</td><td>Statistical, Forecasting</td></tr><tr><td>LINDO</td><td>Distribution, Scheduling, Math Programming</td></tr><tr><td>SIMSCRIPT</td><td>Simulation</td></tr><tr><td>SLAM</td><td>Simulation</td></tr></table>

(Table 4 continued)  
(E) Application Domains\* in Rank Order

<table><tr><td>Domain/Area</td><td>Frequency</td><td>Percentage</td></tr><tr><td>Manufacturing</td><td>139</td><td>72.4</td></tr><tr><td>Finance</td><td>137</td><td>71.4</td></tr><tr><td>Strategic Mgmt.</td><td>119</td><td>62.0</td></tr><tr><td>Marketing</td><td>112</td><td>58.3</td></tr><tr><td>Accounting</td><td>94</td><td>49.0</td></tr><tr><td>Human Resources</td><td>57</td><td>29.7</td></tr></table>

\*Areas where models are being used.

(F) Model Usage by Model Type\*

<table><tr><td>Type</td><td>Frequency</td><td>Percentage</td></tr><tr><td>Forecasting</td><td>158</td><td>82.3</td></tr><tr><td>Simulation</td><td>151</td><td>78.6</td></tr><tr><td>Statistical</td><td>134</td><td>69.8</td></tr><tr><td>Scheduling</td><td>109</td><td>56.8</td></tr><tr><td>Project Management</td><td>109</td><td>56.8</td></tr><tr><td>Decision Analysis</td><td>99</td><td>51.6</td></tr><tr><td>Math. Programming</td><td>84</td><td>43.8</td></tr></table>

\*Each individual response is a rank ordering of model types based on frequency of use.

## RA2: Model Complexity—Descriptive Findings

Tables 5A and 5B—Model Complexity. It is perhaps not surprising that the key factors that modelers and users suggested as contributors to model complexity are the number of variables, equations, and constraints. However, it is surprising to learn of the “very low” critical levels for the complexity factors measured, as listed in Table 5B. Models with an average of 26 equations, 21 constraints, or between 13 and 20 variables were at the critical level of complexity as reported by the practitioners. Table 5B also shows that there is considerable variability in the critical levels of these factors. It is interesting to note that computer time (i.e., model execution time) ranks the lowest as a contributing factor to model complexity. Finally, the data indicates (not shown in Table 5) that over 55% of the practitioners are dissatisfied with the capabilities of the software systems they use to support their modeling activities.

## RA3: Modeling Activities—Descriptive Findings

Table 6A, 6B, and 6C—Model Integration and Interactions. Models are most likely to be managed at the departmental level rather than centrally in an organization, and surprisingly, the results strongly suggest that model integration (i.e., linking two or more existing models) is a frequently occurring task (88%) in organizations. As expected, model integration is the highest among models of the same type. The respondents were asked to indicate the degree of interaction between models, within and across departments, with special emphasis on the sharing of data between models. As expected, within department interactions (e.g., model sharing) are the most frequent and interactions across departments are the least frequent.

## Table 5 Model Complexity

(A) Factors That Contribute to (Measure) Model Complexity

<table><tr><td>Variable</td><td>Frequency</td><td>Percentage</td></tr><tr><td>Number of equations</td><td>162</td><td>84.4</td></tr><tr><td>Number of constraints</td><td>128</td><td>66.7</td></tr><tr><td>Number of input variables</td><td>125</td><td>65.1</td></tr><tr><td>Number of assumptions</td><td>110</td><td>57.3</td></tr><tr><td>Number of output variables</td><td>81</td><td>42.2</td></tr><tr><td>Execution time (minutes)</td><td>47</td><td>24.5</td></tr></table>

(B) Critical Levels of Model Complexity Factors

<table><tr><td>Variable</td><td>Average Critical Level</td><td>Standard Deviation</td></tr><tr><td>Number of equations</td><td>26.0</td><td>20.3</td></tr><tr><td>Number of constraints</td><td>21.1</td><td>24.8</td></tr><tr><td>Number of input variables</td><td>20.3</td><td>32.1</td></tr><tr><td>Number of assumptions</td><td>28.7</td><td>19.5</td></tr><tr><td>Number of output variables</td><td>13.2</td><td>12.6</td></tr><tr><td>Execution time (minutes)</td><td>29.2</td><td>34.3</td></tr></table>

Other Statistics on Modeling Activities. Over 95% of the respondents indicated that they reuse models frequently. Furthermore, 86% indicated that models are located in several model bases in their organization. The survey shows that 82% of the interactions between models are data sharing activities. Other model interactions indicated by the respondents included: (a) using results from one or more area (e.g., manufacturing, marketing, finance, etc.) models to develop a strategic planning model for the firm; and (b) using the results from one model to set goals and constraints for another model. Twenty-five percent of the respondents indicated in their qualitative responses that most interactions between models in their organization are not automated but rather are manual operations. Finally, respondents indicated a strong need for automated support of model integration. This finding supports the assumption of a need for computer-based integrated modeling environments in many organizations.

## RA4: Data Activities—Descriptive Findings

Tables 7A and 7B—Data Sources and Locations. The results indicate that data are most often collected when needed for model execution (i.e., model solution); whereas 36% of model data are from routine automated transactions. Only a small percentage (17%) of the respondents indicated their model data are centrally located in their organization; and storing data occurs most often at the department level in organizations.

Tables 7C, 7D, and 7E—Data Complexity, Accuracy, and Availability. The respondents were asked to rate (on a scale of 1 to 5) four measures of data complexity. The complexity measures included: (1) volatility, accuracy, and ease of measuring data; and (2) availability (accessibility) of data for use by models. The data availability measure distinguishes between data collected during electronic transactions as compared to data that is manually collected and compiled. Data accuracy and availability ranked the highest, whereas data volatility ranked the lowest as measures of data complexity.<sup>3</sup> Further, 25% of the respondents indicated

Table 6 Model Integration  
(A) Model Management Policies

<table><tr><td>Models are Managed:</td><td>Frequency</td><td>Percentage</td></tr><tr><td>Centrally</td><td>25</td><td>14.1</td></tr><tr><td>Type of model</td><td>44</td><td>25.0</td></tr><tr><td>Department</td><td>63</td><td>35.8</td></tr><tr><td>Individual user</td><td>44</td><td>25.0</td></tr></table>

## (B) Model Integration

<table><tr><td>Integration, If Any, Among Models of:</td><td>Frequency</td><td>Percentage</td></tr><tr><td>Same and different types</td><td>62</td><td>35.0</td></tr><tr><td>Usually the same type</td><td>56</td><td>32.0</td></tr><tr><td>Usually different types</td><td>37</td><td>21.0</td></tr><tr><td>No integration</td><td>21</td><td>12.0</td></tr></table>

(C) Frequency of Model Interaction

<table><tr><td rowspan="2">Ranking</td><td colspan="2">Output-Input Model Interactions</td><td colspan="2">Other Interactions</td></tr><tr><td>Within Departments</td><td>Across Departments</td><td>Within Departments</td><td>Across Departments</td></tr><tr><td>1 (= high)</td><td>13 (6.8)</td><td>8 (4.2)</td><td>16 (8.5)</td><td>5 (2.6)</td></tr><tr><td>2</td><td>64 (33.7)</td><td>40 (21.1)</td><td>39 (20.6)</td><td>20 (10.6)</td></tr><tr><td>3</td><td>71 (37.4)</td><td>65 (34.2)</td><td>53 (28.0)</td><td>54 (28.6)</td></tr><tr><td>4</td><td>37 (19.5)</td><td>65 (34.2)</td><td>49 (25.9)</td><td>51 (27.0)</td></tr><tr><td>5 (= low)</td><td>5 (2.6)</td><td>12 (6.3)</td><td>33 (16.9)</td><td>60 (31.2)</td></tr></table>

that model data are made available to users only on an ad-hoc noncomputerized basis (e.g., manually collected), and 36% indicated that model data are made available using database management software.

Other Statistics—Model-Data Activities. Almost 35% of the respondents indicated that their models, data, and solution procedures are managed at the departmental level. Further, 42% indicated that models are stored separate from their solution procedures. Perhaps an interesting finding is that 35% of the respondents indicated that model users, rather the model developers, are responsible for the design and implementation of model-data interfaces in their organization.

## Desirable Features of Modeling Environments— Descriptive Findings

Tables 8A and 8E—Model-Data Interfaces (see features DF1–DF3 in the Introduction). The results clearly show that there is a significant need (i.e., many respondents rank high) for automated access to model data (i.e., databases), and automated error and consistency checking as components of model-data interfaces. This is further supported at the area level, as shown in Table 8E, with the possible exception of error checking in market planning/research departments. It is clear that practitioners rank type conversion as the least desired feature of model-data interfaces.

Tables 8B and 8F—Model Management Systems (see DF1, DF3–DF5). Model integration and model formulation software systems (e.g., an executable general purpose modeling language) are ranked by users as nearly equivalent desirable features in modeling environments. Further, the results suggest that automated model selection and solver selection are the least desired features of modeling environments. These results are consistent across functional areas in organizations with the possible exception of human resource management.

Tables 8C and 8G—Current Software Systems (DF1–DF3). The results in Table 8C show that modeling environment software currently used in organizations is about equally split between decision support systems and model management systems. Further, as shown in Table 8G, this result is consistent across functional areas, with the exception of human resource management.

Tables 8D and 8H—Usefulness of Integrated Modeling Environments (DF1–DF5). The results strongly suggest that computer-based modeling environments would not be considered useful to modelers and users as separate (nonintegrated) systems. As shown in Table 8H, this is strongly supported in the manufacturing, marketing, and accounting areas, and to a lesser extent in finance, strategic management, and human resource management.

Other Statistics—Modeling Environments. More than 75% of our respondents indicated that they support the use of computer-based integrated modeling environments in their organization, but only if they are linked to an existing modeling support system (such as an existing decision support system). The respondents were asked to rate (on a scale of 1 4 not important at all to 5 4 very important) the importance of having one modeling system capable of managing all their models. Almost a third of the respondents (30.3%) answered with a score of 1 or 2. Other qualitative responses to this question strongly suggest that although modelers and users believe integrated modeling environments are desirable, they recognize that it is probably difficult to implement a single comprehensive modeling system that meets most of the needs of their organization.

Table 7 Model—Data Activities

<table><tr><td colspan="3">(A) Data Sources</td></tr><tr><td>Source</td><td>Frequency</td><td>Percentage</td></tr><tr><td>Collected whenever needed</td><td>62</td><td>32.5</td></tr><tr><td>Computer based transactions</td><td>36</td><td>18.8</td></tr><tr><td>Hard copy</td><td>8</td><td>4.2</td></tr><tr><td>All of the above</td><td>85</td><td>44.5</td></tr><tr><td colspan="3">(B) Data Locations</td></tr><tr><td>Location</td><td>Frequency</td><td>Percentage</td></tr><tr><td>Centrally</td><td>33</td><td>17.3</td></tr><tr><td>Department</td><td>72</td><td>37.7</td></tr><tr><td>Other</td><td>86</td><td>45.0</td></tr><tr><td colspan="3">(C) Data Complexity</td></tr><tr><td>Factor</td><td>Average Ranking</td><td>Standard Deviation</td></tr><tr><td>Accuracy</td><td>3.6</td><td>0.8</td></tr><tr><td>Availability</td><td>3.3</td><td>1.1</td></tr><tr><td>Measurability</td><td>2.9</td><td>1.0</td></tr><tr><td>Volatility</td><td>2.6</td><td>1.5</td></tr><tr><td colspan="3">(D) Data Accuracy</td></tr><tr><td>How accurate are the data?</td><td>Frequency</td><td>Percentage</td></tr><tr><td>Inaccurate</td><td>121</td><td>63.0</td></tr><tr><td>Accurate</td><td>21</td><td>11.0</td></tr><tr><td>Neither</td><td>35</td><td>18.0</td></tr><tr><td colspan="3">(E) Data Availability</td></tr><tr><td>How are the data made available?</td><td>Frequency</td><td>Percentage</td></tr><tr><td>Manually</td><td>65</td><td>34.0</td></tr><tr><td>Automatically</td><td>50</td><td>26.0</td></tr><tr><td>Both</td><td>77</td><td>40.0</td></tr></table>

## 4. User Requirements, Modeling Intensity, and Data Complexity

The goal of this part of our study is to provide researchers and practitioners more information about

Table 8 Features/Components of Modeling Environments

## (A) Model-Data Interfaces

<table><tr><td>Desired Features</td><td>Average Ranking*</td><td>Standard Deviation</td></tr><tr><td>Automatic access to model data</td><td>4.2</td><td>1.1</td></tr><tr><td>Error Checking</td><td>4.0</td><td>1.0</td></tr><tr><td>Consistency Checking</td><td>3.8</td><td>1.1</td></tr><tr><td>Type Conversion</td><td>3.3</td><td>1.2</td></tr></table>

\*(5 4 high; 1 4 low).

## (B) Components of MMS\*

<table><tr><td>Desired Features</td><td>Average Ranking**</td><td>Standard Deviation</td></tr><tr><td>Model Integration</td><td>3.1</td><td>1.3</td></tr><tr><td>Model Formulation</td><td>3.0</td><td>1.4</td></tr><tr><td>Model Selection</td><td>2.7</td><td>1.5</td></tr><tr><td>Solver Selection</td><td>2.4</td><td>1.3</td></tr></table>

\*MMS 4 Model Management Systems. \*\*(5 4 high; 1 4 low)

## (C) Current Software Systems\*

<table><tr><td>System Used</td><td>Frequency</td><td>Percentage</td></tr><tr><td>Decision Support</td><td>50</td><td>26.0</td></tr><tr><td>Model Management</td><td>48</td><td>25.0</td></tr><tr><td>Both of the above</td><td>17</td><td>19.0</td></tr><tr><td>Neither of the above</td><td>58</td><td>30.0</td></tr></table>

\*Being used to support modeling and modeling-related activities.

## (D) Modeling Environments

<table><tr><td>Response</td><td>Frequency</td><td>Percentage</td></tr><tr><td>Not very useful</td><td>84</td><td>44.0</td></tr><tr><td>Useless</td><td>50</td><td>26.0</td></tr><tr><td>Somewhat useful</td><td>35</td><td>18.0</td></tr><tr><td>Useful</td><td>23</td><td>12.0</td></tr></table>

the salient relationships between the five modeling environment constructs: modeler/user requirements, modeling environment-need, modeling intensity, model complexity, and data complexity. By a modeler/user

## (Table 8 continued)

## (E) Model-Data Interfaces

<table><tr><td rowspan="2">Functional Area</td><td colspan="4">Average Rankings (5 = high; 1 = low)</td></tr><tr><td>AAMD</td><td>EC</td><td>CC</td><td>TC</td></tr><tr><td>Manufacturing</td><td>4.2</td><td>4.2</td><td>3.9</td><td>3.6</td></tr><tr><td>Marketing</td><td>4.6</td><td>3.7</td><td>4.0</td><td>3.5</td></tr><tr><td>Accounting</td><td>4.1</td><td>4.3</td><td>3.7</td><td>3.3</td></tr><tr><td>Finance</td><td>4.3</td><td>4.2</td><td>3.9</td><td>3.4</td></tr><tr><td>Strategic Mgmt.</td><td>3.9</td><td>3.8</td><td>3.9</td><td>3.0</td></tr><tr><td>Human Resource Mgmt.</td><td>4.1</td><td>4.1</td><td>3.6</td><td>2.9</td></tr></table>

AAMD 4 Automatic access to model data; EC 4 Error Checking; CC 4 Consistency Checking; and TC 4 Type Conversion.

## (F) Modeling Environments

<table><tr><td>Functional Area</td><td>MI</td><td>MF</td><td>MS</td><td>SS</td></tr><tr><td>Manufacturing</td><td>3.6</td><td>3.7</td><td>2.6</td><td>2.5</td></tr><tr><td>Marketing</td><td>3.4</td><td>3.2</td><td>2.7</td><td>2.1</td></tr><tr><td>Account</td><td>3.0</td><td>2.9</td><td>2.4</td><td>2.5</td></tr><tr><td>Finance</td><td>3.0</td><td>3.1</td><td>2.4</td><td>2.4</td></tr><tr><td>Strategic Mgmt.</td><td>3.3</td><td>3.1</td><td>2.2</td><td>2.2</td></tr><tr><td>Human Resource Mgmt.</td><td>2.7</td><td>2.8</td><td>2.0</td><td>2.5</td></tr></table>

MI 4 Model Integration; MF 4 Model Formulation; MS 4 Model Selection; and SS 4 Solver Selection.

## (G) Current Software Systems (Modeling Environments)

<table><tr><td>Functional Area</td><td>DSS</td><td>MMS</td><td>Both</td><td>Neither</td></tr><tr><td>Manufacturing</td><td>28%</td><td>25%</td><td>21%</td><td>26%</td></tr><tr><td>Marketing</td><td>28</td><td>27</td><td>17</td><td>29</td></tr><tr><td>Accounting</td><td>27</td><td>25</td><td>20</td><td>28</td></tr><tr><td>Finance</td><td>27</td><td>25</td><td>18</td><td>30</td></tr><tr><td>Strategic Mgmt.</td><td>22</td><td>26</td><td>22</td><td>29</td></tr><tr><td>Human Resource Mgmt.</td><td>14</td><td>31</td><td>31</td><td>24</td></tr></table>

DSS 4 Decision Support Systems; MMS 4 Model Management Systems.

## (H) Modeling Environments\*

<table><tr><td>Functional Area</td><td>NU</td><td>U</td><td>SU</td><td>U</td></tr><tr><td>Manufacturing</td><td>40%</td><td>22%</td><td>10%</td><td>28%</td></tr><tr><td>Marketing</td><td>37</td><td>21</td><td>15</td><td>27</td></tr><tr><td>Accounting</td><td>43</td><td>21</td><td>19</td><td>18</td></tr><tr><td>Finance</td><td>44</td><td>20</td><td>24</td><td>12</td></tr><tr><td>Strategic Mgmt.</td><td>46</td><td>27</td><td>23</td><td>4</td></tr><tr><td>Human Resource Mgmt.</td><td>45</td><td>28</td><td>19</td><td>8</td></tr></table>

\*As a separate nonintegrated system. NU 4 Not very useful; U 4 Useless; SU 4 Somewhat useful; and U 4 Useful.

requirement we mean a specific modeling or software system needed by a modeler or user to support his/her modeling efforts such as an executable modeling language, an automated model-data interface, automated support for model creation and integration, or a customized model-solver system. By a modeling environment need we mean the need for a computer-based integrated modeling environment (see Geoffrion 1991 and Wright et al. 1997). Modeling intensity refers to the level of effort spent by modelers and users in their modeling activities. Recall that model complexity refers to the number of “parameters” of a model such as number of variables, equations, or constraints. Finally, data complexity refers to the accuracy, availability, and volatility of the data required by a model.

We seek to answer specific questions about modeling activities in organizations such as:

Modeling Intensity. Do complex models (model complexity) require a significant effort (modeling intensity) from modelers and users?

Do complex and automated model databases (data complexity) require more or less effort (modeling intensity) from modelers and users?

Modeler/User Requirements. What is the relationship between the complexity of a model (model complexity) and the number of different software systems/components (modeler/user requirements) needed or used by modelers and users?

What is the relationship between complex and automated model databases (data complexity) and the number of different software systems/components (modeler/user requirements) needed or used by modelers and users?

Does an increase in modeling effort (modeling intensity) by modelers and users usually cause an increase in the number of different software systems/components (modeler/user requirements) desired by modelers and users?

Modeling Environment Need. Does an increase in the number of complex models (model complexity) usually cause an increase in the need for an integrated modeling environment (modeling environment need) in organizations?

Does an increase in the number of complex automated model databases (data complexity) cause an increase in the need for an integrated modeling environment (modeling environment need) in organizations?

Does an increase in modeling effort (modeling intensity) by modelers and users cause an increase in the need for an integrated modeling environment (modeling environment need) in organizations?

Does an increase in the number of different software systems/components (modeler/user requirements) needed or used by modelers and users cause an increase in the need for an integrated modeling environment (modeling environment need) in organizations?

We now turn to a more detailed discussion of the five constructs including their measurements/indicators.

## Modeler/User Requirements and Modeling Environment Need

Modeling often involves an intensive set of activities including model formulation, model integration (i.e., combining two or more models into a single model), model solution, and/or model selection (see DF1; Murphy and Stohr 1986; Liang 1993, 1988b; Bradley and Clemence 1988; and Dolk and Kotterman 1993). As discussed earlier, most of the research in the modeling environment literature focuses on proposing features of modeling environments, such as improved modeling languages or customized model-solver software, without empirical support from modelers and users of models. In addition (and without empirical support), a key assumption in the literature is that usage of models in organizations is increasing due to improved user friendly hardware, modeling languages, and solver software (see research assumption RA1). This discussion leads to the following choices of measurement variables for the Modeler/User Requirements and Modeling Environment Need constructs.

Measuring Modeler/User Requirements and Modeling Environment Need. Modeler/User Requirements is measured by five possible respondent ratings (calibrated on a five-point scale) elicited by the question: “Given your needs, how necessary is automated support for each of the following features in a computerbased modeling environment?” The features are: (1) model formulation, (2) model integration, (3) model selection, (4) model extraction, (5) version management, and (6) model-data interface.

The Modeling Environment Need construct is measured by two questions. The first question is: “How useful would a Model Management System be in your department?” The options for this question are: “Very Useful,” “Somewhat Useful,” “Neither Useful nor Useless,” “Not very Useful,” and “Useless.” The second question is: “What is your opinion regarding the use of models outside a decision support system?” The options for this question (calibrated on a five -point scale) are: “necessary,” “somewhat necessary,” “neither necessary nor unnecessary,” “somewhat necessary,” or “unnecessary.”

## Modeling Intensity

The model management/modeling environment literature assumes that the demand for models is increasing in most organizations; and further, this increase is caused by several factors including the widespread availability of user friendly modeling and solversoftware systems (e.g., see Dolk and Konsynski 1984, Geoffrion 1991, and Kang et al. 1997). The literature further suggests that the increase in modeling efforts in organizations leads “naturally” to the need for automated support for model formulation and other modelrelated activities such as, for example, model integration and model-data interfaces (e.g., see Applegate et al. 1985, Geoffrion 1991, and Wright et al. 1997).

Measuring Modeling Intensity from the Data. Modeling Intensity is measured by two questions concerning individual and departmental modeling efforts in organizations. The first question is: “What proportion of your time is spent on modeling and using models?” The options for this question are: “0% to 20%,” “21% to 40%,” “41% to 60%,” “61% to 80%,” or “81% to 100%.” The second question is: “How many different models are used in your department (computerized or otherwise)?” The options for the second question are: “0 to 10,” “10 to 20,” “20 to 30,” “30 to 50,” or “greater than 50.”

## Model Complexity and Data Complexity

Two important assumptions common to most (if not all) of the published model management/modeling environment research are that: (a) models in organizations differ widely in complexity, application domain, and modeling paradigm (see RA2); and (b) organizations need capable and versatile database management systems to support their modeling efforts (see RA4). The literature further assumes that model and data complexity increases modeler/user requirements and the need for integrated modeling environments (e.g., see Wright et al. 1997, Geoffrion 1991, Dolk and Konsynski 1984, and Elam et al. 1980).

Measuring Model Complexity and Data Complexity from the Data. The complexity of a model is measured by asking respondents to give a critical level to each of three attributes of a model such that if a given model exceeds the critical level in one or more of the attributes, then he/she would consider the model to be complex. Using the definition of a model given in Table 2,<sup>4</sup> the three attributes this study uses to measure model complexity are: “number of variables,” number of equations/constraints,” and “number of assumptions.” The options for each attribute are: “less than 5,” “5–10,” “11–20,” “21–30,” or “greater than 30.” We note that over 80% of the respondents selected all of the three attributes as measures/contributors to model complexity.

Data Complexity is measured by three questions concerning data accuracy, data volatility, and data measurability. The first question is: “How accurate are the data required by your models?” The options are: “Very accurate,” “fairly accurate,” “neither accurate or inaccurate,” “fairly inaccurate,” or “very inaccurate.” The second question is: “How volatile are the data required by your models?” The options are: “very volatile,” “fairly volatile,” “neither volatile, nor stable,” “fairly stable,” or “very stable.” The third question is: “How easy is it to measure the data required by your models?” The options are: “very easy,” “fairly easy,” “neither very easy, nor very difficult,” “fairly difficult,” or “very difficult.”

## 4. Hypotheses and Results

We propose the relationships (model) given in Figure 2 as plausible (and important) hypotheses to be tested.

Figure 2 Proposed Hypotheses\*  
![](/api/attachments/V2K7G8B6/fulltext/images/b35b5a84584eb6eb8d368e50c9a40bb2016b1b298599e47d395b4cd290f453cc.jpg)  
\*Here ‘‘\~’’ and ‘‘!’’ indicate significant positive and negative effects, respectively.

The model in Figure 2 depicts modeling intensity and modeler/user requirements (consequences of model complexity and data complexity) as antecedents of modeling environment-need. The estimated parameters of the structural equations model are given in Table 9. Appendix A contains a discussion of some goodness of fit, reliability, and validity statistics, and a summary of the results from a rigorous simulation analysis of the estimated parameters. The parameters, test statistics, and some of the goodness of fit statistics are estimated using LISREL (Jo¨reskog and So¨rbom, 1986).<sup>5</sup>

It is perhaps appropriate at this point in our discussion to emphasize what we believe are two important aspects of this study which are the data set and our exploratory approach. As discussed earlier, there are no published empirical bases for most of the model management/modeling environment studies reported in the literature. Our analysis is based on a data set compiled from a national survey of modelers and users. Because the data set is somewhat unique and timely, we have chosen to investigate it from an exploratory perspective, giving summary statistics, raising questions and testing hypotheses as the analysis progressed. <sup>6</sup> Given our exploratory approach and limited data on some variables, we refrain from adopting a truly causal view of any of the hypothesized relationships between the latent constructs; we merely attempt to demonstrate and interpret “consistent themes” that are present in the data. We now give a brief discussion of the hypotheses and test results implied in Figure 3.

## Modeling Intensity

Hypothesis 1A. Model complexity has a direct effect on modeling intensity.

Hypothesis 1B. Data complexity has a direct effect on modeling intensity.

Hypothesis 1A is strongly supported by the data. This supports what is perhaps obvious and anticipated: that modelers/users tend to spend a significant effort manipulating (e.g., revising, integrating, etc.) complex models (as measured by the number of variables, number of constraints, and the number assumptions). The magnitude of the t-statistic for Hypothesis 1B given in Table 9 is 0.76, which suggests that data complexity has an insignificant effect on modeling intensity. This supports the view that modelers (and sometime users) are separated (e.g., may not be trained on how to use automated database systems) from the important task of obtaining or managing model data.

Table 9 Parameter Estimates and Goodness of Fit Statistics\* ( -Statistic in Parentheses)

<table><tr><td>Path From</td><td>To</td><td>Original Model</td><td>Revised Model</td></tr><tr><td>Model Complexity</td><td>Modeling Intensity</td><td>0.06(2.80)</td><td>0.18(2.97)</td></tr><tr><td>Data Complexity</td><td>Modeling Intensity</td><td>-0.08(-0.76)</td><td>—</td></tr><tr><td>Model Complexity</td><td>Modeler/User Requirements</td><td>-0.08(-1.32)</td><td>-0.08(-1.49)</td></tr><tr><td>Data Complexity</td><td>Modeler/User Requirements</td><td>ms0.69(-1.97)</td><td>-0.69(-1.79)</td></tr><tr><td>Model Intensity</td><td>Modeler/User Requirements</td><td>0.17(1.33)</td><td>0.21(1.70)</td></tr><tr><td>Model Complexity</td><td>Modeling Environment-Need</td><td>-0.01(-0.58)</td><td>—</td></tr><tr><td>Data Complexity</td><td>Modeling Environment-Need</td><td>-0.03(-0.50)</td><td>—</td></tr><tr><td>Model Intensity</td><td>Modeling Environment-Need</td><td>0.03(1.16)</td><td>—</td></tr><tr><td>Modeler/User Requirements</td><td>Modeling Environment-Need</td><td>0.16(8.28)</td><td>0.21(9.61)</td></tr><tr><td colspan="4">Goodness-of-Fit Indicators:</td></tr><tr><td rowspan="2">Chi-Square Statistic degrees of freedom</td><td></td><td>141</td><td>159</td></tr><tr><td></td><td>100</td><td>104</td></tr><tr><td>Goodness-of-Fit Index</td><td></td><td>0.92</td><td>0.91</td></tr><tr><td>Adjusted Goodness-of-Fit Index</td><td></td><td>0.87</td><td>0.87</td></tr><tr><td>Root Mean Square Residuals</td><td></td><td>0.10</td><td>0.10</td></tr><tr><td>Bentler&#x27;s Comparative Fit Index</td><td></td><td>0.93</td><td>0.91</td></tr></table>

\*Here “1” indicates that the corresponding path coefficient is constrained to be equal to zero in the revised structural equations model.

Figure 3 Results\*  
![](/api/attachments/V2K7G8B6/fulltext/images/5b6bc900cb628561539a8f5e832e1a6a93e9520748034feeea7a772c5e279e47.jpg)  
\*Here $" + \prime \prime$ and $^ { \prime \prime } - \prime \prime$ indicate significant positive and negative effects, respectively.

## User Requirements

Hypothesis 2A. Model complexity has a direct effect on the number of different software systems/components (modeler/user requirements) needed or used by modelers and users.

Hypothesis 2B. Data complexity has a direct effect on the number of different software systems/components (modeler/user requirements) needed or used by modelers and users.

Hypothesis 2C. Modeling intensity has a direct and positive effect on the number of different software systems/components (modeler/user requirements) needed or used by modelers and users.

Hypothesis 2A is at best weakly supported by the data as indicated by the magnitude of its t-statistic (4 1.32). We see that model complexity has a “weak” negative effect on modeler/user requirements. Perhaps a plausible explanation for this result is that modelers and users usually do not manipulate (e.g., revise and integrate) models that have high complexity ratings (i.e., ratings as measured by the number of variables, number of equations/constrainsts, and number of assumptions), and therefore they do not need additional or sophisticated modeling software systems for this purpose. In our analysis we split the data set into two sets: one set consisting of observations where one or more of the model complexity variables are, on the average, low, and the other containing observations where one or more of the model complexity variables are high. Next, we performed a correlation analysis between the model complexity variables and the measurement variables of the modeler/user requirements construct. Again, here the approach is exploratory. The two sets of variables (model complexity and model/user requirements) showed a positive correlation in the first data set where model complexity is low and a negative correlation in the second data set where model complexity is high. These correlations indicate that for only “small” increases in model complexity does modeler/user requirements increase, and for large increases, modeler/user requirements are likely to stay constant or decrease.

Hypotheses 2B and 2C are supported by the data. We see that data complexity has a negative direct effect on modeler/user requirements. This supports the view that modelers (and sometime users) choose to become more separated from the task of managing models that require complex data, and therefore do not need additional or new software systems to support managing of such models. We also note that when modeling intensity increases so does the need for new and specialized software systems. As anticipated, we find that modeling intensity positively affects modeler/user requirements.

## Modeling Environment Need

Hypothesis 3A. Model complexity has a positive effect on the need for a computer-based integrated modeling environment.

Hypothesis 3B. Data complexity has a positive effect on the need for a computer-based integrated modeling environment.

Hypothesis 3C. Modeling intensity has a positive effect on the need for a computer-based integrated modeling environment.

Hypothesis 3D. Modeler/user requirements has a positive effect on the need for a computer-based integrated modeling environment.

It is interesting that Hypothesis 3D is supported while Hypotheses 3A, 3B, and 3C are completely rejected. These results indicate that modeler/user requirements has a positive direct effect on the need for integrated modeling environments. We also conclude that data and model complexity, and modeling intensity have only an indirect effect, through modeler/user requirements, on the need for integrated modeling environments in organizations.

## 5. Some Comments and Conclusions

Understanding the practice and needs of modelers and model-users in business is an important issue for designers of computer-based modeling environments. This study attempts to describe some of the specific needs in business and industry for modeling environments using a data set compiled from a national survey of practitioners. As mentioned previously, since this study is believed to be the first attempt to gather and analyze empirical data from practitioners regarding their modeling activities, we investigated the data set from an exploratory perspective. This was done by analyzing several summary statistics on modeling and model-related activities in organizations, and raising questions (hypotheses) and testing relationships about several of the key assumptions of the modeling environment research reported in the literature. Specifically, we examined the relationships between the following factors: model complexity, data complexity, model intensity, model/user requirements, and the need for integrated modeling environments.

The findings of this study largely support the literature that computer-based integrated modeling environments are needed in organizations. What is interesting is that a large proportion (over 70%) of the reporting practitioners indicated that modeling environments should be integrated with their currently existing modeling-support (e.g., decision support) software systems. Other perhaps significant findings were that only a very small percentage (5%) of modeling software is developed “in-house,” and a very high percentage of modeling efforts in organizations are directed toward solving highly complex unstructured management problems. An analysis of the comments and opinion section in the questionnaire indicates that many modelers believe they lack the necessary expertise to effectively design or use database management systems for model-based work. Finally, we found that the majority of the reporting practitioners are dissatisfied with their current modeling-support software systems.

Surprisingly, a high proportion of the respondents (88%) indicated that model integration is a frequently occurring task in their organizations; this strongly supports the view that automated support for model integration is a highly desired feature in their modeling software. In addition, practitioners reported that statistical models are the most frequently types of models used to support decision making, whereas mathematical programming models are the least frequently used in organizations.

Table 10 Measurement Results

<table><tr><td>Construct</td><td>Number of Questions</td><td>Range of Reliabilities</td><td>Average Reliability</td><td>Composite</td></tr><tr><td>Model Complexity</td><td>3</td><td>0.66 to 0.92</td><td>0.80</td><td>0.90</td></tr><tr><td>Data Complexity</td><td>3</td><td>0.96 to 0.98</td><td>0.98</td><td>0.98</td></tr><tr><td>Modeling Intensity</td><td>3</td><td>0.80 to 0.89</td><td>0.85</td><td>0.89</td></tr><tr><td>User Requirements/Needs</td><td>6</td><td>0.94 to 0.98</td><td>0.96</td><td>0.99</td></tr><tr><td>System Needs</td><td> $\frac{2}{17}$ </td><td>0.87 to 0.99</td><td>0.93</td><td>0.99</td></tr></table>

The quantitative and qualitative findings, the later from the comments and opinion section of the questionnaire, show that: (a) the availability of microcomputers, executable modeling languages, and general purpose spreadsheets has led to an increase in the use of models to support decision making in many organizations; (b) available sophisticated and user-friendly hardware and software have made it easy for even the novice modeler/user to create and use models; (c) there exists a wide application domain for models (e.g., manufacturing, finance, marketing, and human resource management); (d) there is considerable variability in the types of models and model-solvers being used in firms (e.g., statistical, econometric, simulation, scheduling, decision analysis, mathematical programming); and (e) modelers and users of models believe there is a lack of user-friendly commercial software to support the modeling and solution of unstructured problems.

Using covariance structure analysis we empirically tested several hypotheses, some of which have been advanced in the literature, regarding the relationships between the modeling factors: data complexity, model complexity, modeling intensity, modeler/user requirements, and need for an integrated modeling environment. The analysis clearly suggests that: (a) model complexity has a direct positive effect on modeling intensity; (b) data complexity has an insignificant effect on modeling intensity; (c) data complexity has a direct negative effect on modeler/user requirements; and (d) only modeler/user requirements directly affects the need for computer-based integrated modeling environments.

Table 11 Reliability and Significance Tests

<table><tr><td colspan="3">Revised Model(t-statistic in parenthesis)</td><td colspan="2">Sampling Estimates(n = 200 estimates/data sets)</td></tr><tr><td>Path From</td><td>To</td><td>Parameter Estimate</td><td>Average Parameter Estimates</td><td>Test Results</td></tr><tr><td>Model Complexity</td><td>Modeling Intensity</td><td>0.18(2.97)</td><td>0.19</td><td>accept  $0.18^a$ </td></tr><tr><td>Model Complexity</td><td>Modeler/User Requirements</td><td>-0.08(1.49)</td><td>-0.13</td><td>accept  $-0.08^b$ </td></tr><tr><td>Data Complexity</td><td>Modeler/User Requirements</td><td>-0.59(-1.79)</td><td>-0.65</td><td>accept  $-0.59^a$ </td></tr><tr><td>Model Intensity</td><td>Modeler/User Requirements</td><td>0.21(1.70)</td><td>0.16</td><td>accept  $0.21^b$ </td></tr><tr><td>Modeler/User Requirements</td><td>Modeling Environment-Need</td><td>0.21(9.61)</td><td>0.20</td><td>accept  $0.21^a$ </td></tr></table>

<sup>a</sup>Risk level equals 0.05.  
<sup>b</sup>Risk level equals 0.10.

We emphasize that this empirical study is best viewed as exploratory (i.e., descriptive and raising and testing hypotheses as the analysis progressed) and is not without its shortcomings. Because of the limited sample size, we were unable to examine the crossvalidity of the parameter estimates from the structural equations analysis. However, we did perform a rigorous simulation analysis on the estimated parameters which is reported in Appendix A. Also, given our exploratory objectives we refrained from adopting a causal view of any of the hypothesized relationships between the latent constructs. Instead we attempted to: (a) present and interpret consistent themes that relate to the key assumptions of the modeling environment research reported in the literature; and (b) offer some guidance concerning the needs in business and industry for integrated computer-based modeling environments. An important goal of this paper is to persuade readers to think about their current research (e.g., validity of their research assumptions) in terms of what is being suggested and reported by professional modelers and users in Tables 4–8. Finally, we hope that the results from the structural equations analysis will be of benefit to practitioners and designers of integrated modeling environments.<sup>7</sup>

## Appendix A Reliability and Validity of the LISREL Model

## Measurement Model

Before examining the structural model, the measurement model was evaluated by examining both individual item reliability and construct reliability. Table 10 shows that the item reliability of the measures are high ranging from 0.66 to 0.99. The average variance extracted (AVE) should be at least 50% in order to avoid having more variance due to error than valid measurement (Fornell and Larcker 1981). The AVE of all the constructs in the revised model exceeds the acceptable limit of 50%.

<sup>7</sup>Partial support by grants from the NCR Corporation (Cooperative Systems Division), NATO Scientific Affairs Division, and the AT&T Foundation is gratefully acknowledged. However, the views contained in this paper are those of the authors and not of the sponsors. The authors thank the associate editor and referees for many constructive suggestions. We also thank Professor Peg Williams, who helped with the design of the Purdue Technical Database questionnaire.

## Overall Model

Although the chi-square statistic reported in Table 9 indicates that the revised model should be rejected, this test has several well documented problems/limitations (e.g., see Mulaik et. al. 1989, Marsh et al. 1988, Anderson and Gerbing 1984, Bearden et al. 1982). Other measures of the model’s fit reported in Table 9 include the goodness of fit index (Jo¨reskog and So¨rbom 1986), the root mean square residual (Jo¨reskog and So¨rbom 1986), and the comparative fit index (Bentler 1990). The goodness of fit index of 0.91 indicates that the revised model accounts for ninety-one percent of the sum of squares of the sample covariances and provides an acceptable fit (Cuttance 1987). Similarly, the comparative fit index of 0.91 indicates that the revised model provides a substantially better fit to the observed covariance matrix than the null model with no parameters. The root mean square residual shows that the average of the residuals between the fitted and observed covariances in 0.10.

## Simulation Analysis of the Parameter Estimates

Our sample size of 170 is well above the suggested minimum of 100 required for estimating the parameters of the structural equations models of Figures 2 and 3; however, it is not large enough to crossvalidate the results using a holdout sample. As an alternative, we perform a simulation analysis of the parameter estimates to assess their stability in repeated random sampling. This procedure allows us to estimate the bias and covariance matrix of the estimators (see McCarthy et al. 1992), and detect any parameters whose estimated values are strongly affected by seemingly insignificant variations (see Bard 1975, p. 176–183) in the data set. Using the covariance matrix from the original sample, we randomly generate 200 data sets, each consisting of 170 observations on the 17 measurement variables. Next we obtain the maximum likelihood estimates of the five structural parameters for each of the 200 simulated data sets. These estimates are then used to test the null hypothesis that the estimated parameters from the revised model are the true estimates.<sup>8</sup> As shown in Table 11, we could not reject the null hypothesis for any of the estimates n the revised model at the 5% level of significance. The results of a correlation analysis performed on the 17 measurement variables further support the conclusion of the test reported in Table 11.

<sup>8</sup>The interested reader can write to the authors for a detailed description of our simulation and test procedures. The test procedure used in this study is similar to the one used by Chandrasekharan et al. (1994). It probably suffices to say that the procedure is simply a sequence of steps involving standard statistical techniques (for generating additional data samples and performing Binomial tests) that are often used in applied econometric modeling for testing the precision of parameter estimates.

## References

Anderson, J. C. and D. W. Gerbing, “The Effect of Sampling Error on Convergence, Improper Solutions, and Goodness-of-Fit Indices for Maximum Likelihood Confirmatory Factor Analysis,” Psychometrika, 49 (1984), 155–173.

Applegate, L. M., G. Klein, B. R. Konsynski, and J. F. Nunamaker,

“Model Management Systems: Proposed Model Representations and Future Design,” Proc. Sixth International Conf. on Information Systems, (1985), 1–16.

——, B. R. Konsynski, and J. F. Nunamaker, “Model Management Systems: Design for Decision Support,” Decision Support Systems, 2 (1986), 81–91.

Ashton-Tate, Framework III, Ashton-Tate, Torrance, CA, 1988.

Bard, Y., Nonlinear Parameter Estimation, Academic Press, New York, 1975.

Blanning, R. W., “Model Management Systems: An Overview,” Decision Support Systems, 9 (1993), 9–18.

Bentler, P. M., “Comparative Fit Indices in Structural Models,” Psychological Bulletin, 107 (1990), 238–246.

Bollen, K. A., Structural Equations with Latent Variables, Wiley, New York, 1989.

Bradley, G. H. and R. D. Clemence, “Model Integration with a Typed Executable Modeling Language,” Proc. Twenty-First Annual Hawaii International on System Sciences III: Decision Support and Knowledge Based Systems Track, (1988), 403–410.

Brooke, A., D. Kendrick, and A. Meeraus, GAMS: A User’s Guide, Scientific Press, Redwood City, CA, 1988.

C.A.C.I., SIMSCRIPT II.5, Programming Language, C.A.C.I., Los Angeles, CA, 1983.

Chandrasekharan, R., M. Moriarity, and G. P. Wright, “Testing for Unreliable Estimators and Insignificant Forecasts in Combined Forecasts,” J. Forecasting, 13 (1994), 611–624.

Chang, A. M., C. W. Holsapple, and A. B. Whinston, “Model Management Issues and Directions,” Decision Support Systems, 9 (1993), 19–37.

Cunningham, K. and L. Schrage, LINGO Optimization Modeling Language, LINDO Systems, Chicago, IL, 1991.

Cuttance, P., “Issues and Problems in the Application of Covariance Structure Models,” in P. Cuttance and R. Ecob (Eds.), Structural Modeling by Example, Cambridge University Press, New York, 1987.

Dillman, D. A., Mail and Telephone Surveys, Wiley, New York, 1978.

Dolk, D. R., “The Role of an Information Resource Dictionary System,” Comm. ACM, 31, 6 (1988), 704–718.

—— and J. Kottermann, “Model Integration and a Theory of Models,” Decision Support Systems, 9, 1 (1993), 51–63.

—— and B. Konsynski, “Model Management in Organizations,” Information and Management, 9, 1 (1985), 35–47.

—— and ——, “Knowledge Representation for Model Management Systems,” IEEE Trans. on Software Engineering, 6 (1984), 71–91.

Elam, J. J., J. C. Henderson, and L. W. Miller, “Model Management Systems: An Approach to Decision Support in Complex Organizations,” Proc. First International Conf. on Information Systems, (1980), 98–110.

Fornell, C. and D. F. Larcker, “Evaluating Structural Equation Models with Unobservable Variables and Measurement Error,” J. Marketing Res., 18, 1, (1981), 39–50.

Fourier, R., D. M. Gay, and B. W. Kernighan, “A Modeling Language for Mathematical Programming,” Management Sci., 36 (1990), 519–554.

Gass, S. I., “Managing the Modeling Process: A Personal Reflection, “European J. Operational Res.,” 31 (1987), 1–8.

, “Decision-Aiding Models: Validation, Assessment, and Related Issues for Policy Analysis,” Oper. Res., 31, 4 (1983), 603– 631.

Geoffrion, A. M., “An Introduction to Structured Modeling,” Management Sci., 33, (1987), 547–588.

——, “Computer-Based Modeling Environments,” European J. Oper. Res., 41 (1989a), 33–43.

——, “Integrated Modeling Environments,” Computer Sci. in Economics and Management, 21 (1989b), 3–15.

—, “The Formal Aspects of Structured Modeling,” Oper. Res., 37 (1989b), 30–51.

—, “FW/SM: A Prototype Structured Modeling Environment,” Management Sci., 37 (1991), 1513–1538.

, “The SML Language for Structured Modeling: Levels 1 and 2,” Oper. Res., 40 (1992a), 38–57.

, “The SML Language for Structured Modeling: Levels 3 and 4,” Oper. Res., 40 (1992b), 58–75.

—, “Structured Modeling: Survey and Future Research Directions,” ORSA CSTS Newsletter, 15, (1994), 10–20.

Jo¨ reskog, K. G., “A General Method for Estimating a Linear Structural Equation System,” Structural Equations in the Social Sciences, A. S. Goldberger and O. D. Duncan (eds.), Princeton University Press, Princeton, NJ, 1973.

and Dag So¨rbom, “LISREL: Analysis of Linear Structural Relationships by the Method of Maximum Likelihood,” User’s Guide, Version VI, Scientific Software, Mooresville, IN, 1986.

Kang, M., G. P. Wright, R. Chandrasekharan, R. Mookerjee, and N. D. Worobetz, “The Design and Implementation of OR/SM: A Prototype Integrated Modeling Environment,” 1997 Ann. Oper. Res. (special issue on the IS/OR interface).

Kottermann, J. E. and D. R. Dolk, “Model Integration and Modeling Languages: A Process Perspective,” Information Systems Res., 3, 1, (1992), 1–16.

Krishnan, R., “Model Management: Survey, Future Directions and a Bibliography,” ORSA CSTS Newsletter 14, 1 (1993).

Lenard, M. L., “An Object Oriented Approach to Model Management,” Decision Support Systems, 9 (1993), 67–73.

Liang, T. P., “Integrating Model Management with Data Management in Decision Support Systems,” Decision Support Systems 1 (1985), 221–232.

——, “Development of a Knowledge-Based Model Management System,” Oper. Res., 36, 6 (1988), 849–863.

Marsh, H. W., J. R. Balla, and R. P. MacDonald, “Goodness of Fit Indices in Confirmatory Factor Analysis: The Effect of Sample Size,” Psychological Bulletin, 103 (1988), 391–410.

McCarthy, P. S., P. K. Kannan, R. Chandrasekharan, and G. P. Wright, “Estimating Loyalty and Switching with an Application to the Automobile Market,” Management Sci., 38 (1992), 1371–1393.

Medsker, G. J., L. J. Williams, and P. J. Holahan, “A Review of Current Practices for Evaluating Causal Models in Organizational Behavior and Human Resources Management Research,” Working Paper, Krannert Graduate School of Management, Purdue University, West Lafayette, IN, 1990.

Mulaik, S. A., J. Van Alstine, N. Bennet, and C. D. Stillwell, “An Evaluation of Goodness of Fit Indices for Structural Equation Models,” Psychological Bulletin, 105 (1989), 430–445.

Neustadter, L., A. Geoffrion, S. Maturana, Y. Tsai, and F. Vicuna, “The Design and Implementation of a Prototype Structured Modeling Environment,” Ann. Oper. Res., 38 (1992), 453–484.

Norusis, M., SPSS Base System User’s Guide, Release 6.0, SPSS Inc., Chicago, IL, 1987.

ORACLE, ORACLE Version 5.1.c, ORACLE, Belmont, CA, 1989.

Ramirez, R., “The ISUMMS Project and Bibliography,” ISUMMS Project Informal Note No. 2, Department of Management, Iowa State University, 1993.

SAS Institute Inc., SAS/STAT User’s Guide, Version 6, SAS Institute, Cary, NC, 1989.

SAS Institute Inc., SAS/OR User’s Guide, Version 6, SAS Institute, Cary, NC, 1989.

Shaw, M. J., J. P. Tu, and P. De, “Applying Machine Learning to Model Management in Decision Support Systems,” Decision Support Systems, 4, 3 (1988), 285–305.

Will, H. J., “Model Management Systems,” Information Systems and Organization Structure, W. Gruyter, Berlin, 468–482, 1975.

Wright, G. P., N. D. Worobetz, M. Kang, R. Mookerjee, and R. Chandrasekharan, “OR/SM: A Prototype Integrated Modeling Environment Based On Structured Modeling,” INFORMS J. Computing, 9, 2 (1997) 134–153.

Michael J. Shaw, Associate Editor. This paper was received on November 17, 1995 and has been with the authors 7 months for 1 revision.
