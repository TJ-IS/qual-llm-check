---
otero_id: 18740
otero_key: "G3TWA2ZK"
title: "An assessment of DSS performance"
authors: "Louis A. Le Blanc"
year: "1991"
journal: "Information & Management"
doi: "10.1016/0378-7206(91)90050-c"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
SOS

# An assessment of DSS performance

# The impact of utilization and closure

Louis A. Le Blanc

Department of Management, College of Business Administration, University of Arkansas at Little Rock, 2801 South University, Little Rock, AR 72204, USA

The information technology described is a U.S. Coast Guard vessel movement reporting system, known as a vessel traffic service. This group decision support system aids vessel operators to navigate a treacherous portion of the Mississippi River from the Gulf of Mexico to Baton Rouge. Voluntary participants provide inputs for a computer simulated tracking of vessels and receive relevant information about marine traffic from the system. Two time series regression models explain changes in system performance as specified by objective, quantitative criterion variables known as critical success factors. One model relates changes in the safety criteria (vessel accidents) with utilization of the vessel traffic service, and the other regression explains changes in system utilization with factors which dictate use. Despite initial criticism that this decision support system was technically flawed because it did not use radar or television to establish the real-time presence and progress of vessel traffic, this research provides evidence that the vessel traffic service has been very effective in reducing vessel accidents on the lower Mississippi River. The findings suggest that not only are utilization levels of these systems important, but also their very presence is crucial for vessels wishing to avail themselves of the service. The presence of the system provided measurable benefits, while the absence of the vessel traffic system precipitated higher accident rates through lower user participation after its eventual reinstatement.

Keywords: Decision Support Systems, Information System Usage, System Performance Measurement.

## Introduction

A decision support system (DSS) is a computer-based information system that is designed to support unstructured problem solving, decision making, and decision implementation (Alter, 1980; Sprague, 1980). Components of a DSS include hardware, software, data, people and procedures. In transportation applications, computer-based information technology, such as DSS, provides beneficial information to managers that support decision-making processes (Allen and Emmelhainz, 1984; Martland and Waters, 1984).

## Vessel Traffic Services

A vessel traffic service (VTS) is a public sector DSS encompassing the technologies, equipment, and personnel employed to coordinate vessel movements in or approaching a port or waterway.

![](/api/attachments/G3TWA2ZK/fulltext/images/280589c7d3eac7ced46d10a3e713bd24f1215512bea16d6c70a430c2e90f6db1.jpg)

Louis A. Le Blanc is Professor of Computer Information Systems in the College of Business Administration at the University of Arkansas at Little Rock. Prior to this appointment, he was on the faculty at Indiana University–Bloomington. Professor Le Blanc earned the Ph.D. from Texas A and M University in 1978. Dr. Le Blanc completed postdoctoral study in management information systems at the University of Minnesota's Graduate School of Management in 1984 and at

Indiana University's Graduate School of Business in 1987. Dr. Le Blanc has served as a manufacturing systems consultant to AT&T Technologies. In 1986, he was selected as a Faculty Resident with Andersen Consulting. Professor Le Blanc's research interest include software evaluation for management support applications and assessing the impact of system utilization on enterprise level performance. He has recently contributed articles to the Transportation Journal, Evaluation Review, Expert Systems With Applications, and Information and Management.

A VTS provides mariners with accurate and timely information to aid in navigating vessels and may also coordinate traffic movements to minimize accidents. The system attempts to reduce the probability of vessel casualties to protect lives, property, and the environment in general while expediting the movement of vessels.

The VTS concept has evolved over a number of years. In the early 1970s, the U.S. Coast Guard (1973) conducted a comprehensive study of vessel traffic system needs among the nation's ports and waterways. According to this report, the Port of New Orleans and the lower Mississippi River ranked first among the nation's ports in deaths and injuries and second in dollar loss resulting from vessel accidents.

Under the authority of the Ports and Waterways Safety Act of 1972, the U.S. Coast Guard established a VTS for the lower Mississippi River in October of 1977. This DSS, which was designed to assist vessel operators in safely navigating this treacherous inland waterway, utilizes a VHF-FM communications network to distribute information about computer-simulated tracking of vessels.

## The Technology of a Maritime GDSS

## System Components and General Operation

The New Orleans VTS (NOLA-VTS), which commenced operation in October 1977, is a voluntary vessel movement reporting system (Hill, 1973) on the lower Mississippi River. It utilizes a VHF-FM communications network, which is continuously manned and recorded by Coast Guard personnel, and is administered from a Vessel Traffic Center (VTC) in New Orleans. The VTC is staffed by approximately 50 Coast Guardsmen and equipped with radar-like display consoles. The Center processes and disseminates information received from participating vessels' operating in the

![](/api/attachments/G3TWA2ZK/fulltext/images/9ac532aab584c78b6fadc1f3d30898b3de616c42da564fa385bc3b2ae67192d8.jpg)  
Fig. 1. Vessel Traffic Service Display.

