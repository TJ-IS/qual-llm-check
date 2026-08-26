---
otero_id: 21589
otero_key: "HD3CV9TF"
title: "Support for mobile communications planning"
authors: "Hock Chuan Chan; Shiang Long Lee"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00038-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Support for mobile communications planning

Hock Chuan Chan <sup>)</sup>, Shiang Long Lee

School of Computing, National UniÕersity of Singapore, Lower Kent Ridge Road, Singapore 119260, Singapore

Received 30 November 1996; revised 30 October 1997; accepted 1 November 1997

## Abstract

Communications planners have to consider many factors when deciding how best to provide communications to communications users. For mobile situations, time is critical. Planning in such situations is becoming an increasingly difficult task, and manual methods of calculation and planning are rapidly becoming obsolete. The computerization of certain stages of the process of communications planning is one solution to the problem. The planning process is subdivided into separate functional areas. Each is supported with a module, and the modules are then integrated to form a complete communications planning system. The software produced helps to perform mechanical and repetitive tasks, do complex mathematical calculations and keep track of large amounts of information, which would put a strain on human memory. The vital decisions are always made by the user, who may have other non-technical factors not considered by the software. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Communications planner; DSS; Mobile communications; Network management

## 1. Introduction

The concepts of a mobile area communications system is introduced in Section 1.1. The subsequent subsection discusses the difficulties that planners face. The difficulties provide the motivating force for the end-users to develop a computerized support system for the planning processes. The details of the developed system as well as the field studies of the prototypes are described in the subsequent sections.

The system is of practical use in both mobile and more static situations where communications planning is required, for example, during cross-country expeditions, explorations, military troop and equipment movement, as well as mobile phone, paging and wireless computer network planning.

## 1.1. Mobile area communications system

An area communications system is a radio communications system that permits its users to communicate with each other as long as they are within the area of coverage of the system see Fig. 1 . They are Ž . distinct from point communications systems like the conventional static telephone system in that users do not have to be at one particular point e.g., theŽ location of the telephone in order to gain access to . the system.

The main body of an area communications system is composed of a network of interlinked communications centers or communications nodes. Once a user is linked to a node, he is connected to this network, and can communicate with any other user that is also connected, regardless of the distance between them. The communications centers in the network do the switching and act as relay stations and control stations. They receive transmissions from other elements in the network and retransmit them along the shortest path that will allow the transmission to reach its destination.

![](/api/attachments/HD3CV9TF/fulltext/images/1a7dc9fc34e76cc9f6f9990bf216c4458f593f1a48bf78d1d851b4ba0bc9d91d.jpg)  
Fig. 1. Area communications system.

Access into the network of communications centers is achieved by means of user centers, for large groups of users, or user stations, for smaller user groups. Occasionally, where direct links are not possible due to long distances and<sup>r</sup>or obstacles formed by terrain features, ad hoc stations may be used to link communications centers to communications centers or to user stations. These are pieces of communications equipment temporarily detached from the parent communications or user center in order to provide communications to another area.

User centers, user stations and ad hoc stations may displace and move from place to place to suit the needs of communications users. Once they are stationary, they may link back to the main body of the communications network in order to gain access to it. In addition, mobile users may gain access to the network by linking directly to communications centers, user centers or ad hoc stations. They do not need to be stationary to link back to the network, but can maintain communications even when on the move.

Multi-channel radios MCRs are used to linkŽ . centers to other centers, stations and ad hoc stations. They are radios that can operate on two frequencies: one to transmit and one to receive. They operate in the Ultra High Frequency UHF band. They allowŽ . for multiple channels between stations. In other words, many users can communicate at the same time. MCRs normally have directional antennae, so the radio signals tend to travel in a line instead of in all directions. MCR links may carry the signals for facilities like telephones and fax from user stations to user centers.

Single-channel radios SCRs are used to linkŽ . mobile users to communications centers and user centers. They use the same frequency for both transmission and reception. They operate in the Very High Frequency VHF band. They normally haveŽ . omni-directional antennae, so radio signals travel in all directions to form a roughly circular area of coverage.

An area communications system tends to be used in situations where a mobile communications system is required. The individual elements in the area communications network, such as the communications centers, the user centers, the stations and the ad hoc stations, are independent of each other and are capable of moving about, changing the network topology over time.

Area communications systems are thus very useful in situations where the places that are linked by the communications network change over time. For example, they can be used to link the oil wells of an oil extraction operation. As the oil in the wells are exhausted, they are abandoned, and as new sources of oil are discovered, oil rigs are set up at new places. An area communications system can change the configuration of its network to adapt to the new arrangement of oil wells. Area communications systems also have military applications. They may be used to provide communications during a battle for military units that are constantly on the move.

## 1.2. Communications planning

Communications planning is becoming an increasingly complicated task. Very often, planners find themselves dealing with large amounts of information, especially when doing planning for an area communications system, instead of for the simpler point to point communications system.

