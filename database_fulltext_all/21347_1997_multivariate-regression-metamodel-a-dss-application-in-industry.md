---
otero_id: 21347
otero_key: "QPHRHQDQ"
title: "Multivariate regression metamodel: A DSS application in industry"
authors: "Roger W. McHaney; David E. Douglas"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00037-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Multivariate regression metamodel: A DSS application in industry

Roger W. McHaney $^{a,*}$ , David E. Douglas $^{b}$

$^{a}$ Department of Management, Kansas State University, 101 Calvin Hall, Manhattan, KS 66506, USA

$^{b}$ Computer Information Systems and Quantitative Analysis, University of Arkansas, BADM 204, Fayetteville, AR 72701, USA

Received 25 August 1995; revised 4 December 1995; accepted 16 february 1996

## Abstract

A materials handling system simulation (written using GPSS/H) was developed to predict the Automated Guided Vehicle requirements necessary for a major manufacturer to maintain desired levels of production in one of its automobile assembly plants. Rather than use the simulation as a representational DSS and risk complicating the user interface, validated simulation outputs were collected and used to produce a multivariate regression metamodel. This metamodel formed the centerpiece of a narrow-scope suggestion model DSS used on the factory floor to aid in day to day allocations of resources. This article looks at the metamodel development methodology and offers this technique as an effective means of producing a suggestion model DSS from a more complex representational DSS.

Keywords: Automated guided vehicles; Discrete event computer simulation; GPSS/H; Decision support system; Metamodel; Logic transfer

## 1. Introduction

Management science and operations research techniques have led to the development of sophisticated methods and models aimed at improving productivity and efficiency in manufacturing systems. An often cited problem with the use of these technologies occurs during implementation [1]. The process of moving the information gained during model development becomes lost or distorted resulting in problems for system users. Some approaches aimed at reducing these problems have been suggested for particular MS/OR techniques such as discrete event computer simulation [2,3]. Other general ideas [4] for moving from research to practical application have been mentioned in information system literature. While no logic transfer methodology has been adopted as a de facto standard, current widespread interest in the area of decision support systems (DSS) has certainly provided another avenue for overcoming many implementation problems [5]. This article demonstrates how the outputs from a complex representational DSS were transformed into a suggestion model DSS. The purpose of this transformation was to facilitate moving information from simulation to real-world and to simplify the user interface. This was accomplished by capturing the essence of a discrete event computer model in a regression meta-model. The metamodel was used to build a narrow scope decision support system used by line management in daily decision making.

## 1.1. Decision support systems

One person's spreadsheet is another's DSS. This sentiment is reflected in the information system literature through contradictory and varying viewpoints of what exactly comprises a decision support system. In an early attempt to define a DSS, Alter [6] conducted a study of usage. He discovered a wide variety of applications which could be broken into seven distinct types. While this research did not resolve the definition debate, it did indicate DSSs could be used in different ways with varying levels of sophistication.

Although Alter showed a diversity exists in what users believe to be decision support systems and most researchers agree diversity does exist, several questions remain. For instance, are DSSs appropriate for both structured [7] and unstructured decision making [8]? Are DSSs for use by executive management only [9] or are they for use by managers from any organizational level [7]? Are DSSs comprehensive, integrated systems or can they be as simple as spreadsheets?

While no exact answers to the preceding questions are available to practitioners wanting to implement the ideas generated in DSS literature, many of the concepts in the literature are being adopted. This article does not attempt to determine what exactly comprises a DSS. Instead it demonstrates how a complex decision aid classified as a representational DSS [6] was transformed into a mechanism for facilitating semi-structured decision making among operational management in the form of a simplified suggestion model [6].

## 1.2. Discrete event computer simulation

Computer simulation is an analysis tool currently enjoying a great deal of popularity. Its modern roots date back to the 1950s when some of the first computer models were developed. Initially computer simulation, like the hardware and software platforms available at the time, was unwieldy and cumbersome. Problem solving and decision making were time consuming and costly. It wasn't until the late seventies and early eighties that simulation became a reasonable method of analysis for many corporations. Once computer simulation was discovered by industry, its use proliferated [10]. Simulation's annual Directory of Simulation Software lists more than 130 products for 1993 [11]. In the 1991 OR/MS Today Simulation Software Survey, James Swain [12] reports practitioners of OR/MS are very likely to be familiar with simulation and cites over 50 discrete event simulation packages and languages.

In spite of recent improvements in simulation technology and its availability, running a model can still be a difficult and time consuming process. Special hardware, software and trained personnel may be required. Models of large production systems are often many thousand lines of code long and require hours to run. It is not uncommon for an analyst modeling a large system on a microcomputer to start the simulation before leaving for the night, expecting to retrieve the results the next morning. In addition, simulation outputs are observations of random variables and decisions can not be based on single observations. Instead, multiple replications must be collected and statistically analyzed.

