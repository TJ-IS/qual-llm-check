---
otero_id: 27049
otero_key: "KJR6STZ9"
title: "Information Intensive Modeling"
authors: "Levent Orman"
year: "1987"
journal: "MIS Quarterly"
doi: "10.2307/248828"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Information Intensive Modeling
Author(s): Levent Orman
Source: MIS Quarterly, Vol. 11, No. 1 (Mar., 1987), pp. 73-84
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248828
Accessed: 08/05/2014 18:12

Accessed: 08/05/2014 18:12

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Information Intensive Modeling

By: Levent Orman
Cornell University
Graduate School of Management
Ithaca, New York

## Abstract

The interaction of formal information systems and organizational decision models will be examined in this article. It is conjectured that decision models and processes not only determine the information requirements, but that they are influenced by the organizational information systems that are designed to support them. This type of circular relationship between the decision models and the information systems undermines the success of requirements analysis which traditionally views information systems as supporting structures for the decision models, and ignores their counter effect on the decision models. Four different examples are presented to demonstrate the effect of information systems on organizational decision models. The examples range from algorithmic to highly unstructured and speculative, but they all suggest that information-intensive models are qualitatively different from their information-poor counterparts.

Keywords: Information requirements analysis, model management, decision models

ACM Categories: D.2.1, H.1.1

## Introduction

Information is a costly commodity. Many decisions, both personal and organizational, are made without complete information due to its high cost. Many factors contribute to the high cost of information. Raw data have to be collected, stored, and processed; requiring sensory agents, memory, processing capability, and display and transportation media respectively. The computational models needed for processing data have to be generated, which requires analytical talent and insight; they have to be linked to their data and executed, which requires processing; and results have to be interpreted, which requires further processing to link to other data and models. Consequently, the cost of information in general includes not only the costs associated with the collection, storage, retrieval and transportation, but also with both the human and machine processing to make it available in the right form and at the right time. Not surprisingly, considering all these costs associated with information, it is rarely optimal to allocate the necessary resources to the acquisition of complete information for any specific decision. Consequently, less than complete information is the norm in decision sciences rather than the exception [23]. Obviously, there are degrees of incompleteness, and the decisions will be characterized as relatively “information poor” or “information intensive,” depending on the amount of information utilized to reach the decision.

Information poor decisions are not necessarily suboptimal from an organizational point of view since the cost of information is a crucial factor in determining how decisions are made and what information is used. Many seemingly suboptimal decisions turn out to be the optimum strategies for the organization as a whole when the cost of information is factored in. The apparent irrationality of a mid-level manager in insisting on using simple heuristics instead of proven optimum analytical models, or of a government bureaucrat in refusing to grant exceptional treatment no matter how badly his standard rules apply to a particular case, are all attempts to reduce the cost of information and may very well be the overall optimum behavior.

Under a given cost function, a relatively information poor decision process may represent the optimum behavior for the organization, but the decision itself is usually much less than optimum. In other words, a mediocre decision may be the best that can be done, given the cost of information. There is actually some empirical evidence to suggest that under some information overload conditions the cost of information processing is so overwhelming that large quantities of information may be discarded randomly or without adequate consideration [15, 17, 44, 46].

An obvious strategy to improve the quality of decisions then is to lower the cost of information. One approach to lowering the cost of information involves sharing mass produced and centrally controlled information $[44, 55]$ . Sharing information is very effective because information is an unusual resource whose consumption does not reduce its available quantity. Large-scale, organization-wide sharing is usually made possible by employing a single, centrally controlled information system which collects, processes and disseminates information for the whole organization. Mass production is effective since it takes advantage of economies of scale and encourages productivity through specialization. The strategy worked remarkably well in industrial production and it appears promising also in information production. The bureaucracies of modern organizations can be viewed as information factories where specialization of each agent, and mass production for the whole organization, considerably lowers the cost of information. Formal computerized information systems are also attempts in the same direction to increase organizational sharing through central control and mass production by specialized staff and machinery.

However, information is an elusive commodity. What information to produce to meet the needs of a large complex organization is not always obvious, and sharing through central control exacerbates this problem by centralizing the decisions about requirements. The field of 'requirements analysis' attempts to determine the future information needs of organizations [16, 36]. However, the information needs of organizations are not static. They change in response to environmental and organizational pressures, and the requirements analysis often fails to properly take into account the dynamics of the organization [32]. More damaging to the requirements analysis is the possibility that the very introduction of a formal information system may cause changes in the information needs it is trying to meet by changing the cost and availability of information. Since the cost of information usually is a crucial factor in determining the optimum decision process, a reduction in the cost of information may influence how the decisions are made and what information is used to make them, or at least it may render the current decision models suboptimal. Consequently, an information system is not likely to succeed by simply studying and meeting the current information needs of decision makers without taking into account its own impact on the decision models.

