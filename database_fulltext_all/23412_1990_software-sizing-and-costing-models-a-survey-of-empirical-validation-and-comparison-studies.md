---
otero_id: 23412
otero_key: "RJB44DPF"
title: "Software sizing and costing models: a survey of empirical validation and comparison studies"
authors: "Graham Tate; June M Verner"
year: "1990"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1990.4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Software sizing and costing models: a survey of empirical validation and comparison studies

GRAHAM TATE and JUNE M. VERNER

School of Information Sciences, Massey University, New Zealand

Abstract: Effective software cost and size estimation is essential for planning and resource allocation in software development. Recent empirical work which attempts to validate, or which compares, software size and cost estimation models and tools is surveyed. Some observations are made concerning the rather poor results frequently obtained and the need for calibration of models for specific development environments.

## Introduction

The accurate estimation of software size, cost and schedule is important for planning software development and for efficient allocation of resources. Software size is important primarily because it is the most influential single input variable to most cost estimation models. Cost estimation normally involves the prediction both of development effort and of development duration, or schedule. Development schedule is important for two reasons. Firstly, early delivery of operational software can often result in competitive advantage, whereas late delivery can mean lost opportunity; thus opportunity costs are involved. Secondly, the distribution of effort in different skill categories over the various software development phases is essential to planning. There are many models and tools on the market which are designed to assist estimators in performing these estimation tasks. A significant body of research has been concerned with the empirical validation and comparison of some of these models and their associated tools. It is the purpose of this paper to review the results of this empirical research.

It is perhaps most appropriate to begin this survey by stating what it is not about. It is not a survey of sizing and costing estimation methods themselves. There are a number of recent surveys of sizing and costing methods, including: IIT Research Institute (1987, 1987a, 1989), and MERMAID Deliverable D1.2C, (1989), in addition to surveys of earlier work in Boehm (1981) and Mohanty (1981). There are also several other rather more accessible papers on related topics which include survey or review material on software sizing and costing methods, including Boehm (1984) and Kemerer (1987). Nor is this a study of the original empirical basis of well-known existing models, such as COCOMO (Boehm, 1981), SLIM (Putnam, 1978) or Function Point Analysis (FPA) (Albrecht, 1979). It is assumed that the reader has a basic knowledge of the fields of software sizing and costing.

Given this basis, the empirical/comparative part of the survey is concerned with recent studies which:

(a) use data from actual software development projects to validate or calibrate existing models, or to adapt them to specific environments;

(b) compare estimates from two or more software sizing or costing models with each other and with actual results from completed software projects;

(c) compare estimates made using hypothetical project data;

(d) analyze a significant body of new empirical software size, cost, schedule, productivity or related project data.

In several cases, recent comparative studies have resulted in new estimation models being proposed and compared to existing models using the data on which the new models have been based and calibrated. Most comparisons of this type are not, strictly speaking, fair. Indeed it is unlikely that any comparisons are fair unless all models compared have been calibrated to the comparison environment (where calibration is possible) and all of the estimators are equally experienced with all of the tools/models. Several such studies have been included nevertheless, with brief explanatory notes.

The survey looks first at sizing, reviewing the very few available empirical sizing studies. This is followed by a survey of empirical costing studies. Some observations on these empirical studies are contained

in the final section.

## Model evaluation and comparison criteria

There are two major concerns in the evaluation of sizing, costing and scheduling models, namely accuracy and consistency. Accuracy has been the traditional criterion for model evaluation, but recently researchers at IIT Research Institute (1989) have introduced the important concept of consistency, which they have used in their latest study.

Accuracy in this context is most commonly measured by either or both of MMRE or PRED(level). MRE is the magnitude of the relative error and is frequently just called 'the error' in this paper. The MRE for an estimate is obtained by dividing the absolute value of the difference between the estimate and the actual by the (positive) actual. MMRE is the mean magnitude of a set of relative errors; it will frequently be more simply called 'the average error'. PRED(level) is best explained via an example. In reference to a set of estimates made using a particular model, PRED (.25) = 75% means that 75% of those estimates are within 25% of actual.

Consistency, as defined in the IIT Research Institute report (1989), is explained in terms of effort estimates. An adjustment for systematic bias is made as follows. For each estimate, the percentage of actual to estimate (i.e. the reciprocal of estimate to actual) is calculated. The highest and lowest resulting percentages are discarded 'to achieve a truer sampling of percentages'. A mean value of the remaining percentages is computed and applied to all of the given model's effort estimates. The relative error for each project is recalculated using the adjusted efforts. The resulting 'unbiased' estimates can then be evaluated in the normal way using MMRE and PRED, those with the best MMRE and PRED values being the most consistent.

## Empirical studies of sizing models

Before considering the empirical sizing studies themselves, it is appropriate to explain several key sizing model concepts since these sizing model concepts are not generally as widely known as the costing model concepts are. There are two basic approaches to measuring and estimating software size. One aims to measure or estimate quantity of code (usually source code), the other to measure (albeit indirectly) quantity of software function. The units in the first case are typically KSLOC (thousands of source lines of code) or KDSI (thousands of delivered source instructions). The units in the second case are typically function points (Albrecht, 1979; Albrecht and Gaffney, 1983), which represent a functionality rating based on identifying the input/output characteristics of individual transactions and calculating a more or less complex function of the numbers of input data elements, output data elements and files involved. Function points can often be estimated from detailed system specifications. It is quite common for function points to be converted into SLOC for a specific programming language using observed average ratios of lines of code per function point for that language. For example, 105 SLOC/FP is a commonly used ratio for COBOL.

We have been able to find only four reported empirical studies of size estimation methods, which are comparisons between different size estimation approaches. These are the DACS report (IIT Research Institute, 1987) concerned with a wide range of sizing methods and models, studies by Verner and Tate (1989) and Verner (1989), concerned with three models based on function points, and a recent paper by Low and Jeffery (1990) which is concerned with a priori estimates of system size in function points and source lines of code. Both the DACS report and the Verner study contain classifications of size estimation models.

Research work in comparative size estimation normally uses lines of code to measure the size of the actual software produced. This is the only practical way that one can test the accuracy of a size estimate against the finished product. Synthetic metrics such as function points (Albrecht, 1979; Zwanzig, 1984), feature points (IIT Research Institute, 1987; Jones, 1989), Mark II function points (Symons, 1988), and Bang (recently renamed function weight) (DeMarco, 1984, 1989) can only ever be estimated, even after completion of a project. They cannot be objectively and unequivocally counted. In spite of extensive sets of counting rules and guidelines, particularly in the case of FPA, their computation involves more or less subjectivity and different people can obtain different counts for the same system (Low and Jeffery, 1990). Thus the validation of function point estimates poses considerable problems. Objective comparisons are hence best done using LOC, which can actually be counted, often automatically, despite some definitional difficulties (Jones, 1986).

## IIT Research Institute's DACS Report, 1987

The major work in the comparison of software size estimation methods and models is this 1987 report which was produced for the US Air Force Cost Centre by the IIT Research Institute's Data and Analysis Center for Software (DACS). This report discusses 14 approaches/packages for software size estimation and classifies them by the general approach they use. However only six automated models were used in the comparative test. The IITRI study itself is the only reference that can be given for models or approaches for which specific references are not given here. The approaches discussed in the report are shown below within the DACS general classification scheme.

