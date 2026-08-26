---
otero_id: 13858
otero_key: "8GKADY2G"
title: "A decision support tool for allocating temporary-disaster-response facilities"
authors: "Fatih Cavdur; Asli Sebatli"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113145"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support tool for allocating temporary-disaster-response facilities

Fatih Cavdur<sup>⁎</sup>, Asli Sebatli

![](/api/attachments/8GKADY2G/fulltext/images/21e058568e20faeb13ec13e5c182a838cec640328c38059d76787b3ed99757d5.jpg)

Bursa Uludag University, Department of Industrial Engineering, Nilufer 16059, Bursa, Turkey

## A R T I C L E I N F O

Keywords: Humanitarian logistics Facility allocation Relief supplies distribution Decision support systems Mathematical programming Stochastic optimization

## A B S T R A C T

Managing disaster response operations is a challenging task requiring the consideration of many stakeholders under time pressure, risk and uncertainty. Utilization of information technology for decision support might produce great benefits for decision makers to overcome such challenges. This study presents a decision support tool for allocating temporary-disaster-response facilities for relief supplies distribution under demand uncertainty, as one of the many challenging problems in disaster relief operations. The decision support tool developed in this study consists of three main components; database, decision engine and user interface. We also include an example real-life case for illustration and present the results produced by the decision support tool. It is noted that the decision support tool allows decision makers to allocate temporary-disaster-response facilities in many diferent after-disaster situations by taking into account the possible uncertainties to occur after a disaster by utilizing a two-stage-stochastic programming framework. Although it is illustrated with a specific example case in this paper, the flexibility of the decision support tool allows users to consider other cases with as many scenarios as desired. We think that it might be a useful tool to help decision makers in allocating temporary disaster-response facilities for relief supplies distribution.

## 1. Introduction

Catastrophic consequences of disasters are observed all around the world in recent years. Among others, the earthquake in Haiti in 2010 (Haiti Earthquake) and the earthquake and tsunami in Japan in 2011 (Tohoku Earthquake and Tsunami) are just some examples of recent years' catastrophic events causing extreme causalities in their afected areas. It is more unfortunate that the poor management of disaster operations increases these casualties even more. We note, for instance, the criticisms about the poor management of disaster operations in case of Hurricane Katrina in the US in 2005 [1]. On the other hand, managing disaster response operations, is a challenging task requiring to take into consideration of many stakeholders under time pressure, risk and uncertainty. Developing decision support systems to help decision makers might thus produce great benefits in reducing the unwanted efects of disasters.

Allocation of disaster response facilities for relief supplies distribution is one of the challenging problems in DOM, in particular, in Disaster Relief Operations (DRO), which attracts the attention of many researchers as to be detailed in the next section. Although some common problem characteristics exist, some variations can be defined depending on the problem specifications. Providing relief supplies to disaster victims temporarily or for a short-time period after a disaster is one of such problem variations attracting much attention recently. As such facilities are aimed at providing relief supplies to disaster victims temporarily, the corresponding problem can thus be defined as the Temporary-Disaster-Response (TDR) facility allocation problem [2]. Due to the chaotic conditions after a disaster, utilization of such facil ities (i.e., TDR facilities) might make great contributions in performing the relief operations (i.e., relief supplies distribution) to minimize the unwanted efects of the disaster. However, as detailed in the next section, like many other problems in DOM, it is a challenging problem for decision makers who might gain significant benefits from a sophisticated decision support system to improve their decision making process and contribute to eficient management of DOM operations in general.

One of the important characteristic of the problem which needs to be implied is that such facilities are usually managed by local administrations rather than some central-governmental organizations. This approach is motivated by the fact that to improve the eficiency of the relief eforts such a decentralized management scheme might be more desirable in many cases instead of planning the activities centrally. In other words, as it is not possible for central-governmental organizations to tackle such local-level problems, it might be more preferable for central-governmental organizations to leave the management of such local facilities to local administrations and focus on the general management activities of central operations instead. As a result, we note that allocating temporary-disaster-response facilities for relief supplies distribution is a problem that needs to be handled by each local administration independently. In other words, although central relief operations (i.e., arrivals of central organizations to the afected area etc.) must be taken into consideration by local administrations while planning their local-level activities, each local administration might need to manage its own local resources (i.e., temporary-disaster-response facilities) as eficiently as possible to improve the quality of the corresponding relief eforts. By utilizing such a decision support tool, local administrations can manage their local resources more eficiently by performing what-if analyses in pre-disaster phase considering possible uncertainties to occur after a disaster especially if the decision support tool provides a stochastic optimization-based framework just as the one presented in this study.

Motivated by the idea discussed in the previous paragraph, in this study, we introduce a decision support tool aimed at helping decision makers (i.e., the personnel of local administrations responsible for managing such activities) in allocating TDR facilities for relief supplies distribution. The organization of the study is as follows. In the next section, we summarize the related literature mainly focusing on the decision support systems developed in humanitarian logistics. It is followed by the details of the decision support tool developed in this study with three subsections explaining the corresponding components of the system. Following section summarizes how these components are integrated together as a decision support tool. We then illustrate the implementation of the tool with a real-life problem in the following section and finalize the paper by presenting the concluding remarks in the last section.

## 2. Literature review

The process of planning, managing and controlling the flow of some type of disaster relief resources to afected people is defined as humanitarian logistics [3–6]. It is noted that there exist some diferent (i.e., humanitarian) considerations in humanitarian logistics which are not included in a typical general or commercial logistics system. For instance, the metrics of primary concern in such a supply chain (sometimes referred to as a humanitarian or relief chain), are diferent from those in a commercial supply chain. In a commercial supply chain, some monetary driven metrics are considered to measure the performance whereas satisfaction of humanitarian needs is more important in a humanitarian chain. The interested reader can refer to the study of Beamon and Balcik [7] for a comprehensive discussion on the performance measures of humanitarian chains.

One of the important problems in humanitarian logistics considered in various studies is allocating some kind of disaster-response facilities to provide relief supplies to disaster victims. Some examples are the studies of Balcik and Beamon [8], Cavdur et al. [2], Kilci et al. [9], Mete and Zabinsky [10], Murali et al. [11], Noyan et al. [12] and Rawls and Turnquist [13,14]. On the other hand, allocating such disaster-response facilities also requires the consideration of the stochastic nature of the problem as it involves diferent DOM phases such as preparedness and response. As a result of this involvement of diferent DOM phases, several uncertainties might need to be considered, such as the ones about demand (i.e., demand location, type, amount etc.) and transportation (i.e., road status, capacity) etc. Among other dificulties, these uncertainties make it even more dificult to solve the problem as it requires taking into consideration of several stochastic parameters.

Various approaches are proposed to deal with these stochastic problem parameters. Among others, stochastic programming-based studies are noteworthy. In particular, two-stage stochastic programs are usually considered to solve similar disaster-response facility allocation problems. Although the types of facilities might be diferent, the structure of the problem allows the utilization of two-stage stochastic programs. In a typical setting, some pre-disaster activity decisions (i.e., locating facilities) are made in the first stage whereas second-stage decisions are usually about some other post-disaster activities (i.e., relief supplies distribution).

Although this setting nicely represents the problem structure, the quality of solutions is directly related to the scenarios of the corresponding stochastic program (i.e., how comprehensively they represent the stochastic problem parameters). In other words, even if the model is formulated to capture all problem characteristics, the quality of solutions might still be poor due to the limited number of scenarios. On the other hand, a comprehensive scenario construction process producing meaningful scenarios might require professional knowledge in the area (DOM) in addition to the theoretical background in stochastic programming. As a result, a team of professionals and researchers might be required to implement such a stochastic programming framework which might be inconvenient in practice unless a flexible tool is provided for decision makers. Motivated by this fact, we develop such a tool in this study by aiming at combining both of these aspects (professional knowledge and theoretical background) to help in the decision making process. In particular, the tool allows decision-makers without a theoretical background in stochastic programming to define their own meaningful scenarios and run a stochastic programming model under various real-life conditions represented by the corresponding scenarios.