This may be but one explanation of why systems analysts are often bogged down by the changing requirements of managers, even in fairly static organizations [32]. If proved correct, the implications of this assertion for system design, in particular for requirements analysis and the design of decision support systems, are profound. It suggests that information systems should be designed not on the basis of a purely descriptive requirements analysis as widely practiced, but either on a more prescriptive basis or through an expanded descriptive analysis that includes the effect of the information system itself on the information requirements. $^{1}$

The implications for decision support systems are even more drastic. Current research efforts in decision support systems attempting to incorporate the decision models of organizations into their information systems are likely to fail if the effect of the very existence of a decision support system itself on the decision models is not considered. This circular relationship between the decision models and the information system which maintains those models may even require the investigation of the second or the third order effects, or even the more complicated search for an equilibrium point before decision support systems can be successfully introduced.

This article will examine four diverse examples to demonstrate the basic assertion that this influence widely exists and is significant. The examples cover a wide spectrum of decision models, ranging from the most straightforward and structured decisions involving inventory control to the most complex and unstructured decisions of voters in a representational democracy. The discussion also ranges from algorithmic to speculative, following the nature of the examples. The last section suggests some information system design strategies that might overcome the problem of circular relationship. The potential of these strategies for success is briefly discussed.

## Inventory Control

Among the best understood and structured organizational decisions are inventory control, and in particular, inventory reorder decisions. Many useful algorithms exist to optimize and automate these decisions. Ordinarily, one would not expect qualitative changes in optimizing models as the information system changes. Surprisingly, even the well structured and completely optimized models are affected by the changes in information systems, although the effect is not as striking as it is with the more heuristic human decision models and are usually limited to the error terms resulting from the imperfectness of information.

The early studies in economic order quantities and the optimum timing of inventory reorders assumed perfect information at no cost [33]. These assumptions were relaxed in later research since it was obvious that physical inventory taking was a costly endeavor and the inventory data obtained was rarely perfect. Two major sources of error were the human errors introduced during the physical inventory count and the errors in sales estimates used to determine the inventory levels in between the inventory counts. These errors could be reduced by increasing the frequency of inventory counts and using multiple counts each time, but only by increasing the cost of information. Consequently, under optimum scheduling of inventory counts these two sources of error remained highly significant and the models based on periodic inventory counts had to account for the errors in inventory level data. The errors in either direction were costly since they resulted in either stockouts or excess holding costs. The models had to discover the appropriate probability distributions for these errors and include the corresponding costs in the computation of the optimum reorder quantities [52].

The optimum reorder quantities were found to have changed significantly from the perfect information models and the change was due to the asymmetry of the probability distributions with respect to the two types of errors and the cost difference between the possible stockouts and excess holdings. For example, in situations where errors always result in overestimates of inventory due to double counting, and the stockout costs are much higher than the holding costs, the optimum reorder quantity would have to be adjusted upwards to compensate for the errors $[25]$ .

An information system based on data capture at the point of sales, as opposed to periodic inventory count, leads to a different model since the sources of error are quite different. The two sources of error associated with the periodic-inventory-counting information system are eliminated. The human errors resulting from physical stocktaking are eliminated because the process of stock taking is replaced with a perpetual inventory system. The errors resulting from the sales forecast are eliminated since the inventory levels are not estimated using the sales forecast but computed from the actual sales. Consequently, the models have to be changed to eliminate all considerations of these errors in computing the optimum reorder levels.

Moreover, the models may have to be changed further to take into account new sources of error. The data capture at the point of sales also involves human error. These point-of-sales errors are different than the inventory count errors, and they have been shown to have extremely skewed probability distributions since the unfavorable errors are corrected by the customer more frequently than the favorable ones. Consequently, these errors have very different probability distributions than the inventory count errors and they must be modeled differently. Another new source of error is due to the different treatment of the shrinkage and pilferage of inventory. Point of sales systems suffer from cumulative errors due to these sources since they exclusively rely on sales to compute inventory levels and treat other losses statistically. The estimation of these losses involve quite different models in point of sales systems than in inventory count systems since the latter periodically correct for these errors [51].

It is safe to assert that even the optimizing models are not completely independent of information systems due to imperfectness of information, and the models that are sophisticated enough to take into account data errors would have to adjust to changes in information system. Consequently, a transition from one information system to another cannot merely be based on a descriptive requirements analysis, otherwise the new system will continue to provide data for the error models of the previous system which will be rendered obsolete by the introduction of the new system. A decision support system is even more vulnerable since it actually maintains and controls these error models and it would continue to use them until they are explicitly replaced.

## Urban Transportation

