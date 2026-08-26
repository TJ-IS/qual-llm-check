---
otero_id: 27301
otero_key: "FAA6UHE3"
title: "Special Event Data in Shared Databases"
authors: "Wilpen L. Gorr"
year: "1986"
journal: "MIS Quarterly"
doi: "10.2307/249257"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Special Event Data in Shared Databases
Author(s): Wilpen L. Gorr

Source: MIS Quarterly, Vol. 10, No. 3 (Sep., 1986), pp. 239-255

Published by: Management Information Systems Research Center, University of Minnesota

Stable URL: http://www.jstor.org/stable/249257

Accessed: 09/05/2014 08:55

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Special Event Data in Shared Databases

By: Wilpen L. Gorr
Professor of Public Policy and Management Information Systems
School of Urban and Public Affairs
Carnegie-Mellon University
Pittsburgh, Pennsylvania

## Abstract

This article presents special event data for use in database management systems, along with a case study of the collection and representation of such data for an organization. Special event data account for structural changes and pattern interruptions in the time series data of an organization's performance measures, and are important for the strategic management activities of evaluating management's past actions and forecasting exogenous variables such as demand for products and services. Most organizations do not have a practice of collecting, storing, or sharing special event data so this valuable resource is lost as employees forget the past or take new jobs. Now that organizations are widely implementing DBMSs, it is possible and important to provide special event data. Data in the hands of individual end users can lead to errors in interpretation and use. Special event data, if they are included in the database, can help to alleviate this problem by sharing knowledge on shared data.

Keywords: Data structure, information systems, database management, logical design, decision support

ACM Categories: E.1, H.2.1, H.4.2

## Introduction

Special event data describe out-of-the-ordinary events important to the management of an organization. Such events can occur in the environment (e.g., input supply conditions or the demand for goods and services) or in the organization itself (e.g., management decisions and the implementation of new production technologies). Furthermore, special events may be classified as causes and/or effects. For example, suppose that a city government annexes a suburban community. Then, in exchange for paying city taxes, the suburb receives a number of city services, including city water. This causes a step-jump increase in domestic water demand for the city's water utility. Here annexation is the cause and the increase in water demand is the effect. Each is a separate special event, linked as a cause and effect pair and important to the water utility in forecasting water demand.

Interruptions or pattern changes in the time series data of an organization's performance measures, such as the step-jump in water demand, make up on class of special events. Other members of this class include the impulse (outlier), turning point (e.g., a change from an increasing to a decreasing time trend), change in magnitude of seasonality, and change in magnitude of a time-trend slope (e.g., from strongly to weakly increasing). Special event data are valuable for evaluating management's past decisions and forecasting exogenous variables, which, in turn, are essential components of resource allocation and strategic management decisions.

Special event data are becoming more important as database management systems (DBMSs) are being widely implemented. A DBMS makes it possible to integrate data from many sources and to share them with multiple end users for varying applications. Currently, DBMSs provide only limited shared knowledge of data, such as data definitions found in data dictionaries. End users should also be supplied special event data to annotate conventional data elements; otherwise, they may use shared data naively and make mistakes. The purpose of this article is to fill this void by providing a representation of special events suitable for shared use in databases.

Generally, organizations have not had a tradition of collecting and storing special event data, let alone sharing them. Employees gain knowledge of special events in the course of carrying out day-to-day responsibilities but then quickly forget about them or, when recalling them, tend to distort the facts and only recall part of the relevant data (e.g., see Fischhoff [6] and Fischhoff and Beyth [7]). As a result, analysts have to “reinvent the wheel” and relearn the data when repeating analyses periodically. Kennedy and Siegel [9] state “An unfortunate fact of state government is that just when an employee develops an expertise in the database in their area, they leave state government. The process of ‘learning’ the data must then be repeated with new employees.”

Lewandowski [10], writing on sales forecasting, asks his reader to “. . . think how long a manager, or staff member stays on the job. Obviously, nobody remembers what has happened after the person responsible has left, and, since a record is rarely kept, the new manager does not understand why sales have been erratic in some periods.” An example of this is in the case study of this article on the Columbus Ohio Division of Water. The two most knowledgeable persons interviewed on special event data were a former employee and a retiree.

There are two computer forecasting packages that include special event files, FORSYS by Lewandowski [10] and FUTURCAST by Carbone and Makridakis [5]. The representations of special events in these packages, however, are not adequate for the kind of sharing needed in a DBMS. For example, FORSYS only stores a descriptive title of the causal event and additive adjustments that account for the effects on sales. This is only adequate for the analyst who collects special event data and uses them himself in the package. Carbone and Makridakis use multiplicative instead of additive adjustments (more is included on this later) and add an event description for the causal event as well as including the title. The representation of special events for sharing, presented in this article, also includes data on who supplied the data, and how that person produced them (e.g., expert judgement, statistical study, recollection, logical deduction, recorded facts, etc.). These additions allow the end user to contact the supplier from more information and to judge the quality and nature of the data.

