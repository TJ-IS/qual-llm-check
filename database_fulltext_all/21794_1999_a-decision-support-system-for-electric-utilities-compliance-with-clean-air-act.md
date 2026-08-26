---
otero_id: 21794
otero_key: "CXV7G3SH"
title: "A decision support system for electric utilities: compliance with Clean Air Act"
authors: "Parviz Ghandforoush; Tarun K Sen; Michael Wander"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00056-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for electric utilities: compliance with Clean Air Act

Parviz Ghandforoush <sup>a,)</sup>, Tarun K. Sen <sup>a</sup>, Michael Wander <sup>b</sup>

<sup>a</sup> Pamplin College of Business, Virginia Polytechnic Institute and State UniÕersity, 7054 Haycock Road, Falls Church, VA 22043, USA <sup>b</sup> Federal Energy Regulatory Commission, 888 First Street, Washington, DC 29426, USA

Accepted 2 September 1999

## Abstract

The Clean Air Act CAA Amendments established an absolute national limit for sulfur dioxideŽ . $( \mathrm { { S O } } _ { 2 } )$ emissions by the year 2000. The Act is based on a market-oriented system under which power plants will be granted ‘emission allowances’, each of which grants the right to emit a ton of $\mathrm { S O } _ { 2 }$ into the atmosphere. Utilities that reduce their emissions below their allocated allowances may sell the additional allowances in what will presumably be a developing market. Utilities are free to choose how to comply with the Act, but a few generally recognized options are likely to form the basis for compliance strategies. While the options are known, the costs of implementing the options are not known with certainty. Each utility will need to determine the lowest cost, most effective strategy given its current configuration and generation requirements. The compliance strategy decision must also be presented and defended to the appropriate Public Utility Commission PUC . ThisŽ . paper outlines a prototype decision support system DSS using an optimization engine integrated with a database to help aidŽ . utilities in making decisions regarding their compliance strategy. This DSS was created specifically with a mid-western utility company in mind; however, it is generic enough to be useful to any utility. The results obtained using the DSS are very encouraging. The decisions supported by it are consistent with those offered by experts in the industry. The DSS promises to be a very useful tool for strategic planning related to CAA compliance. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: DSS application; Electric utilities

## 1. Introduction

The driving force behind the development of this decision support system DSS is a legislated regula- Ž . tory change. The Environmental Protection Agency Ž . Ž . EPA , under the Clean Air Act CAA Amendments of 1990, has been given the authority to grant sulfur dioxide $( \mathrm { { S O } } _ { 2 } )$ emission allowances to every electric utility in the nation. Each ‘allowance’ granted to a utility represents the right to emit a ton of ${ \mathrm { S O } } _ { 2 }$ into the atmosphere. The total number of allowances issued by the EPA will be approximately 8.9 million in the year 2000. National $\mathrm { S O } _ { 2 }$ emissions of 8.9 million tons<sup>r</sup>yr would represent a 10-million ton reduction in emissions from 1980 levels 7 .<sup>w</sup> <sup>x</sup>

Utilities will have to reduce their emissions to an equivalent rate of 1.2 lb $\mathrm { S O } _ { 2 } /$ million BTU of fuel use. Many utilities are already in compliance and will be granted a sufficient amount of allowances to continue to operate power plants as they are now doing. Other utilities approximately 2000 will haveŽ . to either reduce their $\mathrm { S O } _ { 2 }$ emissions or obtain additional emission allowances. A key provision of the Act allows utilities to buy and sell allowances within their systems 12 .<sup>w</sup> <sup>x</sup>

Utilities emitting more $\mathrm { S O } _ { 2 }$ than allowed will be required to pay a specified fee per ton of excess $\mathrm { S O } _ { 2 }$ and to offset the excess in the following year. It is widely expected that the fees to be levied by the EPA will be greatly in excess of even the most expensive pollution abatement alternatives. Therefore, non-compliance with the CAA Amendments of 1990 by taking no action is not considered a viable option.

The EPA is not regulating how utilities choose to comply with the Act, but it is generally recognized that their major options include the following:

<sup>Ø</sup> retrofitting existing coal-fired units with fuel-gas desulfurization units FGDs or some other pollu-Ž . tion control technology;

<sup>Ø</sup> switching to fuel with a lower sulfur content;

<sup>Ø</sup> purchasing additional allowances required for compliance;

<sup>Ø</sup> modifying plant dispatching using units withŽ lower emission rates more intensively and units with higher emission rates less intensively in order to meet total electrical generation needs ..

The decision-makers who will determine what course of action to propose to the Public Utility Commission PUC will be the utility management.Ž . Supporting them in this decision-making process are the strategic planners. They must be able to configure their units, make estimates of relevant external parameters, project costs for different alternatives, and make recommendations that can be justified — both to management at the utility and to the PUC. The proposed DSS would support these planners in this process.

The DSS is being developed primarily with the profile of a typical utility strategic planner in mind. Generally, these planners are engineers who have worked their way up through the business, and are sophisticated users of computer systems and models. To support these users, the DSS should be designed to be, above all, logical and clear. The emphasis must be on ensuring that the system has an obvious logical flow to support users in supplying information, running the models, and interpreting the results. These planners need to understand the models being used, and have a desire to clearly understand the effect of the parameters being supplied on the results generated by the model. This helps to justify their actions to the PUC.