We also note the crucial importance of developing decision support systems for disaster operations management. It is usually required to make eficient decisions as soon as possible to minimize the unwanted efects a disaster. It is however a challenging task also for decisionmakers due to the complexity of situation caused by the disaster. Developing sophisticated decision support systems to help decision makers might significantly increase the eficiency of the decisionmaking process and produce substantial benefits in performing the corresponding disaster operations. As stated by Thompson et al. [15], it is very important to utilize decision support systems to eliminate such ineficiencies in DOM.

As stated by Ortuno et al. [16], although an increasing trend is noted in developing decision support systems for humanitarian logistics operations, most of these are focused on inventory control rather than transportation and distribution operations. Since inventory control and fleet management operations are related to preparedness and response phases, a focus on these phases for the corresponding decision support systems is also noted though some studies considering mitigation and recovery also exist. Ortuno et al. [16] also states that these systems usually focus on information management rather than decision mechanisms and implies the importance of developing systems supported by the relevant decision mechanisms (models, algorithms etc.). On the other hand, as stated by Fiedrich et al. [17], some existing decision support systems, do not guarantee optimal solutions due to some issues such as problem complexity, information amount and time pressure. In some cases, both engineering and non-engineering issues should be addressed in an integrated manner as in the study of Ahmad and Simonovic [18] on management of floods.

Such decision support systems including more sophisticated decision mechanisms are developed for various purposes. Rolland et al. [1], for instance, propose a methodology for assigning and scheduling skilled-personnel. In another study, Alvear et al. [19] presents a decision support system for emergency management in road tunnels to provide decision recommendations to deal with the emergency in real time. Haynes et al. [20] proposes a service and agent-based architecture for anti-terrorism planning and resource allocation. In another study, Lorca et al. [21] present a decision support tool for post-disaster debris operations. In the study of Hobeika et al. [22], a decision support system is presented for developing evacuation plans around nuclear power stations. In another study about evacuation planning, Tufekci [23] presents a personal computer-based emergency hurricane evacuation planning module, Regional Evacuation Modeling System (REMS) developed at the University of Florida. In another evacuation planning-related study, Hadiguna et al. [24] develop a decision support system to facilitate immediate evacuation after a disaster.

Geographic Information Systems (GIS)-based studies are also note worthy. Integration with GIS might produce important benefits for decision-makers by allowing them modeling real-time scenarios using spatial analysis as in previous studies. Chang et al. [25] use two stochastic programming models for planning disaster operations for flood where the authors utilize a GIS to estimate demand (location and amount). The study of De Silva and Eglese [26] integrates a microtrafic simulator and GIS for planning the evacuation operations after a nuclear disaster which includes four components as object-oriented evacuation simulation model, GIS component, an integration link interface which consists of mechanisms developed for dynamic communication and data-information exchange between the GIS, simulator and user-interface. In a more recent study, Sahebjamnia et al. [27] proposes a hybrid decision support system for configuring humanitarian supply chains.

We finalize this section by noting some studies considering relief supplies distribution. In their study, Ozdamar et al. [28] develop a decision support system integrating multi-commodity network flow and vehicle routing models. In another study, Kondaveti and Ganz [29] propose a decision support system for resource allocation and distribution operations by first clustering disaster victims using their geographic coordinates and then planning resource allocation and distribution operations. Rekik et al. [30] propose a decision support system to combine network design, distribution planning and multicriteria decision-making modules presented in their study. In another study, Fikar et al. [31] presents a simulation and optimization-based decision support system to facilitate disaster relief coordination between diferent organizations. Motivated by these examples, in this study, we propose a decision support system for planning relief supplies distribution operations using temporary-disaster-response facilities as detailed in the following section.

## 3. System components

The decision support tool developed in this study composed of three main components; database, decision engine and user interface; the details of each are explained in the following sub-sections, respectively. We use Microsoft Visual Studio for the core system implementation (i.e., for the integration of the system components) and the user in terface design, whereas other software are used for the other components; Microsoft SQL Server for database, and Maximal Software Mathematical Programming Language and Gurobi Optimizer for decision engine.

## 3.1. Database

The database component of the system is designed using Microsoft SQL Server. There are 19 tables definitions of which are given in Table 1. We present the entity-relationship diagram in Appendix A. As seen in Table 1, it is noted that we can classify the tables as the ones about disaster characteristics, network structure, models and solutions.

There are four tables about disaster characteristics which contain information about commodities (i.e., relief supplies), disasters, disaster types and facilities (i.e., temporary-disaster-response facilities). There are three tables about network structure. These tables contain in formation about the nodes (i.e., neighborhoods, districts, cities etc.), node risks (if available, risk levels of the nodes in the network for dif ferent types of disasters) and paths (possible paths between node-pairs).

Among the other tables about network structure, additional ex planations about the “definition" field of the “nodes" table might be useful to represent the approach adopted to define diferent types of nodes (i.e., neighborhoods, districts, cities etc.) in the network. It is defined as a 12-digit field each triplet of which represents a hierarchy in the network. In particular, the 12 digit can be characterized as “RRR CCC-DDD-NNN” where R, C, D and N represent the digits for Regions (or might be considered as states in some countries), Cities in the given

State, Districts in the given City and Neighborhoods in the given District, respectively. For instance, if we want to refer the neighborhoods of the Yildirim district of Bursa city of Marmara Region in Turkey, as in the illustrative example presented in the following pages, we could use the definition range starting from 005-016-003-001 to 005-016-003-064 representing the first and last alphabetically-ordered neighborhoods (Akcaglayan Neighborhood and 75 Yil Neighborhood) of the district, respectively (see the last three digits). Note that although it represents an example representation from Turkey, it could easily be adapted to be used in other countries as well. For the countries, like the US, for instance, the digits representing regions could be adapted to represent states. Using such a representation schema presents a logical way of defining all neighborhoods in a country.

The remaining tables include information about the decision engine, such as the stochastic programming model given in Appendix B and the details of the solutions (facility allocations) produced by running the model (i.e., such as the objectives and variables of the model together with their corresponding relationships to the stochastic programs and their scenarios).Appendix B Also note that the tables about the model and solutions must have the necessary relationships among themselves as seen in the entity-relationship diagram (see Appendix A) in order to ensure that the solutions are distinguished appropriately and the system is fully integrated.

We also construct several Structured Query Language (SQL) storedprocedures as listed in Table 2 to ensure system integration (i.e., creating model inputs and outputs dynamically through the user interface developed etc.). Since the corresponding procedures are also related to the decision engine and user interface components of the system, they are presented in more detail in the next section (4. System Integration) of the paper after the details of the corresponding com ponents are also explained.

Note that, as seen in Table 2, these procedures can be categorized as the ones for generating model inputs and outputs. We also note that, in order to maintain the current length of the study and to allow the reader to focus on the procedures designed to perform the core decision support operations, a few other procedures designed for some straightforward tasks, such as deleting solution records from the database and ranking solutions according to a selected performance measures, are omitted.

## 3.2. Decision engine

We adapt the decision engine from a recent study of Cavdur et al. [2] where the authors propose a two-stage stochastic programming model for the TDR facility allocation problem. The authors consider the uncertainty in relief supplies demands in the stochastic program they proposed and define five scenarios to model diferent after-disaster situations causing the uncertainty in relief supplies demands. We present the corresponding stochastic programming model in Appendix B. A supplementary file is also provided for more details about the model.

The stochastic program proposed in the study of Cavdur et al. [2] is aimed at performing the allocations of TDR facilities designated for providing short-term (hence the term temporary) relief-supplies to disaster victims under demand uncertainty by minimizing the total number of facilities, travel distance and unsatisfied demand where the facility allocation and service (distribution) decisions are performed in the first and second stages, respectively. The authors use five diferent scenarios, each representing a diferent after-disaster situation (i.e., trafic conditions, time etc.), with its respective probability of occurrence, to model the demand uncertainty for relief supplies. Since TDR facilities have some specific purpose in the sense that they are supposed to serve disaster victims in the short-term (i.e., temporarily) until the arrival of central resources, their allocation requires the consideration of some particular constraints, such as the supply-ratios, safety condi tions and service levels to both prevent chaotic situations and maximize the eficiency of distribution operations as detailed in the study of

Table 1  
Database table definitions.

