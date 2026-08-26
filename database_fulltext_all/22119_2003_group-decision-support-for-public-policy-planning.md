---
otero_id: 22119
otero_key: "DT6CRFS3"
title: "Group decision support for public policy planning"
authors: "Willem J.H. Van Groenendaal"
year: "2003"
journal: "Information & Management"
doi: "10.1016/s0378-7206(02)00044-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Group decision support for public policy planning

Willem J.H. Van Groenendaal

Department of Information Systems, Tilburg University, P.O. Box 90153, 5000 LE Tilburg, The Netherlands

Received 21 January 2000; received in revised form 13 November 2001; accepted 27 April 2002

## Abstract

Decision support often focuses on substantive rationality (what to choose). The procedural rationality (how to choose) of the process of long-term strategic decision making is then often neglected. In strategic decision making, supporting the decision process is more important than supporting the search for an ‘‘optimal’’ solution to the problem, especially since for most policy problems a well-defined objective function does not exist. Such a problem occurs in setting the energy policy for the Indonesian island of Java. Indonesia wants to introduce natural gas into the fuel mix. Ways to support this decision making process with the existing level of IT were analyzed. Because the government of a developing country has very small funds to invest, a specialized group decision support system (GDSS) was designed to allow for long-term support. Its restrictions are discussed here. <sup>#</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Group decision support; Public policy support; Satisficing behavior; Decision logic

## 1. Introduction

Coordinating decision making in policy planning is a major problem for every government. Because of the potentially large efficiency gains, this holds especially for developing countries. Issue areas range from industrial development, energy supply and demand, to education and defense [16]. Some are strongly related, for example, industrialization and energy supply, whereas others are not. Policy planning can be looked upon as a (never ending) sequence of related strategic decisions. A choice limits the range of future options but solves a particular current problem.

The sparse amount of literature on decision support for public administration focuses mainly on the link between the activity level and the related IT-solution.

Strategic decision making as a time consuming process with feedback is neglected; in their evaluation of group decision support system (GDSS) research, Chun and Park [4] do not feel that the time frame of the decision is an important factor, nor do they consider the problem of coordinating a decision process over longer periods. Policy planning and policy evaluation require lots of time, unless there is an immediate crisis. However, here we focus on opportunity problems.

The literature emphasizes the need to invest in a comprehensive and advanced IT-infrastructure to gain advantage. Saxena and Aly even point at the necessity of these investments by rapidly growing developing countries in order to maintain their high economic growth. Bouras et al. [3] show how the Internet a nd Intranet can be used to design policy support. Developing countries, however, lack the financial resources, and therefore, this calls for efficient and cost-effective decision making. Furthermore, a low level of telephone and computer infrastructure, and computer literacy [2] characterizes public administration in a developing country. Therefore, when designing a decision support the available level of IT should, as much as possible, be considered a constraint, in order to minimize the cost of IT investment and, more importantly, the necessity for a comprehensive learning process.

Many frameworks have been formulated to identify differentformsof(group)decisionsupport(see[13,14]). However, these frameworks focus more on the hardware and software, than on the kind of decisions to be taken and their time frame. Views are often limited to decision rooms and computer conference facilities. Policy formulation is characterized by the need for coordination of groups with different and possibly conflicting goals over a long period of time. Governments (as businesses) prefer a policy that leaves as many options as possible open for the future [19].

The process of strategic decision making plays only a minor role in research on decision support [6,7]. Eom identifies many articles and books focusing on IT aspects of (G)DSS, but only a few articles and books that are related to organizational and time aspects of decision making. Only Mintzberg et al. [12] explicitly deal with strategic decision making as a process. So supporting it is not high on the research agenda, despite the fact that it has many fascinating aspects and that improvement has a large impact.

What is there to support? Policy planning or public collective decision making for a particular issue area is characterized by related strategic decisions that must be made simultaneously over time. This process has, however, its own logic due to the many stakeholders, each with its own goals. Simon [17] distinguishes two types of rationality in decision making: substantive rationality (what to choose) and procedural rationality (how to choose). From the application point of view, support of policy planning is in the area of procedural rationality rather than substantive rationality. This support, which leads to better decisions, is sometimes termed prescriptive modeling [1].

