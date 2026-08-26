---
otero_id: 21213
otero_key: "TJBF3ZFY"
title: "A computer-based decision support system for vessel fleet scheduling—experience and future research"
authors: "Kjetil Fagerholt"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00193-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A computer-based decision support system for vessel fleet scheduling—experience and future research

Kjetil Fagerholt\*

MARINTEK and the Norwegian University of Science and Technology, P.O. Box 4125 Valentinlyst, N-7450 Trondheim, Norway

Accepted 30 September 2002

## Abstract

Most ocean shipping companies do the planning of fleet schedules manually based on their experience. Only a few use optimization-based decision support systems (DSS). This paper presents TurboRouter, a decision support system for vessel fleet scheduling, as well as some of the experience gathered from a research project to develop commercial software that is now used by several shipping companies. Perhaps the most important experience is that when designing such systems, the focus should be directed more to the interaction between the user and the system than the optimization algorithm, which has often been the case. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Decision support systems; Vessel scheduling; Optimization

## 1. Introduction

As in almost all business environments with dynamic markets, complex organizational structures and advanced technical systems information technology have become absolutely necessary to keep operations going. In a historical perspective, computer and communication systems are new technologies and have experienced, for the last few decades, rapid development. It is not very provocative to postulate that we have not yet seen the full potential of information technology. Probably, minor parts of all opportunities have been discovered and even less have been realized.

One area with obvious potential for improvement is the systems for vessel fleet scheduling. Ocean shipping is the major transportation mode of international trade. Each year, more than 5 billion tonnes of cargo are shipped by a large number of vessels and the trends indicate that this volume will increase in the future [9]. A ship involves a major capital investment, and its daily operating cost often amounts to several thousands of dollars. Proper planning of vessel fleet schedules may therefore give significant improvements in economic performance, which may be crucial for survival in an increasingly competitive market.

An important and complex challenge in vessel fleet scheduling is to optimally assign available cargoes to the vessels in the fleet, while satisfying a number of practical constraints. Typical constraints can be cargo time windows, vessel capacity, compatibility between ports and vessels due to draft and vessel length, just to mention a few. Today, shipping companies rarely use optimization-based decision support systems for the fleet scheduling. They still do this manually based on their experience, with a pen and a piece of paper and often a spreadsheet to visualize the schedule.

The need for proper fleet routing and scheduling together with the rapid development of computing power indicates that there is a potential for improvement by using optimization-based decision support systems (DSS). Even though there has been some research and software developments on the subject, the shipping industry has thus far lagged behind other sectors of the transport industry, such as trucking and airline applications. In Ref. [12], a bibliography containing 500 references on routing and scheduling problems is presented, whereas only a few of these papers deal with the routing of vessels. Considering the huge operating costs, the cost of mistakes and the complexity of the vessel fleet scheduling, we can only wonder why optimization-based DSS play virtually no role in the ocean shipping industry.

A discussion of the reasons for the low level of attention given to vessel routing and scheduling is found in Refs. [15,16]. One of the reasons mentioned is that the ocean shipping industry has a tradition for conservative thinking and is not usually open to new ideas. My experience after several years in this business confirms this. A statement that one often hears is ‘‘I have done this for 20 years, I do not need a computer’’. Another reason for the low attention on vessel routing and scheduling may be that prior to the microcomputer, routing and scheduling software were primarily batch algorithms operating on large mainframe computers. Such computers were usually not easily available for most shipping companies. In addition, these systems did not possess significant graphics and interactive capabilities. The users had difficulty in ‘seeing’ the solution and therefore, they could not alter the system-generated solution manually. For a solution to be implementable, it must be the user’s solution and not the computer’s solution [1,3].

It is usual to distinguish between three general modes of operation in shipping: liner, tramp and industrial [13]. Liners operate according to a published itinerary and schedule, similar to a bus line. Tramp vessels follow the available cargoes, like a taxicab. Often, a tramp shipping company engages in Contracts of Affreightment (a contract to carry specified quantities of cargo between specified ports within a specific time frame for an agreed upon payment per tonne). Typically, a tramp shipping company has a given amount of contract cargoes that they have committed themselves to carry while trying to utilize its fleet, such that they can maximize the profit from optional spot cargoes. In industrial shipping, the cargo owner also controls the vessel fleet. Industrial operators must ship all their cargoes, while minimizing the cost.

The majority of published work on ocean fleet scheduling has been on the theoretical and experimental levels with a focus on optimization algorithms. In Ref. [5], a real application of crude oil scheduling problem is considered. A major oil company controls several crude oil tankers of similar size and uses them to ship crude oil from the Middle East to Europe and North America. All cargoes are full shiploads. A priori, all feasible tanker schedules are generated. The problem is then formulated as a set-partitioning model, where the columns represent the schedules generated a priori. By solving this model, the schedule for each tanker is determined. An interactive optimization system for a bulk cargo ship-scheduling problem faced by the US Navy is presented in Ref. [10]. They use a similar solution approach as in Ref. [5]. Potential annual savings of up to US\$ 30 million are reported by using the optimization system over the manual system that was currently in place.

