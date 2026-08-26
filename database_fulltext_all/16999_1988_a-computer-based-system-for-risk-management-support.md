---
otero_id: 16999
otero_key: "5BTP3MYW"
title: "A computer-based system for risk management support"
authors: "R.J. Peckham; P. Haastrup; H. Otway"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90011-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Computer-Based System for Risk Management Support

R.J. PECKHAM, P. HAASTRUP

and H. OTWAY

Joint Research Centre, Commission of the European Communities, Ispra, Italy

The scale and complexity of present day industrial operations involving hazardous substances are such that managers are faced with increasingly demanding decision problems. They must simultaneously consider technological, economic, environmental and sociopolitical factors. As a response to this problem a computer based decision support system is being developed to support risk management activities, with special emphasis given to hazardous chemicals. The IRIMS (Ispra Risk Management Support) system is an attempt to integrate a number of data bases, containing information relevant to risk management, with several existing simulation models which can be used to address problems of environmental assessment, risk analysis and system optimisation. The system is designed to be user friendly and results are displayed through high resolution colour graphics allowing the non specialised user to obtain a “feel” for the problem under investigation. The paper describes the current prototype system, which is geared to handle problems on a European scale, and plans for further developments which will allow more detailed studies on particular countries or regions.

Keywords: Decision Support System, Risk Management.

Robert J. Peckham graduated in Physics from Imperial College, University of London, and then did research for higher degrees at the University of Manchester, Nuffield Radio Astronomy Laboratories, Jodrell Bank. For the last ten years he has worked in the Technology Assessment Sector at the JRC Ispra, in systems analysis and simulation applied to energy problems and risk management.

Palle Haastrup has a Ph.D. in Risk Assessment from Risoe National Laboratory and the Technical University of Denmark. He joined the Technology Assessment Sector at the JRC Ispra in 1986, where he engaged in research and developments in risk management, decision support systems, and advanced informatics.

## 1. Introduction

It is now recognised that the successful management of the risks associated with the production, transportation and use of hazardous substances requires that the complete system, including interactions between sub-systems, be considered in analysis (Otway and Peltu, 1985). This implies the simultaneous access to a large amount of information relating to the substances themselves, the production processes and facilities, the transport networks and the environment. In addition to having this information to hand it is also necessary to be able to simulate various scenarios and explore the consequences of different decisions and strategies.

Normally, this would require enormous computing capacity, however the needs of risk managers are less for very detailed technical information than for less-accurate, but more comprehensive analysis. Thus, in the framework of the JRC Industrial Risk Programme, a prototype management support system has been developed to explore the possibilities of using advances informatics techniques and facilities as aids to the management of hazardous substances. This system has been called the IRIMS – Ispra Risk Management Support – System, and was developed by the JRC with support from a series of study contracts given to the International Institute for Applied Systems Analysis (Fedra, 1985).

The IRIMS system is an attempt to integrate a number of data bases containing information relevant to risk management together with several simulation models which can be used to address problems of environmental pollution, risk calculation and optimisation. The system has been implemented using modern methods of information management which allow the interconnection of different modules, and is interfaced to the user through high resolution colour graphics and user friendly menus. This means that simulations can be rapidly set up and run by the user, and repeat runs with varied parameters can be quickly obtained. The graphical display of the results allows the user to obtain a feel for the problem under investigation and concentrate his attention on the most significant parameters without being overwhelmed by too much information.

The present version of the system is a demonstration prototype which will be used to illustrate and explore the potential of this kind of integrated system. The structure is open in the sense that new modules can be added as they become necessary, and all new modules will, in principle, be interconnectable with existing ones and have access to existing data bases. Thus, once the basic structure of the system has been created and tested, it has the possibility of becoming a very comprehensive and general purpose aid to the management of industrial risks. It can also be adapted for any particular problem application and still have the advantage that much relevant information will already exist within the system.

## 2. System Overview