NOLA-VTS area. The goal of the system is to improve vessel transit safety by providing the vessels with advance information of other reported traffic.

Hardware/Software - Before entering or getting under way in the NOLA-VTS area, which represents 360 miles of navigable waterway and is divided into four separate operating sectors, the pilot of a vessel radios to the VTC his position, destination and estimated time of arrival at the first of several designated reporting points, plus other data such as type of cargo if hazardous. This information is input to a computer simulation program, which tracks this vessel by dead-reckoning (updates vessel position as a function of direction and speed of movement) and registers it as a "blip" on the VTC display terminals, which are similar to air traffic control displays. There is a separate display for each operating sector of this DSS. (Refer to Figure 1.)

The processing software was custom developed in a procedural language to simulate the movement of watercraft, given input data such as direction and speed of movement. When a vessel completes its transit through a sector, the vessel's simulated image is transferred to the microprocessor and display for the next sector. There is a series of four processor and display pairs, one pair dedicated to each sector of the lower Mississippi River monitored by the NOLA-VTS.

Communications - A series of VHF-FM transceiver stations are positioned along the Mississippi River, and micro-wave relays beam transmissions to and from the VTC via antennas. A separate VHF-FM channel is designated for each individual VTS operating sector. The VTC monitors radio transmissions between meeting and overtaking vessels to insure that their navigators have passing agreements or overtaking agreements.

User-System Interface – Watching their consoles, Coast Guard personnel at the VTC provide vessel navigators with the information represented by the blips on the scopes relevant to developing situations and the proximity of other vessels. Displayed on each console on command and conveyed by radio to the participating vessel is the name, type, cargo, and mile mark of overtaking or meeting point for each vessel that the participant in the VTS will encounter as they make headway to their destination.

This information is utilized by the vessel operators in making decisions as to the proper navigation strategy in plying the lower Mississippi River. Vessel pilots have an extensive knowledge base which allows them to effectively use the information provided by the VTS. In this regard, Perrow (1984) describes the detailed decision processes involved for marine carriers to safely navigate inland waterways.

## Specific Information Available from VTS

The most critical mission of a VTS is to provide information to vessels in planning their transit of the VTS area. The following information is available from NOLA-VTS (U.S. Coast Guard, 1985) to assist vessels to more safely navigate the lower Mississippi River.

Traffic Summaries – Traffic summaries are predictions of traffic to be encountered by the vessel as it moves to the next reporting point. In addition to predictions of vessels to be met, other critical information such as “No Wake” areas, dredges in operation, ships anchored out of authorized anchorages or other hazardous situations that will be passed is relayed by the VTS to vessels.

Traffic Checks Prior to Getting Underway – The action of getting underway is a most critical maneuver, especially when the vessel must “top around.” (The top around maneuver for a ship is a u-turn from a stationary position commencing at a berth or anchor.) The VTS can provide a prediction of vessels intending to pass an area so that a vessel intending to get underway may choose the best moment to start the maneuver.

In addition to the aforementioned intelligence, NOLA-VTS also provides less critical information $^{1}$ including: (1) areas of low visibility; (2) safety, speed and security zones and limited draft areas; (3) aids to navigation; (4) river stages and bridge clearances; (5) shoal areas; (6) speed checks; and, (7) estimated time to destination.

So as not to unnecessarily clutter the VTS channels, none of this information is automatically provided to vessels. It must be specifically requested. While traffic summaries have the highest priority for response, the answer to any question which is pertinent to the safety of a vessel transit will receive the VTC's prompt attention.

## Vessel Reporting and Operating Procedures

There are three major types of reports required while participating in the NOLA-VTS. These are: (1) the initial report; (2) movement reports; and, (3) a final report. Mariners are also advised that information may be requested from or transmitted to the VTC at any time. This includes traffic summaries, river conditions, or major changes in the vessel's navigating situation.

Initial Report – This is the first report the VTC receives from a vessel. It provides the VTC with pertinent information needed for accurate computer tracking within the VTS area. This report may be made by telephone before leaving dock side.

Prior to a vessel entering the system, the master or person in charge of the vessel should report or cause to be reported, the following information to the VTC: (1) name of vessel; (2) type of vessel (e.g., freighter, tanker, towboat, dredge, crewboat, etc.); (3) present position and destination; (4) speed; (5) general nature of cargo carried (e.g., petroleum, general liquid chemicals, dry bulk, etc.); (6) maximum draft; (7) the overall length of a tow; and, (8) special handling requirements (i.e., any conditions of the vessel that, in the opinion of the master or person in charge, may affect its navigation in the VTS area).

The Initial Report should be given about 15 minutes prior to entering the system or getting underway from anchorage or berth. The call sign for NOLA-VTS is “NEW ORLEANS TRAFFIC.” In communications between the VTC and a vessel, the vessel’s name would be used.

An example of an initial report transmitted by a vessel entering the system follows.

"New Orleans Traffic, LILLIAN E."

"LILLIAN E, New Orleans Traffic."