The growing complexity of radio systems means that planners have to possess a great deal of technical knowledge on communications hardware and their capabilities. A thorough understanding of frequency congestion in the transmission media is also required. Planners need to make decisions to optimally allocate communications resources with many critical constraints to satisfy the needs of communications users. They have to ensure that sufficient capacity is provided for future expansion and network redundancies are provided to ensure reliability. In the radio communications environment, planners must also contend with the requirement of ensuring lineof-sight communications in varying terrain.

In addition, area communications systems add an extra dimension of complexity to communications planning as the planner has to contend with changes in the configuration of the network in addition to all the other factors listed above. It is thus becoming increasingly difficult to depend on manual processes to plan and manage a communications network. Computerized support is essential.

## 1.3. ObjectiÕes of the support system

The main objective is to develop a complete decision support system 14 that may serve as a <sup>w</sup> <sup>x</sup> platform for planning a communications network. A complete system should contain all of the functions and procedures that would be involved in communications planning. These would include point-to-point radio wave propagation calculations, radio area coverage plots of a transmitter site, reliability analysis of large networks, allocation of communication resources, frequency assignment, etc. The system should ensure that these functions, which are essential to the development of a communications plan, can be comprehensively and extensively carried out.

As the system is meant for planning a communications network, performing the above analysis for individual, discrete links is insufficient. Especially in the areas of link reliability, resource allocation and frequency assignment, the characteristics and performance of a link will have an effect on the rest of the network.

Thus, planners cannot simply consider every individual link in isolation during the planning process. The implications of every link for the entire communications network must be taken into account.

This system aims to achieve the following: a toŽ . boost the confidence of the system planners as all critical planning considerations are covered. b ToŽ . assure the users that only the most reliable link is used to establish with its backbone system. c ToŽ . enable planners to develop a complete communications system in phases. It would allow the planners to dictate the timing for the establishment of communication centers to provide communication to users. Ž . d To enable planners to respond quickly to changes in a mobile environment and to cope with the fast pace at which systems may need to be moved and deployed.

The modules developed include the Radio Wave Propagation Module to assess the link quality between a transmission point and a receiving point, the Resource Management Module to keep track of the serviceability and usage of all communications equipment, the Network Reliability Assessment

Module to determine how robust a communications network is to the deletion of nodes and links, the Frequency Management Module to check whether the frequencies used in the communications network might interfere with each other at the network level, and the Report Generation Module to generate various reports and communications instructions. These modules were integrated into Telecommunications Planning Software TPS , which performs as a deci-Ž . sion support system for communications planners.

Current softwares for planning communications are reviewed in Section 2. The system components and the required technical details and literature are presented in Section 3. The development process and the field evaluations of the system are discussed in Section 4. Section 5 presents the conclusion.

## 2. Review of other communications planning systems

Off-the-shelf software to assist the communications planner is available from independent vendors. The kinds of software which would appear to be useful tend to fall into one of the following two categories: propagation calculation software, which analyzes the effect that terrain has on radio wave propagation, and network management processors, which allow the user to monitor a communications network. The review shows that these softwares lack many important functions needed for the communications planners. This provides the motivation for the design, development and evaluation of TPS.

The Computer Engineering of Microwave Systems CEMS software 2 developed by Norton Ž . <sup>w</sup> <sup>x</sup> Engineering is an example of propagation calculation software. It has several features useful for the communications planner. It provides computerized communication path calculations for different types of radio. It also provides features for radial relief plots to allow users to analyze the height of terrain and enables the user to check for inter-modulation interference among the frequencies he is using. An additional module allows the viewing of antenna transmitting patterns.

This software is valuable for point-to-point radio wave propagation calculation. It is also capable of producing coverage plots and checking for frequency interference between two points. It contains several features to help in the communications planning processes. However, the software is limited in certain ways. First and foremost, it is not a complete system. It does not monitor the allocation of communication resources nor assess the capacity of the system in terms of the number of communications links it is capable of supporting nor the redundancy of the system in terms of how vulnerable it is to link failure.

In addition, it does not provide the features to allow the planning of a communications network. Both the radio wave propagation calculation and interference detection portions of the software may only be done between two points at a time. It does not have the capacity to perform the calculations at the network level. Thus, this software is not a complete system for communications planning at the network level. It can only be used to help in certain portions of the planning process. Another commercially available software, the Terrain Analysis Package 15 , has features similar to that of the CEMS.<sup>w</sup> <sup>x</sup>

Network management processors NMPs 11 areŽ . <sup>w</sup> <sup>x</sup> also commercially available, and may be used for network monitoring as well as system planning. The planning function of the NMP enables communications planners to trace the movement of the various elements in the communications network. Computer graphics are used to illustrate the network.

Although NMPs are helpful in the planning of a network, they are not complete system planners, either. They do not provide features for calculating link or network reliability, detecting frequency interference or keeping track of equipment.