The system is implemented on a SUN-3/160 Workstation running under the UNIX Operating System. This operating system allows both program and data base modules to be stored and manipulated using 'tree structured directories'. Interconnections between different modules can thus be achieved by specifying the appropriate 'path' from one file or directory to another while at the same time all information is stored in an orderly and systematic way. Another strength of the UNIX operating system is that it supports several different programming languages and allows the connection of modules in these different languages. This means that program modules which already exist, and which have been thoroughly tested, can be readily integrated and be made to drive or be driven by other modules.

The workstation uses a high resolution (1152 × 900 pixel) colour display for interactive input and output. Once the system is in operation it is controlled mainly by using a pointing device (mouse) in conjunction with the presented menus. The menus are largely self explanatory and always contain instructions on how to use the pointing device or how to obtain an explanation of the current options. The different modules can all be accessed from the main menu, which presents the following options (see also Fig. 1):

Hazardous Substances Databases
Industrial Accidents Reports
EC Directives and Regulations
Geographical and Regional Databases
Chemical Industry Databases
Industrial Structure Optimisation
Chemical Production Technologies
Process Plant Risk Analysis: SAFETI
Industrial Waste Streams Database
Transportation Risk/Cost Analysis
Environmental Impact Assessment
Multi-Criteria Data Evaluation
Explain Current Menu Options
Stop and Quit

Selecting any of these options (apart from the last two) leads to a new menu of options and explanations dealing with the module concerned. The following sections describe the contents and functions of these modules.

## 3. Data Bases and Facilities for Their Access

As said earlier, the system contains a number of data bases which can be accessed either by the user in search of specific information or by particular program modules which make use of the information for simulations or calculations. They are described here.

## 3.1. The Chemical Substances Data Base

A Chemical Substances Data Base is of fundamental importance to any system or manager attempting to address risk problems relating to hazardous substances. This data base must therefore contain entries for all the relevant substances, and for each substance it must contain information relating to the basic physical and chemical properties, the health and risk properties (toxicity, reactivity, flammability etc) and the appropriate production processes and waste streams.

<table><tr><td>IRIMS TOP LEVEL MASTER MENU:</td></tr><tr><td>Hazardous Substances Database</td></tr><tr><td>Industrial Accidents Reports</td></tr><tr><td>EC Directives and Regulations</td></tr><tr><td>Geographical and Regional Databases</td></tr><tr><td>Chemical Industry Databases</td></tr><tr><td>Industrial Structure Optimization</td></tr><tr><td>Chemical Production Technologies</td></tr><tr><td>Process Plant Risk Analysis: SAFETI</td></tr><tr><td>Industrial Waste Streams Database</td></tr><tr><td>Transportation Risk/Cost Analysis</td></tr><tr><td>Environmental Impact Assessment</td></tr><tr><td>Multi-Criteria Data Evaluation</td></tr><tr><td>EXPLAIN CURRENT MENU OPTIONS</td></tr><tr><td>SELECT TO STOP AND QUIT IRIMS</td></tr></table>

to select a menu item, position the mouse pointer, and press the left mouse button ...

Fig. 1. The main menu, from which the different modules can be accessed.  
![](/api/attachments/5BTP3MYW/fulltext/images/aece9546fa8443671b1b46a28a7dbf6b5192a739a4c6e24a373473a14f9ecbc5.jpg)

The data base has been constructed by filling in a questionnaire requesting all the properties of interest for each substance. The sources of information used to determine which substances to include in the data base and to fill in the questionnaire are ECDIN, European Community lists and regulations, and various national and international lists of hazardous substances. For each substance the questionnaire leads to a sequential data file. These sequential data files are converted into a random access data base for access by the user or by the simulation models in the system.

Prototype Demonstration Version 12/86.
All Rights Reserved.

When accessed by the user, the system displays one page of 25 substances at a time and for each

This software system is developed under contract to the Commission of the European Communities, CEC, Joint Research Centre, Ispra Establishment, Italy, by the International Institute for Applied Systems Analysis IIASA, A-2361 Laxenburg, Austria.

substance a set of ten flags indicates the following information:

if the chemical is on EEC list C 176/4

if the chemical is on EEC list C 167/7

