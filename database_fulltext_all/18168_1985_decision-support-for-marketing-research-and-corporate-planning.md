---
otero_id: 18168
otero_key: "GY3CWGJJ"
title: "Decision support for marketing research and corporate planning"
authors: "L.Douglas Smith; John Blodgett; Marius Janson; Vince Bartle"
year: "1985"
journal: "Information & Management"
doi: "10.1016/0378-7206(85)90043-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision Support for Marketing Research and Corporate Planning

L. Douglas Smith, John Blodgett, and Marius Janson

School of Business Administration, University of Missouri-St. Louis, St. Louis, MO 63121, U.S.A.

and

Vince Bartle

Director of Planning and Research, Shelter Insurance Companies, Columbia, MO, U.S.A.

Marketing research and corporate planning are enhanced by an effective decision support system. A system developed and implemented in an insurance company is used to illustrate how computer cartography and statistical procedures can be combined as powerful analytical tools. It also demonstrates how a nonprocedural language (SAS with SASGRAPH) can be used to create modules of systems that are efficiently implemented and easily maintained by analysts with limited programming capabilities.

Keywords: Decision Support System, DSS, Marketing Research, Corporate Planning, Nonprocedural Language

![](/api/attachments/GY3CWGJJ/fulltext/images/ba4d63274e1a0a6ec7747349c222df87dd25cc1acee9ce223655d8ac57c22f55.jpg)  
and displaying demographic data from a DIME geographic-base file.

L. Douglas Smith is an Associate Professor of Management Science and Information Systems and Director of the Center for Business and Industrial Studies at the university of Missouri-St. Louis. He holds a Ph.D. in Management Sciences from the University of Minnesota, and an M.B.A. and B.Sc. (Physics) from McMaster University. His articles have appeared in fifteen national or international professional journals. His research has emphasized the development of models and computer-based systems for the solution of managerial problems.

## 1. Introduction

Senior executives have articulated their perceptions of the primary value of management science for decision-making at higher levels in their organizations. They stress the importance of developing systems that assimilate information and present it in a way that encourages creative, free-form analysis. Borsting [3], Gratwick [6], and Studnicki-Gizbert [13], all emphasize the impor-

![](/api/attachments/GY3CWGJJ/fulltext/images/53f2b69b2f7d4af3aa0141c6632b34f8337a11e34b36d6c0cfdc5049bf8d452b.jpg)

John Blodgett is manager of the Urban Information Center at the University of Missouri-St. Louis. He holds an M.A. in Mathematics from Duke University and a B.A. in Mathematics from the University of Missouri-St. Louis. He has extensive experience in organizing and utilizing statistical databases with specific emphasis on the display of such data on computer-drawn maps. He is the author of GAPS (Geographic Area Profiling System), a SAS-based system used in organizing

![](/api/attachments/GY3CWGJJ/fulltext/images/8677bb7b58971e646bd9a33fb84681000f621ba315f382715ca402d4eddc2049.jpg)

![](/api/attachments/GY3CWGJJ/fulltext/images/e91af9445df804a52623c276ae7d8e11f549e87d7b57fd14125e682e0087b21c.jpg)

Marius A. Janson is an Assistant Professor of Management Information Systems at the University of Missouri-St. Louis. He holds a Ph.D. in Management Sciences from the University of Minnesota and a B.S. in Electrical Engineering from the Netherlands. Professor Janson has worked for N.V. Philips Gloeilampenfabrieken, The Netherlands, Honeywell, and Research, Inc. He performs research on prototyping and the use of statistics in management information systems.

Vincent M. Bartle is director of planning and research at Shelter Insurance Companies, Columbia, Missouri. He holds an M.A. in Accounting and a B.S. in Statistics from the University of Missouri-Columbia. he has served as Vice President and Treasurer for national Aviation Underwriters, has been chairman of the N.A.I.I. research committee, and is author of articles in the National Underwriter and Computer World.

tance of nonalgorithmic tools for this purpose. They are critical of a tendency in operations research to focus on the premature development of optimizing models and procedures that impose an excessive degree of structure on problems encountered in strategic planning.

On another front, management information systems are criticized for their lack of responsiveness to users' needs as they evolve. This deficiency springs from two sources: 1) organizational structures and procedures that cause the development and maintenance of management information systems to be done by specialists removed from the locus of planning activity, and 2) the use of computer languages and programming structures that meet specifications of a particular request for information and then require further computer programming to effect changes in the contents and formats of reports. Wasserman and Gutz [14] emphasize the importance of high-level languages that facilitate the production of prototypical reports and analysis by planning analysts. Sprague [12] and Barbosa and Hirko [2] stress the open-ended aspect of MIS development. Edelman [5] calls for a shift in responsibility for system development and maintenance from data processing professionals to user-analysts.

These criticisms of management science and information system suggest several desirable attributes of decision-support systems for strategic planning:

1. The presentation of information in a form that reinforces the analytical potential of individuals familiar with the business and encourages their involvement in the analysis.

2. The ability of analysts to shift flexibly among various levels of aggregation of information, alternatively reviewing the broad scope and "zooming in" on details to answer specific questions.

3. An evolutionary design in which the system can be changed readily as information is processed and managers' curiosity is aroused.

4. Computer software that enables individuals with limited technical capabilities to use and modify the system.

This paper describes a computer-based decision support system that was developed and implemented with the aforementioned philosophies and technical attributes as goals. The system integrates information about an insurance company's underwriting activities, market demographics, agency force, pricing decisions, promotional expenditures, and concentration of competition. Computer cartography is used in conjunction with various statistical models and procedures to review corporate performance, to portray geographical areas that satisfy particular criteria, and to identify areas that offer potential for new business. The software was created entirely in SAS (Statistical Analysis System) [8,9,10].