It is evident that a more complex relationship than cause and effect pairs is needed for special events in the context of a DBMS, as contrasted to that of a forecasting package. For example, the Columbus Division of Water case study has multiple special events related in causal chains in which a particular special event can be both a cause and an effect. This article, therefore, introduces network and equivalent relational data models to relate special events.

There are scattered applications of special event data in practice and in the literature at this time. See Gorr [8] for examples in the not-for-profit and government areas. On the evaluation side, Carbone and Gorr [4] evaluated the impacts of several air pollution controls implemented in Pittsburgh, Pennsylvania on air quality at a monitoring site. The special event data on the controls were obtained by interviewing air pollution control engineers at the local air pollution control agency. The authors then constructed a multivariate time series model of air quality that accounted for all sources of variation in air quality, they argued, except for special events and the error term. Remaining patterns (improvements in air quality in this case) were then attributed to the special events.

A practical method of evaluation using special event data is to forecast the “counter factual case,” that which would have happened had there been no special event. This is produced by extrapolating the historical trend of a performance measure into the time period of a special event. The comparison of this and the actual performance data from the special event period provides the desired evaluation. A task force of the Blue Cross/Blue Shield Association, under the direction of Susan Brown [3], plans to recommend the use of FU-TURCAST in this way to its member organizations for evaluating the impact of cost containment programs on claims costs of large health insurance customers.

The adjustment factors that FORSYS and FUTURCAST estimate for special events have two important uses in forecasting. First, common forecasting techniques, such as the various smoothing techniques and classical decomposition (e.g., Makridakis, Wheelwright, and McGee [11]), have no direct provision to handle the pattern interruptions of special events. As a result, special events distort forecast model estimates and, therefore, the forecasts themselves, unless the special events are first “removed” via the adjustments. Second, if, for example, a sales manager wants to forecast the impact of a certain kind of promotional activity for a product, he can use the adjustments of past similar activities to include the promotion’s impact in an extrapolative forecast. FUTURCAST’s multiplicative adjustments are dimensionless factors (e.g., 1.2 represents an impact 20% higher than normal) and so can be easily transported to a new application series. A published example of special event forecasting is by McLaughlin [12], who has calculated multiplicative adjustments accounting for the six post-war recessions in the U.S. McLaughlin uses these factors to forecast and bracket the impacts of future recessions on economic indicators.

## Special Event Representation

The field of artificial intelligence has provided general schemes to represent knowledge in computer systems; e.g., semantic networks, production systems, and frames and scripts (e.g., see Barr and Feigenbaum [1]). Rather than pursuing any of these, this section provides common data models for special event data so that they can be included in DBMSs; in particular, this section develops a network model which is implemented via an equivalent relational data model. The latter is applicable, then, to the many modern relational DBMSs.

## Evolutionary Network Model

The water utility example used in the introduction of this article had a cause and effect pair of special events. Generally, however, special events have a more complex relationship than this; for example, a causal chain. To continue the example of the water utility, suppose the increase in water demand caused by annexation caused a new water treatment plant to be built in order to meet the demand. The new plant increases the cost of supplying water, which leads to a water price increase, which later leads to a decrease in water demand. Here we have a whole chain of special events. It is also likely that some causes will have multiple effects; e.g. annexation could produce a step-jump increase in commercial consumption (i.e., water used by retail stores, gasoline stations, etc.) as well as the domestic increase already mentioned.

The structure identified thus far, a chain of events with multiple effects possible, is known as a recursive system in the social sciences (e.g., see Blalock [2]). Corresponding to this is the hierarchical data model. An even more complex structure results by allowing multiple causes of an effect and feedback loop, requiring simultaneous equation causal models and the network data model.

The network model required to represent special event data has a unique feature because the causal chains of special events are open-ended. For example, the collection of special event data is likely to start with the observation of an effect, an interruption in the time series of a performance measure, and then to proceed with interviews to determine its cause. This process may proceed to higher-level causes (and further effects) if appropriate to the needs of the organization's information system. If a recursive system and the hierarchical data model were being used, the result would be that the root node is not fixed, nor even identified at the time the initial special-event-data entries are made in a database.

Figure 1 illustrates a network model that handles the evolution of levels, plus the evolution of separate causal chains later found to be linked. Each node or special event has a three-part identifier. EVENT-CHAIN-ID uniquely identifies each chain ("A" and "B" here). LEVEL numbers each level relative to the first special event discovered at level 0, decreasing upward in the chain and increasing downward. NODE-NO numbers each node of a level starting at 1 and increasing to the right according to order of discovery. An explanation of how the illustrative occurrences in Figure 1 could have evolved follows. First, the analyst responsible for monitoring the organization's performance measures for special events noted the time series pattern interruption A.0.1. On investigation, he determined that A.-1.1 caused A.0.1, but then it was evident that A.-1.1. also caused A.0.2, another pattern interruption. A.0.2 was then found to have three implications, special events A.1.1, A.1.2, and A.1.3. Later, on further investigation, higher-level cause A.-2.1 was determined to cause A.-1.1 and also led to the discovery of A.-1.2.