Furthermore, any policy planning will, at best, lead to a satisficing solution [9], which is a solution path acceptable (not optimal) for almost all parties concerned. Minzberg et al.’s description of the strategic decision process can be used to guide the formulation of an adequate GDSS concept for long-term policy planning. However, the use of a GDSS for policy planning requires (irregular) decision meetings to agree upon important assumptions or solutions for sub-problems, so an adequate organizational context is needed.

To distinguish the GDSS from other forms of group support, other concepts and techniques have been defined and introduced, e.g. computer supported cooperative work (CSCW) and cooperative decision support systems (CDSSs) [5,10]. Here the term GDSS is used, but due to the nature of the problem, the term CSCW or CDSS would (partly) cover the approach also, because the decision process is supported separately and asynchronously.

A prototype GDSS called GASOP is presented here to illustrate our view of supporting long-term policy planning. It was developed to support the formulation of Indonesia’s domestic energy policy for the island of Java (inhabited by more than 120 million people and the location of over 80% of Indonesia’s non-oil economy). For several years, GASOP has been used to analyze Java’s energy policy [18], but always by a team of consultants in cooperation with their Indonesian counterparts in different ministries. The combined use by several ministries after the consultants left has never been realized, due to an inadequate transfer of knowledge and lack of adequate organizational support. Hopefully, others can learn from this experience.

## 2. Rationality in decision making

In the normative view, it is assumed that decision problems can be generalized and solved in an objective and rational manner. A problem can be translated into a mathematical model, future preferences are exogenous, stable and known with adequate precision, and an objective function can be formulated. Under these conditions an optimal solution can be derived.

These conditions are, however, not met in public collective decision making. March argues, that public decision making is characterized by conflicting objectives representing the values of different participants with no ‘optimal’ solution (see also [15]). A similar view on strategic planning for business organizations was developed by Mintzberg [11]. In his view, strategic planning is not about the actual choice, but a formalized procedure to produce an articulated result in the form of an integrated system of decisions. The role of a DSS or GDSS is to help in formalizing and improving parts of this procedure through the use of IT.

In policy planning, the main problem is in coping simultaneously with the complexity of the problem and of the decision process. Combining adequate lessons from substantive rationality on the one hand and with human and organizational performance rationality on the other has resulted in prescriptive models that are concerned with how organizations (and humans) can make good decisions, and how to train them to make better decisions.

The importance of procedural rationality increases (and that of substantive rationality decreases) with the complexity of the planning problem and it is for procedural rationality that prescriptive support is needed most. In this view, decision support is much more than logically consistent models with single solutions as suggested by [8].

## 2.1. Energy planning in Mintzberg’s framework

During the identification phase, recognition is the process in which decision makers become aware of the fact that there is a problem. Diagnosis is required to order and combine the information that made the decision makers aware that there is a problem. During the identification phase, the Indonesian Government recognized that Indonesia’s gas reserves ought to be utilized more efficiently for the domestic market. Stimuli for this policy issue go back more than ten years and came from many sources. Aiding agencies, such as the World Bank and the Asian Development Bank (ADB), wanted to see an economically efficient use of Indonesia’s indigenous resources. Indonesia’s state-owned gas distribution company PGN wanted to increase its distribution activities to supply the rapidly growing economy. Moreover, other public and private companies urged the Indonesian Government to supply them with natural gas. Finally, oil companies had discovered a number of on- and off-shore gas reserves in the vicinity of west Java and south Sumatra that were not exploited.

Through a number of studies by consultants, these stimuli induced what, in Mintzberg et al.’s framework, is called recognition and diagnosis of the problem.