<table><tr><td>Table name</td><td>Table definition</td></tr><tr><td>Commodities</td><td>Commodities. Related to “Disasters” and “Facilities” tables.</td></tr><tr><td>Disasters</td><td>Disasters. Related to “DisasterTypes”, “Commodities” and “Facilities” tables.</td></tr><tr><td>DisasterTypes</td><td>Disaster types. Related to “Disasters” and “NodeRisks” tables.</td></tr><tr><td>Facilities</td><td>Facilities. Related to “Commodities” and “Disasters” tables.</td></tr><tr><td>Nodes</td><td>Nodes. Related to “NodeRisks” and “Paths” tables.</td></tr><tr><td>NodeRisks</td><td>Node risks. Related to “DisasterTypes” and “Nodes” tables.</td></tr><tr><td>Paths</td><td>Paths. Related to “Nodes” table.</td></tr><tr><td>ModelConfigurations</td><td>Model configurations. Related to corresponding model and solution tables.</td></tr><tr><td>ModelConfParams</td><td>Model configuration parameters. Related to corresponding model tables.</td></tr><tr><td>ModelParameters</td><td>Model parameters. Related to corresponding model tables.</td></tr><tr><td>ModelTypes</td><td>Model types. Related to corresponding model and solution tables.</td></tr><tr><td>SPs</td><td>Stochastic programs. Related to &quot;Scenarios&quot; and corresponding solution tables.</td></tr><tr><td>Scenarios</td><td>Scenarios. Related to &quot;SPs&quot; and corresponding solution tables.</td></tr><tr><td>Solutions</td><td>Solutions. Related to corresponding model and solution tables.</td></tr><tr><td>SolutionsObjectives</td><td>Objectives. Related to “Solutions” table.</td></tr><tr><td>SolutionsUs</td><td>Model variables (U). Related to “Solutions” table.</td></tr><tr><td>SolutionsXs</td><td>Model variables (X). Related to “Solutions” table.</td></tr><tr><td>SolutionsYs</td><td>Model variables (Y). Related to “Solutions” table.</td></tr><tr><td>SolutionsZs</td><td>Model variables (Z). Related to “Solutions” table.</td></tr></table>

Cavdur et al. [2].

Although the stochastic program proposed in the study of Cavdur et al. [2] ofers a solution approach for the TDR facility allocation problem, it has some limitations in terms of representing the stochastic nature of the problem. In other words, the authors represent the uncertain problem characteristics (i.e., relief supplies demands) using some pre-defined scenarios with some other default problem parameters which reduces the flexibility of the proposed approach to be used in real-life. On the other hand, in a decision support tool as presented in this study, the users are expected to have more flexibility so that they are allowed to define the corresponding scenarios together with their respective probabilities of occurrence as well as the other problem parameters as detailed in the following subsection (User Interface) of the manuscript.

We present the corresponding stochastic program in Appendix B. A supplementary file is also provided for more details. We refer the interested reader to the study of Cavdur et al. [2] for a more detailed discussion on the stochastic programming model.

## 3.3. User interface

A graphical user interface is designed for users to interact with the system. Microsoft Visual Studio is used for designing the user interface. A screenshot of the user interface is presented in Fig. 1. As noted in the figure, the controls in the user interface are basically divided into two categories and placed on the left-hand side and right-hand side of the interface for ease-of-use. The controls on the left-hand-side are designed to be used for determining problem parameters and performing allocations whereas the ones on the right-hand side are for reporting purposes (i.e., summarizing solutions or facility allocations).

There are five diferent parameters on the left-hand side of the user interface which are again divided into three sub-categories as the parameters about the (i) afected area, (ii) disaster and (iii) model configurations. In the first sub-category (afected area), three more parameters are also determined by the user as regions, cities and districts in order to define the afected area properly in the highest-level of resolution available (i.e., neighborhood level). Note that we represent the network structure in a particular geographical classification hierarchy suitable for some countries, such as Turkey; however, our design can easily be adapted to a diferent representation for a diferent country, such as the United States, for instance, where we can use a geographical hierarchy starting from the states instead of regions. We also note that using the procedures developed, the contents of the controls are populated dynamically by querying the database, i.e., when the user selects a region, its cities are listed and when the user selects a city, its districts are listed dynamically in the corresponding list boxes.

There is only one disaster-related parameter in the midsection to define the afected population rate. Several diferent afected population rates (from 75% to 95%) are considered currently. On the other hand, these are just used to represent some typical conditions and can easily be increased to define more comprehensive settings just by adding the corresponding tuples in the database.

We also have only one parameter in the final set of parameters called model configurations which represents some combinations of some other problem parameters (the parameters which are not included in the first two sets, and thus, are not related to the afected area or the disaster). such as the available budget (number of facilities) and service levels. Similar to the parameters of the other sets, these are also used to represent some typical conditions and the user can define as many model configurations as desired just by adding the corresponding tuples in the database. Also note that, motivated by the study of Cavdur et al. [2], these model configurations are named accordingly so that they represent the particular conditions of the corresponding configuration, such as Standard, Lower Budget etc. More details on the model con figurations are presented in the following section.

Table 2  
SQL stored-procedures for dynamic model data I/O generation.

<table><tr><td>Procedure name</td><td>Procedure definition</td></tr><tr><td>InputFacilities</td><td>Generates model inputs (facilities).</td></tr><tr><td>InputCommodities</td><td>Generates model inputs (commodities).</td></tr><tr><td>InputRegions</td><td>Generates model inputs (network structure, regions).</td></tr><tr><td>InputCities</td><td>Generates model inputs (network structure, cities).</td></tr><tr><td>InputDistricts</td><td>Generates model inputs (network structure, districts).</td></tr><tr><td>InputNodes</td><td>Generates model inputs (network structure, neighborhoods).</td></tr><tr><td>InputCosts</td><td>Generates model inputs (costs).</td></tr><tr><td>InputDemands</td><td>Generates model inputs (demands).</td></tr><tr><td>InputConfigurationParameters</td><td>Generates model inputs (configuration parameters).</td></tr><tr><td>OutputSolutions</td><td>Generate model outputs (single-objective function value).</td></tr><tr><td>OutputSolutionObjectives</td><td>Generate model outputs (multiple-objective function values).</td></tr><tr><td>OutputSolutionsYs</td><td>Generate model outputs (service decisions-vector Y).</td></tr><tr><td>OutputSolutionsXZs</td><td>Generate model outputs (solution details-vectors X and Z).</td></tr></table>

![](/api/attachments/8GKADY2G/fulltext/images/8e0a6793b98061616a238bada39c216e414c270b3b17d0802339c04d87912dce.jpg)  
Fig. 1. User interface screenshot-initial status (without any performed-allocations).

Note that we design our tool in such a way that any combination of the aforementioned problem parameters defines a particular after-disaster situation, or mathematically a stochastic program setting, for the decision engine. After the user defines all problem parameters, a scenario description can be automatically generated to be used as a re ference for the user for reporting purposes. Also note that a particular setting description includes all information required to represent the corresponding situation for the convenience of the user. A description of “Stochastic Program 1: Marmara-Bursa-Yildirim-75%-Standard". for instance, simply represents a stochastic program setting for the Yildirim (district of) Bursa (city of) Marmara (region) of Turkey as the afected area where 75% of the total population is afected considering a standard model configuration. Although such an informative scenario description can be used by choosing the automatic scenario generation option, it is also possible to define one's own scenario as illustrated in the following pages (in Section 5).

After the aforementioned problem parameters are determined, the user can define the scenarios with their respective probabilities of occurrence for the corresponding stochastic programming setting by clicking on the “Define Model Scenarios & Probabilities” button as shown in Appendix C. Each scenario of the stochastic program is represented with a unique scenario identification number in the database. The flexibility of the tool allows the user to generate as many settings as necessary to represent various after-disaster situations. We further note that it is also possible to define a new model configuration by clicking on the “Define New Model Configuration” button where the user can set all problem parameters although one should take caution while setting the corresponding parameters since the resulting configuration might be an unreasonable one in practice (i.e., setting an extremely low or high budget etc.) otherwise. Defining a new model configuration using the tool is also shown in Appendix C. After all settings are entered, the user can then perform the allocations by clicking on the

corresponding button.