In addition, it requires a great deal of time and training in order to learn how to operate an NMP and NMPs have few on-line help facilities. Many decision-makers will be too busy for the lengthy training process required.

## 3. Telecommunications Planning Software TPS ( )

A problem-oriented, modular approach was adopted during the project. The areas where computers could be of greatest use to the communications planner were identified and a separate module was developed to tackle each problem. The design of the communication planner system is based on integration of the various decision support components to enhance the flexibility and efficiency of the decision-making process. This is similar to the approach adopted for the system in Ref. 1 . The<sup>w</sup> <sup>x</sup> decision-maker has the final say, as for the system in Ref. 4 . He has the flexibility of adjusting various<sup>w</sup> <sup>x</sup> locations, considering other factors that are not in the system. This section describes the modules that have been developed and lists the functions that they are capable of performing.

## 3.1. Radio waÕe propagation calculation

This module assesses the link quality between two points for both Ultra High Frequency UHF andŽ . Very High Frequency VHF radio links. It does so Ž . by assessing the shape of the terrain between the points, determining whether a Line-Of-Sight LOSŽ . path exists between them and calculating the relevant path losses, such as the Allowable Path Loss APL ,Ž . the Free Space Loss FSL and the Estimated PathŽ . Loss EPL . Path losses measure the reduction inŽ . strength and clarity of a transmitted signal due to factors like distance and terrain. From the path losses, the Fade Margin FM , a measure of how likely a Ž . transmitted signal will be correctly received, is obtained. The signal strength is calculated using the Boolington method 13 .<sup>w</sup> <sup>x</sup>

Careful consideration is given to the storage and retrieval of terrain data, as the data is potentially very large 10,12 . The approach adopted is to clas-<sup>w</sup> <sup>x</sup> sify terrains according to the degree of variations in heights. Flat terrains need sparse data storage, while hilly terrains require more intensive data. The module also includes a terrain display function for visual checking.

Signal strength is measured using a value known as the Fade Margin. It is obtained by calculating the Allowable Path Loss APL , which is the greatestŽ . reduction in signal strength that can be sustained before the signal from the transmitter can no longer be received with acceptable quality. Then, the Estimated Path Loss EPL is subtracted from APL. EPLŽ . is the sum of all path losses, which are the calculated reductions in signal strength due to the distance between the transmitter and receiver and the obstacles and reflecting points in the signal path, if any.

Distance is one factor that determines the signal strength. Logically, the further apart the two stations are, the weaker the signal will be. Signal strength will also decrease if there are obstacles between the two stations blocking the signal, and it may improve if there are reflecting points along the signal path. Reflecting points work by redirecting signals which would have gone elsewhere towards the receiver. The presence of obstacles and reflecting points depends on the terrain between the two stations.

In path profile calculation, the first step is to obtain the height of the terrain at regular intervals between the two stations. These heights are then used to determine if a LOS path exists between the two points. The height of the LOS path is determined at every point along the path. The height of the terrain at every point, corrected for the curvature of the earth, is compared with the height of the LOS path. If the height of the LOS path is higher than the terrain height at every point, a LOS path exists.

If the LOS path exists, the next step is to see if there are any reflecting points along the path. A rotational ellipsoid zone around the straight-line path between the two points defines the location of all the points where reflection can occur. This zone, called the first Fresnel Zone see Fig. 2 , can be determinedŽ . mathematically. The radius of the first Fresnel Zone at any point along the signal path may be calculated using the equation:

$$
R _ {\mathrm{f} 1} = 5 4 8 \cdot \sqrt {\left(d _ {1} d _ {2} / F D\right)}
$$

where $R _ { \mathrm { f 1 } } = \mathrm { f i r s t }$ Fresnel Zone radius in meters; $d _ { 1 } = \mathrm { d i s t a n c e }$ from point of interest to transmitter in kilometers; $d _ { 2 } = \mathrm { d i s t a n c e }$ from point of interest to receiver in kilometers; F <sup>s</sup> transmitter frequency in megahertz; D<sup>s</sup>total distance between the two stations in kilometers.

All the peaks—a high point between two lower points—along the signal path are determined. The radius of the first Fresnel Zone at every peak is calculated. If the peak is between the first Fresnel Zone and 0.6 of its radius, a reflecting point exists. If no reflecting points are found, EPL is calculated according to a model known as the Free Space Model, using the equation:

FSL<sup>s</sup>20 log 41.87 Ž .FD

![](/api/attachments/HD3CV9TF/fulltext/images/ef5915a8c90f97841db7f53e7c239df8abb62f007a059d09b0aa56244d55c394.jpg)  
Fig. 2. First Fresnel Zone.

where FSL<sup>s</sup>loss due to Free Space; F<sup>s</sup>transmitter frequency in megahertz; D<sup>s</sup>total distance between the two stations in kilometers.