## 2. Corporate Environment

The system was developed for a regional insurance company with a concentration in personal lines (life insurance and property and casualty). The company serves a 13-state area in the lower midwest. At the outset of the project, the company used an IBM 3081 computer to maintain policyholder data and to perform standard accounting functions. Reports were generated to track levels and changes in premiums, number of policies, new business, lapse rates, loss frequency, loss severity, expense ratios, agency force and other summary measures of corporate performance for the different lines of insurance. Some reports were also generated to give breakdowns of the data for geographical areas that corresponded to the span of responsibility of managers (i.e., sales regions, states, and sales districts). A few reports gave data for individual agents.

The Director of Planning and Research had acquired an IBM 3279 terminal and an IBM 3287 color plotter/printer and had begun to experiment with SAS for generating colored maps of the marketing region to illustrate corporate statistics at the county level. He had also created a SAS database from data that appeared in many of the aforementioned reports. He was using SAS with SASGRAPH to study trends in written premiums, number of policies, premiums per policy, new policies generated, policy lapse rates, frequency of claims, severity of losses, policies per agent and profit contribution for various categories of business.

## 2.1. Motivation for the Project

The project arose from a desire to study the company's operations in relation to market opportunities and to structure analysis in terms of specific marketing decisions. A memo from the president of the company to the director of planning and research contained the following request:

“...The end product I am looking for is to define locations which will, with the smallest number of additional support personnel possible, provide substantial increases in business from existing or additional agents.

I want the end product to be placed on maps of our operating areas so we can see how the areas likely to produce additional quality business are related to our present operation....”

In addition, a newly-appointed vice-president of marketing was interested in the company's becoming “more scientific in the development and execution of marketing plans”.

To be served by the system, therefore, were three individuals. In increasing degree of computer literacy and decreasing levels of the corporate hierarchy (with no prejudice about any causal link between these two attributes), they were:

1) the president,

2) the vice president of marketing, and

3) the director of planning and research.

In summary, there were several important conditions that were favorable for the undertaking:

1) The project was initiated and supported by top management

2) The recent appointment of the vice-president of marketing provided an impetus for new procedures in marketing research and planning without the encumbrance of established procedures and patterns of communication, and

3) The necessary computer technology was already in place.

## 3. Design and Implementation of the System

The project was structured in four stages as follows:

1) Development of a database and information structures for analysis and generation of routine reports for marketing research and planning.

2) Development of a system for consolidating information about the company, its performance, and its business environment and presentation of information to managers in a form that encourages the generation of strategic decision alternatives.

3) Development and application of tools for statistical modeling and analysis to identify how various factors affect corporate performance and to help in the design of marketing experiments and promotional campaigns.

4) Development of corporate planning models that utilize information generated in the previous stages.

To date, the first three stages have been completed; the fourth stage has yet to be undertaken.

## 3.1. The Marketing Research Database

Summary data used for analysis and report generation are maintained in SAS databases. All programs in the system were written in SAS so that members of the planning department could maintain and modify them with relative ease. Two SAS databases were created to contain summary information from the company's detailed policy-holder files – one for the current year, the other for the previous year. Files from the two databases are merged for analysis. Demographic data from the U.S. Census summary file STF3A were extracted and placed into a dataset on the database for the current year. Coordinates of polygons for states, counties and sales districts were placed into projected SAS map datasets along with names of counties and names of places that would be used for labels on computer-generated maps.

Concentration of the agency force and average productivity of agency are maintained for the different geographical levels. For selected areas, the prices charged for typical policies by the 13 top insurers were compiled and placed on the database. Finally, summary data for savings and loan institutions were included for indications of changes in economic conditions. Table 1 outlines the contents of the basic marketing research database as it was originally established. The initial analysis consisted of exploratory research to determine the factors that best explain variations in corporate performance among geographical areas. Since then the database has been expanded to include a large number of statistics reflecting loss experience and characteristics of policies written. Separate summary files are created and maintained for the different levels of geographical aggregation according to the following hierarchy: 1) sales region, 2) state, 3) sales district, 4) county, 5) zip within county.

A series of SAS programs is executed in batch mode to create and update the database. Extrac-

Table 1
Examples of Data Maintained at Different Geographical Levels

```txt
Policyholder Data
-Recent year and previous year in separate datasets
-Merged for analysis
-Number of policies
-Policies per agent
-Total annualized premium
-Average annualized premium

Demographic Data
-Population
-Urban or non-urban
-Employed and unemployed
-Over 200% of poverty level
-Below 75% of poverty level
-Over 65 years of age
-Under 15 years of age
-College educated

-Number of Households
-With 1 vehicle
-With 2 vehicles
-With 3 or more vehicles

-Median Household Income

Mapping Data
-County Outlines
-District Outlines
-County Labels (Names)

Agent Data
-Agent count allocated to geographic divisions on basis of number of policies

Pricing Data
-Prices charged by 13 top insurers for typical policies

Economic Data
-Balances for savings and loans
-Deposits in banks and savings and loans
-Outstanding loans in banks and savings and loans
```

tions from the company's detailed policyholder files are performed twice yearly for updating via regeneration. Figure 1 illustrates the batch processing performed for this purpose. Policyholder data are integrated with the data from external sources and then summarized at the different geographical levels. For purposes of determining the concentration of the company's agency force, individual agents are “allocated” among counties in proportion to the number of policies they have there. They are also weighted by an index that reflects the expected level of production given the number of months of experience they possess.