A survey of the literature that follows indicated no existing DSS that help utility planners comply with the CAA. Although the DSS proposed in this paper will not replace human decision-making, it is capable of increasing the quality of their decisions. One of the reasons why a DSS may not exist in the CAA compliance strategy planning is the complexity of using mathematical programming techniques. This paper illustrates how different software packages can be integrated to develop effective DSS.

The DSS integrates a relational database management system DBMS with an integer linear pro-Ž . gramming ILP model. The database interfaces with Ž . external corporate and government databases. The DSS supports several stages of model management: model formulation, model representation, and model solution with a solver interface. Results from the ILP solution can be fed back into the DBMS for user retrieval.

## 2. The DSS architecture

The proposed DSS is made up of several components: a DBMS, a model solution component, and a user interface for the system 3,16 . Fig. 1 illustrates<sup>w</sup> <sup>x</sup> how these components work together in this DSS model. The individual components are described below.

## 2.1. The database

This DSS requires extensive information support from a DBMS 6 . The database module provides<sup>w</sup> <sup>x</sup> several data management functions required to administer the DSS. The DSS database is a distributed database with some components internal to the DSS and others external to it. External to the DSS are utility MIS databases that may be drawn upon to supply the utility configuration information CON-Ž

![](/api/attachments/CXV7G3SH/fulltext/images/efd0839988052def38742d04870d3db1634017b6aa8855b63a3b2e8ffa6d64b0.jpg)  
Fig. 1. The DSS architecture.

FIGS and some decision parameters PARAMS .. Ž . For utility systems to comply with the CAA, the decisions must be made at the individual power-generating unit level. Each utility consists of multiple plant sites and each plant site has multiple powergenerating units numbering in the hundreds, of which coal-fired generating units are in the tens. Each generating unit has unique characteristics and therefore unique coefficients in the ILP formulation. The data required to support this DSS is therefore at two levels: utility and power-generating units. Such data is already available in the DOE and utility MIS databases and have been used in this study.

Part of the database is completely internal to the DSS, which is customized to support the DSS with information needed by the compliance strategy decision-maker. In order to use the DSS, the user must load the internal database. This process can be accomplished via two methods: 1 extraction of dataŽ . from external databases into files readable by the DSS; or 2 operator data entry. The DSS userŽ . interface described later provides menu options forŽ . either method of data loading.

The entity relationship ER model for theŽ . database is shown in Fig. 2. The associated relational tables are shown in Fig. 3. The ER model shows the hierarchical organization of the utility companies, their power plants, and associated generating units. The scenario entity indicates the different choices related to compliance that the organization has at the utility and power-generating unit level. The relationships, S-UNIT and S-UTIL, have data related to the model parameters, some obtained from external databases and some are generated by the ILP model.

![](/api/attachments/CXV7G3SH/fulltext/images/20c748d54d0db9ce0ce647ac878fccc1bbe171d90d7a34bdc3759040c285f1be.jpg)  
Fig. 2. ER model for the DSS.

<table><tr><td>PLANTS</td><td colspan="2"></td></tr><tr><td rowspan="2">Plant Identifier PLANTID</td><td>Plant Name</td><td>Plant Type</td></tr><tr><td>PLNTNAME</td><td>PLNTTYPE</td></tr><tr><td>2857</td><td>Edgewater</td><td>O</td></tr><tr><td>2858</td><td>Gorge</td><td>D</td></tr></table>

<table><tr><td>UNITS</td><td colspan="3"></td></tr><tr><td>Utility Code</td><td rowspan="2">Plant Identifier PLANTID</td><td rowspan="2">Boiler Number BOILERNO</td><td>Unit Name</td></tr><tr><td>UTILCODE</td><td>UNITNAME</td></tr><tr><td>13998</td><td>2857</td><td>11</td><td></td></tr><tr><td>13998</td><td>2857</td><td>12</td><td></td></tr><tr><td>13998</td><td>2857</td><td>13</td><td></td></tr></table>

![](/api/attachments/CXV7G3SH/fulltext/images/29a7ab7b3ea173c2ec62271a1be0accf83987161c1c24c5d7059e0f975d2e0d7.jpg)  
Fig. 3. The relational tables.

## 2.2. The model solution

The model base is an ILP model that generates an optimal compliance strategy and determines the total cost under that strategy. This model utilizes the parameters supplied by the user in the DBMS component, and generates results which are stored back in the database.

Execution of commands to the ILP model is directed through the dialog system with user commands also entered using the ILP software menus. The model integration function is performed by the DBMS software by linking the input parameters in the database and the ILP model scenarios.

## 2.2.1. Background of ILP model

Many of these ILP models are complex in nature, making them difficult to apply and difficult to use <sup>w</sup> <sup>x</sup> 17 . As a result, there is currently no existing DSS that incorporates any of these ILP models in a user-friendly manner. The application of mathematical programming techniques to electric power generation and planning can be found in the state of the art papers by Anderson 2 , Noonan and Giglio 9 ,<sup>w x</sup> <sup>w x</sup> and Peschon and Jamoulle 10 . These research stud-<sup>w</sup> <sup>x</sup> ies are aimed at either minimizing the operating costs of power plants or optimizing capacity expansion and investments in electrical generating facilities. The plant expansion problem is concerned with finding an optimum balance between economies of scale and the opportunity cost of excess capacity. Optimization methods used to solve such electric power plant problems fall into three categories.