Sizing by analogy: relates the proposed system to previously developed modules and systems of similar function and environmental requirements through a database of completed projects. ESD sizing package, Software Sizing Analyzer (SSA) and QSM Size Planner-Fuzzy Logic (Putnam, 1987) were included in this group.

Size-in-size-out: purely statistical approaches that require approximate size estimates based on expert judgement as input. Wideband Delphi technique (Boehm, 1981), Software Sizing Method (SSM) (Bozoki, 1986, 1987), curve fitting and PERT (Putnam, 1978, 1979) were included in this group.

Function Point Analysis: SPQR SIZER/FP and feature points are based on Albrecht's original work on function points (Albrecht, 1979), while ASSET-R (Reifer, 1989), and Before You Leap (BYL) (Gordon, 1987) are based on Albrecht's later work (Albrecht and Gaffney, 1983).

Comparison of project attributes: requires a data base of completed projects with which to relate the new development. Computer Economics Inc. Sizer (CEIS), and QSM Size Planner-Standard Components Sizing (Putnam, 1987) were placed in this group.

Linguistic approach: approaches that count the lexical symbols used in the programmatic expression of an algorithm. ASSET-R (Reifer, 1989), and state machines model (Britcher and Gaffney, 1985) were placed in this group. Note that ASSET-R is included in two of the above classes.

Other: Price SZ (Rapp, 1985; Otte 1986) could not be explicitly related to any of the above classes so was included here.

The following were the models used in the tests carried out: ESD, BYL, SPQR SIZER/FP, SSM, ASSET-R and PRICE SZ.

A small military system (9,177 lines of Fortran code), which had already been completed, was used as a basis for comparison. The inputs required for the models under test were defined by people who did not develop the original software. These people were experienced software development personnel who were furnished with complete specifications of the system.

Table 1 lists the models used and summarizes the results obtained in the DACS research.

The DACS report addressed a number of other issues in its comparative study, including user interfaces, hardware requirements, availability of the various models and their costs, the underlying methods of the various models and their usability.

The DACS report conclusions were as follows:

\- Software size estimation approaches based on analogy are the easiest to apply because they require few inputs and minimal training.

\- The function point approaches require the least experience in the application area to be effective.

\- Asset-R, CEIS, Price-SZ, QSM Fuzzy logic, QSM Standard Components Sizing and SSM are applicable in virtually all user environments.

\- Analogy approaches which use a database of previous projects are restricted to projects in the size range present in the database.

\- BYL, QSM and SPQR function point approaches have not been validated for scientific or real time systems.

\- ASSET-R and QSM Size Planner were the most sophisticated models in terms of their outputs.

\- BYL and ASSET-R were the most user-friendly.

\- The analogy approaches, plus CEIS and SSM, can be applied earliest in the lifecycle.

\- ASSET-R and SSM provided the most accurate size estimates in the test case study.

Table 1. DACS Report comparison summary

<table><tr><td>Model</td><td>ESD</td><td>SSM</td><td>BYL</td><td>Sizer/FP</td><td>Asset-R*</td><td>Price SZ</td></tr><tr><td>Est. size</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>KLOC</td><td>37.6</td><td>11.7</td><td>22.4</td><td>35.9</td><td>6.6,11.9</td><td>21.4</td></tr><tr><td>Function points</td><td>-</td><td>-</td><td>251</td><td>311</td><td>65</td><td>-</td></tr><tr><td>Adjusted FPs</td><td>-</td><td>-</td><td>213</td><td>342</td><td>-</td><td>-</td></tr><tr><td>Relative error %</td><td>310</td><td>27</td><td>144</td><td>291</td><td>-28,30</td><td>133</td></tr></table>

\* Two estimates are given for Asset-R, depending on whether number of algorithms or normalized operator/operand counts are used. The information in the DACS Report was insufficient for adjusted function points to be calculated for Asset-R.

## Verner and Tate, 1989

This research was concerned primarily with component size estimation, rather than directly with system size estimation. However, such an approach is appropriate for FPA-like methods since these estimate system size as a sum of component size contributions. The researchers studied a 440-component information system of 31,513 LOC and 2868 function points (counted in accordance with Zwanzig (1984)) developed using a fourth generation language. Standard FPA (Zwanzig, 1984), Symons' Mark II (Symons, 1988) and a new (Verner) FPA-like model (Verner and Tate, 1989), the last tailored to the particular development environment, were compared. It was found that the component types of standard FPA (input, output, inquiry, internal file and external interface file), while they could be mapped to fourth generation development, were not the natural component types for this environment. The natural component types were relations, menus, screens and reports. After using suitable conversion factors between function points and LOC, e.g. 31,513/2868 = 12.4 LOC/function point for standard FPA, estimated and actual component sizes were compared within component types and overall. The results, expressed in PRED(.25) percentages, are shown in Table 2.

## Verner, 1989

More recent research by Verner has extended the work discussed above. Here the model described in Verner and Tate (1989), based on the first increment (440 components) of a system was used to predict a later increment (667 components) of the same system. The resulting prediction for the whole second increment was 96% of actual size, compared to an estimate based on standard FPA of 73% of actual. This work looked at the prediction of size of system components at two different phases, Phase 1: requirements, and Phase 2: preliminary design. Percentage of actual LOC prediction by component type and overall are shown in Table 3.

Tailored estimation models were also applied to two additional 4GL developments (Informix and Advanced Revelation) and a COBOL development with very good results, PRED(.25) > 85% for all component size estimates in all three cases.

Table 2. Component size estimation (PRED(.25) percentages)

<table><tr><td></td><td>‘Standard’FPA</td><td>Symons’Mark II</td><td>Verner</td></tr><tr><td>Relations</td><td>0</td><td>-</td><td>68</td></tr><tr><td>Menus</td><td>49</td><td>0</td><td>100</td></tr><tr><td>Screens</td><td>42</td><td>49</td><td>80</td></tr><tr><td>Reports</td><td>27</td><td>24</td><td>74</td></tr><tr><td>All component types</td><td>32</td><td>34*</td><td>78</td></tr></table>

\* allowance was made for the fact that the Symons' model did not consider files, entities or relations as separate components.

Table 3. Percentage of actual LOC prediction

<table><tr><td rowspan="2">Phase</td><td colspan="2">Verner</td><td colspan="2">FPA</td></tr><tr><td>1(%)</td><td>2(%)</td><td>1(%)</td><td>2(%)</td></tr><tr><td>Menus</td><td>100</td><td>100</td><td>66</td><td>70</td></tr><tr><td>Relations</td><td>99</td><td>99</td><td>592</td><td>624</td></tr><tr><td>Reports</td><td>95</td><td>96</td><td>52</td><td>55</td></tr><tr><td>Screens</td><td>99</td><td>98</td><td>106</td><td>112</td></tr><tr><td>Updates*</td><td>0</td><td>88</td><td></td><td></td></tr><tr><td>Overall</td><td>95</td><td>96</td><td>71</td><td>73</td></tr></table>

\* batch-type file-to-file functions without direct user interaction.

## Low and Jeffery, 1990

The objectives of this research were to:

(a) evaluate the consistency of the function point estimates as an a priori measure of system size;

(b) identify any limitations in the use of function points as an a priori measure of software size;