## 3.2. Periodic Reports

As a byproduct of the updating process, comprehensive reports are produced which describe the current status of business activity in each geographical area, and the changes in status from the previous year. Table 2 provides an illustration of the report that presents the county business profile. Table 3 shows how a breakdown of business is provided for each agent operating in the county so that managers can identify the individuals responsible for business there. The “proportion of business in the county” refers to the proportion of the agent’s business that is derived from the county. Since each agent tends to have business in

![](/api/attachments/GY3CWGJJ/fulltext/images/08e8ef6ae5c6fe2109a3292a8e3139903475e2da74e9c96f1bbaacca1952b633.jpg)  
Fig. 1. Batch Processing to Generate Database and Produce Periodic Reports.

several counties, an agent business profile is also produced that reorganizes the information in Table 3 by individual agent. Table 4 contains an illustration of the agent business profile. These tables are provided to show the types of periodic reports which can be prepared routinely and which might be viewed as an end-product in a typical management information system.

The periodic reports contain data useful for conducting marketing reviews. Unfortunately they

Table 2
County Business Profile

<table><tr><td colspan="11">11:20 Friday, September 16, 1983SHELTER INSURANCE DATA FOR ALL AUTO POLICIESPOLICIES AS OF AUGUST, 1981MARKET SUMMARY REPORT SHOWING AUTO POLICY ACTIVITY WITH PENETRATION AND RANKS SUMMARIZED BY COUNTY</td></tr><tr><td colspan="11">REGION=EAST STATE=IL DISTRICT=01</td></tr><tr><td>COUNTY</td><td>ALLOCATED AGENT COUNT</td><td>NUMBER OF POLICIES</td><td>NPOLHLDR</td><td>TOTAL ANNUALIZED PREMIUMS</td><td>AVERAGE ANNUALIZED PREMIUM</td><td>POLICYHOLDERS PER 100 HOUSEHOLDS</td><td>EST#POLICIES PER 100 VEHICLES</td><td>EST PREMIUM PER 100 VEHICLES</td><td></td><td></td></tr><tr><td>Boone</td><td>1.7</td><td>1033</td><td>540</td><td>$ 158,262</td><td>$ 153.21</td><td>5.55</td><td>12.84</td><td>$ 1967.50</td><td></td><td></td></tr><tr><td>Carroll</td><td>1.9</td><td>989</td><td>502</td><td>$ 146,513</td><td>$ 148.14</td><td>7.18</td><td>14.21</td><td>$ 2104.41</td><td></td><td></td></tr><tr><td>DeKalb</td><td>1.1</td><td>736</td><td>384</td><td>$ 99,765</td><td>$ 135.55</td><td>8.64</td><td>19.49</td><td>$ 2641.87</td><td></td><td></td></tr><tr><td>JoDavies</td><td>2.1</td><td>1184</td><td>657</td><td>$ 233,273</td><td>$ 197.02</td><td>7.82</td><td>25.06</td><td>$ 4937.41</td><td></td><td></td></tr><tr><td>COUNTY</td><td>RANK AGENTS (ALLOCATED)</td><td>RANK NPOLS</td><td>RANK TOTPREM</td><td>RANK AVGPREM</td><td>RANK PHPERHH</td><td>RANK POLPERV</td><td>HOUSEHOLDS PER AGENT</td><td>POLICIES PER AGENT</td><td>ANNUALIZED PREMIUM PER AGENT</td><td>POPULATION PER AGENT</td></tr><tr><td>Boone</td><td>712</td><td>675.0</td><td>667</td><td>363</td><td>1115</td><td>1156</td><td>5,823</td><td>618</td><td>94,548</td><td>7,150</td></tr><tr><td>Carroll</td><td>883</td><td>787.0</td><td>782</td><td>397</td><td>941</td><td>982</td><td>3,678</td><td>518</td><td>76,794</td><td>4,594</td></tr><tr><td>DeKalb</td><td>411</td><td>921.0</td><td>912</td><td>423</td><td>836</td><td>870</td><td>4,041</td><td>648</td><td>87,867</td><td>4,769</td></tr><tr><td>JoDavies</td><td>985</td><td>597.5</td><td>576</td><td>297</td><td>897</td><td>827</td><td>4,002</td><td>565</td><td>111,258</td><td>3,448</td></tr><tr><td>COUNTY</td><td>AGENTS PER 10000 HOUSEHOLDS</td><td>RANK HHS PER AGENT</td><td>RANK POLICIES PER AGENT</td><td>RANK PREMIUMS PER AGENT</td><td>RANK PERSONS PER AGENT</td><td>RANK AGNTS PER 10000 HHS</td><td>HOUSEHOLDS</td><td>TOTAL POPULATION 1980</td><td>MEDIAN HOUSEHOLD INCOME</td><td></td></tr><tr><td>Boone</td><td>1.747</td><td>70</td><td>723</td><td>273</td><td>70</td><td>1128</td><td>9733</td><td>28,630</td><td>$20,729</td><td></td></tr><tr><td>Carroll</td><td>2.719</td><td>241</td><td>991</td><td>601</td><td>248</td><td>814</td><td>6989</td><td>18,779</td><td>$15,744</td><td></td></tr><tr><td>DeKalb</td><td>2.475</td><td>165</td><td>617</td><td>594</td><td>181</td><td>1091</td><td>4445</td><td>4,624</td><td>$ 8,345</td><td></td></tr><tr><td>JoDavies</td><td>2.499</td><td>193</td><td>816</td><td>153</td><td>353</td><td>1005</td><td>8404</td><td>23,520</td><td>$16,800</td><td></td></tr></table>

