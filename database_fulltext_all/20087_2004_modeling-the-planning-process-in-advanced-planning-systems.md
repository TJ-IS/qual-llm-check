---
otero_id: 20087
otero_key: "QAV5JV7W"
title: "Modeling the planning process in advanced planning systems"
authors: "Anastasia J. Zoryk-Schalla; Jan C. Fransoo; Ton G. de Kok"
year: "2004"
journal: "Information & Management"
doi: "10.1016/j.im.2003.06.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Modeling the planning process in advanced planning systems

Anastasia J. Zoryk-Schalla<sup>a</sup>, Jan C. Fransoo<sup>b,\*</sup>, Ton G. de Kok<sup>b</sup>

<sup>a</sup>IBM Deutschland, Du¨sseldorf, Germany

<sup>b</sup>Department of Technology Management, Technische Universiteit Eindhoven, P.O. Box 513, Pavilijoen F12, NL-5600 MB Eindhoven, The Netherlands

Received 20 December 2002; received in revised form 4 April 2003; accepted 13 June 2003

Available online 9 April 2004

## Abstract

Whereas much of the modeling literature in supply chain planning addresses the analysis of decision models and presents solution techniques and much of the empirical literature on planning systems such as ERP and APS software addresses implementation challenges from an organizational perspective, research on the modeling process of capturing the planning process in planning software is very scarce. In this paper, we examine this modeling process. Our approach is based on a normative method for hierarchical planning and presents a case study where this modeling process was used. We analyze the process, relate it to the literature on modeling, and demonstrate the value of the theory in explaining major observations. We conclude that the hierarchical premise on which most planning processes are based is very difficult to capture in an advanced planning system, and find that users and organizations essentially circumvent this problem by creating their own workflows, independent of the system’s prescribed one.

<sup>#</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Advanced planning systems; Implementation; Modeling; Requirements determination

## 1. Introduction

‘‘One of the key success factors for successful implementation of Advanced Planning and Scheduling (APS) systems is correct and consistent modeling’’. While this perception may be shared by many, it has not been examined. Research on which models for supply chain planning are developed, analyzed, and tested is abundant (e.g., see [10]). In that area, two types of modeling can be distinguished:

1. Observations are made in the real world and captured in simplified models and researchers try to capture the essence of the planning problem. The model is then analyzed, and insights are developed.

2. The focus is on approximate analysis and a solution. The research is generally axiomatic [1] and not empirical, though models are used extensively in many software solutions.

The empirical work on the implementation of planning systems is not as widespread, but exists. It focuses on the strategic and organizational conditions for successful implementation, on the problem of fit between an ERP System and the organization, and the problem from a project management perspective; e.g. [12,13,20]. Since companies—depending on their size—invest hundreds of thousands of Euros (or more) in licensing the software, a significant part being spent on hiring external consultants and making internal people available to make the implementation run smoothly [6], interest in a better understanding of the success and failure factors of software implementations is high.

In the IS literature, modeling the business process has been discussed extensively as information requirements determination (IRD) or user requirements determination [7,8]. An extensive review is given by Browne and Ramesh [5] in their discussion of the cognitive aspects of IRD. While information requirements methodologies generally assume complete capturing of requirements, they do not discuss the specific issue of modeling of planning processes.

Here, we specifically discuss the modeling of the planning process in APS systems. We recognize that other aspects, such as management commitment, setting clear targets, etc., are highly relevant in software implementation, but we abstain from analyzing them; instead, we focus on the modeling process. In order to describe the characteristics of the planning process structure, we build on the work by Schneeweiss [17]. We use his description as a basis for a description and analysis of a case study, which was conducted over 2 years and in which the entire implementation process was documented from a modeling perspective.

## 2. The planning process: theory

In both empirical studies and axiomatic models, it is generally assumed that planning processes are ordered hierarchically [2,3,11,14]. A formal modeling framework for describing hierarchical planning processes was proposed by Schneeweiss. He modeled the interactive process of decision making between two hierarchical levels, in which the higher one anticipates the decisions that may be made by the lower one as a consequence of a set of possible decisions at the higher level. This anticipation is an essential concept, since it requires explicit consideration of the lower level model at the higher level, requiring a formal aggregation process that includes aggregation of products and resources (like the models reviewed by Bitran and Tirupati [3]) and also an aggregation of the decisionmaking process itself.

A decision structure within an organization is represented as a series of decision pairs (tandems), i.e., two decision levels interacting with each other by the first (the top level) giving an instruction to the second (the base level), and the second responding. Before giving its instruction, the top level anticipates the reaction by modeling, either implicitly or explicitly, the behavior of the base level. This is termed an anticipated base model. In general, this can be constructed based on aggregating information and/or on aggregating the base level model.

This cyclic process is shown in Fig. 1.

The top level optimizes its operation using an objective function (in its decision model). Schneeweiss also defines Aspiration Levels (AL), which are lower bounds of the criterion to be reached by the top level. Within each cycle of a hierarchically structured decision process, there is a top–down influence on the base level. Each decision at the top produces an instruction to the base. This influences all components at the base level, which takes this instruction and reacts back to the top. It is important to understand the basic premise that giving instructions or deciding upon reactions will not be performed without knowledge of the other’s decision process. Furthermore, instructions and reactions between the top and the base do not influence the process being controlled; these are termed factual decisions. Only the final outcome of the process between the two levels leads to a decision that is implemented in the real process: a final decision.

