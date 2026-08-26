---
otero_id: 10136
otero_key: "685BRVZR"
title: "A Model for Measuring Information System Size"
authors: "Clive D. Wrigley; Albert S. Dexter"
year: "1991"
journal: "MIS Quarterly"
doi: "10.2307/249386"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Model for Measuring Information System Size

By: Clive D. Wrigley
Faculty of Management
McGill University
Montreal, Quebec
Canada H3A 1G5

Albert S. Dexter
Faculty of Commerce and Business Administration
University of British Columbia
2053 Main Mall
Vancouver, British Columbia
Canada V6T 1Y8

## Abstract

Management of the software development process requires a thorough understanding of the environment in which development takes place. Ability to estimate, plan, and manage resource consumption is limited by the central problem of determining the size of system specifications. To address this issue, a general strategy for measurement and evaluation of system development environments needs to be established. This article presents a research model that will help managers and researchers understand and establish the linkages between units of systems requirements specification, design, and source code. Initial validation of the model was performed by reverse engineering systems written in a fourth generation language from source code to design metrics. Results indicate that the model may provide reliable measures of system size in terms of both design metrics and lines of code.

Keywords: Models and principles, tools and techniques, software metrics, reverse engineering, fourth generation languages, FOCUS, software management, field study

ACM Categories: D.2.1, D.2.2, D.2.8, D.2.9, D.3.2, H.1.0, K.6.3

## Introduction

A central problem facing management is the uncertainty of developing software, in part stemming from rapidly developing technologies, personnel productivity differences, and unknown system size. $^{1}$ This uncertainty inhibits accurate estimation of resource consumption prior to development and therefore threatens rational project planning and control. This uncertainty may be reduced in part, by fully understanding past system development efforts within a firm, as well as by making comparisons across firms. This study applies a research methodology and measurement instrument to one firm's source code and project management system to extract information on previous systems development projects.

In doing so, the methodology establishes the linkages between requirements size, design size, and the amount of FOCUS code needed to implement those requirements. The instrument provides a reliable measure of system size for a specific environment by reverse engineering the source code back to measures of design. The article begins to address the problem of modelling information systems size for the purposes of estimating resource consumption early in the development life cycle. However, the model itself does not include organizational or technical uncertainty. The following three main empirical limitations further restrict the generalizability of the results. First, the study does not measure personnel experience, the use of different productivity tools, or reusable code. Second, only small transaction processing systems, written in a single language within a single firm were measured. Finally, the reverse engineering process only brings code back to measures of design. Thus, the study explains the linkage between design and code. It does not solve the problem of predicting size based upon requirements analysis.

The objectives of this article are to:

1. Present a research design that addresses issues of validity and reliability in the measurement of software development;

2. Provide a measurement instrument that may be used to calibrate individual system development environments; and

3. Empirically test the research approach.

The article proceeds as follows. First, it discusses the relevant literature on sizing techniques and measurement issues. It then develops an effort model and a research model that emphasize validity and reliability of measurement. Next is a validation effort with 26 small transaction processing systems comprising 720 programs written in the FOCUS language containing 60,000 source statements. An automated tool is used to reverse engineer the computer code in order to measure the size of the information systems. The article concludes with a discussion of the limitations and extensions of the research.

## Estimating Models and the Sizing Problem

The problem of software development has consistently ranked in the top 10 IS Issues for the past decade (see, Ball and Harris, 1982; Brancheau and Wetherbe, 1987; Dexter, et al., 1990; Dickson, et al., 1984; Hartog and Herbert, 1986). Numerous software cost estimation models have appeared in the literature over the past two decades. Several authors have suggested a taxonomy of these estimating approaches (Basili, 1980; Benbasat and Vessey, 1980; Conte, et al., 1986; Kitchenham and Taylor, 1984; Wolverton, 1974). A review and critique of these approaches appears in Boehm, 1981; Golden, et al., 1981; Kitchenham and Taylor, 1984; Mohanty, 1981; and Wrigley and Dexter, 1987, with empirical validations performed by Albrecht and Gaffney (1983) and Kemerer (1987). A recurrent problem is that an understanding of system size, however measured, is crucial in order for the human estimator to predict actual effort required to build a given system. Two sizing approaches, lines of code (LOC) and function points (FP), are the most cited.

## Lines of code

Several models exist in which a size estimate in lines of code (LOC) is the prime input into the model. These include the meta model (Bailey and Basili, 1981), COCOMO (Boehm, 1981), and SLIM (Putnam, 1978; 1979; Wolverton, 1974).

However, the use of LOC as an input to an estimating model has several drawbacks. These problems are:

1. LOC size is the net result of the development process. Knowledge of the factors affecting LOC do not emerge until later in the process.