(c) determine if function point estimates are more consistent than SLOC estimates.

The authors used two (apparently hypothetical since no actuals are given) accounting program specifications in this research and used three major data sets:

(1) estimates made by 22 analysts experienced in estimating function points before actual development;

(2) estimates made by two groups of function point naive analysts;

(3) estimates made by 12 analysts who, although experienced in size estimation with SLOC, were not currently using this metric for size estimation.

Set 1: The results for Set 1, summarized below, show quite marked variations about the mean.

<table><tr><td>Program</td><td>FP mean</td><td>FP range</td></tr><tr><td>1</td><td>57.7</td><td>24–159</td></tr><tr><td>2</td><td>39.6</td><td>25–76</td></tr></table>

Possible explanations for these variations are suggested as being due to:

\- differences in analyst perception of user function complexity;

\- value judgements made when estimating the number of function points;

\- different interpretations of the specification;

\- different perceptions of the boundary of the programs as most organizations perform function point counts on entire systems;

\- objectives of the analyst doing the counting

\- analysts' experience with a priori counting.

Low and Jeffrey note that there were organizational differences and that one of the organizations had by far the largest organizational variation about their organizational mean. If this organization was removed from the group, the variations about the mean were reduced to within 24% for Program 1 and 16% for Program 2.

Set 2: These results are shown below. One of the organizations has been removed because of their relative lack of experience in a priori counting of function points.

<table><tr><td>Group</td><td>Mean</td><td>Range</td></tr><tr><td>Experienced</td><td>51.2</td><td>26–73</td></tr><tr><td>Inexperienced</td><td></td><td></td></tr><tr><td>Group A</td><td>83.7</td><td>52–144</td></tr><tr><td>Group B</td><td>72.9</td><td>43–135</td></tr></table>

Set 3: The results from the group of 12 analysts who had some previous experience with source lines of code estimation are shown below. One organization estimated in COBOL SLOC while the other two organizations estimated in PL/1 SLOC. It is worth noting that Low and Jeffery include both blank lines and comment lines in these SLOC. Analysts from two organizations estimated the source lines of code directly from specifications (one must assume these analysts used expert judgement or analogy but this is not specified in the paper) while the analysts from a third organization estimated staff days (presumably on a similar basis) and used an organizational productivity factor (LOC/staff days) to obtain an SLOC estimate.

<table><tr><td>Program</td><td>Language</td><td>Mean</td><td>Range</td></tr><tr><td>1</td><td>COBOL</td><td>1205</td><td>700–1710</td></tr><tr><td>1</td><td>PL/1</td><td>984</td><td>360–2300</td></tr><tr><td>2</td><td>COBOL</td><td>1265</td><td>650–1880</td></tr><tr><td>2</td><td>PL/1</td><td>624</td><td>144–2000</td></tr></table>

The variation about the mean were 72.2% for Program 1 and 80.8% for Program 2. The authors note that there were significant differences between results from the two organisations who estimated in PL/1 and are unsure as to whether this is caused by organizational differences or a difference in the way the results were obtained.

Low and Jeffery conclude that on an organizational basis SLOC estimates are no better than function point count estimates when estimated from program specifications and that function point counts appear to be a more consistent a priori measure of software size than SLOC. They note that there appear to be variations in function point estimates between companies, that experience in the application of function points appears to be an important factor in their successful application, and that software development experience influences function point estimates.

## Empirical studies of cost estimation models

These studies fall into four related and, in some cases, overlapping classes, namely:

(a) model validation research;

(b) model comparison using actual projects;

(c) model comparison using specifications of example projects not actually implemented;

(d) empirical studies investigating relationships in completed project data sets, often without specific reference to existing models.

Included within model validation research is work by researchers other than the model investors aimed at testing the applicability of a model to project data from which the model was not originally derived or calibrated. Model comparison research can be done using actual or hypothetical cases, the former clearly also involves elements of model validation. Model comparison can examine the relative performance of different cost estimation methods in a number of different aspects, the two most common being effort and duration, though other aspects such as phase distribution of effort, or productivity versus elapsed time, can also be compared.

Almost all the studies reported here are ex post or after-completion studies.

## Model validation research

Under this heading we have included independent empirical studies of one model only comparing the predictions of that model with actual project attributes. The following studies are identified together with summaries of their main findings.

## Golden, Mueller and Anselm, 1981

This study compared the Putnam model estimates of minimum time schedule, effort at minimum time schedule, and effort at actual time schedule with actual schedule and effort for four projects at the Xerox Corporation, as shown in Table 4.

While the Putnam effort estimates at the actual time schedule in the last column are quite close to the actual effort, the minimum time effort estimate indicates just how severe the effect of the fourth power effort-schedule tradeoff is and hence how critical schedule constraints are in the Putnam estimates. The study also contains a graphed comparison of actual manloading with Putnam estimates for one of the projects which shows a general similarity of shape and level.

## Wiener-Ehrlich, Hamrick and Rupolo, 1984

The Rayleigh curve model, on which SLIM (Putnam, 1978) is based and which some other models also use, was tested to see if it fitted the time/effort data from four data processing projects. It was found to be a reasonable fit so long as the maintenance phase was defined to include solely corrective maintenance in the sense of Lientz and Swanson (1980).

## Miyazaki and Mori, 1985

This is a very thorough evaluation study of Boehm's Intermediate COCOMO model (Boehm, 1981), together with a calibration of COCOMO to a set of 33 projects of large average size, mainly in COBOL and PL/1, but including some Fortran and Assembly systems. Miyazaki and Mori showed that COCOMO, as calibrated by Boehm to his database, overestimated project effort. However, COCOMO could be effectively calibrated, by fitting a new constant and size exponent, to give a good fit to their data somewhat better (PRED (.20) = 77%) than Boehm's fit to his data (PRED (.20) = 68%). Their calibrated nominal effort equation, compared to COCOMO, was:

E/EAF = 2.15 \* size\*\*0.94 (Miyazaki and Mori)
E/EAF = 3.2 \* size\*\*1.05 Intermediate COCOMO organic mode

where E is effort in man months and EAF is effort adjustment factor.

Note that an exponent value of less than one in Miyazaki and Mori's calibration indicates scale economies for their environment in contrast to the diseconomies of scale shown in the data sets for the different environment for which Boehm originally calibrated Intermediate COCOMO.

Table 4. Comparison of Putnam model estimates with actual time and effort

<table><tr><td>Project</td><td>Min time est. (m)</td><td>Actual time (m)</td><td>Min time effort est. (pm)</td><td>Actual effort (pm)</td><td>Actual time effort est. (pm)</td></tr><tr><td>A</td><td>12.0</td><td>11.0</td><td>124</td><td>167</td><td>176</td></tr><tr><td>B</td><td>12.7</td><td>13,0</td><td>83</td><td>82</td><td>76</td></tr><tr><td>C</td><td>12.8</td><td>15.0</td><td>304</td><td>150</td><td>161</td></tr><tr><td>D</td><td>10.2</td><td>11.7</td><td>70</td><td>51</td><td>41</td></tr></table>

pm = person months; m = months

Miyazaki and Mori supported Boehm's practice of counting only one third of the lines of code in the COBOL declarative divisions and also gave JCL code a weighting of 2. A better fit to their data was also obtained by deleting three of Boehm's cost drivers, namely VIRT (virtual machine volatility), ACAP (analyst capability) and STOR (main storage constraint).