The first category includes large-scale linear programming models 2 that cannot deal with economies<sup>w</sup> <sup>x</sup> of scale such as plant size and plant mix. The second category is comprised of models that take into account economies of scale and only consider the deterministic aspects of plant sizing decisions. These models use a mixed-ILP approach for their solution <sup>w</sup> <sup>x</sup> 9 . The third category consists of models that consider both economies of scale and the stochastic nature of power-generating plants. These models are typically solved using network and non-linear programming algorithms 13 . Since these algorithms <sup>w</sup> <sup>x</sup> lack computational efficiency in solving large-scale problems, their use has been limited only to solving small prototype problems. Otherwise, simulation techniques have been developed to obtain solutions to large problems with stochastic properties 14 .<sup>w</sup> <sup>x</sup>

In this study, we develop a mixed-ILP model to determine the optimal cost of compliance with CAA. The decision variables in this model include the decision of operating a specific generating unit with a particular scrubbing mode and coal type, the amount of output generated by each generating unit, and the number of allowances purchased or sold. The integrality condition associated with several of the decision variables necessitates a mixed integer linear model formulation.

## 2.2.2. Model assumptions

The real compliance strategy decisions are complex and involve many quantifiable factors. In order to build a prototype model, several key simplifying assumptions are made.

Ž . 1 The utility manager considers only coal-fired units in evaluating compliance strategies. Nationally, coal-fired units are responsible for 95% of all $\mathrm { S O } _ { 2 }$ from electric utilities 4 .<sup>w</sup> <sup>x</sup>

Ž . 2 Utilities would not substitute alternate fuels for coal-fired units as a result of the CAA. This assumption was supported by the analysis conducted by the EPA for the US Congress 1 .<sup>w</sup> <sup>x</sup>

Ž . 3 Each individual generating unit would have to meet a specific demand requirement. In reality, the generating unit’s power generation would probably be varied as part of a utility’s compliance strategy. In a fully implemented DSS the user would be able to eliminate this assumption.

Ž . 4 The option to buy or sell electric power from other utilities or non-utility generators would be dominated by economic considerations other than compliance with the CAA. Coal-fired generations are used for base-load and intermediate-load power generation. A utility’s decisions related to purchasing power, implementing conservation policies, and demand-side-management programs are generally based upon its peak-load requirements.

Ž . 5 The model is designed to support the development of a compliance strategy based on existing capacity only. The fully implemented DSS would allow for the inclusion of capacity expansion planning. It is not expected that the CAA will significantly affect the fuel choices for base-load capacity expansion in the future 1 .<sup>w</sup> <sup>x</sup>

The utility manager’s decision-making process in choosing a strategy for complying with the CAA is driven by proper estimation of the model parameters. These variables parameters are generally known or can be estimated with some certainty through engineering studies. Some of the generating unit level parameters, such as the cost of retrofitting a unit with an FGD scrubber may be fairly uncertain. The other key parameters, the fuel price actually the differen-Ž tial price between high- and low-sulfur coal , and the. future market value of an emission allowance, can be estimated with even less certainty.

## 2.2.3. The ILP model

An ILP model is formulated to find the optimal compliance strategy options for an electric utility given a single set of parameter estimates. The following exposition provides a mathematical statement of the model.

2.2.3.1. Definitions. Let, i is the index for powergenerating unit, where i <sup>s</sup> 1, . . . , n; j is the index for scrubbing mode, j<sup>s</sup>u means unscrubbed, j<sup>s</sup>s means scrubbed; k is the index for coal type, k<sup>s</sup>L means low sulfur, k<sup>s</sup>H means high sulfur.

2.2.3.2. Parameters. $C _ { i j k }$ is the cost of operating unit i with scrubbing mode j, and coal type k per unit output. This includes cost of coal. B is the total retrofit expenditure allowed. $A _ { i j k }$ is the price of allowance for generating unit i, scrubbing mode $j ,$ and coal type k. $G _ { i }$ is the generating requirement of unit i Ž . in megawatt hours . $f _ { i }$ is the capacity factor for unit i Ž . 8760 h<sup>r</sup>yr . $r _ { i j k }$ is the $\mathrm { S O } _ { 2 }$ emission rate of unit i, scrub mode $j ,$ and coal type k. E is the emissions allowed. $X _ { \mathrm { M I N } i j k }$ is the minimum allowable operating capacity of unit i in configuration $j ,$ k. $X _ { \mathrm { M A X } i j k }$ is the maximum allowable operating capacity of unit i in configuration $j ,$ k.

2.2.3.3. Decision Õariables. $Y _ { i j k }$ is equal to 1 if generating unit i is operated in j scrubbing mode, with coal type k and equal to 0 if otherwise. $X _ { i j k }$ is the output in megawatts of unitŽ . i, scrubbing mode $j ,$ and coal type k.  is the number of allowances purchased. $\rho$ is the number of allowances sold.

2.2.3.4. ObjectiÕe function. The objective of the ILP model is to minimize the total annual cost of operation, including the cost of allowances purchased and sold.

