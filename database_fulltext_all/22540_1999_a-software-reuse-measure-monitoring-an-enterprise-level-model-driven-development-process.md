---
otero_id: 22540
otero_key: "S4SQE6FP"
title: "A software reuse measure: Monitoring an enterprise-level model driven development process"
authors: "Marcus A Rothenberger; James C Hershauer"
year: "1999"
journal: "Information & Management"
doi: "10.1016/s0378-7206(98)00095-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A software reuse measure: Monitoring an enterprise-level model driven development process

Marcus A. Rothenberger $^{a,*}$ , James C. Hershauer $^{b}$

$^{a}$ School of Accountancy and Information Management, Arizona State University, Tempe, AZ 85287-3606, USA $^{b}$ Department of Management, Arizona State University, Tempe, AZ 85287-4006, USA

Received 11 December 1997; accepted 27 September 1998

## Abstract

The purpose of the research discussed here is to establish a metric for the measurement of reuse in a generic enterprise-level model context and to use this approach to create a specific metric for a company. The paper demonstrates how a software development firm can monitor the reuse success in the development process using the measure. Traditionally, the reuse rate is defined as the percentage of the development effort retrieved as code segments from a software repository. The metric proposed here extends this definition to include reuse of generic enterprise-level model components. An example is given of the successful assessment of a reuse percentage for a software developer's actual project. © 1999 Elsevier Science B.V. All rights reserved.

Keywords: Software reusability; Enterprise-level model; Reuse rate; Software development

## 1. Introduction

Traditional software development methods are not able to produce high quality software quickly $[7]$ . System developers are therefore utilizing the concept of reuse of software in various ways, such as reusing code segments and algorithms as well as knowledge and ideas. However, traditional methods usually have been performed in an ad-hoc manner; systematic reuse requires building and maintaining a software repository containing code that has been developed to be used in several projects. This approach can increase productivity and quality in the software production process $[23]$ . However, developing reusable code components usually requires more effort than developing regular components. In traditional systems development, the goal is to meet user requirements and specifications without concern for any need to integrate the components into future systems. Recently, some organizations have been reconsidering this problem and are starting to develop their software with reusability in mind. Their motivation is a potential increase in the long-term efficiency of the software development process and increase in software quality.

Companies may make substantial initial investments to incorporate the creation of reusable code into their software development process and to maintain it in a software repository for use later. Naturally, a payoff through increased reuse is expected. Also, higher quality code will be produced in less time when much of it is reused – having been previously debugged [3, 4, 12, 17, 20]. However, it must also be realized that the initial cost of producing reusable software components may be much higher than that of regular components. To implement a systematic corporate reuse program, measurement is necessary [10], unfortunately few companies are measuring it [11]. To measure the level of reuse in software projects, we need to be able to assess a percentage reuse rate. The de facto standard is:

$$
\frac {\text { Reused Software }}{\text { Total Software }} \times 100 \%\tag{1}
$$

Companies investing in the implementation of a complex development paradigm for reuse need to be able to monitor its effectiveness. Measuring the reuse percentage allows companies to evaluate the success of their investment. Advanced development techniques, such as object-oriented methodologies and generic enterprise-level models, are facilitating reuse and are becoming more popular among software developers. [8, 22]. Basili et al. [6] have introduced a method of computing the reuse rate for an object-oriented software repository. While they address concerns unique to object-orientation, the question of how to deal with components reused as part of an enterprise-level model has not been explored. Such a measurement needs additional consideration.

## 1.1. Purpose

Our work hopes to find a way to determine a generic metric for the measurement of reuse in an enterprise-level model context and to use this approach to create a metric for a given company. Traditionally, the reuse rate is defined as the percentage of the development effort retrieved as code segments from a software repository and employed as components for a program, with the software repository containing previously written code. The metric proposed here extends this definition to include the reduced development effort through employment of a generic enterprise-level model. Improving software reuse is the major reason for implementing an enterprise-level model based development process. Hence, the assessment of the reuse rate for software projects allows a firm to monitor the success in providing a better development methodology.

## 1.2. A review of software metrics literature

In the field of software complexity measurement, various metrics have been introduced. The most common are McCabe's cyclomatic complexity [18], Albrecht's function points (FP) [2], Halstead's Software Science [13], and lines of code (LOC).

McCabe's approach employs parts of graph theory to assess the complexity of the program. The labor intensity of data gathering for function points and its low reliability because of the use of subjective data to estimate complexity have been criticized [21]. Halstead's method uses software science equations to determine the complexity of a program based on lexical counts of symbols. A common disadvantage of all three metrics is the relatively high cost of obtaining the number. Unless one of the metrics is already part of a company's regular techniques, the measure has to be determined through labor intensive efforts.

Because of the relatively high cost of alternative measures, the oldest metric, LOC, is still the most widely used. Although the quality of this metric has often been questioned, the fact that it is relatively inexpensive and easy to obtain makes many companies prefer this measure. The major criticisms of LOC are:

