---
otero_id: 17403
otero_key: "DTWHKJDG"
title: "Decision support system for production planning — Concept and prototype"
authors: "Hitoshi Tsubone; Haruki Matsuura; Kyoko Kimura"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)e0037-e"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support system for production planning – Concept and prototype

Hitoshi Tsubone $^{a,*}$ , Haruki Matsuura $^{b}$ , Kyoko Kimura $^{c}$

$^{a}$ Department of Management Engineering, Tokyo Metropolitan Institute of Technology, 6-6 Asahigaoka, Hino-city, Tokyo, 191, Japan $^{b}$ Department of Business Administration, Kanagawa University, Tsuchiya 2946, Hiratsuka-city, Kanagawa, 259-12, Japan $^{c}$ Division of Production Management, Konica Corporation, 1-chome, Sakura-cho, Hino-city, Tokyo, 191, Japan

## Abstract

This paper deals with the problem of the decision support system for production planning from the viewpoint of two major functions: physical performance analysis and choice analysis. The first is make clear, through the physical performance analysis, the impact of decision variables on the system performance such as unfilled order rate for market demand, ratio of setup time, average inventory level of finished products and part items, and frequency of replanning. The second is to guide for selecting an alternative or setting the decision variables value, if management can, on the basis of the physical performance analysis results, provide a ranking, preference, or acceptable limits in terms of their contribution or importance to the production system. An example of the prototype DSS for the production planning is also presented from the above-mentioned viewpoint.

Keywords: Production planning; Physical performance analysis; Choice analysis; Multiple criteria

## 1. Introduction

One of the production planning problem is concerned with specifying optimum production capability so as to satisfy the market demand for a forthcoming planning horizon. Such decision problems are often semi-structured, even at the tactical level because of the dynamic nature of the manufacturing environment such as change in product mix, design change, etc. These also cause changes in market demand fluctuation for the finished products, bottleneck change, and changes in manufacturing lead-time, Thus, in order to respond to such changes in the manufacturing environment, it is important for the management to continuously review changing production system status.

It is also necessary to provide manufacturing systems with control capabilities to make a decision for semi-structured problems. That is, when such environment changes are foreseen, the management, at first, has to identify how such changes will affect the production system. Then, they needs to modify or redesign, if necessary, the production planning system, in order to satisfy the market demand for finished products at their minimum inventory level under various constraints.

This is the starting point in our approach in developing the decision support system(DSS) for production planning in a semi-structured environment at the tactical level.

A variety of papers relative to the DSS for production planning have been published. For example, Ramesh and Sekar [5] present an framework for decision support in the hierarchical planning system. Pels and Wortmann [4] discuss the issue of decentralization and decomposition of information system in the hierarchical organization. Lee and Lee [2] discuss the interaction between long-term planning and short-term planning. Lundell and Osrlund [3] present DSS for manufacturing resource planning. Bitran et al.[1], Tsubone, et al.[7], and Tsubone and Sugawara [8] present the hierarchical production planning system which can extend to the DSS. The interactive production planning systems also are presented [9], [10]. Tabucannon [6] presents a methodology how to achieve multiple-goals in an intangible and conflicting environment.

This paper, first, describes two major DSS functions; physical performance analysis and choice analysis. The physical performance analysis clarifies the impact of decision variables or parameters on the manufacturing performance. On the other hand, the choice analysis is a guide, reached on the basis of the results of physical performance analysis, to selecting an alternative or setting an optimum value for decision variables.

Second, the prototype DSS for make-to-stock production planning is presented, from the above-mentioned viewpoint, in a two-stage part fabrication/finished product assembly process.

## 2. DSS for production planning

## 2.1. Manufacturing performance

Production planning is necessary to implement production activities smoothly, as well as to satisfy the market demand, while inventory is maintained at as low a level as possible. The total-cost performance is an important measure as criteria, but does not capture all the production planning effects on manufacturing performance. Additional difficulties lie in estimating intangible costs, such as shortages for unfilled products which prevent meeting market demands, as well as setup costs at a potential bottleneck.