The model has four types of anticipation: exact explicit reactive, approximate explicit reactive, implicit reaction, and non-reactive. De Kok and Fransoo [9] make these more specific to the supply chain planning structure by introducing the idea of effectuation lead time. This is the time that elapses between the moment a decision is made and the time that the consequences of this decision can be observed in the operations of the supply chain. An example occurs in the procurement lead time of components: once the decision to procure a component is made, it will take some time (order processing and planning time at the supplier, physical lead time of producing and shipping the component to the customer, etc.) before that decision is effectuated and the component is available. During this delay the real world changes, and when lower level decisions are likely to be made after the component arrives (possibly the operation now needs more material than was ordered or there is another more important customer to satisfy first), the lower level may decide to fill a different order using this component. This information asymmetry is explicitly included in our approach.

![](/api/attachments/QAV5JV7W/fulltext/images/478839ec343e02c5f821f4bfff0bf3b93f7938b839c9de485101ebd64600d34b.jpg)  
Fig. 1. Decision cycles in the decision hierarchy. Factual decisions are denoted by (\*); the final decision by (\*\*).

We have previously discussed various ways of aggregating the lower into higher level models. Aggregation is a process for simplifying a problem by defining condensed data and decision variables. By considering different hierarchical levels and separate decision models, we can say that the basic difference at each level is in the degree of aggregation. It therefore achieves a reduction of data requirements and of model complexity. This makes a distinction between aggregating the model and aggregating information. Furthermore, there are two kinds of anticipation:, explicit and implicit. Aggregation referring to the model part explicitly deals with complexity reduction. At the top level the decision-making process is represented by an aggregate and simple model in order to reduce complexity and to distribute detailed decisions to lower planning levels. The terms explicit and implicit depend on whether the top-level base model (including the criterion) is the same as the base-level. If this is the case, it is termed explicit anticipation; if not, it is implicit anticipation. Explicit anticipation thus uses a detailed model of the base level, whereas implicit anticipation uses an aggregate model.

## 3. Case description: ALCO

We now describe the supply chain characteristics of the case under consideration by introducing its products, manufacturing facilities, relevant suppliers and service centers.

## 3.1. Supply chain characteristics of ALCO

Our study concerns the implementation of software at a European multi-billion Euro revenue aluminum manufacturing company; we will call this corporation ALCO. It has plants and subsidiaries both in several European countries and outside Europe. ALCO covers a broad range of products, including primary and secondary metal, rolled products for the packaging markets and technical applications, flexible packaging materials for food service and pharmaceutical uses, and finished goods, such as aluminum ladders and household foil. In this case study, we limited ourselves to the ‘‘Rolled Products’’ Division.

This Division used to have two locations: the Aplant and B-plant. The B-plant was a 50% ALCO owned company and a very important supplier of input material about 65% of all input raw materials for the A-plant was supplied by them. The B-plant delivers pre-rolled raw material. Just prior to the start of this study, the Division acquired an additional number of European rolling mills as a first step towards globalization of the company’s operations. This entire set of plants together with a number of significant suppliers and subcontractors formed ALCO’s supply chain. The initial implementation of the software system was conducted at ALCO’s A-plant. The entire supply chain is depicted in Fig. 2.

## 3.2. Overview of decisions in the supply chain

The planning decisions were distributed among three categories: strategic, tactical, and operational planning. Following the terminology used by the selected APS vendor, we term the tactical planning decisions as Master Planning (MP) and the operational planning decisions as Factory Planning.

While acknowledging the importance of strategic planning, given the expense involved in changing strategic direction at capital intensive companies, it is relatively infrequently implemented. The focus here is therefore on Master Planning: given assets, identified markets and products, and strategic business objectives, what is the best way to achieve the maximum return? While the process of MP can vary from company to company, the end objectives and outputs are very similar. The principal outcome is a multiperiod plan that includes the following:

![](/api/attachments/QAV5JV7W/fulltext/images/58a05a4181b74c217ee0bb40607a2764c82882c32bb2e16e7f8e300789071f00.jpg)  
Fig. 2. Supply chain of the Rolling Division of ALCO.

\- Products to be sold in a particular time period. This is divided into regions, sales offices, customers, etc.; i.e., it is allocated to markets.

\- Products for which market demand exceeds production capacity (this is an input into strategic planning).

\- Products to be manufactured at each facility in a particular time period (sourcing of products).

\- Labor required to produce the products (typically down to number of shifts required per week in a facility).

\- Raw material and inventory required to produce the products.

\- Performance measures like expected level of inventory at the beginning and end of the period and inventory trends during the period.

\- Performance measures, like the total revenue, cost, and profit.

## 3.3. Prior performance and perceived problems

Since production used to be limited to two closely related sites with a clear and fairly straightforward routing structure, supply chain planning was not developed as a function in the company until the acquisitions of additional sites. During the last years, positions had been created for people responsible for this new planning task. The challenge and improvement potential seemed large, as very little coordination amongst the plants existed. The new APS software was intended to support the decision-making process. In addition, however, the new software also was to replace the legacy software for Factory Planning and two-stage synchronization between the rolling mill (A-plant) and the raw material supplier (B-plant).