1. The LOC measure does not account for the relative complexity of each line. A very complex algorithm can be written in few lines of code (e.g., complex calculations, graphical output, etc.), while a less complex algorithm might be implemented using many LOC (e.g., textual output to the screen, easy calculations, etc.)

2. The LOC measure does not account for the effect of different programming languages (i.e., an algorithm of the same complexity will usually require more LOC in a COBOL implementation than a C implementation).

3. The LOC metric does not account for variations in programming style. Different usage of white space and lines of comment $[9, 24]$ in the source code will cause the measure to show different LOC counts for the implementation of two algorithms with the same complexity, because of differences in programming style.

In many situations, these concerns do not apply and LOC can be a meaningful measure. Some researchers even argue that LOC is as good as or a better measure for development effort than Halstead's or McCabe's [5]. However, these issues have to be addressed and resolved. For an overview and a more detailed discussion refer to Ref. [1].

## 1.3. Methods

For the present research we use data from MBA Technologies, a software development company that employs an enterprise-level model for some development projects. The study is a field study of the company's development environment, following the approach of comparable research [15, 25]. As some systems development companies are now doing, the participating developer has a generic integrated set of software components for use by potential customers. In the most extreme case, such an approach could mean that the client is implementing a generic system like SAP without any changes to or customization of the software [14].

One project of the firm was used as a case study: for this purpose, structured interviews were conducted with management and analysts. The primary criterion for the selection of the project was the quality of data available. Further interviews were conducted with the employees to explore the nature of reuse in an enterprise-level model based software development approach. These findings were incorporated into the development of the metric.

## 2. Enterprise-level model based software development

The code development of software in an enterprise-level model based context can be split into three structures: deep, middle, and surface. The deep structure is the enterprise-level model itself; it is used for all projects based on the model. Although additions and modifications to the model are possible, they are rather infrequent. In the deep structure, we have the highest reuse rate of the project. If no modifications to the model are made, the reuse rate is 100 percent. The middle structure consists of generic solutions to application areas. These solutions may be readily available in a software library; they may need modification or they may have to be totally written. We expect the greatest variation in reuse rate on this level. The surface structure contains high-level code and represents the part of the program that is unique to the project. It interacts with the middle and the deep structure to execute lower-level components. Because of the nature of the surface structure, the least amount of reuse is expected on this level.

## 3. The specific development environment

To illustrate the methodology and to show the value of the metric approach, we measured the reuse rate for the project of the software developer. Because of variations in enterprise-level model based development approaches across companies, the approach must be customized to the specific situation, although the underlying ideas are applicable to any enterprise-level model based environment.

## 3.1. The company

The participating company for this field study, MBA Technologies specializes in the development of business process and accounting systems using an enterprise-level model. This framework consists of a data model and reusable objects. For an actual development project, the customer's requirements are mapped to the objects of the existing model. Most of this is achieved by reusing components from the enterprise-level model, the deep structure. If the model does not satisfy the requirements, additions can be made to the enterprise-level model and become part of it for future projects. Each class of the enterprise-level model consists of a generic set of attributes and methods; only a fraction of these is needed for each project when the model is employed. The unwanted parts can be by-passed for compiling by setting the appropriate switches. Since the metric includes a size assessment of the source code, this could lead to unintended results. However, assuming that the percentage of code by-passed is about the same for all components of the enterprise-level model, the bypassed code in the deep structure will mathematically even out and the reuse ratio for the deep structure will be valid. A direct comparison of a size-employing-measure for the deep structure and the higher-level structure would be invalid, since the amount of code by-passed in the deep structure would change the results. Components of the middle structure can be reused by retrieving previously written code from a repository. Code reused in the middle structure is not part of the enterprise-level model. We would expect a medium amount of reuse at this level. The small amount of reuse expected in the surface structure is from the use of common access routines. In addition to writing code that ties into reusable components, the company also generates code for all three structural levels. Both hand-written and generated code are integrated into the projects.

## 3.2. The data

To measure the software reuse rate, we decided to use LOC. With these we are referring to the total number of lines without removing white space or comments. Since the decision for a development effort surrogate measure is partially based on the available data, we present it here. Each of the three structures consists of a set of components for which there is a total count available. This includes both hand-written and generated code. Each component is broken down into a set of vectors: the hand-coded parts of the components. For each vector there is also a LOC count available. Therefore, the sum of all vectors' LOC for one component is the hand-written LOC count for that component. The LOC count of the component minus the hand-written LOC count is the generated LOC count of that component. Vectors in the deep structure are a collection of code subpieces called sources. Information on the classification of each source into modified or reused is available; this helps to classify the corresponding vector into either group. The classification of vectors of the other two structures in reused or modified vectors is based on the assessment of the analyst involved in the project.

## 4. The software reuse rate metrics