if the chemical is on EEC list L 230/11

if the chemical is highly toxic

if the chemical is explosive

if the chemical is a water pollutant

if the chemical is flammable

if the chemical is corrosive

if the chemical is radioactive

if further information exists for the chemical

This information therefore gives a very brief overview of the hazard related properties of the substance. If the last flag indicates that more information is present on a substance the user can access a complete 'page' of information for that substance alone, providing more detailed information on the physical, chemical and health properties. This page is divided into five sections dealing with the following aspects:

basic description (name, state, appearance, odour etc),

health properties (toxicity, carcinogenicity, symptoms etc),

production processes,

physical properties (molecular weight, melting point, boiling point etc),

relevant legislation,

a graphic display of the molecular structure and HAZCHEM code.

The section on production processes can be used to page through each process for which information is present, one at a time. For each process the section provides a brief description, the amount produced and the main products and waste streams.

By using this data base the non-expert can rapidly gain knowledge and insight into the main risk-related properties of a substance as well as the quantities produced in Europe and the relevant waste streams. At the same time this information is present in the system for access and use by simulation models and for cross referencing with other data bases.

## 3.2. The Industrial Accidents Data Base

The Industrial Accidents Data Base provides a record of major industrial accidents involving hazardous substances. It contains a summary of the circumstances pertaining to each accident and the consequences incurred in terms of casualties, material and environmental damages. A large section of the graphical page of information is reserved for a colour map of the area surrounding the accident location. This is useful for illustrating to the analyst or decision maker the locations of residential areas, agricultural areas, roads or other industrial facilities which may have been affected by the accident.

When working with the data base, if the user wishes to obtain more detailed information on a particular chemical substance, he can reach that information in the chemical substances data base simply by selecting that substance with the pointing device. Similarly more detailed information on appropriate regulations and legislations can be accessed via the system of interconnecting data bases.

## 3.3. The Regulations and Legislation Data Base

This data base contains text files on relevant regulatory directives that have been issued for the handling of hazardous substances. Within the Chemical Substances Data Base, a reference is made to these regulations if there is a specific directive published for that particular substance.

The information in this data base can either be accessed directly from the main menu, or indirectly when working with other data bases or modules, eg, the chemical process simulation module.

## 3.4. The Regional and Geographic Data Base

The Regional and Geographic Data Base has two primary functions. Firstly it can be used to give the user a map orientated visual representation of the overall European picture with respect to a particular substance or problem, and secondly the information in it can be accessed and used by other modules which make simulations and risk calculations.

The geographical data base display program first generates a map of Europe onto which other spatially distributed information can be overlayed. The latter includes such details as major settlements, national road networks, rivers, lakes and political boundaries, together with major industrial plant and chemical storage locations and their respective coordinates. A zoom feature (currently implemented only for Holland) allows the user to see particular sub-areas in much greater detail. An example of this is shown in Fig. 2.

As geographical information is relevant to a number of the simulation models implemented in the IRIMS system, this data base supports the type of data required. For example, in order to be useful in the transport systems simulation module, the road network is specified in terms of arcs between pairs of settlements, which in turn have their population, names and co-ordinates stored. Information pertaining to the rivers includes the

![](/api/attachments/5BTP3MYW/fulltext/images/654b5b464c0c8ae58792a179f3c4a14c626cee288c7089d5b204558712e47a18.jpg)

Fig. 2. Example of the 'zoom' facility applied to the map of Holland.

length and average flow which will be made accessible by the river pollution simulation module.

and usefulness of the graphical approach as both a focus for discussion and an aid to decision making.

## 4. Environmental Simulation Models

The IRIMS system presently provides three environmental simulation models which allow the user to explore the consequences of potential industrial accidents involving the release of hazardous substances into the atmosphere, river water and ground water. In all three cases example problem descriptions are provided which can be modified interactively by the user to examine the effects of varying parameters such as the meteorology or the amount of a substance released. The results of the simulations are displayed graphically as the calculations proceed, and the most important quantities are also displayed numerically. These modules demonstrate the power

## 4.1. Long Range Atmospheric Transport