![](/api/attachments/FAA6UHE3/fulltext/images/448c1795be304f87fbca7b30cb0e4efe890858ad29122384b985841a201895af.jpg)  
Figure 1. Illustrative Occurrences of the Evolutionary Network Model

Independently, the analyst detected B.0.1, another pattern interruption in a performance measure's time series. This was determined to be caused by B.-1.1 which, however, was simultaneously caused by B.-1.2. B.0.2 was also caused by B.-1.1. Lastly, it occurred to the analyst that A.1.3 has two causes: A.0.2, which was already known, and B.0.1. One option now is to go back and relabel the nodes of chain B to include it in A (e.g., B.0.1 and B.0.2 would be relabeled A.0.3 and A.0.4 respectively), or the two chains could be left as shown in Figure 1. The relational data model presented next allows either of these options.

## Relational Data Model

Since a special event can be both a cause and an effect, one record design must serve both types of special events. Table 1 contains five third-normal-form relations which meet this purpose, and Table 2 defines the data elements of Table 1 not defined in text. In

## Table 1. Third-Normal-Form File Designs for Special Event Data

EVENT:
EVENT-ID $^{1}$ EVENT-DATA-SUPPLIER-ID
EVENT-DATE-SUPPLIED
EVENT-TITLE
EVENT-CATEGORY-ID
EVENT-DATE-START
EVENT-DATE-END
EVENT-DESCRIPTION
EVENT-DATA-SOURCE

EVENT-CATEGORY-DEFINITION: EVENT-CATEGORY-ID\*SYSTEM-COMPONENT

EVENT-DATA-ELEMENT-LINKAGE: EVENT-ID\*DATA-ELEMENT-NAME

DATA-SUPPLIER:
DATA-SUPPLIER-ID
SUPPLIER-NAME
SUPPLIER-AFFILIATION
SUPPLIER-JOB-TITLE

PREDECESSOR-EVENTS:
EVENT-ID\*PREDECESSOR-EVENT-ID $^{2}$

$^{1}$ EVENT-ID = EVENT-CHAIN-ID\*LEVEL\*NODE-NO $^{2}$ PREDECESSOR-EVENT-ID =
PREDECESSOR-EVENT-CHAIN-ID\*
PREDECESSOR-LEVEL\*PREDECESSOR-NODE-NO

Table 2. Data Element Definitions for Special Event Data

<table><tr><td>EVENT-DATA-SUPPLIER-ID</td><td>Identification code of the primary person who processed and provided knowledge of the special event</td></tr><tr><td>EVENT-DATE-SUPPLIED</td><td>Date special event data were obtained from data supplier</td></tr><tr><td>EVENT-TITLE</td><td>Short descriptive title of the special event used in reporting</td></tr><tr><td>EVENT-CATEGORY-ID</td><td>Logical classification identification code of the special event based on the organization&#x27;s systems model</td></tr><tr><td>EVENT-DATE-START</td><td>Date the special event started</td></tr><tr><td>EVENT-DATE-END</td><td>Date the special event ended</td></tr><tr><td>EVENT-DESCRIPTION</td><td>Description of what happened</td></tr><tr><td>EVENT-DATA-SOURCE</td><td>Description of how the special event data were produced (e.g., recollection, statistical study, records, logical deduction, etc.)</td></tr><tr><td>SYSTEM-COMPONENT</td><td>Component from the organization&#x27;s systems model</td></tr><tr><td>DATA-ELEMENT-NAME</td><td>Name of a regular data element from the database being annotated with special event data</td></tr><tr><td>SUPPLIER-NAME</td><td>Name of special event data supplier</td></tr><tr><td>SUPPLIER-AFFILIATION</td><td>Affiliation of data supplier (e.g., department or organization)</td></tr><tr><td>SUPPLIER-JOB-TITLE</td><td>Data supplier&#x27;s job title</td></tr></table>

Table 1, the relation names are followed by a colon, record keys are underlined, and attributes are listed in single columns. The EVENT relation contains the basic data and descriptions for special events. The DATA-SUPPLIER-ID allows end users to contact the data supplier for additional information on a special event. The primary data elements are the EVENT-DESCRIPTION, which is text describing what happened, and EVENT-DATA-SOURCE which is text describing how the special event data were produced.

The EVENT-CATEGORY-DEFINITION relation lists the combination of SYSTEM-COMPONENTS defining an EVENT-CATEGORY. This refers to a systems model of the organization which is best left to an example given in Figure 4. The purpose of the EVENT-CATEGORY is to allow logical retrieval of special event data by end users, independent of data element names in the database.

There is also a linkage connecting special event data to a list of impacted regular data elements in the database. This is the EVENT-DATA-ELEMENT-LINKAGE relation in Table 1. For example, the step-jump increase in domestic water consumption impacts a data element called DOMESTIC-WATER-CONSUMPTION. Including such a linkage in this file permits application programs to process regular data elements and their special event data. An example application is the annotated time series graph, Figure 2, in the next section of this paper. The DATA-SUPPLIER relation's function is obvious.