More striking examples of the influence of the information system on the decision models can be obtained by moving away from optimizing models into the arena of heuristic models. A wealth of examples employing both optimizing and heuristic models can be found in urban mass transit systems. One of the most widely studied problems in transportation is the routing and scheduling of mass transit vehicles, in particular the city buses. Many standard algorithms exist for solving the deterministic routing-scheduling problems by maximizing customer satisfaction and minimizing the route length within the constraints imposed by vehicle capacities and crew scheduling requirements $[4, 11, 19]$ . However, the stochastic demand faced by mass transportation systems complicates the problem considerably because of the non-linearities introduced by the probability distributions. Almost all stochastic routing and scheduling models are heuristic in nature, although the objective of maximizing the customer satisfaction and minimizing route length remains the same. All stochastic models for scheduling mass transit vehicles require an information system that provides probability distributions for the number of passengers on each possible route in each time period, and their destinations and other preferences. These probability distributions are based on the past demand for similar services and perhaps additional customer surveys. A typical solution involves heuristics to reduce the stochastic problem to a deterministic problem, and then uses one of the optimizing algorithms such as integer programming or network analysis to generate the complete schedule. Once the schedule is generated, it is fixed for at least the next period of time, if not the whole lifetime of the system. [21].

An information system which allows customers to register (by phone) their actual transportation needs for the next time period may lead to a completely different formulation of the same routing-scheduling problem, and even to a different type of transportation system. The phone-in system may have been developed to provide a better forecast of the customer demand for the next period by basing it on real data rather than the estimates based on historical data. Yet, as in the inventory control example, the availability of real data may lead to much more than the expected minor improvements in the quality of decisions and the elimination of some statistical forecast procedures. It may lead to the adoption of completely new and different decision models.

Once developed, the phone-in system can be used to collect real time data where customers phone in their transportation requests at the time of actual need, and their requests are serviced in real time by a flexible-route transportation system. Once the information system is in place, there are incentives to extend the fixed-route, fixed-schedule service into a real-time, door-to-door public transportation service, since a system of this sort leads to higher customer satisfaction due to the door-to-door nature of the service, and may lead to a more efficient use of resources due to the elimination of idle travel time with no passengers. These systems are generally referred to as demand responsive dial-a-bus systems $[10]$ .

The decision models in this new environment are drastically different and may actually be easier to solve than the fixed-route, fixed schedule model because of their deterministic nature. The real-time dial-a-bus problem lends itself to incremental optimization since the real data arrives in real time in small increments. The incremental procedure provides at each point in time a temporary solution and as the environment changes (e.g., with the arrival of a new request) the changes are incorporated into the solution in real time. This incremental approach basically transforms a single large stochastic optimization problem into many small easily-solvable deterministic optimization problems, the latter being preferable once the supporting information system is in place [10, 43, 53]. Evidently, an information system developed to enhance the performance of the existing decision models might lead to drastically different decision models and even a different transportation system.

## Administrative Bureaucracy

Bureaucratic hierarchies are useful in economically processing large quantities of information and hence improving organizational decisions. Viewed as information processing systems, bureaucracies can be shown to lead to different decision models than their predecessor structures. Moreover, the various proposals involving the computerization of bureaucracies by introducing formal information systems have been predicted to significantly change the organizational decision models. Both of these assertions strongly support the thesis of this article.

Bureaucracies are common organizational structures both in the public and in the private domain. They increase the ability of an organization to deal with complex decision models and large quantities of data and hence improve the organizational decisions $[6, 29]$ . They accomplish this objective mainly through an hierarchical structure. The hierarchical structure of bureaucracies facilitates information flow both upward and downwards in the hierarchy while severely restricting lateral and multi-level communication, thus leading to specialization of individual agents and mass production of information. Specialization and mass production lead to a reduction in the cost of information as they did to the cost of products in industrial production, and make it possible to incorporate higher quality and quantity information into the decision making process [6, 57]. Bureaucratic hierarchies accomplish specialization and mass production by summarizing data upward in the hierarchy (protecting higher levels from the masses of data) and decomposing goals into subgoals downwards in the hierarchy (simplifying the decision models at each level and protecting each agent from the awesome task of relating his decisions to the overall organizational goals). The resulting tasks at each level are simple, narrow decisions based on minimal but highly relevant data, hence the specialization of individual agents [57].

Bureaucracies clearly provide a significantly different information processing system than their predecessors. Consequently, according to our hypothesis, they are also likely to employ different decision models for the same organizational decisions. There is considerable evidence that bureaucracies make decisions based on much simpler rules and procedures than non-bureacratic organizations, and they are much more reluctant to make exceptions to these simple rules to take into account the unique characteristics of each problem they face $[24, 57]$ . After all, the decomposition of the complex organizational goals with large quantities of organizational data into simple procedure rules with minimal abstract data, at each level of the hierarchy, is what characterizes bureaucracies. This is the very reason why bureaucracies can cope better with a complex, information-intensive environment than previous organizational structures where each individual agent may be exposed to the full complexity of the organizational decisions and complete data about the organizational environment.