In Ref. [6], a software system developed for scheduling the US Coast Guard cutters is presented. The commitments to be fulfilled can result in the nonexistence of feasible schedules. Therefore, they introduce a relaxation of the requirements to obtain feasible schedules, where an under- or overachievement of a commitment is penalized. By generating a set of feasible cutter schedules a priori, the problem is solved as a mixed-integer-programming model. Two more recent contributions to the field are given in Refs. [2,11]. In Ref. [2], a DSS with a spreadsheet interface for scheduling liquid bulk products is described. Their method of solution is based on the one developed in Ref. [5]. They report that savings are achieved compared with manual planning. Ref. [11] presents a prototype decision support system for ship scheduling in industrial bulk trade. The solution method developed has also here similarities with the one used in Ref. [5].

The above references describe some of the few real applications reported in the literature. We have only given references for scheduling within the industrial and tramp shipping segments since these are the targets of the DSS presented in this paper. A more thorough review on published work for all segments that also includes theoretical papers can be found in Refs. [7,16].

This paper presents TurboRouter, a DSS for vessel fleet scheduling. While the above references describe systems and optimization algorithms designed for a specific scheduling problem, TurboRouter is designed to handle a much larger variety of problem structures, both within the tramp and the industrial shipping segment. The development of this system started as a research project in 1996 and has now become a successful commercial software that has been implemented and used by several shipping companies. In addition, to present the DSS, the aim of this paper is to describe some of the experience gathered during the research project and to discuss some reasonable directions for future development.

The remainder of this paper is organized as follows. In Section 2, there is a short background about how the fleet scheduling is done in most shipping companies. Some experience gathered in the initial phase of the project is also presented. Section 3 describes the initial design of the DSS, while Section 4 presents the fleet scheduling functions in the DSS and how they work. Section 5 gives conclusions and some directions for future research and development for the DSS.

## 2. Overview of vessel fleet scheduling

This section provides a brief overview of vessel fleet scheduling. Section 2.1 gives a background with an example of how the planning of fleet schedules is often done in the shipping companies. Section 2.2 describes some of the initial experience gathered from working together with shipping companies.

## 2.1. Background

After working with different shipping companies on several projects, it was clear that the planning of fleet schedules was done with little or no use of advanced computer-based DSS. The only computerbased DSS that was commonly used was a software tool that produces only single vessel—single journey cost and income statements. However, the planning of schedules for the whole fleet was done manually based on the planners’ experience, using a pen and a piece of paper or perhaps a spreadsheet to visualize the schedule. A typical sheet used for visualizing the fleet scheduling problem to the planner is shown in Fig. 1. The sheet is divided into geographical regions. In the upper part, we see the most important information for the cargoes to be considered in the given planning period. They are positioned in the geographical regions according to their port of loading. In the lower part of Fig. 1, we see the open positions and dates of the different vessel, i.e. when and where they are ready for new tasks. It should be emphasized that the sheet in Fig. 1 only serves as an example, and only shows some of the geographical regions, cargoes and vessels to be considered by the shipping company using the sheet.

<table><tr><td>Norway</td><td>Continent</td><td>Baltic</td><td>U.K.</td></tr><tr><td>Stavanger/Rotterdam3500 ts wheat 14-16Bergen/Antwerp3-4000 ts split 15-16Herøya/Sluiskil4000 ts ferts 16-18</td><td>Antwerp/Oslo3500 ts sand 14-16Flushing/Herøya3500 ts nitr. 12-14Rotterdam/Porsgrunn3500 ts coal 12-16</td><td>Muuga/Chatham3100 ts steel 12-16</td><td>Carston/Rafnes3500 ts salt 13-16</td></tr><tr><td>Haugo - Karmøy 15Garmo - Porsgrunn 15Lesnes - Ålvik 14</td><td>Lurnes - Am.dam 11Jambo-Ghent 15</td><td>Haslo - Stettin 13Barco - Tallinn 17</td><td></td></tr></table>

Fig. 1. Example of sheet used for fleet scheduling.

The planner’s challenge is to make an optimal assignment of cargoes to vessels, i.e. optimally ‘connect’ the different cargoes to the available vessels in Fig. 1. However, by using the sheet in Fig. 1, the planner still has to manually ensure that a given assignment is feasible with respect to all constraints, such as the cargo time windows.

## 2.2. Initial experiences

In 1996, marine technology researchers in Trondheim started a research project aimed at developing TurboRouter, a computer-based DSS for improving fleet scheduling, for the shipping companies. The idea was to develop optimization algorithms that could solve these problems for the planners. Since we needed a thorough insight and understanding of the fleet scheduling problems the shipping industry faced, we established a project group, which included a few shipping companies and us.