Designed for reporting purposes, the components on the right-hand side of the user interface are somewhat self-explanatory. As noted in Fig. 1, we can categorize the presented results reported on the righthand-side into four sub-categories including summarized information about (i) solutions (i.e., stochastic programming settings and their scenarios with their respective probabilities of occurrence) ranked for the selected performance measure, (ii) performance measures themselves both for stochastic programs (i.e., first and second stage objectives, Value of Stochastic Solution (VSS) and Expected Value of Perfect Information (EVPI) etc.) and their scenarios (i.e., overall objective, weighted distance, number of facilities, unsatisfied demand), (iii) service decisions and (iv) allocation details. After selecting a particular scenario description, the results for the corresponding scenario are presented to the user as if the scenario is occurred deterministically. In Fig. 1, we note that, since there are no allocations stored in the database initially (before performing any allocations), no results are displayed in the user interface either, representing the initial status of the system. Another screenshot of the user interface is presented in the following pages (again, in Section 5) after performing some allocations for illustration purposes where the controls on the right-hand-side of user interface are then populated with the corresponding information (i.e., performance measures, service decisions and allocation details) by selecting a particular scenario description.

We finally note the controls located at the top of the results section on the right-hand-side providing an important decision support capability for the user. After generating several allocations (i.e., solutions), it might be dificult for the user to analyze these allocations and make decisions based on them. A mechanism for ranking the corresponding allocations with respect to some performance measure might be very useful for improving the decision support capability of the tool. We note such a capability is provided with the controls at the top of the results section where the user can rank solutions with respect to some performance measure by selecting the corresponding performance measure from the drop-down lists.

Note that ranking solutions within a stochastic programming framework might require additional consideration for decision makers due to the existence of the decision variables in diferent stages of the program. In our case, for instance, we note that the allocations are performed in the first stage considering the second stage service decisions for which the most straightforward way is simply ranking the solutions with respect to the overall objective function value of the stochastic program. On the other hand, the users of a decision support tool might want to have more options such as ranking solutions with respect to the first stage objective value, second stage objective value etc. which are available for the user as alternative options in the corresponding combo box.

Our tool provides additional ranking features for decision makers even beyond that. Using the second combo box-button pair, we can also rank the scenarios within the corresponding stochastic programs they belong. In other words, using the scenario ranking mechanism, decision makers can rank the scenarios with respect to some performance measures by preserving the ranking of the stochastic programs among themselves so that all scenarios are ranked within the stochastic program they belong. Decision makers can then analyze the performance measures for a particular stochastic program scenario as if it occurs deterministically. We again have diferent options to rank solutions with respect to some performance measures as before. By using these mechanisms, decision makers not only have the option to rank the so lutions of the stochastic programs (i.e., allocations under uncertainty), but they can also see the best-worst scenarios within each stochastic program with respect to some selected performance measure.

## 4. System integration

After the development process of the aforementioned main components (database, decision engine and user interface) is completed; they are integrated under the decision support framework developed in the study. As stated earlier, Microsoft Visual Studio is used for the integration of the system components. We use Microsoft Visual Studio also for designing the user interface. Additionally, the database component is designed using Microsoft SQL Server whereas Maximal Software Mathematical Programming Language and Gurobi Optimizer are used for developing the decision engine.

The SQL procedures presented earlier while explaining the database component (in Table 2 of Section 3.1) are triggered by the corresponding controls of the user interface. These procedures are basically used to perform the operations in the database component for generating model inputs and outputs dynamically for the decision engine component of the system. Figs. 2 and 3 briefly describe how these procedures are used in the integrated structure of the system for generating the corresponding inputs and outputs, respectively. Note that, in Figs. 2 and 3, the prefixes “T”, “SP” and “UI” used to represent the tables, SQL stored-procedures and user interface, respectively, for the convenience of the reader.

Fig. 2 summarizes the process of generating model inputs. As noted from the figure, model inputs are categorized with respect to the corresponding type of model components represented by them (i.e., facilities, commodities etc.). It is noted that all the other inputs except the last one are all about generating first-hand model inputs (facilities, commodities etc.) whereas the last one represents a higher-level of input as such it particularly defines the model configurations explained in previous pages during the discussions about the user interface of the system.

We can consider the procedure for demand to explain the input generation process since all the others are somehow similar to the one about demand. We note that the input generation procedure for demand (SP\_InputDemands) uses the results of two other stored-proce dures to generate commodities and nodes (SP\_InputCommodities and SP\_InputNodes) as well as the tables about disasters (T\_Disasters) and scenarios (T Scenarios).

We further note that the stored-procedure SP\_InputCommodities also gets inputs from another stored-procedure (SP\_Input\_Facilities) and the table about commodities (T\_Commodities). Similarly, SP\_InputNodes uses the inputs about the afected area entered from the user interface (UI\_Region, UI\_City, UI\_District) and the nodes from the T\_Nodes table.

At this point, we also note that the relationships between the corresponding user interface controls (lists boxes for selecting the region, city and district of the afected area). In other words, when the user makes the region selection, a simple SQL procedure retrieves the cities in the region. Similarly, when a city selection is made, all districts in the city are presented to the user dynamically so that the user can define an appropriate scenario. In summary, by using a particular commoditiesafected area-disaster information combination as its inputs the storedprocedure SP\_InputDemands generates the corresponding demands.

Similarly, Fig. 3 summarizes the process for generating model outputs using the corresponding stored-procedures and system components. As it is done for the inputs, we note a categorization for model outputs, with respect to the corresponding type of model components represented by these outputs. There are four types of outputs in terms this categorization which contains information about general solution, solution objectives, service and inventory. As their names suggest, these represent some kind of solution information especially formatted for the user of the system; the first two stored-procedures are about the solutions in a more theoretical sense whereas the last two are about the real-life or practical implications of these solutions. It is noted that the stored-procedures for generating model outputs also use some inputs from the corresponding user-interface controls and tables.

It is noted that the first and second stored-procedures, namely SP\_OutputSolutions and SP\_SolutionObjectives, retrieve the general solution information and objective function values, respectively, of a particular solution to the user interface. On the other hand the last two stored-procedures, are related to the corresponding decision variables; $x _ { i j k } ( \xi )$ (represents the amount of commodity k to be supplied from neighborhood i to neighborhood j in scenario ξ), y (ξ) (represents the service decisions in scenario ξ, equals 1 if neighborhood i serves neighborhood j and 0 otherwise) and z<sub>i</sub> (represents the number of facilities opened in neighborhood i) of the integer programming model for the decision engine. In other words, the stored-procedure SP\_OutputSolutionYs produces service decisions in terms of the geographical regions (neighborhood names rather than the index values) for a particular solution whereas SP\_OutputSolutionXZs presents the number of facilities in each neighborhood as well as the amount of commodities stored in these facilities again for the corresponding solution. All these outputs are presented under the solution details panel on the right-hand-side of the user interface for the purpose of reporting solution details to the user of the system. It should be noted from the solution tables that the scenario index of the second stage variables (i.e., ξ) is not particularly defined, however, the scenarios of a stochastic program are identified using appropriate integers (i.e., solution identification numbers) in the corresponding solution tables in the database.

We further note that the aforementioned discussions are about the core parts of the decision support tool and thus presented in more details, we have some final remarks about the other decision support capabilities of the tool before concluding this section. Although there are some other components (i.e., stored-procedures etc.) of the tool, they are not discussed in much detail due to our eforts to limit the number of pages of the manuscript.

Among these components the most important one in terms of its decision support capabilities is the solution ranking feature of the tool. As mentioned in the subsection where the user interface is discussed (i.e., 3.3. User interface), the user can rank stochastic program solutions (i.e., allocations) as well as the scenarios within the stochastic programs with respect to some performance measure using the controls on the interface; a capability provided for improving the decision support capability of the tool. Each of the stored-procedures developed for that purpose (SP\_Sort\_Solutions and SP\_Sort\_Scenarios) receive an input parameter to determine the sorting criterion (i.e., performance measure) of the solutions or scenarios based on the selection of the user and returns the sorted-list of solutions or scenarios with respect to the selected performance measure by implementing the corresponding queries on the solution tables. The user can also remove a particular allocation or all allocations by using the corresponding commands under the tasks menu. In particular, by removing some allocations, the user might eliminate some of the allocations from further consideration for decision makers by allowing them to focus on the remaining ones whereas removing all allocations option can be used to initiate the system by restoring it back to its initial status.