The evidence here is inconclusive as to the direction of influence since it is not clear whether the change in information system was the cause or the effect of changes in the decision models during the process of bureaucratization. To elicit that evidence the process of bureaucratization has to be analyzed, as opposed to bureaucracy as the final product. The ecological theory of bureaucracies provides such an analysis and supports our thesis by suggesting a circular relationship where individual components evolve by reacting to each other and the environment in small increments $[29]$ .

Further evidence about the circularity of the relationship between the information system and the decision models is provided by the introduction of computerized formal information systems into bureaucracies. Computerized formal information systems have been proposed to remedy some of the shortcomings of administrative bureaucracies. Among the major shortcomings are the following:

a. Bureaucratic hierarchies, although they tremendously increase the information processing capabilities of organizations, cannot be expanded indefinitely. Their depth is limited by the extent of distortion and delays the organization can tolerate as the information moves up and down the hierarchy. Their breadth is limited by the information processing ability of each agent in the hierarchy since each agent has to oversee his immediate descendants by summarizing the data upwards and by decomposing the goals downwards, and comparing the goals and reports to assess the performance of his immediate subordinates. As the organization grows to take advantage of the economies of scale in information production (among other reasons) the bureaucracy reaches its limit of effectiveness [6, 50].

b. Each agent in a bureaucratic hierarchy has access to a limited amount of information, and is extremely specialized in processing this limited information. As in industrial specialization, information specialization isolates the individual agent from the overall goals of the organization. The subgoals set for an individual agent, and the rules and procedures he has to follow, often appear arbitrary and capricious. The individual agent's inability to access and identify with the organizational goals and the organizational information in its totality leaves him without a sense of purpose; and the simplicity of the rules and procedures he has to follow—although increasing his efficiency—makes him feel insignificant, unimportant and easily replaceable. This type of a workplace has often been described as dehumanizing [48, 57].

Bureaucratic hierarchies impose certain decision models and information processing strategies on the organization. A different information system may lead to different decision models to remedy some of the shortcomings of the bureaucratic decision models. A centrally controlled, formal information system that processes all organizational information and acts as an information clearinghouse for the whole organization may solve many of the problems associated with the bureaucratic decision models. A central clearinghouse transforms the hierarchical structure to a star-shaped organizational structure for information flow purposes. This structure eliminates the distortion and the delays caused by the movement of information up and down the organizational hierarchy through multiple agents and multi-step processing since all agents are connected to each other through the central information system [24]. It also humanizes the process since each agent is directly connected to the organizational information system and able to detect the effect of his actions on the organizational goals and policies. Although the agents still need to be very specialized to maintain efficiency, the rules and procedures they use do not have to be as simplistic due to a wealth of information at their disposal through direct access to the organizational information system and the vast information processing power provided by it [24].

The prerequisite for the star-shaped organizational structure is an all-powerful central information processing agent for the whole organization which controls all organizational information, whether it is centralized or distributed. Only during the last two decades, with extensive computerization and organizational databases, has this option emerged as a real possibility. The structure described here was widely predicted in early MIS literature as the demise of middle management or the collapse of the organizational hierarchy [3, 26, 42, 48, 58]. These predictions have not yet been realized. Actually, the empirical evidence seems to suggest a trend in the opposite direction. Strengthening of middle management has been reported to accompany the introduction of computerized information systems [7, 8, 13, 47]. It is possible to argue, however, that the original predictions were correct by pointing the right direction of change, but grossly off target in estimating the speed of change and assessing the difficulties involved in overcoming the conceptual and technical problems [37, 38], not to mention the organizational inertia [1, 18]. The empirical evidence for strengthening of the middle management might be due to two different phenomena.

The first explanation is the strengthening competitive position of those organizations that utilize computing power to aid the existing decision models, even if the full potential of the formal organizational information system is not developed [9]. Computing power, like most other capital investments, improves the competitive position and the overall effectiveness of the organization, thereby increasing the total power exercised by the organization. Consequently, even with no redistribution of power among agents, each agent may feel an increase in power. A typical example of this is in the military where accelerating capital investments in military hardware has greatly increased the effectiveness. Many decisions that used to be made by colonels during the second world war are now being made by sergeants; however the colonels do not feel robbed of any power since the overall effectiveness and the destructive power of the military has multiplied many times since WWII, and the decisions made by today's colonels confer upon them a great deal more power and responsibility than their WWII counterparts [41].

