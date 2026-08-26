---
otero_id: 19034
otero_key: "DXWADT2Q"
title: "A design and implementation model for life cycle cost management system"
authors: "Nazim U. Ahmed"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(94)00040-p"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Applications

# A design and implementation model for life cycle cost management system

Nazim U. Ahmed \*

Department of Management, Ball State University, Muncie, IN 47306, USA

## Abstract

Design-to-cost is a management philosophy that emphasizes the selection and design of a system based on minimizing life-cycle cost. In some instances, systems alternatives are evaluated using such analysis, but actual implementation of design-to-cost philosophy throughout the entire system life is an exception rather than the rule. Management's lack of planning makes it difficult to implement this important philosophy. This paper analyzes and identifies the issues and provides a framework for design and implementation of a life-cycle cost management system.

Keywords: Design-to-cost; A-B-C classification; Life-cycle cost; Cost break down structure; System life-cycle; Critical success factor; Cost database

## 1. Introduction

American businesses have experienced many fundamental and structural changes within the last decade. Many of the major corporations who once had virtual monopoly, now have to face tough competitions. This is also true about medium-sized and small businesses. One of the major ingredients of being competitive is to lower the costs of production and or service delivery.

Design-to-cost philosophy states that all procurement decisions should be based on cost spread over the entire life of the system [5]. The goal is to minimize the total life-cycle cost. Life-cycle cost includes research and development, installation, and operation throughout the entire system life. This concept has a long history of use in the U.S. Department of Defense for evaluating new weapons system. Non-defense related industries also apply this concept to their major procurement decisions. However, often in both defense industries and also in the private sectors the cost goals are not achieved due to lack of proper planning and control of management tasks at different stages of the life-cycle.

For a complex system it is easy to lose sight of many of the cost elements to be incurred in the future. Also, for simplicity, managers may assume that there is no significant differences between the ownership cost of alternative systems. Another reason for life-cycle costing being not effectively used is the short term view of the management in the United States. Generally, the managers are rewarded for saving money on an immediate basis, ignoring significant potential expenses in the long run.

Recently, because of competitive environment many companies are trying to streamline their production and service delivery systems by investing billions of dollars in technologies like robotics, CAD/CAM [22], group technology, flexible manufacturing system, artificial intelligence [8] and so on. In many instances, the decisions for procurement of new system or modification of existing systems may be based on initial cost or costs to be incurred in the very near future. This approach even though convenient may be not be economically competitive in the long run.

It is only logical that any major procurement decision should be based on life-cycle cost analysis. However, selection of a system based on life-cycle cost alone is not enough. It is important that the cost goals are achieved through proper planning, and execution of management activities. Various cost models such as parametric cost estimating models $[3,11]$ , replacement model $[16]$ and others $[1,7,10,13,23,24]$ exist that attempt to analyze and integrate different life-cycle cost factors analytically. Problems arise during the actual design, implementation, and operation of the system as many of the design-to-cost goals are not met. This paper describes a framework for implementing the design-to-cost philosophy by achieving cost goals at different phases of the systems life.

![](/api/attachments/DXWADT2Q/fulltext/images/6f4d66f1b4a2a570e28ee42974c8dde2f1d231d53d49848fe1f3c56f4497e9b6.jpg)  
Fig. 1. A planning framework for design-to-cost philosophy.

Fig. 1 provides an outline of the framework developed in this paper. The stages of the system life-cycle are condensed into: (1) the acquisition phase and (2) the operation phase. Acquisition phase includes all the activities ranging from research and development, to design and installation. Operation phase includes all the activities during the actual operation of the system. The major management tasks in the acquisition phase involve establishing the design-to-cost goals, developing the initial information system and estimating cost targets, and identifying the critical success factors [6,12,14]. The major management tasks in the operation phase include modification of the IS and operations cost monitoring and control. The IS and database developed in the acquisition phase can be used, with some modification, in the operation phase. It should be emphasized that the management modules should be in place before the actual start of that phase. For example, the information system for acquisition phase should be in place before the initiation of the acquisition phase.

