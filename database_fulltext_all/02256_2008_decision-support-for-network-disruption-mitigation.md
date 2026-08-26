---
otero_id: 2256
otero_key: "7YQFQEVG"
title: "Decision support for network disruption mitigation"
authors: "Diane E. Snediker; Alan T. Murray; Timothy C. Matisziw"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.11.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support for network disruption mitigation<sup>☆</sup>

Diane E. Snediker <sup>a,⁎</sup>, Alan T. Murray <sup>b</sup>, Timothy C. Matisziw <sup>c</sup>

<sup>a</sup> United States Census Bureau, 4600 Silver Hill Road, Washington, DC 20233, USA <sup>b</sup> Center for Urban and Regional Analysis and Department of Geography, The Ohio State University, Columbus, OH 43210, USA <sup>c</sup> Center for Urban and Regional Analysis, The Ohio State University, Columbus, OH 43210, USA

Received 21 February 2007; received in revised form 10 July 2007; accepted 11 November 2007 Available online 22 November 2007

## Abstract

Our increasing reliance on networks of all types, coupled with their increasing vulnerability to disruption, makes it critical to better understand risks associated with natural disasters, terrorist attacks, and other incidents. However, choosing how to best protect, reinforce, and improve a network given a limited budget is a complex problem. We have developed an integrated approach that examines the effects of different network disruption scenarios for a variety of performance measures. The developed decision support methodology allows for comprehensive exploration of disruption impacts, statistically and visually, and facilitates examination of “what-if” planning scenarios. © 2007 Elsevier B.V. All rights reserved.

Keywords: Networks; Survivability; Critical infrastructure; Spatial analysis; Strategic planning; Interdiction

## 1. Introduction

Networks of all types are increasingly vital to numerous aspects of daily life, particularly in highly developed countries such as the United States [4,5]. The impacts of network infrastructure failures on human lives go beyond mere inconvenience, given the potential longterm consequences of network disruption. For example, damaged natural gas pipelines can lead not just to higher energy prices, but energy shortages [40], which could have serious effects on the economy and quality of life. Damaged telecommunications infrastructure can likewise affect banking, transportation, and other economic activities, as well as the ability to provide critical services and information to populations at risk. It is crucial that we better understand the survivability of our critical infrastructures and identify risk mitigation measures [32].

Many recent studies have noted the increasing vulnerability of various types of networks to disruption by accident, disaster, or attack. There are a number of potential sources of network disruption: system complexity, deregulation, economic effects, power-market impacts, terrorism, human error, and natural disasters [5]. The US power grid is one critical network noted as being particularly vulnerable. The continuing evolution of the power system, along with the rising demands placed upon it, has resulted in new patterns of flow, of which we have very little knowledge or experience [21]. Infrastructure improvements are lagging behind increased demand [31], and Amin [5] asserts that “the electric power grid is being used in ways for which it was not originally designed.” As network use grows and expansion occurs, many network structures have experienced a decrease in redundancy and connectivity [2]. Disrupted infrastructures may be further impacted by failure of critical systems that deal with peak demand, as they are being pushed to their limits [4].

An additional impetus for studying the survivability of networks is their dependent nature. Various components of networks are dependent on the proper functioning of other network components, meaning that small disruptions can lead to cascading failures across the network [4]. Large-scale blackouts, for example, are occurring at rates greater than statistics would predict [8]. In addition, most networks rely, in part, on the proper functioning of other networks; in other words, they are interdependent. As Little [23] explains, “[i]nterdependent effects occur when an infrastructure disruption spreads beyond itself to cause appreciable impact on other infrastructures, which in turn cause more effects on still other infrastructures.” For instance, many types of networks are dependent on power and telecommunications networks, which are in turn dependent on each other [4,23].

Here we focus on planning for network survivability and risk management. Survivability is defined as “the capability of a system to fulfill its mission in a timely manner in the presence of attacks, failures, or accidents” [13]. Survivability is distinguished from the related concept of vulnerability given that survivability is concerned with the system's performance after a disaster has occurred, while vulnerability is more concerned with the system's susceptibility to disasters. Vulnerability analysis is also clearly important and could also be addressed with the proposed SDSS. This definition of survivability is generic, and it can be interpreted in many different ways. One might be concerned with survivability in terms of impacts to network connectivity: are all destinations still reachable from all origins [2,27,28]? Or, one might consider impacts to the actual flow through the network: how much normal network activity is inconvenienced or is unable to reach its intended destination [25,28]? Related to system connectivity, one might also ask: what are the effects of interdiction on network flow capacity [18,20,30]? Additionally, one might be concerned with the efficiency of network service: how is transit cost impacted, and are the destinations reachable within a minimum time or distance [21]? Given that many ways exist for understanding survivability, what is missing is a platform to support integrating and comparing alternative measures of system performance after disruption.

![](/api/attachments/7YQFQEVG/fulltext/images/30eb153121101c041975ef366548ed7054d57ef5202c0fa5d63a7d427c37e5e1.jpg)  
Fig. 1. Four scenarios involving the loss of three nodes, each impacting more than 78.5% of flow.

Developing strategies to deal with network disruption is a complex problem. One reason for this is that there exists a high degree of uncertainty as to the type of disruption that might actually occur as a network could be disrupted in hundreds, thousands, or even millions of ways, each with differing impacts to system performance. An example is given in Fig. 1, illustrating four different three-node disruption scenarios, each impacting more than 78.5% of the flow through the Abilene telecommunications network. Note that flow refers to the level of interaction between two network nodes. In this example, this interaction is bytes of data transmitted. More of this analysis with the Abilene network is detailed in the Impact assessment and Application sections of this paper. This network is relatively small, being comprised of 11 nodes and 14 arcs. In network analysis, nodes represent point locations such as telecom routers, power plants, or highway exchanges. Links or arcs refer to the components which integrate nodes, such as cables, transmission lines, or roads. Despite this network's size, there is little overlap in these worst-case scenarios. The associated range of risk can therefore be difficult to assimilate. A network manager might want to understand the difference between the worst-case and next-worst-case scenarios. How much worse is one scenario than the other? Are any components involved in both scenarios? Are particular nodes involved in other worst-case (or near-worst-case) scenarios? And how do these outcomes differ based on the performance measure used? Understanding the implications of network survivability requires exploratory analysis. To support this exploration, and to allow planners to gain management insights, a spatial decision support system for network disruption mitigation is developed. This system is designed to assist in identifying critical network components and to help facilitate decisions about maintaining or enhancing network survivability. From a management and planning perspective, this interactive and integrative support for evaluating a range of scenarios and approaches is a necessity.