The second explanation is the inability of the formal information system to replace the human decision system, as yet mainly due to a lack of conceptual foundation for the centralized control of information. More specifically, automated information systems have been quite successful in replacing the bureaucratic hierarchy in facilitating the upward movement of information since a substantial theory of information summarization exists as contributed by database theory $[55]$ , data modeling and abstraction $[54]$ , and management reporting $[22]$ . On the other hand, centralized information systems have failed to replace the bureaucratic hierarchy in facilitating the downward movement of information, i.e. the translation of goals into subgoals. This failure follows from the total preoccupation of the field of information systems with data. Even the perception of decision models as components of information and a concerted effort to manage the models by developing techniques to compose and decompose them are very recent developments leading to the emergence of the decision support systems subfield $[12]$ . Consequently, if the formal information systems are not ready to successfully replace the corresponding bureaucratic systems, then the evidence suggesting the strengthening of the middle management is merely based on the use of computing power to support the existing human information system, not the creation of a new formalized information system, and hence rendering that counterevidence irrelevant for our purposes.

The major argument in this section is that the computerization of bureaucracies is not likely to remain as mere support systems for the current decision makers and their existing models within the current organizational structure. It is likely to change both the decision models and the organizational structure that supports those models. Consequently, information systems cannot be successfully designed by merely studying the organization descriptively, without making some normative judgements or at least forecasting the effect of the information systems on the organization. Conversely, as long as information systems are designed to simply aid the current decision makers and their existing models, their success will be limited. Their role will be restricted to cost reductions in current activities, which is far from their full potential; especially because those cost reductions will immediately lead to a disequilibrium in the organization by changing the cost parameters of the organizational decision making process and will require reoptimization of the complete process to reach its full potential.

## Representative Democracy

The representative democracy practiced in the modern western world differs considerably from the original plebiscitary democracy of ancient Greece. As the societies grew both in size and complexity plebiscites were increasingly criticized for voting without adequate information and without adequate deliberation $[31]$ . To reduce the information processing burden on the voters and to improve the quality of their decisions, a two-level system is employed where the voters make decisions about the choice of their representatives and the representatives take over the detailed informative processing requirements of the legislative process. The representatives themselves are usually organized into an hierarchy of committees and subcommittees to cope with the information overload $[56]$ . The resulting multilevel structures exhibit many of the characteristics and limitations of bureaucratic hierarchies. In particular, the distortion problem has been studied extensively [28] since it is not clear how representative the representatives are, in light of the special interest groups, political action committees, full time lobbyists and political campaign contributors all trying to sway the political decisions in one direction or the other, not to mention the ultimate conflict between the self interests of a representative and the interests of the constituents he is supposed to represent [2, 28, 48]. As the society grows in size and complexity the information processing requirements of the legislators also increase, and staff hierarchies are created to support the representatives, exacerbating the distortion problem and pushing the structure to its limits [56].

The second limitation of bureaucracies was identified as the dehumanizing work environment they create. The analog of this limitation in representative democracies is the voter apathy that epitomizes modern democracies. A major advantage of the representative democracies was identified as the protection of the public from the burden of legislative information processing. As issues grow more complex, the public is further isolated from the societal goals and procedures to protect them from the complexities of the legislative process. As a result, the voters increasingly fail to see the relationship between the societal goals and their fragmented decisions to choose among seemingly similar political candidates, and the relationship between the governmental decision making process and the simple decision rules they use to elect representatives $[30, 35]$ . The inability to manipulate or even access societal goals and societal information leaves the voters without a sense of purpose, and the simplicity of the rules they follow leaves them insecure about the correctness of their decisions. The increasing gap of sophistication between societal and individual information processing encourages the support of dogmatic ideologies which simplify the societal information processing through standard and universal rules $[14]$ . The alternative of increasing the information processing ability of the individual voter is extremely costly and takes us back to the problems of the plebiscitary democracies and their limitations.

Representative democracies demonstrate the same two major points introduced in connection with bureaucracies:

a. Representative democracies clearly represent a significantly different information processing system than the plebiscitary democracies. In fact, there is considerable evidence that the decision models in a representative democracy are significantly different from those in a plebiscitary democracy. In particular, the leverage exercised by organized interest groups is higher in representative democracies since it is more cost effective to apply political pressure on representatives than on masses of individual voters [27].

b. Formal information systems have been suggested to remedy the problems and limitations associated with representative democracies [24, 39]. A centrally controlled information system which provides a direct link between the government and the people would eliminate both the distortion and the apathy caused by the representative system. The elimination of the distortion follows from the establishment of a direct link between the government and the people, and the processing of information in one stage for each voter. The elimination of apathy follows from the ability of the public to directly access societal goals and information, and to extract the relationship between the societal goals and their personal interests. The decision models used in this environment are likely to be similar to those in plebiscitary democracies and considerably different from the representative democracies. It appears that the introduction of formal information systems may make it possible to return to a plebiscitary democracy merely by aiding the human information processing with formal systems [24, 39].