The model used is a Lagrangian transport model, based on Eliasson (1978). It provides a means by which the user can observe a symbolic representation of the long range atmospheric transport and the resultant effects of a simulated accident emitting a hazardous substance into the atmosphere, and gives the user the ability to adjust parameters and variables. The user specifies the following control variables:

the type and amount of substance emitted,
the location of the accident,
the season of the year and the time of day, the weather pattern (sun/rain and calm/normal/storm),

the duration of simulation, in days.

As the simulation proceeds the model displays the trajectory of the resultant cloud together with the calculated area contaminated, and ground concentration of the contaminant after one hour and six hours. An example trajectory is shown in Fig. 3.

## 4.2. River Pollution Module

The model used to illustrate the environmental impact of toxic chemicals being released into a river, is based in part on the river module of TOXSCREEN (Hetrick and McDowell-Boyer, 1979, 1984).

The dynamic simulation illustrated on the screen, shows the dispersion of a contaminant in a river or part of a river. This is done by dividing the river into a number of reaches, all of which have the same flow rate. The mass of pollutant is calculated for each time step in each reach using an equation similar to the one used in EXAMS (Smith et al., 1977; Burns et al., 1981). The rate of decay of the contaminant, due to several physical and chemical phenomena, can be defined initially by the following first order rate constants:

<table><tr><td>biodegradation,</td><td>(/day)</td></tr><tr><td>hydrolysis,</td><td>(/day)</td></tr><tr><td>oxidation,</td><td>(/day)</td></tr><tr><td>photolysis,</td><td>(/day)</td></tr><tr><td>volatilization.</td><td>(/day)</td></tr></table>

The user can also vary the contamination rate at the pollutant source. The pollutant concentrations, in each time step and in each reach, are then estimated over a given simulation time and displayed graphically as the simulation proceeds.

## 4.3. Groundwater Quality Simulation

The groundwater quality simulation is based on the two dimensional subsurface transport model FEFLOW (Diersch 1980, Diersch and Kaden 1984). This is a finite element model for the simulation of contaminant transport in porous media.

The model can be used to describe how a contaminant migrates from its source through a flowing groundwater field under specified hydrological conditions. This is useful for investigating the effects of, say, underground waste dumps on drinking water supplies. The model can be used to find the extent of the contaminant distribution after a certain elapsed time and to determine the effects of measures taken to divert or arrest the pollutant flow in certain directions, such as the use of additional pumping well or the insertion of impermeable barriers.

The background data required in order to run a problem simulation include the finite element mesh with initial and boundary conditions, hydrogeological data, (hydraulic head, porosity, acquifer thickness, etc.) and operational well data.

The system presently contains this information for a number of specific existing sites and generic problem descriptions for which the finite element mesh has already been generated. The user can modify particular parameters, such as pumping rates of various wells, and then observe the effects of these changes on the simulation.

The simulation module presents a graphical description of the two dimensional flow field, together with graphs of the pollutant concentration in observation wells and pumped well galleries.

Facilities are being developed which will allow the user to interactively create a complete problem description from scratch. This will include CAD based automatic generation of the finite element mesh.

## 5. Multi-Criteria Optimisation

The multi-criteria data evaluation module can be accessed directly from the top-level menu, or it can be operated as a post-processor from several other modules, in particular the transportation risk/cost analysis option. The module solves multicriteria optimisation problems having finite sets of alternatives. Solutions are presented graphically and the user can interactively change the criteria, reset constraints, and rerun the problem solver. This allows him to obtain a feel for the sensitivity of the solution to the various criteria and hence to add some elements of human judgement (by modifying his goals) to the otherwise formal mathematical approach.

Groundlevel concentration:
after 1h: ug/m3
after 6h: ug/m3

IRIMS Demo Prototype: Long-Range Atmospheric Transport

Industrial Accident Scenario
Location: 3.4 W 54.5 N
Substance: tracer
Amount released: 1000 kg

Season: Spring
Weather: sun/storm
Starting hour: 12 hrs
Simulation period: 5 days