These lead to the development phase that results in one or more solutions to the problem. However, because there are no readymade ones, the design of a long-term energy policy (including investing in a gas infrastructure) is required. This is a complex and iterative process, which would normally result in one or two solutions for the short run (up to 5 years), and a limited number of options for the long-term (25 years). Design offers several possibilities for support and is more than the technical design of a gas transmission system. It involves modeling the potential markets, developing a consistent energy pricing policy, reviewing the gas reserves and related supply possibilities, identifying branch line investment projects, and designing regional gas distribution infrastructures. The technical design requires a team of specialized engineers that develop a number of possible solutions, guided by the designed demand forecasts, pricing policies, etc. This process is iterative, the feasibility of meeting demand in different geographical areas and/or economic sectors depends on the cost of the infrastructure. (Note that design may require reentering the identification phase, because new or insufficient information is available.)

All major design activities (market analyzes, pricing policies, etc.) can be supported. The overall policy design can be factored into a set of related design subproblems that must first be solved. The solutions to sub-problems are then combined to search for a clearer view of the total problem and failure at any point leads to iteration.

The next phase is the selection phase, in which all information is coupled and evaluated and in which, through bargaining between the parties, solutions for different sub-problems emerge. If a solution for a subproblem is authorized, it becomes a fixed input for the remaining problem.

As the technical design (or designs) become more and more mature, the analysis focuses on the financial and economic net present values of the investments, the amount of foreign exchange required, the debt– service ratio, investment schedules, the selection of admissible demand categories, and the corresponding energy pricing policy.

Such a process lead to a limited set of ways to introduce natural gas in Java’s fuel mix. These were then proposed to the Indonesian Cabinet, which chose one. The solutions also indicated what other decisions had to be prepared, for example adjustment of the energy pricing policy (which started the social unrest in 1997).

## 3. Energy policy decision process

Policy planning in the field of energy is a sequence of (almost) irreversible decisions, especially when any one leads to a substantial investment. In this section, we briefly describe the problem at hand, which is a typical example of public policy planning, the problem environment and its dynamics.

## 3.1. The decision problem

The immediate reason to adjust Indonesia’s domestic energy policy was the fact that natural gas was available domestically, but most industries used imported oil products. These oil products were heavily subsidized, costing the Indonesian Government billions of US dollars annually. For this reason, the Indonesian Government wanted to replace the imported oil products by domestic natural gas.

For historical reasons, gas was only used in some low value added energy intensive industrial processes, namely, feedstock to produce nitrogen fertilizer and steel and in some power plants. These applications were, however, only profitable if gas was cheap.

Because of the spatial distribution of the gas reserves, the development of a substantial market for gas was required before it would be profitable to connect Java to reserves further away. For this, the limited gas reserves in the vicinity of Java could be used. Therefore, the Indonesian Government wanted to know in which markets/applications the gas was most beneficial to the economy.

## 3.2. Policy coordination structure

The Ministry of Mines and Energy (MoE) coordinates Indonesia’s energy policy. Its goal is to support a technically, financially, and economically efficient energy mix for all sectors of Java’s economy (households, industries, power).

Before GASOP was used, the Ministry of Industry (MoI) wanted to use natural gas as cheap input for some large energy intensive industries (petrochemicals, steel)

to induce further growth in these sectors. They expected that the total economy would benefit through exports and import substitution.

The state-owned electricity company PLN, promotes natural gas for the production of electricity for intermediate and peak loads. PGN wanted the gas for its industrial customers who currently use oil products, and because natural resources belong to the government, the Indonesian state-owned oil and gas company PERTAMINA was a major cash cow for the Indonesian Government.

It was not clear what usage of gas would be most beneficial to the economy. Selling gas at higher prices to high value applications leads to higher income from domestic sales and a more competitive domestic industry, whereas selling gas at a low price to energy intensive industries induces indirect income through exports and import substitution.

Every one of the goals can be achieved through Indonesia’s energy policy, but not all at the same time. Every related problem (how to achieve the goal) has a ‘champion’ or ‘most interested party’. Other participants may, however, have a special interest in the achievement of a champion’s solution. A case to point is the interest that the Ministry of Agriculture (MoA) has in the production of a specific gas based chemical, viz. nitrogen fertilizer. The MoA considers a sufficient supply of fertilizer a cornerstone for a successful food policy. Thus, it has a common interest with the Basic Chemicals Department within the MoI.