If one or more reflecting points exist, it is calculated using the Plane Earth Model, using the equation:

$$
\mathrm{PEL} = 1 1 5. 1 + 4 0 \log D - 2 0 \log \left(H _ {\mathrm{t}} H _ {\mathrm{r}}\right)
$$

where PEL<sup>s</sup>loss due to Plane Earth; D<sup>s</sup>total distance between the two stations in kilometers; $H _ { \mathrm { t } }$ <sup>s</sup>transmitter antenna height in meters; H <sup>s</sup>receiver antenna height in meters.

If there are obstacles blocking the LOS path, there will be a loss of signal strength due to the diffraction around the obstacles. This loss of signal strength is known as Shadow Loss SL . In order to calculateŽ . the value of SL, two things need to be done.

First, the height and the location of the virtual obstacle must be obtained. The virtual obstacle is an imaginary obstacle that has the same effect on signal strength as all the real obstacles in the signal path. It is found by obtaining the intersection point of the lowest unblocked gradient at both the transmitting end and the receiving end of the signal path. The height of the virtual obstacle over the LOS path, H, and the distance from the virtual obstacle to the nearest end point either the transmitter or the re-Ž ceiver ,. $D _ { 1 }$ Ž . , is then calculated see Fig. 3 .

The next step is to determine if SL should be calculated using the Free Space Model or the Plane Earth Model. The Free Space Loss FSL is calcu-Ž . lated using the Free Space Model and the Plane Earth Loss PEL is calculated using the Plane EarthŽ . Model. Both are compared. If FSL<sup>)</sup>PEL, SL is calculated using the Free Space Model. Otherwise, it is calculated using the Plane Earth Model. The equations are:

$$
\begin{array}{l} \mathrm{SL} _ {\mathrm{FS}} = 1 9. 2 2 \log H - 9. 5 \log D _ {1} + 1 0 \log F - 4 1 \\ \mathrm{SL} _ {\mathrm{PE}} = 2 0. 3 \log H - 1 0 \log D _ {1} + 1 0 \log F - 4 0 \end{array}
$$

where SL <sub>FS PE</sub><sup>s</sup>Shadow Loss due to Free Space; SL <sup>s</sup>Shadow Loss due to Plane Earth; H<sup>s</sup>height of virtual obstacle over Line-Of-Sight path in meters; D <sup>s</sup>distance from virtual obstacle to nearest end point in kilometers; F <sup>s</sup> transmitter frequency in megahertz.

The value of EPL is now calculated from the values of FSL, PEL and SL. If FSL<sup>)</sup>PEL, then EPL<sup>s</sup>FSL<sup>q</sup>SLFS. If PEL<sup>)</sup>FSL<sup>q</sup>K, where K is a value that depends on the type and sensitivity of the radio used, then EPL<sup>s</sup>FSL<sup>q</sup>K<sup>q</sup>SLPE. Otherwise, EPL<sup>s</sup>PEL<sup>q</sup>SLPE. The value of APL is then calculated from the transmit power, the antenna gain, the RF cable loss and the equipment sensitivity. The FM value for the link is then obtained by subtracting the value of EPL from the value of APL.

![](/api/attachments/HD3CV9TF/fulltext/images/9ef6d62ff75e363c38c18cc1c20e15f46cef9c6a9bcba1466d61e3c3a46cf23a.jpg)  
Fig. 3. Calculation of virtual obstacle.

A useful output of this module is the coverage plot Fig. 4 , which shows which areas around aŽ . point are likely to have good links with it. This calculation may be done for both UHF and VHF communications.

## 3.2. Resource management

This module keeps track of the resources and equipment available, whether they are in good working condition and when they are freed from usage. It can also display the kind and number of resources available in the entire network at any one time in a user-friendly format, so that resource allocation becomes much simpler.

The most important function of the resource management module is to ensure that the communications elements have enough assets to support planned usage. It is too easy to get carried away during the planning stage and assign more links to a center than it is able to support. Ideally, the program will only provide information to help the user make a decision. It should not make the decision itself.

Also of importance is its ability to locate free assets. If a vital piece of equipment fails during the execution phase, available resources and their projected uses can be obtained, and a replacement found quickly.

The proper management of resources is essential for the production of a good communications plan. Different types of communications equipment have different capabilities, and should be used in different circumstances. For example, in an area communications system, single-channel radios are used to provide area coverage since their antennas are omni-directional, while multi-channel radios are used to link centers since they have directional antennas and may be used to transmit multiplexed signals.

In addition, equipment may break down and require replacements. In situations where resources are heavily constrained, it may be necessary to move equipment around from places where they are not being used to areas where they are urgently required. Some method of keeping track of the locations and usage of equipment would be required for such a function.

![](/api/attachments/HD3CV9TF/fulltext/images/683c43ff99d9190223ba92d1792070a07c03dc05af0870650cd3cbfb5bf9b41e.jpg)  
Fig. 4. Display of a coverage plot.