According to Poulin [19], operating systems, high-level languages, and the use of development tools, such as compiler tools, are not considered reuse. Since we collect data on development hours and complexity of each component used, the number of times the component is used in the project is not relevant.

However, within each component, data is collected on each of the vectors. If vectors are used more than once across different components or across structures, the duplicate vectors must be eliminated from the measure. Since we are looking at the reuse rate of each structure, it does not matter which component used it. However, if the vector is used in more than one structure, it has to count towards the structure for which it was originally developed. The decision to count duplicate components only once agrees with the results of Poulin. Further, we do not count code generated software as reuse in the same way as hand-written code. A separate measure for code generated software reuse is reported.

## 4.1. Creating the measure

The reuse rate of the components are calculated using a method suggested by Basili et al. for the assessment of the degree of reuse in object-oriented code. They looked at program reuse in an object-oriented environment as part of a study to assess its impact on quality and productivity in object-oriented systems. We modified the method to apply it to a component framework rather than a strictly object-oriented class framework. They describe the size of a system S as a function $[Size(S)]$ with a series of properties. The following is a subset of these:

\- size cannot be negative,

\- size is expected to be zero when a system does not contain any component, and

\- when components do not have elements in common, size will be additive.

Reuse(S) is introduced as the amount of reuse in a system S, hence it is an instance of the size metric. Therefore, the three properties of $Size(S)$ also apply for $Reuse(S)$ . $Reuse(S)$ is subject to the following three cases:

1. Component C belongs to the reuse library and has been included in the system S without modifications:

$$
\operatorname{Reuse} (C) = \operatorname{Size} (C)
$$

2. Component C has been created by changing an existing component: Reuse can be estimated as: $\text{Reuse}(C) = (1 - \text{Change} \quad \%) \times \text{Size}(C)$ . Since % Change is difficult to obtain, Basili et al. suggest and justify the following simplification:

\- $C$ is more than $25\%$ modified: $\operatorname{Reuse}(C) = 0$

\- $C$ is less than $25\%$ modified: $\operatorname{Reuse}(C) = \operatorname{Size}(C)$

3. Component C was totally written:

$$
\operatorname{Reuse} (C) = 0
$$

Given this classification, the reuse rate of a system S is:

$$
\begin{array}{l} \text { ReuseRate } (S) = \sum \frac {\text { Reuse } (C)}{\text { Size } (S)} \text { where } \\ C \in \text { Components } (S) \end{array}\tag{2}
$$

If an existing component has been modified for the project we count it as reuse if the modifications are estimated to be less than 25 percent. Although the IEEE Standard for Software Productivity Metrics defines reuse as the number of source statements incorporated without modification into an application [16], we need to include modified components into the measure to account for the productivity gain through reuse of slightly modified components.

Basili et al. assume the existence of a size metric. We can substitute any of the previously discussed measures; they are good surrogate measures for the development effort. For the purpose of our subject company, we use lines-of-code (LOC) as a size measure. The problems with using LOC as a measure of development effort do not apply in the context of the enterprise-level based software development environment of our company. Thus, LOC is a suitable measure for the development effort because:

1. The code is written within the same subject domain. We are measuring reuse in the domain of business process and accounting systems. Similarity of the algorithm type insures that LOC is a good measure for the program complexity, since the average complexity per line of code remains constant across code of the same type.

2. All components are written in the same programming language. The problem that LOC does not adjust for differences in programming languages does not apply to our company.

3. The ratio of Comment LOC/Non-Comment LOC (CLOC/NLOC) and the amount of white space used is constant among the vectors. The software development company follows a rigid methodology. This suggests consistent programming style, including use of comments and white space. This presumption has been confirmed by sampling the code of the project. Hence, the concern that LOC does not adjust for different programming style does not apply to our example.

LOC has an advantage over many more complicated metrics, because it is easy and inexpensive to determine.

## 4.2. Application of the measure to a specific problem

Each of the three structures (surface, middle, and deep) contains a number of components. Each component consists of generated and hand-coded subcomponents. The latter are referred to as vectors. For each component, the total LOC (including generated and hand-written code) is available, as well as the LOC for each hand-written vector. Two reuse rates are calculated for each structure: for the generated, and hand-written code.

To determine the hand-written code reuse rate, an assessment is made for each vector whether it was reused or written for the project. Vectors modified more than 25 percent are considered totally written, while vectors modified less than 25 percent are considered completely reused. To make this assessment, each of the three structures must be examined separately. Structured interviews with the analyst led to the decision for each vector.

In the surface structure, all vectors are fully (newly) written with only one exception. A frequently used data access routine is reused with no modification. All vectors, except the access routine, are categorized as non-reused. In the middle structure, the assessments are made using information recorded on the time sheets during program development, as well as the input of the analyst. Middle structure vectors are classified into two groups: vectors totally written and vectors retrieved from the repository. Vectors newly written are categorized as non-reused. The deep structure is the enterprise-level model itself. All vectors are reused except the ones that are additions to the models or modified more than 25 percent. For the project under consideration, few vector additions are made. The question of which vectors are modified more than 25 percent is answered by analyzing the vector code sub-pieces which we call sources. Changes to deep-structure vectors take place in the form of additions to the sources. If the new sources of any vector account for more than 25 percent of the total sources, the vector is classified as non-reused.