Lengthy run times are not a severe problem in all situations. Simulations are expected to require substantial time and these times are added into schedules and deadlines. While speed improvements would be welcomed, run lengths are not always detrimental to a project. This is especially true when simulation is being used to aid in system design $[13]$ .

Although run times are not always important in the scope of a simulation project, circumstances exist where they do become very important. Lin and Cochran [14,15] report using simulations to model day to day operations on a factory floor. If a piece of machinery breaks down or becomes inoperable, an existing model of the system might be used to determine the ramifications of the situation. If answers can not be gleaned quickly from the simulation, the situation can not be assessed in a timely fashion. Proper action can not be started until after the fact. It is within this context of thinking that an approach for creating an analytic “model” or meta-model of a simulation has been suggested [16,17].

## 1.3. Simulation metamodels

A metamodel is defined as a supplementary model that is used to interpret a more complicated model [18]. To put it another way, a metamodel can be defined as a “model of a model”. Metamodels are increasingly being applied in post-simulation analysis to simplify complex models and provide a means for efficient and effective analysis [19]. The goal of a simulation metamodel is to capture the essence of a model without degrading the output. Metamodeling can offer additional benefits such as a reduction of analysis time, the ability to answer inverse questions (i.e. given a real-world output, what inputs would be required), a greater understanding of the system’s dynamics, and a simplified user interface.

## 2. Discussion of theoretical development

Management science advancements have lead to the development of sophisticated technology used to improve the productivity and efficiency of manufacturing systems. A problem resulting from these developments is the complexity of packaging the technology in a form that can be applied by end users. One method to reduce this complexity is to offer a decision aid within the context of a DSS. Often, the technology will dictate the necessary skill level of the end user and the type of DSS that must be used. Alter's [6] definitional framework provides a taxonomy of these DSS types. Seven distinct DSSs were identified (see Table 1).

Particularly relevant to this study are representational models. Representational models “include all simulation models which are not primarily accounting definitions” [6]. The problem being attacked in this study (i.e. a determination of certain parameters in complex manufacturing system) was investigated and solved using a representational DSS, discrete event computer simulation. However, certain characteristics of the representational DSS are not conducive to use by the desired end users (factory floor line managers) Would they be best served using this complex representational model? Would another of Alter's seven DSS types [6] provide a better candidate for implementation and day to day use?

To help answer this question, a theoretical DSS success framework was consulted. Researchers have investigated a number of factors believed to be related to the successful implementation of computerized DSSs. Guimaraes et al. [20] suggest an approach based on prior research [21-23] for the investigation of factors related to DSS success. These factors are grouped in four categories – implementation characteristics, task characteristics, decision maker characteristics, and DSS characteristics.

The factors grouped under the implementation characteristics category often include user involvement [24–27], user training [28] and organizational and management support [23,29]. Past empirical research has indicated significant relationships between success and these variables [20,30]. The task characteristics relate to the structuredness of the decision being made, the stages of decision making and the complexity and uncertainty involved with the decision [31]. The variable categorized under decision maker characteristics, have included cognitive style, DSS experience, organizational level, education, and information anxiety [20,31]. The fourth set of factors are related to the DSS itself. This class is sometimes referred to as technological factors [31]. Included here are interface type, technology level, the source of information and software and hardware.

Table 1  
Alter's DSS classification

<table><tr><td>Category</td><td>Operation</td><td>User</td><td>Task</td></tr><tr><td>File drawer</td><td>Access data</td><td>Line personnel</td><td>Operational</td></tr><tr><td>Data analysis</td><td>Ad hoc analysis of data files</td><td>Staff analyst</td><td>Operational or analysis</td></tr><tr><td>Analysis information system</td><td>Ad hoc analysis of databases and small models</td><td>Staff analyst</td><td>Analysis/planning</td></tr><tr><td>Accounting models</td><td>Calculations to estimate future results based on accounting definitions</td><td>Analyst or manager</td><td>Planning/budgeting</td></tr><tr><td>Representational models</td><td>Estimating consequences of particular actions</td><td>Staff analyst</td><td>Planning/budgeting</td></tr><tr><td>Optimization models</td><td>Calculate optimal solutions to combinatorial problems</td><td>Staff analyst</td><td>Planning/resource allocation</td></tr><tr><td>Suggestion models</td><td>Perform calculations that generate a suggested decision</td><td>Line personnel</td><td>Operational</td></tr></table>