However, the shipping companies were extremely skeptical to such systems in general, and to optimizing fleet scheduling in particular. The schedule planners usually have a very good reputation within the shipping companies and some were afraid that management and their coworkers would get too much insight into their jobs, further reducing their standing. Some schedule planners were even afraid of becoming redundant. They also argued that it was impossible to model all aspects needed to optimize fleet scheduling.

We soon realized that it was hard to model all necessary constraints and information. An example of a constraint that can be difficult to model in optimization software is the compatibility between vessel and port. There may be cases where a specific vessel cannot usually enter a given port due to draft restrictions. However, if the vessel is not fully loaded, it may still be possible at high tide. This type of constraint will be influenced by the vessel’s draft (which again is influenced by the cargo quantity onboard) and the port’s draft restriction (which again is influenced by the tidal factors).

Another example of aspects or constraints that are hard to model is port opening hours. Sometimes the different cargo owners, who are the shipping company’s customers, may have different agreements with certain ports regarding opening hours. It may also be possible to negotiate extended opening hours in some situations, though at a given cost.

Even though it could be possible to model these aspects, it would require too much user input, and the planners would not be confident with such a system. The schedule planners insisted on a system with a high degree of user interaction with possibilities to evaluate a large number of scheduling alternatives, and where the abovementioned constraints could be judged by an experienced planner from situation to situation. Therefore, we found it necessary to change the focus of the design of the fleet scheduling tool from optimization to decision support. The DSS should help the planners in quickly evaluating a number of scenarios, while the planner, based on his or her experience, should evaluate intricate constraints like the one mentioned above and finally decide on the fleet schedule.

Since the ocean shipping industry can be regarded as relatively conservative and not very open to new ideas, we emphasized the development of the DSS in small steps and getting acceptance from the shipping companies after each step. There have probably been several failures in designing vessel fleet scheduling systems because of low user acceptance. Therefore, it was important to understand the environment of the decision-makers and the type of support they need in order to make effective decisions.

In this way, the initial phase of the project was one of learning both for us and for the shipping companies. We learned a lot about the ocean shipping industry, as well as the necessary requirements for such a DSS, while the shipping companies learned a new way of thinking and planning step by step.

## 3. Initial design of the DSS

This section presents the design of some of the components in the DSS that were made in the initial phase of the research project. Section 3.1 outlines the user interface that is based on electronic sea charts in order to visualize planning information, while Section 3.2 states the importance of good distance calculation routines and describes how this is solved in the DSS.

Section 3.3 presents the schedule calculator, which turned out to be a successful tool for manual planning.

## 3.1. Graphical user interface

Based on the above experience, we focused on developing a user-friendly and intuitive graphical user interface for Windows. The DSS was written in Visual C++ version 6.0, which is suitable for designing Windows applications. In the beginning, the DSS was, in reality, only an information system where information about vessels in the fleet and ports was gathered. However, we soon realized that traditional large-scale maps with geographical representation of port locations, for instance, would be a useful visual aid in order to achieve user acceptance. Therefore, we based our DSS on electronic sea charts (C-MAP). We also made an application for receiving satellite positions from the vessels, so that we could visualize these in the charts. Then, the users got an instant overview of the vessel positions almost in real time, which may be an important prerequisite for proper fleet scheduling. Fig. 2 shows the main screen window of the DSS. The red circles represent the ports entered into the system, while the other symbols correspond to vessel positions. By clicking on such a symbol, the user will see the details for the given position report (see Fig. 2).

It should be noted that such position reports can now be regarded as an off-the-shelf product, and can, for instance, be subscribed for on the Internet. However, in 1996 this was not the case, for the shipping companies, this was quite new and it was regarded as a simple but valuable tool. It was also an efficient platform for presenting further ideas to the shipping companies.

![](/api/attachments/TJBF3ZFY/fulltext/images/844477e64bc38b9d2d38409eb8ef69b10fe0beac452f6869191d93d181eb2701.jpg)  
Fig. 2. Main window of TurboRouter.

## 3.2. Distance calculations

Next, we learned that tables of port-to-port distances are crucial for proper fleet scheduling. The existing distance tables that could be found in different software were static. This means that if you had to enter a new port into the system, you had to manually find and enter the distances from that port to all other ports in the system to maintain a complete distance table. This could be extremely time-consuming. Therefore, we developed an algorithm for automatically calculating port-to-port distances. The algorithm was based on modeling the land contours by nodes and arcs that represented obstacles or infeasible sailing areas. The algorithm would then calculate the shortest (great circle) distance between any two ports without crossing the land contours. The distance calculation algorithm is described in detail in Ref. [8]. By using this algorithm, the user could enter a new port together with its position and the system would calculate all distances needed. This algorithm made it easy to maintain the distance tables in a flexible way.