During the planning and execution of a communications plan, it is also necessary to keep track of the kinds of equipment available at all times. If, for example, it becomes necessary to set up a new link at a particular point in time, the number of resources available and the length of time they will be available must be known, so the required changes to the communications plan can be made.

## 3.3. Network reliability assessment

This module assesses the reliability of a network and calculates how robust it is to the deletion of links and communications centers. It can also identify the links that should be added between the various communications centers in order to improve the performance of the network. It is also able to display the reliability of the network over time, so that the timings when the network is especially vulnerable can be identified and corrective measures taken.

Many variables influence the performance characteristics of a communications network. These include: the network topology, the type of communication lines and terminal equipment, the transmission speed and capacity, routing procedures, communication control procedures and error control procedures.

The type of network topology is one of the most critical aspects in the optimization of a network. An ill-chosen topology will cause inefficiencies in a network that the other factors can do little to ameliorate. A good communications plan ought to have a network topology with a high degree of redundancy and survivability.

A high degree of redundancy means that there are a number of alternative routes that a transmission can take to get from its source to its destination. A high degree of redundancy is an advantage because means that if one link cannot be used because of faulty equipment, interference or because the link is busy, the transmission can arrive at its destination by another route.

A high degree of survivability, or reliability, means that the network is able to sustain the loss of one or more nodes. If all transmissions in the network have to pass through one particular node, the survivability of the network is low. If that node becomes faulty, or is somehow removed from the network, communications originating from one end of the network will be unable to reach destinations on the other end. Such a situation is, obviously, undesirable.

Thus, a good network topology is one with a high degree of both redundancy and reliability, for such a network is robust to the deletion of links and nodes, and transmissions sent through it are likely to reach their destinations in spite of any problems that may be encountered.

The topology calculation module provides algorithms to determine the reliability of a network and to suggest the addition of links between nodes that may improve the network reliability. The algorithms used in this module include modifications from Refs. <sup>w</sup> <sup>x</sup> 5,6 . The redundancy and reliability of a network may be measured using its node connectivity, which is the total number of nodes that can be removed from the network without causing a loss of connectivity. The basic algorithm involves calculating the number of node-disjoint paths between a source node, S, and a destination node, D. Node-disjoint paths are paths that have no nodes in common. If there are a total of N node-disjoint paths between S and D, then there are N paths between the two nodes that do not share any nodes. Thus, N nodes would have to be removed from the network in order to disconnect S and D. The node connectivity between them would therefore be N.

One feature of the system is that it enables the creation of a dynamic network. In other words, the topology of the network may be changed over time. As such, it may be useful to view how the reliability of the network changes over time in order to determine the times that the reliability is low and thus the times that it is vulnerable to the deletion of nodes.

It is easy to detect faults in, make changes to and improve a small network. However, when the number of nodes and links in a network increases, it becomes very difficult to determine the ‘best’ topology or even a ‘good’ topology by simple examination.

In addition, if the network under consideration is not static but is dynamically evolving and changing over time, the problem becomes even more complex. The Network Reliability Assessment Module can determine if a proposed communications network satisfies minimum requirements of reliability, and if it does not, it can make suggestions to improve the network in order to achieve the required level of reliability. The poor network with low reliability see Ž Fig. 5 can be made into an improved network see . Ž Fig. 6 by the addition of the links suggested by the . module.

## 3.4. Frequency management

This module allocates transmission and reception frequencies for the multi-channel radios in the communications network. It reads in the frequencies from a file and allocates them by block. It also checks the network to determine whether the frequencies used might interfere with each other at the network level. If the possibility of frequency interference is detected, the module lists the location and identity of the transmitting station and the receiving station and the type of interference.

![](/api/attachments/HD3CV9TF/fulltext/images/19392fbeec84251bdcff407a4f3eee65c2360f9bd7f16d712212c7f34e990f35.jpg)  
Fig. 5. An unreliable network.

![](/api/attachments/HD3CV9TF/fulltext/images/235e5c9b490d2aa3c629e20110a4788ca772af9b5634e9713a6fee7290378524.jpg)  
Fig. 6. An improved network.

The proper management of frequencies is very important in the development of a good communications plan, especially in situations where the constraints of terrain or other such considerations cause the nodes in the communications network to be clustered closely together, resulting in a highly congested electromagnetic spectrum.

In such situations, there may be significant areas in which the radio signals may overlap, even if directional antennae are used. During the planning stage, if the proper care is not taken in the selection of frequencies, the frequencies chosen may interfere with each other and cause problems that require on-site corrective measures.

Frequency checking may occur at two levels. It may occur at the node level, in which all the transmitting and receiving frequencies originating from and terminating at a communications center or user center are checked by a blocking method to ensure that they do not interfere with each other. It may also occur at the network level, in which every transmitting frequency is checked against all the receiving frequencies of every element to see if interference will occur.