Thus, physical performance measure, such as the unfilled-rate, average inventory level, and total setup time, are generally preferred to be used as manufacturing performance indicators at the tactical planning level.

These measures often have intangible and conflicting relationships in regard to each other. Accordingly, the production planning problems usually involve multiple conflicting objectives. These problems are solved through an interactive process, which continues until they terminate when a mutually acceptable plan is reached.

The DSS role is to facilitate an efficient analysis of various decision alternatives as well as to analyze manufacturing performance in production system. DSS can be divided into distinctly related phase: Physical performance analysis and Choice analysis.

## 2.2. Physical performance analysis

The objective of physical performance analysis is to clarify production system behaviours such as those bearing on the manufacturing performance, by analysing the relationship between production planning rules and the decision variables, such as buffer inventory level, in terms of manufacturing performance.

Such factors are:

(1) How will the safety stock level, required for finished products, be affected by a change in product mix?

(2) How will the total set-up time, pertinent to the part fabrication processes, be affected by changes in lead-time resulting from changes in design for part items or through standardization programs?

(3) How will deviation in production rate and changed production quantity resulting from replanning be affected by production planning procedure?

(4) How much can “nervousness” regarding planning be deduced by increasing the buffer inventory level for part items or finished products?

Since simulation is one of the most effective methods for the management to understand a complex and complicated actual production system, these physical performance analysis can be achieved, through the use of a simulation model, without losing their essentials, by changing decision variables in the production system. The simulation model, using input from the user and database, can estimate important operating characteristics in the production system, such as unfilled order rate, ratio of set-up time or frequency, average inventory level, etc.

The management can identify and confirm a production bottleneck which would affect production capacity, and evaluate the effect of various decision variables, such as buffer inventory and control parameter for smoothing production, on the manufacturing performance.

The input to the physical performance analysis can be obtained from the manufacturing profile database called as MP and the terminal. The MP database stores all the data relative to a production system, such as the unit processing time and set-up time for each part item, and routing at the fabrication process, the unit assembly time for each finished product, the bill of materials, lead-time of part items required for assembly lines, and historical data regarding market demands for each finished product, on an average and a standard deviation, for use in forecasting market demand for finished products.

![](/api/attachments/DTWHKJDG/fulltext/images/39638f1aefd76c1def7864116d3a52420ee6e753a7cc4471c2395d4fc74ece37.jpg)  
Fig. 1. Procedure for physical performance analysis.

Fig. 1 shows a rough procedure for the physical performance analysis.

First, when accessing the MP database, the user needs to identify or check all the data relative to the production system. He needs to, if it necessary, update their pertinent values, add new data, or delete data, according to change in product mix, and change in operating conditions of the production process.

Second, through the performance analysis model, the user can identify any potential bottlenecks and can analyze the operating characteristics for the production system under various production planning rules, by varying the decision variables such as buffer inventory and parameter for smoothing production.

The analytical results are stored in the performance file, from which the data can be extracted relative to the relationship between decision variable value and performance measures values. As examples, these entail: (1) Buffer inventory level versus the unfilled order ratio for finished products. (2) the parameter for smoothing production versus the deviation in monthly production rate. (3) The buffer inventory levels for both part items and finished products, which can control the unfilled order ratio, under various planning rule, within their acceptable upper limit. (4) The inventory level for part items versus the difference between, due to replanning, planned production quantity and actual production quantity under various production planning policies.

## 2.3. Choice analysis

Choice analysis supports the management in choosing an appropriate production plan from among several specified sets or ranges of alternatives. That is, the results of the physical performance analysis indicate that the conflict arises

because an important decision in regard to meeting an objective cannot be made, to the detriment of meeting the other objectives. Thus, the management can, through the choice analysis, make a decision on the value of decision variables and specify the planning rules to be employed for production activities, by providing a ranking, preference, or acceptable limits in terms of their contribution or importance to the production system. The multi-objective production decisions are solved interactively by assessing the decision maker's preference or knowledge about the production system. This is an interactive process, and it terminates when acceptable operating conditions are obtained.

![](/api/attachments/DTWHKJDG/fulltext/images/3f34d8b30b87affcc615b58c72704d0f2d88e688b3af194cdc291329421bcbb2.jpg)  
Fig. 2. Procedure for choice analysis.