The distance algorithm was also used for calculating the distance from a given vessel position to any destination port. Based on that distance and the specified service speed for the vessel, an Estimated Time of Arrival (ETA) for the given port could easily be calculated (see Fig. 2). Then, the fleet schedule planners could evaluate whether the vessel was on time according to its schedule, and delays could be revealed at a much earlier stage than before. They could also use the new function for evaluating whether a vessel at sea could reach a given loading port within a specified time window for a particular cargo.

## 3.3. Manual planning

After testing and using the new function for a while, the shipping companies became confident that the calculated distances were well within the requirements. One of them suggested making the distance calculation also work for a via-port. Then, the idea of the schedule calculator arose. The schedule calculator is a manual planning tool where the user can easily enter a sequence of port calls together with planned time spent in each port for a given vessel. Then, the DSS calculates the sailing distance between the different ports, and hence the sailing time. This again will give the arrival and departure times for each port call.

The planner can use the schedule calculator to test alternative schedules and see if the vessel can reach the different port calls within the specified time windows. The schedule calculator is shown in Fig. 3. We see that there is a Status column, where two different statuses are shown: P for Planned and A for Actual. When the vessel actually departs from a given port, the user will change the status to Actual and enter the actual departure time. If the vessel has experienced a delay in that port, the actual departure time will be later than the planned. By entering the new and actual time for departure, the arrival and departure times for all subsequent port calls will automatically be updated. Then the user immediately sees the consequences of a delay.

![](/api/attachments/TJBF3ZFY/fulltext/images/4d77ac810927ede2b527ab82b6bb37e237e69c1b21e628be5f0764213d80978f.jpg)  
Fig. 3. Schedule calculator in TurboRouter.

The schedule calculator was later extended so that it could calculate fuel consumption for the vessels based on the sailing time and time spent in the ports. Then, the operations department in the shipping company could also use the schedule calculator to plan the purchasing of fuel, i.e. where to fuel bunker and how much. These are important decisions as the fuel price varies a lot between the different ports, and the less fuel onboard, the more cargo the vessel can take.

The schedule calculator turned out to be a success for the shipping company involved in the initial development. Even the most skeptical was happy with the new tool and used it for planning fleet schedules.

## 4. Vessel fleet scheduling

The success of the schedule calculator gave new growth to our goal at the beginning of the project: Develop optimization algorithms for vessel fleet scheduling, i.e. find an optimal assignment of avail able cargoes to vessels in the fleet. The vessel fleet scheduling algorithm that was developed is presented in Section 4.1. Based on the experience from the initial phase of the project, we realized the importance of a good user interface where the user could interact with the optimization algorithm and overrule it if necessary. Therefore, we put a lot of effort in the design of the user interface to facilitate an intuitive user interaction, which is described in Section 4.2, while Section 4.3 presents some ways of visualizing the vessel fleet schedule. For most shipping companies, it is important to interact with the market, for instance, by evaluating spot cargoes. This is discussed in Section 4.4, while Section 4.5 describes how the DSS can be used for more strategic planning issues.

4.1. Optimization routine for the vessel fleet scheduling

When developing an optimization routine for the vessel fleet scheduling, there are a number of aims that may be conflicting, such as:

– Fast solutions/quick response times

– Good solution quality (near the optimal solution)

– Flexibility in modeling real-life constraints

– Allowing interaction with the users.

The first two objectives are clearly conflicting. An ‘exact’ solution approach gives a theoretically optimal solution to the problem. However, this usually means sacrificing quick response times. On the contrary, simple heuristics may often give solutions that are not optimal but take little time. Therefore, there is often a trade-off between speed and solution quality when developing algorithms. This has also been the case for the scheduling algorithm in the DSS. In addition, the algorithm should be flexible so that complex real life constraints and considerations can be modeled. However, in vessel fleet scheduling, there is always some real-life complexities that cannot be modeled, which the user still wants to consider in the planning. Therefore, the scheduling algorithm should also allow for a great degree of user interaction.

To meet these different objectives, we have developed an optimization routine consisting of two different heuristic algorithms. First is the insertion heuristic algorithm, where the cargoes are processed sequentially, inserting one at a time into the work schedule of a vessel until all cargoes are processed. Second, a hybrid local search algorithm will improve any initial solution. The different neighborhoods or movement types that are defined are partly based on the movements defined in Refs. [14,17]. More details of the vessel fleet scheduling routine implemented in the DSS are presented in Ref. [4].

In summary, the optimization routine developed for the vessel fleet scheduling can accommodate the following:

Optimize with respect to financial result (net daily) or with respect to fleet capacity utilization

Cargo time windows

– Vessel capacities

– Compatibility between vessels and loading/discharging ports

– Compatibility between vessel equipment/certificates and products to be shipped

Parcel cargoes or full shiploads

– Split cargoes (the cargoes that can be divided into several cargoes to be shipped by different vessels)

– User-specified planning period

– Multiple products