The remainder of the paper is organized as follows. The next section provides background on network analysis, disaster management, spatial decision support systems, and geographic information systems. The following section describes the developed decision support methodology and provides some implementation details. Next, the use of the system in the analysis of a telecommunications backbone illustrates important features. Finally, conclusions are provided.

## 2. Background

## 2.1. Network analysis and disaster management

Critical infrastructure analysis and protection has been approached in a variety of ways. For instance, much research has focused on the design of survivable networks [11,34] and the reinforcement or fortification of existing networks [32]. Central to this work is the development of an understanding of how disruptions can impact network operation. A typical approach to assessing impacts of disruption is to identify the most significant, critical, or important network components in order to prioritize mitigation efforts [18], and many approaches have been proposed in this regard.

One class of approaches centers on topological properties of individual nodes [2,18], such as their degree (number of coincident links) and betweenness or centrality (the number of shortest paths in which a node appears). These measures approximate a node's importance to the network.

Another class of approaches focuses on identifying the components (nodes or links) involved in the worst-case disruptions, in terms of impacts to flow capacity or other network efficiency measures [6,20,24,30]. More recently, a growing body of research has highlighted the importance of assessing impacts of disruption to system flow. That is, given that many interacting origins/destinations may exist within a network, which components if disrupted will impact the most interaction (flow) between these origin– destination (O–D) pairs? Several models have been proposed in this regard to identify upper and lower bounds on system flow loss given component disruption [25,28].

Other approaches more fully examine the range of possible disruption scenarios. Previous research [26] enumerated all potential node or link disruption scenarios for a network and found that the magnitude of disruption is not always influenced by the topological characteristics of individual nodes. Further, it was found that it is important to consider the full range of potential scenarios, rather than just the worst case. In particular, the nextworse case can often be just shy of the worst. Another complicating factor was that in many cases there were no clear “winners” in terms of most important nodes or links. The nodes or links associated with the worst-case scenario generally differed depending on the magnitude of disruption [27,28].

The motivating factor behind all of this work on assessing network disruption survivability is the ability to gain insight for mitigation efforts. Disaster management planning relies upon a systematic evaluation of all aspects of a potential event. However, given the range of approaches and data available to the decision maker for planning for disaster mitigation and recovery, what is particularly lacking is a set of tools for assimilating this planning information [3]. Further, such planning decisions are often complicated by limited resources, system complexity, and the need to explore alternative plans for disaster management [7]. These observations clearly point to the need for a decision support system for network disruption mitigation.

## 2.2. Spatial decision support systems and geographic information systems

A decision support system (DSS) is defined as a “flexible, adaptive, responsive and interactive computerbased system for decision support” [22]. A spatial decision support system (SDSS) is a DSS with a prominent spatial component. Simon [33] proposed a three-phase process of decision-making. These three phases are: 1) Intelligence — determining whether there is a problem and gathering information about the problem; 2) Design — determination of alternatives; and 3) Choice — deciding upon a particular alternative. Our system focuses on the design phase, identifying alternatives most likely to be beneficial, although it does include some tools which could be considered appropriate to the intelligence and choice phases as well.

In the literature there is an evident interest in decision support system development for disaster management involving networks. For instance, Cosares et al. [11] designed a system to facilitate the design of survivable networks, with a focus on construction cost. In Hood et al. [19] a system for assessing the likelihood of network component failure and evaluating appropriate responses to these potential losses is discussed. Other SDSS have been developed for determining the most efficient methods for evacuating people from an area, based on which parts of the network are expected to still be functional in an emergency [9,38]. The DSS developed in Crozi et al. [12] can be used for assessing the vulnerability of transportation and power networks to earthquakes, and contains a component which determines the maximum and minimum probabilities that two points in a network will be connected after the event. Finally, in a somewhat different field, landscape management, Fuller and Sarkar [16] develop a software program for addressing the impact of connectivity (loss/gain) in biological systems. However, despite this interest in network disaster management, the authors have not found any other systems to date which support spatial decision-making for network disruption mitigation.

Though not in the context of network management, some research has focused on the importance of being able to visualize the choices, scenarios, or solutions on a map while simultaneously examining their rankings or objective values [10,37]. The importance of a graphical interface in enabling the visualization of corridor siting in order to understand the spatial implications of the problem and potential solutions was emphasized in [10]. Uran and Janssen [37] undertook an examination of several different SDSS (for a variety of spatial decisions) to determine why many were not used, and came up with several characteristics that they feel are important for all good spatial decision support systems. They identified the following features that were lacking in many of the unused systems: comprehensible output that is easy to use in decision-making, support for analyzing or evaluating output, support for spatial evaluation, and the ability to easily specify, compare and rank alternatives.

Given the broad geographic extent of many infrastructures, managing associated spatial information can be a challenge. Geographic information systems (GIS) are typically used to support this task. GIS offers a practical means of storing and manipulating geographically referenced objects, as well as facilitating visualization and spatial querying of the associated information. Thus, incorporating GIS functionality into decision support systems is critical for permitting exploration of the geographic implications of disasters. Although many of the DSS mentioned above deal with disaster management, none offer an interactive support system for evaluating potential disruption to network infrastructures which would facilitate understanding of associated spatial implications. In the following sections, we detail the development and implementation of an SDSS for network infrastructure disruption mitigation.

## 3. Supporting infrastructure protection

An SDSS framework for mitigating network disruption impacts is detailed. This approach consists of several interacting components: data input, scenario generation and impact assessment, measurement comparison and testing, exploratory scenario analysis, and disruption remediation. Fig. 2 is a function-oriented diagram illustrating the elements of our implementation of this framework.

![](/api/attachments/7YQFQEVG/fulltext/images/fa8cce51065ca97a5871eb3e65b6cac37106c293cc8ac0623ca2321153d42342.jpg)  
Fig. 2. System framework and function diagram.

## 3.1. Data input

The data input requirements for the developed system are relatively minimal. As can be seen in Fig. 2, the user must supply GIS network topology data (nodes and arcs). Other network attributes (e.g. distance, travel cost, and capacity) can easily be accommodated and/or derived. In addition, O–D flow data for the network can also be input to represent actual activity within the network system and to take advantage of many of the exploratory functions of the SDSS. If flow data is not available, analysis can be simply conducted on connectivity between O–D pairs.

## 3.2. Scenario generation