There was no common planning tool for the whole ALCO supply chain, incorporating both production facilities and suppliers. While local visibility at the Aplant’s shop floor was very high, visibility at the planning level could be improved so that there would be a uniform view of the A-plant and the B-plant in one planning system. In particular, the customer order due dates were quoted with just a rough check of the available capacity at the B-plant. Furthermore, it was very difficult to tune production planning between the sites due to lack of knowledge of the available capacity. The management expected that after the software implementation had been completed, ‘‘a businesswide optimal plant loading, integration between the B-plant and the A-plant, and business-wide optimized product decisions can be achieved’’ (quote from the project definition document). At the individual sites, it was expected that planning could be improved through upstream and downstream visibility of constraints.

ALCO lacked a planning tool for the management and control of inventories. Frequent component inventory stockouts resulted in machine downtime; frequent ordering of wrong materials led to a need for high stocks. Inventory levels were therefore too high but availability of intermediate and finished products from inventory was low. With regard to inventory management, it was expected that after the new software implementation, inventory could be reduced (planned rather than result from crises and planning actions).

The level of customer service was also seen to be insufficient due to incorrect lead time predictions; planning was based on deterministic and static manufacturing lead times, which could vary according to actual capacity and material situations in the plants and low visibility of late orders. Customer service levels varied across products and over time; e.g., some product families at various periods of time had levels as high as 95%, while for other products could have as little as 20%. The system did not provide sufficient visibility and support to provide good lead time estimates for quoting due dates, neither did it provide the Master Planner with details about late orders. With regard to customer service, it was expected that after the new software implementation, transparency of order status and delays could be achieved. It was intended that capacity and material constraints could be incorporated in the real-time due date quotation.

Finally, the current system did not support rapid response. The average time taken to create a balanced sales and operating plan ranged between 3 days to a week of actual working time, by which time much of the input information could have changed and the value of the plan seriously doubted. Additionally, a significant proportion of the planners’ time was spent on tasks like meetings, reports, maintaining data— tasks that prevent him from making what-if analyses and thus improving the plans.

## 3.4. i2 TradeMatrix tool capabilities

Advanced Planning and Scheduling systems are software tools that enable companies to make decisions about supply chain structures, long-term supply plans, and detailed operational schedules [19]. A wide number of large and small vendors market APS software solutions, including i2 Technologies [21], a market leader over recent years.

The general the software is based on a hierarchical structure, consisting of three levels: Demand Planner, Master Planner, and Factory Planner. The Demand Planner generates the forecasts per product/product group (based on historical/statistical data, market strategies, etc.). The Master Planner module creates a plan for the ALCO supply chain by integrating business policies, market demand, and supply chain capabilities into a common plan. The Master Planner updates the operational plan based upon revised sales forecasts from the Demand Planner, and changes in manufacturing capability and resource availability. Factory Planner determines at which time each manufacturing operation of a given customer order should be performed on which particular resource by creating a factory-wide plan. The ALCO solution includes four separate Factory Planner models, one for each of the production sites. The output of the Factory Planner will be used as an input to the more detailed scheduling (sequencing) of manufacturing orders at the shop floor level and as a basis for procurement. These functions are not performed by the i2 TradeMatrix software.

The scope of the implementation also includes the implementation of a due-week quoting process for customer orders. This will be performed by the i2 TradeMatrix ATP (Available-to-Promise [15]) model, connected to the ALCO Order Entry System. The basis for the given quotes is the ATP allocations created because of the MP process. The ATP model will have only a single connection (or ‘‘point of entry’’) to the ALCO Order Entry Systems. The ATP model will operate on a daily basis, in conjunction with the Order Entry system. Fig. 3 shows the various modules and the way they are to be implemented.

We now briefly discuss the way in which the various business processes and models are expected to operate under the new planning regime. The DP model will support a plant-independent sales department representing all four plants. Based on demand data, an unconstrained sales forecast is generated by DP, which supports a multi-dimensional representation of demand according to customers/geography, products, and time. Committed forecasts per Planning Item (i2’s term for aggregate items) are given either by the sales department or by using the DP module. These forecasts are used as input for the MP module, which generates a 12-month plan that is capacity-feasible.

![](/api/attachments/QAV5JV7W/fulltext/images/9e8f8ccc883b6d885383fe527f42a37bcb9bff1001108dd207def463a65cfc2c.jpg)  
Fig. 3. Implementation of i2 TradeMatrix modules at ALCO’s Rolling Division.

The result is a feasible allocation per Planning Item and week. Obviously, this allocation can differ from the original sales forecast. The consequence is that either, based on negotiations with the sales department, replanning has to be performed with a modified forecast or that the allocations are accepted. Customer order quoting is then based on the agreed allocations, using ATP. In this process the specific aggregation/ disaggregation procedures are a key factor to actual performance. In the first model of the implementation, DP has not yet been implemented and forecast data comes directly from the sales department.

After implementation, 18 users will be involved in the use of the software. These include seven users of Factory Planner, six users of Master Planner, and five users of Demand Planner.

## 3.5. The implementation approach at ALCO

The implementation of the tool was directed by a consultant with extensive experience in implementing the software across a variety of industries, including metals. Furthermore, two consultants, one of whom was experienced, were almost continually on-site and worked on modeling the processes in the tool.

Simultaneously, a project team of ALCO worked with the consultants to define the processes.

The implementation approach at ALCO was based on i2’s methodology of business releases. In this, a simple model is first created; it should be able to reap the first business benefits. In subsequent phases, the model is extended and refined to capture the improvement potential. In between the business releases, further refinement takes place. Here, we focus on the first four business releases (BR1–BR4). In hindsight, we have distinguished five phases of implementation for these four business releases. The business releases and their timing are presented in Table 1.