The goal of this study was not to measure success but instead to insure the DSS implementation was successful. Meetings were held with shop floor managers to ascertain their comfort level in certain areas. The set of DSS success factors – implementation characteristics, task characteristics, decision maker characteristics, and DSS characteristics – were used as a guide in determining whether a representational or another type of DSS should be used to aid in day to day production resource decisions. In general, while user training could be implemented, organizational support was present, and the decision was fairly structured; other DSS success considerations such DSS experience, organizational level, education, and information anxiety would cause a complicated software implementation to fail.

To counter this problem, DSS characteristics such as interface type, technology level, the source of information and software/hardware could be controlled to give the implementation a better chance of success. What this meant to the project was that the complexities inherent to the representational DSS were reduced and instead a suggestion model DSS was provided. Suggestion models “generate suggested actions based on formulas or mathematical procedures which can range from decision rules to optimization methods” [6].

In order to transform a representational DSS into a suggestion model DSS, the essence of the simulation would have to be captured. Fig. 1 illustrates the process. It was determined the transformation could be accomplished by developing a multivariate regression metamodel from the simulation.

![](/api/attachments/QPHRHQDQ/fulltext/images/99ed8158373e202c013b6cb92a6c697d3835eb99e8624b0ed8cd7e55484e5ee4.jpg)  
Fig. 1. Representational DSS to a suggestion model DSS.

## 3. Justification for study

In large models of production systems, many interacting factors may create a situation which is difficult or impossible to analyze analytically. This complexity warrants the use of simulation to initially build a model. However, after the model is complete, independent input variables can be measured as can corresponding dependent output variables. Without trying to explain the phenomenon underlying the collected data, a multivariate regression metamodel can be created and used to predict system outputs based on various system inputs. Researchers have successfully applied this methodology in the past $[19,32,33]$ . Friedman and Pressman $[18]$ conducted a series of experiments and concluded metamodel results were as valid as the simulations from which they were derived. Agrawel $[34]$ extensively studied applications of metamodels in the area of computer system models. Madu $[19]$ proposed a series of steps to be used in metamodel development. These steps were used as the basis for the experiment described in this paper (see Fig. 2).

## 4. Study overview

A discrete event computer simulation was written to model a materials handling system for a major Midwestern automobile manufacturing plant. The initial objective of this simulation was to determine system throughput based on several variable inputs. The model was then to be used to help forecast daily throughput. This model, written in GPSS/H [35], was validated through comparison to the installed system. It provided accurate throughput information and was very useful. However, several limitations made the development of a metamodel desirable. These limitations were:

1. The model was developed off-site by consultants on an IBM 4381 Mainframe, which would not be available to production managers.

2. The program required approximately twenty minutes of run time.

3. The program was complex and difficult to use. No polished user interface was available.

4. The production facility did not hold a software license for GPSS/H, the consultants did.

In order to circumvent these limitations, data was collected from the validated simulation and used to create a multivariate regression metamodel. The objective of this procedure was to build a simplified decision support system (DSS) based on a regression equation. Production managers with access to this DSS would be able to predict the expected amount of material their system would move based on the resources available that day. This information could be used to reallocate workers or machinery to coincide with daily production requirements. Rather than wait for a full-blown GPSS/H simulation to run and perform necessary statistical interpretation, production managers would be able to obtain valid information almost instantaneously. This information would allow them to make immediate adjustments to work schedules.

## 5. The model and the metamodel

Outputs from the simulation were used as inputs to the regression metamodel. Independent variables within the measurement or control of the production managers were used as regression inputs. The simulation produced initial values for the dependent variable, system throughput. The independent variables and their ranges are shown in Table 2.

Other independent variables such as the physical layout of the factory, characteristics of the guided vehicles and truck dock arrival times were taken into account by the original GPSS/H simulation and were treated as fixed constraints built into the system. Changes to these variables would require

Fig. 2. Madu's steps for developing a metamodel [19].

changes to the simulation, collection of new data and regeneration of the metamodel.

## 5.1. Automated guided vehicle independent variables

The materials handling system uses automated guided vehicles (AGVs) to move materials from receiving docks to factory-floor production centers. The facility has two types of receiving docks, one being a truck dock and the other being a rail dock. The truck dock is serviced by AGV type 1 and the rail dock is serviced by AGV type 2. Production levels depend on timely deliveries of material by these two types of vehicles. It is expected the regression equation will show a positive relationship between the number of vehicles available and the number of loads moved. In other words, an increase in the number of AGVs should increase the number of loads moved. In earlier simulation studies, it was shown that more than 12 Type 1 or 8 Type 2 AGVs would no longer cause throughput to increase. Instead, congestion would result.

## 5.2. Number of laborers