Software that performs frequency checking at node level is commercially available. However, software that performs frequency checking at network level is not. The frequency management module was developed for just that function. It enables the user to check the communications plan to see if there are areas where the transmitted signals overlap receiver sites and whether the frequencies assigned are likely to interfere with each other. The list of sites that might receive interference is displayed.

The following types of interference may occur <sup>w</sup> <sup>x</sup> 7,16 :

Ž .a Harmonic Interference. This occurs when the frequencies selected obey the equation $f _ { \mathrm { r } } = n f _ { \mathrm { t } }$ where n<sup>s</sup>2, 3, . . .

Ž . b Image Interference. This occurs when the frequencies selected obey the equation $f _ { \mathrm { r } } \pm 1 = f _ { \mathrm { t } } \pm$ $2 f _ { \mathrm { i f } }$ where $f _ { \mathrm { i f } }$ is a constant that varies with the type of radio used.

Ž .c Inter-modulation. This occurs when the frequencies selected obey the equation $2 f _ { \mathrm { t } 1 } - f _ { \mathrm { t } 2 } = f _ { \mathrm { r } }$ $\pm c$ where c is a constant that varies with the type of radio used.

Ž . d Spurious Interference. This occurs when the

frequencies selected obey the equation $f _ { \mathrm { r } } \pm 0 . 5 =$ $( n f _ { \mathrm { t } } + ( m - 1 ) f _ { \mathrm { i f } } ) / m$ where n and m are integers. In addition, for multi-channel radios, the Tx–Rx separation on the same radio, the Tx–Rx separation on different radios and the Rx–Rx separation on different radios cannot be too close. The separation required varies with the radio used.

It is assumed that every radio set has associated with it a particular area, the interference zone, within which its transmissions may interfere with the reception of other radio sets. For radio sets with directional antennae, the area is simplified to be an isosceles triangle for this software. However, just because a radio set is within this area does not mean that the transmissions will definitely cause problems for it. First and foremost, the set might be the intended receiver of the transmission. Secondly, the frequencies used by the two sets might not interfere with each other. Interference will only occur if the two frequencies satisfy certain criteria. For example, if the two frequencies are too close together or are multiples of each other, interference is likely to occur.

In addition, since TPS is capable of handling dynamic networks, it includes a time check to exclude transmissions occurring at different times interfering with each other. For example, if radio set A establishes a link to radio set B from time period 1 to time period 10, and radio set B establishes a link to radio set C from time period 15 to time period 20, the two links should be unable to interfere with each other.

## 3.5. Report generation

This module generates the various reports and communication instructions, including: a Topology. Ž . The topology of the mobile network at any time, either graphical or textual. b Communications As-Ž . sets Deployment. The location, start time and end time of the deployment of every communications asset. c Station Affiliation. The locations at whichŽ . every user station has to deploy and the start and end time of its link with a center for a mobile user. dŽ . Task Allocation. The locations at which every communications center has to deploy, the start time and end time of its deployment and the links it is supposed to take up while deployed. e Link Occu- Ž .

pancy. The number of links that each center has to take up, at intervals of one or two time periods, for the entire network. f Link Status. The start timeŽ . and end time of every link, the Fade Margin and whether it is a Line-Of-Sight link, the locations and identities of the two elements involved, the frequencies used and the direction of transmission. g Com-Ž . munications System Instructions. The locations of the communications assets that are supposed to set up or tear down, arranged in chronological order.

## 4. Development and evaluation

The development process was initiated and maintained by an end-user, who was also the champion for the system. The development team consisted of three persons at any one time. The champion was permanent, while the other two members changed a few times over the full development process. They were temporary employees attached to the organization, and requested to work part-time on the system. All the members had considerable exposure to computers and programming, although they were not holding data processing positions. The system was developed for the personal computer laptops, and it could be easily carried for mobile planning. The modules were programmed in C and Pascal.

As noted in many studies, a champion is an important factor for the success of a system 8 .<sup>w</sup> <sup>x</sup> Similarly, the champion here was instrumental in ensuring the success of this system. He provided the continuity for the development process. As a communications planner himself, he was able to articulate the requirements and designs for the system. In addition, he was able to convince the other communications planners to test various modules of the system in actual planning operations as and when the modules were ready, as well as to test the fully integrated system.

Instead of solving the whole problem at once, the approach adopted was a step-wise progression combined with the employment of physically small and inexpensive microcomputer information processing capability. The system was developed with an initial capability, put in the user’s hands and enhanced in stages. It was through the application of this ‘use– learn–develop’ philosophy that the system was developed to assist planners in deterministic, probabilistic and inferential decision-making. The strong linkage to practice helped ensure a support system that meets the requirements of the planners.