One thing is clear, achieving all goals at the same time is not possible, and there is no method or methodology that allows us to find ‘the solution’. Supporting and coordinating the policy development process is the best that can be achieved. Here, the use of GDSS can make a difference.

## 3.3. The problem environment

Changing Java’s fuel mix is related to a number of other policy issues, such as, energy pricing, economic development and its geographical distribution, industrial policy, environmental policy, and exploitation and exploration of new reserves. These policies need to be coordinated with the energy policy, but every one of them is characterized by its own problems, e.g. due to subsidized prices of oil products that do not reflect the real cost of energy to the economy, energy is used inefficiently, while the environment is unnecessarily polluted. However, quick adjustment of the energy pricing policy meets with strong opposition by residential and industrial consumers, and for steel making and the production of nitrogen fertilizer the subsidies are protection from international competition.

Public administration in a developing country is also ‘highly bureaucratized and extremely centralized’. This makes the formulation of a policy for a complex problem even more difficult. At every level there are inter- and intra-group negotiations. Also, alliances will be formed to achieve particular goals.

There are groups with a less prominent interest in the problem also. The Ministry of Planning (MoP), responsible for the long-term economic plans and growth scenarios, and the Ministry of Finance (MoF) that analyze the effects of the proposed solutions on the budget and on the country’s debt–service ratio will reject them if they are deemed insufficient.

In a volatile economy, a policy decision often lags behind. By speeding up the support processes, the introduction of IT in the form of multilevel group support can improve decision making.

Most literature on GDSS has as a premise that decision makers want to formulate goals they all can support, and that they can use IT to find a solution that meets these goals. Our characterization of the problem of policy planning shows that this view does not fit. Groups have conflicting goals and will not change their view in such a way that their goals will be in line with the goals of other groups. Depending on the importance of a particular goal, a group will, however, concede at a certain point in time and at an appropriate, but not complete, level of goal fulfillment.

## 3.4. Decision dynamics

Energy policy planning is a dynamic process with interrupts, feedback loops, delays, and speedups. There are two basic dynamic aspects: changes in the group of those who have a key interest in the policy (Mintzberg’s political activities), and maintaining consistency over time between successive decisions (decision control and decision communication).

Changes in the composition of the group can result from work already done or decisions already taken. For example, after the Indonesian Government decided to supply gas to refineries in west Java, the refineries and the related department in the MoE lost interest in the problem and were no longer active in policy planning.

Maintaining consistency in assumptions and intermediate results is required to avoid mistakes. For example, the planning of industrial estates and the planning of gas and electricity transmission must be coordinated. This is not always the case, resulting in mis-investments and the loss of potential foreign investments. Good organization and IT-support can help to avoid this.

## 4. GASOP: a multilevel GDSS for policy planning

Thus, every group involved in policy planning has a special interest in and specific knowledge of part(s) of the policy issue, or has an interest in other policy decisions that are affected by the policy to be formulated. This supports the statement that there is no single optimal solution for all related problems. What is needed is a GDSS that allows every sub-group to analyze its own sub-problem and to formulate policy proposals, taking into account the policy proposals of other groups with respect to related sub-problems. All policies need then to be coordinated to formulate a comprehensive and consistent planning for the total problem. Therefore, the system has to fulfil the following criteria:

(i) every sub-problem of the planning should be supported by a (G)DSS for the sub-problem’s ‘champion’;

(ii) to support their own decision process, other groups must have access to the solutions or planning proposals formulated by other groups;

(iii) because some sub-problems are more closely linked than others, several levels of coordination have to be organized.

Depending on the issue, the coordination needs structural support, for example, energy pricing, or temporary support, for example, where to employ natural gas. If the latter problem is chosen, it needs no more specially organized coordination between potential gas users.