Another independent variable expected to have a positive effect on the equation is the number of laborers available to unload an AGV. Upon arrival at a dropoff point, an AGV will take either 5 or 10 minutes to be unloaded depending on the number of laborers assigned to each area. If two are at each stop, the vehicle will require 5 minutes to unload, if one is at each stop, the vehicle will require 10 minutes. A binomial variable is used to represent whether one or two laborers are available to unload an AGV. A value of zero in this variable indicates one laborer, and a value of one indicates two laborers.

Description of independent variables

<table><tr><td>Independent variables</td><td>Variable name</td><td>Lower bound</td><td>Upper bound</td></tr><tr><td>Type 1 Automated guided vehicle</td><td>AGV1</td><td>2</td><td>12</td></tr><tr><td>Type 2 Automated guided vehicle</td><td>AGV2</td><td>2</td><td>8</td></tr><tr><td>Laborers at each station</td><td>LABOR</td><td>1</td><td>2</td></tr><tr><td>Loading spurs  $available^a$ </td><td>SPUR</td><td>2</td><td>4</td></tr></table>

$^{a}$ The range of this variable is not inclusive. Only 2 and 4 are legal values. The intermediate value of 3 is not usable.

## 5.3. Number of loading spurs

The final variable expected to have an effect on the regression equation is whether two or four loading spurs are available in the system. If four loading spurs are available, four vehicles can be loaded simultaneously, otherwise only two can be loaded at once. Another binomial variable is used to represent whether two or four spurs are available for loading AGVs. A value of zero in this variable indicates two spurs, and a value of one indicates four spurs are available. A positive relationship between the number of loading spurs and the dependent variable, loads moved (LM), is expected to result.

## 5.4. Regression equation

The regression equation was expected to take the following form:

$$
\begin{array}{r l} \mathrm{LM} & = \beta_ {0} + \beta_ {1} \mathrm{AGV1} + \beta_ {2} \mathrm{AGV2} + \beta_ {3} \mathrm{LABOR} \\ & + \beta_ {4} \mathrm{SPUR}. \end{array}\tag{1}
$$

The ordinary least squares algorithm was used to compute the coefficients of the regression model. As implied by the preceding equation, a simple, additive model is assumed. Normality and homogeneity were tested and found to be present. The appropriateness of a linear model was confirmed by plotting the residuals versus the dependent variable. No anomalies were detected.

## 5.5. Input data

Different approaches to collecting input data from a simulation are possible. All combinations of the four independent variables and resulting number of loads moved can be collected and fed into the meta-model. While this would provide a full set of data for the regression, Kleijnen [36] contends this is not necessary. Additional research shows adequate meta-models can be generated using a fraction of all possible combinations of independent variables [19,37]. $2^{k}$ full factorial experimental design is recommended. Within this context, independent variables are described as factors. Each factor must consist of at least two levels or categories. Factorial designs are described with reference to the number of categories for each factor (e.g. in this study a $2^{4}$ full factorial design means four independent variables will be used, each with two levels – the highest and lowest permissible values). This design requires only two levels of the k-independent variables be specified to conduct the experiment saving data collection and simulation run time [19]. For these reasons, the $2^{k}$ full factorial design approach was used in constructing the regression metamodel in this study. It is demonstrated with results that this metamodel provides a reasonable fit with the 16 combinations of input variables.

Table 3  
$2^{4}$ Full factorial experimental design

<table><tr><td>Run number</td><td>AGV1</td><td>AGV2</td><td>SPUR</td><td>LABOR</td><td>LM</td></tr><tr><td>1</td><td>+</td><td>+</td><td>+</td><td>+</td><td>932</td></tr><tr><td>2</td><td>-</td><td>+</td><td>+</td><td>+</td><td>587</td></tr><tr><td>3</td><td>+</td><td>-</td><td>+</td><td>+</td><td>697</td></tr><tr><td>4</td><td>+</td><td>+</td><td>-</td><td>+</td><td>773</td></tr><tr><td>5</td><td>+</td><td>+</td><td>+</td><td>-</td><td>802</td></tr><tr><td>6</td><td>-</td><td>-</td><td>+</td><td>+</td><td>448</td></tr><tr><td>7</td><td>-</td><td>+</td><td>-</td><td>+</td><td>478</td></tr><tr><td>8</td><td>-</td><td>+</td><td>+</td><td>-</td><td>476</td></tr><tr><td>9</td><td>+</td><td>-</td><td>-</td><td>+</td><td>557</td></tr><tr><td>10</td><td>+</td><td>-</td><td>+</td><td>-</td><td>645</td></tr><tr><td>11</td><td>+</td><td>+</td><td>-</td><td>-</td><td>669</td></tr><tr><td>12</td><td>+</td><td>-</td><td>-</td><td>-</td><td>456</td></tr><tr><td>13</td><td>-</td><td>+</td><td>-</td><td>-</td><td>478</td></tr><tr><td>14</td><td>-</td><td>-</td><td>+</td><td>-</td><td>320</td></tr><tr><td>15</td><td>-</td><td>-</td><td>-</td><td>+</td><td>308</td></tr><tr><td>16</td><td>-</td><td>-</td><td>-</td><td>-</td><td>270</td></tr></table>