2. LOC size is that which results after requirements have been met. It should not be considered as a target.

3. LOC size estimates at either the requirements phase or the design phase are quite subjective and may vary from one analyst to the next.

The central methodological weakness with the LOC sizing approach is one of causality. LOCs do not themselves cause effort, they are the result of effort expended. While the above authors have contributed substantially to our understanding of the issues, one may conclude that SLIM, COCOMO, and the others are not early sizing models but are better suited to estimating resource consumption and scheduling once a size estimate is available and productivity factors are known.

## Function points

A number of models instead use function points as the basis for sizing a system (Albrecht, 1979; 1984; Albrecht and Gaffney, 1983; Desharnais, 1988; Jones, 1986; Rubin, 1983; 1985; Symons, 1988). This more recent approach classifies software into five basic functional categories. These have been labelled by Albrecht (1979) as external inputs, external outputs, logical internal files, external interface files, and external inquiry. Our ability to estimate these larger units of software is better than estimating LOC because the information necessary to measure the units is available earlier in the life cycle. Problems with function point analysis were succinctly reviewed and articulated by Symons (1988), who indicates that the very process of measurement is fraught with difficulties due to variability in experience and skill among analysts. $^{2}$ Briefly, two criticisms can be levelled at function point analysis:

1. Function point weights and complexity adjustments may not be generalizable outside of a particular project data set. This implies that all scales used in function point analysis are derived from empirical relationships found in a specific project database, pointing to the need to calibrate each environment separately.

2. Assessing the complexity level of each major function type and determining overall processing complexity adjustments is subjective and may vary from one analyst to the next, introducing a source of error in the estimate.

The second criticism may be mitigated when function point analysis is performed with consistent guidelines and by a common analyst group. Recent evidence (Kemerer, 1991) indicates measurement reliability may be reasonable in the above circumstances.

Additionally, the point at which function point measures are available depends, in part, upon the systems analysis modelling techniques and the systems development methodology used. To date there has not been a clear articulation of the relationships between the various systems modelling techniques and function points. For example, outputs from structured analysis may include entities, relationships, and mapping ratios from data modelling; outputs from process modelling may include process bubbles, data stores, data flows, and external entities. De Marco (1982) suggests, but does not operationalize, a “bang” sizing method based upon function point-like primitives that are available early in the systems development life cycle. As a step toward identifying which principle sizing indicators to use, De Marco differentiates systems on two axes: scientific to business processing and function strong to data strong. Much of business data processing can be characterized as data strong. This article assumes that requirements size of these business applications may be captured in terms of their process and data requirements, which in turn cause development effort.

## Effort Model

The next step toward establishing a research model for measuring information system size is to understand the primary antecedents of system development effort. The central question is: On what variables does the amount of effort depend? A model to help structure this question has been synthesized from the literature and appears in Figure 1.

![](/api/attachments/685BRVZR/fulltext/images/16569b4636c6e14422b89165b125bbd1f2827fd28c29a3f00ad58985702103a4.jpg)  
Figure 1. System Development Effort Model

The model is similar in form to one proposed by Chrysler (1978), used by Jeffery (1987), and described by Wrigley and Dexter (1988). Figure 1 may be interpreted as follows. An increase in system requirements size (or scope) increases the effort required to implement, while increases in personnel experience and skill, and methods and tools mitigate this effort. The three constructs, system requirements, personnel experience, and methods and tools, correspond approximately to the concepts of problem space, labor, and capital, respectively. Because the constructs in Figure 1 are temporally antecedent to the development process, this model suggests that these three constructs causally affect effort throughout the entire system development life cycle. The model also suggests that these variables are independent; however, there may well be interaction effects between requirement types, personnel skills, and tools used. For example, more experienced personnel likely would be assigned to the more difficult projects. Because of the possibility of such interaction effects, the model presents only the main effects.

A second causal effect may be proposed to exist between effort and the resulting software product. The software product results only after effort is expended. This relationship shows clearly the justification for not using the outputs from system development as inputs into estimating models. What is required are measures of an information system that exist prior to significant resource consumption, i.e., earlier in the system development life cycle. The remainder of this article focuses primarily on the issue of information system size.

## Research Model

Research into software engineering and the system development process in general has suffered from the lack of a nomological net, i.e., the theoretical connections among a set of concepts or constructs in which to discuss empirical phenomena. Further, substantive research in software engineering has been carried out in the absence of construct validation research. $^{3}$

Figure 2 develops a model to help overcome these deficiencies in software engineering. It provides a framework for the discussion of both construct validation and substantive knowledge about the system development process. It highlights the relationships between the system desired and the one defined for development, and between the design and coding effort expected and actual work hours expended. Figure 2 depicts both the conceptual and empirical relationships among the independent and dependent variables of interest, which originate from the effort model in Figure 1.