$$
\operatorname{Min} \sum_ {i} \sum_ {j} \sum_ {k} \left(C _ {i j k} X _ {i j k}\right) + A _ {i j k} \eta - A _ {i j k} \rho\tag{1}
$$

This includes the total fuel costs high- and low-Ž sulfur coal . Minimization of this function will result. in an optimal solution, but the actual value of the function does not represent the compliance cost. Its value must be adjusted by subtracting the high-sulfur fuel costs only the low-sulfur price premium isŽ attributable to the costs of the compliance . In prac-. tice, the non-CAA related fuel costs are determined by using the low-sulfur price thus eliminating the Ž price premium and then solving the optimization. model. The result represents the fuel costs which are independent of the compliance strategy.

2.2.3.5. Generation constraints. The generation constraints expressed in megawatt hours ensures sufficient power is generated to meet expected generation requirements. These requirements are determined by the user’s capacity factor selection $f _ { i } .$

$$
\sum_ {j} \sum_ {k} f _ {i} X _ {i j k} \geq G _ {i}; i = 1, \dots , n\tag{2}
$$

2.2.3.6. Emissions constraint. The emissions constraint ensures that the total utility ${ \mathrm { S O } } _ { 2 }$ emissions plus the net purchases of allowances do not exceed the allowances granted to the utility by the EPA.

$$
\sum_ {i} \sum_ {j} \sum_ {k} r _ {i j k} X _ {i j k} + \eta - \rho \leq E\tag{3}
$$

2.2.3.7. Capacity constraint. The capacity constraint is formulated to limit production up to the total capacity.

$$
\begin{array}{l} X _ {\text {MINijk}} Y _ {i j k} \leq X _ {i j k} \leq X _ {\text {MAXijk}} Y _ {i j k}; i = 1, \ldots , n; \\ j = u, s; \\ k = L, H \end{array}\tag{4}
$$

2.2.3.8. InÕestment constraint. We impose a limit on total retrofit expenditure by formulating the investment limit constraint.

$$
\sum_ {i} \sum_ {j} \sum_ {k} C _ {i j k} Y _ {i j k} \leq B\tag{5}
$$

2.2.3.9. Operational constraints. This constraint ensures that every generating unit operates under a specific scrubbing mode with a certain coal type.

$$
\begin{array}{l} \sum_ {i} \sum_ {k} Y _ {i j k} = 1;   j = u \text { or } s \\ X _ {i j k} \geq 0 \\ Y _ {i j k} \in \{0, 1 \} \end{array}\tag{6}
$$

The proposed decision model is solved using LINDO 15 . This mathematical programming soft-<sup>w</sup> <sup>x</sup> ware package was chosen because of its computational efficiency in solving binary integer programming problems similar to the one described above. A typical utility’s input to LINDO could involve 18 plants with 50 power-generating units. Each generating unit has the option to choose unit level capacity, low-sulfur coal, high-sulfur coal, and the number of allowances purchased and sold. Thus for a typical utility, the proposed model formulation could have approximately 4500 parameter cell entries.

## 2.3. The user interface

Realizing that the a key to successful use of the DSS is the user interface 8 , a major portion of the<sup>w</sup> <sup>x</sup> overall effort has gone into the design and implementation of the user interface for this DSS. We have attempted to make the user interface as simple as possible. Most user selections are performed using menus.

The DSS is designed to support relatively novice users by providing easy-to-use menus, pre-formatted data displays, and forms for data input. Errors are color-highlighted to quickly point out problems.

The user interface supports the following data management and modeling functions.

Ž .1 Load utility configuration Transfers data from an external file into internal utility, plant, and unit configuration tables.

Ž . 2 Enter utility configuration An alternative to 1; collects input from user on utility, plant, and unit configuration through screens.

Ž . 3 Load scenario Transfers utility and unit level parameter data from an external file into internal scenario tables.

Ž . 4 Choose scenario Utilizes a directory table of available scenarios that are stored.

Ž . 5 Copy scenario Copies a scenario from the directory table into the utility and unit-level parameter tables.

Ž . 6 Delete scenario

Deletes a scenario.

Ž . 7 Enter scenario parameters Directly enters pa - rameter values from users and stores it in the utility and unitlevel parameter tables.

Ž .8 Submit scenario to ILP Retrieves the cur - rent scenario and copies it into a format useable by an external translator program.

Ž . 9 Collect results

Ž . 10 Tabular reports

Retrieves model re - sults and stores in tables.

Retrieves requested data and utilizes DBMS reporting capabilities to generate reports.

Ž . 11 Graphics Retrieves requested data and turns it over to an external program to generate graphs.

Some of the DSS design screens are shown in Figs. 4–6. The database was created using dBASE III<sup>q</sup> and the optimization programs were run using LINDO. The interface between the database and

5 - Collect LP Results

![](/api/attachments/CXV7G3SH/fulltext/images/a66a460cfee2ec1cc014d7072dfbf69f177af8a6deee391f1f0cf42f7adea781.jpg)  
Fig. 4. Main menu.

![](/api/attachments/CXV7G3SH/fulltext/images/a3f62b904cc265c1da60d10f6014bb275e22b0c9ce2505b7787c1d0ecd809d4a.jpg)  
Fig. 5. Utility level parameters input screen.