Deposition estimates:
> 1. ug/m2: km2
deposition: kg
remaining: kg

![](/api/attachments/5BTP3MYW/fulltext/images/d5b08d13f59173ae9a661b67f64546064a0852b2493403cf08e09865dcc9ce37.jpg)  
to select a WEATHER PATTERN for the simulation, position the mouse pointer over the corresponding icon, and press the LEFT mouse button ...

Fig. 3. Example illustration of long range atmospheric transport.

The module incorporates features of several decision-support packages, in particular the Dynamic Interactive Decision Analysis and Support System (DIDASS) (Grauer et al., 1984). In this method the finite set of alternatives are first generated and listed together with all the relevant criteria. These could be for example a set of different possible transportation routes and the associated cost, risk and environmental damage estimates for each route. The user then specifies his objectives for all the criteria in terms of whether he chooses to maximise, minimise or ignore them.

The solution proceeds via two stages; first the non-dominated (Pareto) set of alternatives is found, and then from these the 'best' solution is determined according to the users specified preferences.

In selecting the 'best' solution the reference point approach is used (Wierzbicki, 1979, 1980). In this method the decision maker works interactively with the computer, firstly to obtain information about the available set of alternatives, such as the ranges and distributions of the various criteria, and then to specify his goals by means of a reference point. The reference point need not necessarily be obtainable, but the algorithm will find the single alternative which comes closest to it.

As an aid to this process the user can view the information on the set of alternatives as either scattergrams (plotting any criterion against any other) or as frequency distributions. The set of alternatives on which the algorithm is to operate can also be reduced in number by cutting out all those which have a value of a criterion above or below a certain threshold.

If the solution obtained is not satisfactory for some reason the decision maker can modify his goals (reference point) and re-run the problem solver.

## 5.1. Application to Transport System Optimisation

The optimisation of the risks and costs associated with the transportation of hazardous substances is supported by an interface which allows the user to create problem descriptions for analysis by the multi-criteria evaluation module.

This interface allows the user to select a type and quantity of substance for transportation, and to define the HAZCHEM ratings for toxicity, fire hazard and reactivity. After a source and destination have also been specified the interface makes use of information in the geographical data base in order to determine all the viable transportation paths between the two locations.

The paths selected by the route generator are limited to those lying within a rectangular window enclosing the source and destination. This rectangle is not the smallest which can enclose the two locations but is slightly larger (10 per cent) to allow for routes which may deviate from the more direct ones in order to use roads of higher quality. Along each path different transport modes can be allowed for, and mode changes can occur along route.

For each route/mode combination a risk-cost analysis is performed based on the specified substance properties, the information in the geographical data base, and transportation freight rates. The risk analysis covers possible losses in the form of property damage as well as injuries and fatalities. An example simulation of the transport of 120 tonnes of chlorine from Barcelona to Seville is shown in Fig. 4.

The result of this process is a set of transporta-

INTERNET
ZENVAE CH € IRIMS Demo Prototype: Transportation Risk/Cost Analysis

<table><tr><td>Cost</td><td>19586</td><td>ECU</td></tr><tr><td>Fatalities</td><td>0.061</td><td> $10^{-6}$ </td></tr><tr><td>Injuries</td><td>0.414</td><td> $10^{-6}$ </td></tr><tr><td>Damages</td><td>236.919</td><td> $10^{-2}$ </td></tr></table>

<table><tr><td>CURRLNT MENU OPTIONS:</td></tr><tr><td>call evaluation module</td></tr><tr><td>call path generator</td></tr><tr><td>select destination</td></tr><tr><td>select source location</td></tr><tr><td>select substance/class</td></tr><tr><td>EXPLAIN MENU OPTIONS</td></tr><tr><td>QUIT AND RETURN TO MAIN</td></tr></table>

![](/api/attachments/5BTP3MYW/fulltext/images/c8cab35979f5324461ea15a75cb8ed851be9cfb763225c4884f81f69f5eb0d15.jpg)  
to select a menu item, position the mouse pointer, and press the left mouse button ...