The research model is interpreted as follows. At the conceptual level, there exists a relationship between the size of the requirements of the real system and the size of the eventual software product. Each stage of development is achieved through the various processes; analysis, design, and coding. System specifications at each stage are transformed into the next stage through these processes, which are moderated by two factors: kinds of methods and tools used and the skill level of the system builders. The independent variables are labelled as IV, the moderating variables are depicted as MV, and the dependent variables as DV. The system requirements size construct is further defined as including both system statics and system dynamics. Within an information system, statics is defined as the state of the IS at a point in time. This entails its internal structural relationships as well as its retained data. Similarly dynamics is defined as system responses to external stimuli and internal control mechanisms. It is important to realize that the constructs at this level cannot be measured directly.

In Figure 2, system requirements size (IV) $_{1}$ is shown to cause design size (DV $_{2}$ ) through the process of design. Design size in turn becomes (IV $_{2}$ ), which causes the software size (DV $_{2}$ ) through the coding process. Note that the output of the analysis activity (DV $_{1}$ ) becomes the input into the design activity (IV $_{2}$ ). The size of the working system represents the result of the two transformations from system requirements and design, hence the subscripts 1 and 2. The size of the initial requirements, through the design and coding phases, are reflected in the eventual size of the working system. The process of systems development, among other things, consumes resources during analysis of information requirements, design of specifications, and coding of specifications into an operational system. This conceptualization is consistent with Kottemann and Konsynski (1983) and Wand and Weber (1988), who also maintain that a working information system is the result of a series of transformations from conceptual reality in the minds of users to analysis, design, coding, and a final translation into machine representation via the use of compilers or interpreters. Each of these transformations, except the final translation, requires human effort to understand and structure the information system.

![](/api/attachments/685BRVZR/fulltext/images/4420195ca45783256bc2c2a69876a18e86701669d9a2231900ecc0cde7d40b2e.jpg)  
Figure 2. Research Model for Measuring Information System Size

The principle of top-down decomposition and stepwise refinement implies that units at higher levels of abstraction subsequently map to many units at more detailed levels (DeMarco, 1978; Jackson, 1975; Warnier, 1974). Conceptually, the analysis units consist of (1) the static real world objects that are to be modelled within the information system and (2) knowledge of the dynamic events that will occur at the system boundary involving those objects. The static and dynamic properties of the system should be transformationally invariant throughout analysis, design, and coding. Furthermore, it is hypothesized that system statics and dynamics are measurable at each phase of the system development life cycle (SDLC). The actual measurement units will depend upon the system modelling techniques applied.

At the empirical level, the system static and dynamic aspects of requirements size ( $IV_{1}$ ) are operationalized as entities and relationships, input events, and output events ( $IV_{1}$ ). Similarly, the static aspects of design size ( $DV_{1}$ ) are operationalized as files, fields, projections, and joins, while the dynamic aspects are operationalized as reports, screens, and I/O data elements (DV $_{1}$ ). These design measures are analogous to function points. The size of the working system (DV $_{2}$ ) is operationalized as source lines of code (DV $_{2}$ ). $^{4}$ For the purposes of project management and understanding resource consumption, the most useful operationalization of the transformation processes is work hours.

Because the requirements are temporally antecedent to the eventual code, and to the extent that measures of requirements size are correlated with measures of design size and that measures of design size are correlated with code size, one can specify a causal relationship between requirements, design, and code. In this study, the reverse engineering of the code to the design measures serves initially only as concurrent validation of this relationship. As will be shown in the empirical study, the design size measures explain variations in code size.

The reason that the mapping between measures of requirements, design, and code is important is that these units are functionally related. It is claimed that there is a causal relationship between size of requirements and eventual resource consumption. However, these units are not directly comparable. Once the functional relationships between requirements size and code are established then code becomes a useful measure of output from the development effort. The issue of establishing a consistent relationship is the subject of the next section.

While Figure 2 provides a framework for research, the issue of measurement needs to be addressed. Recalling the earlier discussion on function points, there are two main shortcomings of software measurement: lack of portability of the measures across development environments and measurement reliability. Portability refers to the extent to which the relationships between analysis, design and coding measures are generalizable. Reliability of measurement refers to the extent that various measures of code, or design, are consistently measured by one analyst to the next and from one system to the next. To help overcome both shortcomings, an automated code analyzer is used to reverse engineer source code of working systems to ascertain the specific relationships between design metrics and code. Eventually, as the analyzer is applied to multiple sites, some generalizability, at least for the specific language, may evolve. Reliability, the second problem of measurement, is mitigated by the analyzer's reverse engineering of installed systems. The automated tool provides the expertise of a single expert systems evaluator, eliminating the issue of measurement variance, as well as providing analytical tractability.