## 4.1. The GDSS GASOP

To support the formulation of a long-term energy policy for Java a computerized GDSS, called GASOP, was designed (see Fig. 1). GASOP contains subsystems that are either a DSS or a GDSS to support the discussion on particular sub-problem by specific groups. For example, IRON and STEEL supports decision making on energy supply for iron and steel production in the MoI and POWER determines the optimal long-term fuel mix for power generation. Furthermore, every (G)DSS allows for comprehensive what-if analysis.

![](/api/attachments/DT6CRFS3/fulltext/images/bdf8e1d8fb4e4baafaf94ac01414996f6b848d2cd8cdb713f591fc90c0aa98b4.jpg)  
Fig. 1. Outline of GASOP.

Every (G)DSS-module contains:

(i) A user interface to communicate input data, to set decision variables, and to introduce policy options.

(ii) A system of one or more (simulation) models describing the actual situation for a policy area and all relevant information. The system is used to evaluate the effect of the choices made under (i) and has links to those parts of GASOP that contain relevant information.

(iii) An output system that allows the users to look at results in detail or in graphical form, and with some basic management report facilities.

The user interfaces in GASOP are equipped with some intelligence. First of all, the system checks whether an option introduced, or a choice made by the user is admissible. If not, the inconsistency is communicated to the user. Furthermore, if a combination of input data and/or other options is unlikely from a technical, financial or economic point of view, the user interface will point this out and ask the user if this is what he/she really wants. If so the choice is accepted, but with a warning.

To ensure that the same assumptions on economic and geographical growth scenarios and energy prices are used, there are two modules that contain agreed upon options and current policies (GENGDP and PRICES). This is the first sub-problem (indicated as Level 1). It results in a number of possible energy pricing policies (including no change), and an agreed upon set of scenarios for future economic development (geographically and in time). This information can also be used by groups looking at other problems, such as the planning of electricity transmission and of highways. In this way, the assumptions in the preparation of different policy issues can be coordinated and made consistent.

The GDSSs on the second level can be used to analyze the various sub-problems. In some cases, for example, the DSS for the power sector (POWER) optimization methods (linear programming) are used as well as simulation to derive a solution for the subproblem: the least cost fuel mix for the power sector. The detailed results of short and medium term planning and forecasting by (say) PLN can be introduced also and a consistency check can be performed.

In every block, the main responsibility for a module is indicated along with the other most interested parties. When a solution for a particular sub-problem is decided, this solution is communicated to the level above, which automatically uses the results of the analyses of the other groups.

Previously, we stated that several departments within the MoI have an interest in gas utilization. To facilitate discussion within the MoI, separate modules for the manufacturing bulk consumers (FERTI LIZER, BASIC CHEMICALS, CEMENT, and IRON and STEEL), as well as a module for the rest of the manufacturing sector (OTHER MANUFACTURING) were included at Level 2. The results of the modules for bulk consumers can thus be combined to facilitate the decision process within the MoI. The support can be augmented with OTHER MANUFACTURING, to analyze the effect of all plans for the total manufacturing sector. Each module results in the expected fuel mix (the amount of coal, oil products, natural gas) for the particular subsector or set of subsectors, given energy prices and expected sector growth. So GASOP, as every planning support should, coordinates the use of information and the implementation of agreed upon intermediary solutions for sub-problems. Furthermore, the solutions of logically connected but larger subproblems (total manufacturing and power) can be evaluated.

The total fuel mix is obtained by running the module NATECON (Level 3). In SUPPLY and DEMAND, the energy resources and energy demand are confronted. This module is used mainly to evaluate the technical feasibility of demand scenarios, and the effect new reserves will have on investment plans. Only when the market matures will investments in pipelines to tap reserves that are further away become profitable.