"Traffic, LILLIAN E, I'm at Devil's Swamp Light making six miles per hour, pushing six loads of grain to Paulina Fleet. My draft is nine feet with an overall length of 680 by 70, request traffic summary, OVER."

Movement Report – Movement Reports are made to the VTC by a vessel navigating in the VTS area. The VTC will provide traffic summaries, which advise the vessel of other known traffic and information of general interest.

When a vessel actually enters or gets underway within the VTS area, and/or whenever a vessel passes a reporting point, the master or person in charge of the vessel should report or cause to be reported the following to the VTC on the appropriate sector frequency: (1) name of vessel; and, (2) position (at time of report).

The following is an example of a movement report transmitted by a vessel participating in the system.

"New Orleans Traffic, LILLIAN E, OVER." "LILLIAN E, New Orleans Traffic, OVER." "Traffic, LILLIAN E, Mulberry Grove Light." LILLIAN E, Traffic, you should meet N99 at Manchac Point, followed by two tows above

Plaquemine Point, and two ships and three tows above Georgia Pacific, OVER."

"LILLIAN E, ROGER, OUT,"

Whenever the speed of a vessel is significantly altered or any other information previously furnished the VTC changes, the VTC should be advised as soon as practical. Vessels transiting the VTS area that stop to pick up or discharge barges, anchor, or stop due to fog are requested to make a Movement Report indicating the situation. Any change in previously reported information (e.g., number of barges, cargo, draft, etc.) should be reported to the VTC.

Final Report – Whenever a vessel moors or anchors with the VTS area or departs from the VTS area, the master or person in charge of the vessel should report or cause to be reported the time and place of mooring, or departing the VTS area to the VTC. This report terminates the tracking of the vessel by the VTC. This report also may be made by telephone when possible.

The following is an example of a Final Report transmitted by a vessel upon mooring.

"New Orleans Traffic, LILLIAN E, moored Paulina Fleet, OVER."

LILLIAN E, New Orleans Traffic, ROGER, OUT."

Report of Hazardous Circumstances – The master or person in charge of a vessel in the VTS area should report to the VTC as soon as possible any hazard or unusual circumstances observed while in the VTS area. These include but are not limited to: (1) collisions, rammings, or groundings; (2) any casualty which may impair the safe operation of the vessel; (3) vessels blocking the channel;(4) reduced visibility or other adverse weather conditions; (5) obstructions or encroaching shoal not previously reported; (6) defects observed on another vessel, such as navigation lights extinguished; (7) defects in any aid to navigation; and, (8) any other information that might be pertinent to the safe navigation of the area.

The following is an example reporting of an aid to navigation outage.

"Traffic, LILLIAN E, I'd like to report Southwest Pass Light 17 extinguished and Southwest Pass

Lighted Buoy 3 off station about a half mile to the southwest, OVER."

"LILLIAN E, New Orleans Traffic, OUT."

Other Requests Transmitted to VTS - The purpose of the VTS is to provide information to vessels so that they may more safely plan their transit of the VTS area. Consistent with this objective, the following is an example protocol for vessels participating in the VTS to acquire information about visibility.

"New Orleans Traffic, JOSEPH P. SOUTH, I'm preparing to get underway from Ama Anchorage, do you have any fog reports up to the Kaiser Dock in Baton Rouge? OVER"

JOSEPH P. SOUTH, Traffic, ROGER. Patchy fog from 48 Mile Point to Burnside and shut out fog at Bayou Goula and Plaquemine Bends, OVER."

## Marine Decision-Making with VTS Support

Navigating the lower Mississippi River involves decisions which are relatively unstructured and usually relate to the passing and overtaking of vessels. A navigation decision may be unstructured because of its novelty, time constraints, or lack of knowledge.

The decision support offered by a VTS is the central collection and broadcast of traffic and related information. This reduces the uncertainty about other vessels' positions as well as their intentions. Advanced warning of critical or hazardous areas is also included in this central distribution of information by the VTS. From this input of more accurate and complete data, vessel pilots are better able to make decisions about when and where to pass or overtake other shipping.

Decisions on how to pass (face-to-face meeting of vessels) or overtake (one vessels passes another going in the same direction) are usually quickly reached but gradually implemented due to the slowness of large ships and barge tows to react to decisions to change course and/or speed. These decisions have very permanent effects with severe consequences if they are not made in the best manner. Poor decisions cannot be reversed quickly because of the nature of vessel steerage and propulsion and may result in a serious accident. Such accidents can result in significant dollar losses as well as the loss of life.

## Measures of DSS performance

From the time of their introduction nearly a decade ago by Rockart (1979), the critical success factor (CSF) method has been used primarily for systems planning purposes. This technique identifies the organizational objectives and information systems and the factors that indicate their successful achievement (Munro and Wheeler, 1980; Boynton and Zmud, 1984).

More recently, research studies have reported engaging the CSF methodology for monitoring and reliability assessment of information systems. Jenster (1986–87) investigated the relationship between organizational performance and executive monitoring of strategic success factors across different business strategies. Zahedi (1986) employed strategic success factors to measure the reliability of information systems in achieving their goals. In using the critical success factor approach to study the implementation of decision support systems, Liang (1986) conducted an experimental study to investigate the relative importance of different critical success factors.