Vectors that appear more than once in any of the structures are counted only in one place. Those vectors are counted towards the LOC of the structure for which they were originally programmed. This applies to both reused and non-reused vectors. Hence, for each of the three structures, the following calculations apply:

the assessment for each component. Making the 25 percent assessment for each component results in a lower granularity of the generated code reuse rate than for the hand-written code reuse rate where we made the assessment for each vector. In the surface structure, all components are generated and therefore are classified as non-reused. In the middle structure, some of the components are newly developed for the project, while some of the components are retrieved from the

$$
\text { ReuseRate } _ {\text { Hand   -   Written   -   Code }} = \frac {\text { TotalReusedLOC } _ {\text { Hand   -   Written }}}{\text { TotalLOC } _ {\text { Hand   -   Written }}}\tag{3}
$$

where

$$
\text { Total } \text { ReusedLOC } _ {\text { Hand - Written }} = \sum_ {v \in \text { ReusedVectors }} L O C (v) - \sum_ {d \in \text { DuplicateReusedVectors }} L O C (d)
$$

and

$$
\text { TotalLOC } _ {\text { Hand - Written }} = \sum_ {v \in \text { Vectors }} L O C (v) - \sum_ {d \in \text { Duplicate   Vectors }} L O C (d)
$$

While the formula of the ReuseRate $_{\text{Hand-Written-Code}}$ applies to any development environment, the formulas for $TotalReusedLOC_{Hand-Written}$ and $TotalLOC_{Hand-Written}$ are adjusted to the subject company's environment and available data.

In the software development environment of MBA Technologies, the vectors consist only of hand-written code. Generated code is included, together with the hand-written code of the vectors, in the total LOC count for each component. Therefore, we must make repository. For the components from the repository, individual assessments of modification extent are made by the analyst. In the deep structure or enterprise-level model, components are reused unless they are added to the model. Since none were added for this project, all components were classified as reused. The reuse rate for generated code is then calculated. The first formula applies to any company, while the other two are adjusted to the particular development environment:

$$
\text { ReuseRate } _ {\text { Generated - Code }} = \frac {\text { TotalReusedLOC } _ {\text { Generated }}}{\text { TotalLOC } _ {\text { Generated }}}\tag{4}
$$

where

$$
\text { TotalReusedLOC } _ {\text { Generated }} = \sum_ {c \in \text { Reused   Components }} \left(\text { LOC } (c) - \sum_ {v \in \text { Vectors } (c)} \text { LOC } (v)\right)
$$

$$
\text { TotalLOC } _ {\text { Generated }} = \sum_ {c \in \text { Components }} \left(\text { LOC } (c) - \sum_ {v \in \text { Vectors } (c)} \text { LOC } (v)\right)
$$

Table 1
Project reuse rate

<table><tr><td></td><td>Reuse rate coded</td><td>LOC coded</td><td>Estimation % code bypassed</td><td>Adjusted LOC coded</td><td>Reuse rate generated</td><td>LOC generated</td></tr><tr><td>Surface structure</td><td>0.4%</td><td>18,701</td><td>0.0%</td><td>18,701</td><td>0.0%</td><td>391,603</td></tr><tr><td>Middle structure</td><td>57.0%</td><td>28,970</td><td>10.0%</td><td>26,073</td><td>56.4%</td><td>459,377</td></tr><tr><td>Deep structure</td><td>95.9%</td><td>82,196</td><td>35.0%</td><td>53,427</td><td>100.0%</td><td>447,324</td></tr><tr><td>Total</td><td>67.4%</td><td>129,867</td><td></td><td>98,201</td><td>54.4%</td><td>1,298,304</td></tr></table>

## 5. Example case data

The software reuse rate was established for the example case data. The results of the calculations are shown in Table 1. The spreadsheets containing the results of the calculations for each structural level are provided in Appendix B. The spreadsheets calculating those results from the set of vectors are not included for space considerations. They are available from the authors upon request.

The software reuse rates are reported for each of the three structures. Within each the reuse rate for handwritten and generated code are reported separately. The reuse rate for generated code has to be interpreted differently from the reuse rate for hand-written code. While code generation, by itself, already represents a productivity gain over coding by hand, it still requires effort to use the generator to create code. Therefore, the maximization of reuse for generated code is an additional gain in productivity. The reuse of previously generated code requires substantially less effort than the generation of new code.