The module TRANSMISSION contains different options for pipeline development. The total technically feasible transmission system has been split into logically connected subsystems, which can be considered separately (for example, branch lines to particular demand centers) or can be postponed to later date (for example, connections to gas reserves further away). TRANSMISSION is used to develop and analyze investment options for gas transmission given the results of DEMAND and SUPPLY. For the proposed transmission system, TRANSMISSION calculates the financial and economic cost of planned investments and their distribution over the planning horizon. For the evaluation of the total proposed energy policy, COST/BENEFIT is used; this combines all financial and economic information.

## 4.2. Implementation

The level of IT at the MoE at the time GASOP was developed was low. There was no Intranet, only some LANs within different departments. As a result, GASOP was build using Lotus 123, with every module a separate (set) of spreadsheets. To use GASOP every department involved in the formulation of energy policy had to have a copy of the software. Maintaining the official (agreed upon) version of the software was the responsibility of the MoE-consultants. A department or ministry and the consultants developed solutions to sub-problems, but only after consultation and decision makers at different levels could agree upon the changes or assumptions to be introduced in the official version of GASOP. Changes in the government’s level of IT were not required and only a limited investment was needed in additional schooling. The main problem was coordinating the activities of the different groups supported by GASOP. Indeed, this is where the project failed.

## 4.3. Decision support organization

To facilitate the correct use of the support GASOP can give, regular and irregular meetings were organized. Every 3–6 months, representatives of the different departments (up to the director-generals of the most important ministries) met to discuss proposed solutions to sub-problems. During a meeting, proposals were ranked and decisions (re)formulated. After authorization, decisions were implemented in the official version of GASOP, e.g. a decision not to increase the amount of gas for Java’s major steel factory and a nitrogen fertilizer plant in west Java. Also, new sub-problems that had been identified were discussed and possible strategies evaluated.

Representatives of all major stakeholders participated in the general meetings, which could last for several days. There were also many irregular meetings of small groups, the composition of these depended on the problem at hand and the stage of a proposal. A group would use GASOP (or the results obtained with GASOP) to analyze a sub-problem and evaluate a variety of proposals. One or more consultants were always present at these meetings, which could be within a department, between departments, or between ministries, but also with representatives of the industry. In this way, the political feasibility of the proposals was tested. A solution proposed by the ‘problem owner’ was communicated to others to allow them to evaluate the effect of this proposal on their own analyzes. However, only in general meetings were decisions put to the test, after this, all parties had to accept the decision. Before this, a party could have protested at a higher organizational level, but, given the many prior discussions, this never happened.

## 5. Results

The results obtained with GASOP have had an impact on the formulation of Java’s energy policy and were used to resolve a number of important issues, but also raised several new ones.

GASOP was used to rank demand categories. For the first time, the Indonesian Government became aware that it was not profitable to serve all customers, and that energy intensive ones (nitrogen fertilizer, iron and steel, cement) should not be developed at the expense of the rest of the manufacturing sector: they were neither financially nor economically viable. The Indonesian Cabinet decided to use Java’s scarce gas reserves in high value industrial applications (served mainly by PGN), and in some forms of power generation.

The use of GASOP has, for the first time, made the Indonesian Government aware of the fact that Indonesia’s commercial gas reserves are limited and that the issue of gas export or domestic use needs further consideration. Since Indonesia is the largest exporter of LNG in the world, the Indonesian Government assumed that there was sufficient and affordable gas available for the domestic market also. It was shown that, due to the spatial distribution of Indonesia’s gas reserves and the long-term export contracts, this is not true.

It was also shown that the information on the gas reserves in the vicinity of Java is unreliable and should be updated before substantial investments are made. As a result these reserves are under study. Several of the investments to improve the current grid have been realized over the past years. With new findings in Sumatra, a connection between west Java (where most industry is located) and south Sumatra has been found to be an effective investment, the Japanese Government will supply a soft loan for this.

Also Indonesia’s gas law has been changed as a result of support of the planning process. According to the previous energy law, investments in gas transmission could only be made by PERTAMINA. Historically, this state-owned company’s main task was negotiating with foreign oil companies and executing/monitoring the export contracts signed by the Indonesian Government. As a result of this focus, the emerging domestic market was neglected. To foster the domestic market, the government has allowed the gas distribution company PGN to invest in gas transmission pipelines to supply its distribution networks.