Finally, the PREDECESSOR-EVENTS relation implements the evolutionary network relationship of special events as described previously. It allows, for example, an application program to produce charts such as in Figure 1. Every node's predecessor nodes must be recorded in this relation and the components of the PREDECESSOR-EVENT-ID are analogous to those, therefore, of the EVENT-ID. Some example records of this relation for the chains in Figure 1 are:

$$
\begin{array}{c c c c c c} \text {single cause - A} & 0 & 1 & A & - 1 & 1 \\ \text {multiple causes - A} & 1 & 3 & A & 0 & 2 \\ A & 1 & 3 & B & 0 & 1 \\ \text {simultaneous causes - B} & - 1 & 1 & B & - 1 & 2 \\ B & - 1 & 2 & B & - 1 & 1. \end{array}
$$

## Special Event Data Collection

Special event data can be collected successfully through an interview process. One person can handle this even in a large organization. This person ought to be an analyst in strategic decision making or planning, and should have skills in statistics and interviewing.

There are four steps to collecting the data. Step 1 for the first-time collection of special event data is the identification of performance measures of importance to the management of the organization. Top management can agree on what these should be, and quite often these measures are likely to be aggregate-level data such as monthly sales volume of a product in a geographic region. In step 2, time series plots of these measures are needed in order to identify pattern interruptions which by definition are special events. Time series residual analysis is also useful for this purpose. After the initial special event data collection effort is completed, the analyst continues to monitor time series plots to identify special events.

Step 3 is to identify and interview knowledgeable persons within and outside the organization to determine the causes and effects of the pattern interruptions. For the Columbus Division of Water case, this writer conducted telephone interviews with seven persons, including a manager and an analyst of the Division, a former employee with ten year's experience, a retiree with 26 year's experience, two consultants, and a large water customer. Everyone interviewed to date has felt that it is important to collect special event data and that somebody in their organization should have that responsibility.

In step 4 the data collector must analyze the results of the interviews and encode them in files in the organization's DBMS. This step requires careful investigation, following up leads, reinterviewing as necessary, conducting ad hoc studies, etc.

## Case Study

The Columbus, Ohio Division of Water has 450 employees and an annual budget of over \$50 million. In 1984, its three water treatment plants produced 4.55 billion cubic feet (BCF) of water which were distributed to 176,516 domestic, 11,823 commercial, 269 industrial, and 5 suburban community (or so-called “master-metered”) customers. While some city departments, such as police and fire, obtain their revenues from general revenue funds (taxes), the Division of Water covers all its capital and operating expenses, plus maintains a reserve of approximately 7% excess revenue, through user charges. User charges consist of both a fixed charge per unit time, and a variable charge depending on a customer’s level of water consumption.

Corresponding to the budgeting cycle of the city of Columbus, the Division of Water designs new user charges in July for implementation at the start of the following calendar year. An important component in budgeting of user charges is the short-term forecast of water consumption by sector (domestic, commercial, etc.). Forecasts that are either too high or too low can have serious consequences for this government unit, so forecast accuracy is important. In part, this case demonstrates that water consumption forecasts can be made more accurately and with greater confidence by using special event data.

Past forecasters for the Division of Water have included a summer intern and two external consultants; all were interviewed to collect special event data. The summer intern could not determine the causes of several substantial pattern changes in water consumption time series data, which he was forecasting for the design of user charges. To compensate for his lack of knowledge, he decided to use double exponential smoothing, a time series technique which automatically adjusts a straight-line forecast model to the most recent time trend in the data. While this may have improved forecast accuracy somewhat, it did not improve the confidence which can be placed in the forecast. There was still no basis to explain why the new pattern arose and if it would persist. The two consultants who had done forecasting for the Division, one with an engineering firm and the other university-based, both agreed that special event data would improve forecasts based on the Division's historical data.

244 MIS Quarterly/September 1986

![](/api/attachments/FAA6UHE3/fulltext/images/a1dc4fac7f0d2eb4c65b39545fd0c657d12dc2f5e5b8c62c438441732b5c83b7.jpg)  
Figure 2. Annotated Time Series Plots of Metered Water Consumption by Sector

Besides these forecasters, special event data would be helpful to others associated with or employed by the Division of Water. For example, system capacity planners have to make use of historical consumption data, as do budget officers who monitor and make short-term forecasts of revenues and expenses. Various managers, such as the Manager of Administrative Services, need to have a general understanding of consumption patterns.

Figure 2 contains time series plots of water consumption by sector (1960-1984), annotated with special events. The boxes drawn on these plots contain the pattern interruptions defining the initial set of eight special events. Three types of pattern interruptions were found: change in magnitude of trend slope (A.0.1), step change in level (B.0.1, C.0.1, D.0.1, and D.0.2), and turning point (D.0.3, E.0.1, and E.0.2). The titles associated with the boxes in Figure 2 are from special events believed to have caused the pattern interruptions; for example, the start up of the new Anheuser-Busch Brewing Company in 1968 caused the step change in level of commercial water consumption in that same year (C.0.1). Figure 3 shows the relationship of all 15 special events identified. There are five causal chains ranging in complexity from the simplest possible, consisting of a single cause and effect (chains A, B, and C), to the three-level chain D. Neither multiple causes of an effect, nor simultaneous causes were encountered.