\*At the request of the company, the data in this table have been replaced with hypothetical data.

comprise hundreds of pages of output for automobile insurance alone. They are virtually impossible to digest and to place in proper perspective. The challenge of the project was to convert the data into useful managerial information, to provoke good questions, and to support the further analysis necessary to answer the questions expeditiously. The remaining sections of the paper describe the development of tools for these purposes.

Table 3
Breakdown of County Business by Agent

<table><tr><td colspan="7">SHELTER SALES DISTRICT =02 COUNTY = CLINTON</td></tr><tr><td>OBS</td><td>AGENT</td><td>Proportion of Policies this Year in County</td><td>Proportion of Policies last Year in County</td><td>No. of policies This Year in County</td><td>No. of policies Last Year in County</td><td>Percentage Change in Policies</td></tr><tr><td>36</td><td>Rodney, John P.</td><td>.43</td><td>.42</td><td>811</td><td>763</td><td>6.29</td></tr><tr><td>37</td><td>Snyder, Charles</td><td>.72</td><td>.70</td><td>1473</td><td>1391</td><td>5.89</td></tr><tr><td>38</td><td>Greer, George</td><td>.10</td><td>.10</td><td>97</td><td>113</td><td>-14.16</td></tr><tr><td>39</td><td>Baker, Gene</td><td>.11</td><td>.10</td><td>283</td><td>251</td><td>12.75</td></tr><tr><td colspan="7">SHELTER SALES DISTRICT =02 COUNTY = DAVIESS</td></tr><tr><td>OBS</td><td>AGENT</td><td>Proportion of Policies this Year in County</td><td>Proportion of Policies last Year in County</td><td>No. of policies This Year in County</td><td>No. of policies Last Year in County</td><td>Percentage Change in Policies</td></tr><tr><td>40</td><td>Graul, Max</td><td>.82</td><td>.81</td><td>1573</td><td>1554</td><td>1.22</td></tr><tr><td>41</td><td>Eads, Kenneth</td><td>.62</td><td>.59</td><td>1083</td><td>987</td><td>9.72</td></tr><tr><td>42</td><td>Schultz, John</td><td>.12</td><td>.12</td><td>251</td><td>269</td><td>-6.69</td></tr><tr><td>43</td><td>Miller, Terry</td><td>.32</td><td>.31</td><td>701</td><td>643</td><td>9.02</td></tr></table>

\*At the request of the company, the data in this table have been replaced with hypothetical data.

Table 4
Agent Business Profile

<table><tr><td colspan="11">SHELTER INSURANCE AUTO POLICY ACTIVITY REPORTAGENT ACTIVITY DISTRIBUTED AMONG COUNTIES 1981-82SERVICING/AGENT = ARNETT, HENRY</td></tr><tr><td>REGION</td><td>STATE</td><td>DIST.</td><td>COUNTY</td><td>Portion of Bus. in Co.</td><td>Previous Portion in Co.</td><td>Current # Policies Serviced</td><td>Previous Policies Serviced</td><td>% Change in # Policies Serviced</td><td>Current Total Premiums ($1,000)</td><td>Previous Total Premiums ($1,000)</td></tr><tr><td>West</td><td>AK</td><td>05</td><td>Jackson</td><td>.81</td><td>.80</td><td>4969</td><td>4761</td><td>4.37</td><td>916</td><td>875</td></tr><tr><td>West</td><td>NE</td><td>01</td><td>Other</td><td>.19</td><td>.20</td><td>763</td><td>812</td><td>-6.03</td><td>149</td><td>151</td></tr><tr><td>West</td><td>NE</td><td>01</td><td>Total</td><td>1.00</td><td>1.00</td><td>5732</td><td>5573</td><td>2.85</td><td>1066</td><td>1027</td></tr></table>

\*At the request of the company, the data in this table have been replaced with hypothetical data.

## 4. Development of the Management Information System

The first task in the further development of the system was to enable information of the type contained in the periodic reports to be obtained in a more meaningful form. Capabilities were needed to produce reports that are flexible in their content and format, to produce accompanying maps that give a good geographical perspective of the attributes being portrayed, and to allow managers to shift back and forth between a focus on the entire marketing area and a focus on some small segment of the marketing area.

## 4.1. Geographic Mapping and Reporting of Descriptive Statistics

Perhaps the most appreciated feature of the system is its ability to produce color-coded maps that present statistics by county or by sales district as desired. SAS with SASGRAPH enables this to be accomplished easily. Programming macros can be written, saved, invoked and altered interactively by the user. Macros written in the nonprocedural SAS language can thus provide users with outlines of computer programs which are easy to modify. Modifications can be effected dynamically by re-specifying macros that define key parameters for SAS procedures.

For example, a macro entitled “\_MAPIT”

contains the necessary instructions for generating maps covering all or part of the marketing area. Among these instructions are qualifiers of the SAS GMAP procedure that control the appearance of the map. These qualifiers themselves are defined in SAS macros. The user can redefine the following macros interactively when generating a map:

1) \_DATA to define the name of the dataset that contains the information (variable) to be mapped

2) \_MAPVAR to designate the variable whose value is to be represented on the map

3) \_TITLES to specify the title to be given to the map

4) \_MAPSPEC to define attributes of the plot such as midpoints of the ranges of values to be represented by each plotting symbol

5) \_SYMBOLS to redefine the color and form of the symbol used to represent the values specified in MAPSPEC.

