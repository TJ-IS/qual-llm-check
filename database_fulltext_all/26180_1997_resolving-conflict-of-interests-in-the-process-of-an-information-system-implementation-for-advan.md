---
otero_id: 26180
otero_key: "DCS9DT2W"
title: "Resolving Conflict of Interests in the Process of an Information System Implementation for Advanced Telecommunication Services"
authors: "Jae-Hyeon Ahn; Ann E. Skudlark"
year: "1997"
journal: "Journal of Information Technology"
doi: "10.1177/026839629701200101"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Resolving con¯ ict of interests in the process of an information system implementation for advanced telecommunication services

JAE-HYEON AHN and ANN E. SKUDLARK AT&T Labs, 600 Mountain Avenue, Murray Hill, NJ 07974, USA

From many empirical studies, organizational issues have been considered the most critical bottleneck for successful information system (IS) implementations. In this paper, an organizational issue of resolving con¯ ic of interests among the stakeholders is addressed. Using the decision analytic approach, the major source of disagreement among the stakeholders were identi® ed, discussed and resolved. The approach was applied to a problem of implementing an information system for advanced telecommunication services. The case presented here showed how to resolve the con¯ icting interests proactively and demonstrated the value of the approach. The decision analytic approach presented in this paper was a viable and very useful tool in resolving the con¯ ict of interests among the people included in the negotiation process. As a result of the successful negotiation, it was estimated to have saved \$6.9 million dollars after tax for AT&T.

## Introduction

Information systems have been implemented in many diverse areas and have not been always successful. Gladden (1982) reported that 75% of information systems developed were either never completed or the completed systems were never used. Lyytinen and Hirschheim (1987) con® rmed that at least half of these information systems were failures in spite of the numerous progresses and strides made in the development, implementation and usage of them. Raheb (1992) also reported that more than 70% of all information systems developed within Canadian companies were never implemented. Information system (IS) failures continued in the 1990s (Ubokudom, 1993; Curie, 1994; Oz, 1994a,b; Beynon-Davies, 1995).

There has been considerable research into IS failure types and reasons for frequent IS failures (Lucas, 1975; Alter and Ginzberg, 1978; Gladden, 1982; Bailey and Pearson, 1983; Markus, 1983; Lyytinen and Hirschheim, 1987; Sauer, 1993). The research on IS failures is valuable because it gives signi® cant learning experience in identifying the pattern of events leading to failures, and provides opportunities for improving the IS implementation process. Case histories for failed IS development projects are especially valuable in understanding the complexity of IS failure and developing theories (Benbasat et al., 1987; Adel-Hamid and Madnick, 1990; Sauer, 1993; Beynon-Davies, 1995; Ewusi-Mensah and Przasnyski, 1995).