LINDO was created using a dBASE III<sup>q</sup> program that took ASCII output from LINDO and loaded the database. Similarly, the program extracted data from the database and used it as input for LINDO. The system was developed as a prototype. Since we use a relational DBMS, the prototype can be extended to any RDBMS platform.

![](/api/attachments/CXV7G3SH/fulltext/images/c0239bf7a8616f6f867ffd4251dd7a01cadcd79dc88267927f9f5553133f4765.jpg)  
Fig. 6. Unit level parameters input screen.

The main menu shows the major tasks that can be accomplished. Using this menu, the utility and power plant data bases can be loaded, parameters of the scenarios can be developed, the ILP model can be processed, the data from the ILP model can be returned back to the system, and the reports and graphs can be reviewed. Most of these operations can be performed using a mouse.

## 3. Results and model validation

The proposed model was validated by testing the DSS on eight utility operations. Information on preliminary utility compliance strategies was collected from utility trade literature. While a number of preliminary announcements were reviewed, only a select group contained generating unit specific details which were needed to compare the preliminary strategies against least cost compliance strategies developed using the DSS.

Table 1 summarizes the eight utilities CompaniesŽ A–H for which generating unit level compliance. strategies were obtained. The strategies were often broken down by actions to be undertaken to meet phases I or II of the CAA. Phase I allowances, generally targeted at the dirtiest coal-fired power plants, will only affect a small subset of the nation’s utilities. Phase II allowances will be issued to every utility in the nation. For the purpose of comparing preliminary compliance plans and results of the DSS, capital investments to meet phase I plans were assumed to be part of phase II compliance strategies. The cost estimates, unless otherwise specified, were assumed to represent estimates of the costs of compliance throughout the useful life of the plant.

In order to use the DSS to analyze these utilities’ compliance plans, data had to be collected on all these utilities from a number of sources. Boiler-unit level data on fuel consumption, generating unit capacity, and fuel process were obtained from publications 5,11 . Data required by the DSS to model <sup>w</sup> <sup>x</sup> compliance decisions, such as the generating unit efficiencies and maximum capacity factors and reserve margins had to be estimated. The EPA emission allowances also were estimated based upon the assumption of 1.2 lb $\mathrm { S O } _ { 2 } / \mathrm { m m }$ BTU per generating unit 17 .<sup>w</sup> <sup>x</sup>

Table 1 Utility profiles

<table><tr><td>Utility</td><td>Description of unit level strategy</td><td>Estimated compliance cost</td></tr><tr><td>Company A</td><td>Planned to retrofit three units. They would excess allowances generated to bring the entire system into compliance.</td><td>US$725 million</td></tr><tr><td>Company B</td><td>Announced four potential options which vary slightly. All phase II compliance strategies called for retrofitting one station and switching to low-sulfur coal at up to 10 other unspecified units.</td><td>US$4105–4501 million</td></tr><tr><td>Company C</td><td>Retrofit two units.</td><td>US$100 million</td></tr><tr><td>Company D</td><td>Switch to low-sulfur coal.</td><td>US$20–50 million over 10 years</td></tr><tr><td>Company E</td><td>Retrofit four units. Switch to low-sulfur coal at others.</td><td>US$675 million</td></tr><tr><td>Company F</td><td>Retrofit two units. Switch to low-sulfur fuel at others.</td><td>US$300 million</td></tr><tr><td>Company G</td><td>Retrofit two units and change to low-sulfur fuel at others.</td><td>US$250–300 million</td></tr><tr><td>Company H</td><td>Retrofit all coal-fired units — overcomply and trade excess allowances</td><td>US$1.6 billion for 10 years</td></tr></table>

All utilities in this study plan to use the primary compliance strategies of either switching to lowsulfur coal or retrofitting units with FGD units. In general, these plans call for a mixture of retrofitting units with scrubbers and switching other units to low-sulfur coal. The extremes are represented by Company H which plans to retrofit all coal-fired units and to generate excess emission allowances which it will then sell, and Company D which intends to switch all its units to low-sulfur coal.

## 3.1. Analyzing the results

In assessing the DSS results, it is important to consider a number of factors. First, many of the parameters estimated were not known with certainty by the utility planners themselves. Others, which were known by the utility planners, were not available and therefore had to be estimated. The estimated parameters were always kept within the acceptable range.

The DSS ILP model does not capture the ‘hoarding’ of allowances by utilities who are projecting the need for increased capacity to meet rising demand, and the future market price increases of allowances. In reviewing the results, it is important to recognize that there are undoubtedly cases where real economic circumstances, not modeled in the DSS, exist, and which are significantly affecting the results. In general, the market parameters, such as the purchase and sales price of an allowance, have been adjusted within the acceptable range in an attempt to replicate the least-cost strategies of the utilities.

For each of the utilities, using the DSS, costs of compliance were computed Table 2 . These wereŽ . compared against estimates that the utilities have published. In several cases except utilities A, B, andŽ H the cost estimates are reasonably close. The . deviations in costs for utilities A, B, and H are primarily due to additional or less compliance workŽ . being done by these utilities. This indicates that the DSS decisions closely resemble actual decisions made by utility planners. This strongly supports the effectiveness of such a DSS.