![](/api/attachments/8GKADY2G/fulltext/images/ea81df72d11f5e1813978d42f65a2fa557aa018d06cb10f05a0b1b5016c7087c.jpg)  
Fig. 2. Overall structure for generating model inputs.

Finally, we also provide two additional features again accessible under the tasks menu of the tool for exporting solution reports to a spreadsheet (i.e., a Microsoft Excel file) and printing them out. These are not also detailed here since they can be regarded as straightforward software development implementations; however, by the availability of these features, the user has the option to share the results (either in electronic or paper forms) with other decision makers who do not have access to the decision support tool which might yield a better decisionmaking experience.

## 5. Implementation: an illustrative example

In this section, we illustrate the implementation of the decision support tool using an example with diferent parameter settings where we define 50 diferent after-disaster settings for diferent combinations of afected population rates and model configurations. In particular, we consider an example afected area (Marmara-Bursa-Yildirim) with two diferent afected population rates as 75% and 95%, under diferent model configurations. We also define five diferent planning periods as the stochastic program scenarios varying between 8 h and 72 h. Currently, there are five diferent model configurations (i.e., standard, lower budget etc.) each represents a particular setting of some model parameters as presented in Table 3.

The first model configuration (MC1-Standard) is referred as the standard configuration and adapted from the study of Cavdur et al. [2]. Second model configuration (MC2-Lower Budget) limits the total number of facilities available as 100 (with a maximum number of 10 facilities per neighborhood) in order to represent the restriction on available budget. Two of the following configurations (MC3 and MC4) are defined to see the efects of changing safety and service levels. In particular, as seen in Table 3, MC3 represents the configuration where safety and service levels are at their lowest levels (Lower Safety-Service Levels) whereas in MC4 (Higher Safety-Service Levels) both parameters are greater than all of their realizations in other configurations. Final model configuration MC5 (Lower Demand Satisfaction) simply represents the worst case in terms of humanitarian metrics since the unit cost of unsatisfied demand is decreased.

In addition to five diferent model configurations, since there are also five diferent planning periods varying between 8 h to 72 h (3 days) representing the stochastic program scenarios, we totally have 25 different settings for a particular afected area and afected population rate. Finally, by considering two diferent afected population rates, the total number of settings is now 50 for a particular afected area. The results are summarized in Tables 4 and 5 for the first and second 25 settings defined for the two diferent afected population rates (75% and 95%), respectively.

![](/api/attachments/8GKADY2G/fulltext/images/2e93ea8144a9da55a8116613040fc52e4f0b19bcc563b58f3c47cde4d99045ad.jpg)  
Fig. 3. Overall structure for generating model outputs.

Table 3  
Model configuration definitions.

<table><tr><td>Configuration</td><td> $N_T$ </td><td> $n_i$ </td><td> $S_T$ </td><td>M</td><td>λ</td><td>α</td><td>β</td><td>γ</td></tr><tr><td>MC1-Standard</td><td>900</td><td>100</td><td>0.975</td><td>1,000,000</td><td>1000</td><td>10</td><td>10</td><td>15</td></tr><tr><td>MC2-Lower Budget</td><td>100</td><td>10</td><td>0.975</td><td>1,000,000</td><td>1000</td><td>10</td><td>10</td><td>15</td></tr><tr><td>MC3-Lower Safety-Service Level</td><td>900</td><td>100</td><td>0.950</td><td>1,000,000</td><td>1000</td><td>5</td><td>5</td><td>15</td></tr><tr><td>MC4-Higher Safety-Service Level</td><td>900</td><td>100</td><td>0.990</td><td>1,000,000</td><td>1000</td><td>20</td><td>20</td><td>15</td></tr><tr><td>MC5-Lower Demand Satisfaction</td><td>900</td><td>100</td><td>0.975</td><td>1,000,000</td><td>1000</td><td>10</td><td>10</td><td>1</td></tr></table>

Table 4 represents a summary of the performance measures for the optimal solutions of the first 25 scenarios (i.e., scenarios for an afected population rate of 75%) for the deterministic versions of the stochastic program scenarios. As expected, we note that the performance measures get worse for longer planning periods in general. Depending on the model configuration, however, the corresponding worsening is observed in terms of diferent performance measures.

For instance, if we compare the results for the first two model configurations (MC1 and MC2) for longer planning periods, it is noted that the first performance measure (weighted-distance) keeps increasing in the first model configuration whereas a sudden increase (from 54 to 1,439,097 between planning periods of 24 and 48 h) is observed for the third performance measure (unsatisfied demand) in the second model configuration. Note that it is an expected result since the second model configuration limits the total number of facilities available (lower budget), and thus, it is not possible to allocate more than 100 facilities which causes great amount of unsatisfied demand for longer planning periods as observed for the last two planning periods (48 h and 72 h) in the results. The next model configuration-pair (MC3 and MC4) represents the efects of changing safety and service levels. It is noted from the results that restrictions on the safety and service levels significantly afect the performance measures. In particular, lowering the safety level allows allocating facilities in more neighborhoods. As a result, this configuration produces better scores especially in terms of the first performance measure (weighted-distance) than the other model configuration (MC4) requiring a higher safety level which is achieved by allowing higher service levels also at the expense of a worse performance. In other words, lowering safety and service levels allows facility allocations in more neighborhoods, even if they are not safe, making it easier for disaster victims to reach these facilities whereas disaster victims walk or travel longer distances in the second case where it is allowed to allocate facilities only in very safe neigh borhoods which, on the other hand, can serve many others.

Table 4  
Optimal solutions-performance measures (PMs) for diferent model configurations (MCs) and planning periods (PPs) for an afected population rate of 75%.

<table><tr><td>Configuration</td><td>Scenario-1(8 hour PP)</td><td>Scenario-2(16 hour PP)</td><td>Scenario-3(24 hour PP)</td><td>Scenario-4(48 hour PP)</td><td>Scenario-5(72 hour PP)</td></tr><tr><td>MC1-PM1</td><td>1,554,672</td><td>3,107,557</td><td>4,661,563</td><td>9,322,530</td><td>13,984,987</td></tr><tr><td>MC1-PM2</td><td>29</td><td>54</td><td>75</td><td>148</td><td>217</td></tr><tr><td>MC1-PM3</td><td>47</td><td>51</td><td>55</td><td>56</td><td>54</td></tr><tr><td>MC2-PM1</td><td>1,554,673</td><td>3,169,942</td><td>5,148,141</td><td>4,227,351</td><td>2,216,516</td></tr><tr><td>MC2-PM2</td><td>29</td><td>52</td><td>73</td><td>100</td><td>100</td></tr><tr><td>MC2-PM3</td><td>47</td><td>53</td><td>54</td><td>1,439,097</td><td>3,886,609</td></tr><tr><td>MC3-PM1</td><td>585,224</td><td>1,169,064</td><td>1,754,939</td><td>3,506,653</td><td>5,258,919</td></tr><tr><td>MC3-PM2</td><td>40</td><td>61</td><td>80</td><td>153</td><td>224</td></tr><tr><td>MC3-PM3</td><td>47</td><td>51</td><td>49</td><td>55</td><td>51</td></tr><tr><td>MC4-PM1</td><td>2,735,426</td><td>5,470,881</td><td>8,205,382</td><td>16,410,294</td><td>24,615,667</td></tr><tr><td>MC4-PM2</td><td>25</td><td>48</td><td>72</td><td>143</td><td>213</td></tr><tr><td>MC4-PM3</td><td>48</td><td>59</td><td>55</td><td>93</td><td>56</td></tr><tr><td>MC5-PM1</td><td>59,639</td><td>119,589</td><td>196,290</td><td>359,058</td><td>521,760</td></tr><tr><td>MC5-PM2</td><td>14</td><td>22</td><td>30</td><td>55</td><td>80</td></tr><tr><td>MC5-PM3</td><td>541,777</td><td>1,084,130</td><td>1,608,161</td><td>3,250,325</td><td>4,890,386</td></tr></table>

Table 5  
Optimal solutions-performance measures (PMs) for diferent model configurations (MCs) and planning periods (PPs) for an afected population rate of 95%.