## Jeffery, 1987

Jeffery (1987a) tested Putnam's SLIM model in respect to its relationship between increasing difficulty and decreasing productivity using a large database of 47 Australian data processing projects. His data, which produced a productivity (PR) equation:

PR = effort\*\*(-0.47) \* t\*\*(-0.05) \* constant did not support the SLIM model

PR = effort\*\*(-0.66) \* t\*\*(1.33) \* constant in this regard, showing no relationship between productivity and difficulty and giving no support for the contention that productivity is reduced by project time compression in the environment Jeffery studied. Jeffery noted that this conclusion also applied to other models, such as COCOMO and PRICE S, which also imply decreasing productivity with time compression.

## Funch, 1987

This US study used 26 Air Force/Electronic Systems

Division (ESD) and Mitre Corporation projects, largely embedded, human-machine interface systems, comprising 110 software configuration items, to recalibrate five of the Basic and Intermediate COCOMO equations. The conclusions were that recalibration improved results substantially, that recalibration of the coefficient only was superior to exponent/coefficient recalibration and that the Intermediate model provides moderate improvements over the Basic model. A comparative summary of the recalibration is given in Table 5.

## Marouane and Mili, 1989

This study used a Tunisian database of 47 projects in a variety of languages (with COBOL predominating) most of which were developed in the previous four years. There were quite a number of large projects, comparatively more than in Boehm's COCOMO database. The authors calibrated Basic COCOMO to Tunisian conditions to obtain a model which they called TUCOMO. The main findings were substantial economies of scale. A summary of the calibration is given in Table 6.

## Comparison using actual project data

This section summarizes a number of studies in which two or more costing models are applied, in all cases after completion, to one or more actual projects for which data is available.

Table 5. Comparative summary of recalibration

<table><tr><td></td><td>ESD/Mitre</td><td>COCOMO</td></tr><tr><td colspan="3">Basic</td></tr><tr><td>embedded</td><td>E = 6.5 * size**1.20</td><td>E = 3.6 * size**1.20</td></tr><tr><td>semi-detached</td><td>E = 2.4 * size**1.12</td><td>E = 3.0 * size**1.12</td></tr><tr><td colspan="3">Intermediate</td></tr><tr><td>embedded</td><td>E/EAF = 2.4 * size**1.20</td><td>E/EAF = 2.8 * size**1.20</td></tr><tr><td>semi-detached</td><td>E/EAF = 3.1 * size**1.12</td><td>E/EAF = 3.0 * size**1.12</td></tr><tr><td colspan="3">Schedule</td></tr><tr><td>embedded</td><td>M = 3.8 * E**0.32</td><td>M = 2.5 * E**0.32</td></tr></table>

E is effort in man months; EAF is effort and adjustment factor; M is the elapsed time schedule in months

Table 6. Summary of calibration

<table><tr><td></td><td>TUCOMO</td><td>COCOMO</td></tr><tr><td colspan="3">Effort</td></tr><tr><td>organic</td><td> $E = 2.74 * size**0.76$ </td><td> $E = 2.4 * size**1.05$ </td></tr><tr><td>embedded</td><td> $E = 6.85 * size**0.66$ </td><td> $E = 3.6 * size**1.2$ </td></tr><tr><td colspan="3">Schedule</td></tr><tr><td>organic</td><td> $M = 2.31 * E**0.55$ </td><td> $M = 2.5 * E**0.38$ </td></tr><tr><td>embedded</td><td> $M = 1.82 * E**0.59$ </td><td> $M = 2.5 * E**0.32$ </td></tr></table>

## Kitchenham and Taylor, 1984–85

The 1984 study compared effort and schedule estimation for COCOMO and Putnam's Rayleigh curve model (Putnam, 1978) for 20 British Telecom (BT) and ICL projects, mostly of small to medium size (Kitchenham and Taylor, 1984). The 1985 study used data from an additional 14 projects, and extended the earlier work (Kitchenham and Taylor, 1985). There appear to be significant differences between the BT and ICL development environments, the latter being significantly more productive than the former, though not necessarily on the same kinds of applications. There was considerable variability in the data, the ratio of SLOC per person month varying by a factor of over 30 for the BT data and 20 for the ICL data. Kitchenham and Taylor found that both of the models required calibration in order to make sensible predictions of effort and duration, but that a fairly large historical database was required. They recommended the establishment of a sufficiently large database of completed projects to enable empirical relationships to be established to provide models calibrated to the environments in which they will be used. The 1985 paper suggested that it was possible to develop cost models tailored to a particular environment and to improve the precision of the models at later development phases by including additional information such as the known effort for the earlier phases.

## Caccamese, Cappello and Dodero, 1986

This study compared SLIM (Putnam, 1978) and COCOMO (Boehm, 1981) estimates for manpower and effort scheduling with actuals for three systems software projects. The findings were that the manpower and effort distribution laws embedded in the models did not fit the real distribution, COCOMO being a worse fit than SLIM.

## Conte, Dunsmore and Shen, 1986

Conte, Dunsmore and Shen used six sets of project data, the first being Boehm's data set on which COCOMO was based. The other five data sets listed in Appendix B of Conte et al. (1986) include sets from NASA-Goddard Space Centre, anonymous industry data, data from a Belady and Lehman study, data from a 1978–80 Yourdon survey and a US Army data set. The 187 projects in all were from widely differing environments, with the inclusion of both defence and commercial COBOL systems. The applicability of a number of models to this large collection of projects was investigated. This study is thus partly a validation of several models and partly a comparison of them. The main conclusions are listed for each model.

(a) Putnam models: The Putnam resource allocation model is in fact a small set of models based on the Rayleigh curve, together with some related relationships, including difficulty/productivity and effort/time equations. Conte et al. based their analysis on Putnam (1978, 1984, 1984a). They found that the Putnam models overestimate effort for small and medium-sized systems, exaggerate the effect of schedule compression on effort and are quite sensitive to the choice of Technology Factor Level. The difficulty/productivity relationship proposed by Putnam was not confirmed. The effort prediction performance of the model was poor with a mean error around 90% and a PRED(.25) of 10%.

(b) Jensen's model: The study was based on Jensen, (1984). The effort prediction was poor with mean error around 80% and a PRED(.25) of 17%.

(c) Boehm's Basic COCOMO: The model (Boehm, 1981) performed very poorly on a mix of commercial COBOL systems but quite well on a set of defence COBOL systems. The mean error was 70% with a PRED(.25) of 40%.

(d) Conte et al's COPMO: As a result of investigating the effect of team size on effort, Conte et al., proposed a new model, COPMO, which, when calibrated separately to each of the six data sets, gave a mean error of 21% and a PRED(.25) of 75%.

## Acosta and Golub, 1987

This study at US Army Aviation Systems Command compared two COCOMO variants, SECOMO (the software engineering cost model developed by Headquarters, US Army Material Command) and SWCE. The models were applied to data for 13 contracted embedded systems, mostly of medium size. In almost all cases the models underestimated actual effort, SECOMO more so than SWCE. The four worst underestimates were all of a similar order and for systems from a single contractor, suggesting a strong local environment effect in that case. The authors commented on analysis difficulties caused by variability in data and the need to search through available cases to identify subsets of relatively consistent data before calibrating estimation models.