Table 4  
Data ranges for Table 2

<table><tr><td>Input variable</td><td>(+) High value</td><td>(-) Low value</td></tr><tr><td>AGV1</td><td>12</td><td>2</td></tr><tr><td>AGV2</td><td>8</td><td>2</td></tr><tr><td>LABOR</td><td>1</td><td>0</td></tr><tr><td>SPUR</td><td>1</td><td>0</td></tr></table>

Table 3 contains two levels of each of the four independent input variables and the resulting number of loads moved in the simulation. Each result is an average based on multiple replications of the simulation with startup conditions removed. The regression metamodel was created with this data. Table 4 contains the high and low values indicated as ‘+’ or ‘-’ in Table 3.

## 5.6. Regression analysis

Table 5 summarizes the results of the regression analysis. All four independent variables were found to contribute significantly to the regression equation with a Prob > T of 0.0001 for AGV1, AGV2 and SPUR; and a Prob > T of 0.0014 for LABOR. The regression model itself was also found to be significant (Prob > F = 0.0001). The regression coefficient (adjusted R-sq) indicated 95.68% of the variation in the dependent variable LM was explained by the variation of the independent variables in the regression equation.

Table 5  
Results and regression

<table><tr><td colspan="6">Analysis of variance</td></tr><tr><td>Source</td><td>DF</td><td>Sum of squares</td><td>Mean square</td><td>F-value</td><td>Prob &gt; F</td></tr><tr><td>Model</td><td>4</td><td>512950.75000</td><td>128237.68750</td><td>84.009</td><td>0.0001</td></tr><tr><td>Error</td><td>11</td><td>16791.25000</td><td>1526.47727</td><td></td><td></td></tr><tr><td>C total</td><td>15</td><td>529742.00000</td><td></td><td></td><td></td></tr><tr><td>Root MSE</td><td></td><td>39.07016</td><td>R-square</td><td>0.9683</td><td></td></tr><tr><td>Dep mean</td><td></td><td>556.00000</td><td>Adj R-sq</td><td>0.9568</td><td></td></tr><tr><td>C.V.</td><td></td><td>7.02701</td><td></td><td></td><td></td></tr><tr><td colspan="6">Parameter estimates</td></tr><tr><td>Variable</td><td>DF</td><td>Parameter estimate</td><td>Standard error</td><td>T for H0: parameter = 0</td><td>Prob &gt; |T|</td></tr><tr><td>INTERCEP</td><td>1</td><td>111.975000</td><td>27.17022948</td><td>4.121</td><td>0.0017</td></tr><tr><td>AGV1</td><td>1</td><td>27.075000</td><td>1.95350792</td><td>13.860</td><td>0.0001</td></tr><tr><td>AGV2</td><td>1</td><td>31.125000</td><td>3.25584653</td><td>9.560</td><td>0.0001</td></tr><tr><td>SPUR</td><td>1</td><td>114.750000</td><td>19.53507917</td><td>5.874</td><td>0.0001</td></tr><tr><td>LABOR</td><td>1</td><td>83.000000</td><td>19.53507917</td><td>4.249</td><td>0.0014</td></tr></table>

Table 6  
Interpretation of model

<table><tr><td>AGV1</td><td>When an AGV of type #1 is added to the system approximately 27 additional loads can be moved per shift.</td></tr><tr><td>AGV2</td><td>When an AGV of type #2 is added to the system approximately 31 additional loads can be moved per shift.</td></tr><tr><td>SPUR</td><td>When four rather than two parallel spurs are used for loading in the AGV system, approximately 115 additional loads can be moved per shift.</td></tr><tr><td>LABOR</td><td>When two rather than one laborer is used for unloading an AGV, approximately 83 additional loads can be moved per shift.</td></tr></table>

Eq. (2) is the regression model as determined by the ordinary least squares algorithm.

$$
\begin{array}{r l} \mathrm{LM} & = 1 1 1. 9 7 5 + 2 7. 0 7 5 (\mathrm{AGV} 1) + 3 1. 1 2 5 (\mathrm{AGV} 2) \\ & + 1 1 4. 7 5 (\mathrm{SPUR}) + 8 3 (\mathrm{LABOR}). \end{array} \tag {2}
$$