Another measure shown in Table 2, indicates how the DSS’ recommendation for retrofitting and fuel grade choices matched with the utility’s actual plans Ž . Table 1 . Except for utilities A, B, and H, the DSS recommendations matched the utilities’ strategies. This is also a strong endorsement of the quality of the ILP model embedded in the DSS.

Another powerful feature of the DSS is its ability to perform sensitivity analyses, as illustrated by the ILP results shown in Fig. 7. The DSS allows the user to interactively perform repeated ‘what if’ analyses to develop the least-cost compliance strategy over a range of assumptions on any variable of interest, such as the price of an allowance or the differential between high- and low-cost sulfur coal. The user can easily set up new trials and store the results of previous ones, with the ultimate goal of making a quality decision. In addition, comparison graphics can be generated, as shown by the graph in Fig. 8.

These validations indicate that in most cases the DSS’ recommendations are justifiable. Those that are not can be explored further by experts in the utilities.

Table 2  
Summary of results using DSS

<table><tr><td>Utility</td><td>DSS compliance cost</td><td>Utilities estimated compliance cost</td><td>No./% of retrofit decisions correctly made by DSS</td><td>No. of units</td></tr><tr><td>A</td><td>1375</td><td>725</td><td>13/17</td><td>17</td></tr><tr><td>B</td><td>2250</td><td>4100</td><td>15/19</td><td>19</td></tr><tr><td>C</td><td>113</td><td>100</td><td>100%</td><td>5</td></tr><tr><td>D</td><td>100</td><td>20–50</td><td>100%</td><td>10</td></tr><tr><td>E</td><td>600</td><td>675</td><td>100%</td><td>19</td></tr><tr><td>F</td><td>250</td><td>250–300</td><td>100%</td><td>10</td></tr><tr><td>G</td><td>307</td><td>250–300</td><td>100%</td><td>10</td></tr><tr><td>H</td><td>548</td><td>1600</td><td>13/18</td><td>10</td></tr></table>