Prototypes of the system at progressive stages of development were tested with actual communications planner in actual mobile situations. The planners were highly experienced with the traditional non-supported methods of planning. The use of the system led to time savings, better accuracy, better resource management, and better response to fast changing situations. The results, obtained from direct observation and open interviews, are summarized below. This evaluation approach is similar to the case study research method 17 , and the field study<sup>w</sup> <sup>x</sup> evaluation used in Ref. 3 .<sup>w</sup> <sup>x</sup>

## 4.1. Radio waÕe propagation module eÕaluation

The radio wave propagation calculation module produces great time savings as well as vast improvements in terms of precision, accuracy and neatness. Previously, a point-to-point radio wave propagation calculation would require 15 min to produce. The graph produced by such a calculation would only contain the obvious contour heights and would be subject to human errors of judgment and estimation.

Using the radio wave propagation calculation module on a 486 PC, a radio wave propagation calculation with a 200-m interval may be done within 1 s for distances of up to 40 km and within 2 s for distances of up to 80 km. This does not include the time required to key in the location of the transmitter and the receiver, but these locations may be expressed as a six- or seven-digit number, and would only take a proficient operator a few seconds to enter. The graph produced is also more accurate and detailed than a manually produced graph.

Previously, it required half a day to produce a coverage plot of a point at 15 degree intervals. Using the radio wave propagation calculation module, a planner may produce a coverage plot at 1 degree intervals in about 20 min. The coverage plot obtained is also more accurate and detailed than one obtained manually.

Many favorable comments on this module were received from users who found the use of graphics and the division of the coverage plot into areas of varying decibel levels to be especially useful.

## 4.2. Resource management module eÕaluation

Previously, many diagrams and charts were required to monitor the use and deployment of resources and equipment in the communications network. In addition, at least one planner had to be assigned the task of keeping track of the communications equipment. Even so, occasional mistakes would occur due to miscommunications, late or missing updates of equipment status and other human errors.

The resource management module automatically takes note of any changes in equipment status without the need for human supervision, thereby freeing planners for other tasks. Updates are done immediately, so that the most up-to-date picture of equipment status is available to communications planners at all times. Human errors are also minimized, resulting in greater accuracy. Thus, the resource management module results in manpower and time savings as well as a reduction in errors and inaccuracies for the communications planner.

## 4.3. Network reliability assessment module eÕaluation

The greater the complexity of the communications network, the more important is the network reliability assessment module. If network reliability assessment is not done, the network may be weak. A single unstable link may lead to entire sections of the network being cut off from each other and unable to communicate with the other parts of the network. If network reliability assessment is done manually, it becomes nearly impossible to calculate the reliability for six or more nodes.

Thus, the network reliability assessment module performs a very useful function. By enabling communications planners to determine whether a communications network meets minimum standards of reliability and, more importantly, enabling planner to improve the network if it does not, it gives planners and users the assurance that the network will not be easily disconnected.

## 4.4. Frequency management module eÕaluation

When the topology and connectivity of the communications network is available, it takes an hour to allocate frequencies manually, based on center level frequency checking. This type of frequency checking only ensures that the frequencies that converge on a single center do not interfere with each other. To manually check the frequencies for an entire network may require four to 6 h.

Thus, the frequency management module is a great time-saver for the communications planner. It enables the planner to perform the tasks of frequency allocation and frequency checking much faster than he would be able to manually.

## 4.5. Report generation module eÕaluation

Previously, it took three or four communications planners and one supervisor 2 h to prepare the reports and instructions once the communications plan was finalized. Using the report generation module, one planner can perform the same task in the time required to print a page on a printer.

The use of this module enables communications planners to produce the documentation required for the dissemination of communications instructions and important information quickly and with less manpower then is required using manual methods.

## 4.6. General eÕaluation

As a decision support system, one of the most important areas that should be evaluated is whether the program provides real-time user interface. In this area the system has succeeded. Most applications are done quickly, within 10 s or less. The longest waits are those for frequency checking and network reliability assessment, and even these are usually completed within 30 s to 1 min, for a reasonably sized network, on a 486 computer.

The system is also user-friendly. Commands are menu-driven and may be accessed by keyboard or by mouse, which makes it easy for the user to select the commands and options he wishes to use. The use of the mouse enhances the use of the menus by allowing the user to simply move the mouse to point to the option he wants and to select it by clicking on the mouse button.

By the use of computer graphics and simple language, results and information are presented to the user in a format that is easily understood. Thus, very little training is required in order to use the program for communications planning.

Users found the system to be easy to understand and use and useful in the task of communications planning. Previously, the process of planning required an average of 4 h and five men to complete. Using the system, it only takes two men half an hour to complete, thus saving time and manpower. The users’ perceptions are in agreement with the findings in Ref. 9 , which reported that DSS could enhance <sup>w</sup> <sup>x</sup> decision-making, particularly if the decision process followed a normative decision model. A user under pressure to plan fast can now follow the recommended procedures, instead of taking shortcuts and making wild guesses.

## 5. Conclusion