## VTS Critical Success Factors

Following the process outlined by Bullen and Rockart (1981), the identification of vessel safety as the CSF for a vessel traffic service on the lower Mississippi River between the Gulf of Mexico and the Port of Baton Rouge was the result of interviews and discussions with members of the Port Safety Council $^{2}$ of the Port of New Orleans. All maritime parties who were interviewed uniformly stipulated that vessel safety (i.e., absence or reduction of marine accidents) was the most important criterion or success factor for a vessel traffic service on the lower Mississippi River or any other U.S. port.

Since the strategic mission of the NOLA-VTS is to improve vessel safety by providing advance information about reported maritime traffic on the Mississippi River between Baton Rouge and the Gulf of Mexico, vessel safety serves as a CSF. Accordingly, the critical success measures, or the key performance indicators of the CSF, include the various types of vessel accidents such as collisions and rammings as well as the rate of voluntary system usage.

## Research on System Use as a Dependent Variable

Ein-Dor and Segev (1981) suggested that system success be considered as the primary criterion variable for research on computer-based systems. They identified several measures employed to determine information system success and selected system use as their preferred measure. Keen (1975) has questioned the practice of equating success with use, since the latter is so easily measured. Robey (1979) demonstrated a strong positive relationship between use of information systems and the attitudes of users toward the same systems. However, Schewe (1976) in earlier research did not find any significant relationship between attitudes toward the information system and system usage. Ginzberg (1981) reported that user satisfaction and actual usage have low correlations and in some instances are negatively correlated. Lucas (1978) contended that use was a good indicator of system success only when participation in the system is voluntary. Trice and Treacy (1988) summarized the history of research that employed utilization as a dependent variable.

## Research on System Use as an Independent Variable

System usage also has been employed as an explanatory variable and associated with recognized measures of system performance or success, such as profit or market share. A number of laboratory studies have attempted to relate DSS usage with performance (Benbasat and Schroeder, 1977; King and Rodriguez, 1978; Chakravarti et al., 1979; Benbasat and Dexter, 1982; McIntyre, 1982; Dickmeyer, 1983; Eckel, 1983; Aldag and Power, 1986; Goslar et al., 1986; Cats-Baril and Huber, 1987; and Sharda et al., 1988). These studies all varied with respect to the nature of DSS support, types of decisions, and performance measures. However, system usage as an explanatory variable was always operationalized as the availability or absence of a DSS. Field research (Fudge and Lodish, 1977; Edelman, 1981; and Gochenouer, 1985) also operationalized system usage as the presence or absence of such assistance. Prior information systems research has neglected to relate system usage as a continuously measured explanatory variable with any measure of system performance.

## System Utilization and System Performance

Lucas (1975) provided some empirical evidence for a general relationship between the use of an information system and organizational performance. He argued that it was difficult to draw conclusions about causality from cross-sectional studies and suggested the need for both laboratory and field studies to confirm and expand his findings.

If use can be correlated with a criterion for system success, usage rate could also be an appropriate measurement for a “successful” system. Furthermore, if usage rate increased when system users should be employing the DSS, then system use would be an appropriate measure of success, especially for a voluntary system.

By definition, a DSS is designed to enhance the effectiveness of decision making. If utilization of the DSS can be associated with the desired changes in the criterion variable, such as the frequency of accidents, then decision making has likely been improved through increased use of the DSS. Moreover, if utilization rates are affected by conditions suggesting increased use of the DSS (i.e. hazardous weather conditions, fast currents, or heavy river traffic), this would also support usage or utilization rate as an appropriate DSS success factor.

The purpose of the following analysis is to measure the effect of the NOLA-VTS on river safety as measured by the change in accidents resulting from the DSS operation and the change in system utilization attributable to such factors as heavy traffic and system closure. The author advocates use of a CSF evaluation approach in appraising the feasibility of any DSS and to give an objective measure of system success.

## Methodology and Variable Selection

Regression analysis was selected as the most appropriate technique for constructing models of the factors which contribute to the changes in vessel accident frequency and system utilization rate. The methodological approach taken was to incorporate variables in the regression equations which would account for all possible sources of variation in the criterion variables (accidents or utilization) and identify those factors which contributed at a statistically significant level to changes in the criterion for system success.

## Criterion Variables

The New Orleans Vessel Traffic Service audits shipping accidents that occur in its operating area and records them on a daily log. The vessel casualty data collected is organized according to one of the following accident types: (1) collision; or, (2) ramming.

Collision - A collision is defined as any contact between vessels which are underway, anchored, moored, or in the process of docking or undocking. It should be noted that collisions rarely involve ship-to-ship incidents; they usually involve at least one barge tow assembly.