Finally, the Appendix is a report of all 15 special events generated from the EVENT, EVENT-CATEGORY-DEFINITION, DATA-SUPPLIER, and PREDECESSOR-EVENTS files. Each special event is identified via the EVENT-ID, as seen previously in Figure 3, and EVENT-TITLE. The entries for event dates, description, and data source are from the EVENT file. The cate-

![](/api/attachments/FAA6UHE3/fulltext/images/78ed7233f1c25d5b45504d621ebcfe08fe35ab8e3304d03cb2eb06aad0879540.jpg)  
Figure 3. Causal Chain Occurrences of Special Event Data

## MIS Quarterly/September 1986

gory entries are collections of system components obtained by checking off the appropriate boxes in Figure 4. Figure 4 portrays the Division of Water through four major subsystems, ten subsubsystems, and twenty-eight finer categories. Besides the usual production and environment components (subsystems 1 and 2), Figure 4 also includes a measurement subsystem to record measurement units, and a management-actions subsystem to record the impacts of management decisions.

Figures 2 and 3 show overall features of the special event data collected. Next, it is useful to discuss each causal chain in some detail to show the richness and value of the special event data entries of the Appendix.

## Chain A

In viewing the domestic water consumption time series in Figure 2, it is evident that the time trend slope decreases abruptly in 1971

For example, summer rainfall is an important determinant of annual domestic consumption. If there is a dry spell, residents use more water than usual to water lawns. Domestic consumption was therefore regressed on time (to estimate a time trend), summer rainfall, and a dummy variable interacted with time to allow (event A.0.1). An interview with D.E. Lord (event A.-1.0 in the Appendix) revealed the cause of this to be the end of a sustained period of land annexation by the city. In 1971 it should have been possible to learn of this so that forecasts for 1972 and beyond could have been appropriately reduced. In terms of making use of all historical data to forecast 1985 and beyond, a regression model that ignores the change in 1971 would provide an overall average slope for the time trend (from 1960 to 1984) that would be too low prior to 1971 and too high afterwards, leading to forecasts that are too high for 1985 and beyond. Event A.0.1 contains specific information to aid the forecaster on this and related points.

□ Sector
□ Domestic
□ Commercial
□ Industrial
□ Master-Metered

![](/api/attachments/FAA6UHE3/fulltext/images/6b183024c5963680e7902181b13c5b462a1d1e99f32e0caf747b7943564b7f92.jpg)

2. Division of Water Actions Subsystem
□ Change in User Charges

4. Measurement Subsystem
Financial Components
□ Revenue
□ User Charges
□ Cost
□ Fixed
□ Variable
Water Volumes
□ Finished Water Pumpage
□ Metered Consumption
□ Number of Customers

Figure 4. System Components of the Columbus Division of Water the time trend slope to change in 1971. The slope decreased from 60 to 35 BCF per year in 1971 and this change is statistically significant, so a forecaster should use this specification. A forecaster can be confident of a slope around 35 BCF per year after 1971, because we know that after 1971 the time trend is limited to growth in per capita consumption and new construction in the existing city land area. The more volatile and less predictable period prior to 1971 is past.

## Chain B

Figure 2 reveals a very substantial step increase in the level of domestic water consumption in 1982-1984. Event B.-1.1 in the Appendix is the result of a consultant's study that claimed the cause of this to be three consecutive dry summers. The consultant argued this by eliminating other possible causes and examining rainfall data. Under B.1.1 in the Appendix, this writer further corroborated this conclusion by running a regression model that showed that the dry spells indeed quantitatively account for the step jump in consumption. The forecaster of 1985-and-beyond water consumption should thus use a regression model including summer rainfall, which accounts for the step jump. Furthermore, examination of the summer rainfall data for 1960-1984 reveals no dry spell lasting for more than three years. So, unless there is specific information on 1985 weather to the contrary, a forecaster should use a normal rainfall forecast for 1985, thereby lowering the forecast to levels similar to 1980. All of this knowledge is compactly represented in the Appendix, and is readily accessible to the forecaster.

## Chain C

Figure 2 shows a relatively large, 20% step-jump increase in commercial water consumption in 1968. Clues pointed to the start up of a new, large water customer, the Anheuser-Busch Brewing Company. Individual customer data were not available from the Division of Water as far back as 1968, and Division employees could not recall precisely when the brewery came on line. So, as shown under

C.-1.1 in the Appendix, this writer telephoned the brewery to determine that it indeed started in 1968. Evidently it was then mistakenly classified as commercial instead of industrial. Such misclassifications are common in utility companies, both those publicly and privately owned, and Division of Water employees acknowledged that sometimes misclassifications occurred in the Division. The data-source entry of event C.0.1 summarizes additional strong evidence suggesting that the brewery accounts for C.0.1.