![](/api/attachments/DXWADT2Q/fulltext/images/fd297aed051d1fb8bfbc39f3dd2d8b14c47840bdda652a46482ac1f46a572083.jpg)  
Fig. 2. An example of a cost breakdown structure.

## 2. Acquisition phase

The major management tasks in this phase are described below.

## 3. Establishing design-to-cost goals

Design-to-cost goals consist of the target minimum for different categories of cost spread over the entire service life. The important vehicle for establishing the cost goals is the cost break down structure (CBS) [4]. The process involves developing a satisfactory CBS and then the CBS framework is analyzed in terms of importance of cost items using a technique called A-B-C analysis [22].

## 3.1. Developing the cost breakdown structure framework

The idea is to breakdown the total system life-cycle costs into hierarchical cost categories. These are generally established on the basis of functional activity areas, major element of a system, classes of common cost items, etc. A cost break down structure should satisfy three major requirement.

(1) identify major items or significant activities and be well defined having the same meaning throughout the entire organization.

(2) be designed in such a manner that it is possible to identify the impact of cost change in a particular area without affecting the other areas.

(3) be compatible with the data requirements for management cost reporting and control.

Fig. 2 shows a hypothetical cost break down structure for a computer system. The cost break down structure in this example is general and has been simplified. All cost items and their relationship may not be known by a single person. If it is large then it is impossible. A satisfactory framework may be obtained through an interdisciplinary and iterative process. In the cost break down structure, it should be possible to isolate the costs in different categories for management reporting and control purposes.

## 3.2. A-B-C analysis of cost break down structure

A-B-C analysis is a technique frequently used in the operations management and quality control. It is derived from a simple but very important concept called the “pareto” principle. A manager should identify and distinguish between the “vital few” and the “trivial many” items. For attaining efficiency and profitability, one should put more emphasis on the “vital few” items. The “A” items are those that are few in number but critical, in the sense that they constitute a significant portion of the costs. “B” items number more than “A” items and are moderately critical. “C” items may number in the hundreds but together constitute a minor portion of the total cost.

In the illustration, “A” items are marked with “\* \* \*”, “B” items are marked with “\* \*” while “C” items are not marked. The A-B-C analysis should be done at a level of cost break down structure where the costs are specific. For example, initial cost, and operation cost are extremely important, since they are at the top of the cost break down structure. However, classifying them as “A” items will not reveal useful information for cost control purposes. Thus, hardware and software costs were designated as “A” items, but not all of their child necessarily will be “A”. Once the cost break down structure is analyzed, it is important to design the management control and reporting system so that the “A” items are most emphasized and the “C” items least.

## 4. Developing cost database and initial information system

It is extremely important to develop a cost database [21] and management information system for cost monitoring and control. The cost break down structure is an extremely important input for the design of a cost information system.

The essential components of the initial IS are the cost database and cost data dictionary $[17]$ that supports the three information modules (IM). The procurement IM should provide on-line information and generate report on procurement cost, lead time, vendor information and other related information. The planning and scheduling IM should generate information relevant to planning and scheduling of acquisition activities. The cost management IM should enhance management decision support by incorporating models and techniques for cost analysis, simulation, future cost and variance forecasting, etc.

The data dictionary and design of cost database are critical. The database design should support the planning activities in relation to the CBS. The purpose of the data dictionary is to provide documentation of data structures and semantics with a brief description of use, possible ranges of values, sources etc. This will prevent confusion of the meaning of the terms.

Finally the IS should: (1) provide summary information to top management, (2) provide routine reports to departmental managers, 3) continuously monitor critical cost components and provide exception reports.

## 5. Establishing cost targets

Cost break down structure is the main vehicle that identifies different cost components and their relationships. Cost targets are the actual value of the cost components in the framework. Developing the cost profiles (i.e., projecting costs over the life-cycle) involves the following steps:

(1) Within each cost category in the cost break down structure, establish the cost element-time matrix. This is the projection of cost for each cost element over the life-cycle.

(2) For each cost category estimate relevant factors for such variables as inflation, effects of learning curves, discount rate etc., and adjust the cost projection accordingly.