Ramming - A ramming is the collision of a vessel with a fixed object such as a wharf, dock, pier, bridge, submerged object, aid to navigation, or oil rig. Collisions and rammings are combined for purposes of this study because they are similar types of accidents and should respond in a similar way to external factors. Furthermore, rammings are very few in number and would lead to a noncontinuous series if used separately.

The VTS statistics used in this study span more than five years from April 1979 to June 1984. (There was a six month closure of the NOLA-VTS in 1982, thereby interrupting the series.) These 57 months represent a time series of accidents on the lower Mississippi River from the moment when NOLA-VTS began recording statistics on utilization of their system until the method of determining utilization rate was changed in mid-July of 1984. Over this period, there were 552 collisions and rammings reported to NOLA-VTS.

System Utilization - The system usage rate is expressed as a percentage. This variable was constructed by aggregating the daily utilization to provide a monthly figure. The U.S. Coast Guard calculates the level of participation in the New Orleans VTS at the hour of peak daily traffic. System participation, or utilization, is the percentage of total traffic that is communicating with the VTC.

Table 1  
Descriptive Statistics for Model Variables. $^{a}$

<table><tr><td></td><td>Accidentsb</td><td>Utilization (Percent)</td><td>River Stage (Feet)</td><td>Traffic (Vessels)</td></tr><tr><td>Mean</td><td>9.7</td><td>66.9</td><td>7.3</td><td>78</td></tr><tr><td>S.D.</td><td>7.9</td><td>9.9</td><td>4.6</td><td>22</td></tr><tr><td>Minimum</td><td>0.00</td><td>47.7</td><td>1.1</td><td>40</td></tr><tr><td>Maximum</td><td>35.00</td><td>82.8</td><td>16.5</td><td>108</td></tr></table>

$^{a}$ All statistics in Table 1 are monthly figures.  
$^{b}$ Collisions and rammings.  
Source: United States Coast Guard and United States Army Corps of Engineers (New Orleans, LA).

Table 1 lists various descriptive statistics about the criterion and explanatory variables used in the regression analysis.

## Explanatory Variables

Five general categories of explanatory variables were identified: (1) river stage; (2) traffic level; (3) system utilization (described in the previous section on criterion variables); (4) system closure; and, (5) weather.

River stage - The stage of the river (height above sea level) is a very critical factor for vessel safety, because river stage directly determines the velocity of the current. The hazardous conditions that often accompany the changes in the river stage (hence, river current) precipitate many vessel casualties on the lower Mississippi River.

Traffic Level – According to maritime authorities, traffic density is another major factor influencing the occurrence of accidents in the study area. Monthly measures of traffic volume include ocean-going ships, barge tow assemblies, tugs, as well as excursion craft. Monthly observation on traffic levels were constructed by aggregating the daily peak traffic loads on the lower Mississippi River as determined by the NOLA-VTS.

System Closure - The NOLA-VTS was not operative for six months from mid-March 1982 through August 1982 due to federal budgetary constraints. A single indicator variable represented system operation before and after the shutdown. This variable measures the residual effect of the six month absence of the NOLA-VTS on maritime casualties on the lower Mississippi River.

Weather – Meteorological conditions that are hazardous to navigation in the study area are those which produce strong winds, heavy rainfall, and fog. Tropical storms and abrupt changes in wind direction that accompany frontal passages and squall lines are common seasonal occurrences. During the winter and spring seasons, fog commonly forms when warm, moist Gulf air invades the area. Indicator variables were constructed to model the seasonal weather patterns which affect navigational safety on the lower Mississippi River.

## Analysis and Results

Regression models were constructed and evaluated to determine the best explanatory equations for vessel accidents as well as NOLA-VTS utilization. The most powerful regression model was selected for collisions/rammings and system use. Explanatory variables incorporated in these models included measures of river traffic, system utilization, river stage (proxy for river current) system closure, and weather.

## Vessel Casualty Model

The best model for collisions/rammings explained about 72 percent of the variation in monthly accidents of this type (see Table 2). The overall fit of the regression function, as given by the F-statistic's high level of significance, was quite good.

River stage - This equation includes river stage variables with a quadratic effect. Differentiation of the river stage portion of the model, which was significant at the one percent level, indicates that collisions and rammings began to increase when the river stage reached 1.7 feet.

Traffic Level - According to the regression, river traffic had a statistically significant (also at the one percent level) effect on collisions and rammings. For every one unit increase in vessel traffic, the model predicted nearly a .2 unit increase in these accidents per month.

VTS utilization - Change in utilization rate for the NOLA-VTS also had a statistically significant impact on collisions/rammings along the lower Mississippi River. A one percent increase in system utilization rate 'is associated with a 0.26 unit reduction in the monthly number of collision/rammings, assuming constant values for all other variables in the equation (i.e., traffic and river current). The level of statistical significance for the utilization rate variable indicates that this effect of NOLA-VTS usage on weekly collisions/rammings has only a one percent chance of being a random effect.

Table 2
DSS Performance Models