## Kemerer, 1987

This study used 15 large DP projects, mostly written in COBOL in a US software house environment. The models compared were SLIM (Putnam, 1978), COCOMO (Boehm, 1981), Function Point Analysis (Albrecht and Gaffney, 1983) and ESTIMACS (Rubin, 1985). The data, though carefully collected, showed high variability in project productivity, measured in SLOC/pm (source lines of code per person month), the highest being 2,491 (for a project of 289 KSLOC) and the lowest 406 (for a project of 450 KSLOC), both on COBOL projects. Comparisons are made solely on the basis of effort prediction, but there is also a separate validation study of FPA. Conclusions drawn include the following:

(a) None of the models, when uncalibrated to the environment database, give good effort estimates, all overestimating substantially (from 85–772%).

(b) After calibration, the best fitting model (SLIM in this case, which paradoxically also gave the worst overestimates before calibration) explained 88% of the behaviour of the actual person month effort in this data set.

(c) Albrecht's model, as described in Albrecht and Gaffney (1983), for estimating effort from function points, has been validated by this study on an independent data set in the sense that it shows that there is a very similar linear regression between function points and effort for the Albrecht and Gaffney, and Kemerer data sets. The relationship is not a very close one, however, giving an MMRE of 1.03 and a PRED(.25) of $33\%$ .

(d) For the data set used, the adjustment factors in FPA and the cost drivers in COCOMO appeared to have little effect, from which Kemerer concluded that they did not model effectively the factors affecting productivity in that particular environment.

(e) Unadjusted function point counts were a better estimator of SLOC than adjusted function points.

(f) The models using ex post SLOC (SLIM and COCOMO) gave better results than the models using ex post function points. Kemerer conjectured that ex ante function points may be easier to estimate accurately than SLOC which might offset function points' less satisfactory measure of 'size' in this context.

(g) The results are rather sensitive to the presence of outliers in the data.

## Martin, 1988

This study reports a software costing tool evaluation study undertaken in Canada, using seven completed projects of substantial size (93–1990 person months) and comparing WICOMO (a COCOMO implementation from the Wang Institute of Graduate Studies), SYSTEM-3 (Jensen, 1981), Before You Leap (BYL) (Gordon, 1987, but no reference given in this paper) and SPQR (Jones, 1986). All models tended to overestimate effort. All models also tended to give estimates varying in the same direction with each specific project, all overestimating greatly on three of the seven, and underestimating significantly on one project. Martin noted some inconsistencies in the source data that could partially account for this. Even with calibration, using regression of estimated effort against actual effort, both the regression constant (324–877 pm) and the standard error of the estimate (341–747 pm) were embarrassingly large for all models. For both effort and schedule BYL gave the lowest standard error of estimate, followed by SPQR, WICOMO and SYSTEM-3.

## Pfleeger and Bollinger, 1989

This recent work by Pfleeger and Bollinger concentrates on reuse issues in object-oriented development. The Pfleeger (1989) model should perhaps be described as a partial model in that it makes reuse adjustments to an average value, obtained using another model, such as COCOMO (Boehm, 1981). Cost factors affecting productivity can be defined by the user and, for each such factor X, a cost multiplier is generated from estimates of the portion of the project affected by X, the cost of creating X, the cost of incorporating X into the project, and the number of projects over which the costs will be amortized. In a study involving six projects, the Pfleeger model had less than half the error of COCOMO and Ada-COCOMO (Boehm, 1987) and a PRED(.25) of 50% compared with 0 for COCOMO and Ada-COCOMO. These results are only preliminary, but suggest that the Pfleeger model may capture more about the relationship between cost and reuse that either COCOMO or Ada-COCOMO.

## IIT Research Institute, 1989

This study was done by the IIT Research Institute for the US Air Force Cost Centre and the US Army Cost and Economic Analysis Centre under the sponsorship of the Ada Joint Program Office. It applied two Ada-specific models (COSTMODL (NASA, 1988), an Ada-COCOMO implementation (Boehm, 1987) and SoftCost-Ada (Reifer, 1989a)) and four non-Ada-specific models (PRICE S (Park, 1988), SYSTEM-3 (Jensen, 1987), SPQR/20 (Jones, 1986) and SASET (Martin, 1988)) to eight projects: four command and control (three using object-oriented design and one structured design); three tool/environment using object-oriented design; and one avionics using structured design. The tool/environment projects were commercial contracts, the others government contracts. Two estimates were made for each model, one using all relevant information from the completed projects, the other using actual project values for size, application type, programming language and other model inputs that must be known early in development, but average or nominal values for model input ratings not likely to be known quite so early. The results of the study were that:

\- though an Ada-specific model (SoftCost-Ada) gave the best overall results, the need for Ada-specific models was not clearly supported;

\- frequently different models gave the best results for different evaluation criteria: accuracy for effort, accuracy for schedule, consistency for effort, consistency for schedule, as well as accuracy/consistency for contract type and application type; the best performances typically had a PRED(.3) of around 50%;

\- different models also tended to give the best results for nominal estimates as distinct from full-knowledge estimates; moreover, the best nominal estimates were not a great deal worse than the best full-knowledge estimates.

Summary test case results giving the best two performances for overall accuracy and consistency are given in Table 7. The reader should note, however, that these results are different from the best performances in different application categories. For the latter the reader is referred to the original report, Illinois Institute of Technology Research Institute (1989).

## Comparison using hypothetical systems

Studies in this category use one or more example problem statements as input to a number of different cost estimation models/packages to obtain estimates of effort, duration, peak staff, etc. The example problems are not implemented, so there is no comparison with actual. The problem is often taken from some supposedly independent source. A difficulty with this type of study is the absence of an actual environment to which models may be calibrated. Thus differences between models may reflect differences between calibration environments more than real differences between the models themselves.

## Mohanty, 1981

This is an early comparison of 12 different models using a computation-intensive hypothetical system of 36,000 machine language instructions. Many of the early cost estimation models used in this study may have provided useful input into later models, however most (with one notable exception), are not now in widespread current use. The results which are summarized in Table 8, show a 5–7 fold variation between the lowest and highest cost estimates which would appear to indicate that the range of variation between different models has not narrowed significantly since then. Most of the models used in this study did not provide a schedule estimate.

Table 7. Summary IITRI test case study results. Best two performances overall for different criteria