The above discussion lays out the conceptual and operational framework. The next section presents the empirical portion of the research, first discussing the reverse engineering process and then describing a specific field investigation. A prototype automated code analyzer has been developed that reads the source code of working systems and produces a design metrics database. Statistical routines analyze this database and provide the empirical measures that relate the design metrics to lines of code.

## The Empirical Study

## Description of the reverse engineering process

It has been argued that the source code from working systems can be reverse engineered to establish linkages between source code and measures of design. The findings discussed in the next section are the result of reverse engineering the code back to the design metrics shown in Figure 2.

If we assume that system designers decompose a requirement specification into processes (programs, modules) that deal with or hide some aspect of the specification (see, e.g., Parnas, 1972), then it is reasonable to classify a system's programs according to the function(s) they perform by analyzing the language usage within each program. For example, a program that has a high content of screen I/O and file manipulation statements will most likely be an online transaction capture program. Once the linkages are established between design metrics and code for a given environment, it is then possible to introduce effort and other project factors into the measurement model. This is achieved by extracting resource consumption data from the project management system and regressing these data against the design metrics. The resulting regression may help explain effort for a specific system development environment consisting of a unique mixture of people skills and applied technology.

At the heart of the measurement process is the code analyzer, which takes as input the source code of completed working systems and generates a number of software metrics. The code analyzer scans and parses each program's source code and populates a database of software measures. These include:

1. Program classification

Input: The program accepts input from a file or a screen and modifies the database.

Output: The program reads from internal files and generates files or printed output.

Mixed: The program contains both input and output definitions described above.

Control: The program calls other programs either by user selection (through menus) or job controls

2. Program length measured by text lines (excluding comments)

3. Software science and cyclomatic complexity metrics (see Halstead, 1977; McCabe, 1976)

4. Number of screen images and number of data elements per screen

5. Number of reports and output variables

6. Number of files accessed and their structures

7. Number of projection and join manipulations performed on files

## Research setting

For any empirical assessment of the reverse engineering process a general strategy for data collection and analysis is necessary. As systems evolve through the development process from requirements to eventual working programs, the project management system should collect the following types of data: amount of resource consumption at each milestone, personnel involved (classed by skill level), any CASE tools or other methods used, and other demographics. Thus, the measurement includes both project details and the eventual code. This strategy amounts to the establishment of a software metrics group in each organization, as advocated by both DeMarco (1982) and Basili (1988).

A single 4GL FOCUS environment was selected for the empirical analysis. One problem facing management in a 4GL development environment is that the software engineering research to date deals primarily with 3rd generation languages. Although measurement is difficult in 3GL environments, the uncertainty regarding the impact of a 4GL makes the measurement even more problematic. To date few studies exist concerning the nature of 4GLs (e.g., Harel and McLean, 1985; Misra and Jalics, 1988; and Verner and Tate, 1988), even though usage has grown rapidly. Therefore, there is a current need to study 4GL development environments.

The research setting can be described as typical of modern commercial development shops. The DP services group employs nearly 80 people in a variety of jobs including clerical, machine operators, information center staff, programmers, senior analysts, and project leaders. The information systems in use consists of those developed in-house as well as modified packages. Both 3GL (COBOL, PL/1) and 4GL (FOCUS) languages are used. The staff turnover is comparatively low—most professional personnel were on staff throughout the time period of the systems analyzed. Only one programmer, who wrote 15 percent of the code, was unavailable to answer questions that arose during the course of the investigation. The computing environment was constant, e.g., same operating system, screen editors, etc., over the development period from 1984 to 1988 for the systems analyzed.

The data available for this study comprise 26 application systems written in FOCUS. All systems were identified via discussions with managers and senior analysts and cross-checked with the project control system. All systems developed by the company's Small Projects Group between 1984 and 1988 became the data for analysis. To ensure that all FOCUS source code was analyzed, the researchers and the analysts scrutinized both source and production libraries. Data available from the project management system, but not used in this article, include:

• Business function/application type

\- Programmer(s) and skill level

\- Hours to build: analysis to implementation plus maintenance

\- Project elapsed time

The 26 systems contained more than 770 FOCUS programs and 60,000 FOCUS lines of code (LOC). To establish the relationship between detailed design and LOC, the FOCUS source code was first reverse engineered using the program as the unit of analysis. Then, to establish the relationship between preliminary design and LOC, the program measures were aggregated to form overall system measures. Therefore the discussion will proceed first by considering the program as the unit of analysis followed by a discussion considering the system as the unit of analysis.

## Data Analysis

## Program level