<table><tr><td colspan="6">SUMMARY OF LP RESULTS - GENERAL PUBLIC UTILITIES (COMPLIANCE COSTS)</td></tr><tr><td colspan="2">OBJECTIVE FUNCTION VALUE (mm $)</td><td colspan="4">624.585</td></tr><tr><td colspan="2">LOW SULPHUR COAL CONSUMED (TRILLS)</td><td colspan="4">22.638</td></tr><tr><td colspan="2">LOW SULPHUR COAL PRICE ($/MMBTU)</td><td colspan="4">1.80</td></tr><tr><td colspan="2">HIGH SULPHUR COAL CONSUMED (TRILLS)</td><td colspan="4">196.784</td></tr><tr><td colspan="2">HIGH SULPHUR COAL PRICE ($/MMBTU)</td><td colspan="4">1.50</td></tr><tr><td colspan="2">NUMBER OF ALLOWANCES PURCHASED</td><td colspan="4">0.</td></tr><tr><td colspan="2">ALLOWANCE PURCH. PRICE($TOM SO2)</td><td colspan="4">300.</td></tr><tr><td colspan="2">NUMBER OF ALLOWANCES SOLD</td><td colspan="4">459278.</td></tr><tr><td colspan="2">ALLOWANCE PURCH. PRICE($TOM SO2)</td><td colspan="4">-300</td></tr><tr><td colspan="6">UNIT LEVEL FUEL/DISPATCH/RETROFIT DECISIONS (MW):</td></tr><tr><td>PLANT NAME</td><td>UNIT#</td><td>LOW SULF W/OUTFGD</td><td>HIGH SULF W/OUTFGD</td><td>LOW SULF W/FGD</td><td>HIGH SULF W/FGD</td></tr><tr><td>PORTLAND</td><td>1</td><td>.0</td><td>.0</td><td>.0</td><td>134.2</td></tr><tr><td>PORTLAND</td><td>2</td><td>.0</td><td>.0</td><td>.0</td><td>206.4</td></tr><tr><td>TITUS</td><td>1</td><td>68.8</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>TITUS</td><td>2</td><td>67.1</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>TITUS</td><td>3</td><td>68.8</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>CONEMAUGM</td><td>1</td><td>.0</td><td>.0</td><td>.0</td><td>722.1</td></tr><tr><td>CONEMAUGM</td><td>2</td><td>.0</td><td>.0</td><td>.0</td><td>722.1</td></tr><tr><td>HOMER CITY</td><td>1</td><td>.0</td><td>.0</td><td>.0</td><td>526.7</td></tr><tr><td>HOMER CITY</td><td>2</td><td>.0</td><td>.0</td><td>.0</td><td>521.6</td></tr><tr><td>HOMER CITY</td><td>3</td><td>.0</td><td>.0</td><td>.0</td><td>552.2</td></tr><tr><td>SEWARD</td><td>12</td><td>51.0</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>SEWARD</td><td>14</td><td>.0</td><td>.0</td><td>.0</td><td>115.5</td></tr><tr><td>SEWARD</td><td>15</td><td>.0</td><td>.0</td><td>.0</td><td>339.8</td></tr><tr><td>SHAWVILLE</td><td>1</td><td>.0</td><td>.0</td><td>.0</td><td>209.8</td></tr><tr><td>SHAWVILLE</td><td>3</td><td>.0</td><td>.0</td><td>.0</td><td>297.3</td></tr><tr><td>WARREN</td><td>1</td><td>37.4</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>WARREN</td><td>2</td><td>37.4</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>KEYSTONE</td><td>1</td><td>.0</td><td>.0</td><td>.0</td><td>722.1</td></tr><tr><td>KEYSTONE</td><td>2</td><td>.0</td><td>.0</td><td>.0</td><td>722.1</td></tr><tr><td colspan="6">SUMMARY OF LP RESULTS - GENERAL PUBLIC UTILITIES (BASE COSTS)</td></tr><tr><td colspan="2">OBJECTIVE FUNCTION VALUE (mm $)</td><td colspan="4">600.699</td></tr><tr><td colspan="2">LOW SULPHUR COAL CONSUMED (TRILLS)</td><td colspan="4">282.660</td></tr><tr><td colspan="2">LOW SULPHUR COAL PRICE ($/MMBTU)</td><td colspan="4">1.50</td></tr><tr><td colspan="2">HIGH SULPHUR COAL CONSUMED (TRILLS)</td><td colspan="4">136.762</td></tr><tr><td colspan="2">HIGH SULPHUR COAL PRICE ($/MMBTU)</td><td colspan="4">1.50</td></tr><tr><td colspan="2">NUMBER OF ALLOWANCES PURCHASED</td><td colspan="4">0.</td></tr><tr><td colspan="2">ALLOWANCE PURCH. PRICE($TOM SO2)</td><td colspan="4">300.</td></tr><tr><td colspan="2">NUMBER OF ALLOWANCES SOLD</td><td colspan="4">223141.</td></tr><tr><td colspan="2">ALLOWANCE PURCH. PRICE($TOM SO2)</td><td colspan="4">-300</td></tr><tr><td colspan="6">UNIT LEVEL FUEL/DISPATCH/RETROFIT DECISIONS (MW):</td></tr><tr><td>PLANT NAME</td><td>UNIT#</td><td>LOW SULF W/OUTFGD</td><td>HIGH SULF W/OUTFGD</td><td>LOW SULF W/FGD</td><td>HIGH SULF W/FGG</td></tr><tr><td>PORTLAND</td><td>1</td><td>134.2</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>PORTLAND</td><td>2</td><td>206.4</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>TITUS</td><td>1</td><td>68.8</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>TITUS</td><td>2</td><td>67.1</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>TITUS</td><td>3</td><td>68.8</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>CONEMAUGM</td><td>1</td><td>722.1</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>CONEMAUGM</td><td>2</td><td>722.1</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>HOMER CITY</td><td>1</td><td>526.7</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>HOMER CITY</td><td>2</td><td>521.6</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>HOMER CITY</td><td>3</td><td>.0</td><td>.0</td><td>.0</td><td>552.2</td></tr><tr><td>SEWARD</td><td>12</td><td>51.0</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>SEWARD</td><td>14</td><td>115.5</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>SEWARD</td><td>15</td><td>339.8</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>SHAWVILLE</td><td>1</td><td>209.8</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>SHAWVILLE</td><td>3</td><td>297.3</td><td>.0</td><td>.0</td><td>.0</td></tr><tr><td>WARREN</td><td>1</td><td>37.4</td><td>.0</td><td>.0</td><td>.0</td></tr></table>

Fig. 7. Summary of ILP results.

![](/api/attachments/CXV7G3SH/fulltext/images/1569228f4d6bdc8b95feffc322d78d9f7b758d981cf72235ee4daefde525d7d2.jpg)  
COST LOW  COST HIGH □ COST RETRO □ COST ALLOW  
Fig. 8. Comparison graph indicating cost structure for compliance.

## 3.2. Limitations

The DSS developed is a prototype only and it is aimed at:

<sup>Ø</sup> demonstrating to the user how a DSS can aid the utility manager’s compliance strategy development;

<sup>Ø</sup> facilitating the process of defining the system requirements; and

<sup>Ø</sup> shortening the development time and costs of a fully implemented system.

With the prototype, we can involve more users in the industry to review the DSS and suggest improvements. The current working prototype represents a basis for communications that will help utilities in clearly defining the strategic planner’s requirements.

The DSS needs to be integrated with the utility’s other computer-based strategic planning tools. For example, the utility’s capacity planning decisions Žwhich may come directly from a computer-based model should be incorporated into the DSS through . modules connected to databases. In addition, the DSS should support the option to use additional computer-based models to generate the parameters now entered by the user.

A number of simplifying assumptions were made in the development of the ILP component of the DSS. The fully implemented DSS should support alternate model formulations selected by the user. It is recognized, however, that only a limited number of formulations will be possible, and that many simplifying assumptions will still be required.

## 4. Conclusions

We have successfully developed a prototype DSS for an electric utility that clearly demonstrates support for the critical success factors that the utility must achieve in order to succeed in its mission. The DSS illustrates the potential for supporting the utility’s development of a strategy for complying with the CAA Amendments of 1990. We have also been able to directly support the utility’s need for a structured well-documented approach to developing that strategy.

The fully developed DSS would help the firm minimize the risk of not complying by providing sensitivity analyses and comparison graphics. This information indicates how much external unknowns would have to change before their strategy should change or before costs of the current strategy become prohibitively high.