Another macro can be invoked to direct the plot to a hard-copy plotter instead of producing it on the user's screen. Thus analysis can be performed at the terminal, prototypical maps and reports can be produced for perusal, and then hard-copy maps or reports can be directed to the company's IBM 3287 printer-plotter or laser printer at will. By subsetting the data set containing the variable to be mapped, the user can obtain maps of a portion of the geographic area magnified automatically to fill a page of the prescribed size. Figure 2 illustrates a map covering the 13-state marketing area by sales distract. Maps of subsets of the area are automatically "blown up" by SAS for detailed study.

![](/api/attachments/GY3CWGJJ/fulltext/images/76c9295db5967d9ed2d02a5c5da6f8bbcc956efe330010274da4f952106eb983.jpg)  
Fig. 2. Marketing Area by District.

Another mapping option enables the identification of counties that satisfy a number of criteria. Figure 3 is an example of a map that shows counties targeted according to combined criteria of: current agent productivity, current agent concentration, and hypothetical agent concentration if a new agent were added to the county.

![](/api/attachments/GY3CWGJJ/fulltext/images/0e81f744582729919c801a6460d505fbfdba65df668622dbef30ee5530f0f1b7.jpg)  
Fig. 3. Counties Selected According to Agent Productivity, Agent Concentration, and Concentration with an Additional Agent.

## 4.2. Maps with Labels

PROC GMAP does not currently provide support for the location of labels on maps. We therefore developed SAS software to expand the map dataset used by PROC GMAP to include pseudopolypgons defining symbols and characters that comprise the labels. Modules written in the new SAS macro language invoke PROC FSEDIT in order to allow the user to establish parameters for mapping similarly to \_MAPIT described earlier. They also enable the user to designate parameters that determine the size and angle of printed labels.

![](/api/attachments/GY3CWGJJ/fulltext/images/9fe6904c4813817c6e64bc7479bb4653fff0377d0be3b5aa1d294acef388a5d2.jpg)  
Fig. 4. Sales Districts with Labels of Cities.

A special places location file provided by Rand McNally was used to produce another SAS dataset that gives the labels for plotting, the geographical coordinates of the places for positioning the label, and other variables that allow the selection of places whose labels should appear (e.g., county, sales district, SMSA code, and population). Figure 4 provides an example of a map generated for Missouri that has labels for places satisfying certain selection criteria.

Reports are able to be generated with similar ease. With labels maintained on the SAS datasets to serve as headings for variables, reports are automatically formatted by SAS to fit into the space made available on a page.

By analyzing and comparing plots for three variables (market penetration, company agent concentration, and average agent productivity), new insight has been obtained about the company's marketing position and the mix of marketing strategies that should be considered for the generation of new business in individual counties. It has become much easier to view decisions involving and area in the context of the company's total marketing strategy and effort.

## 4.3. Relational Statistical Analysis

The next step in the development of the management information system was to establish tools that facilitate the construction, and use of explanatory statistical models to give guidance in strategic planning. The basic statistical model underlying the initial work used some measure of corporate

## Table 5

Examples of Variables used in the Early Development of Explanatory Statistical Models performance as the dependent variable. The explanatory (independent) variables included:

```txt
I. Variables Chosen for Preliminary Analysis of Corporate Productivity
1) Number of Policies
2) Total Annualized Premiums
3) Market Penetration (Policyholders per 100 households)
4) Growth in Policies (Percent change '81-'82)
5) Growth in Premiums (Percent change '81-'82)
6) Growth in Market Penetration (Percent change '81-'82)

II. Variables Chosen for Preliminary Analysis of Agent Productivity
1) Policies per allocated agent (August 1982)
-agents allocated to counties in proportion to their policy volumes
2) Annualized premium per agent (August 1982)
3) Growth in policies per agent (Percentage change Aug.'81-'82)
4) Growth in premium per agent (Percentage change Aug.'81-Aug.
'82)

III. Variable Chosen for Geographic Concentration of Agents
-(Agents per 10,000 households) allocated to counties on basis of premium dollars

IV. Variables Chosen to Represent Relative Prices of Standard Policies
1) Price as a percentage relative to the price of a policy from the major competitive company in the region
2) Price as a percentage relative to the average price of policies from the top three competitors in the region
3) Difference between the price charged by the company and the price charged by the major competitor
4) Difference between the price charged by the company and the average price charged by the top three competitors

V. Variables Chosen to Represent Demographic Attributes
1) Percentage of families with more than one car
2) Percentage of workforce employed
3) Percentage of population below 75% of the poverty levels
4) Percentage of population above 200% of the poverty levels
5) Percentage of population of minority race
6) Percentage of individuals over 16 with some college education
```

1) agent concentration

2) pricing

3) competitors' agent concentration

4) economic conditions

5) promotional support

6) demography, and

7) qualitative factors such as corporate reputation in the area, the type of claims services, and the location and appearance of agent's offices.

Several of these variables were available on the marketing research database; others are able to be acquired only with considerable effort and expense. Part of the statistical analysis would therefore have to be directed toward an assessment of the value of acquiring data for several of the independent variables. The purpose of the relational statistical analysis is to help answer the following questions:

1) What factors explain variations in corporate performance among counties? For which of the factors should more data be acquired?

2) How does agent productivity depend upon agent concentration? What would be the expected benefit from adding agents in different locations?

3) What would be the expected benefit from various types of promotional efforts?

Table 5 contains a list of variables that were used in preliminary statistical analysis. As in most studies of this nature, several problems are encountered in statistical modeling. We shall discuss three that seem universal in work of this type.

Considerable collinearity exists among the explanatory (independent) variables. An efficient method is therefore required to help the analyst select combinations of the independent variables that together produce the greatest explanatory power.