<table><tr><td rowspan="2">Explanatory Variables $^{a}$ </td><td colspan="2">Coefficients</td></tr><tr><td>Accidents</td><td>Utilization</td></tr><tr><td>Constant</td><td>7.6850</td><td>28.0154 ***</td></tr><tr><td>River Stage</td><td>-0.3115</td><td>0.3653 ***</td></tr><tr><td>River Stage $^{2}$ </td><td>0.0943 ***</td><td></td></tr><tr><td>Traffic</td><td>0.1870 ***</td><td></td></tr><tr><td>Utilization</td><td>-0.2594 ***</td><td></td></tr><tr><td>Utilization (-1)</td><td></td><td>0.5788 ***</td></tr><tr><td>System Closure</td><td></td><td>-9.0583 ***</td></tr><tr><td>Dec-Jan</td><td></td><td>2.7923 **</td></tr><tr><td>Oct-Nov</td><td></td><td>2.4809 *</td></tr><tr><td>R. Squared</td><td>0.7174</td><td>0.9034</td></tr><tr><td>D-W Stat</td><td>1.91</td><td>1.85</td></tr><tr><td>D.F.</td><td>52</td><td>50</td></tr><tr><td>F-Ratio</td><td>33.0056 ***</td><td>93.5174 *</td></tr></table>

\*\*\* 1 percent level of significance.  
\*\* 5 percent level of significance.  
\* 10 percent level of significance.  
$^{a}$ River Stage $^{2}$ indicates the quadratic term. Utilization $(-1)$ indicates a lag of one period.

An increased utilization rate that is strongly correlated with the desired impact on the criterion variable (i. e., river accidents) documents a successful DSS implementation in the public sector. System use is an appropriate success measure in this and similar systems where usage is voluntary and where a linkage can be established between utilization and performance.

## Utilization Model

The best equation for utilization explained 90 percent of the variation in the monthly usage rate of the NOLA-VTS. All variables incorporated in the final model exhibited levels of statistical significance of at least ten percent. In time series regression, the Durbin–Watson (DW) statistic is highly relevant, as positive correlation of residuals which are adjacent in time is frequently a problem (Pindyck and Rubinfeld, 1981). The DW statistic is a formal test for serial correlation, and neither regression equation exhibited positive serial correlation.

River Stage – As previously hypothesized, a voluntary DSS can be termed “successful” if utilization of such a system increases under circumstances where users have more need for the system’s information in decision making. For example, in times of faster river currents, Mississippi River mariners would place more reliance upon (i.e., make greater use of) the information and assistance provided by the DSS. As estimated by the model and significant at the one percent level, a one foot increase in the river stage would be associated with almost a 0.4 percent increase in system utilization.

Lagged Utilization Rate - Another variable incorporated in this utilization model was the previous month's utilization rate. A lagged endogenous variable represents the existing momentum whereby the level of the criterion variable is expected to amount to an approximately fixed percentage lower (or higher) than the previous time period (Ostrom, 1978). A one unit increase in the prior months usage rate was associated with nearly a six-tenth percent (0.58) increase in the current month's level of participation by users. This lagged utilization variable was statistically significant at the one percent level.

System Closure – Perhaps the most significant results come from an indicator variable which modeled the effects upon system utilization resulting from the closing and then re-opening of the VTS. Significant at the one percent level, this variable estimated that system usage was nine percent lower after NOLA-VTS was closed because of federal budget reductions. As predicted by the model for vessel casualties, a nine percent reduction in user participation would likely result in an increase of two and one-third (2.34) collisions/rammings per month after the closure of this voluntary DSS. This effect has only a one percent chance of being a random phenomena.

According to Carpenter (1988) and based on historic casualty records for the Port of New Orleans, the average cost of each VTS preventable casualty is \$545,000. Based on the average monthly increase in vessel accidents after the system closure, the additional value of the rise in accidents is estimated at \$1.3 million per month or well over \$15 million per year. The anticipated federal budgetary savings resulting from a six month shutdown of the NOLA-VTS is just under \$1.1 million – an estimate of the average amortized capital improvement and annual operating costs for half a year (Carpenter, 1988). In other words, for every one dollar saved for the federal budget by a six month closure, there were over 14 dollars of additional accident costs expected in the year following system replacement.

Weather – The weather indicator variables for December–January and October–November were statistically significant at the five and ten percent levels, respectively. The coefficients for these weather indicators suggest that utilization would be expected to increase between two and three percent during these months as compared to the summer base period of June through September.

## DSS Performance Measurement Using CSFs

The NOLA-VTS can be considered as a successful implementation of a public sector and voluntary DSS. Despite initial criticism that the system was technically flawed because it did not use radar to establish the real-time presence and progress of vessel traffic (Center for Wetland Resources, 1981), this analysis provides evidence that NOLA-VTS has been very effective in reducing vessel casualties on the lower Mississippi River. It is relied upon by mariners when conditions are hazardous for navigation – the hallmark of a successful DSS.