<table><tr><td>Configuration</td><td>Scenario-1(8 hour PP)</td><td>Scenario-2(16 hour PP)</td><td>Scenario-3(24 hour PP)</td><td>Scenario-4(48 hour PP)</td><td>Scenario-5(72 hour PP)</td></tr><tr><td>MC1-PM1</td><td>1,968,834</td><td>3,938,050</td><td>5,906,028</td><td>11,808,550</td><td>17,713,942</td></tr><tr><td>MC1-PM2</td><td>36</td><td>64</td><td>96</td><td>187</td><td>273</td></tr><tr><td>MC1-PM3</td><td>45</td><td>42</td><td>45</td><td>47</td><td>43</td></tr><tr><td>MC2-PM1</td><td>1,968,828</td><td>4,206,593</td><td>6,843,167</td><td>2,837,351</td><td>1,684,721</td></tr><tr><td>MC2-PM2</td><td>36</td><td>63</td><td>94</td><td>100</td><td>100</td></tr><tr><td>MC2-PM3</td><td>45</td><td>53</td><td>54</td><td>2,744,448</td><td>5,844,613</td></tr><tr><td>MC3-PM1</td><td>740,184</td><td>1,481,055</td><td>2,221,442</td><td>4,440,868</td><td>6,663,149</td></tr><tr><td>MC3-PM2</td><td>43</td><td>69</td><td>103</td><td>193</td><td>281</td></tr><tr><td>MC3-PM3</td><td>43</td><td>41</td><td>40</td><td>45</td><td>43</td></tr><tr><td>MC4-PM1</td><td>3,464,610</td><td>6,929,102</td><td>10,394,019</td><td>20,787,183</td><td>31,184,779</td></tr><tr><td>MC4-PM2</td><td>31</td><td>60</td><td>90</td><td>181</td><td>272</td></tr><tr><td>MC4-PM3</td><td>50</td><td>53</td><td>66</td><td>49</td><td>63</td></tr><tr><td>MC5-PM1</td><td>73,439</td><td>146,871</td><td>223,823</td><td>455,842</td><td>676,469</td></tr><tr><td>MC5-PM2</td><td>17</td><td>27</td><td>38</td><td>71</td><td>101</td></tr><tr><td>MC5-PM3</td><td>688,339</td><td>1,376,600</td><td>2,061,957</td><td>4,114,586</td><td>6,179,193</td></tr></table>

The final model configuration (lower demand satisfaction) represents the worst situation for humanitarian concerns since the unit cost of unsatisfied demand is the lowest in this case. As expected, it produces the worst results in terms of the third performance measure (unsatisfied demand), even worse than those of the second configura tion (i.e., lower budget) for longest planning period of 72 h.

The results for the next set of 25 scenarios are presented in Table 5 where we note the same model configuration-planning period combinations as in Table 4 for an afected population rate of 95%. Similar interpretations as for Table 4 are also applicable for Table 5. In parti cular, in addition to a standard configuration (MC1-Standard), we note the effects of limiting the total number of facilities (MC2-Lower Budget), changing the safety-service levels (MC3-Lower Safety-Service Levels and MC4-Higer Safety-Service Levels) and decreasing the cost of unsatisfied demand (MC5-Lower Demand Satisfaction) for diferent planning periods varying between 8 h to 72 h in the corresponding scenarios.

Comparing the results presented in the first set and second sets of 25 scenarios presented corresponding to the two diferent afected population rates in Tables 4 and 5, respectively; we obviously note that a higher rate of afected population yields worse scores for the measures of performance in general due to increasing relief supplies demands. We finally note that the results presented in this section are for illustration purposes only and as many scenarios as desired for any other afected area and population rate can be defined in a similar fashion.

A sample screenshot of the user interface after performing some allocations is shown in Fig. 4. We note that there two diferent stochastic programs each with five diferent scenarios for which the op timal allocations of temporary-disaster-response facilities are performed in the Yildirim district of Bursa city of Marmara region of Turkey as an example afected area.

It might be easier to understand and interpret the allocations for a particular solution by the corresponding solution definition, especially if either the decision maker uses the automatic scenario description generation option or oneself makes a meaningful description already. It is noted that there are two stochastic programs each with five diferent scenarios (i.e., for five diferent planning periods) defining the allocations for the same district and afected population rate (Yildirim district with an afected population rate of 75% for varying planning periods between 8 h and 72 h) for the standard model configuration. It is further noted that although the two stochastic programs are used to perform the allocations for the problems with the same parameters, scenario probabilities of the programs are diferent as noted in the figure.

The screenshot given in Fig. 4 presents the solution details corresponding to the first ranked scenario of the first ranked stochastic program defined by the user since it is the currently-selected scenario description (i.e., Marmara-Bursa-Yildirim-95%-Standard-8 h to occur with a probability of 10%). The other scenarios of the stochastic programs can also be interpreted similarly. The details can be analyzed by selecting the corresponding scenario description, such as the objectives (performance measures), service decisions and allocation details in the user interface.

We finally note from the screenshot that the solutions are sorted with respect to the overall objective function value (which is the default option also) for both stochastic programs and their scenarios, resulted with the corresponding ranking of the solutions and scenarios. Changing the performance measure for which the solutions and scenarios to-be-ranked (i.e., cost-distance, number of facilities or unsatisfied demand) might produce different results by utilizing different perspectives for the decision makers. Decision makers can also analyze solutions (i.e., allocations) by changing the other problem parameters as well as the scenario probabilities by utilizing the stochastic optimization framework. For instance, the same scenario settings can be run with diferent probabilities to see the risk efects. In other words, in our example case, a negative or left-skewed (positive or right-skewed) distribution represents a pessimistic (an optimistic) decision making perspective whereas a symmetric distribution models the behavior of risk-neutral decision maker.

## 6. Conclusions

We observe the catastrophic consequences of disasters all around the world in recent years. In addition, poor management of disaster operations increases unwanted efects of the disaster even more. On the other hand, it is a non-trivial task for decision makers since they might encounter many challenging problems in Disaster Operations Management (DOM) for which utilizing sophisticated decision support systems might significantly increase the eficiency in the management of the corresponding disaster operations. In this paper, a decision support tool is presented for allocating Temporary-Disaster-Response (TDR) facilities for relief supplies distribution under demand un certainty as one of the many challenging problems in DOM.

![](/api/attachments/8GKADY2G/fulltext/images/175c5ffe36d8a38f243256c4b00ff53c2306dd349795978f839f1de62baa207b.jpg)  
Fig. 4. User interface screenshot after performing some allocations.

The decision support tool developed in this study consists of three main components; (i) database, (ii) decision engine and (iii) user interface, details of which are explained in the corresponding sub-sections of the paper. We also include an example real-life case for illustration and present the results produced by the decision support tool. As illustrated with the given example real-life case, we note that the decision support tool developed in this study allows decision makers to allocate TDR facilities under many diferent after-disaster situations considering the possible uncertainties to occur after a disaster, such as diferent afected population rates, planning periods etc. by utilizing a two-stagestochastic programming framework. Although a specific example case is used in this paper for illustration, the flexibility of the decision support tool allows its users to consider other cases with as many other diferent settings as desired. We think that by defining more realistic cases with comprehensive scenarios, it might be a useful tool to help decision makers in the process of allocating TDR facilities for relief supplies distribution.

Although they are not discussed in detail in previous sections to limit the number of pages of the paper, the tool presented in the study provides additional decision support features. Among these, the most important one in terms of its decision support capabilities is the solution-scenario ranking features of the tool using which the allocation can be ranked with respect to some performance measure. The user can also remove a particular allocation or all allocations to eliminate some of the allocations from further consideration for decision makers by allowing them to focus on the remaining ones or to initiate the system by restoring it back to its initial status, respectively. Similarly, we also provide additional features for exporting solution reports to a spreadsheet and printing them out, using which, it is possible to share the results (either in electronic or paper forms) with other decision makers who do not have access to the decision support tool for a better decision-making experience.

In future studies, some extensions can be added to the decision support tool presented in this study. Potential improvements and future studies can be categorized with respect to the components of the system. In terms of the database component, although a generic and flexible database is currently designed, it can require some minor improvements to store additional parameters in future studies, such as user information for multi-user environments and additional model parameters for new models to integrate to the decision mechanism. A more user-friendly design for the user interface might also be considered. We also think that increasing the flexibility of the system via the user interface (to provide more flexible interactions with the database and decision mechanism) will be a very useful improvement. Finally. decision mechanism can also be extended to consider new models, algorithms and solution approaches.