There is the possibility that some counties, for one reason or another, would not conform to the statistical model being fit. This may be due to some identifiable attribute that could be considered with the definition of another variable, or it may be due to some inexplicable anomaly (perhaps even erroneous data collected from primary or secondary sources).

Finally, there is the problem of presenting the results of the statistical analysis in a manner that stimulates managers to think creatively of additional explanatory factors and to develop strategic alternatives that can produce further information about effective marketing practices.

Table 6
Sample output from \_RSQUARE to Identify Best Regression Models

<table><tr><td colspan="3">SELECTION OF REGRESSION CANDIDATES</td></tr><tr><td>N= 102</td><td colspan="2">REGRESSION MODELS FOR DEPENDENT VARIABLE PHPERHH</td></tr><tr><td>NUMBER IN MODEL</td><td>R-SQUARE</td><td>VARIABLES IN MODEL</td></tr><tr><td>1</td><td>0.51887774</td><td>APERHH</td></tr><tr><td>2</td><td>0.53481536</td><td>APERHH PCTEMP1</td></tr><tr><td>3</td><td>0.54175398</td><td>APERHH PCTEMP1 CHGHOME</td></tr><tr><td>4</td><td>0.54931439</td><td>APERHH URBAN PCTEMP1 CHGHOME</td></tr><tr><td>5</td><td>0.55865797</td><td>APERHH GRAPERHH URBAN PCTEMP1 CHGHOME</td></tr><tr><td colspan="3">Legend:</td></tr><tr><td>PHPERHH</td><td colspan="2">number of policy holders per 100 households</td></tr><tr><td>APERHH</td><td colspan="2">number of agents per 10,000 households</td></tr><tr><td>PCTEMP1</td><td colspan="2">percent of population employed</td></tr><tr><td>CHGHOME</td><td colspan="2">percentage change in home mortgage lending</td></tr><tr><td>URBAN</td><td colspan="2">indicator urban versus nonurban county</td></tr><tr><td>GRAPERHH</td><td colspan="2">percentage change in agents per household</td></tr></table>

## 4.4. Tools to Support Relational Statistical Analysis

Again, series of SAS programming macros were created to allow analysis to be conducted flexibly and efficiently. Multiple regression is the basic analytical method for which support for relational statistical analysis was designed. The user first specifies a macro that contains subsetting criteria for analysis (e.g., choose all counties in Missouri). Then the relevant performance measure (dependent variable) is designated via a MACRO assignment. The list of possible explanatory (independent variable)

dent) variables is provided next. (The list defaults to the entire set.) For preliminary analysis, the user can then give a command “\_RSQUARE” that invokes the SAS RSQUARE procedure in such a manner that the “best” statistical models having one, two, three, four, or five independent variables are identified. Table 6 contains a sample output from this procedure.

On the basis of this output, the user then designates explicitly the set of independent variables that should be used for a complete regression analysis. The command “-REGR” causes the regression model to be fit by the least-squares procedures, fitted values and residuals to be computed, and the regression model to be displayed. Also produced is a set of weights that would be applied to each observation if “robust estimates” are desired using the method of Andrews [1]. Observations with weights less than one are those for which unusual values seem to occur and which are influential in the determination of the values of the regression parameters. The user can then request that weighted regressions be performed iteratively through a designated number of iterations. With each iteration, the new values of regression parameters are displayed and the “exceptional” cases are listed showing the values of the explanatory (independent) variables, the value of the dependent variable, the residuals, and the weight that would be given to the observation is subsequent robust regression iterations. Table 7 demonstrates the process.

Table 7
Results from Robust Regression After 3rd. Iteration