The phases are actual parts of the project implementation. Although they were not set up in advance, they characterize the content of the process. Following the Business Release Methodology, phase 1 had its focus on developing a first simple model of the A-plant with limited functionality and limited complexity. Phase 2 described the modeling activities within the software that were necessary to achieve the functionalities. In this phase, the detailed modeling of a production site took place; it included the formal definition of material buffers for bottleneck resources and work in process, the definition of groups of product items (planning items), resources, and manufacturing operations, including their lead times. The specific challenge there was, while modeling, to find the correct balance between a model that was easy to maintain and understand and a model that had sufficient detail so that planning results were realistic.

Table 1  
Phases identified for description of project implementation

<table><tr><td>Phases</td><td>Description</td><td>Duration (months)</td><td>Originally planned as</td><td>Planned duration of BR (months)</td></tr><tr><td>1</td><td>Initial requirements and criteria setting</td><td>2</td><td rowspan="2">BR1</td><td rowspan="2">4</td></tr><tr><td>2</td><td>Initial modeling</td><td>8</td></tr><tr><td>3</td><td>Model modification</td><td>3</td><td>BR3</td><td>3</td></tr><tr><td>4</td><td>Model extension and advanced requirements and criteria setting</td><td>5</td><td>BR2</td><td>6</td></tr><tr><td>5</td><td>Advanced modeling</td><td>8</td><td>BR4</td><td>6</td></tr></table>

After having completed phase 2, planners were confronted with the prototype model. Key users had to understand its usage, the user interface, reveal possible modeling errors, and decide on further improvements.

Accordingly, phase 3 focused on main repair work and remodeling. Specifically, planners and modelers became aware of the high modeling complexity with which APS tools have to contend and they had to revise solutions already implemented. Originally, this was not expected to happen until BR3. Phase 2 formally completed BR1, after which the MP was supposed to be live; in fact, it was delayed until after phase 3, but the planners found the process helpful, in an isolated setting, while they still had access to the legacy systems and spreadsheets.

Phase 4 mainly focused on the business processes that should be supported by the newly developed tools. The processes had to be seen in conjunction with all legacy systems that were still part of the planning process. In traditional IS development, definition of business processes is made before any modeling activities are started. As this was not the case, the definition of business processes revealed further modeling mistakes to be corrected.

Phase 5 represented an extension to the already existing prototype model, which was focused on the development of a Due Week Quoting Process, based on the existing planning results.

The cumulative throughput time of the phases of implementation considered was 26 months, though initially a throughput time of 19 months was anticipated.

The process description already reveals that the methodology does not provide a clear and extensive IRD phase. Requirements were given by business objectives rather than the needs of the workflow processes. In fact, the vendor’s methodology is somewhat similar to prototyping, in that prototyping allows various stages to be implemented as an emerging workable version [4]. Furthermore, the implementation uses a packaged solution that needs to be configured. However, the extremely high degree of freedom that exists in the modeling phase in APS systems makes the configuration of the system somewhat akin to developing a system from scratch.

## 4. Case study analysis

## 4.1. Data collection

One of the authors was actively involved in the case study as a project manager of one of the subprojects. She collected all data about the implementation project, including:

\- reports from project meetings;

\- project reports;

\- project definition documents;

\- interviews with end users and other gathering of end-user experiences;

\- observations during the implementation process;

This information was carefully collected, organized, and described extensively and retrospectively in a research document [22]. The other authors assisted in composing this document and in conducting the analyses of the results. In the analyses, the data from the study, documented as a series of observations, were related to the literature and theoretical treatise.

We first discuss the observations that are directly related to the actual model in the APS and then analyze the observations.

## 4.2. The APS model

Schneeweiss [17] distinguishes three characteristics as principal components in hierarchical planning systems: the Aspiration Levels set by the decision maker, the recognition of stochastic information (leading to information asymmetry), and the existence of anticipation functions (as a means of dealing with information asymmetry). In the model using the TradeMatrix software, difficulties could be identified for each of these characteristics.

Aspiration levels are values of a criterion that are essential for the decision maker. There can be a discrepancy between the formal optimal value of the decision maker’s criterion and the perceived possible Aspiration Level. Only if this discrepancy can be removed can the whole process terminate and a final decision made. The decision maker will constantly need to revise the model and input parameters until the optimal value satisfies at least the Aspiration Level. Alternatively, the decision maker may decide to reduce the Aspiration Level. In the APS software the aspirations level of a centralized Master Planning Model can be expressed by business rules/business objectives which have to be fulfilled. As an example, consider the criterion C as one of maximizing demand satisfaction according to predefined forecasts. The Aspiration Level (AL) is defined as the minimum demand level that has to be fulfilled in any case. The APS software does not recognize this Aspiration Level as such. Therefore, although Aspiration Levels in Schneeweiss’s concept are not considered as constraints, in terms of the APS software it can only be entered as a constraint, possibly leading to infeasibility. The second way of dealing with Aspiration Levels is to define an objective function in the first step, e.g. maximize demand, without knowing the optimum solution $C ^ { * } .$ . It is up to the judgment of the planner to assess whether $A L$ has been met if his Aspiration Level is higher than $C ^ { * }$ and to play with objective functions and constraints such that he meets AL. At ALCO, in phases 1 and 2, the Aspiration Levels were defined as constraints using the business rules feature of the APS software. When the planners were testing the system and comparing the perfor mance with the legacy systems, they discovered that the APS system rendered infeasible solutions while they thought that feasible solutions existed. Consequently, the Aspiration Levels were not made explicit in the system and the planners manipulated the model inputs in order the get a feasible solution.