Examples of mapping of CSF's at policy, strategic and operational levels

<table><tr><td>Phase/level</td><td>Policy</td><td>Strategic</td><td>Operational</td></tr><tr><td>Acquisition</td><td>1.0 Acquisition cost variation should be less than 1%.</td><td>1.1 Construction cost variance should be less than 1%1.2 No construction delay should be allowed</td><td>1.1.1 Monitor vendor purchase cost weekly1.1.2 Monitor construction cost weekly1.1.3 Report exception and take immediate action1.2.1 Compare progress with schedule weekly1.2.2 Project future monthly schedule1.2.3 Report exceptions and anticipated actions</td></tr><tr><td>Operation</td><td>2.0 First two year cost should be within budget</td><td>2.1 Monthly cost variance should be less than 2%2.2 No quarterly cost overrun in “A” items</td><td>2.1.1 Monitor departmental cost weekly2.1.2 Project cost on a monthly and quarterly basis2.1.3 Report exceptions, anticipated exceptions and actions2.2.1 Review cost of “A” items weekly2.2.2 Project cost of “A” items on a monthly and quarterly basis2.2.3 Report exceptions and actions</td></tr></table>

(3) Develop a hierarchical cost profile at each level following the cost break down structure framework.

For estimating the cost, a Life-cycle cost (LCC) steering committee should be organized with managers from each department affected by the system. They should be knowledgeable in the appropriate aspects of the system so that they understand the short term and long term ramifications of the costs. The cost estimation should ensure that managers:.

Step 1. Understand the cost break down structure in major cost categories.

Step 2. Decide who is responsible for cost estimation, reporting and control and concern with the assignments.

Step 3. Form a team in their own departments for estimating costs assigned to them.

Step 4. Resolve the responsibility for those cost elements, that fall into the “fuzzy” areas by assigning cost to departments that are closer to that cost centre or devising other ways to resolve it.

Step 5. Review the “A” and “B” cost items to see if there are any discrepancies in the estimate.

Since most of these are future costs, it may be useful to require three cost estimates for “A” and “B” items. These estimates are pessimistic, most likely and optimistic cost estimates similar to PERT-cost.

## 6. Identifying critical success factors

Critical success factors (CSF) are important variables $[14,15]$ that can aid in the successful implementation of a project. The idea was first introduced by Daniel $[9]$ was refined by John Rockart $[20]$ for designing IS. According to Rockart, management should identify CSF before designing or implementing an IS.

CSF should be established at the top management or corporate level, at middle management or strategic level and also at lower or operational level. CSF's for top management emphasize policies and guidelines. CSF's at the middle management or strategic level transforms policies into strategies. At the operational level, strategies are transformed into specific actions. Table 1 provides examples of mapping of CSF's. Here the CSF at the policy level for the acquisition phase is to keep the cost overrun to less than 2 percent of the estimated amount. This can be transformed into CSF's at the strategic levels of monitoring construction cost variance and construction cost delay etc. The CSF's at the operational level would consists of monthly and weekly review of construction cost etc.

## 7. Operation phase

Most of the system cost is incurred during the actual operation throughout its service life $[4]$ . It is important that serious planning and control effort are aimed at attaining the design-to-cost goals during the operation phase. Basic planning of the management tasks for this phase should be done before hand and preferably even before the system is acquired. This includes establishing the cost goals, identifying the critical success factors, cost management and reporting system etc. Also, the planning and task coordination during the acquisition phase should be performed by keeping in mind the integration requirement with the operation phase.

## 8. Modifying the information system

The initial IS was geared towards acquisition activities. However, not all of it should be scrapped as many of its features could be incorporated into the new IS. Planning for the initial IS should consider the future requirements. This would reduce the cost and time of modifications.

The main components that can be retained with minor modifications are: (a) Database, (b) data dictionary, and (c) database management system. It is assumed that the database was developed to be useful for the entire system life-cycle. Also, the data dictionary should have been based on the content of the database. The criteria on which the database management system was selected in the acquisition phase should also be the same for the operation phase.