<table><tr><td>Evaluation criteria</td><td>Model</td><td>Performance (within 30%)</td><td>Range (%)</td></tr><tr><td colspan="4">Effort accuracy</td></tr><tr><td rowspan="2">full knowledge</td><td>SoftCost-Ada</td><td>4 out of 7</td><td>0–13</td></tr><tr><td>SASET</td><td>4 out of 8</td><td>-29–29</td></tr><tr><td rowspan="2">nominal</td><td>SASET</td><td>4 out of 8</td><td>-24–29</td></tr><tr><td>SYSTEM-3</td><td>3 out of 8</td><td>-17–28</td></tr><tr><td colspan="4">Schedule accuracy</td></tr><tr><td rowspan="2">full knowledge</td><td>SYSTEM-3</td><td>4 out of 8</td><td>-27–-7</td></tr><tr><td>PRICES</td><td>3 out of 8</td><td>3–18</td></tr><tr><td rowspan="2">nominal</td><td>SPQR/20</td><td>6 out of 8</td><td>-23–28</td></tr><tr><td>PRICES</td><td>4 out of 8</td><td>-26–21</td></tr><tr><td colspan="4">Effort consistency</td></tr><tr><td rowspan="2">full knowledge</td><td>SYSTEM-3</td><td>5 out of 8</td><td>-14–28</td></tr><tr><td>PRICES</td><td>5 out of 8</td><td>-26–22</td></tr><tr><td rowspan="2">nominal</td><td>COSTMODL</td><td>3 out of 6</td><td>-23–30</td></tr><tr><td>SoftCost-Ada</td><td>3 out of 7</td><td>0–28</td></tr><tr><td colspan="4">Schedule consistency</td></tr><tr><td rowspan="2">full knowledge</td><td>SYSTEM-3</td><td>5 out of 8</td><td>0–28</td></tr><tr><td>PRICES</td><td>5 out of 8</td><td>-29–28</td></tr><tr><td rowspan="2">nominal</td><td>SPQR/20</td><td>6 out of 8</td><td>-28–20</td></tr><tr><td>PRICES</td><td>5 out of 8</td><td>-28–29</td></tr></table>

Table 8. Comparison of cost estimation models

<table><tr><td>Model</td><td>Estimate (person months)</td><td>Schedule (months)</td></tr><tr><td>Farr and Zagorski</td><td>87</td><td>-</td></tr><tr><td>Naval Air Development Centre</td><td>480</td><td>-</td></tr><tr><td>Wolverton</td><td>222–326</td><td>-</td></tr><tr><td>Kustanowitz</td><td>384–664</td><td>19.6–25.8</td></tr><tr><td>Aerospace</td><td>322</td><td>-</td></tr><tr><td>GRC</td><td>294</td><td>-</td></tr><tr><td>SDC</td><td>288</td><td>-</td></tr><tr><td>PRICES</td><td>319</td><td>18</td></tr><tr><td>Walston and Felix</td><td>136</td><td>13.8</td></tr><tr><td>Aron</td><td>127</td><td>-</td></tr><tr><td>Schneider</td><td>211</td><td>-</td></tr><tr><td>Doty</td><td>164</td><td>-</td></tr></table>

## McCallum, 1983

Strictly speaking the example used by McCallum was not a hypothetical system as the work described shows how three different cost estimation methods were used to estimate cost for a proposed system of 102,350 lines of assembly language code. The methods used were: an aerospace top down software estimation method based primarily on memory estimates; a method using the Rayleigh (Putnam, 1978) model; and PRICE S (Park, 1988). The results obtained from these models were compared with estimates obtained by an independent group. The author describes the calibration of past projects to get an appropriate technology factor, C, to use with the Rayleigh model.

## Results were:

<table><tr><td></td><td>Effort (person years)</td></tr><tr><td>Aerospace Method</td><td>65.72</td></tr><tr><td>Rayleigh</td><td>64.25</td></tr><tr><td>RCA PRICES uncorrected</td><td>65.5</td></tr><tr><td>corrected for management effort</td><td>69.25</td></tr><tr><td>Independent group</td><td>67.5</td></tr></table>

The most interesting feature of this study is that the models had been calibrated using past history for use in the development environment and were all within $5\%$ of the independent group's estimate.

## Rubin, 1985

A single problem was used, the results being compared in a panel discussion at the 8th ICSE. The problem statement was taken from IBM's Independent study program workbook on estimating the applications development process (IBM, 1980). The tools compared were: Jensen's JS-1/JS-2, Putnam's SLIM, GEC's GECOMO (a COCOMO variant) and Rubin's ESTIMACS. Each tool was represented by its main developer. The key estimation results are presented in Table 9.

The results, particularly in the case of JS-2, probably tell us more about differences in the environments for which the models are intended (defence contracts in the case of JS-2) and in which they were calibrated than they do about particular model differences. Rubin's paper also contains an interesting tabulation of the input information from the problem statement used by each of the tools.

Table 9. Comparison of estimates from common problem statement

<table><tr><td></td><td>JS-2</td><td>SLIM</td><td>GECOMO</td><td>ESTIMACS</td></tr><tr><td>Effort (pm)</td><td>940*</td><td>200*</td><td>363</td><td>113†</td></tr><tr><td>Duration (m)</td><td>31</td><td>17</td><td>23</td><td>16</td></tr><tr><td>Peak staff</td><td>43</td><td>17</td><td>22</td><td>15</td></tr></table>

pm = person months; m = months  
\*minimum time solution  
$\dagger$ assumes application structures of average complexity and a pm = 152 hours

## Rollo and Ratcliff, 1988

Rollo and Ratcliff used a hypothetical study based on a JSD (Jackson Structured Design) (Jackson, 1983) design of a library system to investigate the applicability of FPA and COCOMO as cost estimation models for systems using JSD. The primary purpose of the study was to see if JSD specifications provided suitable inputs to these particular methods for estimating costs. They based their FPA estimate on the FP/COBOL SLOC ratio and effort per COBOL SLOC values given in (Albrecht and Gaffney, 1983). The SLOC calculated in this way were also used as input to COCOMO. Their estimates resulted in 6879 work hours using FPA and 9983 work hours with a schedule of 12.26 months using organic mode intermediate COCOMO model.

## Heemstra, van Genuchten and Kusters, 1989

This study describes a controlled experiment in which 14 experienced project leaders made early lifecycle estimates for the same project, given only an 'information plan' for what was in fact a known completed project. They each estimated project time and effort first manually, second using BYL (Gordon, 1987 but no reference given in this paper), third using ESTIMACS (Rubin, 1985) (effort only), as well as giving final estimates based on all of these. The estimates varied greatly and were mostly very different from actual. For example the final estimates of schedule varied from 6 to 20 months and of effort from 10 to 48 person months, compared to actuals of 6 and 8 respectively, with an SLOC of 6500. The conclusions of the study were that early estimation is unlikely to be accurate, whether an estimation tool is used or not; that calibration of estimation tools is essential; that lines of code work less well than function points as an estimator for the 'volume of an information system' at an early stage of development.

## Other recent empirical studies

Under this heading we have included analyses of project data sets whose main purpose has been to investigate relationships between important variables, rather than to validate or compare particular models.

## Jeffery, 1987

In a 3-phase study (Jeffery, 1987), data on 47 MIS projects from four large Australian organizations was analyzed in the first phase, data from 38 projects from three environments in the second phase and data from 23 projects in four organizations in the third phase (Jeffery, 1987). Phase 1 gave no support (in an MIS environment) for the argument that reducing a project's elapsed time would decrease the project's productivity. Phase 2 found consistent support for a productivity model of the form

$$
\text { Productivity } = \mathrm{K} * \mathrm{LOC} ^ {* *} \mathrm{B} * \mathrm{MXSTAFF} ^ {* *} (- \mathrm{C})
$$

The Phase 3 study investigated the relationship between staffing levels, elapsed time and productivity. There was lower productivity with higher staff levels in all organizations studied. This reduction was largest where the average experience of the team was lowest. Based on this, and other data, Jeffery developed a software productivity package called CLAIR with a form similar to the equation above but with an experience multiplier appended.

## Desharnais, 1988