A relationship very similar to what was expected resulted from the regression. Table 6 provides a brief interpretation of the regression equation in terms of the underlying model.

## 5.7. Metamodel validity

Simulation validity is a measure of how well the model matches the real world system it represents. Metamodel validity is a measure of how well the metamodel matches the simulation upon which it is based. Fig. 3 illustrates this concept.

The simulation was validated through comparison to the actual system when it was installed. In order to assess the validity of the metamodel, a sequence of 20 sets of variables were used as inputs to both the simulation and the metamodel. Madu [19] cautions while it is advisable to evaluate metamodel validity using input values that satisfy the constraints on the model, it is important not to use the values that were used in metamodel development. This precludes the extreme values used in regression development from being part of the validation data set. For this reason, random values within the boundaries of the sample data were chosen. Values of the independent and corresponding dependent variable (LM) were collected from both the simulation and metamodel and compared. Table 7 contains the test run values.

![](/api/attachments/QPHRHQDQ/fulltext/images/cc1c5f6cf237e6951f004f5908062c2b0581a86816c80a247167ab93c0d43af9.jpg)

![](/api/attachments/QPHRHQDQ/fulltext/images/c2e9cf4043ea88bdf2f1ebf5cec36f25758ee0c88b92661adde1bebb1be7f8a5.jpg)  
Fig. 3. Metamodel validation.

Table 7  
Metamodel validation data $^{4}$

<table><tr><td>AGV1</td><td>AGV2</td><td>SPUR</td><td>LABOR</td><td>LM-SIM</td><td>LM</td><td>% Differenceb</td></tr><tr><td>3</td><td>4</td><td>1</td><td>0</td><td>399</td><td>432.45</td><td>8.38</td></tr><tr><td>4</td><td>3</td><td>0</td><td>1</td><td>384</td><td>396.65</td><td>3.29</td></tr><tr><td>4</td><td>3</td><td>1</td><td>0</td><td>409</td><td>428.40</td><td>4.74</td></tr><tr><td>4</td><td>6</td><td>1</td><td>1</td><td>616</td><td>604.78</td><td>1.82</td></tr><tr><td>4</td><td>8</td><td>1</td><td>0</td><td>547</td><td>584.03</td><td>6.77</td></tr><tr><td>5</td><td>3</td><td>1</td><td>1</td><td>548</td><td>538.48</td><td>1.74</td></tr><tr><td>5</td><td>6</td><td>1</td><td>1</td><td>657</td><td>631.85</td><td>3.83</td></tr><tr><td>6</td><td>2</td><td>1</td><td>0</td><td>444</td><td>451.43</td><td>1.67</td></tr><tr><td>6</td><td>3</td><td>1</td><td>1</td><td>547</td><td>565.55</td><td>3.39</td></tr><tr><td>6</td><td>6</td><td>0</td><td>1</td><td>522</td><td>544.18</td><td>4.25</td></tr><tr><td>6</td><td>8</td><td>1</td><td>0</td><td>625</td><td>638.18</td><td>2.11</td></tr><tr><td>7</td><td>5</td><td>1</td><td>1</td><td>694</td><td>654.88</td><td>5.64</td></tr><tr><td>7</td><td>6</td><td>0</td><td>1</td><td>588</td><td>571.25</td><td>2.85</td></tr><tr><td>8</td><td>4</td><td>1</td><td>1</td><td>720</td><td>650.83</td><td>9.61</td></tr><tr><td>8</td><td>6</td><td>0</td><td>1</td><td>573</td><td>598.33</td><td>4.42</td></tr><tr><td>8</td><td>8</td><td>1</td><td>0</td><td>649</td><td>692.33</td><td>6.68</td></tr><tr><td>9</td><td>6</td><td>1</td><td>0</td><td>624</td><td>657.15</td><td>5.31</td></tr><tr><td>10</td><td>2</td><td>1</td><td>1</td><td>683</td><td>642.73</td><td>5.90</td></tr><tr><td>11</td><td>4</td><td>0</td><td>1</td><td>575</td><td>617.30</td><td>7.36</td></tr><tr><td>12</td><td>4</td><td>1</td><td>0</td><td>645</td><td>676.13</td><td>4.83</td></tr></table>

$^{a}$ Paired T = -0.91, Prob > |T| = 0.3736.  
$^{b}$ Average % difference = 4.73.

The difference or absolute error is obtained with the following formula [33]:

$$
\left| \text { Metamodel } - \text { Analytic } \right| / \text { Analytic }.\tag{3}
$$