The enterprise-level model allows the programmer to bypass hand-written code that is part of the generic model but not needed for the current version of the project. The portion of by-passed hand-written code varies across the three structural levels, but is consistent within each of the structures. Therefore, the bypassed code does not affect the validity of the reuse rate for hand-written code for each of the three levels. However, in order to calculate a total reuse rate, we have to weight the reuse percentage for each structure by the LOC of each structure. For the total reuse rate for generated code, this will produce a valid result, because generated code cannot be by-passed according to the company's development environment. For the calculation of the total reuse rate for hand-written code, we have to make adjustments for the by-passed code. Weighting the three percentages by the LOC counted would overemphasize the reuse percentages of the structural levels with a high portion of by-passed code, since by-passed code is included in the LOC count available. To implement such an adjustment we obtained estimates for the percentage of code bypassed in each level of the project, based on interviews with the analysts. The adjusted LOC count is the original count reduced by the percentage of by-passed code. The adjusted counts are used to weigh each of the three percentages in order to obtain a total reuse rate for hand-written code.

It has to be noted that the three individual reuse percentages are a better measure than the total, since the latter is based on an additional estimate. Therefore, we advise using the individual figures for the analysis of trends in reuse percentages across projects.

Although we are excluding by-passed code from the measure, its existence in a project will simplify changes and updates of the software in the future. Modifications in the behavior of the software can potentially be implemented by just resetting a series of bypass switches, assuming that the new behavior is available as by-passed code in the project. While the by-passed reused code will not contribute to the reuse percentage total, it will contribute to the software being more flexible and easier to change.

## 6. Conclusion

Our approach to a metric was developed to assess the software reuse rate for projects in enterprise-level model software development frameworks:

1. We propose that lines of code (LOC) can be a valid measure for development effort in an enterprise-level model based development environment.

2. The reuse rate should be reported and evaluated separately for each of the three levels in an enterprise-level model based development project (deep, middle, and surface).

3. Within each structure, the reuse rate for hand-coded and generated code should be reported and considered separately.

4. In establishing the reuse rate, each structure should be broken down into the smallest possible modules: each module should be classified into whether it has been modified more or less than 25 percent. Depending on this assessment, each module will be classified as reused (less than 25 percent) or non-reused.

5. Duplicate modules have to be eliminated from the measure.

This approach can be applied to any enterprise-level model based software development environment. A concrete application of the method, however, will vary with the development environment and available data of the software project for which the reuse rate has to be established. To show the feasibility of this approach, a metric has been created for a development project of a real company and the reuse rate has been calculated.

The need to customize the method to the exact nature of the enterprise-level model is one weakness of this approach. However, since enterprise-level models vary across software development companies, a common mathematical formula for all variations of enterprise-level models does not seem possible. The method provides the means to eliminate duplicate usage of code down to the module level, where modules are the smallest separately reported code packages. Code that has been utilized in several places in the project, within or across modules by copying the same lines of source code to different locations, cannot be identified as duplicate code. Therefore, it will count multiple times to the measure. This weakness cannot be eliminated easily, since copying previously written code to several locations in the source code is common programming practice. In a sound development environment we would expect this type of multiple use of code to be negligible, since programmers have the option of using the modules as a whole in several places.

The accuracy of the reuse measure can be maximized by breaking down the project into as many separately measured modules as possible which will be classified either as reused or non-reused. The ability to break down the project into a large number of very small modules is in practice limited to the size of the modules for which separate size measures have been recorded.

With the metric, the success of using an enterprise-level model to achieve reuse in software development can be monitored. In a successful development process, the improvement of the enterprise-level model would lead to an improvement of the average reuse percentage of the projects.

## Acknowledgements

The authors thank Dan O'Neill, Richard Solar, and Gary Hall of MBA Technologies, Phoenix, Arizona, for providing the field setting for this research, for giving access to analysts and resources, and for supplying the data for the example.

## Appendix A

## A.1 Lines of code (LOC)

Lines of code (LOC) is the count of total lines of code including white space and lines of comments.

## A.2 Generated code

Generated code is code that has been created using code generator software.

## A.3 Hand-written code

Hand-written code is code that has been developed and written by a team of developers without the use of code generators.

## A.4 Component

Components are software modules. Each structural level consists of a number of components. The LOC count available for components includes both handwritten and generated code.

Table 2  
Surface structure summary