Stochastic information consists of probability distribution functions of all random variables occurring in the decision model. The APS software does not explicitly take into account stochastic information. The underlying optimization model is a deterministic mathematical model involving multiple constraints and some objective function. Uncertainty is considered in three distinct ways:

\- Estimating (i.e. forecasting) exogenous random variables, such as future demands.

\- Introducing slack parameters, such as safety stocks and excess capacity, which are incorporated into constraints and/or the objective function.

\- Replanning, as incorporated in a rolling schedule approach.

In the MP model of the initial modeling phase, future demand was not entered as stochastic information but as a point estimate, based on historical data. Therefore, uncertainty would be dealt with in an iterative manner, using a rolling schedule approach and obviously not according to the suggestion that uncertainty needs to be considered by anticipating the lower level behavior at the higher level. But there is an essential flaw in such an approach: if demand, lead times, and other exogenous variables are not set as random variables, structures of optimal planning strategies are likely to differ significantly from the strategies that utilize the combination of a rolling schedule approach with deterministic optimization. It can be argued that the mental model of experienced planners considers this implicitly.

In the first two phases of implementation, rules and principles of anticipation were not seen to be an issue and were completely neglected. In view of this, in the initial modeling phase no type of anticipation function was considered. Since the Factory Planner models (base level models) were not developed then, an explicit definition of anticipation functions was not possible. In this stage of the project not even implicit approximate anticipation was achieved, since no netted forecast or netted capacity were actually uploaded. In phases 4 and 5, extensive changes in the modeling were made to accommodate for this relationship by including extremely implicit anticipation relationships through the use of fixed lead times and the use of MRP logic to coordinate the various Factory Planners.

## 4.3. Analysis of the APS model