Based on subjective and likely premature user perceptions, the initial criticism of NOLA-VTS is not consistent with the research findings of this study, which is supported by objective measures of system performance. Srinivasan (1985) has reported that perceived measures of system effectiveness are not always positively associated with actual behavioral measures, as appears to be the case with this DSS. As employed in this post-implementation review, the CSF approach objectively measures the effect of the DSS on system performance by ascertaining whether this VTS in fact accomplished what it was designed to accomplish.

The CSF of vessel safety as measured by the level of collisions and rammings relates the enterprise level performance with the usage of information technology. The desired impact (i.e., reduced accidents) was associated at a high level of statistical significance with immediate increases in the utilization rate of the DSS.

Furthermore, the initial model reported in this research employed utilization as an independent variable in the regression equation. This utilization measure was inversely correlated with vessel accidents – increases in DSS utilization were associated with reductions in marine casualties assuming fixed levels of the other explanatory variables. The information systems literature does not report any prior empirical research studies which employed the rate of system usage as an explanatory variable – directly relating utilization rate of the information technology with the desired changes in enterprise level performance.

In this field study of an actual working DSS, measurement of system utilization was calculated as an objective quantitative scale of NOLA-VTS participants as a percentage of total potential users. This is in contrast to most research studies previously reported about system utilization which employ a self-report from users on their usage of an information system. This approach may suffer from validity problems, as self-reported usage rates could have little correlation with actual usage.

Objectives measures of performance, in the opinion of the author, are superior to subjective measures of user “happiness” or satisfaction. Performance appraisal of information systems should be in terms which are related to organizational goals, like a CSF, that can objectively guide systems development, operation, and evaluation.

## Summary and Conclusions

The lower Mississippi River is one of the largest port systems in the world, and possibly the nation's most dangerous port area. Many hazardous cargoes are transported on this river, and any accident could potentially close the river to traffic. If one should happen in a populous area, many human fatalities could result. These circumstances can only underscore the need for an effective VTS (i.e., maritime DSS) on the lower Mississippi River.

The most interesting results of this study come from the statistical significance of the system closure variable for the critical success factor of system utilization. With only a one percent chance of being a random effect, the cessation of the NOLA-VTS for six months had a residual effect of decreasing user participation by an estimated nine percent, and thereby increasing the predicted number of collisions and rammings by more than two per month.

These findings suggest that not only are utilization levels of these systems important, but also their presence is crucial for vessels wishing to avail themselves of the service. In the final analysis, the presence of the VTS provided measurable benefits, while the absence of the DSS precipitated higher accident rates through lower user participation after its eventual reinstatement.

The need for radar and/or television surveillance is questionable as a cornerstone technology for a VTS on the lower Mississippi River. The natural configuration (a physical geography of winding and narrow stretches of water with 20 feet high levees on each side) does not always lend itself to electronic surveillance. Furthermore, the ocean-going vessels and barge tow assemblies are so large (many in excess of 300 feet in length and corresponding width) and proceed so slow (top speeds of five miles per hour on inland waterways) that radar and/or television monitoring is not necessary. To track and monitor the movements of large vessels moving at slow speeds, VTS technology does not have to be equivalent (in sophistication, complexity, and expense) to that required for tracking of relatively small aircraft flying at hundreds of miles per hour on a straight course. A system's substance in terms of "results" is more meaningful than the system's form in terms of perceptions.

## References

Aldag, R.J. and D.J. Power, “An Empirical Assessment of Computer-Assisted Decision Analysis,” Decision Sciences, 17 (1986), 572–588.

Allen, M.K. and M.A. Emmelhainz, “Decision Support Systems: An Innovative Aid to Managers,” Journal of Business Logistics, 5 (1984), 128–142.

Alter, S.L., Decision Support Systems: Current Practice and Continuing Challenges, Addison-Wesley Publishing Company, Reading, MA, 1980.

Benbasat, I. and R.G. Schroeder, "An Experimental Investigation of Some MIS Design Variables," MIS Quarterly, 1 (1977), 37–50.

Benbasat, I. and A.S. Dexter, "Individual Differences in the Use of Decision Support Aids," Journal of Accounting Research, 20 (1982), 1–11.

Boynton, A.C. and R.W. Zmud, “An Assessment of Critical Success Factors,” Sloan Management Review, 25 (1984), 17–27.

Bullen, C.B. and J.F. Rockart, "A Primer on Critical Success Factors," CISR Working Paper Number 69, Center for Information Systems Research, Sloan School of Management, Massachusetts Institute of Technology, June 1981.

Carpenter, S.P., “Cost Recovery for Vessel Traffic Service Operations: An Evaluation of Value Added and Fee Assessment,” Proceedings Of The Sixth International Symposium Vessel Traffic Services’ Gothenburg, Sweden, May 17–19, 1988.

Cats-Baril, W.L. and G.P. Huber, “Decision Support for Ill-Structured Problems: An Empirical Study,” Decision Sciences, 18 (1987), 350–372.

Center for Wetland Resources, Lower Mississippi River Safety Study, Louisiana State University, Baton Rouge, LA, 1981.

