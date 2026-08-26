---
otero_id: 17456
otero_key: "HZ5UJYKT"
title: "Evolution of the strategy and structure of a human resource planning DSS application"
authors: "R.J. Niehaus"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00016-l"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Evolution of the strategy and structure of a human resource planning DSS application $^{*}$

R.J. Niehaus

Navy Department, Rm 2832, Arlington Annex, Washington, DC 20370, USA

## Abstract

A multi-year effort is described which resulted in the implementation of a series of human resource planning DSS applications in the U.S. Navy shipyard community. These applications span both corporate (integrated management of eight shipyards Navy-wide with 78,000 employees in 1986) and local (individual shipyards with 9,000 employees) perspectives. Many tough management and technical DSS implementation challenges were faced in the environment of the wide-scale reductions of the U.S. defense establishment. The paper first concentrates on the development, implementation and introduction of a DSS in a large organization that is going through a personnel downsizing process. Then, a discussion is provided of the implementation of complex human resource planning models in a DSS that can be used by a mid-level staff person. Methodological issues are discussed both in terms of the model and implementation technology.

Keywords: Human resource planning; Downsizing; Workforce planning models; Goal programming

## 1. Introduction

The purpose of this paper is to describe the strategy and structure of developing a large-scale DSS applications used in the downsizing of the U.S.. naval shipyards. All aspects of DSS development are included from both strategic and structural perspectives. A description is provided of the setting and procedures used during the initial strategic management policy and problem identification phase at the highest levels in the Navy. The evolutionary steps which followed are described to show how the initial concerns were met through the use, modification and information engineering of installed model and DSS capabilities. Each section of the paper will relate the discussion to the practice of using DSS concepts in an operational context.

This paper follows in the tradition of Keen and Morton [20], Sprague and Carlson [28], Bonczek, Holsapple and Whinston [6] and Emery [18] where the emphasis is on building effective decision support systems. The effort is in melding interactive information systems with embedded models with management decision making to enhance the value of the outcomes. In this case, it was difficult to determine where the intervention of DSS technology began and human resource decision making resulted since the capabilities were implemented in the context of a series of short duration high profile situations. This work relates to the implementation issues discussed in Andriole [3] and several of the papers in Blanning, Holsapple and Whinston [5]. The DSS was used to provide the framework to bring together strategic management with shorter term operational decisions.

The work is the fruition of seminal DSS developments in human resource planning area reported by Charnes, Cooper, and Niehaus [17]. These applications are related to the civilian personnel workforce of Navy. Similar efforts related to military personnel can be found in Bollar, Lehto, Offir and Silverman [7] and Weigel and Wilcox [30]; or for industrial organizations by Bulla and Scott [12], Heyer [19], Quigley and Henshaw [26], and Miret [22]. The development of integrated DSS capabilities to support human resource planning can also be found in Boza [8], Manzini and Gridley [21], Smith [27] and Verhoeven [29].

All aspects of DSS development are included from both strategic and structural perspectives. Such developments as the use of embedded Markov processes in goal programming models, goal-arc distribution models, interactive computing, use of reduced dual formulations for computational efficiency, development of front-end shells, downsizing to a computer work station environment, etc.

The DSS used in this paper resulted in a microcomputer version of the long established mainframe based Computer-Assisted Manpower Analysis System (CAMAS) which has been in use since the early 1970s. (See Niehaus [23,24,25] and Bres, Niehaus and Sholtz [11]). The CAMAS capabilities were implemented to cover all shore based headquarters organizations and field installations where the 300,000 civilian employees are situated. The microcomputer version started with a spreadsheet application to support a short term issue and grew into a generalized capability available for use by both Navy headquarters commands and large field installations. The resulting Micro CAMAS or MCAMAS is now being considered for use by a variety of installations across the U.S. Department of Defense facing major reductions.

The paper concentrates on the development, implementation and introduction of a DSS in a large organization that is going through a personnel downsizing process. Then, a discussion is provided on the implementation of complex human resource planning models in a DSS that can be used by a mid-level staff person. Methodological issues are discussed both in terms of the model and implementation technology. Finally a summary of accomplishments is provided with a view to the future.

## 2. Problem domain and DSS development

The DSS embodied in CAMAS has always been developed in the domain of live management issues. The approach has been to start with operational issues, provide some preliminary analysis capabilities, and then broaden out the effort with more advanced capabilities suggested by theoretical and research considerations. As the more advanced capabilities are validated, they are introduced into the simpler DSS already in use. With this approach it is difficult to separate the DSS development from the problem domain since a conscious effort is made to not stray too far from the validity testing provided by participation in live management decision processes. This is very similar to how the original developments in operations research occurred. The development of the DSS becomes a natural outgrowth of the iterative integrated process of supporting management decision making with computer-assisted model based technology.

The problem domain is based in civilian personnel issues in the management of the U.S. Navy shipyards. These public shipyards concentrate on the maintenance and overhaul of the fleet. This includes the refuelling of those ships which use nuclear reactors for propulsion (or deactivation for those nuclear ships which have reached their useful/economic life). The primary driver for shipyard workload is the military strategy of the United States which is reflected in the tempo of operations. As can be imagined, the past few years have been one of trauma inviting the use of DSS approaches.

The study began in 1986 as a quick reaction effort to support the Naval Sea Systems Command (NAVSEA) to answer Secretary of the Navy and Congressional questions concerning a reduction of 8,000 jobs in the eight public naval shipyards. The purpose of the reduction was to provide better balance between the U.S. industrial base of public and private shipyards. The study grew into support of a comprehensive DSS application aimed at workload balancing of ship overhaul assignments to smooth skills requirements and minimize employee turbulence. A follow-on effort at the individual shipyard level provided for the integration of strategic and operational skills and career balancing between the occupations and departments of the shipyard.