In 1967, Division engineers knew that the brewery was starting operation and could have provided, and most likely did provide, the forecaster with this information for the 1968 forecast. For the purpose of using data from this period to estimate a forecast model for 1985 and beyond, it is desirable to adjust the historical data to eliminate the 1968 step jump (e.g., see Lewandowski [5]). Otherwise the time trend slope would be biased high. The entries in C.-1.1 and C.0.1 allow the forecaster to make this adjustment with confidence, knowing that this was a special one-time event.

## Chain D

It is helpful to refer to Figure 3 for a summary of this three-level chain of special events. D.-2.1, at the top, is the start of effluent charges on industrial sewage required by the EPA. This triggered D.-1.1, the reclassification of Anheuser-Busch Brewery from the commercial to the industrial sector. As noted in C.0.1, the brewery had been misclassified as commercial when, in fact, it was the largest single water consumer and industrial water polluter in Columbus. The data-source entry of D.-1.1 summarizes the evidence indicating that the brewery and several other firms were reclassified. This evidence is deductive; no records or knowledgeable employees could be found to factually document the reclassification.

The reclassification led to a step-jump decrease in commercial water consumption in 1976 (D.0.1) and a corresponding step-jump increase in industrial consumption at the same time (D.0.2). These events produce spurious time trends in the commercial and industrial time series in Figure 2. For example, the post-

1975 industrial data, increased by the addition of the brewery and other firms, causes a regression time trend to have a positive slope calculated over 1960-1984, when in fact industrial consumption generally declined after 1973 except for the reclassification. Unless the data are adjusted, forecast models and forecasts are misled here.

As seen in Figure 3, the start of effluent charges, D.-2.1, also caused industries to conserve water in 1977-1980. Effluent charges are a function of water consumption, so in an effort to reduce these charges (which produced a 35% average increase in sewage bills) industries cut water consumption. This produced the industrial water consumption decline of D.0.3. In 1976, given information on the start of effluent charges, a forecaster could have predicted the decline of 1977-1980.

## Chain E

The economic recession following the October 1973 Arab oil embargo (event E.-1.1) was particularly strong and, besides other things, led to downward trends in commercial and industrial water consumption (E.0.1 and E.0.2). While it is difficult to see, because of the reclassification of Anheuser-Busch Brewery and other firms, the time series recovered, but not fully. There was some permanent loss of water consumption in these sectors. A forecaster of 1985 and beyond needs to account for the effects of the recession so as not to bias the long-term trend used in extrapolation.

## Conclusion

The Columbus Division of Water case study has demonstrated that special event data can be readily collected through interviews, even by an analyst outside of the organization under study. It demonstrated that the file designs and other tools developed here adequately represent special event data, and it has provided a clear picture of what special events look like in shareable form. Finally, it has given several examples of how special event data can be used profitably in an organization. Future work includes the generation of some case studies of actual implementations and uses of special event data in DBMSs.

Several applications of special event data are contemplated using the reporting capabilities of DBMSs or general computer packages. For example, reports such as in the Appendix, by data element or systems logical category, are essential to “learning the data.” Similarly, use of a graphics package to produce annotated time series plots such as Figure 2, and use of a chart-making package to display hierarchy occurrences of causal chains such as Figure 3, are necessary. Furthermore, selected special event data can be fed into statistical packages, such as FUTURCAST, to build special-purpose files on special event data, including adjustment factors for time series forecasting.

A related future area of research and development is on data dictionaries for aggregate data. As end users expand their use of data and end-user computing, the demand for aggregated, transformed, or otherwise enhanced transaction data has increased. Consequently, there is a need to develop data dictionaries for such data, which typically have more volatile definitions than basic transactions data. One form of special event data here is the change of an aggregate data element's definition. Corresponding data dictionaries should have a time stamp on entries to provide a history of definitions to the user. This would account for otherwise spurious pattern changes, and would make aggregate data more shareable.

Another area of future research is to investigate the applicability of special event data to strategic or competitive scanning. This would shift the focus more to data external to an organization, and might require different data collection methods than those used in this article.

## References

[1] Barr, A. and Feigenbaum, E.A. The Handbook of Artificial Intelligence, Volume 1, Stanford Press, Stanford, California, 1981.

[2] Blalock, Jr., H.M. (ed.) Causal Models In the Social Sciences, Aldine Publishing Co., New York, New York, 1985.

[3] Brown, S. Personal Communication, Blue

Cross/Blue Shield Association, Chicago, Illinois, August 9, 1985.

[4] Carbone, R. and Gorr, W.L. "An Adaptive Diagnostic Model for Air Quality Management," Atmosphere Environment, Volume 12, Number 8, August 1978, pp. 1785-1791.

[5] Carbone, R. and Makridakis, S. FUTURCAST software package, Futurion Associates, Inc., 4067 Greensburg Pike, Pittsburgh, Pennsylvania.