All statistical analyses were performed using the statistical package MIDAS. Of the 770 programs, five distinct program classifications emerged: updates, primarily reflecting input events (n = 129); reports, reflecting output events (n = 369); a mixed category having both updates and reports (n = 71); menus controlling access to these processes (n = 151); and unclassified programs (50). While this last classification comprised 6 percent of the number of programs, it involved less than 1 percent of the total code. Furthermore, the code analyzer did not classify the programs because they contained no code chunks or keywords that were identifiable as a design decision, and hence no design effort was involved. Generally, these programs consisted mainly of small code stubs (e.g., “include” files, utility programs, function key definitions, etc.). They were therefore discarded from further analysis. The program demographics are shown in Table 1.

For the 720 programs a means/variance test was run to determine how the programs in each classification differed from one other. The means and variance, in terms of LOC, of each program class were significantly different (p < .001). Therefore, two indicator variables, representing updates and reports, were added to allow a single regression model to be tested. (The following coding scheme was used: update = 10, report = 01, mixed = 11, menu = 00.)

From the operational measures of design identified in Figure 2, the regression model to explain code size in terms of lines of FOCUS code at the program level is shown in Figure 3.

Adjusted $R^{2}$ for the model is .82 with a standard error of 46.8, while F = 425 and p = 0. As can be seen from the standard error terms, parenthesized under the regression co-efficients, the regression variables are highly significant at p < .01, except the report\_indicator (p < .08) and the files\_accessed variable (p < .59). The latter case is due to the variable being collinear with fields\_in\_files, a problem addressed by a more parsimonious model below.

This result indicates that a linear model substantially explains code size. However, our general notions of complexity suggest that increases in requirements and design size may result in a nonlinear increase in code size. To address the possibility that code size increases non-linearly with increased size of design, and to make the sizing method more generalizable to other settings, second-order terms for each of the six non-dummy independent variables were added to the model. This expanded model explained less than

Table 1. Program Demographics: LOC

<table><tr><td>Classification</td><td>Frequency</td><td>Min Size</td><td>Max Size</td><td>Mean</td><td>Std. Dev.</td><td>% of Total Code</td></tr><tr><td>Updates</td><td>129</td><td>9</td><td>910</td><td>156.9</td><td>188.4</td><td>33.4</td></tr><tr><td>Reports</td><td>369</td><td>4</td><td>757</td><td>64.9</td><td>73.6</td><td>39.5</td></tr><tr><td>Mixed</td><td>71</td><td>14</td><td>679</td><td>129.4</td><td>125.3</td><td>15.2</td></tr><tr><td>Menus</td><td>151</td><td>4</td><td>285</td><td>47.7</td><td>40.8</td><td>11.9</td></tr><tr><td>Total</td><td>720</td><td>4</td><td>910</td><td>84.2</td><td>112.2</td><td>100.0</td></tr></table>

<table><tr><td>LOC = 19.88*[update_indicator] + 8.40*[report_indicator] + 1.18*[files_accessed] + (4.60) (4.84) (2.10).26*[fields_in_files] + 12.36*[projections_and_joins_on_files] + (.09) (1.29)27.72*[screen_images] + 1.96*[input_data_elements] + (1.7) (.16).77*[output_data_elements]; (.04)</td></tr></table>

Figure 3. Program-Level Model

1 percent additional variance in code size compared with the more parsimonious linear model. Another alternative for dealing with the possible non-linearity issue required performing a log transform on each of the variables. However, this transform also did not improve the results.

A visual analysis of the regression residuals shows no heteroscedastic behavior. However, the Kolmogorov-Smirnov statistic (.11) for distribution equality when compared to a normal distribution indicates that the residual error term is slightly non-normal. As shown in Figure 4, a log transform of the dependent variable, LOC, removes the non-normal behavior remaining in the error term. The regression terms are significant at p < .01, except for input\_data\_elements (p < .08) and files\_accessed (p < .03); however, the explained variance drops to 59 percent:

The independent variables in Figures 3 and 4 represent information available at the detailed design stage. A more parsimonious model, one that represents information available earlier in the SDLC, is shown in Figure 5.

The explained variance for this more parsimonious linear model drops to 77 percent with each of the independent variables significant at p < .05. The residual error term behaved identically to the larger model. The log transform on the dependent variable removed the apparent non-normal behavior and the explained variance dropped to 51 percent, while all independent variables retained their significance at p < .001.

## System level