Evaluating network infrastructure requires the assessment of disruption scenarios of interest. A scenario here refers to the debilitation of a set of network components (nodes/arcs). For instance, a user might be interested in evaluating possible impacts associated with a two-node failure. The developed SDSS provides support for generating these scenarios in multiple ways. As Fig. 2 indicates, options include complete enumeration of all potential scenarios, statistical sampling of scenarios, adhoc identification of scenarios, strategy-based disruption, and optimization-based methods for determining the upper and lower bounds on disruption impacts. Once a particular scenario has been generated, its potential impact to system performance can be assessed relative to derived ranges.

The optimization option in the SDSS allows the user to identify the disruption scenarios maximizing or minimizing network damage (e.g. the upper and lower bounds of disruption). One spatial network optimization model capable of identifying these bounds is the Flow Interdiction Model [28]. This model, and its variations [25,27], focus on maximization and minimization of disrupted flow or connectivity involving a specific number of disrupted nodes or links. The mathematical details for this model are provided in Appendix A.

While bounds on network survivability are clearly of planning interest, often multiple optima or near-optimum scenarios may exist. One might wish to further characterize the range of potential disruption scenarios within the established bounds. Thus, another option for scenario generation, consistent with the systematic simulation approach discussed earlier, is to enumerate all scenarios. Where such an approach is not computationally feasible, an alternative function is provided to randomly sample a certain number of disruption scenarios. Using this scenario enumeration/sampling method, the user can specify nodal disruption, arc disruption, or a combination of the two. Previous approaches have generally concentrated on one or the other, so the ability to model scenarios involving both nodal and arc disruption is a valuable feature.

The third option in Fig. 2 for Scenario generation and Impact assessment, strategy-based disruption or attack, is an approach for identifying nodal disruption scenarios and comparing them with the best and worst-case scenarios (identified by one of the above methods). For each strategy, nodes are disrupted one by one given an attack strategy. For example, in the random strategy, nodes are successively chosen at random for disruption. In addition to random disruption, node loss can also be set to proceed in decreasing fashion based on nodal characteristics (e.g.

degree and centrality), with and without recalculation of these characteristics after each disruption.

A fourth option, ad-hoc/situation specific, is also provided. This approach involves manual selection of the components to be disrupted. Disruption results and measures associated with that scenario can then be visualized in a graphical interface. This permits users to interactively swap performance measures for any of the scenarios generated and evaluate and compare the outcomes spatially and graphically. This is a valuable feature given that impact to multiple performance attributes of a system might be of concern (e.g., flow, connectivity, accessibility, etc.).

## 3.3. Impact assessment

As illustrated under Impact assessment in Fig. 2, for each disruption scenario, impacts to network performance can be measured in terms of impacts to origin–destination (O–D) connectivity and system flow. Assessing these impacts involves determining, for each O–D pair, whether any viable paths still exist between that origin and destination. A path here simply refers to a sequence of arcs and nodes that can connect an O–D pair. Thus, many potential paths of movement often exist for each O–D pair. All flow between an origin and destination is considered to be disrupted if no paths between those nodes are available given the component disruption scenario.

Further, a variety of common network topology indices can be reported for each scenario, including measures of accessibility, connectivity, and centrality. The measures are described briefly below, and the mathematical definitions of some available statistics are listed in Table 1.

Various measures of connectivity are available for each generated scenario within the SDSS. These include shortest path/minimum cost measures (e.g., average, minimum, and maximum shortest path by distance or travel cost and by number of steps) as well as the cyclomatic number, gamma index, alpha index, and beta index. All of these measures give a general description of the network's overall connectivity (see [17] for more details). Centrality of individual network arcs and nodes, or the network as a whole, can also be computed in the SDSS for each disruption scenario. The centrality of each node is a measure of how many shortest paths it appears in (except those where it is the origin or destination) [15].

Three common accessibility and dispersion measures (commonly referred to as the T, D, and L matrices) are also provided for describing disruption scenarios. The T matrix, or accessibility matrix, is a measure of the number of nodal sequences between each O–D pair in the network (excluding those sequences from a node back to itself).

The D matrix, also known as the Shimbel distance or dispersion matrix, contains the shortest path, in number of links, between each O–D pair in the network. The L matrix, or value graph, is similar to the D matrix; however, actual distance or travel cost figures between nodes are used rather than the number of steps. All three of these accessibility measures can be summarized for individual nodes or for the network as a whole (see [35] for more information).

## 3.4. Measurement comparison and testing

Given that a variety of survivability measures can be analyzed in the SDSS, incorporating the capability to compare them is an important consideration. At the most basic level, the system can compute distributional statistics (mean, median, standard deviation, etc.) for individual numbers of disrupted components, for a range of numbers of components, and for the user's current selection of scenarios (this is the statistical distributions option in Fig. 2). The SDSS also provides the capacity to derive a Flow Disruption Index (FDI). This measure is generated for each network node or link, given a particular number of disrupted components, and represents the disruptive potential of a scenario containing that node or arc relative to the worst-case scenario involving any nodes or arcs. The mathematical specification of the FDI is given in Appendix B.

Definitions of selected connectivity and centrality measures

<table><tr><td>Measure</td><td colspan="2">Definition</td></tr><tr><td>Cyclomatic number</td><td> $a - n + s$ </td><td></td></tr><tr><td rowspan="2">Gamma index</td><td> $(a/3(n-2))*100$ </td><td>(non-planar)</td></tr><tr><td> $(a/(n(n-1)/2))*100$ </td><td>(planar)</td></tr><tr><td rowspan="2">Alpha index</td><td> $((a-n+s)/((n(n-1))/2)-(n-1))*100$ </td><td>(non-planar)</td></tr><tr><td> $((a-n+s)/2n-5)*100$ </td><td>(planar)</td></tr><tr><td>Beta index</td><td> $a/n$ </td><td></td></tr><tr><td>Node centrality</td><td> $C_{B}(p_{k}) = \sum_{i \neq k} \sum_{j \neq k > i} b_{ij}(p_{k})$ </td><td></td></tr><tr><td>Node relative centrality</td><td> $C'_{B}(p_{k}) = 2C_{B}(p_{k})/n^{2} - 3n + 2$ </td><td></td></tr><tr><td>Network relative centrality</td><td> $C'_{B} = \frac{\sum_{i} \left[ C'_{B}(p_{k}^{*}) - C'_{B}(p_{i}) \right]}{n - 1}$ </td><td></td></tr></table>