This study involved 82 MIS projects developed at ten organizations between 1983 and 1988. It used function points exclusively, rather than lines of code, and the analysis was concerned solely with effort prediction. The importance of calibration to the development environment was clearly shown but team and project manager's experience levels showed no significant influence.

## Jeffery and Low, 1989

This study analyzed 112 projects from six Australian organizations. The aim of the study was to test the extent to which industry-derived generic effort estimation/management models need calibration for individual organizations. Jeffery's CLAIR, developed from different data (Jeffery, 1987) from the same Australian MIS environment 5–10 years earlier, and Basic COCOMO, organic mode (Boehm, 1981), were compared. It was found that both CLAIR and COCOMO gave overestimates, COCOMO (calibrated to a quite different environment) much worse than CLAIR. Jeffery and Low concluded that organizational calibration appeared to be essential.

This study used function points as well as LOC in an appropriate version of the CLAIR model and also investigated productivity variations between organizations, both in function points/day and in LOC/day. It was concluded that function points/day differed significantly between organizations; LOC/day, though not differing significantly, were highly variable between organizations; also LOC/function point ratios for the same language (COBOL) were significantly different between organizations. The authors highlighted the need for clear, unambiguous definitions of software metrics.

## Observations

(a) The data sets used to validate or compare the models show great variability, not only in project size and type but also in productivity defined as LOC/person month. Even where a data set, e.g. from a single organization engaged in one line of business, might be considered fairly homogeneous there are usually productivity variations of more than an order of magnitude. In spite of efforts to quantify most aspects of a project affecting cost and to collect data consistently, both the quality and the completeness of the data for estimating purposes must in most cases be questioned. In particular, abnormal or atypical projects appear to be present in most data sets without the reasons for the abnormality being effectively recorded. Some method of data collection during a project which records relevant information about abnormalities (for example, massive iterated rework in several lifecycle phases) near the time they occur would seem to be desirable. Robert Park's observations in his 'open letter to cost model evaluators' (Park, 1989) make a number of very pertinent points concerning the mismatch that frequently occurs between the formats, and even the definitions, of project data as collected and the formats and definitions of estimation data as required by costing models. As he states: "This violates a fundamental principle of estimating – that the tool for data collection should be the same as the tool used for estimation."

(b) The results in general are disappointing. Using Conte's (Conte et al., 1986) suggested criteria that an acceptable estimate should have an MMRE ≤ 0.25 and PRED(.25) ≥ 75%, only a few sets of very carefully fitted ex post project estimates, such as those of Conte's generalized COPMO model, manage to meet these criteria. Most sets of estimates, even after calibration, come nowhere near to these criteria of acceptability.

(c) It is necessary to calibrate most models to new environments in order to avoid bias in estimates due to differences between the calibration environment and the application environment. Comparisons between models in which one or more models have been calibrated or tailored to a particular environment, while other have not, may be both misleading and unfair, unless a model purports to be widely applicable without calibration. The IIT Research Institute (1989) concept of consistency is a useful one for assessing the potential value of a model following calibration. Possibly the simplest method of calibration – if nothing more sophisticated is available – is by simple linear regression of model estimates against actuals to obtain a straight line scaling of estimates.

## Acknowledgements

Much of the work for this paper was done in conjunction with the MERMAID project which is partially funded by the Commission for the European Communities as Esprit Project P2046.

## References

Acosta, E.O. and Golub, D.H. (1987) Early Experience in Estimating Embedded Software Costs at AVSCOM, Proceedings of the International Society of Parametric Analysts Ninth Annual Conference, VI, 1, San Diego CA, May 5–7, 665–75.

Albrecht, A.J. (1979) Measuring Application Development Productivity, Proceedings Joint Share/Guide/IBM Application Development Symposium, Oct, 83–92; also reprinted in Jones, T.C. (ed) (1981) Programming Productivity Issues for the 80s IEEE Press, 34–43.

Albrecht, A.J. and Gaffney, J.E. Jnr (1983) Software Function, Source Lines of Code, and Development Effort Prediction: A Software Science Validation, IEEE Transactions on Software Engineering, SE-9, 6, 639–48.

Boehm, B.W. (1981) Software Engineering Economics, Prentice-Hall, New York.

Boehm, B.W. (1984) Software Engineering Economics, IEEE Transactions on Software Engineering, SE-10, 1, 4–21.

Boehm, B.W. (1987) Ada-COCOMO presentation at the Third International COCOMO Users' Group Meeting, Software Engineering Institute, Pittsburgh, PA, November.

Boehm, B.W. and Royce, W. (1989) TRW IOC Ada COCOMO: Definition and Refinements, Proceedings of the International Society of Parametric Analysts, 11th Annual Conference, Washington DC, VIII, 2, 3–100.

Bozoki, G.J. (1986) Software Sizing Method, GJB Associates, 552 Marine World Parkway #1202 Redwood City, CA 94065.

Bozoki, G.J. (1987) SSM presentation at Third International COCOMO Users' Group Meeting, Software Engineering Institute, Pittsburgh PA, November.

Britcher, R.N. and Gaffney, J.E. Jnr (1985) Reliable Size Estimates for Software Systems Decomposed as State Machines, Proceedings of IEEE COMPSAC85, October, 9–11.

Caccamese, A., Cappello, L. and Dodero, G. (1986) A Comparison of SLIM and COCOMO Estimates Versus Historical Manpower and Effort Allocation, 2nd COCOMO Users Group Meeting, Wang Institute, MA, May.

Conte, S.D., Dunsmore, H.E. and Shen, V.Y. (1986) Software Engineering Metrics and Models, Benjamin/Cummings Publishing Coy. Inc.

DeMarco, R. (1982) Controlling Software Projects: Management, Measurement and Estimation. Yourdon Press.

DeMarco, T. (1984) An Algorithm for Sizing Software Products, Performance Evaluation Review, 12, 2, 13–22.

DeMarco, T. (1989) In the Land of Function Metrics presentation at 5th International COCOMO Users' Group Conference, Pittsburgh, PA, October.

Desharnais, J-M. (1988) Analyze statistique de la productivité des projets de développement en informatique à partir de la technique des points de fonction, Rapport d'activité de synthèse, Programme de maîtrise en informatique de gestion, Université du Quebec à Montréal, December.

Funch, P. (1987) Recalibration of Intermediate COCOMO to recent AF Acquisitions, Third COCOMO Users' Group Meeting, Carnegie Mellon University, Software Engineering Institute, Pittsburgh, PA, Nov 3–5.

Heemstra, F.J., van Genuchten, M.J., and Kusters, R.J. (1989) Selection of Cost Estimation Packages Report EUT/BDK/36, Department of Industrial Engineering and Management Science, Eindhoven University of Technology, The Netherlands.

Golden, J.R., Mueller, J.R. and Anselm, B. (1981) Software Cost Estimating: Craft or Witchcraft, Database 12, 3, Spring, 12–14.

Gordon Group (1987) Before you Leap Users guide.

IBM (1980) Estimating Application Development Projects Workbook, IBM Corporation, NAD Education Staff Services, East Irving, Texas.

IIT Research Institute (1987) A Descriptive Evaluation of Software Sizing Models, prepared for Headquarters USAF/Airforce Cost Centre, Washington, DC 20330-5018, 4550 Forbes Boulevard, Suite 300 Lanham, MD 20706-4324, September.