A formal information system for a representational democracy is not qualitatively different from the information systems advocated for organizational bureaucracies. However the scale of operations is simply overwhelming, considering the limited information processing capability of individuals and the consequent problems associated with plebiscites. If the formal information systems are expected to eliminate the major problems associated with the representative democracies, they have to provide enormous information processing capabilities to aid the public. The aid must be (as in bureaucracies) in moving the information both upwards and downwards in the hierarchy. Downwards, the societal information must be summarized and custom tailored for each voter; upwards, the personal goals must be aggregated properly to establish the societal goals.

The design and management of such a large scale system is beyond current capabilities both technically and conceptually. Moreover, the computational models to translate personal goals to societal goals are not available since aggregating non-linear utility functions are not fully understood $[49]$ . The point to be made though is that the possibility of such systems exists. As easy as it is to contemplate such systems, it is equally clear that the introduction of such information systems might drastically change the decision models and the decision processes. Such extreme examples are useful so far as they dramatize the point and make it easier to see the influence an information system may have on the decision models.

## Conclusions

Four very different examples have been presented to demonstrate how information systems may influence the organizational decision models. The major implication of this influence is the difficulty of successfully completing a requirements analysis and developing an information system that actually meets the organizational needs. If the very introduction of an information system leads to changes in the decision models which might further change the requirements from the information system, then this type of dynamic circular relationship will make it impossible to actually design successful systems based on requirements captured at a point in time.

The circular relationship argument adds one more reason to a whole literature of reasons for the failure of requirements analysis. The reasons range from the dynamic nature of organizations and the environmental changes that take place during the time it takes to develop information systems, to the inability or the reluctance of the decision makers to reveal their requirements [30]. The difficulty posed by the circularity assertion appears to be more formidable than the previous reasons since it cannot simply be resolved by better forecasts of the organizational environment or better communication between the systems analysts and the line managers. It points out an inherent relationship between the requirements and the information systems which may require a complete redesign of the system design process [5]. Three possible approaches to the problem must be considered.

Normative design: Information systems could be designed normatively reflecting the way decisions should be made with little or no reference to the current procedures and policies. This approach requires: 1) a thorough analytical understanding of the goals and the means to achieve those goals, and the costs and benefits associated with each alternative; 2) a receptive organization which is willing to reorganize and force the decision makers to adapt to the new decision models. Neither of these conditions are likely to be met by any significant number of organizations or decision makers.

Equilibrium analysis: The requirements analysis may be expanded to include a detailed study of the effect of the planned information system on the decision models and the organizational structure. The study may have to include the second and third order effects due to the circularity of the relationship, or even a search for an equilibrium point where the relationship stabilizes. Although not as difficult as the normative design, the equilibrium analysis significantly complicates the requirements analysis and forces analysts to estimate the future behavior of the decision makers under different conditions. The unpredictability of the environment may make it impossible to find a stable enough equilibrium point at which the information system is targeted.

Evolutionary systems: New approaches to system design may be adopted to increase the flexibility of information systems. The increased flexibility may be used to encourage the design of tentative and constantly evolving systems through fast feedback response. Such flexible and evolving systems would require multilevel structures with highly automated interfaces, end-user design facilities, and self-adapting and learning behavior similar to that of biological systems. There is considerable research effort directed to this end. [34, 37, 40].

Evolutionary systems, sometimes referred to as 'open systems' [45], are characterized by their ability to spontaneously adapt and learn, and they are significantly different from existing commercial systems. They are also fundamentally different from modern requirements analysis techniques such as prototypes. Although prototypes are successful in simulating evolutionary systems during the analysis phase, they are restricted to that phase in terms of scope, duration and objectives. Prototypes are short-lived and inefficient to operate, and they do not learn and spontaneously adapt to their environment. Like all requirements analysis techniques they are designed to elicit and articulate the information requirements and they are based on the assumption of independently existing requirements.

If the requirements do not have an independent existence but are merely shaped by the existing information system, then basing the next information system on the requirements shaped by the existing information system may lead to a vicious circle. A circle of this sort has a long cycle period due to the slowness of organizational learning and the inertia against organizational change, and simple techniques such as prototyping are not likely to break the circle because of their short duration and limited exposure. A truly evolutionary system remains evolutionary throughout the life cycle of the system, and provides broad exposure to the organization by being efficient enough to be operationally feasible so that the organization as a whole can learn from it and react to it at its own pace.