<table><tr><td>Component</td><td>Total LOC(coded + generated)</td><td>Coded LOCincl. repeated vectors</td><td>Non-reused coded LOC</td><td>Reused coded LOC</td><td>Generated LOC</td><td>More than 25% modified?</td><td>Reused generated LOC</td></tr><tr><td>BIVR16</td><td>12,158</td><td>352</td><td>352</td><td>0</td><td>11,806</td><td>yes</td><td>0</td></tr><tr><td>BIVR19</td><td>13,323</td><td>966</td><td>966</td><td>0</td><td>12,357</td><td>yes</td><td>0</td></tr><tr><td>BIVU09</td><td>19,342</td><td>886</td><td>886</td><td>0</td><td>18,456</td><td>yes</td><td>0</td></tr><tr><td>BIVU11</td><td>12,770</td><td>171</td><td>171</td><td>0</td><td>12,599</td><td>yes</td><td>0</td></tr><tr><td>BIVU20</td><td>26,386</td><td>2,397</td><td>2,397</td><td>0</td><td>23,989</td><td>yes</td><td>0</td></tr><tr><td>IV01</td><td>79,735</td><td>4,878</td><td>4,801</td><td>77</td><td>74,857</td><td>yes</td><td>0</td></tr><tr><td>IV02</td><td>56,924</td><td>3,442</td><td>3,365</td><td>0</td><td>53,482</td><td>yes</td><td>0</td></tr><tr><td>IV03</td><td>45,675</td><td>2,840</td><td>2,763</td><td>0</td><td>42,835</td><td>yes</td><td>0</td></tr><tr><td>IV04</td><td>28,109</td><td>853</td><td>776</td><td>0</td><td>27,256</td><td>yes</td><td>0</td></tr><tr><td>IV05</td><td>17,883</td><td>500</td><td>423</td><td>0</td><td>17,383</td><td>yes</td><td>0</td></tr><tr><td>IV06</td><td>38,972</td><td>546</td><td>469</td><td>0</td><td>38,426</td><td>yes</td><td>0</td></tr><tr><td>IV07</td><td>59,489</td><td>1,332</td><td>1,255</td><td>0</td><td>58,157</td><td>yes</td><td>0</td></tr><tr><td>TOTAL</td><td>410,766</td><td>19,163</td><td>18,624</td><td>77</td><td>391,603</td><td></td><td>0</td></tr><tr><td></td><td colspan="7">Reuse Rate</td></tr><tr><td>Coded</td><td colspan="7">0.4%</td></tr><tr><td>Generated</td><td colspan="7">0.0%</td></tr></table>

Table 3  
Middle structure summary