<table><tr><td colspan="8">ROBUST REGRESSION</td></tr><tr><td colspan="8">DEP VARIABLE: PHPERHH POLICYHOLDERS/PER 100/HOUSEHOLDS</td></tr><tr><td></td><td></td><td>SUM OF</td><td>MEAN</td><td></td><td></td><td></td><td></td></tr><tr><td>SOURCE</td><td>DF</td><td>SQUARES</td><td>SQUARE</td><td>F VALUE</td><td>PROB&gt;F</td><td></td><td></td></tr><tr><td>MODEL</td><td>2</td><td>92.010967</td><td>46.005484</td><td>193.782</td><td>0.0001</td><td></td><td></td></tr><tr><td>ERROR</td><td>99</td><td>23.503406</td><td>0.237408</td><td></td><td></td><td></td><td></td></tr><tr><td>C TOTAL</td><td>101</td><td>115.514</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">ROOT MSE</td><td>0.487245</td><td>R-SQUARE</td><td>0.7965</td><td></td><td></td><td></td></tr><tr><td colspan="2">DEP MEAN</td><td>0.797569</td><td>ADJ R-SQ</td><td>0.7924</td><td></td><td></td><td></td></tr><tr><td colspan="2">C.V.</td><td>61.09131</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>PARAMETER</td><td>STANDARD</td><td>T FOR HO:</td><td></td><td>VARIABLE</td><td></td></tr><tr><td>VARIABLE</td><td>OF</td><td>ESTIMATE</td><td>ERROR</td><td>PARAMETER=0</td><td>PROB &gt; |T|</td><td>LABEL</td><td></td></tr><tr><td>INTERCEP</td><td>1</td><td>0.005444545</td><td>0.072372</td><td>0.075</td><td>0.9402</td><td>INTERCEPT</td><td></td></tr><tr><td>APERHH</td><td>1</td><td>1.469124</td><td>0.075641</td><td>19.422</td><td>0.0001</td><td>AGENTS/PER 10000/</td><td></td></tr><tr><td>URBAN</td><td>1</td><td>0.081471</td><td>0.133007</td><td>0.613</td><td>0.5416</td><td>HOUSEHOLDS</td><td></td></tr><tr><td colspan="8">ROBUST REGRESSION: EXCEPTIONAL CASES</td></tr><tr><td>STATE</td><td>CNTYNUM</td><td>COUNTY</td><td>APERHH</td><td>URBAN</td><td>PHPERHH</td><td>RESIDUAL</td><td>WEIGHT</td></tr><tr><td>IL</td><td>5</td><td>Bond</td><td>1.379</td><td>0</td><td>1.223</td><td>-1.0981</td><td>0.620865</td></tr><tr><td>IL</td><td>9</td><td>Brown</td><td>2.682</td><td>0</td><td>1.098</td><td>-3.4881</td><td>0.176250</td></tr><tr><td>IL</td><td>21</td><td>Christian</td><td>0.681</td><td>0</td><td>1.708</td><td>0.5996</td><td>0.715176</td></tr><tr><td>IL</td><td>25</td><td>Clay</td><td>1.557</td><td>0</td><td>3.053</td><td>0.4229</td><td>0.659526</td></tr><tr><td>IL</td><td>41</td><td>Douglas</td><td>0.983</td><td>0</td><td>0.884</td><td>-0.7487</td><td>0.887255</td></tr><tr><td>IL</td><td>51</td><td>Fayette</td><td>1.278</td><td>0</td><td>2.739</td><td>0.5931</td><td>0.586199</td></tr><tr><td>IL</td><td>57</td><td>Fulton</td><td>1.530</td><td>0</td><td>1.220</td><td>-1.3630</td><td>0.486028</td></tr><tr><td>IL</td><td>73</td><td>Henry</td><td>0.988</td><td>0</td><td>0.568</td><td>-1.0732</td><td>0.564702</td></tr><tr><td>IL</td><td>81</td><td>Jefferson</td><td>1.361</td><td>0</td><td>1.239</td><td>-1.0506</td><td>0.655467</td></tr><tr><td>IL</td><td>83</td><td>Jersey</td><td>0.460</td><td>0</td><td>1.248</td><td>0.5255</td><td>0.893893</td></tr><tr><td>IL</td><td>87</td><td>Johnson</td><td>2.508</td><td>0</td><td>10.84</td><td>6.5595</td><td>0.070141</td></tr><tr><td>IL</td><td>91</td><td>Kankakee</td><td>0.514</td><td>1</td><td>0.285</td><td>-0.6620</td><td>0.899366</td></tr><tr><td>IL</td><td>107</td><td>Logan</td><td>0.799</td><td>0</td><td>0.398</td><td>-0.9156</td><td>0.641765</td></tr><tr><td>IL</td><td>109</td><td>McDonough</td><td>1.025</td><td>0</td><td>0.647</td><td>-1.0590</td><td>0.580534</td></tr><tr><td>IL</td><td>113</td><td>McLean</td><td>0.507</td><td>1</td><td>1.398</td><td>0.4632</td><td>0.887500</td></tr><tr><td>IL</td><td>119</td><td>Madison</td><td>0.785</td><td>1</td><td>2.483</td><td>1.0655</td><td>0.403859</td></tr><tr><td>IL</td><td>121</td><td>Marion</td><td>1.260</td><td>0</td><td>2.846</td><td>0.7319</td><td>0.506935</td></tr><tr><td>IL</td><td>127</td><td>Massac</td><td>0.248</td><td>0</td><td>0.970</td><td>0.6157</td><td>0.835171</td></tr><tr><td>IL</td><td>133</td><td>Monroe</td><td>0.926</td><td>0</td><td>2.566</td><td>1.0324</td><td>0.418069</td></tr><tr><td>IL</td><td>145</td><td>Perry</td><td>0.245</td><td>0</td><td>0.947</td><td>0.5973</td><td>0.862751</td></tr><tr><td>IL</td><td>149</td><td>Pike</td><td>2.062</td><td>0</td><td>11.84</td><td>8.3327</td><td>0.056976</td></tr><tr><td>IL</td><td>151</td><td>Pope</td><td>5.150</td><td>0</td><td>8.098</td><td>-0.7806</td><td>0.954209</td></tr><tr><td>IL</td><td>155</td><td>Putnam</td><td>1.598</td><td>0</td><td>0.369</td><td>-2.3327</td><td>0.252953</td></tr><tr><td>IL</td><td>181</td><td>Union</td><td>1.437</td><td>0</td><td>3.324</td><td>0.9009</td><td>0.415827</td></tr><tr><td>IL</td><td>185</td><td>Wabash</td><td>1.359</td><td>0</td><td>1.278</td><td>-1.0096</td><td>0.692207</td></tr><tr><td>IL</td><td>187</td><td>Warren</td><td>2.181</td><td>0</td><td>0.997</td><td>-2.7178</td><td>0.226871</td></tr></table>

To place the results of the statistical analysis in perspective, the regression package is fully integrated with the software for geographic mapping. Particularly useful is the ability to plot residuals from the regression model in one of two forms. In the first form, the actual values of the residuals are plotted on the relevant map. Areas are shaded green to identify counties where performance is above the “expected” level considering the explanatory variables; areas are shaded red to identify counties where performance is below the “expected” level. Another macro, “\_CLASSES” groups the observations into a specified number of classes with equal numbers of observations for selecting shading patterns.