The evolutionary systems appear to be the most promising solution to the dilemma posed by the interaction of information systems and the decision models, since the normative studies of decision making are in their infancy, and equilibrium analysis would require extensive research into the relationship between information systems and decision models. On the other hand, there is considerable research effort already devoted to increasing the flexibility of information systems and evidence that they may actually be cheaper in the long run than fixed systems, once the conceptual framework is in place.

## References

[1] Argyris, C. "Resistance to Rational Management Systems," Innovation, Volume 10, Number 3, September 1970, pp. 28–34, 1970.

[2] Axelrod, R. Conflict of Interest: A Theory of Divergent Goals With Applications to Politics, Markham Publishing, Chicago, Illinois, 1970.

[3] Becker, S.W. and Neuhauser, D. The Efficient Organization, Elsevier, New York, New York, 1975.

[4] Bennington, G. and Rebibo, K. "Overview of RUCUS Vehicle Scheduling Program," in Workshop on Automated Techniques for Scheduling Vehicle Operators for Urban Public Transportation Services, D. Bergmann and L. Bodin (eds.), North Holland, Amsterdam, Holland 1975.

[5] Berrisford, T. and Wetherbe, J. "Heuristic Development: A Redesign of Systems Design," MIS Quarterly, Volume 3, Number 1, March 1979, pp. 11–19.

[6] Blau, P.M. The Dynamics of Bureaucracy, University of Chicago Press, Chicago, Illinois, 1963.

[7] Blau, P.M. "The Hierarchy of Authority in Organizations," American Journal of Sociology, Volume 73, Number 2, June 1968, pp. 453–462.

[8] Blau, P.M. and Schoenherr, R.A. The Structure of Organizations, Basic Books, New York, New York, 1971.

[9] Blau, P.M., Falbe, C.M., McKinley, W. and Tracy, P.K. "Technology and Organization in Manufacturing," Administrative Science Quarterly Volume 21, Number 1, March 1976, pp. 20–42.

[10] Bodin, L., Golden, B., Assad, A. and Ball, M. "Routing and Scheduling of Vehicles and Crews: The State of the Art," Computers and Operations Research, Volume 10, Number 2, March 1983, pp. 63–211.

[11] Bodin, L., Rosenfield, D. and Kydes, A. "UCOST. A Micro Approach to a Transit Planning Problem," Journal of Urban Analysis, Volume 5, Number 1, January 1978, pp. 47–69.

[12] Bonczek, R.H., Holsapple, R.W. and Whinston, A.B. Foundations of Decision Support Systems, Academic Press, New York, New York, 1981.

[13] Child, J. "Predicting and Understanding Organization Structure," Administrative Science Quarterly, Volume 18, Number 2, June 1973, pp. 168–185.

[14] Cox R. Ideology, Politics and Political Theory, Wadsworth, Belmont, California, 1969.

[15] Chervany, N.L. and Dickson, G.W. "An Experimental Evaluation of Information Overload in a Production Environment," Management Science, Volume 20, Number 10, June 1974, pp. 1335–1344.

[16] Davis, G.B. "Strategies for Information Requirements Determination," IBM Systems Journal, Volume 21, Number 1, January 1982, pp. 4–30.

[17] Driver, M.J. and Streufert, S. "Integrative Complexity: An Approach to Individuals and Groups as Information Processing Systems," Administrative Science Quarterly, Volume 14, Number 2, 1969, pp. 200–294.

[18] Dyckman, T.R., Hoskin, R.E. and Swieringa, R.J. "An Accounting Change and Information Processing Changes," Accounting, Organizations and Society, Volume 7, Number 1, March 1982, pp. 1–11.

[19] Ford, L. and Fulkerson, D. Flows in Networks, Princeton University Press, Princeton, New Jersey, 1962

[20] Galbraith, J.K. The New Industrial State, Houghton Mifflin, Boston, Massachusetts, 1978.

[21] Golden, B. and Yee, J. "A Framework For Probabilistic Vehicle Routing," AIEE Transactions, Volume 11, Number 2, March 1979, pp. 109–112.

[22] Hendriksen, E.S. Accounting Theory, J.D. Irwin, Chicago, Illinois, 1977.

[23] Hilton, R. "The Determinants of Information Value: Synthesizing some General Results," Management Science, Volume 27, Number 1, January 1981, pp. 57–64.

[24] Inbar, M. Routine Decision Making: The Future of Bureaucracy, Sage Publishing, Beverley Hills, California, 1979.

[25] Inglehard, D.L. and Morey, R.C. "Inventory Systems With Imperfect Asset Information," Management Science, Volume 18, Number 8, April 1972, pp. 388–396.

[26] Jackson, R. "Computers and Middle Management," Journal of Systems Management, Volume 21, Number 4, April 1970, pp. 41–45.

[27] Key, V.O., Jr. Politics, Parties and Pressure Groups, Cromwell, New York, New York, 1964.