The objective to create a complete computerized decision support system for the communications planner to serve as a platform for planning a communications network has been achieved. The various functions of communications planning are supported. One of the guiding principles of the design of the system is that the computer should only be used as a tool to assist in decision-making and should not make decisions by itself. This is especially so when there is a high probability that other non-technical factors could be important. Thus, the various modules were developed to perform functions which may be handled by humans, but are quicker, more accurate and less subject to error when done by computer, like complex mathematical calculations, tedious and repetitive tasks and keeping track of large quantities of information. At no point is the user’s prerogative to make decisions taken from him.

One advantage of this system is its capacity to handle communications networks, including dynamic communications networks that change their topology over time. Frequency interference and reliability checks may be done at the network level, and the graphics-based interface enables the user to view the topology of the entire communications network as a whole during the planning process. It is also an interactive system. Most of its functions can be completed in less than 10 s. Thus, it enables planners to react quickly to changes that may arise during the planning stage.

The modules developed are by no means an exhaustive list of all the tasks that a communications planner must perform. However, his other tasks require an element of human expertise and experience that a computer is unable to provide. The modules cover the most critical aspects of communications planning that can be safely and easily delegated to the computer. It is thus a useful tool for the communications planner that can relieve him of many of the problems associated with his job.

The system is proof that a DSS for mobile communications planning is possible, and can be effective even for fast decisions. The development approach demonstrates a way for such a DSS to be designed and built, with continual user trial and feedback.

## References

<sup>w</sup> <sup>x</sup> 1 T. Alshemmeri, B. Alkloub, A. Pearman, Computer-aided decision-support system for water strategic-planning in Jordan, European Journal of Operational Research 102 3 1997Ž . Ž . 455–472.

<sup>w</sup> <sup>x</sup> 2 CEMS Users Manual, Norton Engineering, 1992.

<sup>w</sup> <sup>x</sup> 3 A. Clarke, B. Soufi, L. Vassie, J.s Tyrer, Field-evaluation of a prototype laser safety decision-support system, Interacting with Computers 7 4 1995 361–382.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 P.J. Densham, G. Rushton, Providing spatial decision-support for rural public-service facilities that require a minimum

workload, Environment and Planning B—Planning and Design 23 5 1996 553–574. Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 S. Even, Graph Algorithms, Pitman, London, 1979.

<sup>w</sup> <sup>x</sup> 6 L.R. Ford, D.R. Fulkerson, Flows in Networks, Princeton Univ. Press, NJ, 1962.

<sup>w</sup> <sup>x</sup> 7 S. Goldman, Frequency Analysis, Modulation and Noise, McGraw-Hill, New York, 1948.

<sup>w</sup> <sup>x</sup> 8 G. Hall, J. Rosenthal, J. Wade, How to Make Reengineering Really Work, Harvard Business Review, Nov–Dec, 1993.

<sup>w</sup> <sup>x</sup> 9 D.H. Hammond, T.D. Clark, S.J. Hartman, S.M. Crow, One more time—does a computer-based decision-support system improve managerial decisions, International Journal of Computer Applications in Technology 8 5–6 1995 290–300.Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 H.M. Hearnshaw, D.J. Unwin, Visualization in Geographical Information Systems, Wiley, New York, 1994.

<sup>w</sup> <sup>x</sup> 11 Network Management Processor User Manual, Siemens-Plessey, 1992.

<sup>w</sup> <sup>x</sup> 12 D.J. Peuquet, Introductory Readings in Geographic Information Systems, Taylor & Francis, New York, 1990.

<sup>w</sup> <sup>x</sup> 13 P. Rohan, Introduction to Electromagnetic Wave Propagation, Artech House, London, 1991.

<sup>w</sup> <sup>x</sup> 14 R.H. Sprague, E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

<sup>w</sup> <sup>x</sup> 15 Terrain Analysis Package Users Manual, SoftWright, 1992.

<sup>w</sup> <sup>x</sup> 16 D.R. White, A Handbook Series on Electromagnetic Interference and Compatibility, Don White Consultants, 1985.

<sup>w</sup> <sup>x</sup> 17 R.K. Yin, Case Study Research, Design and Methods, Sage Publications, USA, 1994.

Dr. H.C. Chan is a senior lecturer at the School of Computing, National University of Singapore. He has BA Hon and MAŽ . degrees from the University of Cambridge, UK, and a PhD in Management Information Systems from the University of British Columbia, Canada. He has taught courses in programming, database and information systems, and has published articles in various conferences and journals, including ICIS, HICSS, MISQ, JDM and IJHCS. Mr. S.L. Lee graduated from Nanyang Technological University, Singapore, with BEng Mechanical in 1990.Ž . He received his MEng Mechanical from Nanyang Technological Ž . University in 1993 and MSc in Computer and Information Sciences from National University of Singapore in 1996. His on-going works include management information systems and optimization programming.