Chakravarti, D., A.A. Mitchell and R. Staelin, “Judgement-Based Marketing Decision Models: An Experimental Investigation of the Decision Calculus Approach,” Management Science, 25 (1979), 251–262.

Dickmeyer, N., “Measuring the Effects of a University Planning Decision Aids,” Management Science, 29 (1983), 673–685.

Eckel, N.L., “The Impact of Probabilistic Information on Decision Behavior and Performance in an Experimental Game,” Decision Sciences, 14 (1983), 483–502.

Edelman, F., “Managers, Computer systems, and Productivity,” MIS Quarterly, 5 (1981), 1–19.

Ein-Dor, P. and E. Segev, A Paradigm For Management Information Systems, Praeger Publications, New York, NY, 1981.

Fudge, W.K. and I.M. Lodish, “Evaluation of the Effectiveness of a Salesman’s Planning System by Field Experimentation,” Interfaces, 8 (1977), 97–106.

Ginzberg, M., “Early Diagnosis of MIS Implementation Failure: Promising Results and Unanswered Questions,” Management Science, 27 (1981), 459–478.

Gochenouer, J.E., “An Empirical Study of the Impact of a Decision Support language on knowledge Workers,” unpublished Ph. D. dissertation, Florida Institute of Technology, 1985.

Goslar, M.D., G.I. Green and T.H. Hughes, “Decision Support Systems: An Empirical Assessment for Decision Making,” Decision Sciences, 7 (1986), 79–91.

Hill, R.C., "Increased Safety Through Vessel Traffic Systems," Proceedings Marine Safety Council, U.S. Coast Guard, U.S. Department of Transportation, 30 (1973), 251–257.

Jenster, P.V., “Firm Performance and Monitoring of Critical Success Factors in Different Strategic Contexts.” Journal Management Information Systems, 3 (1986–87), 17–33.

Keen, P.G.W., "Computer-Based Decision Aids: The Evaluation Problem," Sloan Management Review, 21 (1975), 17–29.

King, W.J. and J.I. Rodriguez, “Evaluating Management Information Systems,” MIS Quarterly, 2 (1978), 43–51.

Liang, T.P., “Critical Success Factors of Decision Support Systems: An Experimental Study,” Data Base, 17 (1986), 3–15.

Lucas, H.C., "Performance and the Use of an Information System," Management Science, 21 (1975), 908–919.

Lucas, H.C., “Empirical Evidence for a Descriptive Model of Implementation,” MIS Quarterly, 2 (1978), 27–41.

Martland, C.D. and W.G. Waters, “The Adoption of Microcomputers: Strategies and Implications,” The Logistics Transportation Review, 20 (1984), 309–314.

McIntyre, S., “An Experimental Study of the Impact of Judgement-Based Marketing Models,” Management Science, 28 (1982), 17–23.

Munro, M.C. and B.R. Wheeler, “Planning, Critical Success Factors, and Management’s Information Requirements,” MIS Quarterly, 4 (1980), 27–38.

Ostrom, C.W., Times Series Analysis: Regression Techniques, Sage University Paper Series on Quantitative Applications in the Social Sciences, Series Number 07-009, Sage Publications, Beverly Hills, CA, 1978.

Perrow, C., “Chapter 6-Marine Accidents,” Normal Accidents: Living With High-Risk Technologies, Basic Books, New York, NY, 1984, 170–231.

Pindyck, R.S. and D.I. Rubinfeld, Econometric Models and Economic Forecasts, McGraw-Hill, New York, NY, 1981.

Robey, D., "User Attitudes and Management Information Use," Academy of Management Journal, 22 (1979), 527–538.

Rockart, J.F., “Chief Executives Define Their Own Data Needs,” Harvard Business Review, 57 (1979), 81–93.

Sanders, G.L. and J.F. Courtney, “Field Study of Organizational Factors Influencing DSS Success,” MIS Quarterly, 9 (1985), 77–93.

Schewe, C.D., “The Management Information System User: An Exploratory Behavioral Analysis,” Academy Management Journal, 19 (1976), 577–590.

Sharda, R., S.H. Barr and J.C. McDonnell, “Decision Support System Effectiveness: A Review and an Empirical Test,” Management Science, 34 (1988), 139–159.

Srinivasan, A., “Alternative Measures of Systems Effectiveness: Associations and Implications,” MIS Quarterly, 9 (1985), 243–253.

Sprague, R.H., "A Framework for the Development of Decision Support Systems," MIS Quarterly, 4 (1980), 1–26.

Trice, A.W. and M.E. Treacy, “Utilization as a Dependent Variable in MIS Research,” Data Base, 19 (1988), 33–41.

U.S. Coast Guard, Analysis Of Port Needs, Department of Transportation, Washington, DC, 1973.

U.S. Coast Guard, Users Manual, Fourth Edition, Vessel Traffic Service, New Orleans, LA, 1985.

Zahedi, F., “Reliability of Information Systems Based on the Critical Success Factors Formulation,” MIS Quarterly, 11 (1987), 187–203.