The first step in the choice analysis, to form the management policy, as combination of various objectives, in account with the results of physical performance analysis. Examples are as follow:

Objective O $^{A}$ : Control the unfilled order rate (A) for finished products within their acceptable upper limit (a %).

Objective O $^{B}$ : Control the average inventory level (B) for finished products within b %, in regarding to weekly average market demand.

Objective O $^{C}$ : Control the average inventory level (C) for part items within c %, in regarding to weekly average requirements.

Objective O $^{D}$ : Control the ratio of setup time (D) to the processing time within d %.

Objective O $^{E}$ : Control the deviation (E) in monthly production rate within e %.

Objective O $^{F}$ : Control the ratio (F) of the difference, due to replanning, between planned production quantity and actual production quantity, in regarding to weekly production within f %.

The value for pertinent measures in each objective must be set within a feasible limit or range, if only a single objective would be selected.

The second step of the choice analysis is to select objectives one by one in order of importance, then to set its acceptable limit. For example, $O^{A}(a)/O^{B}(b)/O^{C}(c)/...$ etc., denotes the importance ranking for management objectives as mentioned above. The primary priority is Objective $O^{A}$ , second is Objective $O^{B}$ under the conditions which can satisfy Objective $O^{A}$ , while third is Objective $O^{C}$ under the conditions which can satisfy Objective $O^{A}$ and $O^{B}$ , and so forth, until all the decision variable values are specified and a feasible production planning rule is selected. The notation in the bracket expresses an acceptable upper limit in each management objective.

![](/api/attachments/DTWHKJDG/fulltext/images/ea126606eeda28b0d6021496cc02752519560be2b86567934ec1702fea0e9e7f.jpg)  
Fig. 3. DSS architecture.

Fig. 2 represents a procedure for the choice analysis.

In the decision process through the choice analysis, the developed system has two approaches, involving only a slight difference in detail. One approach is where all the acceptable limits are set at the same time, when objectives are determined. The other approach is where each acceptable limit is set each time an individual objective is selected as having the highest priority among the objective set. The latter approach is shown as example in the later chapter.

## 2.4. DSS architecture

The architecture developed aids the management to assess the physical performance analysis and to determine, through the appropriate choice analysis, the value of various decision variables, while still remaining knowledgeable about the implications of their decisions for all aspects of the production system.

The DSS architecture, as shown in Fig. 3, is composed of the control subsystem, the database subsystem, the model subsystem, and the report subsystem.

The control subsystem supports the management to handle the situation employing the DSS and to interact with other subsystems. The database subsystem contains all data required for the formulation of the model. At the physical performance analysis phase, the model subsystem, using input from the user and database files, can be used to analyze important operating characteristics of the production system. At the choice analysis phase, the model subsystem furnishes guides enabling the user to set respective values for decision variables and to select a production planning rule, if the management can rank the importance about various factors or objectives.

The user can control the solution process by setting initial parameters and selecting pertinent algorithms, in the interactive process for both performance analysis and choice analysis. The report subsystem is a critical link in the communication process, between the model subsystem and the DSS user. This subsystem furnishes access to the basic data and the model solution, showing them on the screen and presenting hard-copy reports.

## 3. Prototype DSS for production planning

## 3.1. Production system model

The production system for a prototype DSS can be modeled as a two-stage fabrication/assembly process. The materials are processed into different item categories for respective finished products on the fabrication processes. They are fed to the assembly lines to be assembled into a variety of finished products, in accordance with diverse market demands. It is assumed that the market demands for finished products fluctuates independently in each period. All unfilled demands for finished products are backordered as “unfilled order”, when there is no longer any stock in hand.

Loss time for setup can be regarded on assembly lines as minor and negligible, but it cannot be considered negligible in the fabrication processes. The materials become available part items for assembly one week after they start to be processed in the fabrication processes.

Two-level planning model is used to plan production of finished products and part items. First, an aggregate model is used to determine the aggregate number of units of finished products and part items, respectively, to be produced in the immediate month of the planning horizon. These number of units are determined by using an aggregate forecast demand for finished products. The aggregate production planning takes place once a month.