IIT Research Institute (1987a) Software Cost Models Research Paper, prepared for US Army Cost and Economic Analysis Center, 1900 Half Street, Washington DC, September.

IIT Research Institute (1989) Estimating the Cost of Ada Software Development, prepared for US Airforce Cost Centre (AFCSTC) Arlington, VA, 22202, US Army Cost and Analysis Center (USACEAC) Washington, DC, 20324-200, and Ada Joint Program Office (AGPO), Arlington Va 22202, 4600 Forbes Boulevard, Lanham MD 20706-4324, April.

Jackson, M. (1983) System Development, Prentice-Hall, New York.

Jeffery, D.R. (1987) The Relationship between Team Size, Experience, and Attitudes and Software Development Productivity, COMPSAC87, Tokyo, October, 2–8.

Jeffery, D.R. (1987a) Time Sensitive Cost Models in the Commercial MIS Environment, IEEE Transactions on Software Engineering, SE-13, 7, 852–9.

Jeffery, D.R. and Low, G. (1989) Generic Estimation Tools in the Management of Software Development, pre-publication draft, School of Information Systems, University of New South Wales, Australia.

Jensen, R.W. (1981) A Macro-level Software Development Cost Estimation Methodology 14th Asilomar Conference on Circuits, Systems and Computers, New York, IEEE.

Jensen, R.W. (1984) A comparison of the Jensen and COCOMO schedule and cost estimation models, Proceedings of the International Society of Parametric Analysis, 96–106.

Jensen, R.W. (1987) SYSTEM-3 presentation at Third International COCOMO Users' Group Meeting, Software Engineering Institute, Pittsburgh PA, November.

Jones, T.C. (1986) Programmer Productivity, McGraw-Hill Book Company, New York.

Jones, T.C. (1989) Software Estimating: A Survey of the State of the Art, presentation at 5th International COCOMO Users' Group Conference, Pittsburgh, PA, October.

Kemerer, C.F. (1987) An Empirical Validation of Software Cost Estimation Models, Communications of the ACM, 30, 5, 416–29.

Kitchenham, B. and Taylor, N.R. (1984) Software Cost Models, ICL Technical Journal, May, 73–102.

Kitchenham, B. and Taylor, N.R. (1985) Software Project Development Cost Estimation, Journal of Systems and Software, 5, 4, 267–78.

Lientz, B.P. and Swanson, E.B. (1980) Software Maintenance Management: A Study of the Maintenance of Computer Application Software in 487 Data Processing Organizations, Addison-Wesley, Reading, MA.

Low, G.C. and Jeffery, D.R. (1990) Function Points in the Estimation and Evaluation of the Software Process IEEE Transactions on Software Engineering, 16, 1, 64–71.

Marouane, R. and Mili, A. (1989) Economics of software project management in Tunisia: Basic TUCOMO, Information and Software Technology, 31, 5, 251–7.

Martin, R. (1988) Evaluation of Current Software Costing Tools Software Engineering Notes, 13, 3, 49–51.

Martin, M. (1988) SASET Users' Guide, Denver Aerospace Corporation, July.

McCallum, D.H. (1983) A Comparison of Three Software Costing Techniques Proceedings of IEEE 1983 National Aerospace and Electronics Conference (NAECON), 1021–6.

MERMAID (1989) State of the Art Survey, Volume 1: Effort and Size Estimation Models, Esprit project P2046, Deliverable D1.2C Vol 1, February.

Miyazaki, Y. and Mori, K. (1985) COCOMO Evaluation and Tailoring, Proceedings of the 8th International Conference on Software Engineering, 292–9.

Mohanty, S.N. (1981) Software Cost Estimation: Present and Future, Software - Practice and Experience, 11, 103–21.

NASA (1988) COSTMODL, Software Development Cost Estimation Program developed by Mission Planning and Analysis Division of NASA, Johnson Space Center, Houston, TX.

Otte, J.E. (1986) Parametric Software Sizing Case Study, Proceedings of COMPSAC86, IEEE, 707–10.

Park, R.E. (1988) The Central Equations of the Price Software Cost Model 4th International COCOMO Users' Group Conference, Software Engineering Institute, Pittsburgh, PA, November.

Pfleeger, S.L. (1989) An Investigation of Cost and Productivity for Object Oriented Development Ph.D Thesis, George Mason University, Fairfax, VA.

Pfleeger, S.L. and Bollinger, T. (1989) A Reuse-Oriented Survey of Software Cost Models, unpublished draft, Contel Technology Centre, Fairfax, VA, June.

Putnam, L.H. (1978) A General Empirical Solution to the Macro Software Sizing and Estimation Problem, IEEE Transactions on Software Engineering, July, 345–81.

Putnam, L.H. and Fitzsimmons, A. (1979) Estimating Software Costs, Datamation, September, 189–98; October, 171–8; November, 137–40.

Putnam, D. (1987) Size Planner, An Automated Sizing Model, presentation to the 3rd COCOMO User's Group Meeting, Pittsburgh, November.

Rapp, W. (1985) RCA PRICE Software Sizing, Proceedings of the 7th International Conference of Parametric Analysts, Orlando, FL, May, 454–92.

Reifer, D. (1989) ASSET-R Manual, Reifer Consultants Inc. 25550 Hawthorne Boulevard, Suite 208/Torrance CA.

Reifer, D. (1989a) SOFTCOST-R User's Manual, Reifer Consultants Inc., 25550 Hawthorne Boulevard Suite 208/Torrance CA.

Rollo, T. and Ratcliff, B. (1988) Software Cost Estimation for JSD Products - An Interim Proposal, Jackson User Update, London.

Rubin, H.A. (1985) A Comparison of Cost Estimation Tools (A Panel Discussion), Proceedings of the 8th International Conference on Software Engineering, IEEE Computer Society Press, 174–80.

Symons, C.R. (1988) Function Point Analysis Difficulties and Improvements, IEEE Transactions on Software Engineering, 14, 1, January, 2–11.

Verner, J.M., Tate, G., Jackson, B. and Hayward, R.G. (1989) Technology Dependence in Function Point Analysis: A Case Study and Critical Review, Proceedings of the 11th International Conference on Software Engineering, Pittsburgh, May, 375–382.

Verner, J.M. (1989) A Generic Software Size Estimation Model Based on Component Partitioning, Ph.D Thesis, Massey University, Palmerston North, New Zealand.

Wiener-Ehrlich, W.K., Hamrick, J.R. and Rupolo, V.F. (1984) Modelling Software Behaviour in Terms of a Formal Life Cycle Curve: Implications for Software Maintenance, IEEE Transactions on Software Engineering, SE-10, 4, July, 376–83.

Zwanzig, K. (1984) (Ed.) Handbook for Estimating Using Function Points, GUIDE Project DP-1234, GUIDE Int. November.

## Biographical notes

Graham Tate is a professor of computer science at Massey University. He has thirty years experience in computing and is a consultant to government and commercial organizations and a member of a government computing policy committee in New Zealand. His main areas of current research are software economics and metrics, software prototyping, and CASE.

June M. Verner is a lecturer in computer science and information systems at Massey University and a consultant to government and commercial organizations in New Zealand. Her current research is in software engineering economics, particularly software size estimation.

Address for correspondence: School of Information Sciences, Massey University, Palmerston North, New Zealand.