## Acknowledgements

This research was supported by Tubitak, the Scientific and Technological Research Council of Turkey (115M020). We would like to thank Burcu Balcik for her valuable contributions.

Appendix A. Database-entity-relationship diagram  
![](/api/attachments/8GKADY2G/fulltext/images/8136458f7a679ea426a4d997a164b73d3967932fa685f05286c1d21e901bbc5a.jpg)

## Appendix B. Decision engine-stochastic programming model

This section presents the two-stage stochastic programming model adapted from the study of Cavdur et al. [2]. Indices:

i, j: neighborhood; $i , j = 1 , . . . , n _ { N }$

$k , p ,$ , q: commodity; $k , p , q = 1 , . . . , n _ { C }$

ξ: scenario

## Parameters:

$d _ { j k } ( \xi ) \colon$ demand of commodity k in neighborhood j for disaster scenario ξ

$c _ { i j } .$ cost $( \mathrm { i . e . , }$ distance) between neighborhoods i and j

$\nu _ { k } \mathrm { : }$ unit volume of commodity k

$w _ { k } \mathrm { : }$ unit weight of commodity k

$V { : }$ volume capacity of a TDR facility

$W { : }$ weight capacity of a TDR facilit

$r _ { p q } .$ supply-ratio between commodities p and q

n : maximum number of TDR facilities that can be allocated in neighborhood i

$N _ { T } { \mathrm { : } }$ total number of TDR facilities available

s : safety level of neighborhood i

$S _ { T } \mathrm { : }$ safety level threshold

α: maximum number of neighborhoods that a neighborhood can serve

$\beta \colon$ maximum number of neighborhoods that a neighborhood can be served by

λ: scaling factor

γ: penalty for unit unsatisfied demand

M: a big number

p(ξ): probability of scenario ξ

## Variables:

z : number of facilities opened in neighborhood i