Two production planning rules are adopted in the assembly lines: “Fixed planning” and “flexible planning”. Fixed planning fixes or freezes the number of units for each finished product to be produced at the assembly lines over the accumulated total lead-time, in order to avoid nervousness due to replanning. Flexible planning varies the number of units of finished product, up to those units for which respective part items can be supplied, though the aggregate number of units remains fixed.

![](/api/attachments/DTWHKJDG/fulltext/images/d6111b88aa9c104efe3c7265d0123cf3c2f7c087e45f1fffc62a3ee5da527344.jpg)  
Fig. 4. Demo in physical performance analysis.

## 3.2. Performance criteria

The criteria used to evaluate the manufacturing performance in the production planning system are:

(1) The unfilled-rate or shortage in meeting market demand, that is, the demand ratio which would be unfilled when immediately using the finished products stock.... (A).

![](/api/attachments/DTWHKJDG/fulltext/images/286997595562d2b9f164baa804d86c1444a9a0cb7c19b299b544063ea2276cff.jpg)  
Fig. 5. Demo in physical performance analysis.

(2) The average inventory level of finished product.... (B).

(3) The average inventory level of parts items.... (C).

(4) The ratio of total set-up time to total processing time at the fabrication process.... (D).

(5) The deviation in the monthly production rate.... (E).

(6) The changed production quantity due to replanning, that is, difference in the actual production quantity of each finished product and the planned quantity as a measure representing the results due to replanning.... (F).

These criteria measures are expressed in a normalized fashion for the examples for prototype DSS.

## 3.3. Decision variables and planning rules employed

The decision variables in the production system are:

(1) The buffer inventory level for parts items and finished products, indicating $\alpha$ and $\beta$ respectively.

(2) The control parameter or coefficient ( $\gamma$ ) for smoothing production.

An additional controllable factor is the determination of production planning rule to be set, that is, either fixed planning rule or flexible planning rule can be employed in the weekly planning.

## 3.4. Example for prototype DSS

## (1) Physical performance analysis

Fig. 4 and 5 show examples of the output, obtained through the physical performance analysis under the conditions for simplified case study regarding this study without losing essential.

## (2) Choice analysis

Table 1 shows an example of a decision process, in which the allowable ranges for respective performance measures are determined each time when objectives are determined.

“Step 0” in Table 1 indicates the source data, that is, respective performance measure values obtained through the physical performance analysis. They are stored from the minimum value to the maximum value of each performance measure when the decision variables vary from zero to their respective specific value. “Step 1” indicates the allowable range of each performance measure, under the conditions in Objective O $^{A}$ (1 %) as the primary objective. “Step 2” indicates the performance measures under the conditions in Objective O $^{A}$ (1%)/O $^{D}$ (7%), i.e., under the conditions by which the second priority is Objective O $^{D}$ . “Step 2” also indicates that flexible planning rule has been selected or specified as production planning rule at the time when Objective O $^{D}$ has been determined. Objective O $^{B}$ is selected as the next priority in step 3. This procedure terminates when all the decision variables are fixed at respective specific values. Accordingly, this system can indicate how various policies will fix the decision variables at their specific value, depending the objective ranking and acceptable upper limits.

Table 1  
Demonstration for choice analysis