The above analysis has been conducted with the program as the unit of inquiry. However, the information necessary to establish individual program size is only available after extensive design work is complete. The research model shown in Figure 2 suggests that measures of systems size may be made earlier than during the detailed design phase. In order to move toward an understanding of size earlier in the SDLC, it is necessary to consider the entire system as the unit of analysis rather than individual programs. To achieve this, it was necessary to aggregate from the detailed design phase certain measures that would be available earlier in the SDLC and would represent system level measures. Recalling from Figure 2, during preliminary design the following measures of system size are available: screens, reports, and files. The program design measures were aggregated to obtain each system's size. For example, screen and report images, along with unique file definitions, were identified and counted. The regression model used to explain code size at the system level is shown in Figure 6.

```txt
In LOC = 3.0 + .38*[update_indicator] + .19*[report_indicator] - .07*[files_accessed] +
(.06) (.07) (.07) (.03)
.007*[fields_in_files] + .14*[projections_and_joins_on_files] +
(.001) (.02)
.33*[screen_images] + .004*[input_data_elements] +
(.03) (.002)
.004*[output_data_elements];
(.001)
```  
Figure 4. Log Transform Model

<table><tr><td>LOC = -16.8 + 16.90*[update_indicator] + 10.19*[report_indicator] + 21.22*[files_accessed] + (4.56) (5.22) (5.30) (1.76)</td></tr><tr><td>41.08*[screen_images] + .94*[output_data_elements]; (1.51) (.04)</td></tr></table>

Figure 5. Earlier Program-Level Model

For these 26 systems the three measures of design size explain LOC size quite well. The number of screens, reports, and files together explain 94 percent of the variance in the linear regression model with each of the independent variables significant at p < .01. An analysis of the residuals shows both homoscedastic behavior and a normal distribution, with a Kolmogorov-Smirnov statistic of .12, well within the critical point of .26 at the 5 percent level of significance. The negative intercept is not meaningful in this context because there are no observations close to the zero intercept; thus, extending the regression line past the range of the small data set is inappropriate.

## Extensions and Summary

The main contributions of this article are as follows. It develops the theoretical relationships among the measures of system size available at each phase of system development. It establishes a methodology for determining the factors that contribute to code size for specific development environments. If each system development environment is to be analyzed prior to using any sizing technique, then the measurement process must be reliable and computationally tractable. This research achieves both of these objectives.

Based upon the regression results presented above we may conclude at the program level that given an accurate detailed design, which specifies the major input and output activity for programs, good predictions of code size are possible. This alone explains 83 percent of the variance in code size in this study. Furthermore, it is possible to explain overall system size in terms of LOC if the developers create an accurate preliminary design document that specifies major system objects such as master files (representing system statics), and screens and reports (representing system dynamics). These measures of preliminary design size together explain 94 percent of the variance in code size. However, at the systems level, it is premature to state that the model holds generally because several large systems could create this exceptionally high $R^{2}$ result.

The extendability of the regression model for predicting new system development has not been assessed. This would require longitudinal tracking of the system development process. However, the tracking of new project development given the above calibration of existing systems is a reasonably straightforward extension. In fact, once a manager has this type of data on past systems and productivity, this approach may help to set up organizational standards for predicting new development or enhancements to existing systems.

Measures of systems design in this research were derived from the source code. The design units used are typical of business transaction processing systems. For systems such as scientific or function-strong systems, it is likely that measurement units in addition to screens, reports, etc. would need to be reverse engineered out of the software to reflect design and, eventually, requirements size.

![](/api/attachments/685BRVZR/fulltext/images/f776a067ef8bc81cd1e50f624ec272ba545964540cf5f0ba1f52d7ddae4a82a9.jpg)  
Figure 6. System-Level Model

Moving from design specification back to requirements specification is a difficult problem for reverse engineering. Semantic inferences from the design specification would have to be made by methods such as aggregating a number of processes to represent a conceptual input or output event. Further, the identification of entities and relationships in the code would likely require domain knowledge to be effective. The machine-reversed requirements would also have to be validated by human analysts. Future studies should focus on properties of information systems that are measurable during analysis and can be empirically correlated to the amount of effort and code required for development. In order to make the linkage between design size and requirements size it would be easier to start from a complete set of requirements specifications such as data flow diagrams and/or entity relationship models. In the case of data flow diagrams, these may be measured by counting process bubbles, number of data flows, stores, and data elements. For the ER Models, the number of entities, number of relationships, and number of attributes may be counted. These units may then be regressed against LOC.

To summarize, this article has placed the problem of system sizing into a framework that shows both the conceptual and empirical linkages between design metrics and effort. The two major limitations of the paper are (1) that only the design to code transformation has been fully operationalized; and (2) the empirical analysis has been limited to small business systems using a 4GL within a single commercial environment. However, because the automated tool is portable, the research method is fully generalizable to measuring and evaluating other FOCUS system development environments. This is a first step in the measurement and evaluation of a major 4GL language.