As indicated in Table 7, the average absolute difference between the simulation and the regression metamodel in the twenty experimental runs is 4.73%. In related studies of metamodel validation [33,38] similar absolute error rates were found to be acceptable. A paired t-test was used to further insure no significance difference between the simulation and metamodel existed. The resulting t-value was -0.91 and the p-value was 0.3736. This further indicates no significant difference exists. Additional validation techniques are discussed by Friedman and Friedman [38].

## 6. Summary

This paper demonstrates how a representational DSS can be simplified into a suggestion model DSS without a loss of accuracy. This transformation was accomplished using a multivariate regression meta-model developed from a discrete event computer simulation. By reducing a large discrete event simulation model to a linear equation and by placing the resulting equation into a small computer program, production management has the ability to answer resource allocation questions rapidly and efficiently. While this concept may not be appropriate in all circumstances, in systems where linear relationships can be demonstrated to exist and where adequate regression explanatory power can be shown, simulation regression metamodels can be powerful and useful tools.

This concept was illustrated within the context of a real world application. A materials handling system in a major automotive assembly plant was simulated with the GPSS/H language. This stochastic model was reduced to a metamodel using the ordinary least squares algorithm to calculate regression coefficients for known independent variables in the system. Using the metamodel, automated guided vehicle requirements can now be calculated within the context of an easy-to-use suggestion model decision support system rather than a complex representational DSS.

## References

[1] A. Geoffrion, Can MS/OR Evolve Fast Enough?, Interfaces 13 (1983) 10–15.

[2] R. McHaney, Bridging the Gap: Transferring Logic From a Simulation into an Actual System Controller, Proceedings of the 1988 Winter Simulation Conference, Society for Computer Simulation, San Diego, CA (1988) 178–183.

[3] R. McHaney, Reusing Simulation Logic in System Development Projects, in: Zobrist and Leonard, Eds., Progress in Simulation, Vol. 1 (Ablex Publishing Corporation, Norwood, New Jersey, 1992) 159–185.

[4] T. Korson and V. Vaishavi, Managing Emerging Software Technologies: A Technology Transfer Framework, Communications of the ACM 35, No. 9 (1992) 101–111.

[5] S. Floyd, C. Turner and K. Davis, Model-Based Decision Support Systems: An Effective Implementation Framework, Computers and Operations Research 15, No. 5 (1989) 481–491.

[6] S. Alter, A Taxonomy of Decision Support Systems, Sloan Management Review (Fall 1977) 37–56.

[7] R. Sprague and E. Carlson, Building Effective Decision Support Systems (Prentice-Hall, Englewood Cliffs, New Jersey, 1982).

[8] P. Keen and M. Scott Morton, Decision Support Systems: An Organizational Perspective (Addison-Wesley, Reading, MA, 1978).

[9] P. Keen and G. Wagner, DSS: An Executive Mind-Support System, Datamation (1979).

[10] D. Christy and H. Watson, The Application of Simulation: A Survey of Industry Practice, Interfaces 13, No. 5 (1983) 47–52.

[11] J. Rodrigues, Ed., Directory of Simulation Software, Vol. 4 (The Society for Computer Simulation, San Diego, CA, 1993).

[12] J. Swain, Flexible Tools for Modeling, OR/MS Today, (Dec. 1993) 62–78.

[13] R. McHaney, Computer Simulation: A Practical Perspective (The Academic Press, San Diego, CA, 1991).

[14] L. Lin and J. Cochran, Estimating Simulation Metamodel Parameters for Unexpected Shop Floor Real Time Events, Computers and Industrial Engineering 19, No. 1–4 (1990) 62–66.

[15] L. Lin, J. Cochran and J. Sarkis, A Metamodel-Based Decision Support System for Shop Floor Production Control, Computers in Industry 18 (1992) 155–168.

[16] R. Blanning, The Construction and Implementation of Meta-models, Simulation 24 (1975) 177–184.

[17] A. Pritsker, Developing Analytical Models Based on Simulation Results, in: Proceedings of the 1989 Winter Simulation Conference (Washington DC, Dec. 4–6), SCS, San Diego (1989) 653–660.

[18] L. Friedman and I. Pressman, The Metamodel in Simulation Analysis: Can it be Trusted? Journal of the Operational Research Society 39, No. 10 (1988) 939–948.

[19] C. Madu, Simulation in Manufacturing: A Regression Meta-model Approach, Computers and Industrial Engineering 18, No. 3 (1990) 381–389.

[20] T. Guimaraes, M. Igbaria and M. Lu, The Determinants of DSS Success: An Integrated Model, Decision Sciences 23, No. 2 (1992) 409–430.