<table><tr><td>Step</td><td>Objective combination</td><td>Planning rule</td><td>A</td><td>D</td><td>B</td><td colspan="2">E</td><td>C</td><td>F</td></tr><tr><td rowspan="2">0</td><td rowspan="2">Source data</td><td>Fix</td><td>0 ~ 0.28</td><td>0.09 ~ 0.11</td><td>0.12 ~ 0.97</td><td>0</td><td>~ 0.05</td><td>0 ~ 0</td><td>0 ~ 0</td></tr><tr><td>Flexible</td><td>0 ~ 0.27</td><td>0.04 ~ 0.10</td><td>0.09 ~ 0.97</td><td>0</td><td>~ 0.05</td><td>0.19 ~ 1.02</td><td>0.06 ~ 0.15</td></tr><tr><td rowspan="2">1</td><td rowspan="2"> $O^A(1\%)$ </td><td>Fix</td><td></td><td>0.09 ~ 0.09</td><td>0.54 ~ 0.96</td><td colspan="2">0.006 ~ 0.04</td><td>0 ~ 0</td><td>0 ~ 0</td></tr><tr><td>Flexible</td><td></td><td>0.04 ~ 0.09</td><td>0.36 ~ 0.96</td><td colspan="2">0.006 ~ 0.04</td><td>0.19 ~ 1.01</td><td>0.08 ~ 0.14</td></tr><tr><td rowspan="2">2</td><td rowspan="2"> $O^A(1\%) / O^D(7\%)$ </td><td>Fix</td><td></td><td></td><td>-</td><td colspan="2">-</td><td>-</td><td>-</td></tr><tr><td>Flexible</td><td></td><td></td><td>0.36 ~ 0.96</td><td colspan="2">0.006 ~ 0.04</td><td>0.60 ~ 1.01</td><td>0.11 ~ 0.14</td></tr><tr><td rowspan="2">3</td><td> $O^A(1\%) / O^D(7\%)$ </td><td>Fix</td><td></td><td></td><td>-</td><td colspan="2">-</td><td>-</td><td></td></tr><tr><td> $O^B(60\%)$ </td><td>Flexible</td><td></td><td></td><td></td><td colspan="2">0.006 ~ 0.04</td><td>0.60 ~ 1.01</td><td>0.11 ~ 0.14</td></tr></table>

## 4. Conclusion

DSS has to be developed to help the management arrive at appropriate decisions and to strengthen their production management problem-solving abilities, when faced with a rapidly changing manufacturing environment, such as changing in market demands and changing in operating conditions of production process through operation improvement “Kaizen” activities.

This paper, first, presented two major DSS functions for production planning in semi-structured environment, and described their relationship from the viewpoint of problem finding and solving in the production system. We have presented, second, a prototype DSS for production planning. A demonstration of the system has been made for IBM 9370. The physical performance analysis can, through using a simulation model as the main tool, guide management in finding problem in a production system. On the other hand, the choice analysis is, as it were, a problem solving tool. That is, it can acts as a guide for selecting an alternative or setting the value of decision variables, if management can provide objective ranking and importance to the production system, on the basis of accumulated knowledge, through the physical performance analysis.

There is no theoretical foundation in particular for the method developed. Regardless of this fact, it is useful in guiding decision making, while focusing very carefully indeed on how the managers think and what factors they are likely to regard as relatively important.

## References

[1] G.B. Bitran, A.E. Hass, and C. Hax, Hierarchical Production Planning Systems: A two-stage process, Operations Research 30 (1983) 717–741.

[2] J.K. Lee and H.G. Lee, Interaction of Strategic Planning and Short-term Planning, Decision Science 3 81987) 141–154.

[3] P. Lundell and B. Osrlund, A Decision Support System for Long Range Manufacturing Resource Planning, Engineering Costs and Production Economics 12 (1987) 159–164.

[4] H.J. Pels and J.C. Wortmann, Decomposition of Information Systems for Production Management, Computers in Industry 6 (1985) 435–452.

[5] R. Ramesh and C. Sekar, An Integrated Framework for Decision Support in Corporate Planning, Decision Support Systems 4 (1988) 365–375.

[6] M.T. Tabucanon, Multiple Criteria Decision Making in Industry, Elsevier Science Publishers BV (1988).

[7] H. Tsubone, H. Matsuura, and T. Tsutsu, Hierarchical production planning system for a two-stage process, International Journal of Production Research 29 (1991) 769–785.

[8] H. Tsubone and M. Sugawara, A Hierarchical Production Planning System in the Motor Industry, Omega 15 (1987) 113–120.

[9] H. Tsubone, M. Anzai, M. Sugawara, and H. Matsuura, Interactive Production Planning and Scheduling System for Flow-type Manufacturing Process, Engineering Costs and Production Economics 16 (1991).

[10] H. Tsubone, H. Matsuura, and M. Kanda, Interactive Due, Management System, OMEGA 20 (1992).