In future studies the automated code analyzer will provide a systematic tool to assist in the measurement and evaluation of the systems development process; this type of research should be extended across firms and across the systems development life cycle. The method should be used in a wider variety of FOCUS environments encompassing both small user-developed applications and larger professionally developed systems. Enhancements to the code analyzer will allow the measurement of code reusability. The objective is to move toward estimating effort earlier in the life cycle, recognizing the need to control for or measure managerial style, motivation, personnel differences, and other development support tools.

## Acknowledgements

This research is supported in part by the Natural Sciences and Engineering Research Council of Canada, and Information Builders Inc. The authors would like to thank the associate editor and the anonymous reviewers for their considered comments and helpful suggestions.

## References

Albrecht, A. J. "Measuring Application Development Productivity," Proceedings of the IBM Applications Development Symposium, GUIDE/SHARE, October 1979, pp. 83–92.

Albrecht, A. J. AD/M Productivity Measurement and Estimate Validation, CIS & A Guideline 313, IBM Corporate Information Systems and Administration, New York, NY, November 1984.

Albrecht, A.J. and Gaffney J., Jr. "Software Function, Source Lines of Code, and Development Effort Prediction: A Software Science Validation," IEEE Transactions on Software Engineering (SE-9:6), November 1983, pp. 639–648.

Bailey, J.W. and Basili, V.R. "A Meta-Model for Software Development Resource Expenditures," Proceedings of the Fifth International Conference on Software Engineering, March 1981, pp.107–116.

Ball, L. and Harris, R. "SMIS: A Membership Analysis," MIS Quarterly (6:1), March 1982, pp. 23–45.

Banker, R.D., Datar, S.M., and Zweig, D. "Software Complexity and Maintainability," Proceedings of the Tenth International Conference on Information Systems, Boston, MA, December 1989, pp. 247–255.

Basili, V.R. Models and Metrics for Software Management and Engineering: Tutorial, IEEE Computer Society Press, New York, NY, 1980.

Basili, V.R. and Rombach, H.D. "The TAME Project: Towards Improvement Oriented Software Environments," IEEE Transactions on Software Engineering (14:6), June 1988, pp. 758–773.

Benbasat, I. and Vessey, I. "Programmer and Analyst Time/Cost Estimation," MIS Quarterly (4:2), June 1980, pp. 31–42.

Boehm, B.W. Software Engineering Economics, Prentice-Hall Inc., Englewood Cliffs, NJ, 1981.

Brancheau, J.C. and Wetherbe, J.C. "Key Issues In Information Systems Management," MIS Quarterly (11:1), March 1987, pp. 23–45.

Chrysler, E. “Some Basic Determinants of Computer Programming Productivity,” Communications of the ACM (21:6), June 1978, pp. 472–483.

Conte, S.D., Dunsmore, H.E., and Shen, V.Y. Software Engineering Metrics and Models, Benjamin/Cummings Publishing Company, Inc., Menlo Park, CA, 1986.

DeMarco, T. Structural Analysis and System Specification, Yourdon Press, New York, NY, 1978.

DeMarco, T. Controlling Software Projects, Prentice-Hall, Englewood Cliffs, NJ, 1982.

Desharnais, J.M. Analyze statistique de la productivite des projets de développement en informatique a partir de la technique des points de fonction, master of science thesis, Universite du Quebec à Montreal, Montreal, Quebec, December 1988.

Dexter, A.S., Graham, J.A., and Huff, S. "The Issues of Concern to Information Systems Managers: A Survey," working paper, 1990-1, Faculty of Commerce and Business Administration, University of British Columbia, Vancouver, British Columbia, 1990.

Dickson, G.W., Leitheiser, R.L., Nechis, M., and Wetherbe, J.C. “Key Information System Issues for the 1980’s,” MIS Quarterly (8:3), September 1984, pp. 135–159.

Golden, J.R., Mueller, J.R., and Anselm, B. "Software Cost Estimating: Craft or Witchcraft," DATA BASE (12:3), Spring 1981, pp. 12–14.

Halstead, M.H. Elements of Software Science. Elsevier, North-Holland, New York, NY, 1977.

Harel, E.C. and McLean, E.R. "The Effects of Using Nonprocedural Computer Language on Programmer Productivity," MIS Quarterly (8:2), June 1985, pp. 109–120.

Hartog, C. and Herbert, M. “MIS Rates the Issues,” Datamation, November 15, 1986, pp.79–86.

Jackson, M. Principles of Program Design, Academic Press, London, 1975.

Jeffery, D. R. "Software Engineering Productivity Models for Management Information System

Development," in Critical Issues in Information Systems Research, R.J. Boland, Jr. and R.A. Hirshheim (eds.), John Wiley, London, 1987, pp. 113–134.