a = number of links in the network.  
n = number of nodes in the network.  
s = number of subgraphs in the network.  
i,j,k = node indices.  
$p = \mathrm { a }$ particular node.  
b = node betweeness for pair ij (the percentage of pair ij's geodesics on which $( p _ { k } )$ appears).  
$p _ { k } * =$ the node with highest relative centrality in the network.

![](/api/attachments/7YQFQEVG/fulltext/images/acd60708773b4a0131e49d49502e6b0c028a5e45e2b81dc45e89bb9771a3e7c6.jpg)  
Fig. 3. Flow data from and to Kansas City (magnitude reflects amount of flow).

Another desirable aspect of the developed SDSS related to measurement comparison is the ability to visualize flows between O–D pairs on a map (view flow data). Because this generally includes flows from every origin to every destination, it is hard to discern many differences when viewing this information for the network as a whole, even for small networks. Therefore, the capability to view the flows involving each node separately is also provided. This feature includes an option to size these flows in relation to flows for the network as a whole, or in relation to flows for only that node. The former option allows the user to see how these flows compare to all network flows, while the latter generally permits more differentiation between the flows for a particular node. Fig. 3 presents an illustration of this functionality.

## 3.5. Impact exploration

A central feature of the system is the ability to explore the range of disruption scenarios and their consequences, both statistically and spatially (see Fig. 2). Thus, the system is implemented with two linked sections of the screen: a graph of all results on one side, and maps and charts of selected results on the other side. This allows the user to see the spatial configuration that accompanies a particular scenario while simultaneously viewing its disruption impact relative to other scenarios. This is very important because it allows the user to consider the spatial implications of particular scenarios rather than a list of components — there may be significant geographical aspects to the problem that would not otherwise be highlighted. The locations of critical components could have important implications for their vulnerability, potential for protection, and interaction with other systems. It is also significant that these maps are interactive to permit in-depth and flexible scenario analysis.

The intent of this multiple screen design is to allow the user to select a scenario or subset of scenarios and generate and view information about their selection. This information may include maps of each selected scenario, summary maps or charts indicating the prominence of each network component within the chosen subset, or other summary statistics. More details about the inter-related activities of interactive graphing/ mapping and interactive spatial and range impact analysis are given in the Application section.

## 3.6. Disruption remediation

An important component of an SDSS is the ability to use provided information and insight for decisionmaking, in many cases predicting or determining the consequences of potential actions. As shown in Fig. 2, in the case of network disruption, two possible protection strategies are strengthening particular network components (reinforcement/protection) and adding new links to the network (network modification). The system allows the analyst to quantify the effect that different protection scenarios would have on the range of possible network disruption. With this information it is possible to develop remediation priorities.

This aspect of the system is extremely valuable because of the challenges involved in remediation. The cost of adding an additional link to the network is likely to be much larger than the cost of reinforcing a node, and these costs will likely vary depending on the particular link or node involved. The cost–benefit tradeoff is not straightforward, due to the complexity discussed previously. While the network manager can likely estimate the cost of particular remediation scenarios, the benefits of those scenarios will differ depending on the measure (s) used and level(s) of disruption considered.

## 4. Application

The spatial decision support system developed here, NIMPRO (Network Interdiction Mitigation and PROtection), was programmed in Microsoft Visual Basic 6.0, relying on component modules to carry out specific functions. Such components currently include ESRI MapObjects 2.4, ILOG CPLEX 10.0, and GigaSoft ProEssentials 5. The decision was made to develop the system in Visual Basic using MapObjects rather than within a commercial GIS in order to take advantage of the more complete programming methods available. Embedding GIS functionality within an SDSS is typically considered to be more appropriate than adding decision support functions to a GIS [22]. All of the GIS functions necessary for NIMPRO were provided by or derived from MapObjects.

In this section the implementation and benefits of selected functions are highlighted, and the Abilene

Internet2 backbone network is used to illustrate the associated functionality. Abilene is a telecommunications network mainly connecting U.S. research institutions and topologically consists of eleven nodes (routers) connected by fourteen arcs (fiber optic cables). Flows between routers (in bytes) were obtained to represent actual network activity, details of which can be found in [1,28]. For this analysis, we use past flows to represent current or future operating conditions, but this need not be the case. Users can easily input flows estimated for any time period. Many methods exist for estimating future interaction levels (See [14,29,36,39,41]).

In terms of the optimization approach to identifying best- and worst-case scenarios, NIMPRO aids in this process by generating and solving the Flow Interdiction Model [28] and its variants [25,27], and displaying model results. Specifications for the models are entered via checkboxes, drop-down menus, and other standard Windows data entry controls in a dialog box. These specifications include: whether the user wishes to maximize or minimize post-disruption performance, the desired performance measure (e.g. flow or connectivity), whether to interdict nodes or links, and how many components to disrupt. Additionally, the user may specify particular components for reinforcement to prevent their disruption. This allows for the identification of best and worst cases under different potential protection scenarios. NIMPRO is integrated with ILOG CPLEX (a commercial optimization solver) via a DLL. Once a selected mathematical program is generated using the input network data, CPLEX is automatically called to solve the problem, and the solution results are read back into the SDSS for visualization and analysis. The main benefit of this integration is its ease of use— the problem specification is developed from the topology (and flow) data already entered into the system and results appear quickly with no need for editing of files, switching between programs, or deciphering CPLEX output on the part of the user. For very large networks, this functionality can be invaluable in allowing the program user to examine the bounds of disruption survivability of the network, as well as to evaluate potential disruption scenarios in terms of these bounds.

Table 2 includes these bounds for disruptions involving two through six nodes in the original Abilene network, as well as for the case where the Washington DC node is reinforced (cannot be disabled). We can see from this table that none of the lower bounds within this range are affected by the reinforcement of Washington DC, indicating that this node is not in any of the bestcase scenarios. However the DC node is involved in four out of five worst-case scenarios (loss of two, three, five and six nodes), as evidenced by the reduced upper bounds of disruption given protection of the DC node. Although the best- and worst-case disruption scenarios are certainly of concern, there are many other scenarios falling between these bounds that are potentially important. This is where scenario enumeration or sampling is crucial.

Table 2  
FIM-generated disruption bounds for the Abilene network (with and without Washington DC reinforced) in terms of percent of flow bytes disrupted

<table><tr><td rowspan="2"></td><td colspan="2">Unreinforced</td><td colspan="2">Washington DC reinforced</td></tr><tr><td>Lower bound</td><td>Upper bound</td><td>Lower bound</td><td>Upper bound</td></tr><tr><td>2 nodes lost</td><td>15.04</td><td>73.53</td><td>15.04</td><td>63.82</td></tr><tr><td>3 nodes lost</td><td>29.12</td><td>81.10</td><td>29.12</td><td>80.62</td></tr><tr><td>4 nodes lost</td><td>39.40</td><td>91.61</td><td>39.40</td><td>91.61</td></tr><tr><td>5 nodes lost</td><td>50.55</td><td>95.96</td><td>50.55</td><td>94.54</td></tr><tr><td>6 nodes lost</td><td>60.31</td><td>98.64</td><td>60.31</td><td>96.21</td></tr></table>

Enumerated scenarios are summarized in a graph on the left side of the main screen, with the number of components disrupted referenced on the X axis and the chosen measure of network performance (e.g. number of O–D pairs disconnected, percent of flow disrupted, etc.) listed on the Yaxis. This chart allows the user to view the full range of network disruption across the various levels of component disruption to facilitate further examination of this range. Fig. 4 illustrates this chart for node disruption and percent of flow bytes disrupted in the Abilene network. It is evident from this chart that while there is a fairly large difference between the worst-case and next-worst-case scenarios for one or two nodes disrupted, for three or more nodes disrupted there is almost no difference in percent flow bytes disrupted from one scenario to the next worst.

In order to more closely compare scenario impacts, the ability to zoom in on a portion of the chart is incorporated as individual scenarios can be difficult to distinguish given the volume of data. An option is also included to view this distribution in 3D, where the user can rotate it both vertically and horizontally in order to provide alternate renderings of the complete distribution. The user may directly select a charted scenario to immediately view the geographical outcome associated with the scenario in a map displayed on the right side of the screen. The user may also choose to select a subset of scenarios for further analysis by several methods: individually selecting points, drawing a box to select a group of data, or using a dialog box to select a range of X (e.g. 1–3 nodes disrupted) and or Y values (e.g. scenarios within 5% of the worst). This allows the user to visualize which nodes or links are involved in scenarios over a range of potential disruptions of interest. If multiple scenarios are chosen, a map is generated for each, allowing the user to quickly examine the spatial characteristics of the selected group of scenarios. Fig. 1 illustrates these maps for four selected scenarios. As noted previously, these scenarios all involve the loss of three nodes, each resulting in the disruption of more than 78.5% of the flow. There is not a great deal of spatial overlap in these scenarios; all but two of the nodes in the network are represented in this selection. So how does a manager determine which components' protection might benefit the network the most?

There are two other possible views of the data for the selected scenarios: a map and a chart summarizing the appearances of each component in the selection. In the map, each node or arc is sized proportionally to the number of selected scenarios in which it appears. This allows the user to see the spatial extent of the selected scenarios in a summary form, facilitating quick visual inspection of the locations of components featured in the most selected scenarios with respect to one another. Fig. 4 presents an example of this view in the Abilene network for the selection of the top ten worst-case scenarios involving the loss of 2 through 6 nodes. We can see from this map that the Washington DC and Sunnyvale nodes appear the most in this particular selection, thus there is reason to believe that reinforcing or hardening these nodes against attack might be warranted.

An interactive approach to network protection assessment is also implemented in NIMPRO. The user can simply select on a network component on the righthand map or chart to toggle its reinforcement status as on or off. With each new set of reinforced components, the color of the scenario points in the left-hand chart will change for all scenarios that would no longer be possible if the specified nodes or links were reinforced (i.e. all disruption scenarios involving one or more of those protected components). This permits the user to visualize where the reinforced scenarios occur within the range of all possible scenarios. In addition, a table below the graph illustrates the difference between the worst-case scenario with and without the reinforcement of the selected components for each number of components disrupted. Table 3 contains the figures from this difference table for Washington DC with the same selection as above. We can see that reinforcing Washington DC would make the most difference given a loss of two nodes, since the percent of flow loss associated with the worst-case scenario drops from 73.53 to 63.82.

963 D.E. Snediker et al. / Decision Support Systems 44 (2008) 954–969  
![](/api/attachments/7YQFQEVG/fulltext/images/810864f1a03589ede52841a28dde2e5ced925089e0ca5f66965b4d4431e13b88.jpg)  
Fig 4 Nodes appearing in top 1 0 worst-case scenarios by percent flow bytes disrupted (2–6 nodes lost)

Table 3  
Worst-case difference table with Washington DC disrupted

<table><tr><td rowspan="2"></td><td colspan="12">Number of nodes disrupted</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td></tr><tr><td>Original worst case</td><td>0.00</td><td>37.63</td><td>73.53</td><td>81.10</td><td>91.61</td><td>95.96</td><td>98.64</td><td>99.02</td><td>99.38</td><td>99.67</td><td>99.85</td><td>100.00</td></tr><tr><td>Current worst case</td><td>0.00</td><td>29.25</td><td>63.82</td><td>80.62</td><td>91.61</td><td>94.54</td><td>96.21</td><td>96.21</td><td>96.90</td><td>97.08</td><td>97.23</td><td>N/A</td></tr><tr><td>Difference</td><td>0.00</td><td>8.38</td><td>9.71</td><td>0.47</td><td>0.00</td><td>1.42</td><td>2.43</td><td>2.41</td><td>2.48</td><td>2.59</td><td>2.62</td><td>N/A</td></tr></table>

If we look at the top ten worst-case connectivity disruption scenarios involving the loss of two through six nodes, we find that the most important nodes are not the same as those identified as being important to system flow. In this case, Kansas City appears in the most selected scenarios, with Sunnyvale and Atlanta in a tie for second place. Washington DC now appears in the second least number of selected scenarios. If Kansas City is protected from an attack, the worst-case scenario is only slightly reduced, due to the large number of scenarios which result in equivalent levels of connectivity disruption.

If the selection is based on particular criteria (i.e. top ten worst-case scenarios given the loss of two through six nodes), the system will re-apply these selection criteria for the scenarios that are still viable after reinforcement, and update the aggregate map to reflect each node's new appearance totals. This is critical for assisting the user in considering protection scenarios involving more than one component. For example, considering no nodal reinforcement, we find that the Washington DC and Sunnyvale nodes appear to be the most critical to system flow. After Washington DC is reinforced, however, Atlanta appears the most in the resulting selection, with New York a close second (Fig. 5). Sunnyvale is third, but has a substantially lower number of appearances than the other two. In this case, it appears that many of the most damaging scenarios involving Sunnyvale also involve Washington DC, so reinforcing both of these nodes may not be the most cost-effective option for disruption mitigation in this case. In the connectivity disruption analysis, after Kansas City is reinforced, the nodes which are directly connected to it (Indianapolis, Denver, and Houston) appear most important in the adjusted selection (Fig. 6). Again, the other originally critical nodes drop in importance after nodal reinforcement. These insights would be very difficult and time-consuming without an SDSS like NIMPRO to facilitate these analyses.

A network planner may also want to explore adding a link to the network to determine the effect that this would have on the network's survivability. For this example, we experimented with adding arcs between Seattle and Indianapolis, and Seattle and Chicago, as these arcs would appear to provide an additional connection between the eastern and western portions of the network. In its current form, the network could be split into two subgraphs through loss of just two components.

To complete the analysis, we generated distribution statistics (minimum, maximum, and median flow bytes interdicted at each level of disruption) for each network configuration containing an additional arc, as well as the original configuration. We then performed a comparison of these statistics over the range of disruption levels that we examined before — loss of two through six components. Results of this comparison are given in Table 4. We can see from these results that adding an arc between Seattle and Indianapolis would provide no additional benefits over the original configuration in terms of the flow disruption possible given node disruption. For link disruption, either link addition offers some improvements in the best, worst, or median case disruptions that can be expected. However, close inspection shows that the Seattle–Chicago addition offers more improvement (greater survivability) in more cases than the Seattle–Indianapolis addition, at least within this range of component loss. If we simply inspected a map of the network, these two network modification plans might have appeared to be roughly equivalent, but clearly they are not.

## 5. Conclusions

Network management and protection is an extremely complex problem. This paper introduced a spatial decision support system methodology and its implementation, NIMPRO, which helps to facilitate exploratory analysis of disruption scenarios. It does this through providing multiple views of network infrastructure, including interactive charts and maps, and through many mathematical and statistical tools that allow the user to obtain insights about disruption and “what-if” analyses. There are countless ways of examining a network's survivability, and we have designed this application to be flexible in representing these, and to allow examination of their geographic and topologic implications. We have found no other SDSS which allow a manager to input data about any network and run analyses specifically designed to help him or her make decisions about how best to mitigate disruptions to the network under future disaster scenarios. Some previous systems and approaches have incorporated related problems, such as survivable network design or earthquake vulnerability, but these have been specific to particular types of networks, technologies, or disasters. Our approach is applicable to any networked system and is concerned with the difficulties of assessing, understanding, and mitigating the effects of disruptions of all types.

![](/api/attachments/7YQFQEVG/fulltext/images/f761b602ead4aaf5fd2fbae865d984c8029bc7a6ef9ef48a992a75042f4ff046.jpg)  
Fig. 5 . Nodes appearing in top 1 0 worst-case scenarios by percent flow bytes disrupted (2–6 nodes lost) with Washington DC reinforced

![](/api/attachments/7YQFQEVG/fulltext/images/7a28cbbde4e1549b6f9fb84bdbd31c183e205417838a70f5afc88eb3db7d52c6.jpg)  
Fig. 6 . Nodes appearing in top 1 0 worst-case connectivity disruption scenarios (2–6 nodes lost) with Kansas City reinforced

Minimum, maximum, and median percent flow bytes interdicted for node and link interdiction scenarios for varying network configurations

<table><tr><td rowspan="2"></td><td colspan="3">2 nodes int.</td><td colspan="3">3 nodes int.</td><td colspan="3">4 nodes int.</td><td colspan="3">5 nodes int.</td><td colspan="3">6 nodes int.</td></tr><tr><td>Min</td><td>Max</td><td>Med</td><td>Min</td><td>Max</td><td>Med</td><td>Min</td><td>Max</td><td>Med</td><td>Min</td><td>Max</td><td>Med</td><td>Min</td><td>Max</td><td>Med</td></tr><tr><td>Original</td><td>15.0</td><td>73.5</td><td>37.8</td><td>29.1</td><td>81.1</td><td>60.2</td><td>39.4</td><td>91.6</td><td>74.6</td><td>50.6</td><td>96.0</td><td>84.7</td><td>60.3</td><td>98.6</td><td>90.3</td></tr><tr><td>Sea-Chi</td><td>12.2</td><td>70.4</td><td>32.4</td><td>20.7</td><td>80.4</td><td>52.5</td><td>33.0</td><td>90.9</td><td>70.8</td><td>45.6</td><td>96.0</td><td>84.7</td><td>60.3</td><td>98.6</td><td>90.3</td></tr><tr><td>Sea-Ind</td><td>15.0</td><td>73.5</td><td>37.8</td><td>29.1</td><td>81.1</td><td>60.2</td><td>39.4</td><td>91.6</td><td>74.6</td><td>50.6</td><td>96.0</td><td>84.7</td><td>60.3</td><td>98.6</td><td>90.3</td></tr><tr><td rowspan="2"></td><td colspan="3">2 links int.</td><td colspan="3">3 links int.</td><td colspan="3">4 links int.</td><td colspan="3">5 links int.</td><td colspan="3">6 nodes int.</td></tr><tr><td>Min</td><td>Max</td><td>Med</td><td>Min</td><td>Max</td><td>Med</td><td>Min</td><td>Max</td><td>Med</td><td>Min</td><td>Max</td><td>Med</td><td>Min</td><td>Max</td><td>Med</td></tr><tr><td>Original</td><td>0</td><td>49.4</td><td>0</td><td>0</td><td>63.7</td><td>0</td><td>0</td><td>67.6</td><td>28.2</td><td>6.0</td><td>77.3</td><td>43.7</td><td>14.7</td><td>81.0</td><td>55.0</td></tr><tr><td>Sea-Chi</td><td>0</td><td>43.4</td><td>0</td><td>0</td><td>53.2</td><td>0</td><td>0</td><td>63.7</td><td>0</td><td>0</td><td>68.8</td><td>22.0</td><td>6.0</td><td>77.3</td><td>41.1</td></tr><tr><td>Sea-Ind</td><td>0</td><td>49.4</td><td>0</td><td>0</td><td>63.7</td><td>0</td><td>0</td><td>67.6</td><td>22.0</td><td>0</td><td>77.3</td><td>41.1</td><td>6.0</td><td>81.0</td><td>49.9</td></tr></table>

Due to problem complexity, it is important for network planners who want to make best use of any available funds to examine their network's survivability from multiple perspectives. Choosing one method that appears to provide an easy answer is overly simplistic and may lead to a poor decision. NIMPRO assists with allowing the problem to be examined via a range of approaches by bringing them together into one application. Within the same system, a user can evaluate O–D connectivity and multiple measures of flow in the network, maximum and minimum disruption scenarios and all scenarios in between, protection scenarios, and a large number of associated statistics and summary measures.

With our interface design, we have tried to address the complexity of the decisions to be made, and to synthesize many different forms of analysis to promote network understanding. In describing spatial decision support systems, several authors stressed the importance of viewing the actual geography of a scenario along with its statistical information, and we have therefore dedicated half of the screen to scenario display, either individual or aggregate. The display is also interactive, in that selecting a point on the left-hand side of the screen immediately changes the display on the right-hand side. Also, the user may select directly from the aggregate map or chart to reinforce a node or arc, which updates the chart and table on the left-hand side of the screen. The user can quickly and easily specify and see the effects of different potential protection options without having to make changes to the underlying data, or go through a long series of steps. In addition, statistics and other views of the data have been offered at multiple levels of granularity as much as is practical. We provide both aggregate and individual level map views, and distribution statistics are available for any combination of disruption scenarios desired through the statistical distribution function. If desired, network measures can be calculated for the network under each disruption scenario, as well as for the original network.

As detailed above, Uran and Janssen [37] identified several features missing from unused SDSS; we have tried to incorporate these as well. Comprehensible output is provided by the ability to save results and statistics to spreadsheet files, where they can be combined in any way that the user wishes. In addition, all charts and maps may be saved as images for later visual consideration, or sharing with members of a team. The reinforcement option addresses the critical decision support function of testing “what-if” scenarios. While the complexity of the problem does not lend itself to a simple ranking function, users can easily manipulate and rank the spreadsheet output by any desired criteria.

A very important area for future research, and a logical next step, would be to include tools that help the user with the choice phase of the decision-making process. The application generates a lot of information, potentially from many different perspectives. As has been noted throughout this paper, this information is often contradictory and does not always point to a clear best solution. Thus, providing ways to incorporate this information with things like cost–benefit analyses, component vulnerability studies, and cross-infrastructure dependencies would also be beneficial.

## Acknowledgment

This material is based upon work supported by the National Science Foundation under Grant No. 0720989. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.

## Appendix A. The Flow Interdiction Model [28]

## Notation

$k$ index of paths, entire set denoted K $j$ index of nodes, entire set denoted J $o$ index of origins, entire set denoted Ω $d$ index of destinations, entire set denoted Λ $N _ { o d }$ set of paths enabling O–D flow $f _ { o d }$ flow observed between O–D $p$ number of nodes to remove $\varPhi _ { k }$ set of nodes along path k $X _ { j }$ {1 if node j is disrupted {0 otherwise $Y _ { k }$ {1 if path k remains unaffected by disruption {0 otherwise $Z _ { o d }$ {1 if no flow possible between O–D {0 otherwise

Flow Interdiction Model (FIM)

Maximize or minimize

$$
\sum_ {o} \sum_ {d} f _ {o d} Z _ {o d}\tag{1}
$$

Subject to:

$$
\sum_ {k \in N _ {o d}} Y _ {k} + Z _ {o d} \geq 1 \quad \forall o, d\tag{2}
$$

$$
Z _ {o d} \leq (1 - Y _ {k}) \quad \forall o, d, k \in N _ {o d}\tag{3}
$$

$$
Y _ {k} \geq 1 - \sum_ {j \in \Phi_ {k}} X _ {j} \quad \forall k\tag{4}
$$

$$
Y _ {k} \leq (1 - X _ {j}) \quad \forall k, j \in \Phi_ {k}\tag{5}
$$

$$
\sum_ {j} X _ {j} = p
$$

$$
X _ {j} = \{0, 1 \} \quad \forall j\tag{6}
$$

$$
Y _ {k} = \{0, 1 \} \quad \forall k\tag{7}
$$

$$
Z _ {o d} = \{0, 1 \} \quad \forall o, d
$$

The objective function (1) maximizes or minimizes the total flow disrupted. (To optimize connectivity, O–D flow $( f _ { o d } )$ can be ignored.) Constraints (2) and (3) indicate whether flow is possible between a given O–D pair based on the paths still available. Constraints (4) and (5) indicate whether given paths are still available based on the disrupted nodes. Constraint (6) specifies the number of nodes $( p )$ to be disrupted. Constraint (7) restricts the decision variables to be binary integers.

## Appendix B. Flow Disruption Index (FDI)

## Notation

i index of components (nodes or links) $o$ index of origins, entire set denoted Ω $d$ index of destinations, entire set denoted Λ $f _ { o d }$ flow observed between O–D $p$ number of components to remove $X _ { i }$ {1 if component i is disrupted {0 otherwise $Z _ { o d }$ {1 if no flow possible between O–D {0 otherwise

$$
D _ {i} = \frac {\text { Maximum } (p - 1 | X _ {i} = 1) \sum_ {o} \sum_ {d} f _ {o d} Z _ {o d}}{\text { Maximum } (p) \sum_ {o} \sum_ {d} f _ {o d} Z _ {o d}}\tag{1}
$$

Function (1) divides the worst-case disruption scenario involving a particular component (i) by the worst disruption scenario overall for p components disrupted.

## References

[1] Abilene, http://abilene.internet2.edu/ (2005).

[2] R. Albert, I. Albert, G.L. Nakarado, Structural vulnerability of the North American power grid, Physical Review E 69 (2) (2004).

[3] N. Altay, W.G. Green III, OR/MS research in disaster operations management, European Journal of Operational Research 175 (1) (2006).

[4] M. Amin, Toward self-healing infrastructure systems, Computer 33 (8) (2000).

[5] M. Amin, Scanning the technology: energy infrastructure defense systems, Proceedings of the IEEE 93 (5) (2005).

[6] M.O. Ball, B.L. Golden, R.V. Vohra, Finding the most vital arcs in a network, Operations Research Letters 8 (2) (1989)

[7] K. Bryson, H. Millar, A. Joseph, A. Mobolurin, Using formal MS/OR modeling to support disaster recovery planning, European Journal of Operational Research 141 (3) (2002).

[8] B.A. Carreras, V.E. Lynch, I. Dobson, D.E. Newman, Critical points and transitions in an electric power transmission model for cascading failure blackouts, Chaos 12 (4) (2002).

[9] C.J.E. Castle, P.A. Longley, A GIS-based spatial decision support system for emergency services: London's King's Cross St. Pancras underground station, in: P. van Oosterom, S. Zlatanova,

E.M. Fendel (Eds.), Geo-information for Disaster Management, Springer-Verlag, Berlin, 2005.

[10] R.L. Church, S.R. Loban, K. Lombard, An interface for exploring spatial alternatives for a corridor location problem, Computers & Geosciences 18 (8) (1992).

[11] S. Cosares, D.N. Deutsch, I. Saniee, O.J. Wasem, SONET toolkit: a decision support system for designing robust and costeffective fiber-optic networks, Interfaces 25 (1) (1995).

[12] M. Crozi, R. Galetto, A. Spalla, A web GIS for managing postearthquake emergencies, in: P. van Oosterom, S. Zlatanova, E.M. Fendel (Eds.), Geo-information for Disaster Management, Springer-Verlag, Berlin, 2005.

[13] R.J. Ellison, D.A. Fisher, R.C. Linger, H.F. Lipson, T.A. Longstaff, N.R. Mead, SURVIVABILITY: protecting your critical systems, IEEE Internet Computing 3 (6) (1999).

[14] A.S. Fotheringham, M.E. O'Kelly, Spatial Interaction Models: Formulations and Applications, Kluwer Academic Publishers, Boston, 1989.

[15] L.C. Freeman, A set of measures of centrality based on betweenness, Sociometry 40 (1) (1977).

[16] T. Fuller, S. Sarkar, A software package for optimizing connectivity in conservation planning, Environmental Modelling & Software 21 (5) (2006).

[17] P. Haggett, R.J. Chorley, Network Analysis in Geography, Edward Arnold (Publishers) Ltd., London, 1969.

[18] P. Holme, B.J. Kim, C.N. Yoon, S.K. Han, Attack vulnerability of complex networks, Physical Review E 65 (5) (2002).

[19] J.N. Hood, T. Olivas, C.B. Slocter, B. Howard, D.P. Albright, Vulnerability assessment through integrated transportation analysis, Transportation Research Record 1822 (2003).

[20] E. Israeli, R.K. Wood, Shortest-path network interdiction, Networks 40 (2) (2002).

[21] R. Kinney, P. Crucitti, R. Albert, V. Latora, Modeling cascading failures in the North American power grid, The European Physical Journal B 46 (1) (2005).

[22] Y. Leung, Intelligent Spatial Decision Support Systems, Springer-Verlag, New York, 1997.

[23] R.G. Little, Controlling cascading failure: understanding the vulnerabilities of interconnected infrastructures, Journal of Urban Technology 9 (1) (2002).

[24] K. Malik, A.K. Mittal, S.K. Gupta, The k most vital arcs in the shortest path problem, Operations Research Letters 8 (4) (1989).

[25] T.C. Matisziw, A.T. Murray, Modeling s–t path availability to support disaster vulnerability assessment of network infrastructure, Computers & Operations Research (in press) doi:10.1016/j. cor.2007.09.004.

[26] T.C. Matisziw, A.T. Murray, T.H. Grubesic, Exploring the vulnerability of network infrastructure to disruption. Submitted for review (submitted for publication).

[27] T.C. Matisziw, A.T. Murray, T.H. Grubesic, Bounding network interdiction vulnerability through cutset identification, in: A.T. Murray, T.H. Grubesic (Eds.), Critical Infrastructure: Reliability and Vulnerability, Springer, New York, 2007.

[28] A.T. Murray, T.C. Matisziw, T.H. Grubesic, Critical network infrastructure analysis: interdiction and system flow, Journal of Geographical Systems 9 (2) (2007).

[29] J. Ortuzar, L.G. Willumsen, Modelling Transport, John Wiley & Sons, New York, 2001.

[30] H.D. Ratliff, G.T. Sicilia, S.H. Lubore, Finding the n most vital links in flow networks, Management Science 21 (5) (1975).

[31] J. Salmeron, K. Wood, R. Baldick, Analysis of electric grid security under terrorist threat, IEEE Transactions on Power Systems 19 (2) (2004).

[32] M.P. Scaparra, R.L. Church, A bilevel mixed-integer program for critical infrastructure protection planning, Computers & Operations Research 35 (6) (2007).

[33] H.A. Simon, The New Science of Management Decision, Harper & Row, New York, 1960.

[34] S. Soni, H. Pirkul, Design of survivable networks with connectivity requirements, Telecommunication Systems 20 (1,2) (2002).

[35] E.J. Taaffe, H.L. Gauthier, M.E. O'Kelly, Geography of Transportation, Prentice-Hall, Inc., Upper Saddle River, New Jersey, 1996.

[36] O.Z. Tamin, L.G. Willumsen, Transport demand model estimation from traffic counts, Transportation 16 (1) (1989).

[37] O. Uran, R. Janssen, Why are spatial decision support systems not used? Some experiences from the Netherlands, Computers, Environment and Urban Systems 27 (5) (2003).

[38] K. van Zuilekom, M. van Maarseveen, M. Van der Doef, A decision support system for preventive evacuation of people, in: P. van Oosterom, S. Zlatanova, E.M. Fendel (Eds.), Geo-information for Disaster Management, Springer-Verlag, Berlin, 2005.

[39] H. Wei, A.T. Murray, T.C. Matisziw, An EM algorithm for inferring OD traffic matrix, Association of American Geographers Annual Meeting, Chicago, March 2006.

[40] T.J. Wilbanks, Energy systems and infrastructures, in: S.L. Cutter, D.B. Richardson, T.J. Wilbanks (Eds.), The Geographical Dimensions of Terrorism, Routledge, New York, 2003.

[41] A.G. Wilson, Inter-regional commodity flows: entropy maximizing approaches, Geographical Analysis 2 (3) (1970).

Diane Snediker was a graduate student in the Department of Geography and a research assistant in the Center for Urban and Regional Analysis at The Ohio State University when this research was carried out and this paper was written. She is now employed as a Geographer at the U. S. Census Bureau.

Alan Murray is Director, Center for Urban and Regional Analysis, and Professor, Department of Geography, at The Ohio State University. He obtained a B.S. in mathematical sciences, an M.A. in statistics and applied probability and a Ph.D. in geography, all from the University of California at Santa Barbara. He is the editor of Geographical Analysis. His research and teaching interests are in location modeling and analysis, geographic information science, urban/regional planning and development, optimization, and transportation. He has published on a range of technical and application oriented topics in journals such as the Papers in Regional Science, Annals of Regional Science, Journal of Regional Science, Operations Research, International Journal of Geographic Information Sciences, Geographical Analysis, Journal of Geographical Systems, Journal of Urban Planning and Development, European Journal of Operational Research, Computers and Operations Research, Transportation Research, and Urban Studies, among others.

Tim Matisziw received his Ph.D. from The Ohio State University in 2005. Dr. Matisziw is a Post-Doctoral Research Fellow of the Center for Urban and Regional Analysis at The Ohio State University. His current research addresses modeling issues in transportation, location science, and spatial optimization.