[6] Fischhoff, B. "Hindsight-Foresight: The Effect of Outcome Knowledge on Judgment Under Uncertainty," Journal of Experimental Psychology: Human Perception and Performance, Volume 1, Number 3, February 1975, pp. 288-299.

[7] Fischhoff, B. and Beyth, R. “‘I Knew It Would Happen’ Remembered Probabilities of Once-Future Things,” Organizational Behavior and Human Performance, Volume 13, Number 1, February 1975, pp. 1-16.

[8] Gorr, W.L. "On the Use of Special Event Data in Governmental Information Systems," to appear in Public Administration Review.

[9] Kennedy, J. and Adams, M. “Implementation of a State-Level Energy Information Management System,” Inter-Office Communication, Ohio Division of Energy, Columbus, Ohio, January 4, 1984.

[10] Lewandowski, R. "Sales Forecasting by FORSYS," Journal of Forecasting, Volume 1, Number 2, April-June 1982, pp. 205-214.

[11] Makridakis, S., Wheelwright, S.C. and McGee, V.E. Forecasting: Methods and Applications, (2nd Ed.), John Wiley and Sons, New York, New York, 1983.

[12] McLaughlin, R.L. "A Model of an Average Recession and Recovery," Journal of Forecasting, Volume 1, Number 1, January-March 1982, pp. 55-65.

## About the Author

Wilpen L. Gorr is Professor of Public Policy and Management Information Systems at Carnegie-Mellon University. He has designed information systems for several government and not-for-profit organizations. His primary research interests are the design of decision support systems, data and methods needed in strategic management, and the design of adaptive filtering techniques for automated, real-time analysis of data. His teaching responsibilities include MIS and data analysis courses for graduate students in the School of Urban and Public Affairs of Carnegie-Mellon University.

# Appendix Special Event Data Report Columbus Division of Water

Event A.-1.0 End of Land Annexation

Category: Government Action

Supplied by: D.E. Lord, retired manager, Administrative Services Group on 8/20/85 Event Dates

Event Dates
Start: 1971
End: 1971

Description: The city aggressively annexed land throughout the later 1950s and the 1960s. It also extended water service to communities beyond the city limits. By 1971, there were very few additional areas left that could be connected, save Westerville and part of Reynoldsburg.

Data Source: D.E. Lord's recollections.

Event A.0.1 Change in Slope of Domestic Consumption Trend

Category: Domestic Sector, Metered Consumption

Supplied by: W.L. Gorr, independent researcher, Carnegie-Mellon University on 9/12/85

Event Dates
Start: 1971
End: 1971

Description: From 1965 to 1971 domestic consumption increased by 60 million BCF per year. This reduced to 35 million BCF per year in 1971-1984. These estimates are corrected for rainfall variations.

Data Source: W.L. Gorr carried out a statistical study on data provided by J. Boomhouwer of Black & Veatch. Gorr regressed annual domestic consumption on time (year) and summer rainfall, with a dummy variable allowing change in slope starting in 1971. The dummy variable was significant at the 95% level, indicating a significant change in time trend slope.

Event B.-1.1 Dry Spell

Category: Weather, Rainfall

Supplied by: J. Boomhouwer, engineer, Black & Veatch on 9/10/84

Event Dates
Start: 1982
End: 1984

Description: Summer rainfall (June, July, and August) for 1982-1984 was 8.2, 9.6, and 6.8 inches respectively. Average summer rainfall (1965-1984) was 10.7 inches, so 1982-1984 was below average. 1984 and 1982 were the lowest and second lowest summer rainfall years respectively in the 20-year period 1965-1984.

Data Source: Letter from J. Boomhouwer to K. Molli dated 9/10/84.

Event B.1.1 Temporary Increase in Domestic Consumption

Category: Domestic Sector, Metered Consumption

Supplied by: W.L. Gorr, independent researcher, Carnegie-Mellon University on 9/13/85 Event Dates

Start: 1982
End: 1984

Description: Domestic water consumption over 1982-1984 was 17% higher than the pervious 5 years on average. Virtually all of this increase was due to the dry summers of 1982-1984.

Data Source: W.L. Gorr regressed annual domestic consumption on summer rainfall (June-August), time (year), and a dummy variable to adjust the time trend starting in 1971. The relevant residuals show that 12 to 16 points out of the 17% increase were due to the dry spell.

Event C.-1.1 New Anheuser-Busch Brewery

Category: Commercial Sector, New Customer

Supplied by: W.L. Gorr, independent researcher, Carnegie-Mellon University on 8/14/85 Event Dates

Event Dates
Start: 1967
End: 1968

Description: The Anheuser-Busch Brewery started operation in 1967 and got into full production in 1968.

Data Source: W.L. Gorr called the brewery on 8/14/85 to verify the starting dates for production.

Event C.0.1 Increase in Commercial Consumption

Category: Commercial Sector, Metered Consumption

Supplied by: W.L. Gorr, independent researcher, Carnegie-Mellon University on 8/14/85 Event Dates