In the second form, the extreme residual values only are shaded (green for cases where performance is exceptionally higher than expected, red for cases where performance is exceptionally lower than expected). Given these geographical portrayals of results from the statistical modeling, managers are able to superimpose their own knowledge on the analysis in a systematic manner.

By focusing on the values of residuals, the analyst can also selectively collect further information in an efficient manner to determine whether another factor appears to influence corporate performance. For example, information about the concentration of competitors' agents is expensive to compile. The importance of this information can be assessed by collecting it for a few counties with “extremely low” (i.e., negative) residuals, a few with “extremely high” residuals, and a few with residuals near zero. If the residual classification is related to the new explanatory factor, the new information is judged to be potentially valuable.

In summary, a variety of tools allows the conduct of relational statistical analysis to be conducted flexibly and efficiently. The integration of traditional statistical tools, robust statistical procedures, and computer cartography greatly enhances the value of the system to analysts and managers.

## 5. Implementation and Use

The basic system was developed on the University of Missouri computer system and then installed at the company. Four months of elapsed time and 100 man-hours of effort were required to design and implement the segment for the analysis, mapping and reporting of descriptive statistics. Most of the effort was consumed in producing the programs for generating and regenerating the data base from the detailed policyholder files and U.S. Census tapes. The interactive mapping capabilities had been developed for another competition study reported by Smith et al. [11]. Less than 20 hours were required to make the necessary modifications.

An additional 100 man-hours were required to refine and implement the robust statistical procedures and to integrate them with the mapping software. Approximately half of this time was consumed with cosmetic modifications that made the procedures easy to use as a “black box” for nontechnically trained analysts. Further work was required to develop a “character generator” that enables labels to be superimposed on maps generated by SASGRAPH. The mapping procedures, character generator, and robust statistical procedures are all readily portable to other installations equipped with SAS.

The director of planning and research and his senior analyst began immediately to use the system in their work. They expanded the number of performance variables and explanatory variables on the database and performed extensive analyses of corporate productivity in the marketing area. They identified counties where productivity was significantly higher or lower than average considering the resources deployed. They studied underwriting losses as a function of numerous rating factors and market characteristics. In short, the decision support system facilitated a shift in emphasis from tracking aggregate corporate performance to investigating reasons for variation in performance and examining potential effects of strategic decisions.

The vice-president of marketing has requested an IBM 3279 terminal of his own so that he can conduct his own analysis. The director of planning and research is familiar with SAS and comfortably performs his own subsetting of files and calculations of new variables by using SAS interactively. The vice-president of marketing is not familiar with the SAS language. He will use the system in a more structured fashion, concentrating on its use for inquiry and analysis of descriptive statistics. We anticipate having to make some modifications that give the system more of a “turnkey” character for use by the vice-president of marketing.

## 6. Conclusion

The management information system seems to have satisfied the criteria that were outlined in the introduction to this paper. Managers have found that it serves as an excellent tool for the presentation of large volumes of information in an understandable form. Useful questions have been provoked; answers to some have been provided.

The use of a high-level language (SAS with SASGRAPH) enabled responsibility for system development and maintenance to be assumed by planning analysts. Modifications can be made to the system without the intervention of data processing professionals.

Finally, the integration of robust statistical procedures and computer cartography enables analysts and managers to cooperate more fully in efforts to understand the business environment and generate strategic alternatives for adapting to it.

## References

[1] D.F. Andrews, “A Robust Method for Multiple Linear Regression,” Technometrics, 16 (1974): 523–531.

[2] L.D. Barbosa and P.G. Hirko, "Integration of Algorithmic Aids Into Decision Support Systems," MIS Quarterly, 4 (1980): 1-12.

[3] Jack R. Borsting, "Decision-Making at the Top," Management Science, 28 (1982): 341-351.

[4] Dean W. Boyd, R.C. Phillips, and S.G. Regulinski, "Model of Technology Selection by Cost Minimizing Procedures," Management Science, 28 (1982): 418-424.

[5] Franz Edelman, “Managers, Computer Systems and Productivity,” MIS Quarterly, 5 (1981): 1–18.

[6] John Gratwick, “Systems Science and Transportation Policy – The Canadian Experience,” paper delivered at CORS/TIMS/ORSA Joint National Meeting, Toronto, Canada (1981).

[7] Ulysses J. LeGrange, Testimony Before the Federal Energy Regulatory Commission, Docket No. 0E79-1 (1979).

[8] SAS Institute Inc., SAS/GRAPH User's Guide, 1981 Edition, Cary, NC: SAS Institute Inc., 1981, 125 pp.

[9] SAS Institute Inc., SAS User's Guide: Basics, 1982 Edition, Cary, NC: SAS Institute Inc., 1982, 923 pp.

[10] SAS Institute Inc., SAS User's Guide: Statistics, 1982 Edition, Cary, NC: SAS Institute Inc., 1982, 584 pp.

[11] L. Douglas Smith, J. Blodgett, C. Cole, and M. Watters, "A System for Analysing Competition in Distribution of Petroleum Products," Studies in Management Science and Systems: Energy Models and Studies, (Benjamin Lev, ed.) North Holland Publishing Company (1983): 309–324.

[12] Ralph H. Sprague Jr., "A Framework for the Development of Decision Support Systems," MIS Quarterly, 4 (1980): 1-26.

[13] K.W. Studnicki-Gizbert, “Policy Objectives, Conflict Management and Managerial Efficiency,” paper delivered at CORS/TIMS/ORSA Joint National Meeting, Toronto, Canada (1981).

[14] Anthony L. Wasserman, and Steven Gutz, "The Future of programming," Communications of the ACM, 25 (1982): 196–205.