– Combination of spot and contract cargoes – Inclusion/exclusion of time charter vessels.

In addition, the user has the possibility to enter soft sequencing constraints. Such constraints may, for instance, put restrictions on the sequence of products taken in a given vessel tank. This type of constraint is rather complex and there are always a number of exceptions to the rules. Therefore, these constraints are modeled as soft, in the sense that the user will only get a warning when such a constraint is violated, and it is up to him or her to consider if it really is a problem or not.

## 4.2. User interaction

When developing the function regarding the assignment of cargoes to vessels in the fleet, and hence the fleet scheduling, it was important that the user interface allowed for a high degree of user interaction. In addition to the optimization algorithm, which should only calculate a suggestion for fleet schedules, the user should be able to easily overrule and alter the suggestion from the optimization algorithm. It should also be possible to use the cargo assignment function completely as a manual tool. The planner should be able to manually assign cargoes to vessels, and the DSS should calculate whether the given assignment is feasible with respect to all modeled constraints and the economic consequences of the given assignments.

We developed a user interface as shown in Fig. 4 for the cargo assignment function. The rows in the user interface represent available cargoes to be assigned to vessels, while the first columns show some information for the cargoes in order to enable the planner to recognize the different cargoes. The information that is shown for each cargo can be user-specified. The last columns represent the available vessels in the fleet, i.e. the vessels to which the cargoes can be assigned. It should be emphasized that Fig. 4 represents only a small, artificial planning problem, and serves only for demonstration purposes.

The cells in the spreadsheet-like user interface in Fig. 4 have different colours:

The grey cells represent physical constraints entered into the system, restricting a given cargo to be assigned to a specific vessel. Such constraints can, for instance, be draft restrictions in loading or discharging ports, or that the particular cargo quantity is too large compared with the given vessel capacity. By holding the cursor over the cell, the reason for the constraint will be displayed.

Red indicates timing constraints due to cargo time windows.

![](/api/attachments/TJBF3ZFY/fulltext/images/19d3808dd060ae6e665bfb3fbcfa102ed5dc7a248bd61ee461a11729a4e64c6a.jpg)  
Fig. 4. User interface for planning of fleet schedules.

Green represents assignments of cargoes to vessels. For example in Fig. 4, cargo 1 is assigned to the vessel Iver Exact. By holding the cursor over a green cell, the user will see the arrival and departure times at the corresponding loading and discharging ports. White represents potential assignments that are feasible both with respect to physical and timing constraints.

Fig. 4 also shows an example of the soft sequencing constraints, described in the last section. We see that cargo 5 that is assigned to the vessel ‘Iver Libra has a ‘W’ displayed in the cell. This indicates a warning due to the sequencing constraints, and if the user holds the cursor over the cell, more details about the warning will appear.

The planning of vessel fleet schedules can be performed in different ways. The user can manually double-click in any white cell, and it will become green to indicate that the given cargo is now assigned to the specific vessel. The DSS will then automatically calculate the consequences of the given assignment, such as the given assignment’s impact on the financial result, both for the whole fleet and for the single vessel. By assigning a cargo, the DSS simultaneously calculates the underlying schedule for the vessel, i.e. it calculates where in the vessel’s sequence of port calls it is optimal to insert the two new calls (loading and discharging). This may also mean that when assigning a particular cargo to a given vessel, other cargoes may become infeasible for the given vessel due to the timing constraints. Then, they will turn up red in the user interface as shown in Fig. 4.

In the above way, the DSS can be used as a completely manual planning tool, where the system only calculates the consequences of different ‘what-if queries regarding the assignment of cargoes to vessels. Another way of planning the fleet scheduling is to activate the optimization algorithm. Then the DSS will suggest an optimal or near-optimal fleet schedule (i.e. the fleet schedule giving the best financial results for the whole fleet). There is also a semiautomatic planning function. If selected, it will activate the insertion algorithm described in Section 4.1 and consider the first unassigned cargo in the list. This cargo will be assigned to the vessel that gives the best impact on the financial result (or the capacity utilization) for the whole fleet.

As mentioned before, there are a lot of requirements that are hard to model that will influence the planner’s choice of fleet schedule. Even though the optimization algorithm gives the best solution with respect to financial results for the whole fleet, there may be a reason for the planner selecting another schedule. Therefore, the planner can manually change the solution suggested by the algorithm, just by double-clicking the white/green cells to assign/deassign. In this way, the planner can easily work with a large number of alternative solutions in the user interface shown in Fig. 4 in order to select the solution he or she feels is the best. The planner can also manually fix particular assignments of cargoes to vessels and let the optimization algorithm suggest optimal assignments for the remaining cargoes.