Jones, C. Programming Productivity, McGraw-Hill, Inc., New York, NY, 1986.

Kemerer, C.F. "An Empirical Validation of Software Cost Estimation Models," Communications of the ACM (30:5), May 1987, pp. 416–429.

Kemerer, C.F. “Reliability of Function Points Measurement: A Field Experiment,” working paper, 3193-90-MSA, Massachusetts Institute of Technology, Cambridge, MA, January 1991.

Kemerer, C.F. "An Empirical Validation of Software Cost Estimation Models", Communications of the ACM (30:3), May 1987, pp. 416–429.

Kitchenham, B.A. and Taylor, N.R. "Software Cost Models," ICL Technical Journal (4:1), May 1984, pp. 73–102.

Kottemann, J.E. and Konsynski, B.R. "Complexity Assessment: A Design and Management Tool For Information System Development," Information Systems (8:3), 1983, pp. 195–206.

McCabe T.J. "A Complexity Measure," IEEE Transactions on Software Engineering (2:4), December 1976, pp. 308–320.

Misra, S.K. and Jalics, P.J. Third Generation versus Fourth Generation Software Development," IEEE Software (5:4), July 1988, pp. 8–14.

Mohanty, S.N. "Software Cost Estimation: Present and Future," Software-Practice and Experience (11:2), February 1981, pp. 103–121.

Parnas, D. "On the Criteria to be Used in Decomposing Systems Into Modules," Communications of the ACM (15:12), December 1972, pp. 221–227.

Putnam, L.H. "A General Empirical Solution to the Macro Software Sizing and Estimating Problem," IEEE Transactions on Software Engineering (SE-4:4), July 1978, pp. 345–361.

Putnam, L.H. and Fitzsimmons, A. “Estimating Software Costs,” Datamation (25:10, 11, 12), September, October, November 1979 (three-part article).

Rubin, H.A. "Macro-Estimation of Software Development Parameters: The ESTIMACS System," in SOFTAIR Conference on Software Development Tools, Techniques, and Alternatives, Arlington, VA, July 25–28, 1983,

pp. 109–118.

Rubin, H.A. “The Art and Science of Software Estimation: Fifth Generation Estimators,” in Proceedings of the 7th Annual ISPA Conference, Orlando, FL, May 7–9, 1985, pp. 56–72.

Schwab, D.P. "Construct Validity in Organizational Behaviour," in Research in Organization Behaviour (2), JAI Press Inc., Greenwich, CT, 1980, pp. 3–43.

Symons, C.R. "Function Point Analysis: Difficulties and Improvements," IEEE Transactions on Software Engineering (14:1), January 1988, pp. 2–11.

Verner, J. and Tate, G. "Estimating Size and Effort in Fourth Generation Development," IEEE Software, July 1988, pp. 15–22.

Warnier, J. Logical Construction of Programs, Van Nostrand Reinhold, New York, NY, 1974.

Wolverton, R.W. "The Cost of Developing Large-Scale Software," IEEE Transactions on Computers (C-23:6), June 1974, pp. 615–636.

Wand, Y. and Weber, R. “An Ontological Analysis of Some Fundamental Information Systems Concepts,” Proceedings of the Ninth International Conference on Information Systems, Minneapolis, MN, December 1988, pp. 213–225.

Wrigley, C.D. and Dexter, A.S. "Software Development Estimation Models: A Review and Critique," Proceedings of the Administrative Sciences Association of Canada: MIS Division, Toronto, Ontario, June 1987, pp. 125–138.

Wrigley, C.D. and Dexter, A.S. "A Model for Estimating Information System Size: Preliminary Findings," Proceedings of the Ninth In-

ternational Conference on Information Systems, Minneapolis, MN, December 1988, pp. 245–255.

## About the Authors

Clive D. Wrigley is assistant professor of management information systems at the Faculty of Management at McGill University. He received his Ph.D. in management information systems from the University of British Columbia. He conducts research and consults in the areas of productivity, system modelling tools, and electronic data interchange.

Albert S. Dexter is associate professor of management information systems at the Faculty of Commerce and Business Administration at the University of British Columbia. He has served as national examiner in information and computer systems for the Certified General Accountants Association of Canada. He has also served as an expert witness for the Supreme Court of British Columbia on issues of accounting and economics. Currently he is involved in court cases concerning software copyright infringement. Professor Dexter's research has appeared in such journals as Communications of the ACM, Datamation, Human Computer Interaction, INFOR, MIS Quarterly, and Management Science. He has also published numerous books on information systems and systems analysis and is an associate editor for INFOR. His current research interests are in the analysis, design, evaluation, and implementation of information systems; the relationship between information technology and competitive advantage; and electronic data interchange.