[28] Krislov, S. Representative Bureaucracy, Prentice-Hall, Englewood Cliffs, New Jersey, 1974.

[29] Langton, J. “The Ecological Theory of Bureaucracy. The Case of Josiah Wedgewood and the British Pottery Industry,” Administrative Science Quarterly, Volume 29, Number 3, September 1984, pp. 330–354.

[30] Long, N. The Polity, Rand McNally, New York, New York, 1962.

[31] Lowi, T.J. American Government: Incomplete Conquest, Dryden Press, New York, New York, 1976.

[32] Lucas, H.C. Why Information Systems Fail, Columbia University Press, New York, New York, 1975.

[33] McClain, J.O. and Thomas, L.J. Operations Management: Production of Goods and Services, Prentice-Hall, Englewood Cliffs, New Jersey, 1985.

[34] McLean, E.R. "End Users as Application Developers," MIS Quarterly, Volume 3, Number 4, December 1979, pp. 37–46.

[35] Mosca, G. The Ruling Class, McGraw-Hill, New York, New York, 1939.

[36] Munro, M.C. and Davis, G.B. "Determining Management Information Needs: A Comparison of Methods," MIS Quarterly, Volume 1, Number 2, June 1977, pp. 55–67.

[37] Orman, L. "A Multilevel Design Architecture for Decision Support Systems," Data Base, Volume 15, Number 3, Spring 1984, pp. 3–10.

[38] Orman, L. "Familial Model of Data," Computer and Information Sciences, Volume 13, Number 3, September 1984, pp. 149–175.

[39] Orman, L. "Fighting Information Pollution With Decision Support Systems," Journal of MIS, Volume 1, Number 2, 1984, pp. 64–71.

[40] Orman, L. "Flexible Management of Computational Models," Decision Support Systems, Volume 2, Number 4, December 1986.

[41] Perrow, C. "Is Business Really Changing?" Organizational Dynamics, Volume 3, Number 1, Summer 1974, pp. 32–44.

[42] Power, D.J. "Impact of Information Management on the Organization: Two Scenarios," MIS Quarterly, Volume 7, Number 3, September 1983, pp. 13–20.

[43] Psaraftis, H. "A Dynamic Programming Solution to the Single Vehicle Many-To-Many Immediate Request Dial-a-Ride Problem," Transportation Science, Volume 14, Number 2, May 1980, pp. 130–154.

[44] Revsine, L. "Data Expansion and Conceptual Structure," Accounting Review, Volume 45, Number 3, July 1970, pp. 513–523.

[45] Rich, E. Artificial Intelligence, McGraw-Hill, New York, New York, 1983.

[46] Schroder, H.M., Driver, M.J. and Streufert, S. Human Information Processing, Holt, Rinehart and Winston, New York, New York, 1967.

[47] Segev, E. and Ein-Dor, P. "Organizational Context and MIS Structure: Some Empirical Evidence," MIS Quarterly, Volume 6, Number 3, September 1982, pp. 55–68.

[48] Simon, H.A. The Shape of Automation for Men and Management, Harper and Row, Chicago, Illinois, 1965.

[49] Simon, H.A. The Science of the Artificial, MIT Press, Cambridge, Massachusetts, 1969.

[50] Simon, H.A. Administrative Behavior, The Free Press, New York, New York, 1976.

[51] Stohr, E.A. "Information Systems for Observing Inventory Levels," Operations Research, Volume 27, Number 2, March 1979, pp. 242-259.

[52] Tapiero, C.S. "Optimization of Information Measurement with Inventory Applications," INFOR, Volume 15, 1977, pp. 50–61.

[53] Tharaken, G. and Psaraftis, H. "An Exact Algorithm for the Exponential Disutility Dial-a-ride Problem," Transportation Science, Volume 15, Number 2, May 1981, pp. 81–94.

[54] Tsichritzis, D.C. and Lochowsky, F.H. Data Models, Prentice-Hall, Englewood Cliffs, New Jersey, 1982.

[55] Ullman, J.D. Principles of Database Systems, Computer Science Press, Potomac, Maryland, 1984.

[56] Wahlke, J.C. and Fulay, H. The Legislative System, John Wiley & Sons, New York, New York, 1962.

[57] Weber, M. From Max Weber: Essays in Sociology, Translated by H.H. Gerth and C.W. Mills, Oxford University Press, Oxford, England, 1946.

[58] Whisler, T.L. The Impact of Computers on Organizations, Praeger Publishing, New York, New York, 1970.

## About the Author

Levent Orman is Associate Professor of Information Systems at Cornell University, Graduate School of Management. He received M.M. and Ph.D. degrees from Northwestern University, Graduate School of Management. His recent publications appeared in Information Systems, Decision Support Systems and Transactions on Software Engineering.