By using these new functions for assigning cargoes to the vessels in the fleet, the planners were able to test a large number of schedule alternatives in a short time. Before they had to make a lot of manual calculations that were very time-consuming. For instance, only to test whether a vessel is able to put a new cargo into the vessel’s work schedule, a large number of calculations regarding sailing times and then tests of port arrival times against cargo time windows have to be performed. It is not hard to imagine that due to this time-consuming manual scheduling, the planners were not able to examine all interesting alternatives, thus often missing the optimal one.

## 4.3. Visualization of the vessel fleet schedule

The planning interface (Fig. 4) only gives limited schedule information, especially when it comes to visualizing the time and capacity utilization of the fleet. When the user decides on a given assignment of cargoes to vessels, the underlying schedule details can be viewed in the schedule calculator described in Section 3.3. However, this dialogue only shows the schedule for one vessel at a time. Therefore, we have also developed a number of other dialogues for visualizing the vessel fleet schedule.

In Fig. 5, we see the Fleet schedule list, where the planned port calls for all vessels are shown on their arrival dates. The fleet schedule list corresponds to a spreadsheet, one of which the shipping companies used to visualize the schedule. Therefore, they were familiar with this way of viewing the schedule, which was important in order to get acceptance. We have also made it possible for the user to view added information for each port call, such as the arrival and departure times and information about the cargo to be loaded/discharged in the ports.

<table><tr><td>Week</td><td>Date</td><td>Voy</td><td>Isarstern</td><td>Voy</td><td>Iver_Gemini</td><td>Voy</td><td>Iver_Libra</td><td>Voy</td><td>Iver_Exact</td></tr><tr><td></td><td>1-Nov Thu</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>2-Nov Fri</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>JOSE</td></tr><tr><td></td><td>3-Nov Sat</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>L 1 = MTBE</td></tr><tr><td></td><td>4-Nov Sun</td><td></td><td></td><td></td><td></td><td></td><td>JOSE</td><td></td><td></td></tr><tr><td>45</td><td>5-Nov Mon</td><td></td><td></td><td></td><td></td><td></td><td>JOSE</td><td></td><td></td></tr><tr><td></td><td>6-Nov Tue</td><td></td><td></td><td></td><td></td><td></td><td>L 6 = MTBE</td><td></td><td></td></tr><tr><td></td><td>7-Nov Wed</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>8-Nov Thu</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>9-Nov Fri</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>WILMINGTON (USA-NC)</td></tr><tr><td></td><td>10-Nov Sat</td><td></td><td>JOSE</td><td></td><td></td><td></td><td></td><td></td><td>D 1</td></tr><tr><td></td><td>11-Nov Sun</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>46</td><td>12-Nov Mon</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>13-Nov Tue</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>14-Nov Wed</td><td></td><td></td><td></td><td>ROTTERDAM</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>15-Nov Thu</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>16-Nov Fri</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>JOSE</td></tr><tr><td></td><td>17-Nov Sat</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>L 2 = MTBE</td></tr><tr><td></td><td>18-Nov Sun</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>47</td><td>19-Nov Mon</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>20-Nov Tue</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>21-Nov Wed</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>22-Nov Thu</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>23-Nov Fri</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>24-Nov Sat</td><td></td><td></td><td></td><td></td><td></td><td>GALVESTON</td><td></td><td>GALVESTON</td></tr><tr><td></td><td>25-Nov Sun</td><td></td><td></td><td></td><td></td><td></td><td>D 6</td><td></td><td>L 4 = Methanol</td></tr></table>

Fig. 5. Fleet schedule list.

Other ‘views’ that have been developed for the planner to really understand and evaluate the fleet schedule include:

– Gantt diagrams, where the timing aspect is visualized. By using this view, the user can easily see vessel idle time in the plan.

– Graphs showing the capacity utilization as a function of time, both for each vessel and for the whole fleet.

The schedules can also be viewed geographically in the sea charts.

## 4.4. Interacting with the market

In industrial shipping, where the cargo owner also controls the fleet, the objective is to ship all cargoes with a given fleet at a minimum cost. However, in tramp shipping, the shipping company must, in addition to a given set of contract cargoes, also consider whether to ship various cargoes from the spot market or not. Therefore, in the planning of fleet schedules in tramp shipping, the planner not only has to decide an optimal assignment of cargoes to available vessels, but also decide which spot cargoes to ship.

In the DSS, it is possible to indicate whether a cargo is a contract cargo (and hence, a commitment) or a spot cargo not yet in contract. The optimization algorithm will then first try to assign the committed cargoes, and then try to assign the spot cargoes that give the highest positive impact on the financial result for the fleet. When this is combined with manual planning as described in Section 4.2, the planner can use the cargo assignment function in the DSS to decide an optimal fleet schedule, including the decision about which spot cargoes to ship or not.

In the ocean shipping industry, it is also usual to relet cargoes, i.e. allow a rival shipping company ship that cargo at a price to be agreed upon. This can also easily be modeled such that the DSS also can be a tool for evaluating these issues.

## 4.5. Strategic planning