Examples of the types of input and outputs were generated and reported in the literature during the formative stages of this work. (See Bres, Niehaus, Sharkey, and Weber [9], [10], Aguilar, Bres, Niehaus and Sharkey [2], and Aguilar, Niehaus, and Sharkey [1]. This paper will summarize this work leaving the earlier reports for those that want a more comprehensive review of actual data results from a human resource planning perspective.

## 2.1. Corporate planning and control

Corporate planning by its nature involves the setting of indirect targets which are linked or integrated with each other, generally over multiple time periods. Such planning has both strategic and control phases. The strategic phase initially involves the resolution of alternatives in order to choose the course-of-action or family of courses-of-action to follow. This phase by its nature normally has unstable elements which come and go in a very rapid fashion. The timely use of DSS capabilities is crucial to influence the outcomes as they relate to various participants.

The control phase of corporate planning involves the tracking and adjustments of the strategic decisions or management targets to try to stay within some bounds of the management targets. The strategic planning alternative may need to be adjusted on a fairly continuous basis as new facts become known. Here too, there can be enough uncertainty to want to have the ability to rapidly reenter the strategic planning environment as the unexpected occurs. In the naval shipyard case, planning for the unexpected turned out to be the norm.

The development of the DSS started with a question by the Admiral in charge of the shipyards asking if CAMAS could be used to assist in managing the reduction of 8,000 personnel in less than nine months across the eight public shipyards with total employment of 78,000. The policy issue under consideration was the shift of workload to private shipyards to preserve the industrial base of the United States. The specific questions were: (1) what would happen if there were a total freeze on employment at all the shipyards and (2) what were the effects of setting employment ceilings over a number of periods at each of the eight shipyards. The initial answers were needed in two days to be used as backup material for hearings by the U.S. Congress.

Given the short time frame, spreadsheet versions of a simple flow model were constructed using personnel movements and attrition data obtained from CAMAS. The results indicated large scale personnel layoffs would be needed to make such changes in so short a period of time. The DSS analyst suggested that additional runs be made to see what could be done in an eighteen month time frame. It was also suggested that a quarterly tracking system be initiated to validate the projections. As a result of the initial review of the model results, staffing was provided so that the shipyard management group could eventually take ownership of the process.

An analysis was made comparing the projected workforce reductions across the eight shipyards. This analysis in conjunction with Congressional oversight was used to shift ship overhauls between shipyards to balance the workload such that no management induced personnel reductions were required. Such changes also affected the actual movements of the U.S. Navy fleet as ships that were expected to be in Hawaii following their overhaul would now be in California. This example shows the power of the use of a DSS including the need for a validation stage to ensure as much accuracy as possible to insure against decisions based on misinformation.

Based on the usefulness of the analysis capabilities, steps were initiated to develop a standardized DSS accessible on a microcomputer. Optimization models using goal programming methodologies were also investigated as a parallel off-line effort during this period. The focus was to downsize the mainframe CAMAS models for processing on a microcomputer. This was done with the goal of moving as much as possible of the ownership of the DSS to the end user.

The Navy used the personnel flow models in connection with total quality management studies aimed at improving the efficiency of the naval shipyards. During 1986-87 components of the Navy such as the Naval Sea Systems Command (NAVSEA) implemented the results of the study. Among the recommendations related to the use of the DSS were:

\- Complete model studies to achieve better balance between more common higher level skills and basic skills.

\- Run computer personnel flow models to initiate workforce reductions on the order of 10% since the shipyards had been staffed to accommodate high side contingencies.

\- Run models to smooth the turbulence of the permanent workforce force by shifting to a richer mix of on-call and temporary employees.

## 2.2. Installation level planning

An integrated approach was used at the shipyard level which relates the management process with the DSS. This approach was tested at Mare Island Naval Shipyard in California. Emphasis was on the decisions necessary for direction and continuity to ensure a productive organization The DSS was used to develop the strategic and tactical plans and to monitor and control the stream of decisions as the workforce changes unfolded. Innovative management practices were instituted to integrate necessary management decisions with employee needs at each stage of development.

The organization uses a common planning methodology. The key driver is the workload available to the shipyard. The Navy fleet maintenance, overhaul and nuclear refuelling schedule is determined centrally to account for fleet operations, required maintenance cycles, and new ship additions. Quarterly, there is a workload conference which includes all eight of the naval shipyards to assure local input to shipyard workload balancing issues.

During the 1988–1991 period, Mare Island Naval Shipyard underwent a large overall workload reduction with intermediate periods of minor growth consistent with ship overhaul schedules. The initial applications involved occupational structural issues to balance movements and promotions between white and blue collar workers. Between 1987 and 1990, the workforce was reduced from 10,000 to 6,400 employees in a series of reorganizations and reductions-in-force (RIFs).

The DSS analyst was invited to be a member of the top management team to recommend the strategies for two large personnel reductions. This team included senior representatives from the planning staff, production department, comptroller's department, and human resources office. Consultation was also sought from a wide variety of in-house constituencies including the shop superintendents who oversee the actual production work. The DSS was refined and focused in terms of job category definitions, additional scenarios, and areas which needed additional backup transaction based reports for clarification.

In addition to meetings with the immediate decision makers, many presentations were made to a wide variety of shipyard personnel as well as to outside interested parties. This ranged from senior management briefings to the Commanders of all the shipyards to presentations to support staffs. The work was reviewed by the U.S. General Accounting Office at the request of Congressional members whose constituents would be affected by the planned reductions. A very favorable assessment was provided in their report to Congress. Implementation of a DSS involves much more than getting a capability running on a computer for use by a limited group within the organization. Where possible, interested outsiders should also be kept informed as to how decisions which affect them are being made.

A wide variety of personnel programs were used to facilitate the workload changes while providing a way for shipyard employees to maintain an orderly life, where possible. The idea is that any important decision should use all available information and be as forthright as possible with both management and employees. The DSS and related transaction report based information systems were used for:

\- Planning for resource availability to meet the projected mid 1990s workload,

\- Planning for workforce strengths to reduce personnel impacts,

· Using a flexible workforce,

\- Using personnel flow models for projecting management actions to ensure management has considered long-term impacts of accelerating attrition,

\- Using apprentice programs as a training pipeline,

\- Implementing a comprehensive outplacement program,

\- Maintaining a computerized skills bank of data on employees who have left who are interested in returning to the shipyard for future work,

\- Keeping the workforce lean to compete successfully for work, and

\- Maintaining a highly skilled workforce.

Many model alternatives were run over the course of the Mare Island downsizing to help guide the shipyard from a personnel strength of over 9800 to 7200 at the conclusion of the 1990 RIF action. During the six months before the 1990 RIF, the DSS was used frequently as changes were proposed or made to the workload and on-board personnel.

One of the successful strategies in the downsizing was a variety of efforts to accelerate attrition. The DSS was used to estimate the effects of controlling personnel movements within the shipyard to channel employees to available opportunities both within and external to the shipyard. The shipyard was aided by a robust external labor market in the San Francisco Bay Area. All the different efforts accelerated attrition and eased the impact of separations due to RIF. In the end,

1,101 employees were separated through the efforts to accelerate attrition leaving 460 employees who had to be terminated in the 1990 RIF action.

The DSS was used extensively in the 1991 RIF. In this case, the local labor market was much less robust and most of the less severe accelerated attrition actions had already been taken in the 1990 RIF. Originally, a much larger reduction was expected. Through much planning and subsequent management action by both the shipyard and higher level authorities, the difficult RIF actions were brought to a minimum. In the end approximately 450 fewer jobs were eliminated because of the better forecasts provided by the DSS. Actual results came within one percent of the forecasted values.

## 3. Relationship of models to DSS use

Several model methodologies are incorporated into the MCAMAS decision support system. These include: (1) no hires, (2) force fit, and (3) best fit views of the future. The “no hires” case assumes there will be no replacement of losses from the outside with normal personnel flows permitted to continue within the organization. The “force fit” case assumes that workload requirements will be balanced precisely at each time period with adjustments accommodated through external additions or deletions to the workforce. Normal internal personnel flows are permitted to continue. The “best fit” case assumes the balancing of the workforce within each period as well as over time. This permits some management flexibility both in the internal movements and external additions or deletions to the workforce.

Two types of models were used: (a) simple personnel flow models to obtain rapid first cut results and (b) optimization models to obtain a fit of the workforce as close as possible to the workload over time, including management controlled, flexible personnel flows. The simple models which use deterministic Markov methods were renamed "no hire" and "forced fit" so that users would not be turned off by the use of formal management science terminology. The optimization models use goal programming approaches and renamed “best fit” for the convenience of the users. The formal mathematical description of these models is provided in the Appendix.

Mare Island Naval Shipyard  
![](/api/attachments/HZ5UJYKT/fulltext/images/e7f1488f75e2a972cd47215493515a0dd1121ad388f88ddbcca79badaefb875e.jpg)  
Fig. 1. Comparison of goals and projected workforce by model type.

Mare Island Naval Shipyard  
![](/api/attachments/HZ5UJYKT/fulltext/images/9ffe79de1a10c24258d0b537d63d360cf90039dd116c5d4764fbbae095c6a812.jpg)  
Fig. 2. Comparison of deviations from workforce goals by model type.

In addition to the extensive information engineering changes, new model structural improvements were developed as well. In this case, the most needed flexibility features of goal-arc distribution models were reintroduced into previously developed human resource goal programming models using standard linear programming solution methods. The revised models were able to correct statistical and organizational issues surrounding the fact that too much flexibility gives too many choices.

Fig. 1 is an example of an output which was used to make the decision as to the best level of projected workload for the Mare Island shipyard in the June 1990 to September 1993 period. In this example the goal and forced fit workforce profiles are the same since in the forced fit model the sum of additions and reductions to the workforce are developed to force the profile to the goal levels. The no fires profile shows a workforce greatly in excess of projected workload for the first six periods. The best fit profile show a workforce which is over assigned workload in several of the periods with a smoother transition suggested if some additional workload can be found to fill in the gaps. This information was used in negotiations with the shipyard headquarters organization and at the shipyard wide workload planning conference to obtain the needed additional workload. Supporting more detailed reports were developed to show the differences at the skill level.

Additional charts were developed to show the impacts in terms of aggregate numbers of personnel. Fig. 2 shows the relationship of the workload to the number of personnel over or under the projected to be available to be assigned. Since the reductions are monotonically decreasing, there are no underages from the goals. (In situations where the workload dips and then grows again, there could be both overages and underages in terms of how close one meets the goals when the best fit model is used.)

Mare Island Naval Shipyard  
![](/api/attachments/HZ5UJYKT/fulltext/images/726496e8c30e70548c4cbce969724b1534acf62dadf89d81e024cfc8d202ba7a.jpg)  
Source: Aguilar, Niehaus and Sharkey [1]  
Fig. 3. Comparison of projected hires/fires by model type.

In Fig. 2 one can see the number of people in each periods for which there is no work for them to do. In the no-fires case the numbers are so large as to indicate that an employment freeze will be insufficient to address the workload drawdown. In the best fit case, the projected overages appear to be more manageable, suggesting room for review or negotiation to permit mitigation of the personnel turbulence caused by the workload reduction.

Fig. 3 shows the projected effect on hiring and firing that each of the model types indicate. The no fires alternative freezes employment during the downturn with some hiring after the workload stabilizes at a lower level of effort. The forced fit alternative produces the widest swings in firing and then rehiring since the corrections to the workload/workforce balance are taken immediately in the periods in which they occur. In the best fit alternative, the swings are less drastic with the most substantial reductions taken in the first period. (It should be noted that there can be both hiring and firing in the same period since there may be some skill shortages even in the midst of the downturn. This can lead to additional analysis to see if retraining rather than rehiring should be done.)

From the charts one can see that either an employment freeze or a strict adherence to preassigned workload projections will result in the most extreme discontinuities. The use of the charts by the top management of the shipyard caused a change in philosophy to: (a) rearrange the workload of the shipyard to ensure smoother personnel transitions, (b) seek more work in the earlier periods from the headquarters group which controls the shipyards, and (c) negotiate with the other shipyards for suitable workload packages which could be transferred. In the end the actual workload of the shipyard very closely matched the best fit profile.

## 4. Implementation of the DSS

This DSS application was fortunate to be able to build upon a wide variety of civilian personnel planning models and supporting information systems which the U.S. Navy had developed starting in 1968. (See Charnes, Cooper and Niehaus [17], Niehaus [23] and Bres, Niehaus and Sholtz [11]). These mainframe based models were downsized to operate in a microcomputer environment starting with quick reaction fixes to meet urgent requests for information. At later stages of the effort, a major revision of the collection of models and reporting capabilities were integrated into a comprehensive microcomputer package which could be operated by members of the corporate and individual shipyard staffs. This revision was done by a contractor to ensure the development of well defined system design specifications and associated documentation and user manuals.

The use and improvement of the DSS was iterative and evolutionary. In the corporate planning application, the first versions were run by the DSS analyst using downloads from the mainframe system with the results presented to Admiral in charge of the shipyards. The outputs were revised based on these discussions and stable spreadsheets developed. The first version had the complete models embedded in a spreadsheet such that the calculations for each of the shipyards was done at one-at-a-time. These complete spreadsheets for all eight shipyards, updated with the latest data sets, were provided to the shipyard planning organization. The spreadsheet was designed for use at both the corporate and individual shipyard levels.

Later, the spreadsheets were revised to accommodate the optimization models. Development and testing was done at one of the naval weapons stations responsible for maintenance and update of the engineering changes and standards related to all of the computer control systems for the missile weapons systems aboard Navy ships. Because of the need to speed up the processing, the spreadsheet macros were revised to make the computation intense calculations outside the spreadsheet using several computer programs written in FORTRAN. This spreadsheet capability was reinstituted in the DSS developed to assist in studies at Mare Island shipyard.

## 4.1. Exploratory development and use

The DSS was developed on an prototype basis with simultaneous use by the shipyard management officials. During the initial NAVSEA headquarters studies the outputs were handcrafted using a combination of mainframe and microcomputer approaches. Since only the simple models were involved, the system was developed using a set of macros in LOTUS 1-2-3. The personnel transition data were developed using the mainframe CAMAS software. As with the current MCAMAS, strength data and other aggregate numbers were hand entered into the spreadsheet. The output displays are developed from printing portions of the spreadsheet.

The rates of movement (transition rates) between personnel categories defined by occupation and responsibility level are fundamental features of these models. These data are estimated from historical data available through CAMAS, which at the time operated only on a mainframe computer. The transition rates are used to project the movement of the current workforce and future hires by the periods used in the particular model sturdy.

A number of needed features became apparent very early. The first of these was the desire to ensure more stability in the transition rates. The response was to develop a weighted average of the data using the relevant last three periods. A FORTRAN program was written using the CAMAS transition data to make the calculations and read the results into the spreadsheet. In this subsystem each transition matrix used in the shipyard study is a weighted average of the data from the last three years. For example, the April-June transition matrix used in the projections is computed from the data for that quarter in 1987, 1988, and 1989. Data for these three years were given weights of 1, 2 and 3, respectively for the weighted average. That is, the final transition matrix was a composite of data using the 1987 data multiplied by one-sixth, the 1988 data multiplied by one-third, and the 1989 data by one-half.

With the initial simple models in use, attention was placed on developing the goal programming optimization models. At the time, the issue under study was the balancing of the personnel in the blue and white collar occupations. A goal-arc distribution model (See Charnes, Cooper, Lewis, and Niehaus [14,15] and Charnes, Cooper, Nelson and Niehaus [16]) which had been developed during research into civilian equal employment opportunity planning (and later Navy military sea/shore personnel distribution) was downloaded from an IBM 3083 for operation on an IBM PC/AT. The conversion to the microcomputer was straight forward since the software was in a version of FORTRAN acceptable to the IBM PC Professional FORTRAN compiler. The spreadsheet was modified with special menus to accept the input data while taking the computational intensive operations out of the spreadsheet by means of a separate FORTRAN program. The final results are read back into the spreadsheet for retention and printing.

The goal programming models were actually developed for a large naval shore installation which became interested in using the CAMAS models for recruitment planning for its professional engineering staff. In addition to the goal arc models, experimentation was started on the possibility of adapting a mainframe model using a commercially available microcomputer linear programming package. In this case the LINDO package was chosen based on discussions with colleagues at Carnegie-Mellon University and the University of Texas.

## 4.2. User oriented capabilities

Many of the tricks developed during the mainframe days were adapted for use on the microcomputer. A FORTRAN program was written to take advantage of the reduced dual formulation of the goal programming model which had originally been developed in the late 1970s. (For the formulation see Bres, Niehaus, and Sholtz [11]). A reduced dual formulation reduces the size of the actual problem to be solved, thus easing computational requirements (see Charnes and Cooper [13]; Armstrong and Hultz [4]).

Over several years, the LOTUS spreadsheet was improved with special menus for the various functions, the Flex model was added and eventually the Best Fit Flex model included. By 1990,

![](/api/attachments/HZ5UJYKT/fulltext/images/5bff9d81112e7a45601f323a503d90414e2a576854d26f0e4e46fd4570d27e47.jpg)  
Fig. 4. MCAMAS run sequence.

Table 1

<table><tr><td>Table 1</td></tr><tr><td>MCAMAS Main Menu</td></tr><tr><td>(1) Create/Edit Data Files</td></tr><tr><td>(2) Extract Gains/Losses</td></tr><tr><td>(3) Model Data Preparation</td></tr><tr><td>(4) Simple Flow Model</td></tr><tr><td>(5) Best Fit Model</td></tr><tr><td>(6) Exit</td></tr><tr><td>Please Select by Number</td></tr></table>

with the exception of the personnel transition data, all the models could be run by a mid-level staff person after a few days training. Basically all that had to be done was to follow the MCAMAS run sequence in Fig. 4 and then know how to translate the data into previously developed Harvard Graphics files if graphical outputs were desired.

Most of the training involves running real life situations through the system. This was done by first running a real life example through the system explaining each step. Then, the mid-level staff person was given additional scenarios needed at the time and asked to run the system with tutoring. The results were translated into a management presentation for a decision meeting of top management officials. At the decision meeting, additional changes were requested. At this point the mid-level staff person was asked to make the changes without any outside help. Finally, these changes were reviewed with needed corrections, if any, provided. At this point the staff analyst was on her (his) own with consultation available by telephone if difficulties arose. Generally, the transition went very smoothly once there was confidence on the part of the user.

Because it was clear that the modelling capability should be available to the larger shore installations, work was started in 1989 to streamline the information support system. Attention was placed on making the complete capability accessible from a 386/486 microcomputer. Model solution times have been reduced from over an hour to a few minutes using the LINDO 386 package. A menu-driven shell system was written in the "C" programming language which integrates the complex of capabilities involving LOTUS 1-2-3, LINDO, FORTRAN and COBOL programs, Harvard Graphics, and a word processing package. This MCAMAS capability includes a personnel transition rate subsystem to permit downloading of the basic personnel data from the Defense Civilian Personnel Data System (DCPDS), the Department of Defense (DoD) corporate data base covering civilian personnel.

Tables 1 and 2 show the primary menu screens used in MCAMAS from which various sub menus are accessed. The screen in Table 1 is used for access to the system functions. The functions in the screen in Table 2 are used to extract the personnel files from the DCPDS and build transition rate, projected retirement and salary distribution files and reports. In addition, spreadsheet and word processing menus are used to make model data changes and develop the output reports

Table 2  
MCAMAS Data Files Function Selection Menu

<table><tr><td>Run Flag</td><td></td><td>Function</td></tr><tr><td>N</td><td>MME</td><td>- Build Personnel Master File Extracts</td></tr><tr><td>N</td><td>JCLEMM</td><td>- Run Personnel Master File Level Fix</td></tr><tr><td>N</td><td>MMX</td><td>- Aggregate DONOL Occupation Level Codes</td></tr><tr><td>N</td><td>MOE</td><td>- Extract Retirement Eligibles and Non-Eligibles</td></tr><tr><td>N</td><td>MTH</td><td>- Build Transition Rate Reports</td></tr><tr><td>N</td><td>MTJ</td><td>- Produce Transition Rate Reports</td></tr><tr><td>N</td><td>MNP</td><td>- Combine Transition Rate Matrices</td></tr><tr><td>N</td><td>MTI</td><td>- Build GOALARC File</td></tr><tr><td>N</td><td>MOL</td><td>- Produce Expected Retirement Report</td></tr><tr><td>N</td><td>MSA</td><td>- Produce Salary Distribution Reports</td></tr></table>

Run Flag: Y = Run, N = Don't Run  
SPACE = Move Highlight, F1 = Accept Selections, ESC = Exit MCAMAS

Further rationalization of the MCAMAS support system may be accomplished at some point in the future. For example, the report output capabilities could be improved and the graphics outputs integrated with the spreadsheet data. More than likely any such improvements would be accomplished using a shell development system such as Object Vision or macros within EXCEL along with related WINDOWS based packages.

Beta tests of the menu-driven package have been completed at Mare Island shipyard. Additional installations are also being started at other naval shipyards. These MCAMAS capabilities are now ready for export across the Navy as well as for other DoD installations.

## 4.3. Shipyard DSS

Fig. 5 shows the DSS which finally resulted at the shipyard level. Here, the MCAMAS models became part of a much larger integrated system of models and transaction reporting capabilities being tested for use by all eight of the shipyards. This system was developed to run on microcomputers with some downloads from mainframe databases such as the Defense Civilian Personnel Data System (DCPDS). The DSS has both strategic, and tactical components.

The DSS developed at Mare Island shipyard is aimed at integrating workload and workforce planning. This system has both “top down” and “bottom up” components. The purpose is to provide rapid evaluation of short and long term workload and workforce quality/quantity issues. Skills balancing strategies are developed at both the individual shop and cross-organizational levels. Particular attention is placed on identifying and tracking the core workforce.

The workload analysis part of the DSS produces two types of reports. There is the workload forecasting model producing one to seven year studies by shop. These outputs are complemented by one to three year workload profiles by trade skill. The heart of the shorter range or one to three/four year workforce planning is total shipyard analysis using the types of model outputs briefly described at the beginning of this paper. Analyses are produced comparing “no hiring”, “force-fit to goals” and “best-fit to goals” management options. The system involves an eight period model which uses quarters to the end of the first full fiscal year and years thereafter. The shipyard-wide reports are extended to the shop level by deterministic models producing monthly workforce plans and trade level manning plans.

![](/api/attachments/HZ5UJYKT/fulltext/images/4351b3fd82f0ba085ae862bd0599a94695f6333c250b746a10506cab1d690e6a.jpg)  
Fig. 5. Mare Island Shipyard workload/workforce decision support system.

Attention at the strategic level is more on macro decisions using more aggregate numbers to frame the scenarios at the total shipyard level. The strategic component uses the MCAMAS flow models. The tactical component uses the output of the strategic component as well as the more micro planning done at the individual shop level. Focus in the Work Load/Work Force Forecasting (WLFC/WFFC) and Employee Development Information Computer Tracking System (EDICTS) components is on shorter term monthly planning keyed to individual workload packages. Outputs include monthly and more frequent reports on available manning and training requirements by skill for each of the individual shops.

## 5. Conclusion

This report traces the development of an operational decision support system application which has had short and long term payoffs from its inception. The application illustrates how DSS capabilities are used in actual decision making situations. Generally, the situation has been rough and fluid with built in conflicts and strong points-of-view on most if not all of the critical issues involved. In many cases the DSS capabilities provided a way to set the bounds in dealing with uncertainty during the strategic turns of the decision making process. The same capabilities were later used in the control phase during the tactical implementation of the strategic decisions.

There have been both significant management achievements and technical improvements as a result of this application. The management achievements include:

\- Assistance in projecting management actions required for the initial drawdown of the eight U.S. public shipyards by 8000 jobs without any significant management directed RIFs.

\- Restructuring the personnel policies of the naval shipyards focusing on a nucleus of skilled and qualified workers supplemented with “on-call” workers permitting more flexibility for management while providing a viable employment arrangement which protects the basic benefits of the workers;

\- Analysis of the occupational structure issues at the shipyard level permitting a better understanding of the internal flows of the workforce particularly as it relates to movements between blue and white collar workers;

\- Integration of the strategic and tactical planning in the development of a workload-workforce decision support system which brings together workload planning requirements with personnel staffing;

\- Analytic assistance in the development of the strategic plans for two major reductions at one of the naval shipyards allowing the development of an effective outplacement program recognized as the best such effort in the U.S. Department of Defense; and

\- Extension of the decision support system to the analysis of longer term shipyard training needs during major workforce reductions which preserved the apprentice program.

The technical improvements were accomplished at minimum cost using a small number of knowledgeable in-house staff and for the most part available computer hardware and existing or inexpensive microcomputer software. Up until the recent development of the MCAMAS information support system, most of the staff hours were on a part time basis with several other studies and applications underway as well. Even in the latter case, the MCAMAS software and documentation were developed using very small contractor task orders with less than two work-years expended.

In a real sense, these applications are one of the payoffs of the U.S. Navy's long term commitment to the use of decision support systems for human resource planning. They show that when both the strategy and structure of development and implementation work together, the payoffs reinforce one another providing a robust environment for continued improvements.

## Appendix

## MCAMAS models

This DSS application was fortunate to be able to build upon and use the wide variety of civilian personnel planning models and supporting information systems which the U.S. Navy has developed starting in 1968. (See Charnes, Cooper and Niehaus [17], Niehaus [23] and Bres, Niehaus and Sholtz [11]). Several model methodologies are incorporated into the MCAMAS decision support system. The models include: (1) no hires, (2) force fit, and (3) best fit views of the future. The “no hires” case assumes there will be no replacement of losses from the outside with normal personnel flows permitted to continue within the organization. The “force fit” case assumes that workload requirements will be balanced precisely at each time period with adjustments accommodated through external additions or deletions to the workforce. Normal internal personnel flows are permitted to continue. The “best fit” case assumes the balancing of the workforce within each period as well as over time. This permits some management flexibility both in the internal movements and external additions or deletions to the workforce. A brief review of the methodology of each is discussed below.

## Definition of variables

The definition of variables for the MCAMAS models is as follows:

$E_{k}^{+}(t),E_{k}^{-}(t)=$ Positive or negative deviation, respectively, for the $k^{th}$ personnel category in time t.

$x_{k}(0)$ = Initial inventory of personnel in category k.

$x_{k}(t)$ = Personnel on-board (in place) in the $k^{th}$ personnel category in time t.

$M_{ik}(t)$ = Personnel movement or transition rate between the $i^{th}$ personnel category and the $k^{th}$ personnel category for designated time period.

<table><tr><td> $G_{k}(t)$ </td><td>= Personnel requirement (goal) for the  $k^{th}$  personnel category in period t.</td></tr><tr><td> $y_{k}(t)$ </td><td>= Hires in the  $k^{th}$  personnel category in period t.</td></tr><tr><td> $z_{k}(t)$ </td><td>= Excess personnel or reductions-in-force (RIFs) in the  $k^{th}$  personnel category in period t.</td></tr><tr><td> $\alpha_{kt}$ </td><td>= Penalty for a positive goal discrepancy for the  $k^{th}$  personnel category in period t.</td></tr><tr><td> $\beta_{kt}$ </td><td>= Penalty for a negative goal discrepancy for the  $k^{th}$  personnel category in period t.</td></tr><tr><td> $\gamma_{kt}$ </td><td>= Penalty for a hire in the  $k^{th}$  personnel category in period t.</td></tr><tr><td> $\delta_{kt}$ </td><td>= Penalty for an excess person or reduction-in-force (RIF) the  $k^{th}$  personnel category in period t.</td></tr><tr><td>C(t)</td><td>= Total personnel ceiling for period t.</td></tr><tr><td> $s_{k}(t)$ </td><td>= Average salary for the  $k^{th}$  category in period t.</td></tr><tr><td>B(t)</td><td>= Salary budgetary ceiling for the period t.</td></tr><tr><td>T</td><td>= Number of time periods in the planning horizon.</td></tr></table>

No hires model

The “no-hires” model uses a simple Markov model with no replacement. All that is done is to sequentially multiply the vector of personnel by job category by a matrix of personnel movement rates for the number of periods to be projected, or:

$$
\mathrm{x} _ {\mathrm{k}} (\mathrm{t}) = \sum_ {\mathrm{i}} \mathrm{x} _ {\mathrm{j}} (\mathrm{t} - 1) \mathrm{M} _ {\mathrm{ik}} (\mathrm{t}), \mathrm{t} = 1, \dots , \mathrm{T}
$$

The personnel transition rates can be different for each of the periods with only the condition that the length of the particular period to be projected be the same as that for which the transition rates were obtained. Assuming the data is available and reasonably stable, smoothing of the transition rates may be useful (such as using weighted averages of several similar past periods). The “no-hires” models is best used in the preliminary stages of a downsizing to demonstrate that a more reasoned approach may be needed to ensure some replacements in critical job categories or areas of high attrition.

Force fit model

The “force fit model” uses specific staffing goals for each occupation and level in each planning period. Hires and fires are determined after projecting the prior workforce using historical transition rates and comparing the remaining workforce to the targets. The hire and fire numbers are totalled separately. The goals reflect anticipated workload over the planning periods. This is called a force fit model since workforce targets must be exactly met. All that is done in this case is to use the simple Markov models with sufficient replacement to meet the job category targets. For many management decisions this is all that is required particularly during the preliminary development of alternatives. This model can be stated as:

$$
\begin{array}{l} \mathrm {G_ {k} (t) - \sum_ {i} x_ {k} (t - 1) M_ {ik} (t - 1) - y_ {k} (t)+ z_ {k} (t)} \\ = 0, t = 1, \dots , T \\ \text {where y_{k} (t), z_{k} (t)\geqslant 0 and y_{k} (t) z_{k} (t) = 0} \\ \left(i. e. n o t b o t h y _ {k} (t) a n d z _ {k} (t) > 0\right) \end{array}
$$

Best fit model

The issue is simultaneously meeting management targets as closely as possible, while allowing consideration of planning alternatives would be better for shipyard and Navy missions. The optimization models have been engineered to look at several versions of the underlying situation. In many situations, there are strong management or external constraints (e.g., the ability to hire required skilled employees) that will affect the outcome. These constraints may make it impossible or at least inadvisable to meet the detailed staffing goals precisely in each planning period. The best one can hope for is to meet the goal as closely as possible.

The overall idea of the best fit model can then be stated as:

Minimize deviations from manpower and promotion goals, hiring and firing

Subject to:

Personnel on-board

Projected workforce flows

Hiring constraints

Workforce ceiling constraints

Salary budget constraints

These goal programming models combine projected personnel flows and staffing goals for each category along with management and external constraints. Solutions of these models give recommended hires, fires, and staffing targets to come as close as possible to specified requirements over the entire planning horizon, given the identified constraints. Mathematically, the model can be stated as:

$$
\begin{array}{l} \text { Min } \sum_ {t} \sum_ {k} \left[ \alpha_ {k t} E _ {k} ^ {+} (t) + \beta_ {k t} E _ {k} ^ {-} (t) + \gamma_ {k t} y _ {k} (t) \right. \\ \left. + \delta_ {k t} z _ {k} (t) \right] \\ \text { subject   to: } \\ \text { Goal   Constraints: } \end{array}
$$

$$
\mathrm{G} _ {\mathrm{k}} (\mathrm{t}) - \mathrm{x} _ {\mathrm{k}} (\mathrm{t}) + \mathrm{E} _ {\mathrm{k}} ^ {+} (\mathrm{t}) - \mathrm{E} _ {\mathrm{k}} ^ {-} (\mathrm{t}) = 0
$$

Personnel Transition Conditions

$$
\mathrm{x} _ {\mathrm{k}} (t) - \sum_ {i} \mathrm{M} _ {i \mathrm{k}} (t) \mathrm{x} _ {i} (t - 1) - \mathrm{y} _ {\mathrm{k}} (t) + \mathrm{z} _ {\mathrm{k}} (t) = 0,
$$

Personnel Ceiling Constraints:

$$
\sum_ {k} x _ {k} (t) \leqslant C (t)
$$

Salary Budget Constraints:

$$
\sum \mathrm{s} _ {\mathrm{k}} (\mathrm{t}) \mathrm{x} _ {\mathrm{k}} (\mathrm{t}) \leqslant \mathrm{B} (\mathrm{t})
$$

Non-negativity Constraints:

$$
\mathrm{x} _ {\mathrm{k}} (t), \mathrm{y} _ {\mathrm{k}} (t), \mathrm{z} _ {\mathrm{k}} (t), \mathrm{E} _ {\mathrm{k}} ^ {+} (t), \mathrm{E} _ {\mathrm{k}} ^ {-} (t) \geqslant 0
$$

The best fit model includes salary budget constraints. However, experience has shown that in the shipyard planing case that the addition of the total personnel ceiling to be sufficient to reflect corporate controls on the outcomes.

Flex model

Methods other than firing could be used to deal with excess personnel. Detailing to other jobs, cross-assignment, and work rescheduling have all been used to deal with this situation. For most occupations, higher level positions are filled by internal promotion. These internal promotions create vacancies at lower levels that are usually filled by external hires. The lower level vacancies could alternatively be filled by excess employees in other occupations. A special version of the optimization model, called the “flex model” was developed to explicitly recognize these management flexibilities and allow changes to projected transfer and promotion rates for all the job categories under study. The mathematical structure of this non-linear goal-arc model can be found in Charnes, Cooper, Nelson and Niehaus [16]. This model was reformulated from the mainframe to run on a microcomputer using specialized optimization software.

Operational examples using Mare Island shipyard data were developed to study occupational structure issues particularly as related to the transfers between blue and white collar occupations. The difficulty of the Flex model was that it permitted more flexibility than exists in the constrained world of shipyard management. For this reason, a controlled version of a promotion planning model originally developed in the 1970s for EEO planning and naval laboratory professional personnel promotion planning was adapted to permit limited flexibility in modelling shipyard personnel movements.

## Best fit flex model

The force fit model has been useful for quick results that provide approximate management guidance for the overall business outcomes. However, the force fit model doesn't have enough flexibility to deal with wide swings in workload over the planning period that are best met by changing traditional workforce flows. On the other hand, the flex model was found to allow too much flexibility to target specific staffing areas where more management attention should be placed. The microcomputer version of the flex model also can't represent additional constraints as well as the best fit model. To accommodate these concerns, a “best fit flex” model has been developed. This model adds selective promotion flexibility to the best fit model. Demotions, while included in the original promotion planning and flex models, were not included this formulation. Also, promotions were only permitted within a given job category constrained by a percentage of the promotion rate.

The best fit flex model involves adding the following additional variables to the best fit model:

$\theta_{\mathrm{ikt}} =$ Weight applicable to the transfers (above the historical promotion rate) of personnel from job category i to job category k, where i and k are lower and higher levels of the same occupation in period t.

$\xi_{\mathrm{ikt}} =$ Weight applicable to the expected transfers not allowed (below the historical promotion rate) for personnel from job category i to job category k, where i and k are lower and higher levels of the same occupation in period t.

$q_{ik}(t) = \text{Number of personnel in job category i who transfer (are promoted) to job category k in period t above the historical rate.}$

$r_{ik}(t) = \text{Number of personnel in job category i who do not transfer (are not promoted) to job category k in period t who would have been expected to transfer (i.e. the number below the historical rate).}$

$T_{ikt}$ = Matrix of admissible flexible transfers for time t. ( $T_{ikt} = 1$ if flexible transfers allowed; = 0 otherwise).

The model then becomes:

$$
\begin{array}{l} \text {Min} \sum_ {\mathrm{t}} \sum_ {\mathrm{k}} \sum_ {\mathrm{i}} \left[ \alpha_ {\mathrm{kt}} \mathrm{E} _ {\mathrm{k}} ^ {+} (\mathrm{t}) + \beta_ {\mathrm{kt}} \mathrm{E} _ {\mathrm{k}} ^ {-} (\mathrm{t}) \right. \\ \left. + \gamma_ {\mathrm{kt}} \mathrm{y} _ {\mathrm{k}} (\mathrm{t}) + \delta_ {\mathrm{kt}} z _ {\mathrm{k}} (\mathrm{t}) + \theta_ {\mathrm{ikt}} q _ {\mathrm{ik}} (\mathrm{t}) + \xi_ {\mathrm{ikt}} r _ {\mathrm{ik}} (\mathrm{t}) \right] \end{array}
$$

subject to:

Goal Constraints:

$$
\mathrm{G} _ {\mathrm{k}} (t) - \mathrm{x} _ {\mathrm{k}} (t) + \mathrm{E} _ {\mathrm{k}} ^ {+} (t) - \mathrm{E} _ {\mathrm{k}} ^ {-} (t) = 0
$$

Personnel Transition Conditions:

$$
\begin{array}{r l} & \mathrm {x_ {k} (t) - \sum_ {i} M_ {ik} (t) x_ {i} (t - 1)- y_ {k} (t)+ z_ {k} (t)} \\ & \quad - \sum_ {i} T _ {i k t} q _ {i k} (t) + \sum_ {i} T _ {i k t} r _ {i k} (t) \\ & \quad + \sum_ {i} T _ {k i t} q _ {k i} (t) - \sum_ {i} T _ {k i t} r _ {k i} (t) = 0 \end{array}
$$

Promotion Constraints:

$$
\begin{array}{r l} \sum_ {k} T _ {i k t} q _ {i k} (t) - \left[ 1 - \sum_ {k} M _ {i k} (t) \right] x _ {i} (t - 1) & \geqslant 0 \\ - r _ {i k} (t) + M _ {i k} (t) x _ {i} (t - 1) & \geqslant 0 \end{array}
$$

(for all $i, k$ such that $T_{ikt} = 1$ ; note that $q_{ik}(t), r_{ik}(t) = 0$ for $i, k$ such that $T_{ikt} = 0$ ).

Personnel Ceiling Constraints:

$$
\sum_ {k} x _ {k} (t) \leqslant C (t)
$$

Salary Budget Constraints:

$$
\sum_ {k} s _ {k} (t) x _ {k} (t) \leqslant B (t)
$$

Non-negativity Constraints:

$$
\mathrm{x} _ {\mathrm{k}} (\mathrm{t}), \mathrm{y} _ {\mathrm{k}} (\mathrm{t}), \mathrm{z} _ {\mathrm{k}} (\mathrm{t}), \mathrm{E} _ {\mathrm{k}} ^ {+} (\mathrm{t}), \mathrm{E} _ {\mathrm{k}} ^ {-} (\mathrm{t}), \mathrm{q} _ {\mathrm{ik}} (\mathrm{t}),
$$

$$
r _ {i k} (t) \geqslant 0
$$

## References

[1] Aguilar, M., R.J. Niehaus and F.J. Sharkey, Management of a Major Downsizing at a Naval Shipyard, in R.J. Niehaus and K.F. Price, Eds. Bottom Line Results from Strategic Human Resource Planning, New York: Plenum Press, 1992.

[2] Aguilar, M., E.S. Bres, R.J. Niehaus and F.J. Sharkey, A Best Fit Planning Model for Managing Personnel Turbulence, in R.J. Niehaus and K.F. Price, Eds. Human Resource Strategies for Organizations in Transition, New York: Plenum Press, 1990.

[3] Andriole, R.H., Handbook of Decision Support Systems, Blue Ridge Summit, PA: TAB Books, 1989.

[4] Armstrong, R.D. and J.W. Hultz, An Algorithm for a Restricted Discrete Approximation Problem in the $L_{1}$ Norm, SIAM Journal of Numerical Analysis, 1977, 14 (3), 555–565.

[5] Blanning, R.W., C.W. Holsapple and A.B. Whinston Eds., Decision Support Systems: Special Issue on Model Management Systems, 9 (1993), 19–37.

[6] Bonczek, R.H., C.W. Holsapple, and A.B. Whinston, Foundations of Decision Support Systems, New York: Academic Press, 1981.

[7] Boza, T.B. Flow Modelling Software for Human Resource Planning, Human Resource Planning, Vol. 1, No. 2. 1978. pp. 79–102.

[8] Bres, E.S., R.J. Niehaus, F.J. Sharkey, and C.L. Weber, Use of Personnel Flow Models for Analysis of Large Scale Work Force Changes R.J. Niehaus, Ed., Strategic Human Resource Planning Applications, New York: Plenum Press, 1987.

[9] Bres, E.S., R.J. Niehaus, F.J. Sharkey, and C.L. Weber, Coping with Occupational Structure Issues at Large Public Industrial Organizations, R.J. Niehaus and K.F. Price, Eds., Creating the Competitive Edge through Human Resource Applications, New York, Plenum Press, 1988.

[10] Bres, E.S., R.J. Niehaus, and D. Sholtz, Shore Activity Manpower Planning Models, NPRDC TR 79-10, San Diego: Navy Personnel Research and Development Centre, 1979.

[11] Bulla, D.N. and P.M. Scott, Manpower Requirements Forecasting: A Case Example, in R.J. Niehaus, Ed. Strategic Human Resource Planning Applications, New York: Plenum Press, 1987.

[12] Charnes, A. and W.W. Cooper, Management Models and Applications of Linear Programming (New York: John Wiley and Sons, Inc., 1961).

[13] Charnes, A., W.W. Cooper, K.A. Lewis and R.J. Niehaus, A Multi-Objective Model for Planning Equal Employment Opportunities in M. Zeleny, Ed., Multiple Criteria Decision Making: Kyoto 1975 (New York: Springer Verlag, 1976).

[14] Charnes, A., W.W. Cooper, K.A. Lewis, and R.J. Niehaus, A Multi-Level Coherene Model for EEO Planning, in A. Charnes, W.W. Cooper, and R.J. Niehaus. Eds., Management Science Approaches to Manpower Planning and Organization Design, New York: Elsevier North-Holland, 1978. pp. 13–29.

[15] Charnes, A., W.W. Cooper, A. Nelson, and R.J. Niehaus, Model Extension and Computation in Goal-Arc Network Approaches for EEO Planning, INFOR, Vol. 20, No. 4, November 1982.

[16] Charnes, A., W.W. Cooper and R.J. Niehaus, Studies in Manpower Planning (Washington: U.S. Navy Office of Civilian Manpower Management, 1972), NTIS No. AD 055952.

[17] Emery, J.C., Management Information Systems: The Critical Strategic Resource (New York: Oxford University Press, 1987).

[18] Heyer, N.O. Managing Human Resources in a High Technology Enterprise in R.J. Niehaus, Ed., Human Resource Policy Analysis: Organizational Applications, New York: Prager, 1985.

[19] Keen, P.G.W. and M.S.S. Morton, Decision Support Systems: An Organizational Perspective (Reading, MA: Addison-Wesley, 1978).

[20] Manzini, A.O. and J.D. Gridley, Integrating Human Resources and Strategic Business Planning (New York: AMACOM, 1986).

[21] Mensch, G. and R.J. Niehaus, Eds. Work, Organizations, and Technological Change, New York: Plenum Press, 1982.

[22] Miret, P., Interactive Decision Support Systems: New Aids for Human Resource Policy Analysis and Formulation in R.J. Niehaus, Ed., Human Resource Policy Analysis: Organizational Applications, New York: Prager, 1985.

[23] Niehaus, R.J., Computer-Assisted Human Resources Planning, New York: Wiley Interscience, 1979.

[24] Niehaus, R.J., Human Resource Planning Flow Models, Human Resource Planning, Vol. 3, No. 4, 1980. pp. 177–187.

[25] Niehaus, R.J., Models for Human Resource Decisions, Human Resource Planning, Vol 11, No. 2, 1988.

[26] Quigley, M.O. and T.J. Henshaw, A Model to Simulate the Effects of Work Force Dynamics on Compensation Policy in R.J. Niehaus, Ed. Strategic Human Resource Planning Applications, (New York: Plenum, 1987).

[27] Smith, A.R., Ed. Manpower Planning in the Civil Service, Civil Services Studies 3, London: Her Majesty's Stationary Office, 1976.

[28] Sprague, R.H. and E.D. Carlson, Building Effective Decision Support Systems (Englewood Cliffs, NJ: Prentice Hall, 1982).

[29] Verhoeven, C.J., Instruments for Corporate Manpower Planning: Applicability and Applications, Eindhoven: University of Eindhoven, 1980.

[30] Weigel, H.S. and S.P. Wilcox, The Army's Personnel Decision Support System, Decision Support Systems, to appear in 1993.

![](/api/attachments/HZ5UJYKT/fulltext/images/9b038308ae50c190b9bb8bcdbad0ae0e8522ad13542fef7a5980a80283db6d37.jpg)

Richard J. Niehaus is Head, Program Management Branch for Manpower, Personnel and Training Information Resource Management in the U.S. Navy Office of the Chief of Naval Operations. He holds a B.S. in Physics from Santa Clara University, a M.S. in Industrial Administration from Carnegie-Mellon University and a D.B.A. from George Washington University. He was awarded the 1975 NATO Systems Science Prize for his

publications on the theory, modelling, data collection, computer systems development, organization and management of large-scale human resource planning systems. He has authored and/or edited ten books and written numerous papers which have appeared in such journals as Management Science, Naval Research Logistic Quarterly, INFO, Human Resource Planning, and the Monthly Labor Review.