![](/api/attachments/DXWADT2Q/fulltext/images/4cca42acd68a46af79ea05d210743fcc78161cbeed5867d1f332a55a81a9d849.jpg)  
Fig. 3. Operations information system.

Some modifications need to be made in the initial IS as its requirements will change for the operation phase. For example, the procurement information module may not be necessary if the procurement decisions are routine and not very complex. The schematic of the information system for operation phase is shown in Fig. 3.

The planning and scheduling module in this phase should be different from that of the acquisition phase. This module should generate information about manpower planning, equipment planning, maintenance planning, etc.

The cost monitoring module should generate information about major cost items (“A” and “B”

items) routinely, on an exception basis, and also at important milestones of the system life-cycle.

The management decision support module is important and should be designed in such a way that managers can use it as a planning and analysis tool for cost management and control.

This decision support [8] should include management science models like linear programming, scheduling, forecasting, and simulation [22]. Finally, it should track the status of the critical success factors and project them into the future to anticipate any problems or opportunities.

## 9. Cost monitoring and control

Once the decision is made to acquire a system on the basis of design-to-cost philosophy, continuous monitoring and control is necessary to make sure that different activities progress according to the scheduled plan of action. To accomplish this, management must establish proper monitoring and control procedures which should include: (1) report generation, (2) tracking of critical success factors, and (3) establishing an incentive scheme.

## 9.1. Report generation

Administering life-cycle cost activities is very complex. It involves managers of several departments. Necessary reports include (1) cost items in the cost break down structure, (2) those for the departments, (3) those for major cost components, (4) summaries for top management, (5) exception reports for departments and top management, (6) comparison statistics, and (7) projection reports [19].

## 9.2. Tracking critical success factors

Critical success factors are important barometers to judge the success of the system in terms of attainment of design-to cost goals. Each one should be associated with one or more performance measures $[18]$ . The IS should be able to generate statistics on these performance measures. Based on these statistics, managers should take appropriate action for achieving the cost goals.

## 9.3. Establishing incentive scheme

Two types of incentive systems should be designed for implementing the design-to-cost philosophy. The internal incentive system should not necessarily concentrate on immediate cost saving. Some long term factors should also be incorporated so that managers do not try to achieve short term saving at the expense of long term gain.

Sometimes a significant portion of the life-cycle cost is incurred through outside personnel or organizations. The external incentive system should be based on negotiations between the firm and the outside contractors. For well established systems, fixed price contracting procedures are common. For newly developed systems, contracts can be relatively flexible and cost reimbursing agreements may have to be negotiated.

One common method of contract payment is incentive contracting $[2]$ . According to this, a sharing ratio is negotiated between the firm and the contractor. For example, a 40/60 sharing ratio means that in case of cost savings from the target, 40 percent of the savings will go to the firm and 60 percent of the cost savings will go to the contractor. This will be true about the cost overrun also.

## 10. Conclusion

Design-to-cost is a management philosophy that emphasizes the selection of a system based on total minimum life-cycle cost. Even though, this seems logical, the traditional acquisition decisions are still biased towards initial price. There is a sizeable body of literature which attempts to analyze the cost relationships for complex systems. Problems arise during the actual management of the life-cycle cost.

This paper provides a conceptual framework for design and implementation of a life-cycle cost management system. The life-cycle is condensed into two major phases. The acquisition phase includes the activities from research and development, design, up to the installation of the system. The operation phase includes the activities during the actual use of the system.

The IS developed for the acquisition phase should be modified to generate relevant information for the operation phase. This includes routine and exception reports to be generated for departments and top management. Also, the decision support module of the IS should provide important planning information by generating scenarios for different decisions and situations. Tracking the CSF is also important as it provides the necessary information to devise strategies for achieving design-to-cost goals. Finally, an incentive scheme should be established both for internal personnel and external contractors.

## References

[1] Ahmed, N.U., “Design-to-cost Approach in Selecting Production System,” Production and Inventory Management, 29: 2 (1988), 52–56.

[2] Auer, J.H. and C.E., Harris, Major Equipment Procurement, Van Nostrand Reinhold Company, New York (1983).