Fig. 4. The European Road Network used in the Transportation Risk/Cost Analysis module.

tion routes and modes, together with their calculated criteria values. These alternatives can then be evaluated using the multicriteria optimisation module; firstly to find the nondominated set, and then the optimum solution. All the previously described facilities of the multi-criteria evaluation module (e.g. constraint setting and definition of the reference point) can be used to allow human judgement to enter in the selection of the final best solution.

## 6. Conclusions

The IRIMS system represents an attempt to integrate a wide range of data bases, simulation models and decision aids into a single user-friendly tool for risk managers and policy makers.

The present version of the system is a demonstration prototype designed to illustrate the power and potential of modern information processing technology in this field. The simulation models currently implemented have been chosen primarily to demonstrate the benefits of this approach, and may need to be refined or replaced for careful studies of particular phenomena. The open, modular architecture of the system will permit the addition of new modules as they become available, and the tailoring of the system for application to particular case studies.

Future developments of the system will include the addition of more information to the data bases, fuller access to the data bases by the simulation models, and a greater degree of freedom for the user in setting up problem simulations.

At the same time the system is being adapted to make it applicable to a particular case study – namely the risks associated with the production, transportation and use of chlorine in Holland. This study is being carried out in collaboration with the Dutch Ministry of Housing, Physical Planning and the Environment. This will necessitate a much greater level of detail in the regional and geographical data bases for Holland and the incorporation of a zoom feature to allow this greater detail to be displayed.

Undoubtedly the case study will provide many ideas for the future development of the system. In addition, it is being demonstrated to managers and policy makers working in the field of hazardous substance risks, both to get suggestions for improvements and to explore possibilities for other collaborations with European governments or industries.

## References

IRIMS, The ISPRA Risk Management Support System, A Computer Based Prototype. 1986, EUR Report No. 10862 EN, Commission Of The European Communities, JRC, Ispra.

Burns, L.A., Cline, D.M., and Lassiter, R.R. (1981) Exposure Analysis Modeling Systems (EXAMS): User Manual and Systems Documentation. USEPA Environmental Research Laboratory, Athens, GA. 460p.

Diersch, H.-J. (1980) Finite-Element-Program-system FEFLOW. Program description, Institut für Mechanik der AdW der DDR, Berlin.

Diersch, H.-J. and Kaden, S. (1984) Contaminant Plume Migration in an Aquifer: Finite Element Modeling for the Analysis of Remediation Strategies: A Case Study. CP-84-11. International Institute for Applied Systems Analysis, A-2361 Laxenburg, Austria. 88p.

Eliassen, A. (1978) The OECD study of Long Range Transport of Air Pollutants: Long Range Transport Modelling. Atmos. Environ., 12, 479.

Fedra, K. (1985) Advanced Decision-Oriented Software for the Management of Hazardous Substances: A Prototype Demonstration System - Final Report (Dec 85). Study Contract No. 2748-85-07 ED ISP A. International Institute for Applied Systems Analysis, A-2361 Laxenburg, Austria.

Grauer, M. and Kaden, S. (1984) A Non-linear Dynamic Interactive Decision Analysis and Support System (DI-DASS/N). Users Guide. WP-84-23. International Institute for Applied Systems Analysis, A-2361 Laxenburg, Austria. 55p.

Hetrick, D.M. and McDowell-Boyer, L.M. (1978) TOXSCREEN: A multimedia screening level model for assessing the potential fate of toxic chemicals released to environmental media. In Proceedings, 1983 Summer Computer Simulation Conf., Simulation Councils, Inc., La Jolla, CA;, pp. 464–469.

Otway, Harry and Peltu, M. (1985) Regulating Industrial Risks: Science, Hazards and Public Protection, Butterworths, London and Boston.

Smith, J.H., Mabey, W.R., Bohonos, N., Holt, B.R., Lee, S.S., Chow, T.W., Bomberger, D.C. and Mill, T. (1977) Environmental Pathways of Selected Chemicals in Freshwater Systems. EPA 600/7-77-113, U.S. Environmental Protection Agency.