The DSS has also been applied for more strategic issues. Typical strategic issues where the DSS can be used are on tonnage/fleet and cargo contract evaluations. One of the shipping companies that is now using the DSS, used the system for evaluating how their existing fleet could handle a new potential Contract of Affreightment and what financial contribution the new contract would give.

It is also easy to add one or several new vessels to the existing fleet to evaluate the consequences. The DSS has also been used by another shipping company for evaluating the potential improvements by merging two competing shipping companies. First, the fleet and cargoes for a given period were modeled for two shipping companies separately, and simulations were run to see how the two fleets could handle their cargoes and what the financial results would be. Then, the same period was modeled as if the two fleets were merged and it was all run in one operation. The shipping company found by using the DSS that by merging the two fleets (and its cargo contracts) they could run the whole operation at much less cost.

## 5. Concluding remarks and future research

Most shipping companies do the planning of fleet schedules manually based on their experience. Very few use optimization-based decision support systems. There has also been little work on this subject, and the majority of the published work on vessel fleet scheduling has been on the theoretical and experimental level with a focus on optimization algorithms. Few real applications have been reported, especially within the tramp-shipping segment.

This paper presents TurboRouter, a decision support system (DSS) for vessel fleet scheduling in the tramp and industrial shipping segment. To the author’s knowledge, this is the only DSS for vessel fleet scheduling presented in the literature handling all the different problem features described in Section 4.1, as well as facilitating a good interaction between the user and the system.

In addition, to present the DSS, a main goal of the paper has been to give a treatment to the ‘human factor’ involved in the development of a new type of application to be used in the ocean shipping industry. The development of this system started as a research project in 1996 and has now become a successful commercial software that has been implemented and used by several shipping companies. In this respect, the paper may contribute in a more general way, as I believe these discussions and processes will be valid and interesting in the development of any application in a mature industry.

The need for involvement and participation of the potential users was recognized right from the beginning. The process from the initial phase of the research project and up to now has been a learning process, both for the shipping companies involved and for us. We have learned a lot about the ocean shipping industry in general, and about the requirements for a DSS for fleet scheduling in particular. For instance, the need for a user interface facilitating a good interaction between the planner and the DSS was an important lesson that was learned. On the other hand, the shipping companies have gained new insight and ideas on how to improve the fleet scheduling. In the beginning, several of the planners were skeptical even to the distances calculated by the DSS, which were often double-checked before use in calculations. Now, they accept the distances without questions. Even though some still need to be convinced about the practical use of the optimization-based scheduling function, most are now beginning to see the improvement potential of using the system. During the project period, the shipping companies have grown from being extremely skeptical about optimization-based DSS for the fleet scheduling to see the improvement potential of using such systems.

In general, DSS benefits are often difficult to measure. However, it is sure that the shipping companies that have implemented the DSS have also experienced significant improvements in fleet scheduling. For example, one shipping company, engaged in the tramp-shipping segment, used the DSS during the first time after implementation together with their manual fleet scheduling system. The company found that by comparing it with the manual system, they were able to improve the fleet utilization so that they could ship two additional spot cargoes over a period of a few weeks. This represented a significant improvement on the bottom line for the shipping company. TurboRouter users have also reported that the time spent on schedule planning has been cut significantly, thus freeing the schedulers for other creative tasks.

The DSS has also been used for more strategic planning issues, such as the evaluation of fleet size and composition and cargo contracts. For example, one shipping company used the system for evaluating a new potential cargo contract for a cargo owner. The company used the DSS to demonstrate to their potential new customer that they could handle the new contract with their existing fleet. In that particular contract negotiation, the cargo owner stated the point that the shipping company should have a good fleet scheduling tool in order to get the contract.

To summarize, TurboRouter includes the characteristics of an effective DSS from the generic DSS framework described in Ref. [18]:

It supports, but does not replace the decisionmaker.

– It supports semi-structured decisions, where parts of the analysis can be calculated by the computer, but where the decision-maker’s insight, experience and judgement are needed to control the process.

– It combines modeling techniques with database and presentation techniques.

– It emphasizes ease of use, user friendliness, user control, flexibility and adaptability.

During the development from a research project in 1996 to a commercial software, we have experienced that integration with other systems is very important. Information should only be typed once. For instance, data about vessels, ports and cargoes most often also exists in the shipping company’s administrative systems. Therefore, the DSS should be integrated with these administrative systems in order to reuse this data. Recently, we have developed an application for information exchange between TurboRouter and ShipNet, which is probably the most widespread administrative and accounting system in the shipping industry.

In the last couple of years, we have seen a number of portals for spot cargoes emerging on the Internet. These portals will, to some extent, act as a broker between the cargo owner and the shipping companies. Even though none of these have yet become very important and dominant, the trend may still go in the direction of such portals. Recently, we have started a new research project to develop a search engine that can search the relevant portals and employ user specifications to find a number of spot cargoes that may be interesting for the shipping company. These cargoes can be fed into the DSS, such that the planner can test how the different cargoes will fit in the fleet schedule together with the existing cargo commitments. In this way, the shipping companies can quickly test a large number of spot cargoes, in order to choose the ones that fit best, i.e. the ones that will reduce the fleet’s ballast sailing and waiting time.