GASOP has also helped to convince the Indonesian Government to adjust its energy pricing policy; prices were adjusted to be more in line with the economic cost of the different fuels and the rates will be further adjusted in the future. This issue was, however, already high on the political agenda due to the efforts of the World Bank and the IMF. GASOP has proven to be a valuable tool for the asynchronous support of the energy policy planning process. In this respect, working with GASOP can be qualified as CSCW that improved the quality of the decisions.

Did the use of GASOP speed up the decision process? This is a question that cannot be answered, since there is no alternative information. The system in combination with the policy formulation process has, however, lead to a different view within many government bodies on Indonesia’s domestic energy policy. But others (industries, oil companies, etc.) have used the results. New roads for policy planning have been discovered.

## 5.1. Drawbacks

Is GASOP a success? Are there no drawbacks? As always, there are. The proposed use in various ministries has never occurred. For three years the system was used for policy evaluation and formulation, but always with the help of consultants hired to support the development of a new energy policy. After the consultants left, only parts of GASOP were used, and these not as originally intended. Only the MoE and the gas distribution company PGN actually used (parts of) GASOP. PGN for its marketing strategy, using the detailed information on the value of gas in various production processes.

Although a transfer of knowledge was conducted, insufficient attention was paid to this aspect. Also, the organizational setting was problematic. During the time the consultants were working on the problem, there was support by the various ministries. After the consultants left the MoE was mainly responsible for GASOP. For the civil servants in other ministries, the MoE is seen—at least to some extent—as a competitor rather than as a co-worker. Insufficient attention was paid to define an adequate intra-ministerial organizational structure, with clear responsibilities and sufficient high level support. It was mistakenly assumed that the clear advantages of the system, which were sufficiently demonstrated, would be convincing enough. Thus, the support by the consultants failed. A better organizational setting would have made the system more beneficial.

That the concepts embodied in GASOP are considered valuable is, however, broadly recognized. In 1998, the ADB formulated a technical assistance project, that is, donated money, for a revamp of the original energy policy study and the related software modeling concept. The scope has, however, been downsized. Hopefully, more attention will be paid to the transfer of knowledge and the organizational setting.

## 6. Conclusions

Policy formulation for strategic issues is a difficult, time consuming and a never ending process, involving many government bodies and other stakeholders. Each has its own goals, that often conflict with those of others. To ‘solve’ this problem, the development of a hierarchical GDSS to facilitate the long-term decision process (how to choose) is more appropriate than trying to formulate an oversimplified normative model that allows the calculation of an ‘optimal’ solution (what to choose). Such a GDSS can be looked upon as a prescriptive model (to improve the decision making process), not as a model that results in ‘the’ decision.

The aim of this paper was to give an impression of how policy planning can be divided into subproblems, how these sub-problems are connected, and how the decision making process in a developing country can be supported without expensive investments in IT and human resources. The modular structure of GASOP allowed the different groups to concentrate on their own sub-problems, coordinating at the same time, the solutions for particular subproblems so far and making sure that everyone used the correct inputs.

By connecting solutions for sub-problems and evaluating their effect, an energy policy for Java was obtained that was better communicated, and therefore, better understood. It was through bargaining between the ‘owners’ of the different sub-problems that this satisficing policy formulation was reached. Through this process, a clear picture of all issues emerged. It allowed the Indonesian Government to improve the quality of its decisions on energy-related problems and domestic gas utilization. The GDSS GASOP was instrumental in revealing a number of policy issues, that had been neglected or had not been identified. These issues are now on the political agenda, policy planning is a continuous and time consuming process demanding an adequate organizational setting.

## References

[1] D.E. Bell, H. Raiffa, A. Tversky, Descriptive, normative, and prescriptive interactions in decision making, in: D.E. Bell, H. Raiffa, A. Tversky (Eds.), Decision Making: Descriptive, Normative, and Prescriptive Interactions, Cambridge University Press, Cambridge, UK, 1988.