[3] Black, J.H., “Application of Parametric Estimating to Cost Engineering,” AACE Transactions, (1984), B.10.1–B.10.5.

[4] Blanchard, B.S., Design and Manage to Life Cycle Cost, M/A Press, Portland, Oregon (1978).

[5] Boden, W.H., “Designing for life-cycle cost,” Defense Management Journal, 12:1 (January 1976), 29–37.

[6] Boynton, A.C. and Zmud, R.W., “An Assessment of Critical Success Factors,” Sloan Management Review, (Summer 1984), 17–27.

[7] Bryan, N.S. and Rosen, J.J., “A New Life Cycle Cost Model: Flexible, Interactive and Controversial,” Defense Management Journal, 16: 3 (1980), 2–7.

[8] Bullers, W.I., Jr. and Richard, R.A., “Toward a Comprehensive Conceptual Framework for Computer Integrated manufacturing,” Information and Management, 18: 2, (February 1990), 57–67.

[9] Daniel, R.D., “Management Information Crisis,” Harvard Business Review, (Sept.-Oct. 1961), 111.

[10] Dreger, G.T., “Cost Management Models for Design Application,” AACE Transactions, (1988), J.4.1.-J.4.2.

[11] Ferens, D.V., “Software Parametric Cost Estimation: Wave of the Future,” Engineering Costs and Production Economics, 14: 2 (July 1988), 157–164.

[12] Freund, Y.P., “Critical Success Factors,” Planning Review, 16: 4 (July/August, 1988), 20–23.

[13] Greer, W.R. and Liao, S.S., “Competitive Weapon Systems Procurement: A Summary and Evaluation of Recent Research,” National Contract Management Journal, 17: 2 (Winter 1984), 37–47.

[14] Jenstor, P.V., “Using Critical Success Factors in Planning,” Long Range Planning, 20: 4 (1987), 102–109.

[15] Malcom, M.C. and Basil, R.W., “Planning Critical Success Factors, and Management’s Information Requirements,” MIS Quarterly, 4: (1980), 29–39.

[16] Montag, G.M., “Life-Cycle Costing Building Replacement Analysis Model,” ASHRAE Journal, (August 1981), 39–44.

[17] Navathe, S.B. and Kerschberg, L., “Role of Data Dictionaries in Information Resource Management,” Information and Management, 10: (1986), 21–46.

[18] Pinto, J.K., “Variations in Critical Success Factors Over the Stages in the Project Life Cycle,” Journal of Management, 14: 1 (1988), 5–18.

[19] Postula, F.D., “Development of an Integrated Cost Forecasting,” AACE Transactions, (1985), G.3.1.-G.3.7.

[20] Rockart, J.F., “Chief Executives Define Their Own Data Needs,” Harvard Business Review, (Mar.-Apr. 1979), 81–93.

[21] Samid, G., “Cost Data Base: How to build or buy the one you need,” Cost Engineering, 26: 2 (April 1984), 37–40.

[22] Schonberger, R.J., Operations Management, Business Publication Inc., Plano, Texas, (1985).

[23] Wierda, L.S., “Product Cost-Estimation by the Designer,” Engineering costs and Production Economics, 13: 3, (March 1988), 189–198.

[24] Wilson, R.L., “Operations and Support Cost Model for New Product Concept Development,” Computers and Industrial Engineering, 11: 1, (1986), 128–131.

![](/api/attachments/DXWADT2Q/fulltext/images/1eddd323aece378accddf18e80d357e2154370f4f957451aceed8f355e724d54.jpg)

Dr. Nazim U. Ahmed is currently a professor in the Department of Management at Ball State University. He obtained his Ph.D. degree from Texas A&M University. His primary teaching interests are in the areas of Operations Management and Information Systems. Dr. Ahmed's publications have appeared in International Journal of Production Research, Journal of Operations Management, Transportation Research, Journal of Busi

ness Research, Information and Management, Computers and Industrial Engineering, Production and Inventory Management, Journal of the Academy of Marketing Science and also in other journals.