The decision model used in the APS software is formal: it consists of objective functions and constraints. A formal model should capture reality in such a way that the users recognize the model as their perception of reality (the planner’s mental model, based on the cognitivist view that thought is representational [16,18]. Both the mental and the formal model are, by definition, different from reality.

![](/api/attachments/QAV5JV7W/fulltext/images/6ecc0d80980917dce133ce18afe7ff8cdc76671818148a5151ca8a88bd033d05.jpg)  
Fig. 4. Two models and reality.

The conceptual graph in Fig. 4 enables the assessment of the effectiveness of an APS system as a decision support tool for a planner. Our assessment is based on the following assumptions:

1. The input for the planning process is a sales plan that is exogenous to the planner.

2. The planner takes decisions of which the impact on actual sales can only be observed after some time has elapsed.

3. The planner is in control; i.e. whatever the APS system proposes, the planner has the ultimate responsibility to either follow the proposal, modify it, or reject it and propose an alternative.

The first assumption is typical for the supply chain management context. Given the sales plan, the planner proposes a production plan that ensures the realization of the sales plan, if possible. The second assumption implies that both planner and APS may propose production plans that either cannot be executed or do not exploit the capabilities of the firm. Conversely, sales plans may be rejected, implicitly or explicitly by APS or planner, though they are executable. The third assumption implies that the mental model of the planner is prime, implying that any APS proposal that is perceived to be infeasible by the planner will be rejected or modified.

Now let us consider possible courses of action that may occur after the sales plan is available. Both models decide whether this sales plan is feasible (F) or infeasible (I), depending on an explicit (APS) or implicit (mental) confrontation. Assuming that an outside observer has complete knowledge about the actual (in)feasibility of the sales plan, we can also ‘‘decide’’ on its (in)feasibility in reality. From this we can characterize eight different situations, as depicted in Table 2. Each of the situations is assessed in terms of the planner’s behavior and the actual performance. The planner’s behavior is characterized by four possible actions:

\- accept;

\- modify;

\- workaround;

\- propose modifying sales plan.

The first action implies that according to the planner the APS plan satisfies the sales plan in an appropriate way. The second action implies that according to the planner the APS plan does not satisfy the sales plan in an appropriate manner, or that the sales plan is infeasible according to the APS system and the planner finds workarounds within the APS to satisfy the sales plan, still. These workarounds relate to changes to APS outputs and inputs other than the sales plan, such as resource and utilization constraints. The third action implies that the planner performs workarounds outside the APS and communicates an alternative plan to his organization. The fourth action implies that the planner concludes that the sales plan is infeasible. Note that the second, third, and fourth action can occur simultaneously.

Table 2  
Feasibility (F) and infeasibility (I) in reality (R), the APS model (A) and the planner’s mental model (M)

<table><tr><td>A</td><td>M</td><td>R</td><td>Planners behavior</td><td>Performance</td><td>Impact on acceptance APS</td></tr><tr><td>F</td><td>F</td><td>F</td><td>Accept APS plan</td><td>Sales plan realized as expected</td><td>Neutral</td></tr><tr><td>F</td><td>F</td><td>I</td><td>Accept APS plan</td><td>Sales plan unexpectedly not realized</td><td>Neutral</td></tr><tr><td>F</td><td>I</td><td>F</td><td>Modify APS plan workarounds outside APS propose to modify sales plan</td><td>Sales plan not realized, while it was possible</td><td>Acceptance of APS deteriorates</td></tr><tr><td>F</td><td>I</td><td>I</td><td>Modify APS plan workarounds outside APS propose to modify sales plan</td><td>Sales plan not realized</td><td>Acceptance of APS deteriorates</td></tr><tr><td>I</td><td>F</td><td>F</td><td>Modify APS plan workarounds outside APS</td><td>Sales plan realized as expected</td><td>Acceptance of APS deteriorates</td></tr><tr><td>I</td><td>F</td><td>I</td><td>Modify APS plan workarounds outside APS</td><td>Sales plan unexpectedly not realized</td><td>Acceptance of APS improves</td></tr><tr><td>I</td><td>I</td><td>F</td><td>Modify APS plan workarounds outside APS propose to modify sales plan</td><td>Sales plan not realized, while it was possible</td><td>Neutral</td></tr><tr><td>I</td><td>I</td><td>I</td><td>Modify APS plan workarounds outside APS propose to modify sales plan</td><td>Sales plan not realized</td><td>Neutral</td></tr></table>

If the APS signals that the sales plan is feasible or infeasible, while the planner thinks the opposite and this is confirmed after actual execution, then this raises serious doubts. Only if the APS signals infeasibility, while the planner assumes feasibility, but turns out to be wrong, it is likely that the APS gains acceptance.

From this perspective, it is clear why planners find workarounds and use them extensively.

If we further specify this concept in the terminology of the different models that exist between the APS system and the planner, then we can describe the issues formally (cf. Fig. 5), using the following notation:

<table><tr><td> $I$ </td><td>Index indicating reality (R), the APS model (A), and the mental model of the planner (M)</td></tr><tr><td> $f_i$ </td><td>Objective function (relating the state to the performance)</td></tr><tr><td> $x_i$ </td><td>State</td></tr><tr><td> $f_i(y;x_i)$ </td><td>Performance for decision variable y</td></tr></table>

Because $x _ { \mathrm { R } }$ and $f _ { \mathrm { R } }$ cannot be observed, the actual status of reality is formally unknown; in fact, it only exists as a representation in the planning system $( x _ { \mathrm { { R } } } x _ { \mathrm { { A } } } )$ or as a representation in the mental model of the planner $( x _ { \mathrm { R } } x _ { \mathrm { M } } )$ . Further note that the actual realized performance $( f _ { \mathrm { R } } ( x _ { \mathrm { R } } ) )$ can only be observed ex post.

A similar formulation can be used for the representation of constraints. We use the function $g _ { i }$ for this matter; $b _ { i }$ will be used for the right hand side. Finally, we use y to denote the decision variables in the planning problem. Using this notation, the process of planning using the APS software and the Aspiration Levels, can be described as:

![](/api/attachments/QAV5JV7W/fulltext/images/7bce0dde638ae1b75b5f8794a0c92ac1c30eeb39e60a0bf11464afbe6b02de50.jpg)  
Fig. 5. Difference in state descriptions (x<sub>i</sub>) objective functions $( f _ { i } ) .$ and performance $( f _ { i } ( x _ { i } ) )$

## 4.3.1. Problem

$$
\min f _ {\mathrm{A}} (y; x _ {\mathrm{A}})\tag{1}
$$

$$
\text { subject   to } g _ {\mathrm{A}} (y; x _ {\mathrm{A}}) \leq b _ {\mathrm{A}}\tag{2}
$$

This can either result in infeasibility or in a feasible, optimal solution $y ^ { * } .$ such that

$$
g (y ^ {*}; x _ {\mathrm{A}}) \leq b _ {\mathrm{A}}\tag{3}
$$

Aspiration Levels are set by the planner as

$$
f _ {\mathrm{A}} (y; x _ {\mathrm{A}}) \geq \mathrm{AL}\tag{4}
$$

Furthermore, the planner will check whether

$$
f _ {\mathrm{M}} (y ^ {*}; x _ {\mathrm{M}}) \geq \mathrm{AL}\tag{5}
$$

If $f _ { \mathrm { M } } ( y ^ { * } ; x _ { \mathrm { M } } ) \le \mathrm { A L }$ , planners may change the plan (y). When this happens, difficulties due to different feasibilities between M and A will occur. From the model, it can be seen that the planner has additional options. The one observed in the case study was that planners adjust $x _ { \mathrm { A } }$ such that $f _ { \mathrm { A } } ( y ; x _ { \mathrm { A } } ) = f _ { \mathrm { M } } ( y ; x _ { \mathrm { M } } )$ without maintaining consistency between $x _ { \mathrm { A } }$ and $x _ { \mathbf { M } } .$ The model thus helps us in understanding some effects.

## 4.4. The modeling process

Following i2’s Business Release Methodology, the implementation started with a ‘‘simple’’ model: not all functionalities were implemented at once. Here, we will discuss some of the consequences this approach had on the actual implementation.

When starting the process, requirements for the software were formulated at a high aggregation level. These included conflicting objectives, such as minimizing lost sales, maximizing utilization, and minimizing inventory cost. No analysis was made to assess these conflicts. Furthermore, when the individual modules were defined, their specifications of were not linked to the original requirements. These inconsistencies led to selections being made from different requirements in different business releases. In fact, the requirements discussed in this phase of the project can be characterized as the Aspiration Levels that the business management and project management had decided on with respect to the performance of the supply chain after the APS system had been implemented. It included items like improved customer service, reduced lead times, and increased capacity utilization.

The implementation focused initially on modeling plant A before the other plants. Furthermore, within this plant, the focus was primarily on capacity plan ning. This scope was defined as Business Release 1 and was meant to obtain fast business benefits. It reduced the complexity of the model to one plant, and abstained from material coordination problems. When the model was released, this led to immediate problems with the planning of long lead time items. The aggregate items that were modeled at the Master Planner level (‘‘Planning Items’’) did not cover the items with a long lead time, but merely reflected the resource structure of plant A. Items with a common routing were aggregated into Planning Items, while long lead time items were not recognized at the Master Planning level. Furthermore, the later development of the model (in Business Release 2) to include multiple plants, led to serious problems, since the re-allocation decision (if there was a shortage of capacity in one plant, production of the item can take place in one of the others) was not incorporated into the data structure of the planning items. In fact, each item was defined from the perspective of one plant only. Since the software had already been released, this meant that the model in plant A had to be changed. But this was infeasible for organizational reasons (the model had already been developed and planners were working with it); furthermore, it had been expected that the addition of the new plants would be an extension of the existing model rather than a change to it. The project team chose not to model the re-allocation of products across plants and each item that existed in more than one plant received a different item identification for each of the plants. Trying to reduce complexity in BR1 thus prevented the project team from formulating requirements that were sure to be consistent.

Simultaneously, the focus on a simple initial model to get a quick implementation and ‘‘quick wins’’ led to a situation where the complexity of the planning solution was underestimated. The consequence is that not only the implementation of the partial prototype solution did not make sense, but also that remodeling, add-ons, and workarounds were necessary in order to make the solution acceptable.

No formal relationship between Master Planner and Factory Planner was considered. Depending on the specific relationship between the two hierarchically separated levels, this relationship can either be modeled as constraints from Master Planner [10], as instructions to execute certain tasks, or as release of production orders with agreed due dates. In a multi-echelon supply chain, this effectively means that inventory positions between various production units are managed at the higher level, whereas at the lower level, allocation of orders to machines (and possible sequencing and scheduling) takes place [2]. No rules and constraints for inventory management have been modeled in the project at ALCO. It turned out later that the requirements stated were not consistent with the consequence that although material buffers and safety stock levels were defined, they were not used for inventory management.

A second example of complexity underestimation occurred in the definition of business objectives, layers, and priorities. This definition needs a deep understanding of the model. When the first user impressions were gained after having worked with the prototype, planners realized that they could not really intervene in the solution process. Once having set the whole sequence of business objectives, the solution process became a black box from the planner’s point of view. After running the planning algorithm, the planner has to decide what to do if the proposed plan does not seem correct. This next cycle involves changing the sequence of business objectives and planning layers. Selecting the next cycle of decision making turned out to be difficult, as it corresponded to selecting a sequence of business objectives. Since the software does not assist the planners in understanding the consequences of changing the sequence of business objectives, the planners tended to iteratively adjust them. Finally, the model had to be simplified in order to allow the planners to work effectively with it. This simplification entailed a reduction in the number of echelons in the bill-ofmaterial of the products, a reduction in the number of products included in the Master Planning Model, and a reduction in the level of detail of the resources.

## 5. Conclusions and discussion

We have presented the results of a case study that analyzed the modeling process of the implementation project of i2 TradeMatrix, a major Advanced Planning and Scheduling software system. Both the model and the modeling process were described from the perspective of theoretical knowledge in modeling hierarchical planning processes. The case study demonstrated that many problems occur and that they can be linked directly to errors in the modeling process. A number of important assumptions, such as the ability to simplify the model to reach quick results and a move to abstain from explicitly modeling the hierarchical relationship between the two planning modules turned out to be wrong. The hierarchical planning models turned out to be valuable in developing explanations for the effects observed in the case study.

Our analysis suggests that APS tools may not be capable of assisting the modeler in properly defining the planning process and planning model. Extensive support from highly trained modelers is necessary. Moreover, since humans must play an essential role in operating the advanced planning system, it can be argued that the actual knowledge about hierarchical planning structures and algorithms is still insufficiently developed to allow for easy implementation using IT tools. The implementation of advanced and complicated tools such as APS systems will probably remain difficult. It seems that the only way to deal with this is to take time and be aware of difficulties.

This study was different from other studies in several ways. First, we were able to document the implementation of an APS system including all its modeling steps during a real process. Second, the project had to face many more difficulties than we had anticipated. Finally, the literature on hierarchical production planning turned out to provide a number of probable explanations as to why there were so many problems in this project.

## References

[1] J.W.M. Bertrand, J.C. Fransoo, Operations Management Research Methodologies using quantitative modeling, International Journal of Operations and Production Management 22 (2), 2002, pp. 241–264.

[2] J.W.M. Bertrand, J.C. Wortmann, J. Wijngaard, 1990, Production Control: A Structural and Design-Oriented Approach, Elsevier, Amsterdam.

[3] G.R. Bitran, D. Tirupati, 1993. Hierarchical production planning, in: S.C. Graves, A.H.G. Rinnooy Kan, P.H. Zipkin

(Eds.), Logistics of Production and Inventory, North-Holland, Amsterdam.

[4] B.H. Boar, Application Prototyping: A Requirements Definition Strategy for the 1980s, Wiley, New York, 1984.

[5] G.J. Browne, V. Ramesh, Improving information requirements determination: a cognitive perspective, Information & Management 39, 2002, pp. 625–645.

[6] G. Bylinsky, The challenges move in on ERP, Fortune 140 (10), 1999, pp. 306C.

[7] T.A. Byrd, K.L. Cossick, R.W. Zmud, A synthesis of research on requirements analysis and knowledge acquisition techniques, MIS Quarterly 16 (1), 1992, pp. 117–138.

[8] G.B. Davis, Strategies for information requirements determination, IBM Systems Journal 21, 1982, pp. 4–30.

[9] A.G. de Kok, J.C. Fransoo, Planning Supply Chain Operations: Definition and Comparison of Planning Concepts, 2003 (in: [11]).

[10] A.G. de Kok, S.C. Graves (Eds.), Supply Chain Management: Design, Coordination and Operation (Handbooks in Operations Research and Management Science, vol. 11), Elsevier, Amsterdam, 2003.

[11] A.C. Hax, D. Candea, 1984. Production and Inventory Management, Prentice-Hall, Englewood Cliffs.

[12] K. Hong, Y. Kim, The ciritical success factors of ERP implementation: an organizational fit perspective, Information and Management 40, 2002, pp. 25–40.

[13] M.L. Markus, C. Tanis, 2000. The enterprise systems experience—from adoption to success, in: R.W. Zmud (Ed.), Framing the Domains of IT Management: Projecting the Future, . . ., Through the Past, Pinnaflex Educational Resources, Cincinnati.

[14] H.C. Meal, Putting production decisions where they belong, Harvard Business Review 62 (2), 1984, pp. 102–111.

[15] J. Orlicky, Material Requirements Planning: the New Way of Life in Production and Inventory Management, McGraw-Hill, London, 1975.

[16] Z.W. Pylyshyn, Computation and Cognition: Towards a Foundation for Cognitive Science, MIT Press, Cambridge, 1984.

[17] C. Schneeweiss, Hierarchies in Distributed Decision Making, Springer, Berlin, 1999.

[18] G.F. Smith, Defining managerial problems: a framework for prescriptive theorizing, Management Science 35 (8), 1989, pp. 963–981.

[19] H. Stadtler, C. Kilger (Eds.), Supply Chain Management and Advanced Planning: Concepts, Models, Software and Case Studies, second ed., Springer, Berlin, 2002.

[20] J. Swan, S. Newell, M. Robertson, The illusion of ‘best practice’ in information systems for operations management, European Journal of Information Systems 8 (4), 1999, pp. 284–293.

[21] http://www.i2.com, April 2003.

[22] A.J. Zoryk-Schalla, Modeling of Decision Making Processes in Supply Chain Planning Software: A Theoretical and Empirical Assessment of i2 TradeMatrix, Unpublished Ph.D. Thesis, Technische Universiteit Eindhoven, Eindhoven, 2001, online available at http://alexandria.tue.nl/extra2/200210477.pdf.

![](/api/attachments/QAV5JV7W/fulltext/images/9de8db6794b1751b83c080f8b4c944ac74f76b53149586e8fe56e3f685d48a13.jpg)

Anastasia J. Zoryk Schalla is senior consultant at IBM Business Consulting Services, Germany. She holds an MSc in mathematics for Rheinisch Westfa¨lische Technische Hochschule Aachen (RWTH), Germany, and a PhD in industrial engineering and management science from Technische Universiteit Eindhoven. She has worked as a project manager at the Central Commercial Department at

ALCO, Germany, being responsible for supply chain management implementation projects and business process re-engineering for all planning processes in four European plants. Her interests lie in the area of production planning and control and supply chain management. She has published in journals as Production and Operations Management Systems, Production Planning and Control, VDI-Nachrichten, ID-Spezial, Arbeitsvorbereitung.  
![](/api/attachments/QAV5JV7W/fulltext/images/8b035a6dad585067261429a4e693ac0ba8ca5b4220cbd55cb9eaa026faa9d2c9.jpg)

Jan C. Fransoo is full professor of operations planning and control at the Technische Universiteit Eindhoven and also serves as research director of the European Supply Chain Forum. He holds an MSc in industrial engineering and a PhD in operations management from Technische Universiteit Eindhoven and has held visiting positions at Clemson University, Stanford University, and The

Anderson School at UCLA. His research interests lie in the area of production planning and control and supply chain management, particularly in process industries. He has published in journals such as IIE Transactions, Journal of the Operational Research Society, European Journal of Operational Research, OR Spektrum, International Journal of Operations and Production Management, International Journal of Production Economics, Production and Operations Management, Transportation Research, Supply Chain Management and Supply Chain Management Review. He is a member of INFORMS, POMS, DSI, and the Academy of Management.

![](/api/attachments/QAV5JV7W/fulltext/images/06fb44d4caac24000c6823bdd424ef32983aa4569ddb8ee4b6941acbb64ee644.jpg)

Ton G. de Kok is full professor of operations planning and control at Technische Universiteit Eindhoven. He holds an MSc in mathematics from Rijksuniversiteit Leiden and a PhD in mathematics from Vrije Universiteit in Amsterdam. He has worked as OR consultant and logistics innovation manager within Philips Electronics. He is the director of the European Supply Chain

Forum at Technische Universiteit Eindhoven. His research interests lie in the area of production planning and control and supply chain management, particularly in high volume electronics and semiconductor industries. He has published in journals such as Management Science, IIE Transactions, Journal of the Operational Research Society, European Journal of Operational Research, OR Spektrum, Advances in Applied Probability, Journal of Applied Probability, Performance Evaluation, Probability in the. Engineering and Informational Sciences, International Journal of Production Research, Operations Research Letters and International Journal of Production Economics. He is a member of INFORMS, POMS, ORS and EUROMA.