<table><tr><td>Component</td><td>Total LOC(coded + generated</td><td>Coded LOCincl. repeated vectors</td><td>Non-reused coded LOC</td><td>Reused coded LOC</td><td>Generated LOC</td><td>More than 25% modified?</td><td>Reused generated LOC</td></tr><tr><td>aqr01</td><td>19,281</td><td>1,913</td><td>0</td><td>1,913</td><td>17,368</td><td>no</td><td>17,368</td></tr><tr><td>OEPR</td><td>73,725</td><td>4,091</td><td>0</td><td>4,091</td><td>69,634</td><td>no</td><td>69,634</td></tr><tr><td>SSPU02</td><td>13,570</td><td>1,025</td><td>0</td><td>1,025</td><td>12,545</td><td>no</td><td>12,545</td></tr><tr><td>SSSM0</td><td>56,297</td><td>3,518</td><td>0</td><td>3,518</td><td>52,779</td><td>no</td><td>52,779</td></tr><tr><td>SIVR17</td><td>15,735</td><td>552</td><td>552</td><td>0</td><td>15,183</td><td>yes</td><td>0</td></tr><tr><td>SIVR18</td><td>28,814</td><td>5,151</td><td>5,151</td><td>0</td><td>23,663</td><td>yes</td><td>0</td></tr><tr><td>SIVU01</td><td>22,462</td><td>2,050</td><td>2,050</td><td>0</td><td>20,412</td><td>yes</td><td>0</td></tr><tr><td>SIVU02</td><td>24,975</td><td>716</td><td>716</td><td>0</td><td>24,259</td><td>yes</td><td>0</td></tr><tr><td>SIVU03</td><td>31,706</td><td>978</td><td>978</td><td>0</td><td>30,728</td><td>yes</td><td>0</td></tr><tr><td>SIVU04</td><td>11,894</td><td>260</td><td>260</td><td>0</td><td>11,634</td><td>yes</td><td>0</td></tr><tr><td>SIVU05</td><td>9,096</td><td>351</td><td>351</td><td>0</td><td>8,745</td><td>yes</td><td>0</td></tr><tr><td>SIVU06</td><td>20,927</td><td>611</td><td>611</td><td>0</td><td>20,316</td><td>yes</td><td>0</td></tr><tr><td>SIVU07</td><td>15,521</td><td>346</td><td>346</td><td>0</td><td>15,175</td><td>yes</td><td>0</td></tr><tr><td>SIVU08</td><td>4,365</td><td>324</td><td>324</td><td>0</td><td>4,041</td><td>yes</td><td>0</td></tr><tr><td>SIVU10</td><td>27,294</td><td>1,132</td><td>1,132</td><td>0</td><td>26,162</td><td>yes</td><td>0</td></tr><tr><td>SSMNTR</td><td>43,310</td><td>3,929</td><td>0</td><td>3,929</td><td>39,381</td><td>no</td><td>39,381</td></tr><tr><td>SH32</td><td>69,375</td><td>2,023</td><td>0</td><td>2,023</td><td>67,352</td><td>no</td><td>67,352</td></tr><tr><td>Total</td><td>488,347</td><td>28,970</td><td>12,471</td><td>16,499</td><td>459,377</td><td></td><td>259,059</td></tr><tr><td></td><td colspan="7">Reuse rate</td></tr><tr><td>Coded</td><td colspan="7">57.0%</td></tr><tr><td>Generated</td><td colspan="7">56.4%</td></tr></table>

Table 4  
Deep structure summary

<table><tr><td>Component</td><td>Total LOC(coded + generated)</td><td>Coded LOCincl. repeated vectors</td><td>Non-reused coded LOC</td><td>Reused coded LOC</td><td>Generated LOC</td><td>More than 25% modified?</td><td>Reused generated LOC</td></tr><tr><td>SUOM</td><td>2,275</td><td>260</td><td>0</td><td>260</td><td>2,015</td><td>no</td><td>2,015</td></tr><tr><td>AMSBLF</td><td>2,293</td><td>706</td><td>0</td><td>706</td><td>1,587</td><td>no</td><td>1,587</td></tr><tr><td>DL50</td><td>41,114</td><td>10,717</td><td>815</td><td>9,875</td><td>30,397</td><td>no</td><td>30,397</td></tr><tr><td>SS50</td><td>69,578</td><td>17,308</td><td>2,517</td><td>14,551</td><td>52,270</td><td>no</td><td>52,270</td></tr><tr><td>NV50</td><td>32,861</td><td>5,031</td><td>0</td><td>4,954</td><td>27,830</td><td>no</td><td>27,830</td></tr><tr><td>TX50</td><td>10,982</td><td>1,352</td><td>0</td><td>1,103</td><td>9,630</td><td>no</td><td>9,630</td></tr><tr><td>PR90</td><td>17,550</td><td>1,571</td><td>0</td><td>1,571</td><td>15,979</td><td>no</td><td>15,979</td></tr><tr><td>PL75</td><td>1,209</td><td>45</td><td>0</td><td>45</td><td>1,164</td><td>no</td><td>1,164</td></tr><tr><td>DE60</td><td>37,733</td><td>0</td><td>0</td><td>0</td><td>37,733</td><td>no</td><td>37,733</td></tr><tr><td>AQ54</td><td>37,733</td><td>461</td><td>0</td><td>317</td><td>37,272</td><td>no</td><td>37,272</td></tr><tr><td>JB40</td><td>109,241</td><td>15,212</td><td>0</td><td>15,135</td><td>94,029</td><td>no</td><td>94,029</td></tr><tr><td>OEPR</td><td>14,973</td><td>0</td><td>0</td><td>0</td><td>14,973</td><td>no</td><td>14,973</td></tr><tr><td>ER50</td><td>4,872</td><td>291</td><td>0</td><td>291</td><td>4,581</td><td>no</td><td>4,581</td></tr><tr><td>SR50</td><td>10,086</td><td>1,148</td><td>0</td><td>899</td><td>8,938</td><td>no</td><td>8,938</td></tr><tr><td>DE50</td><td>115,951</td><td>29,157</td><td>0</td><td>29,157</td><td>86,794</td><td>no</td><td>86,794</td></tr><tr><td>SH50</td><td>22,381</td><td>249</td><td>0</td><td>0</td><td>22,132</td><td>no</td><td>22,132</td></tr><tr><td>Total</td><td>530,832</td><td>83,508</td><td>3,332</td><td>78,864</td><td>447,324</td><td></td><td>447,324</td></tr><tr><td></td><td colspan="7">Reuse rate</td></tr><tr><td>Coded</td><td colspan="7">95.9%</td></tr><tr><td>Generated</td><td colspan="7">100.0%</td></tr></table>

## A.5 Vector

Vectors are the hand-coded parts of components. Each component consists of several vectors. For each vector there is a LOC count available.

## A.6 Enterprise-level model

The enterprise-level model is a framework of software components implementing generic business solutions which can be mapped to the specifications for concrete business systems.

## A.7 Structural levels

Structural levels are a classification for code developed in an enterprise-level model software environment. It is a classification into three structural levels: deep structure, middle structure, and surface structure. The deep structure is the code that is part of the enterprise-level model itself. The middle structure consists of higher-level code for generic solutions to application areas. The surface structure represents the highest-level code making use of the two levels below.

## Appendix B

B.1 Surface structure summary (Table 2)

B.2 Middle structure summary (Table 3)

B.3 Deep structure summary (Table 4)

## References

[1] R. Adamov, P. Baumann, Literature Review on Software Metrics, Angewandte Informations Technik, 1989.

[2] A. Albrecht, J. Gaffney, Software function, Source lines of code, and development effort prediction: a software science validation, IEEE Transactions on Software Engineering 9(6), 1983, pp. 639–648.

[3] U. Apte, C.S. Sankar, M. Thakur, J.E. Turner, Reusability-based strategy for development of information systems: implementation experience of a bank, MIS Quarterly 14(4), 1990, pp. 420–433.

[4] B.H. Barnes, T.B. Bollinger, Making reuse cost-effective, IEEE Software 8(1), 1991, pp. 13–24.

[5] V.R. Basili, Qualitative Software Complexity Models: A Summary, Tutorial on Models and Methods for Software Management and Engineering, IEEE Computer Society Press, Los Alamitos, CA, 1980.

[6] V.R. Basili, L.C. Briand, W.L. Melo, How reuse influences productivity in object-oriented systems, Communications of the ACM 39(10), 1996, pp. 104–116.

[7] A.W. Brown, Integrated project support environments, Information and Management 15(3), 1988, pp. 125–134.

[8] B.J. Cox, Planning the software industrial revolution, IEEE Software 7(6), 1990, pp. 25–33.

[9] W. Evangelist, Software complexity metric sensitivity to program structuring rules, Journal of Systems and Software 3(3), 1983, pp. 231–243.

[10] W. Frakes, C. Terry, Software Reuse: Metrics and Models, ACM Computing Surveys, 28(2) 1996.

[11] W.B. Frakes, C.J. Fox, Sixteen Questions About Software Reuse, Communications of the ACM, 38(6) 1995.

[12] J.E. Gaffney, Jr., T.A. Durek, Software reuse – key to enhanced productivity: some quantitative models, Information and Software Technology 31(5), 1989, pp. 258–267.

[13] M.H. Halstead, Elements of Software Science, Elsevier North-Holland, Inc., 1977.

[14] J. Hershauer, Manufacturing Strategy in the Global Software Industry: Make, Customize, Assemble, or Gather, 3rd International Conference of the European Operations Management Association, London Business School, London, 1996, pp. 299–302.

[15] J. Hershauer, A. Karim, H. Owens, A. Philippakis, A field observation study of an expert system prototype development, Information and Management 17(2), 1989, pp. 107–116.

[16] IEEE, Standard for Software Productivity Metrics, IEEE Standard #1045-1992, IEEE Computer Society Press, New York, 1992.

[17] C.W. Krueger, Software Reuse, ACM Computing Surveys, 24(2), 1992.

[18] T.J. McCabe, A Complexity Measure, IEEE Transactions on Software Engineering, 2(4) (1976) 308–320.

[19] J.S. Poulin, Measuring Software Reuse – Principles, Practices, and Economic Models, Addison-Wesley Pub. Co., Reading, Mass., 1997.

[20] J.S. Poulin, J.M. Caruso, D.R. Hancock, The business case for software reuse, IBM Systems Journal 32(4), 1993, pp. 567–594.

[21] R.S. Pressman, Software Engineering: A Practitioner's Approach, McGraw-Hill, 1987.

[22] G. Sindre, R. Conradi, E.-A. Karlsson, The REBOOT approach to software reuse, Journal of Systems Software 30, 1995, pp. 201–212.

[23] M.E. Swanson, S.K. Curry, Results of an asset engineering program, Information and Management 16(4), 1989, pp. 207–216.

[24] E.J. Weyuker, Evaluating software complexity measures, IEEE Transactions on Software Engineering 14(9), 1988, pp. 1357–1365.

[25] M.H. Zack, Electronic messaging and communication effectiveness in an ongoing work group, Information and Management 26(4), 1994, pp. 231–241.

![](/api/attachments/S4SQE6FP/fulltext/images/a302f7fbda57425516762122c8812925b6c112de1f79e871b939562ee4844b91.jpg)

Marcus A. Rothenberger is a doctoral candidate in Computer Information Systems at the School of Accountancy and Information Management at Arizona State University. He holds an MBA from Arizona State University and he received his undergraduate education in Computer Science and Business from the Technical University of Darmstadt in Germany. Previously he worked for Deutsche Bank AG in the Information

Engineering area. His dissertation research is on software reusability. Other research interests include information systems development, performance measurement, software engineering, and database systems. He presented several papers at the AIS, DSI, and ICIS conferences.

![](/api/attachments/S4SQE6FP/fulltext/images/1294803b7c0a17dc1bf6b9ae54dcf9485167811a7e907a66f422d8c73a59f13b.jpg)

James C. Hershauer is a Professor of Management at Arizona State University. He holds a B.S. in Engineering from Purdue University and an M.B.A. and D.B.A. in Production Management from Indiana University. He has published articles in operations management and information systems on many topics including productivity, quality, environmental management, systems development processes, and information

search strategies in journals such as Management Science, Decision Sciences, International Journal of Production Research, OM Review, Quality Progress, Interfaces, Computers & Industrial Engineering, Information & Management, Public Productivity Review, and International Journal of Purchasing & Materials Management. He is also co-author of three research monographs on productivity and quality. He was the Editor of Decision Sciences from 1990 through 1992 and was awarded a Fellows Citation in the Decision Sciences Institute in 1993.