$$
y _ {i j} (\xi) = \left\{ \begin{array}{l} 1, \\ 0, \end{array} \right.
$$

1, if neighborhood serves neighborhood for scenario i j $\xi$

otherwise

$x _ { i j k } ( \xi ) ;$ amount of commodity k to be supplied from neighborhood i to neighborhood j for scenario ξ

$u _ { j k } ( \xi ) \colon$ amount of unsatisfied demand of commodity k in neighborhood j for scenario ξ

Objective function:

$$
\min f = \lambda \left(\sum_ {i = 1} ^ {n _ {N}} z _ {i}\right) + \sum_ {\xi} p (\xi) \left[ \sum_ {i = 1} ^ {n _ {N}} \sum_ {j = 1} ^ {n _ {N}} c _ {i j} \left(\sum_ {k = 1} ^ {n _ {C}} x _ {i j k} (\xi)\right) + \gamma \left(\sum_ {j = 1} ^ {n _ {N}} \sum_ {k = 1} ^ {n _ {C}} u _ {j k} (\xi)\right) \right]\tag{B.1}
$$

Subject to:

$$
\sum_ {i = 1} ^ {n _ {N}} x _ {i j k} (\xi) = d _ {j k} (\xi) - u _ {j k} (\xi), \forall j, k, \xi\tag{B.2}
$$

$$
r _ {p q} x _ {i j p} (\xi) = r _ {q p} x _ {i j q} (\xi), \forall i, j, \forall p, q; p > q, \forall \xi\tag{B.3}
$$

$$
\sum_ {j = 1} ^ {n _ {N}} \sum_ {k = 1} ^ {n _ {C}} v _ {k} x _ {i j k} (\xi) \leq V z _ {i}, \forall i, \xi\tag{B.4}
$$

$$
\sum_ {j = 1} ^ {n _ {N}} \sum_ {k = 1} ^ {n _ {C}} w _ {k} x _ {i j k} (\xi) \leq W z _ {i}, \forall i, \xi\tag{B.5}
$$

$$
z _ {i} \leq \sum_ {j = 1} ^ {n _ {N}} \sum_ {k = 1} ^ {n _ {C}} x _ {i j k} (\xi), \forall i, \xi
$$

$$
\sum_ {j = 1} ^ {n _ {N}} y _ {i j} (\xi) \leq \alpha , \forall i, \xi\tag{B.6}
$$

(B.7)

$$
\sum_ {i = 1} ^ {n _ {N}} y _ {i j} (\xi) \leq \beta , \forall j, \xi\tag{B.8}
$$

$$
\sum_ {k = 1} ^ {n _ {C}} x _ {i j k} (\xi) \leq M y _ {i j} (\xi), \forall i, j, \xi\tag{B.9}
$$

$$
y _ {i j} (\xi) \leq \sum_ {k = 1} ^ {n _ {C}} x _ {i j k} (\xi), \forall i, j, \xi\tag{B.10}
$$

$$
z _ {i} \leq n _ {i}, \forall i\tag{B.11}
$$

$$
\sum_ {i = 1} ^ {n _ {N}} z _ {i} \leq N _ {T}\tag{B.12}
$$

$$
z _ {i} = 0, \forall i \in \{i: s _ {i} \leq S _ {T} \}\tag{B.13}
$$

$$
z _ {i} \in \mathbb {Z} ^ {+} \cup \{0 \}, \forall i\tag{B.14}
$$

$$
y _ {i j} (\xi) \in \{0, 1 \}, \forall i, j, \xi\tag{B.15}
$$

$$
x _ {i j k} (\xi) \in \mathbb {Z} ^ {+} \cup \{0 \}, \forall i, j, k, \xi\tag{B.16}
$$

$$
u _ {j k} (\xi) \in \mathbb {Z} ^ {+} \cup \{0 \}, \forall j, k, \xi\tag{B.17}
$$

The objective function given by Eq. (B.1) consists of the minimization of three components as the total (i) number of facilities allocated con sidering the accessibility of the neighborhoods, (ii) weighted-distance traveled by disaster victims and (iii) unsatisfied demand, where facility allocation and service decisions are performed in the first and second stages, respectively. Eq. (B.2) ensures that the total amount of supply equals to the satisfied demand. $\operatorname { E q . }$ (B.3) defines the supply-ratios between diferent commodity types. In other words, it is ensured that all commodities from the same neighborhood are supplied according to a certain (balanced) supply-ratio based on some standards and assumptions presented in Cavdur et al. (2016). Eqs. (B.4) and (B.5) are about the volume and weight capacities, respectively. Eq. (B.6) provides the relationship between the relevant decision variables. Eqs. (B.7) and (B.8) restricts the number of neighborhoods a neighborhood can serve and be served by, respectively, in order to prevent the chaotic situations after a disaster. Eqs. (B.9) and (B.10) relates the corresponding decision variables. Eq. (B.11) restricts the number of facilities allocated in a single neighborhood. while Eq. (B.12) limits the total number of facilities. Eq. (B.13) prevents allocating facilities in the neighborhoods whose safety levels are below the required threshold value for safety. Eqs. (B.14), (B.15), (B.16) and (B.17) are variable definitions.

Appendix C. User interface-additional forms  
![](/api/attachments/8GKADY2G/fulltext/images/6642ff3363bb0505055cb802c03ac564d2e3ef5fc20711b975b6059b5733f973.jpg)

Fig. C.1. Defining scenarios & probabilities.  
![](/api/attachments/8GKADY2G/fulltext/images/e2dfc2aca468aa099934c1b81773b2164a9962c0b188f1cff41727aef1a7d13b.jpg)  
Fig. C.2. Defining special configuration settings.

## Appendix D. Supplementary data

Supplementary data to this article can be found online at https://doi.org/10.1016/j.dss.2019.113145.

## References

[1] E. Rolland, R.A. Patterson, K. Ward, B. Dodin, Decision support for disaster management, Oper. Manag. Res. 3 (1–2) (2010) 68–79, https://doi.org/10.1007/ s12063-010-0028-0.

[2] F. Cavdur, M. Kose-Kucuk, A. Sebatli, Allocation of temporary disaster response facilities under demand uncertainty: an earthquake case study, International Journal of Disaster Risk Reduction 19 (2016) 159–166, https://doi.org/10.1016/j. ijdrr.2016.08.009.

[3] A.M. Caunhye, X. Nie, S. Pokharel, Optimization models in emergency logistics: a literature review, Socio Econ. Plan. Sci. 46 (1) (2012) 4–13, https://doi.org/10. 1016/j.seps.2011.04.004.

[4] G. Kovacs, K.M. Spens, Humanitarian logistics in disaster relief operations, International Journal of Physical Distribution & Logistics Management 37 (2) (2007) 99–114, https://doi.org/10.1108/096000307107.

[5] M. Natarajarathinam, I. Capar, A. Narayanan, Managing supply chains in times of crisis: a review of literature and insights, International Journal of Physical Distribution & Logistics Management 39 (7) (2009) 535–573, https://doi.org/10. 1108/096000309109.

[6] J.B. Sheu, Challenges of emergency logistics management, Transportation Research Part E: Logistics and Transportation Review 43 (6) (2007) 655–659, https://doi. org/10.1016/j.tre.2007.01.001.

[7] B.M. Beamon, B. Balcik, Performance measurement in humanitarian relief chains, Int. J. Public Sect. Manag. 21 (1) (2008) 4–25, https://doi.org/10.1108 095135508108.

[8] B. Balcik, B.M. Beamon, Facility location in humanitarian relief, Int. J. Logist. 11 (2) (2008) 101–121, https://doi.org/10.1080/13675560701561789.

[9] F. Kilci, B.Y. Kara, B. Bozkaya, Locating temporary shelter areas after an earthquake: a case for Turkey, Eur. J. Oper. Res. 243 (1) (2015) 323–332, https://doi. org/10.1016/j.ejor.2014.11.035.

[10] H.O. Mete, Z.B. Zabinsky, Stochastic optimization of medical supply location and distribution in disaster management. Int. J. Prod. Econ. 126 (1) (2010) 76–84 https://doi.org/10.1016/j.ijpe.2009.10.004.

[11] P. Murali, F. Ordonez, M.M. Dessouky, Facility location under demand uncertainty: response to a large-scale bio-terror attack, Socio Econ. Plan. Sci. 46 (1) (2012) 78–87, https://doi.org/10.1016/j.seps.2011.09.001.

[12] N. Noyan, B. Balcik, S. Atakan, A stochastic optimization model for designing last mile relief networks, Transp. Sci. 50 (3) (2015) 1092–1113, https://doi.org/10. 1287/trsc.2015.0621

[13] C.G. Rawls, M.A. Turnquist, Pre-positioning of emergency supplies for disaster response, Transp. Res. B Methodol. 44 (4) (2010) 521–534, https://doi.org/10.1016/ i.trb.2009.08.003.

[14] C.G. Rawls, M.A. Turnquist, Pre-positioning planning for emergency response with service quality constraints, OR Spectr. 33 (3) (2011) 481–498, https://doi.org/10. 1007/s00291-011-0248-1

[15] S.M. Thompson, N. Altay, W.G. Green III, J. Lapetina, Improving disaster response eforts with decision support systems, Int. J. Emerg. Manag. 3 (4) (2006) 250–263, https://doi.org/10.1504/IJEM.2006.011295.

[16] M.T. Ortuno, P. Cristobal, J.M. Ferrer, F.J. Martin-Campo, S. Munoz, G. Tirado, B. Vitoriano, B. Vitoriano, J. Montero, D. Ruan (Eds.), Decision aid models and systems for humanitarian logistics. A survey, Atlantis Press, Paris, 2013, pp. 17–44, , https://doi.org/10.2991/978-94-91216-74-9\_2 Decision Aid Models for Disaster Management and Emergencies.

[17] F. Fiedrich, F. Gehbauer, U. Rickers, Optimized resource allocation for emergency response after earthquake disasters, Saf. Sci. 35 (1–3) (2000) 41–57, https://doi. org/10.1016/S0925-7535(00)00021-7

[18] S. Ahmad, S.P. Simonovic, An intelligent decision support system for management of floods, Water Resour, Manag, 20 (3) (2006) 391–410. https://doi,org/10.1007

s11269-006-0326-3.

[19] D. Alvear, O. Abreu, A. Cuesta, V. Alonso, Decision support system for emergency management: road tunnels, Tunn. Undergr. Space Technol. 34 (2013) 13–21, https://doi.org/10.1016/j.tust.2012.10.005.

[20] S.R. Haynes, T.G. Kannampallil, M.A. Cohen, A. Soares, F.E. Ritter, Rampart: a service and agent-based architecture for anti-terrorism planning and resource allocation, Intelligence and Security Informatics, Springer, Berlin, Heidelberg, 2008, pp. 260–270, , https://doi.org/10.1007/978-3-540-89900-6\_26.

[21] A. Lorca, M. Celik, O. Ergun, P. Keskinocak, A decision-support tool for post-disaster debris operations, Procedia Engineering 107 (2015) 154–167, https://doi.org/10. 1016/j.proeng.2015.06.069.

[22] A.G. Hobeika, S. Kim, R.E. Beckwith, A decision support system for developing evacuation plans around nuclear power stations, Interfaces 24 (5) (1994) 22–35, https://doi.org/10.1287/inte.24.5.22

[23] S. Tufekci, An integrated emergency management decision support system for hurricane emergencies, Saf. Sci. 20 (1) (1995) 39–48, https://doi.org/10.1016/ 0925-7535(94)00065-B

[24] R.A. Hadiguna, I. Kamil, A. Delati, R. Reed, Implementing a web-based decision support system for disaster logistics: a case study of an evacuation location assessment for Indonesia, International Journal of Disaster Risk Reduction 9 (2014) 38–47, https://doi.org/10.1016/i.iidrr.2014.02.004

[25] M.S. Chang, Y.L. Tseng, J.W. Chen, A scenario planning approach for the flood emergency logistics preparation problem under uncertainty, Transportation Research Part E: Logistics and Transportation Review 43 (6) (2007) 737–754. https://doi.org/10.1016/j.tre.2006.10.013

[26] F.N. De Silva, R.W. Eglese, Integrating simulation modelling and GIS: spatial decision support systems for evacuation planning, J. Oper. Res. Soc. 51 (4) (2000) 423–430, https://doi.org/10.1057/palgrave.jors.2600879.

[27] N. Sahebjamnia, S.A. Torabi, S.A. Mansouri, A hybrid decision support system for managing humanitarian relief chains, Decis. Support. Syst. 95 (2017) 12–26, https://doi.org/10.1016/j.dss.2016.11.006.

[28] L. Ozdamar, E. Ekinci, B. Kucukyazici, Emergency logistics planning in natura disasters, Ann. Oper. Res. 129 (1–4) (2004) 217–245, https://doi.org/10.1023/ B:ANOR.0000030690.27939.39

[29] R. Kondaveti, A. Ganz, Decision support system for resource allocation in disaster management, 2009 Annual International Conference of the IEEE Engineering in Medicine and Biology Society, IEEE, 2009, pp. 3425–3428, , https://doi.org/10. 1109/IEMBS.2009.5332498.

[30] M. Rekik, A. Ruiz, J. Renaud, D. Berkoune, S. Paquet, A decision support system for humanitarian network design and distribution operations, in: V. Zeimpekis, S. Ichoua, I. Minis (Eds.), Humanitarian and Relief Logistics, Springer, New York, NY, 2013, pp. 1–20. , https://doi,org/10.1007/978-1-4614-7007-6 1.

[31] C. Fikar, M. Gronalt, P. Hirsch, A decision support system for coordinated disaster relief distribution. Expert Syst. Appl, 57 (2016) 104–116. https://doi,org/10.1016 j.eswa.2016.03.039.

Fatih Cavdur is an associate professor in the Department of Industrial Engineering at Uludag University. He has a Ph.D. in Industrial Engineering and Operations Research with a minor in Computational Science/High Performance Computing from PennState University. He teaches courses and performs research activities in operations research and its applications in various areas.

Asli Sebatli is a Ph.D. student in the Department of Industrial Engineering at Uludag University where she also received her MS degree. In her thesis, she worked on the de velopment of a decision support system prototype for disaster-response facilities alloca tion. Her research interests include operations research applications in humanitarian logistics.