The structured analysis approach provided by the a fully implemented DSS will help utility management to present and defend their strategies before the PUC. A fully developed system can also help to rapidly answer ‘what if’ questions posed by the PUC. This support will also help utilities develop proposals to the PUC.

One lesson learned in the development of this DSS is that a careful selection of ILP software must be made. The ILP software used in the prototype is computationally efficient in solving a large utility problem in a fully implemented DSS. The dialog system and DBMS should be carefully selected with an eye towards efficiency and user friendly interfaces. The development of DSS in assisting strategies related to the CAA should be continued. This prototype demonstrates the potential benefits that can be obtained from a fully implemented effectiveness of such DSS.

## References

<sup>w</sup> <sup>x</sup> 1 Analysis of H.R. 3030 Title V: Acid Deposition Control, Energy Information Administration, US DOE, November, 1990, pp. 1–35.

<sup>w</sup> <sup>x</sup> 2 D. Anderson, Models for determining least-cost investments

in electricity supply, Bell Journal of Economics and Management Science 3 1 1972 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 A.A. Baldwin, D. Baldwin, T. Sen, The evolution and problems of model management research, Omega 19 1991Ž . 511–528.

<sup>w</sup> <sup>x</sup> 4 Electric Power Annual 1989, Energy Information Administration, US DOE, 1989, pp. 76–77.

<sup>w</sup> <sup>x</sup> 5 Inventory of Power Plants in the United States, Energy Information Administration, US DOE, 1991.

<sup>w</sup> <sup>x</sup> 6 T.P. Liang, Integrating model management with data management in decision support systems, Decision Support Systems 1 1985 221–232.Ž .

<sup>w</sup> <sup>x</sup> 7 R. Lock, D.P. Harkawik, The New Clean Air Act: Compliance and Opportunity, Public Utilities Report, June, 1991.

<sup>w</sup> <sup>x</sup> 8 P. Ma, F.H. Murphy, E.A. Stohr, A graphics interface for linear programming, Communications of the ACM 32 1989 Ž . 996–1012.

<sup>w</sup> <sup>x</sup> 9 F. Noonan, R.J. Giglio, Planning electric power generation: a nonlinear mixed-integer model employing benders decomposition, Management Science 23 9 1977 .Ž . Ž .

<sup>w</sup> <sup>x</sup>10 J. Peschon, E. Jamoulle, An Integrated Set of Power System Planning Models, Paper presented at the Joint National ORSA<sup>r</sup>TIMS Meeting, Chicago, IL, 1975.

<sup>w</sup> <sup>x</sup> 11 Power Plant Deliveries Data for January–December, National Coal Association, 1997.

<sup>w</sup> <sup>x</sup> 12 J. Quarles, W.H. Lewis, Jr., The New Clean Air Act: A Guide to the Clean Air Program as Amended in 1990, Morgan, Lewis and Bockius, 1990, 39–44.

<sup>w</sup> <sup>x</sup> 13 S. Roger, A dynamic model for planning capacity extensions: an application to plant reliability and electric power systems, Department of Operations Research, Stanford University, 1970.

<sup>w</sup> <sup>x</sup> 14 C.R. Scherer, J. Leland, Electric power system planning with explicit stochastic reserves constraints, Management Science 3 9 1977 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 L. Schrage, LINDO: Linear, Interactive, and Discrete Optimizer, The Scientific Press, 1989.

<sup>w</sup> <sup>x</sup> 16 The Clean Air Act Amendments of 1990 Summary Materi-

als, US EPA, Office of Air and Radiation, November 15, 1990, pp. 5–7.

<sup>w</sup> <sup>x</sup> 17 W.L. Winston, Operations Research, Applications and Algorithms, PWS Kent Publishing, Boston, 1991.

Dr. Parviz Ghandforoush is Professor of Management Science and Information Technology at Virginia Polytechnic Institute and State University. He received his BSEE and MBA from the University of Texas at Austin and PhD in Operations Research from Texas Tech University. His current research interests are in web-based technologies, e-commerce, mathematical programming and decision analysis. He is the Co-Director of the Systems Integration Center and serves on the editorial board of Computers and Operations Research and IEEE transactions on Engineering Management. He has published numerous articles in journals including the NaÕal Research Logistics, IIE Transactions, Computers and Operations Research, INFORMS Journal on Computing, European Journal on Operational Research, International Journal of Production Research and others.

Dr. Tarun K. Sen is Professor of Accounting and Information Systems and Co-Director of the Systems Integration Center at the Pamplin College Of Business in Virginia Polytechnic Institute and State University. He received his PhD in MIS from the University of Iowa in 1985. His teaching and research interests are in database management systems, model management systems, neural network applications in financial prediction tasks and building decision support systems using data warehouses. His articles have appeared in Management Science, INFORMS Journal on Computing, Omega, IEEE Transactions on Systems Man and Cybernetics, Decision Support Systems and International Journal of Intelligent Systems in Accounting Finance and Management.

Michael Wander is a graduate of the MBA program at the Pamplin College of Business at Virginia Polytechnic Institute and State University. He has been with the Federal Energy and Regulatory Commission at Washington, DC. He is on the advisory board of the Pamplin College of Business MBA program.