[21] W. Fuerst and P. Cheney, Factors Affecting the Perceived Utilization of Computer-Based Decision Support Systems in the Oil Industry, Decision Sciences 13, No. 4 (1982) 554–569.

[22] H.C. Lucas, Empirical Evidence for a Descriptive Model of Implementation, MIS Quarterly 2, No. 2 (1978) 27–41.

[23] L.G. Sanders and J.F. Courtney, A Field Study of Organizational Factors Influencing DSS Success, MIS Quarterly 9, No. 1 (1985) 77–93.

[24] A.M. Baronas and M.R. Louis, Restoring a Sense of Control During Implementation: How User Involvement Leads to System Acceptance, MIS Quarterly 12, No. 1 (1988) 111-124.

[25] B. Ives and M.H. Olson, User Involvement and MIS Success: A Review of Research, Management Science 30, No. 5 (1984) 586–603.

[26] G.M. Kasper, The Effect of User-Developed DSS Applications on Forecasting Decision-Making Performance in an Experimental Setting, Journal of Management Information Systems 2, No. 2 (1985) 26–39.

[27] R.I. Mann and H.J. Watson, A Contingency Model for User Involvement in DSS Development, MIS Quarterly (March, 1984), 27–37.

[28] R. Nelson and P. Cheney, Training End-Users: An Exploratory Study, MIS Quarterly 11, No. 4 (1987) 547–559.

[29] H.J. Watson, A. Lipp, P.Z. Jackson, A. Dahmani and W.B. Fredenberger, Organizational Support for Decision Support Systems, Journal of Management Information Systems 5, No. 4 (1989) 87–109.

[30] C.R. Franz and D. Robey, Organizational Context, User Involvement, and the Usefulness of Information Systems, Decision Sciences 17, No. 2 (1986) 329–356.

[31] R.P. Minch, Application and Research Areas for Hypertext in Decision Support Systems, Journal of Information Systems Management 6, No. 3 (1989–1990) 120–136.

[32] J. Kleijnen, Regression Metamodels for Generalizing Simulation Results, IEEE Transactions on Systems, Man, and Cybernetics 9, No. 2 (1979) 93–96.

[33] L. Friedman, The Multivariate Metamodel in Queuing System Simulation, Computers and Industrial Engineering 16, No. 2 (1989) 329–337.

[34] S. Agrawel, Metamodeling: A Study of Approximations in Queuing Models (The MIT Press, Cambridge, MA, 1985).

[35] J. Henriksen and R. Crane, GPSS/H User's Manual, 3rd edition (Wolverine Software Corporation, Annandale, VA, 1989).

[36] J. Kleijnen, Statistical Tools for Simulation Practitioners (Marcel Dekker, New York, 1987).

[37] J. Kleijnen and C. Strandridge, Experimental Design of a Regression Analysis in Simulation: An FMS Case Study, European Journal of Operational Research 33 (1988) 257–261.

[38] L.W. Friedman and H.H Friedman, Validating the Simulation Metamodel: Some Practical Approaches, Simulation 45, No. 3 (1985) 144–146.

![](/api/attachments/QPHRHQDQ/fulltext/images/8a07d3572003e3a7cde5d93c079d29cc056ddb274629f1a3949ce3144959f136.jpg)

Roger McHaney was employed by the Jervis B. Webb Company for 8 years prior to his return to academia. At the Webb Company he simulated numerous materials handling systems for customers including General Motors, Goodyear, Ford, IBM, Chrysler, Kodak, Caterpillar, the Los Angeles Times, and the Boston Globe. His current research interests include automated guided vehicle system simulation, innovative uses for simulation languages and simulation

success. After completing a Ph.D. in Computer Information Systems and Quantitative Analysis at the University of Arkansas, he accepted a position as Assistant Professor at Kansas State University. Roger is author of the 1991 Academic Press book, Computer Simulation: A Practical Perspective.

![](/api/attachments/QPHRHQDQ/fulltext/images/2fa5af3781bf01a31f1ee00db28c7868a8db584d1d11c023a6a179d17d38b881.jpg)

David E. Douglas is Department Chair and Professor of Computer Information Systems and Quantitative Analysis at the University of Arkansas. Dr. Douglas received his Ph.D. in Industrial Engineering at the University of Arkansas and is an active member of the Decision Sciences Institute, the Southwest Decision Sciences Institute, the Institute of Industrial Engineering and the American Society of Quality Control. He has served the Southwest Decision Sciences

Institute in many capacities including the Board, Vice President of Student Liaison, track chair, paper reviewer, and discussant. His research interests include object-oriented technologies, client-server computers, re-engineering and systems development. His publications have appeared in the Journal of Computer Information Systems, Communications of the ACM, Industrial Engineering, as well as other journals and conference proceedings.