As mentioned earlier, most of the research efforts in vessel fleet scheduling have been focused on the development of optimization algorithms. Our experience tells us that the ocean shipping industry was not yet ready for this. Therefore, we focused even more on the user interaction when developing the DSS. However, now it seems like the industry is accepting more of this new way of planning. Therefore, I believe that the research focus should again be directed towards optimization algorithms, but one should be more aware of the user interaction and environment that the algorithms should function together with.

## Acknowledgements

The author acknowledges Sverre Inge Heimdal, a former employee at MARINTEK, for initiating this project. The author would also like to thank Arve Loktu and Geir Brønmo at MARINTEK who have done the programming of TurboRouter. The Research Council of Norway contributed with financial support that made the development of TurboRouter possible. The shipping companies, Beltship Management and Iver Ships, are also greatly acknowledged for contributing with expertise and financial support.

Finally, the author would like to thank the anonymous referees for insightful comments and suggestions that improved the paper.

## References

[1] C. Basnet, L. Foulds, M. Igbaria, FleetManager: a microcomputer-based decision support system for vehicle routing, Decision Support Systems 16 (1995) 195–207.

[2] D.O. Bausch, G.G. Brown, D. Ronen, Scheduling short-term marine transport of bulk products, Maritime Policy and Management 25 (4) (1998) 335 – 348.

[3] L. Bodin, L. Levy, Visualization in vehicle routing and scheduling problems, ORSA Journal on Computing 6 (3) (1994) 261– 269.

[4] G. Brønmo, K. Fagerholt, Fleet scheduling algorithms in TurboRouter, MARINTEK Report MT23 F01-023 (2001).

[5] G.G. Brown, G.W. Graves, D. Ronen, Scheduling ocean transportation of crude oil, Management Science 33 (3) (1987) 335 – 346.

[6] K. Darby-Dowman, R.K. Fink, G. Mitra, J.W. Smith, An intelligent system for US Coast Guard cutter scheduling, European Journal of Operational Research 87 (1995) 574– 585.

[7] K. Fagerholt, Optimisation based methods for solving ship routing and scheduling problems, Dr.ing. dissertation, Department of Marine Systems Design, Norwegian University of Science and Technology, Trondheim, Norway (1999).

[8] K. Fagerholt, S.I. Heimdal, A. Loktu, Shortest path in the presence of obstacles: an application to ocean shipping, Journal of the Operational Research Society 51 (2000) 683 – 688.

[9] Fearnleys Review, Annual, Fernsearch, Oslo, Norway (1997).

[10] M.L. Fisher, M.B. Rosenwein, An interactive optimization system for bulk-cargo ship scheduling, Naval Research Logistics 36 (1989) 27 – 42.

[11] S.-H. Kim, K.-K. Lee, An optimization-based decision support system for ship scheduling, Computers & Industrial Engineering 33 (1997) 689–692.

[12] G. Laporte, I.H. Osman, Routing problems: a bibliography, Annals of Operation Research 61 (1995) 227– 262.

[13] S.A. Lawrence, International Sea Transport: The Years Ahead, Lexington Books, Lexington, MA, 1972.

[14] J. Potvin, J. Rosseau, An exchange heuristic for routing problems with time windows, Journal of the Operational Research Society 46 (1995) 1433– 1446.

[15] D. Ronen, Cargo ships routing and scheduling: survey of models and problems, European Journal of Operational Research 12 (1983) 119– 126.

[16] D. Ronen, Ship scheduling: the last decade, European Journal of Operational Research 71 (1993) 325– 333.

[17] P. Toth, D. Vigo, Heuristic algorithms for the handicapped persons’ transportation problem, Transportation Science 31 (1997) 60– 71.

[18] E. Turban, Decision Support and Expert Systems: Management Support Systems, 3rd ed., Macmillan, New York, NY, 1993.

![](/api/attachments/TJBF3ZFY/fulltext/images/7726d5a82d7832aad9f69be6ea9ee03bad6f33ba8ba04edeeccaba23505bb389.jpg)

Kjetil Fagerholt is a Senior Research Engineer at MARINTEK, Trondheim, Norway. He also holds a position as an Associate Professor at the Norwegian University of Science and Technology, from which he also received his Dr.ing. and MSc degrees. His research interests include management science, operational research and decision support systems for the transportation industry in general, and the ocean shipping industry in particular. His prior research

has been published in several refereed journals, including the Journal of the Operational Research Society, European Journal of Operational Research, OMEGA – The International Journal of Management Science, International Transactions in Operational Research, Maritime Policy and Management and Naval Research Logistics.