[2] S.J. De Boer, M.M. Walbeek, Information technologies in developing countries: a study to guide policy formulation, Information Management 19 (3), 1999, pp. 207–218.

[3] C. Bouras, P. Destounis, J. Garofalakis, V. Triantafillou, G. Tzimas, P. Zarafidis, A co-operative environment for local government: an Internet–Intranet approach, Telematics and Informatics 16 (1/2), 1999, pp. 75–89.

[4] K.J. Chun, H.K. Park, Examining the conflicting results of GDSS research, Information and Management 33 (6), 1998, pp. 313–325.

[5] B. Daily, A. Whatley, S.R. Ash, R.L. Steiner, The effects of a group decision support system on culturally diverse and culturally homogeneous group decision making, Information and Management 30 (6), 1996, pp. 281–289.

[6] S.B. Eom, Mapping the intellectual structure of research in decision support systems through author citation analysis (1971–1993), Decision Support Systems 16, 1996, pp. 315–338.

[7] S.B. Eom, The intellectual development and structure of decision support systems, Omega, International Journal of management Science 26 (5), 1998, pp. 639–657.

[8] R.A. Howard, Heathens, heretics, and cults: the religious spectrum of decision making, Interfaces 22 (6), 1992, pp. 15–27.

[9] J.G. March, Bounded rationality, ambiguity, and the engineering of choice, in: D.E. Bell, H. Raiffa, A. Tversky (Eds.), Decision Making: Descriptive, Normative, and Prescriptive Interactions, Cambridge University Press, Cambridge, UK, 1988.

[10] H. El Mansouri, A. Alquier, P. Zarate, A multi-agent model for decision oriented cooperative systems, in: Proceedings of the 2nd International Conference on the Design of Cooperative Systems, INRIA, Rocquencourt, France, 1996, pp. 357–373, ISBN 2-7261-0980-2.

[11] H. Mintzberg, The Rise and Fall of Strategic Planning, Prentice-Hall, New York, 1994.

[12] H. Mintzberg, D. Raisinghani, A. Theoret, The structure of the unstructured decision processes, Administrative Science Quarterly 21, 1976, pp. 246–275.

[13] J. Morison, O.R. Liu Sheng, Communication technologies and collaboration systems, Information and Management 23, 1992, pp. 93–112.

[14] M.A. Nour, D. Chi-Chung Yen, Group decision support systems: towards a conceptual foundation, Information and Management 23, 1992, pp. 55–64.

[15] Organisation for Economic Cooperation and Development (OECD), Project and Policy Appraisal: Integrating Economics

and Environment, Organisation for Economic Cooperation and Development, Paris, France, 1994.

[16] K.B.C. Saxena, A.M.M. Aly, Information technology support for re-engineering public administration: a conceptual framework, International Journal of Information Management 15 (4), 1995, pp. 271–293.

[17] H.A. Simon, Rationality as process and as product of thought, in: D.E. Bell, H. Raiffa, A. Tversky (Eds.), Decision Making: Descriptive, Normative, and Prescriptive Interactions, Cambridge University Press, Cambridge, UK, 1988.

[18] W.J.H. Van Groenendaal, The Economic Appraisal of Natural Gas Projects, Oxford University Press, Oxford, UK, 1998.

[19] W.J.H. Van Groenendaal, J.P.C. Kleijnen, On the assessment of economic risk: factorial design versus Monte Carlo methods, Journal of Reliability Engineering and Systems Safety 57, 1997, pp. 91–102.

![](/api/attachments/DT6CRFS3/fulltext/images/970021e18ef42d1fd003fa371645e6b43d2837af3366d31cc14473a1db2010f3.jpg)

Willem J.H. Van Groenendaal is associate professor at the Faculty of Economics and Business Administration, and fellow of the Center for Economic Research (CentER), both within Tilburg University, The Netherlands. His research interests focus on decision support, policy formulation, and investment analysis. He also works as a consultant for international development agencies.