However, IS failure is a relative term depending on how we de® ne \`failure’ : there are several de® nitions of it (Lucas, 1975; Bailey and Pearson, 1983; Robey and Markus, 1984; Lyytinen and Hirschheim, 1987; Sauer, 1993). Lyytinen and Hirschheim (1987) de® ned it as \`inability of an IS to meet a speci® c stakeholder group’s expectations’. The stakeholders are a group of people sharing a pool of values that de® ne what the desirable features of an IS are and how they should be obtained. Sauer (1993), however, viewed the IS failure more conservatively than Lyytinen and Hirschheim, suggesting that an information system should not be considered a failure until all stakeholders cease to support the progress of the IS project. Despite the different de® nitions of IS failures, it is generally agreed that most of the reasons for failure are related to organizational and behavioural issues rather than technical ones (DeSanctis, 1983; Lucas, 1975, 1976; Jin and Franz, 1986; Lyytinen and Hirschheim, 1987; Alter, 1992, Sauer, 1993). For example, Lucas (1976) emphasized the issues by arguing that the major reason most information systems have failed is that we have ignored organizational behaviour problems in the design and operation of systems. Organizational issues are important because the work practice (the method used by people and technology to perform work) should be changed to realize a value from the newly implemented IS. The change process (Schein, 1969) is critical for successful IS implementation. The process should be well managed and any potential problems should be addressed before an IS implementation (Alter, 1992). Not surprisingly, when AT&T was trying to implement an information system for advanced telecommunications services, an organizational problem emerged and had to be resolved.

As of January 1995, there were two major business units in AT&T representing residential and business long-distance market segments. Business unit A was responsible for the residential market segment and business unit B was responsible for the business market segment. Business unit A proposed to implement an information system to provide enhanced network communication services to customers while at the same time enhancing the handling of customer speci® c data in the network. The system was expected to reduce the unit cost of telecommunication services and provide marketing bene® t by fast, intelligent and customized feature activation mechanisms. According to the plan, all calls, regardless of market segment, go through the proposed information system. As a result, the calls would experience an additional half a second delay in call setup time. Because business unit B was concerned about the potential effect of the call setup time delay, they were reluctant to cooperate. More precisely, business unit B was reluctant to let their customers’ calls go through the IS because: (1) they couldn’t articulate any economic value of participating, (2) they worried that business unit A could control the information of business unit B customers, and (3) the idea of a new system was proposed not by them but by business unit A. According to other research (Keen, 1981; Markus, 1983) those are typical reasons leading to the failure of information systems; con¯ icting shareholder’s interests, shift of political power, ownership, etc.

Anticipating potential problems in the implementation of the proposed information system, we tried to raise those issues proactively. Using the decision analytic approach, the major sources of disagreement among the stakeholders were identi® ed, discussed and resolved.

## Implementation of an information system for advanced telecommunications service

The Universal Subscriber Data Structure (USDS) is a communications network platform initiated by the AT&T business unit A. As customer demand for advanced communication services is driving the development of many new services and features, the USDS was proposed to be a platform enabling enhanced telecommunications services.

To provide the advanced services, we need an activation mechanism which identi® es the customer or household each time they access the AT&T network. These identi® ers may be the customer’s telephone number, calling card number, mobile identi® cation number, etc., depending on the access methodology used to enter the telephone network. These identi® ers are used to activate the feature or features to which the customer has subscribed or has access. These same identi® ers are also used to restrict access to the network or to identify customers who wish to be excluded from non-subscription type capabilities such as third number billing or collect calls. In addition to these identi® cations or trigger data, there may be service speci® c

![](/api/attachments/DCS9DT2W/fulltext/images/151e0bf86fd21458605f72dd9158d07d5e9e4afbfdd7b5b5b0c709ee047ee2a5.jpg)  
Figure 1 Network, architecture of USDS NCPAS. Network Control Point, Administration, System: NEMOS. Network Management Operations Systems; TNM, Total Network Management; CSMS, Consumer Service Management System; STP, Signal Transfer Point.

## Con¯ ict of interests in IS implementation

information stored for each subscriber such as a telephone number for call forwarding or select collect features. In the current strategic business unit (SBU) environment, customers who subscribe to multiple features have redundant trigger data stored for each service or feature. This implies that there are multiple databases or trigger tables for automatic number identi® cation (ANI), multiple data provisioning/maintenance processes and, as a result, unnecessary costs attributed to the accumulation, storage and utilization of multiple versions of the same customer information for real-time call handling.

While there are common customer data stored in multiple locations, there is no easy method available to link this information to give a complete picture of the customer’s utilization of the AT&T network and services. In addition, there are also common customer data that could be used by multiple services or features which are not currently stored for real-time call processing at all. Customer language preference, toll discount plan information, and special needs status for hearing-impaired person are examples. With the apparent inef® ciency of call processing, there was a strong need to develop a system which would satisfy the customer’s diverse needs while reducing cost and inef® ciency of call processing. The proposed system, Universal Subscriber Data Structure (USDS) will use a common set of features and services that are consistently triggered by a universal customer record which will store subscriber-speci® c information and will be accessed and utilized during the call setup process. Figure 1 shows the architecture of USDS in the AT&T network.

The implementation of USDS will reduce unit cost and provide marketing bene® ts. It will reduce network database capital cost, provisioning cost, electronic switching system development cost, etc. Also it will provide a fast feature activation mechanism so that we can provide fast, customized and integrated customer services.

According to the original deployment plan of USDS, all telephone calls would go through the USDS platform regardless of whether they are calls originated from business unit A customers or business unit B customers. Necessary information is retrieved from the USDS database by going through the USDS platform for call processing. If a call matches with the trigger table for automatic number identi® cation (ANI), it goes through the USDS platform and experiences a slight incremental call setup time delay. This was expected to be about 500 milliseconds. Business unit A considered the call setup time delay effect negligible. Business unit B, on the other hand, disagreed. They suspected that the call setup time delay would result in substantial business unit B customer loss, due to anticipated claims by their competitors that they provide better quality of service than AT&T.

In spite of business unit B’ s initial refusal to cooperate, business unit A saw the value of implementing the USDS platform and wanted to gain cooperation from business unit B on this issue so that all telephone calls would go through the USDS platform. Because business unit B opposed the idea, the problem was how to negotiate in a way that it would lead to a mutually bene® cial solution for both business units.

## Negotiation between two business units

According to the original deployment plan or \`interbusiness cooperation’ strategy, telephone calls going through the USDS platform would experience about a 0.5 second delay in call setup time. Because of this delay, business unit B was opposed to the USDS platform. The major argument from business unit B was that they expected unfavourable effects on their customer retention and winback efforts. They suspected that competitors can take advantage of the call setup time delay in their marketing efforts.

When the negotiations failed, we (the USDS team representing business unit A), realized the USDS deployment schedule was in jeopardy. As a result, it was decided to implement a fallback strategy, or \`provisioning \$25+ business unit A market segment’ strategy. According to the strategy, only 15% of the customer base of business unit A (the market segment whose monthly telephone bill is greater than \$25) would go through the USDS platform. In October 1994, upper management of business unit A approved the implementation of the USDS concept, provided we go ahead with the fallback strategy. They strongly believed that the full bene® t of implementing the platform cannot be realized without the inter-business unit cooperation.

The provisioning \$25+ business unit A market segment strategy had a major drawback in that it could have adverse effect on customer satisfaction. To explain this more clearly, let’ s categorize business unit A and business unit B customers into 3 categories: business unit B’ s non-featured customers; \$25- business unit A customers; and \$25+ business unit A customers. Currently, for most calls, the AT&T network can distinguish between residential calls and business calls. But, business unit B’ s non-featured customers represent a customer segment which we can’ t distinguish from the business unit A customer originated calls.

Table 1 shows the possibility of delivering USDS platform-based services for inter-business unit cooperation and \`provisioning \$25+ business unit A market segment’ strategies, respectively.

Table 1 Services provided by different strategies

<table><tr><td>Calls from rows to columns</td><td>Business unit B non-featured customers</td><td>$25- business unit A customers</td><td>$25+ business unit A customers and subscribers</td></tr><tr><td colspan="4">Inter-business cooperation strategy:</td></tr><tr><td>Business unit B</td><td></td><td></td><td></td></tr><tr><td>Non-featured customers</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>$25- business unit A customers</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>$25+ business unit A customers and subscribers</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="4">Provisioning $25+ business unit A market segment strategy:</td></tr><tr><td>Business unit B</td><td></td><td></td><td></td></tr><tr><td>non-featured customers</td><td>No</td><td>No</td><td>No</td></tr><tr><td>$25- business unit A customers</td><td>No</td><td>No</td><td>No</td></tr><tr><td>$25+ business unit A customers and subscribers</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Under the inter-business cooperation strategy, everybody can use the services provided by the USDS platform. On the other hand, under the provisioning \$25+ business unit A market segment strategy, it was obvious that many features provided by USDS would only be available to \$25+ business unit A customers and subscribers. This incomplete service could make AT&T customers very dissatis® ed, and either we may lose our valuable customers or we need to ® nd a way to compensate them for their dissatisfaction. Realizing those issues, it was necessary to estimate the potential effect of the incomplete services. By showing those problems explicitly, we expected to demonstrate effectively and resolve the anticipated problems for provisioning only \$25+ business unit A customers and eventually solicit the cooperation from business unit B in the negotiation process.

## Decision analytic approach

Negotiation analysis provides prescriptive theory and useful advice for negotiators. Game theory has provided a theoretical starting point for the negotiation analysis, especially in well-structured repeated negotiations and the study of industrial organization. However, game theory lacks prescriptive usefulness, even though it seems to provide a logically consistent framework for analysing certain negotiation situations. There are at least three problems in game theory. First, there are multiple equilibria in game theoretic modelling and there is no method for choosing the best strategy. Rather than prescribing which strategy to choose, game theory tries to predict what will happen in the negotiation situation. In spite of several attempts to re® ne those multiple equilibria problems (Selten, 1975; Kreps and Wilson, 1982; Owen, 1995), game theory still doesn’t provide useful prescriptive advice guiding the choice of which strategy to follow. Second, game theory makes strong rationality assumptions when it predicts the probable outcome. However, it is known that people show bounded-rationality ± meaning that people try to be rational in actions, but show cognitive and computational limitations. Therefore, the prediction of outcome based on the rationality assumption could be misleading. Third, game theory makes common knowledge assumptions on the elements, structures and rules of the negotiation situation. But, the reality is that we have no information or little information at best about the player’ s possible strategies, value structures, beliefs, and other external variables related to the situation. Therefore making common knowledge assumptions in the negotiation situation, in many cases, tends to be unrealistic.

![](/api/attachments/DCS9DT2W/fulltext/images/acf73cf9b189e2309b6c93df7733c70d19b568c3bf51e259926acbbd75096559.jpg)  
Figure 2 Decision analysis cycle

On the other hand, decision analysis deal with the negotiation situation in a different way: it deals with the other negotiating party descriptively rather than prescriptively. The descriptive approach is a critical difference allowing subjective assessment of the negotiating party’ s probabilities, preferences and rational behaviour. The decision analytic approach is gaining acceptance as a viable new approach for negotiation analysis (Raiffa, 1982; Sebenius, 1992).

There are decision problems with signi® cant, longlasting impacts. Those problems may be characterized by: the complexity of the variables and their interactions; the dynamic nature of the problem; and the uncertainty of the decision environment. Because of the signi® cance of the problems, they warrant careful thought and analysis. They need a systematic approach to gain insight on the decision problem and support the selected alternative rather than an intuitive or holistic approach. Decision analysis addresses those problems: it provides prescriptive advice in those complex, dynamic and uncertain decision situations, based on utility theory and probability theory as a way of representing uncertainty (Howard and Matheson, 1983). And it has been successfully practiced in business, government, public policy, the medical area, and so on (Howard and Matheson, 1983; Corner and Kirkwood, 1991). To solicit the best result in the negotiation process with business unit B, we decided to adopt the decision analytic approach for at least the two following reasons. First, it will provide a formal, unequivocal language for communication among the people included in the negotiation process. Second, it will give useful insight by discovering the source of disagreements among the people involved in the negotiation process.

## Decision analysis cycle

When we apply decision analysis principles to real world problems, we often follow an iterative procedure, called the decision analysis cycle. Generally, a decision problem can be characterized by uncertainty, complexity, dynamic natures, allocation of ® nite resources, and multiple objectives. The goal of the decision analysis is to formulate the decision problem into a formal model so that we can derive the best recommendation and gain enough insights for the problem at hand. The decision analysis cycle we generally follow is shown in Figure 2.

The cycle consists of three stages: formulation stage, input assignment stage and evaluation stage. In the formulation stage, we formulate the decision problem with the variables we have chosen and with the objectives we want to achieve. Also, we elicit creative alternatives that we want to evaluate. In the input assignment stage, we assess the necessary information for analysis such as outcomes, probabilities associated with the outcomes, time preference, risk preference, and so on. In the evaluation stage, we evaluate each alternative based on the structure we have framed, the information we have, and our preferences. Then, we iterate the whole decision analysis cycle until we are satis® ed with the model and the insights it gives. Following the decision analysis cycle does not guarantee good outcomes, but it helps to make sure that we do not miss any important factor during the whole decision process.

Table 2 Summary of strategies

<table><tr><td>Strategy</td><td>Going through USDS platform</td><td>Call setup time delay on business unit B</td><td>Utilization of USDS</td><td>Cost</td><td>Availability of terminating feature</td></tr><tr><td>Inter-business cooperation</td><td>All business unit A and B customer calls</td><td>0.5 sec delay</td><td>Maximum use</td><td>No cost for ANI trigger table management</td><td>All calls processed by USDS</td></tr><tr><td>Provisioning $25+ business unit A market segment</td><td>Only $25+ business unit A customer calls</td><td>No effect</td><td>Limited to the $25+ business unit A customers</td><td>Cost for provisioning $25+ business unit A customers</td><td>Only when $25+ business unit A customer initiate calls</td></tr><tr><td>Provisioning business unit B non-featured customers</td><td>All calls except business unit B non-featured calls</td><td>No effect</td><td>All business unit A customers</td><td>Cost for provisioning business unit B non-featured customers</td><td>All business unit A initiated calls</td></tr></table>

## Development and analysis of a model

To resolve the con¯ ict of interests between the two business units, we decided to follow the decision analysis cycles described in Fig. 2. It was expected that the process would clearly reveal and eventually resolve the disagreements between the two parties, whether they are based on different information or different values. In the following, we will review the development of the model at each stage in more detail.

## Formulation stage

## Alternatives generation

Initially, there were two alternatives to consider. The ® rst alternative (inter-business cooperation) was to let every call of business unit A and B customers go through the USDS platform assuming that business unit A can get cooperation from business unit B. The cooperation from business unit B means that their nonfeatured calls go through the USDS platform which would result in the call setup time delay on their customers. This alternative will make the terminating features, like True Ties¾ or True Messages¾ , available to every business unit A and B customers. The alternative was to provide trigger tables for automatic number identi® cation (ANI) for the \$25+ business unit A customer segment. It would limit the ability to provide terminating features on business unit A and B originated calls, but it would not have any call setup time delay on the business unit B customer calls. This strategy was called \`provisioning \$25+ business Unit A market segment’ strategy. We considered other strategies, but they were dropped from further consideration.

## New alternative

As we analysed these two strategies, there were two major attributes to trade off. One was the bene® t of USDS which would provide enhanced telecommunication services and better marketing support for business unit A. The other was the potential loss of business unit B customers and possibly business unit A customers too. Because of the apparent con¯ ict of interests between the two business units, it was very dif® cult to attain cooperation from business unit B for a successful USDS implementation. So, we devised a new strategy both minimizing the risk of potential customer loss and maximizing the utilization of the USDS platform. The strategy was to provide ANI trigger tables for all business unit B non-featured customers so that their calls do not go through the USDS platform at all. With that strategy, business unit B non-featured customers will not experience any call setup time delay and business unit A customers can utilize the bene® t of the USDS platform. It was called a \`provisioning business unit B non-featured customers’ strategy. The three strategies are summarized in Table 2.

## Structuring

To structure the problem, we used an in¯ uence diagram framework which is popular in decision analysis practices. An in¯ uence diagram is a directed graph which provides graphical representation of a decision problem and captures the dependencies among the variables in the problem (Clemen, 1996). It uses four types of nodes and two types of arcs to represent variables and relationships among them (Figure 3). The rectangle symbolizes a decision node which represents a decision variable for the decision maker and contains decision alternatives. The oval symbolizes a chance node which represents uncertain events and contains random variables for the event. The double circle symbolizes a deterministic node which represents functional or logical relationships among variables. The rounded rectangle symbolizes a value node which represents an objective to maximize or minimize. An arc into a chance node implies the probabilistic dependency between the nodes. An arc into a decision node implies that when a decision is made, the value of the predecessor is known to the decision-maker. Figure 3 shows an in¯ uence diagram we developed using the conventional in¯ uence diagram notations.

In the previous business case analysis, some deterministic variables related to each decision were identi® ed. For example, development cost, labour and capital savings, etc, were assessed as a point estimate for each strategy. Those variables are summarized and represented as a single \`net present value (deterministic)’ node in Figure 3. In addition to the factors identi® ed in the previous business case analysis, we identi® ed three more crucial factors which were operator cost because of the enquiries regarding incomplete services; loss of business unit A customers; and loss of business unit B customers. We included these variables and quanti® ed them probabilistically to show the impact of incomplete services and argue the value of cooperation strategy.

![](/api/attachments/DCS9DT2W/fulltext/images/b6fc39312cc70fe63862c92a54fe3d3da2819f1879990860be8695429df8b0c1.jpg)  
Figure 3 In¯ uence diagram

Table 3 Comparison of strategies (unit: \$1 000)

<table><tr><td></td><td>Expected value (business unit A)</td><td>Expected value (business unit B)</td><td>Expected value (AT&amp;T)</td><td>Standard deviation (AT&amp;T)</td></tr><tr><td>Inter-business cooperation</td><td>6 472.3</td><td>-2 170.8</td><td>4 301.5</td><td>3 569.5</td></tr><tr><td>Provisioning business unit B non-featured customers</td><td>3 886.9</td><td>-434.2</td><td>3 452.7</td><td>1 540.4</td></tr><tr><td>Base case: (provisioning $25+ business unit A market segment)</td><td>-2 597.0</td><td>0</td><td>-2 597.0</td><td>7 779.2</td></tr></table>

As shown in Figure 3, \`additional cost’ node and \`net present value (deterministic)’ node were used to calculate deterministically the \`net present value after tax’ node which was the objective to maximize. The \`additional cost’ node was assessed by adding three nodes which are \`operator cost’ , \`revenue loss of business unit A’ , and \`revenue loss of business unit B’ . The three nodes were further decomposed into levels that allow realistic assessments.

## Input assignment stage

Based on the structure and variables represented in the in¯ uence diagram, we gathered relevant information from many sources. This information included: number of customers in each market segment; average monthly revenue/customer; pro® t margin; operator cost per minute for resolving customer complaints; average length of operator service; and so on. The detailed assumptions and the way variables were assessed are available elsewhere (Ahn and Skudlark, 1995), and are not available in this paper for reasons of con® dentiality. We also documented the source of information, so we know who is responsible for the validity of the information and who to ask to gather more information.

## Evaluation stage

Before the formal evaluation, we made some assumptions regarding the planning horizon, time preference and risk preference. When the model was evaluated, a ® ve year planning horizon was used which is standard for AT&T business case analysis. The analysis was done using the time series capability of a software called CADET (computer aided decision evaluation tool) which was developed in AT&T Bell Labs for decision analysis practices (AT&T, 1995). In terms of time preference, the annual discount factor was used which was supplied by the AT&T Treasury department for internal consistency. In terms of a decision criterion, expected value (net pro® t after tax) was used in the analysis. Considering the size of the AT&T asset (Howard 1988), it was assumed that a risk-neutral decision criterion would best represent the risk attitude of AT&T.

Based on the model developed and the assumptions made, the expected value and standard deviation of each strategy was calculated (shown in Table 3). The second and third column show the expected value of each strategy from the perspective of business unit A and business unit B. The fourth and ® fth columns show the expected value and standard deviation of each strategy from the AT&T corporate standpoint (the fourth column is the sum of the second and third columns).

According to this analysis, inter-business cooperation strategy gave AT&T the maximum expected value. The provisioning business unit B non-featured customers strategy was a close second. Provisioning \$25+ business unit A market segment strategy was considered the worst strategy to take. The analysis from business unit A’s standpoint was the same as the AT&T corporate view ± which means that whatever was good for AT&T was good for business unit A as well. On the other hand, from business unit B’s perspective, \`no cooperation’ was the best thing for the performance of their market segment. Inter-business cooperation was the worst strategy for business unit B. Because the strategy required unilateral cooperation and loss for business unit B, their opposition was understandable.

## Con¯ ict of interests in IS implementation

According to Table 3, inter-business cooperation had a larger expected value and also a larger standard deviation than the provisioning business unit B nonfeatured customers strategy from the AT&T corporate point of view. This meant that inter-business cooperation had more risk than the provisioning business unit B non-featured customers strategy because of the possible, but unlikely, scenario of losing customers caused by the call setup time delay. On the other hand, if provisioning business unit B non-featured customers was chosen, we can effectively get rid of the risk of losing business unit B customers due to the call setup time delay. The base case strategy, or strategy of provisioning only \$25+ business unit A customers, has the worst expected value and the largest standard deviation because of the expected operator cost and the potential business unit A and B customer loss due to incomplete services. According to this analysis, we could save \$6.9 million after tax for AT&T during the ® ve year period by having full cooperation from business unit B. By following the provisioning business unit B non-featured customers strategy, we could still save \$6.0 million after tax rather than following the base case strategy.

Considering the lack of incentive from business unit B for the cooperation strategy, the second best strategy was seriously considered. With the provisioning business unit B non-featured customers strategy, business unit B could get rid of the risk of losing customers due to the call setup time delay. The estimated cost for provisioning business unit B non-featured customers (about \$0.43 million) was supposed to be paid by business unit A. From business unit A’ s point of view, with this strategy, they could provide USDS services to all business unit A customers which eliminates virtually all concerns on the incomplete service. As a contingency strategy, the strategy was reserved in the event that all the efforts for inter-business cooperation failed.

## Further negotiation

Based on the analysis in the previous section, we started to renegotiate with business unit B. In the process, we represented the problem with an in¯ uence diagram framework, and explained how we structured the problem. Detailed explanations for assumptions, probability and value assessments followed. The power of the in¯ uence diagram representation was so great that business unit B understood and agreed with the decomposed structure of the problem without dif® culty. Because of the general agreement on the structure, discussions were focussed on disagreements on the speci® c numbers such as provisioning cost and rate at which customers might leave AT & T rather than subjective speculation or pointless arguments.

Then, we showed the value of inter-business cooperation emphasizing the change of paradigm shift from each business unit perspective to the AT&T corporate perspective. As the negotiation continued, we used two negotiation tactics. First, we proposed the provisioning business unit B non-featured customers strategy as the second best strategy for business unit B to choose. Business unit B was persuaded to take at least this strategy if they couldn’t cooperate with business unit A. Because they agreed to the structure of the problem, they couldn’t argue their position except questioning certain value assessments which didn’t change the attractiveness of the cooperation. In fact, one of the major differences between the two business units was the potential rate at which customers might defect from business unit B. The decomposed structure effectively identi® ed the major disagreements between business units A and B. Second, we indicated that we would bring these issues to top management and argue the myopic business practice of business unit B unless they cooperated or at least took the second best strategy. The threat was very effective and credible because: all the costs and bene® ts of each strategy were quanti® ed; the value of cooperation was clearly shown from the AT&T corporate perspective; and because the structure of the problem was already agreed except some value judgments, there were not many counter arguments possible.

After several discussions and reviews of the analysis, the negotiation ® nally came to an end. Business unit B ® nally proposed to cooperate with business unit A and let their calls go through the USDS platform. In return, they asked for support for targeted marketing efforts from the USDS platform capability which was acceptable to business unit A. At the conclusion of the negotiation, business unit A was able to deploy the USDS platform and all AT&T calls were allowed to go through the platform to achieve maximum use. On the other hand, business unit B was able to get support for their targeted marketing efforts in return for the cooperation. Both business units were satis® ed with the ® nal outcome.

## Conclusion

Organizational issues have been identi® ed as the most critical bottleneck for successful information system (IS) implementations. Unless those issues are handled before IS is designed and implemented, the IS will be more likely a failure than a success. Unsolved organizational issues would lead to a lack of user acceptance and participation, resistance to the change in work practices, lack of top management support, and so on, which are all considered to be critical factors leading to a failure of IS.

In this paper, an organizational issue was addressed: resolving con¯ icting interests of the stakeholders. During the whole negotiation, the decision analytic approach was useful in many ways. First, it provided a clear and effective language for communication among people involved in the negotiation process. Explicit graphical representation of variables and their relationships in the in¯ uence diagram framework was especially effective in discovering and resolving disagreements to achieve agreement on the problem structure itself. Second, it was ¯ exible enough to change the perception of the problem and reframe it. As shown, the analysis from the AT&T corporate point of view rather than each business unit changed the nature of problem, and provided a strong rationale for cooperation between the two parties. Third, the approach made it possible to separate the formulation and the value judgment of the negotiation problem, so it became easier to focus attention on a speci® c issue and identify disagreement on the issue.

As a result of the successful negotiation, business unit A was able to deploy the USDS platform and let all AT&T calls go through the platform to achieve maximum use. On the other hand, business unit B was able to get support for targeted marketing efforts in return for their cooperation. By successfully resolving con¯ icting interests before an information system is implemented, it was estimated that AT&T saved at least \$6.9 million dollars after tax during the ® ve year planning horizon. The USDS platform is now fully in service in the network as of June 1996.

Case studies on IS failures give important insights into the pattern of events leading to failures and provide opportunities for improving the process. We believe that IS can be implemented more successfully by learning from the history of failures and acting proactively to resolve any issues which can lead to a failure. From our experiences, we believe that the decision analytic approach is a viable and very useful tool in addressing organizational issue like resolving the con¯ ict of interests among the stakeholders in the IS implementation process. The case presented in this paper showed how to resolve the con¯ icts and demonstrated the value of the approach.

## Acknowledgement

We are grateful to the editor and anonymous reviewers for their helpful suggestions on an earlier draft of this paper. Their suggestions greatly improved its presentation.

## References

Adel-Hamid, T.K. and Madnick, S.E. (1990) The elusive silver lining: how we fail to learn from software development failures. Sloan Management Review, 32, 39± 48.

Ahn, J. and Skudlark, A.E. (1995) Value of CCS-BCS Cooperation for Universal Subscriber Data Structure (USDS) Platform Implementation. AT&T Bell Labs Technical Memorandum, ITD-95-28367H.

Alter, S. (1992) Information Systems: A Management Perspective. Addison-Wesley. Reading, MA.

Alter, S. and Ginzberg, M.J. (1978) Managing uncertainty in MIS implementation. Sloan Management Review, 19, 23± 31.

AT&T (1995) CADET (Computer Aided Decision Evaluation Tool) Version 1.2 Manual.

Bailey, J. and Pearson, S. (1983) A tool for computer user satisfaction. Management Science, 29, 530± 45.

Benbasat, I., Goldstein, D.K. and Mead, M. (1987) The case research strategy in studies of information systems. MIS Quarterly, 11, 369± 86.

Beynon-Davies, P. (1995) Information systems ©failureº : the case of the London ambulance service’s computer aided despatch project. European Journal of Information Systems, 4, 171± 84.

Clemen, R.T. (1996) Making Hard Decisions. 2nd Edn, Duxbury Press, Belmont, CA.

Corner, J.L. and Kirkwood, C.W. (1991) Decision analysis applications in the operations research literature, 1970± 1989. Operations Research, 39, 206± 19.

Curie, W. (1994) The strategic management of a large scale IT project in the ® nancial services sector. New Technology Work & Employment, 9, 19± 29.

DeSanctis, G. (1983) Toward friendly user MIS implementation. Communications of the ACM, 26, 732± 38.

Ewusi-Mensah, K. and Przasnyski, Z.H. (1995) Learning from abandoned information systems development projects. Journal of Information Technology, 10, 3± 14.

Gladden, G.R. (1982) Stop the life-cycle, I want to get off. Software Engineering Notes, 7, 35± 39.

Howard, R.A. (1988) Decision analysis: practice and promise. Management Science, 34, 679± 95.

Howard, R.A. and Matheson, J.E. (1983) Readings on the Principles and Applications of Decision Analysis. Strategic Decision Group, Menlo Park, CA.

Jin, K.G. and Franz, C.R. (1986) Obstacle coping during systems implementation. Informaton and Management, 11, 65± 75.

Keen, P. (1981) Information systems and organizational change. Communications of the ACM, 24, 24± 33.

Kreps, D. and Wilson, R. (1982) Sequential equilibrium. Econometrica, 50, 863± 94.

Lucas, H.C. (1975) Why Information Systems Fail. Columbia University Press, New York, NY.

Lucas, H.C. (1976) The Analysis, Design and Implementation of Information Systems McGraw-Hill, New York.

Lyytinen, K. and Hirschheim, R. (1987) Information systems failures ± a survey and classi® cation of the empirical literature. Oxford Surveys in Information Technology, 4, 257± 309.

Con¯ ict of interests in IS implementation

Markus, M.L. (1983) Power, politics and MIS implementation. Communications of the ACM, 26, 430± 44.

Owen, G. (1995) Game Theory, 3rd Edn, Academic Press, San Diego.

Oz, E. (1994a) Information systems mis-development: The case of Star\*Doc. Journal of Systems Management, 45, 30± 4.

Oz, E. (1994b) When professional standards are lax: the Con® rm failure and its lessons. Communications of the ACM, 37, 29± 36.

Raheb, S.E. (1992) There’s no excuse for failure: tips on how businesses can develop effective information systems. Canadian Manager, 17, 18± 19.

Raiffa, H. (1982) The Art and Science of Negotiation. Harvard University Press, Cambridge, MA.

Robey, D. and Markus, M.L. (1984) Rituals in systems design. MIS Quarterly 8, 5± 15.

Sauer, C. (1993) Why Information Systems Fail: A Case StudyApproach. Alfred Waller, Henley-On-Thames, UK.

Schein, E. (1969) Process Consultation: Its Role in Organizational Development. Addison-Wesley, Reading, MA.

Sebenius, J.K. (1992) Negotiation analysis: a characterization and review. Management Science, 38, 18± 38.

Selten, R. (1975) Re-examination of the perfectness concept for equilibrium points in extensive games. International Journal of Game Theory, 4, 25± 55.

Ubokudom, S.E. (1993) The Kansas ® nancial information system (KFIS): policy design and policy failure. Public Budgeting & Finance, 13, 63± 72.

## Biographical notes

Jae-Hyeon Ahn is a senior technical staff member in AT&T Labs, New Jersey. He received a BS and an MS in industrial engineering from Seoul National University, South Korea. He received a PhD in Engineering± Economic Systems from Stanford University in 1993. He has research and consulting experiences in the telecommunications, energy and health industries. His current research interests include strategy analysis in the telecommunications industry, business case analysis, Bayesian network modelling and medical decision making. His papers appear in Management Science, European Journal of Operational Research and Decision Support Systems.

Ann E. Skudlark is a technical manager in AT&T Labs, New Jersey. She received a BS from the University of Rhode Island and an MBA from the University of South Florida. She supervises a decision and intelligent systems group which supports and enhances business decision making process. Her current research interests include formalizing scenario planning in the decision analysis process and understanding risk management implications in electronic commerce. She has published in the Journal of Direct Marketing.