Event Dates
Start: 1968
End: 1968

Description: The brewery was classified, it appears, as a commercial customer. Total commercial consumption increased 20% from 0.94 to 1.12 BCF per year as a result.

Data Source: Neither records nor knowledgeable employees have been found to verify the classification of Anheuser-Busch as commercial, but there is strong evidence that this is so. The increase in commercial consumption is the same size as Anheuser-Busch's consumption (about 5% of the total consumption). "Industrial" is the only other classification possible for the brewery, but industrial consumption did not increase in 1977/78. So the brewery must have been classified commercial.

Event D.-2.1 Start of Effluent Charges on Industrial Sewage

Category: Government Action, Pollution Control

Supplied by: K. Molli, formerly an administrator, Administration Services Group on 8/14/85 Event Dates

Event Dates
Start: 1976
End: —

Description: EPA regulations required the Columbus Division of Sewers and Drains to begin effluent charges in 1976 on sewage of industrial customers. These charges, which increased sewage bills by 35% on the average, are a function of the type of effluent and water consumption of a firm.

Data Source: K. Molli's and B. Covington's recollections.

Event D.-1.1 Reclassification of Brewery and Other Firms from Commercial to Industrial

Category: Division of Water Management Action

Supplied by: W.L. Gorr, independent researcher, Carnegie-Mellon University on 8/14/85 Event Dates

Event Dates
Start: 1976
End: 1976

Description: The Division of Water reclassified the brewery from a commercial class customer to an industrial class customer.

Data Source: No records or knowledgeable employees have been found to verify this event; nevertheless, there is substantial evidence suggesting that it did occur. B. Covington of Data Processing, states that around 1976 several commercial customers were reclassified as industrial due to the start-up of effluent charges on industrial sewage. Furthermore, the decrease in commercial consumption of 0.26 BCF in 1976 is matched by a 0.25 BCF increase in industrial consumption. 0.17 BCF of this change is accounted for by Busch Brewery.

Event D.0.1 Step Jump Down in Commercial Consumption

Category: Commercial Sector, Metered Consumption

Supplied by: W.L. Gorr, independent researcher, Carnegie-Mellon University on 8/14/85 Event Dates

Event Dates
Start: 1976
End: 1976

Description: Commercial water consumption decreased 0.26 BCF permanently due to the reclassification of Busch Brewery and other firms from the commercial to industrial category.

Data Source: Time series of annual commercial water consumption.

Event D.0.2 Step Jump Up in Industrial Consumption

Category: Industrial, Metered Consumption

Supplied by: W.L. Gorr, independent researcher, Carnegie-Mellon University on 8/14/85 Event Dates

Event Dates
Start: 1976
End: 1976

Description: Industrial water consumption increased by 0.25 BCF per year “permanently” due to the reclassification of Anheuser-Busch Brewery from the commercial to industrial category.

Data Source: Time series of annual industrial water consumption.

Event D.-1.2 Industrial Conservation of Water Category: Industrial Sector, Metered Consumption

Supplied by: K. Molli, formerly an administrator, Administration Services Group on 8/14/85

Event Dates
Start: 1977
End: 1980

Description: Numerous industrial customers decreased water consumption in order to reduce effluent charges. Often this was accomplished by recycling water or by using production processes requiring less water.

Data Source: K. Molli's recollections.

Event D.0.3 Industrial Consumption Decline Category: Industrial, Metered Consumption

Supplied by: W.L. Gorr, independent researcher, Carnegie-Mellon University on 8/14/85

Event Dates
Start: 1978
End: 1980

Description: Industrial consumption was 0.769 BCF in 1978. This declined by 13% to an average of 0.670 BCF in 1978-1980.

Data Source: Annual time series of metered industrial consumption.

Event E.-1.1 Economic Recession Category: Macro Economic Condition, Decline

Supplied by: K. Molli, formerly an administrator, Administration Services Group on 8/14/85 Event Dates

Event Dates
Start: 1974
End: 1975

Description: After the October 1973 Arab oil embargo, the USA and other countries had a strong recession.

Data Source: Common knowledge.

Event E.0.1 Industrial Consumption Decline

Category: Industrial Sector, Metered Consumption

Supplied by: K. Molli, formerly an administrator, Administration Services Group on 8/14/85 Event Dates

Event Dates
Start: 1974
End: 1985

Description: Several industrial firms permanently scaled back production levels or closed completely during the recession, thereby reducing industrial water consumption.

Data Source: K. Molli's recollections.

Event E.0.2 Commercial Consumption Decline

Category: Commercial Sector, Metered Consumption

Supplied by: W.L. Gorr, independent researcher, Carnegie-Mellon University on 9/13/85 Event Dates

Event Dates
Start: 1974
End: 1975

Description: The commercial sector decline of 27 MCF from 1973 to 1974 and 105 MCF from 1974 to 1975 was likely due to the 1974/75 economic recession.

Data Source: Observation of the commercial water consumption time series and knowledge of the economic recession. This is a correlation.
