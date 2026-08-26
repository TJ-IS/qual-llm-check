---
otero_id: 19850
otero_key: "J6ERGG8F"
title: "Decisions for information or information for decisions? Optimizing information gathering in decision-intensive processes"
authors: "S. Voorberg; R. Eshuis; W. van Jaarsveld; G.J. van Houtum"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113632"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decisions for information or information for decisions? Optimizing information gathering in decision-intensive processes

S. Voorberg <sup>\*</sup>, R. Eshuis, W. van Jaarsveld, G.J. van Houtum

Department of Industrial Engineering and Innovation Sciences, Eindhoven University of Technology, the Netherlands

## A R T I C L E I N F O

Keywords: Decision intensive process Markov decision process Information acquisition Decision support

## A B S T R A C T

Decision-intensive business processes are performed by decision makers who gather different pieces of infor mation to reach the process objective: a final decision of high quality, for instance, the final price of a quote or the diagnosis of a failure of a hightech machine, as a result of an information-gathering process with minimum costs and efforts. Gathering all possible pieces of information results in high quality decisions, but also yields high costs and efforts. Therefore, decision makers require decision support to determine which information to gather to make the best final decision. This paper introduces an approach that supports a decision maker in the continuous trade-off between the effective acquisition of more information and cost-efficient decision making. The approach uses a well-defined modeling notation for decision-intensive processes, CMMN, and links it to a standard optimization technique, Markov Decision Processes. The approach calculates an optimal informationgathering solution, such that the expected result of the main decision minus the process cost for collecting in formation is optimized. The approach uses the solution to configure a run-time recommendation tool for the decision maker. The approach is flexible and allows that a decision maker ignores the advice; it then continues to offer recommendations in the subsequent states. We show the feasibility and effectiveness of our approach on a real-world quote process.

## 1. Introduction

## 1.1. Motivation

Nowadays many business processes rely on knowledge workers that gather data from different sources to make informed decisions. Exam ples are handling complex insurance claims, developing new medicines, or diagnosing failures of high-tech machines. Such business processes require substantial flexibility [1], as new information may lead to new insights, hence new decisions. Business processes that are dependant upon knowledge workers who perform interconnected decision-making tasks to drive critical organizational objectives are called Decision Intensive Processes (DIPs) [1,2].

The purpose of a DIP is to assist knowledge workers, i.e. decision makers, in making efficient and effective final decisions [1,2]. Effec tiveness refers to weighing the alternatives and making the ‘correct final decision, efficiency to using capital optimally for gathering infor mation. These two factors are dependent, requiring a trade-off to be made. A good decision should require a minimum investment of money and effort and an efficient decision should still have a high quality. Information is the linking pin between these two factors. Collecting in formation improves the knowledge position of a decision maker and increases the effectiveness of the final decision in a DIP. However, the gathering of information costs money and slows down the process, thus impedes efficiency. Hence, the goal of making an efficient final decision can be translated into the goal of effectively collecting information.

A simple example of a DIP is the process of diagnosing a failure of a hightech machine. To determine which part of the machine is failing, an engineer can collect information on software failures, do remote checks, do test runs, etc. Each piece of gathered information improves the knowledge position of the engineer and therefore decreases the uncer tainty of diagnosing a wrong cause of failure. However, the time that a machine is not running is costly to the organization. Hence, an engineer needs to balance, while diagnosing, the costs and gains of gathering additional information in determining the cause of failure.

## 1.2. Problem statement and related work

For many DIPs an abundance of data is available to support human decision making. A decision maker can find themselves entangled in a web of possible actions and decisions and feel the pressure to make costeffective decisions of good quality. In environments where the amount of information is overwhelming, this causes problems to oversee the situation [3]. Still, intelligence of human decision makers, i.e., tacit knowledge, is indispensable in many situations. Hence, there is a need to improve the support for data-driven human decision making [4,5].

Next to the work on DIPs [1,2,6], there is a stream of related work on knowledge-intensive processes [7–9], in which decision-making plays a less prominent role, or decision-aware processes [10–12], which do not focus on decision making by knowledge workers. Some of these works [8,13] stress the need for incurring data that appears during the process. However, the use of only data is not enough to optimize the actions that are taken in a DIP. The process model can raise additional constraints on actions that have to be incurred in the optimization. In the described streams of literature, this combination of information and process optimization has been recognized [6,11,14]. However, no paper has given a clear approach on how to combine the information and the process model into one optimization problem. The main modeling lan guage for decision making in business processes is the DMN notation [15], which declares decision rules organized in decision tables. How ever, decision rules specify patterns based on information without continuously optimizing the expected benefit of decisions or checking process constraints that affect those decision rules. Hence, there is the need for an approach where human decision makers can control a DIP while receiving recommendations for decisions that optimize for both the process model and the information model.

## 1.3. Aim and contributions

This paper defines an approach that guides decision makers in making decisions in DIPs in the most efficient and effective way. The approach optimizes the cost of acquiring additional information versus the benefit of a final decision with improved quality and thus more profit. There are two sequential phases: a design-time phase and a deployment phase (Fig. 1). In the design-time phase the decision maker is assisted in finding an optimal information-gathering solution from process models and probabilistic data. A user-defined DIP model (specified in CMMN [16]), consisting of information gathering tasks and decisions, is translated into a Markov Decision Process (MDP [17]) with constraints. An MDP is well suited since the discrete event structure of an MDP is comparable to that of a DIP. Furthermore, we introduce an information structure: a function that computes the reward for each final decision given the available information. To maximize the expected profit according to the information structure, for every state of the DIP the optimal action (gathering new information or taking a final decision) is computed by the MDP. In the deployment phase, the CMMN user model and a general process control plan fragment combine into a CMMN model that can be deployed with a CMMN engine; the deployed instance is linked with the MDP information-gathering solution in order to provide in every state a recommendation to the decision maker who controls the DIP.

As host notation we use CMMN [16], since it is an OMG standard that is well suited for expressing DIPs [18]. Especially for DIPs, CMMN allows the flexibility of manually chosen tasks, opposed to BPMN. Although some form of flexibility can be introduced in BPMN by using ad-hoc subprocesses, we will use CMMN which was specifically designed for pro cesses in which users can decide to perform or skip an enabled task (manual activation). We extend CMMN with flexible decision support in a way that goes beyond the current state of the art. Using an optimization method that takes into account both process and infor mation we surpass the sole declaration of decision rules in DMN. The flexibility occurs when the decision maker ignores the support and takes a different action. Other than DMN, the MDP has an optimal solution also for any new situation that appears, and the approach supports such ignoring actions. The approach of this paper applies to any process modeling language in which decision makers have to decide per case which information-gathering tasks to perform.

![](/api/attachments/J6ERGG8F/fulltext/images/c9389c45470b4ba898b2577b3c182649fd45e5dc662987205f48eff6e0c4bff0.jpg)  
Fig. 1. Overview of the approach; each number refers to a section.

This paper makes three main contributions, as we explain in Section 8. First, we define an approach that optimizes a given DIP. Second, the approach considers the data and process structure when optimizing a DIP. Third, we introduce a flexible recommendation tool that guides a human decision maker, while allowing recommendations to be ignored.

## 1.4. Organization

In Section 2, we introduce CMMN as host notation for DIPs and MDP as optimization method. Subsequently, we introduce a motivating example and its CMMN case in Section 3. In Section 4, we discuss important assumptions and constraints in our approach that allow to use it in a consistent way. Section 5 introduces the design time steps of the approach and Section 6 introduces the deployment phase of the approach. Section 7 shows the use of the approach on the motivating example. Finally, Section 8 and 9 discuss the related work and future directions, respectively.

## 2. Preliminaries

## 2.1. Case modeling management notation

The OMG standard Case Management Model and Notation (CMMN) [16] offers a representation for semi-structured business processes in which cases are handled in a flexible way. CMMN mainly focuses on defining, in a declarative way, the flow of a case in a case plan model. The structure of the accompanying case file is assumed to be modeled by a different language, for example using a UML class diagram or an ER model. A CMMN case plan model, consists of stages, in which composite work is performed, tasks, in which atomic pieces of work are performed, and milestones, which are intermediate or final business objectives. These constructs are related via business rules, called sentries. Changes in the case file cause sentries to be triggered and allow tasks or actions to get enabled and started. Manual activation stages/tasks can be per formed or skipped if they are enabled. CMMN can be used in combi nation with BPMN, for modeling structured routine business processes, and DMN, for modeling decisions embedded in processes. Table 1 shows the graphical notation for CMMN.

In the case of a DIP, the decision maker is constantly balancing be tween making progress by collecting more information or making a final decision based on the collected information. As we will show in this paper, CMMN is well suited to express this. Especially, CMMN allows stages and tasks to be manually started or skipped (triangle symbol). However, CMMN does not provide guidance to decision makers when to perform these actions. Therefore, we introduce MDPs to consider the future effect of decisions on both the case file and the case plan.

## 2.2. Markov decision process

The approach that we define relies on Markov Decision Processes (MDPs) as mathematical optimization model [17]. A Markov Decision Process is a technique that optimizes sequential decision making under uncertainty. MDPs optimize the expected reward over a series of future actions. Thus, MDPs can be used to foresee what the effects will be of taking actions now and in the future. Using backward induction (sometimes also called dynamic programming) as solution method for finite horizon problems [17, p. 92], one can compute the optimal action for every state the process can be in. We specifically discuss this method for our approach in Section 5.5. Every action taken by the agent, for instance a decision maker, brings the process in a new state and returns a certain reward. The subsequent state after taking an action is defined by the transition and more specifically by the transition probability. Hence, the next state is uncertain and depends on a probability distribution. At the end of Section 3, we give an example of an MDP based on the introduced example. Section 5.4 gives a detailed description of how we translate a CMMN plan into an MDP model.

## 3. Motivating example

This section introduces a real-world case scenario that describes the need for decision support in information gathering. We use this example case in Section 7 to show the feasibility of our approach and its benefits.

Koffer services is a company that performs maintenance on aircraft components. Airliners close service contracts with Koffer for a specific component over multiple years. The market of aircraft component maintenance is competitive and requires sharp offers from Koffer to bring in contracts. To know the profit margins that are available for a specific component, information gathering is crucial. Koffer engineers need support on which information is most important and still valuable enough to collect such that they win attractive contracts and avoid un attractive contracts.

The process of these service contracts works as follows. Koffer re ceives a Request for Quotation (RFQ) from a potential client, who may also send this RFQ to competitors of Koffer. The RFQ refers to an airplane component, for which the client requests a proposed contract that explains Koffer's terms for the service contract, in this scenario a specific repair price for the serviced component. After performing an internal DIP in which extra information can be gathered, Koffer sends the terms of their contract. Koffer either earns the contract or the client chooses the offer from a competitor. Koffer is looking for an approach to support the decision makers by informing them about the value of gathering more information and the value of current options for the conditions of the contract.

For this paper, we focus on the internal DIP. At the moment that the RFQ arrives, Koffer has no exact information concerning the properties of the component that should be quoted. Koffer can gather information on this component and the terms and conditions of this RFQ through the data attributes listed in Table 2. Note that Parts Manufacturer Approval (PMA) and Designated Engineering Representative (DER) are method that suppress the cost of a component by using cheaper alternatives. Over and above parts are excluded from the contract and can be charged separately.

![](/api/attachments/J6ERGG8F/fulltext/images/a1de5a1ff7f762ff19f731ec8a7d4cac7ebe6c9972b6bb3d0f58d679a8f53191.jpg)

Koffer aims to optimize the process of gathering information through these attributes and hence to increase their certainty about how much profit they can make on this component. This increased certainty im proves the effectiveness of their quote price. At the same time, Koffer loses efficiency because of valuable time that is lost while gathering information. Other, possibly more profitable, RFQs might not be handled as long as this RFQ is still the main focus. Hence, they need a DIP to optimally make the trade-off between time and information. Fig. 2 shows the CMMN plan for the internal DIP. This figure contains more tasks than the information-acquiring tasks of Table 2, since the entire DIP includes other tasks as well.

Fig. 3 shows the Markov Decision Process that is the translation of the Obtain Total Repair Cost substage from the CMMN plan in Fig. 2, according to the translation defined in Section 5.4. The state defines which tasks have been performed and what attribute informa tion has been collected, where ⊥ means the information is unknown. In Fig. 3 we only show the information. One takes an action by deciding which subsequent task to perform. Every action causes a change of process (case file) or information (case plan) status. Transition proba bilities determine the unknown outcome of information acquiring tasks. By putting cost (negative reward) on performing more tasks and returning a reward based on how good the final decision is, we can use the optimized policy to find the best action such that the expected profit is maximized.

## 4. Optimizable DIPs

In this paper we focus on DIPs with a specific structure that allows linking them to Markov Decision Processes (MDPs) for optimization. Hence, we call them optimizable DIPs. In Section 4.1, we set out what is the specific constraint for optimizable DIPs. In Section 4.2 we discuss how CMMN is used to model these optimizable DIPs.

## 4.1. Stable information

In a DIP information is gathered to reach the end goal in an optimal way. In this paper we use data attributes to model the information needs of a DIP. In the class of optimizable DIPs, we assume acquired infor mation to be accurate and stable, i.e., values acquired for data attributes are assumed to be correct and are not changed once acquired. The assumption that data attributes are stable allows us to use them to decrease uncertainty on the received reward. Attribute values are retrieved by performing tasks. If a DIP only has stable data attributes, tasks are monotonic: if a task writes an attribute it is performed at most once during execution.

Before executing the DIP, the value of a data attribute X can be

## Table 2

Information acquiring tasks and attributes.

<table><tr><td>Task</td><td>Data Attribute</td><td>Reference</td></tr><tr><td>Obtain net repair cost</td><td>Net repair cost</td><td>A</td></tr><tr><td>Obtain Expected number of repairs</td><td>Expected number of repairs per year</td><td>B</td></tr><tr><td>Check customer credibility</td><td>Customer credibility</td><td>C</td></tr><tr><td>Check market prices</td><td>Current mean market price</td><td>D</td></tr><tr><td>In-house capability check</td><td>In-house capability</td><td>E</td></tr><tr><td>Determine PMA/DER</td><td>PMA/DER possibilities</td><td>F</td></tr><tr><td>Determine over and above</td><td>Over and above options</td><td>G</td></tr><tr><td>Fix contract length</td><td>Contract period</td><td>H</td></tr><tr><td>Obtain transport cost</td><td>Transportation cost</td><td>I</td></tr></table>

estimated using a probability distribution, $P ( X = x ) \in [ 0 , 1 ] ,$ , where x is a value for X. The probability distribution could be derived for example by analyzing historical data or by interviewing domain experts. For each execution of a DIP with n data attributes, the set with data attributes is denoted by $D = \{ X _ { 1 } , . . . , X _ { n } \}$ . For each data attribute $X _ { i } \in D$ we assume a domain dom(X ) of possible values for X . The space of data attribute values is denoted by $\mathcal { D } = d o m ( X _ { 1 } ) \times \ldots \times$ dom(X ). Using a probability distribution for each data attribute allows us to know the set of possible values and also the relative appearance of every possible value. The probability distributions enable to estimate the different outcomes (variability) of a specific decision. Also, one can compare different future scenarios where more information becomes available, which would improve the certainty of decisions by decreasing the variability of possible outcomes. Hence, knowing these distributions enables to determine if data attributes can provide extra information for a final decision.

## 4.2. Plan constraints in CMMN

Although the main trade-off for an optimizable DIP lies in the data attribute value gathering (information perspective), we are considering this problem from the perspective of a business process. As such, many different constraints might prevent a decision maker from taking the most direct path in collecting certain attribute values. For example, there might be subtasks that must be performed first before one can continue with other tasks. These constraints are modeled in the CMMN process model, for instance required tasks, precedence constraints be tween tasks, and stages that contain tasks. Furthermore, we allow for tasks in the CMMN model that are part of the procedure but actually do not affect the decision making part of the DIP. Our approach, in particular the MDP, deals with all these additional constraints. This means that we do not only optimize from an information-perspective (case file), but also from a process-perspective (case plan).

While we allow for plan constraints, we also make some simplifying assumptions in this paper. These assumptions are necessary to filter out a tractable MDP model (cf. Section 5.4). First of all, our algorithm does not support milestones. Therefore, any milestones that are currently modeled in a CMMN model will be excluded, except for the milestone that models the achievement of the main goal of the whole case. In section 9 we discuss how this assumption can be relaxed. Furthermore, we assume that tasks are instantaneous, so upon invocation they return immediately an outcome (data attribute value). Non-instantaneous tasks lead to an explosion of the state space of an MDP.

## 5. Dynamic decision support for optimizable DIPs: design time

In this section, we define the design-time steps of our approach to optimize the process of information gathering in Decision Intensive Processes. The upper part of Fig. 1 shows a flowchart of this part of the approach, consisting of five steps. These steps translate the DIP into an optimizable MDP model and solve it. Section 6 explains how we use the solved MDP to configure a recommender that offers decision support during deployment.

## 5.1. Create CMMN model

The first step is modeling a DIP with CMMN notation. A CMMN process model is called a case plan model, which consists of a top-level stage that contains stages, tasks and milestones. CMMN calls these ele ments plan items, and distinguishes between the definition and the use of plan items. However, we assume that each definition is used only once in a case plan model, hence we equate plan item definitions and plan items. Note that this assumption follows directly from the stable infor mation assumption in Section 4.1, causing tasks to be monotone. We allow the use of all possible CMMN task types including human tasks, case tasks and process tasks. For example, in Fig. 2, tasks such as Define

![](/api/attachments/J6ERGG8F/fulltext/images/a999fc15a0b448da95ebc83472f5cfc4435b235ed5e57156b54d37ce8de3a47e.jpg)  
Fig. 2. CMMN plan for Koffer.

![](/api/attachments/J6ERGG8F/fulltext/images/82d17f9d2fed0363f1703f639ca9a8741f04df268120cc0a9cf2db1b3e3bb2ea.jpg)  
Fig. 3. Markov decision process.

Over and Aboves or Collect Customer Information are case tasks, while Estimate Current Market Prices is a human task. However, since only the output data of a task is needed to make de cisions, the specific CMMN task type can be ignored. CMMN is suited for dynamic data where stages or tasks can be visited multiple times to update data items. However, because of the stable information assumption (Section 4), the stages and tasks in our DIP are not reac tivated after their completion. Tasks for which the decorator (!) is used are required: these model elements need to be finished before the parent stage can be completed.

This paper focuses especially on tasks and stages that need to be activated manually by the user, i.e., decision maker. The approach helps the user to decide, while enacting the CMMN process model, whether and when to activate such a task or stage. Note that a manually activated task or stage can have an entry criterion, that needs to evaluate to true before the manual activation decision can be made. The approach allows that for some task or stage automatic activation is used. However, to keep the interpretation of the model clear, we have not implemented this in our example case. We only consider entry criteria having sentries with on statements. To keep the model representation interpretable, sentries having if statements are not considered. However, MDPs do allow for the use of conditions on the data through if statements.

Data in a CMMN case is stored in a case file, which contains case file items. Therefore, the case file will denote the set of data attributes that can be acquired. To simplify the presentation, we allow a task to be connected to at most one case file item. However, this constraint can be relaxed by taking the joint probability distribution of the case file items for that specific task. To see an example of a CMMN model that is ac cording to the optimizable DIP description, we refer to Fig. 2.

## 5.2. Retrieve MDP structure

To be able to continue our approach, we require that all tasks are assigned to one of four classes: three classes of tasks and a class of stages. Furthermore, we require the presence of a single milestone that termi nates the process. Fig. 4 is a meta model in UML notation that shows how these different classes are associated with each other and relate to the CMMN classes. The class diagram also contains the class of case file items with their known probability distribution.

![](/api/attachments/J6ERGG8F/fulltext/images/4bbf07ba994c17884b854496b60fcc0bbdc4971c49f9db4b6ee53e559f1053e9.jpg)  
Fig. 4. CMMN meta model [16,19] extended with support for DIPs (in gray).

## 5.2.1. Tasks

Consider the complete set of tasks T also introduced in Fig. 4. For every task t ∈ T we assign an associated cost $c _ { t s }$ representing the cost and effort op performing the task, and a boolean variable that keeps track of whether the task has been performed.

Each DIP works towards a final decision. We model this final decision with a decision making task. We assume a DIP has one such decision making task, that is not followed by other tasks. However, in Section 9, we come back to this assumption and give suggestions on how the approach could be extended with multiple (sub)decisions in one DIP.

Definition 5.1 (Decision making tasks/Milestones). A decision making task uses acquired information from the case file to choose a decision f from a set of decision alternatives F . The decision finishes the DIP by achieving its final milestone.

We define the decision making task d ∈ T. In accordance with the UML class diagram in Fig. 4, a decision making task d is associated with an information structure (Section 5.3) and a single milestone and in herits two attributes from the task class. In the CMMN models, we interpret decision (DMN) tasks to be decision making tasks. Moreover, a decision making task is always followed by a milestone. Normally an underlying DMN model would define the decision tree for a decision task, but in our approach we define an MDP that governs the decision through a look up table that is introduced in Section 6.

Definition 5.2 (Procedural tasks). A procedural task is a task that is performed to progress towards the final decision of the DIP. It has a direct effect by being either required(1) or preceding(2) or part of a stage(3) or information acquiring(4)

We define the set of procedural tasks $P \subset T .$ . In the example we see the task of Requesting Permission Market Authority preceeds task Estimate Current Market Price. Hence, the permission is a preceding task(2) in this example, which makes it a procedural task. We define procedural tasks that collect one of the attribute values of unknown attributes as information acquiring tasks, $I \subseteq P .$

Definition 5.3 (Information Acquiring tasks). An information acquiring task is a procedural task that updates one or more attributes in the case file when it finishes.

An example of an information acquiring task is the In-House Capa bility check in Fig. 2. Every information acquiring task has a known association with one case file item and these tasks also inherit the process-related class attributes for procedural tasks.

Besides decision making and procedural tasks, a DIP can have additional tasks. Although they may have a certain cost associated, they do not directly affect the decision in the process and thus are negligible for the MDP and the approach. Therefore, any additional tasks are dis carded. Discarding those tasks for the decision-making model does not mean those tasks are removed from the business process.

Definition 5.4 (Additional tasks). An additional task is a task that is in the CMMN model and is neither a decision making nor a procedural task.

## 5.2.2. Stages

Stages v ∈ V create the hierarchy inside a plan model. We use stages to group certain clusters of tasks. The stage is an identifier of a cluster of tasks. Similar to a task if a stage is in the preceding set of another stage or task, it prevents the task/stage inside the cluster from starting if it has not been opened yet. Due to their structure, for the MDP model we can interpret stages as a special class of procedural tasks.

## 5.2.3. Labeling tasks

Based on the UML class diagram and using the constraints for the optimizable DIP, we can recognize and retrieve all the above defined classes of tasks and stages automatically. The decision making task is attached to the only milestone in the plan. Furthermore, all tasks that do not fulfill any constraints to other tasks and are not associated with an attribute are discarded as additional tasks. The remaining tasks are procedural. Any of these procedural tasks that have an association with an attribute are classified as an information acquiring task. Similar to procedural and additional tasks, stages can be filtered naturally from the starting CMMN model and do not require additional verification by the plan builder. Note that the Koffer case according to Fig. 2 does not contain any additional tasks.

The introduced task types resemble activity types that have been proposed for making decisions in processes [14]: Decision making tasks resemble decision activities, information acquiring tasks resemble administrative activities and additional tasks resemble operational ac tivities. However, procedural tasks with procedural constraints (required, precedence) have no counterpart in [14].

## 5.3. Information structure

A DIP is performed to achieve a specific functional goal that relates to a decision to obtain the best outcome. This final decision is the crucial step that affects the outcome of the whole process. For example, in the Koffer case in Section $^ { 3 , }$ the decision on the quoted price is the final decision. While each DIP has a specific functional goal, i.e., an outcome, a final decision should be both efficient and effective, which are non functional goals. Since both non-functional goals are in conflict, this requires a trade-off between them. Note that the literature on DIPs or related Knowledge-Intensive Processes (Section 8) considers only func tional goals and not the trade-off between non-functional and functional goals to reach an optimal decision.

To optimize for decision efficiency, one could set constraints on, for example, the total effort spent on the process. However, these pre defined constraints could affect the search for optimality in a negative way. For example, if a constraint permits to only collect a single piece of information, one cannot react in a flexible way to the situation. Hence, it is preferable to be able to compare efficiency and effectiveness in a direct way. Therefore, we propose to define a cost factor for the time spent on different tasks. This way, we can also distinguish better be tween tasks that are cheap (simple task) versus expensive (difficult task). Together with a reward function based on the process outcome, it is then possible to make this direct comparison. We next introduce mathemat ical notation for specifying how to optimize the process. We require a function that connects the effect of acquired data on final decisions and the cost of collecting that data to a reward. More precisely, the input of this function includes a final decision $f$ from a set of alternatives ${ \mathcal { F } } ,$ which must be chosen to terminate the process, and all the data attribute values ${ \mathcal { D } } ,$ with a known value. We call this function the information structure. In earlier work [20], we already introduced a first definition for this information structure. We extend that definition here, such that it also optimizes over the decision variable that directly determines the outcome of the process.

Definition 5.5 (Information Structure). Given a set of data attributes $D = \{ X _ { 1 } , . . . , X _ { n } \}$ with possible values $\mathcal { D } = d o m ( X _ { 1 } ) \times \ldots \times d o m ( X _ { n } )$ and a set of final decision alternatives ${ \mathcal { F } } ,$ the information structure is a function $Y : \mathcal { D } \times \mathcal { F } {  } \mathbb { R } ,$ , which gives the reward given all information and the chosen alternative. We denote by $Y ( X _ { 1 } , . . . , X _ { n } , f ) \textit { a }$ function that gives the reward, where the data attributes are random variables.

The method CalcRevenue() in Fig. 4 is the actual information structure Y that, based on the attribute values and the set of decision alternatives, calculates the optimal decision for the decision making task. An information structure can be derived through a combination of data analysis and domain knowledge. If there is a set of historical cases of this process, where preferably all data attributes, the decision and the outcomes are known, one could use techniques such as regression to estimate the effect of parameters on the outcome, while taking into account the decision options, as we discuss in [20].

We give a small example to show what the information acquisition can do with the outcome of the process. Suppose we have two data at tributes, $X _ { 1 } , X _ { 2 } ,$ for which the values are unknown: $P ( X _ { 1 } = 0 ) = P ( X _ { 1 } =$ $3 ) = 0 . 5 , P ( X _ { 2 } = 1 ) = P ( X _ { 2 } = 4 ) = 0 . 5 .$ . The two decision alternatives that can be taken are 0 (decline) or 1 (accept): $\mathcal { F } = \{ 0 , 1 \}$ . The information structure is attribute 2 minus attribute 1 multiplied by the final decision: $Y ( X _ { 1 } , X _ { 2 } , f ) = ( X _ { 2 } - X _ { 1 } ) f .$ The acquisition cost is 0.5 per attribute: $c _ { 1 } , c _ { 2 } =$ 0.5. Suppose the decision maker first wants to explore the acquisition of attribute 2. $\mathrm { I f } X _ { 2 } = 4 ,$ , we know the optimal final decision, independent of the value of $X _ { 1 : f } = 1$ . Then, knowing that $P ( X _ { 1 } = 0 ) = P ( X _ { 1 } = 3 ) = 0 . 5 ,$ there is an expected profit ${ \bf f } { \bf E } [ Y ] = ( 0 . 5 \cdot ( 4 - 3 ) + 0 . 5 \cdot ( 4 - 0 ) ) \cdot 1 =$ 2.5. However, when $X _ { 2 } = 1$ , the optimal decision is: $f = 0 ;$ , because E[Y] $= ( 0 . 5 \cdot ( 1 - 3 ) + 0 . 5 \cdot ( 1 - 0 ) ) \cdot f = - 0 . 5 \cdot f .$ Hence, the optimal profit E [Y] = 0 for f = 0. Similarly, we can derive that without any information the optimal decision is $f = 1$ , with an expected profit of 0.5. To interpret the value of attribute $^ { 2 , }$ we compare the profits when knowing and not knowing the value of $X _ { 2 } .$ For attribute 2: we have $( 0 . 5 \cdot 2 . 5 + 0 . 5 \cdot 0 ) \textrm { -- }$ $0 . 5 = 0 . 7 5$ as profit increase, which exceeds the costs c . So, it does pay off to acquire the information for attribute 2 right now.

In conclusion, executing a DIP in the most efficient and effective way can be viewed as a problem of profit maximization. Collecting less in formation can decrease the cost of the process. However, the lack of information creates uncertainty about the outcome of the final decision. By collecting more information this uncertainty can be decreased. The information structure is the solution to consider both factors by making a trade-off between extra cost versus improved revenue.

## 5.4. Filter MDP model

Given the information structure and the assignment of tasks to the specific classes, one can now filter out an MDP model. In this paper, we focus on the approach and not on the specific mathematical details of filtering out an MDP.

For the CMMN model, the MDP state s of the DIP is a vector that contains for each variable its value. A variable is either a case file item (data attribute) or a status attribute of a task or stage (case plan item). During the execution of the DIP each stable data attribute $X _ { i } , 1 \le i \le$ n begins with an unknown value, expressed with symbol ⊥. The actual value $x _ { i }$ for $X _ { i }$ can be retrieved. Together the data attribute variable i has a state $s _ { i } \in$ dom (X ) ∪ {⊥}. A vector with data attribute values, both known and unknown, is interpreted as an information state, denoted with $\boldsymbol { s } = ( s _ { 1 } , . . . , s _ { n } )$ . Furthermore, the total space of possible states is denoted by ${ \mathcal { S } } = ( d o m ( X _ { 1 } ) \cup \{ \perp \} ) \times \ldots \times ( d o m ( X _ { n } ) \cup \{ \perp \} )$ ). For each procedural task o $\Gamma s \mathrm { t a g e } y \in P \cup V ,$ we use a binary status attribute $\sigma _ { y }$ that has value 1 if and only if the task or stage y has finished: $\boldsymbol { \sigma } = ( \sigma _ { a } , \sigma _ { b } ,$ $\ldots , \sigma _ { | P \cup V | } )$ . We call σ the plan state. The total state of the process is $\begin{array} { r } { \pmb { \mathscr { s } } = ( \sigma , } \end{array}$ s).

For the information acquiring tasks to have the performed variable set to true, we require the associated case file items to have a known value. Based on this, the decision maker can choose from two different sets of actions. First, the decision maker can choose to perform a pro cedural task and possibly acquire an uncertain attribute, i.e., $\mathbf { a } = \boldsymbol { p } \in P ,$ which changes the state because the task performed attribute is set to true. Notice that although we do not include the exact value of the ac quired attributes information in the plan state, this value does have a crucial effect on the outcome of the process as part of the information state s. Second, the decision maker can decide to make a final decision, a $= f \in { \mathcal { F } } .$ In that case we end up in a terminating state because the DIP is finished. Notice that the opening of stages and required or preceding tasks puts some extra constraints on the actions allowed.

Let preceding be the set of procedural tasks or stages that must have been performed before task or stage a is allowed. In Fig. 2 this is denoted by a dotted line that connects the two tasks. Finally, let required be the boolean variable that denotes if task b must be performed before the process can be finished. Then, for the decision maker to take action a, we require the following conditions to hold:

$$
\begin{array}{l l} \forall \mathbf {b} \in p r e c e d i n g _ {\mathbf {a}}: \sigma_ {\mathbf {b}} = 1 & (\text { Preceding   tasks   or   stages }) \\ \text { if } \mathbf {a} \in \mathcal {F}: \forall \mathbf {b} \in P \cup V, \text { if } r e q u i r e d _ {\mathbf {b}} = 1, \text { then } \sigma_ {\mathbf {b}} = 1 & (\text { Required   tasks   or   stages }) \end{array}
$$

As long as the decision maker takes information acquiring actions, we incur a cost for the specific task that is performed. The moment the decision maker decides to make a final decision, we retrieve an expected reward based on the currently known attribute values and the decision taken. Hence,

$$
R (s, \mathbf {a}) = \left\{ \begin{array}{l l} - c _ {\mathbf {a}} & \text { if } \mathbf {a} \in P \\ \mathbf {E} [ Y (s, \mathbf {a}) ] & \text { if } \mathbf {a} \in \mathcal {F} \end{array} \right.
$$

Note that we can take the expectation over Y as it has been defined also for the set of random variables D. For a state s where some infor mation is already revealed, the expected reward of taking final action a can be expressed as a conditional expectation as follows $\pmb { \mathrm { E } } [ Y ( s , \mathbf { a } ) ] = \pmb { \mathrm { E } } [ Y$ $( X _ { 1 } , . . . , X _ { n } , \mathbf { a } ) | \forall i : x _ { i } = s _ { i } \mathbf { i } \mathbf { f } s _ { i } \neq \bot ]$ . This takes into account the known attribute values, while using the distribution for the remaining attributes.

Transitions happen with a certain probability that can be derived from the probability distributions that we establish when classifying the information-gathering tasks. We define two transitions: state transitions (case plan) and information transitions (case file). The total transition of an action a in the DIP constitutes of the product of both transitions. Looking back at the defined classes of tasks, only in information acquiring tasks we have an information transition. In the other classes the information transition probability will always be 1.

For state transitions we have the following:

$$
P _ {\mathbf {a}} ^ {p} (\sigma , \sigma^ {\prime}) = \left\{ \begin{array}{l l} 1 & \text { if   } \mathbf {a} \in P \cup V \text {   and   } \sigma_ {\mathbf {a}} = 0 \text {   and   } \sigma_ {\mathbf {a}} ^ {\prime} = 1 \\ & \text { and   } \forall \mathbf {p} \in P \setminus \{\mathbf {a} \}: \sigma_ {\mathbf {p}} = \sigma_ {\mathbf {p}} ^ {\prime} \quad \text {(Procedural task)} \\ 1 & \text { if   } \mathbf {a} \in \mathcal {F} \text {   and   } \forall \mathbf {b} \in P \cup V: \sigma_ {\mathbf {b}} = \sigma_ {\mathbf {b}} ^ {\prime} \text {(Decision - making task)} \\ 0 & \text { otherwise } \end{array} \right.
$$

For information transitions we define the following, where ↔ means an information-acquiring task and case file item are associated:

$$
P _ {\mathbf {a}} ^ {c} (s, s ^ {'}) = \left\{ \begin{array}{l l} P (X _ {i} = x _ {i}) & \text { if   } \mathbf {a} \in I: \text { if   } i \leftrightarrow \mathbf {a}: s _ {i} = \bot \text {   and   } s _ {i} ^ {'} = x _ {i} \text {   and   for   } j \Leftrightarrow \mathbf {a}: s _ {j} = s _ {j} ^ {'} \\ 1 & \text { if   } \mathbf {a} \in \mathcal {F} \cup V \cup P \setminus I \text {   and   } 1 \leq i \leq n: s _ {i} = s _ {i} ^ {'} \\ 0 & \text { otherwise } \end{array} \right.
$$

Hence, the total transition probability is then:

$$
P _ {\mathbf {a}} (\mathbf {s}, \mathbf {s} ^ {\prime}) = P _ {\mathbf {a}} ^ {p} (\sigma , \sigma^ {\prime}) \cdot P _ {\mathbf {a}} ^ {c} (s, s ^ {\prime})
$$

By collecting extra information, it is possible to reduce the uncer tainty on the final decision outcome. Hence, there is a higher certainty that one actually will earn what is expected. However, to arrive at that point, efficiency is lost while acquiring additional information. The trade-off between collecting more information and maximizing the ex pected reward based on the final decision is the key parameter that this MDP tries to maximize by scaling those rewards to their probability of happening. One needs to know the probability distributions of the in dividual attributes because they allow to compare the change in profit between the attributes based on their probabilities.

## 5.5. Solve MDP

To solve a finite horizon MDP, we can use the technique of backward induction. However, this is only the case in scenarios where the state space still is tractable in computer memory. Backward induction starts from all the possible scenarios that the process could end up in and their reward. By thinking backwards what would have been the best action to maximize reward if still one variable would be uncertain, we set one step back in time. This becomes a recursive procedure all the way back until all attributes are uncertain. During this backward induction, every possible state is visited. This also means that for every possible state, we have determined what is the optimal action to take. To know in detail how backward induction works for a MDP based on an optimizable DIP, we refer to our earlier work [20], which builds on existing MDP solution techniques [17]. Note that the state space of an MDP grows exponen tially. This means that we can solve problems up to the size of the example case. Hence, scalability is an important future extension, which we discuss in the conclusion. An MDP always optimizes for the expected profit. However, by retrieving information one also decreases the un certainty of the outcome. Because in this paper we dot not put any conditions on the information structure, this function can become very complicated with many dependencies between attribute values. There fore, we cannot give any further indication on the variance reduction for different information-acquiring decisions.

## 6. Dynamic decision support for optimizable DIPs: deployment

The outcome of our approach for the design-time phase is a solved MDP that offers an advice for every possible state in which the DIP can be. We now define how to use these MDP advices during deployment.

The lower part of Fig. 1 shows how a decision maker controls a CMMN engine while interacting with the MDP recommender. For this purpose, we introduce a plan fragment to control the execution of the user defined CMMN process model. A plan fragment is a reusable part of a case plan model and often contains multiple plan items. Inserting the plan fragment into the CMMN user model results in an integrated CMMN model. The CMMN engine is configured with this integrated CMMN model to let the decision maker control the DIP and launch tasks. After every task completion, the result is incurred in the new state that is sent to the MDP recommender to obtain a new action set and recommen dation. Next, both the new state and the action set and recommendation are sent to the decision maker, who selects one of the actions.

![](/api/attachments/J6ERGG8F/fulltext/images/1a55479a3d82487f79fce2d366f601965f0fe3807b624eea6f0ae8f4f5ddd470.jpg)  
Fig. 5. Process control plan fragment for user CMMN model.

## 6.1. Process control plan fragment

Fig. 5 shows the process control plan fragment that fits the con straints of an optimizable DIP and its context, the CMMN user model. The figure shows the final decision point as defined by Decision-making task; in the example in Fig. 2 this would be task Decide on Price. Furthermore, when deciding to gather more information the corre sponding task from the CMMN user model is performed (cf. Fig. 2).

The actual need for a plan fragment and the extra tasks is because of the effectiveness versus efficiency trade-off. This trade-off only appears after the DIP has been modeled according to our approach. Hence, when performing the DIP the decision maker needs a recurring process phase where he actually makes the trade-off supported by the MDP recommender.

The plan fragment consists of a task Request MDP recommender which results in a recommendation and subsequently the task Information or Decision where the decision maker can consult the MDP recommendation and decide on the next step. The two milestones cap ture the decision maker's decision and control the next phase of the integrated plan. By integrating the plan fragment with the user model, an integrated CMMN model is obtained that configures a CMMN engine supporting the DIP.

## 6.2. Decision making support

The outcome of solving the MDP can be seen as a multi-dimensional matrix that functions as a look-up table for decision makers. During the Information or Decision task, the decision maker makes a deci sion, given the current state and MDP support, i.e., an optimal action and the corresponding expected profit for that action. Also other possible actions and their expected profit are shown to the decision maker. Section 7.3 will give an example of how the information could be shown to the decision maker.

The MDP support consists of three parts. Those parts are components of the recommendation handed to the decision maker in the Information or Decision task in Fig. 5. First, the decision maker is given a list of allowed actions according to the current state of the CMMN user model. Second, the MDP advises the optimal next action, either a pro cedural task, e.g., which task from the CMMN user model in Fig. 5, or a final decision. Note that for specific scenarios, we first might need to perform a ‘non-acquiring’ procedural task before we can actually perform the information acquiring task that gives us the required in formation. In that case the MDP will first advice the non-acquiring task. Third, the MDP shows the expected profit for all possible actions. This comparison was discussed in section 5.3. As long as additional infor mation still offers more value in expectation, the recommendation will be to continue information gathering.

## 6.3. Decision maker

As shown in Fig. 1, the decision maker is the responsible process controller, i.e., the outgoing arcs of the Information or Decision task are based on a decision from a decision maker who is assisted by the MDP recommender. The inserted plan fragment then allows the CMMN engine to control the process being enacted. When the task is completed, the CMMN engine calls the recommender for a new state-specific advice, even when the previous advice was not followed by the decision maker. This new advice is then shown to the decision maker. This loop con tinues until the decision maker takes a final decision, after which the CMMN engine will terminate the process. However, tacit knowledge of decision makers cannot be captured in a mathematical model. Our approach therefore allows a decision maker to ignore recommendations and acquire information that is not most profitable according to the MDP. Still, the MDP offers advice in any resulting state.

## 7. Evaluation/case study

Based on the example DIP case introduced in Section 3, we next show a proof of concept for our approach and validate its feasibility. Further more, the outcome of the MDP for the example case is compared to the current decision method within Koffer. On https://is.ieis.tue. nl/staff/heshuis/OptimizingInformationGathering/, a second case is made publicly available, where we focus on optimizing failure diagnosing and dispatching of maintenance engineers.

## 7.1. Validation case

The Koffer case that was introduced in Section 3 is based on a real world case, but the company is confidential. The validity of this model was discussed with actual decision makers for this specific kind of pro cesses at the company. Also the data set-up, though simplified to four

## Table 3

Procedural tasks for Koffer case.

<table><tr><td></td><td>Stages</td><td>Cost</td><td>Preceding</td><td>Required</td><td></td></tr><tr><td>1.</td><td>Koffer DIP</td><td>0</td><td>()</td><td>0</td><td></td></tr><tr><td> $\alpha$ .</td><td>Obtain total repair cost</td><td>20</td><td>()</td><td>0</td><td></td></tr><tr><td> $\beta$ .</td><td>Obtain expected amount of repairs</td><td>0</td><td>()</td><td>1</td><td></td></tr><tr><td></td><td>Procedural tasks</td><td>Cost</td><td>Preceding</td><td>Required</td><td></td></tr><tr><td>2.</td><td>Request permission market authority</td><td>20</td><td>()</td><td>0</td><td></td></tr><tr><td>3.</td><td>Collect contract information</td><td>10</td><td>()</td><td>1</td><td></td></tr><tr><td>4.</td><td>Collect customer information</td><td>30</td><td>()</td><td>1</td><td></td></tr><tr><td></td><td>Information acquiring tasks</td><td>Cost</td><td>Preceding</td><td>Required</td><td>Case File Item</td></tr><tr><td>5.</td><td>Obtain net repair cost</td><td>10</td><td>( $\alpha$ )</td><td>0</td><td>A</td></tr><tr><td>6.</td><td>Obtain yearly amount of repairs</td><td>8</td><td>( $\beta$ )</td><td>0</td><td>B</td></tr><tr><td>7.</td><td>Check customer credibility</td><td>2</td><td>()</td><td>1</td><td>C</td></tr><tr><td>8.</td><td>Estimate current market prices</td><td>100</td><td>(2)</td><td>0</td><td>D</td></tr><tr><td>9.</td><td>In-house capability check</td><td>3</td><td>()</td><td>1</td><td>E</td></tr><tr><td>10.</td><td>Determine PMA/DER</td><td>20</td><td>( $\alpha$ , 5)</td><td>0</td><td>F</td></tr><tr><td>11.</td><td>Determine over and above</td><td>15</td><td>( $\alpha$ , 5)</td><td>0</td><td>G</td></tr><tr><td>12.</td><td>Fix contract length</td><td>4</td><td>( $\beta$ )</td><td>0</td><td>H</td></tr><tr><td>13.</td><td>Obtain transport cost</td><td>12</td><td>(4)</td><td>0</td><td>I</td></tr></table>

possible values per attribute to maintain tractability, has been retrieved from this company. Finally, the decision tree that we will use as benchmark was developed in cooperation with the same decision makers.

## 7.2. Design-time approach

## 7.2.1. Create CMMN model

For the first stage of our approach, we require a CMMN model of the optimizable DIP according to the constraints defined in Section 5. For the example DIP we already introduced the CMMN model in Section $^ { 2 , }$ which does satisfy the required optimizable DIP set-up according to the constraints introduced in Section 4.

## 7.2.2. Retrieve MDP structure

The next step that is necessary to create an MDP is to assign all necessary tasks in the CMMN model to one of three subsets. How to assign tasks to these sets follows directly from the CMMN model in Fig. 2. Table 3 shows the stages and procedural tasks and their associ ations with other tasks including also the information acquiring tasks and the associated case file items. Table 4 defines the case file containing all case file items. There are no additional tasks.

To retrieve the MDP structure of the example DIP we need an in formation structure for the decision-making task. We define the following information structure, based on the case file items introduced in Table 4 and the Koffer case,

$$
\begin{array}{l} Y (s, f) = E \cdot \overbrace {B \cdot H} ^ {\text { Expected   number   of   repairs }} \cdot \overbrace {P (\mathcal {D} \geq f)} ^ {\text { Quote   accepted }} \\ \left[ \overbrace {f - A (1 - 0 . 2 G) - F - I} ^ {\text { Expected   Revenue }} \right] \quad \forall f \in \mathbb {R} \\ Y (s, \text { No   bid }) = 0 \end{array}
$$

The random variable $\mathcal { D }$ is modeled by a normally distributed random variable with $\mu = D$ and $\sigma = 2 0 0$ . Furthermore, we have decision alternatives, = {No bid,1800,2000,2200}.

Filter MDP model. The next step in our approach is to build up the MDP model from the information structure and the tasks assigned to different classes. Following the approach in Section $5 . 4 ,$ we filter the following plan state which is a tuple of tasks 2 to 13 and stages α and $\beta .$ In this state, the σ parameter is the ‘completed’ attribute for tasks and stages: $\boldsymbol { \sigma } = [ \sigma _ { 2 } , \sigma _ { 3 } , \sigma _ { 4 } , \sigma _ { 5 } , \sigma _ { 6 } , \sigma _ { 7 } , \sigma _ { 8 } , \sigma _ { 9 } , \sigma _ { 1 0 } , \sigma _ { 1 1 } , \sigma _ { 1 2 } , \sigma _ { 1 3 } , \sigma _ { \alpha } , \sigma _ { \beta } ]$ . Note that besides this case plan state, there is also an information state that con tains the acquired values of the case file items, where x is the data attribute value: $\textbf { \textit { s } } = \ [ x _ { A } , x _ { B } , x _ { C } , x _ { D } , x _ { E } , x _ { F } , x _ { G } , x _ { H } , x _ { I } ]$ . The action space consists of two sets. Either we collect more information by performing one of the twelve procedural tasks or we open a stage, or we take a final decision:

$$
\mathscr {A} = \{2, 3, 4, 5, 6, 7, 8, 9, 1 0, 1 1, 1 2, 1 3, \alpha , \beta \} \cup \{\text { No   bid }, 1 8 0 0, 2 0 0 0, 2 2 0 0 \}
$$

Table 3 lists precedence and required constraints for the information

gathering actions to become enabled in a specific state.

Next, the reward for a given state and action is either the extra cost for gathering information, given in the tables, or the expected profit based on the information that is available in the current state s and final decision $f \in { \mathcal { F } } ;$

$$
R (s, \mathbf {a}) = \left\{ \begin{array}{l l} - c _ {\mathbf {a}} & \text { if } \mathbf {a} \in P \cup V \\ \mathbf {E} [ Y (s, f) ] & \text { if } \mathbf {a} = f \end{array} \right.
$$

Finally, the transitions can be derived exactly the way they were introduced in section 5.4 using the probability distributions in Table 4. As described in Section $5 . 5 ,$ the filtered MDP can be solved using backward induction techniques. We used Python to program an algo rithm that optimizes MDPs that are built from tables such as Tables 3 and 4.

## 7.3. Deployment

After all the design-time steps have been taken as explained above, the process to be enacted can be deployed. Having the MDP solution, the decision plan fragment is combined with the user CMMN plan and enacted by the CMMN engine to support the decision maker in per forming the DIP. Fig. 6(a) shows the current state of the case, where green filled tasks have been performed and green lined tasks are enabled. Because of constraints for this specific state, the final decision is not yet allowed and the decision maker can choose between six different tasks to continue the DIP. In expectation the optimal choice would be to perform In-house capability check. However, the five other tasks are also enabled in the current situation and their expected profit is also given. In this specific state most of the important information is already collected and therefore the differences in profit between the different options are marginal.

The recommender shows the allowed options and the expected profit for each decision in the Possible Tasks table in Fig. 6(c). Moreover, because the MDP calculates the optimal future profit, the decision maker can es timate the effects of current decisions. Using the decision plan fragment that is inserted in the user plan, shown in Fig. 6 with the brown color, the CMMN engine can enact on the decisions that are taken. In accordance with Fig. 1, the CMMN engine returns the new state of the process and calls for the MDP recommender in the new state. A demonstrator for this specific case can be accessed via https://is.ieis.tue. nl/staff/heshuis/OptimizingInformationGathering/.

## 7.4. Numerical analysis

We compare the outcome of the approach with a decision tree that is based on the current decision process and is created in cooperation with sales managers in the company that inspired the example. The decision tree is shown in Fig. 8 in appendix A. In Table 5 we introduce some statistics based on the case model that was introduced in Section $3 . { \mathrm { F i g . ~ } } 7$ (a) shows the distribution of final decisions over all possible outcomes of the case file items. $\mathrm { F i g . 7 ( b ) }$ shows the proportion of cases in which a task is executed. Note that we removed the required tasks $( 3 , 4 , 7 , 9 , \beta )$ as they are always executed to finish the process.

Table 4  
Case file items for Koffer case.

<table><tr><td></td><td>Case File items</td><td>Distribution values</td><td>Distribution</td></tr><tr><td>A.</td><td>Net repair cost</td><td>{1500,1700,1900,2100}</td><td>Uniform</td></tr><tr><td>B.</td><td>Expected number of repairs per year</td><td>{40,60,80,100}</td><td>Binomial(0.2)</td></tr><tr><td>C.</td><td>Customer creditworthiness</td><td>{0,1}</td><td>Bernoulli(0.3)</td></tr><tr><td>D.</td><td>Current mean market price</td><td>{1700,1900,2100,2300}</td><td> $\left[\frac{1}{8},\frac{3}{8},\frac{3}{8},\frac{1}{8}\right]$ </td></tr><tr><td>E.</td><td>In-house capability</td><td>{0,1}</td><td>Bernoulli(0.6)</td></tr><tr><td>F.</td><td>PMA/DER possibilities</td><td>{100,200}</td><td>Bernoulli(0.3)</td></tr><tr><td>G.</td><td>Over and above options</td><td>{0,1}</td><td>Bernoulli(0.5)</td></tr><tr><td>H.</td><td>Contract period</td><td>{1,2,3,4}</td><td> $\left[\frac{1}{6},\frac{2}{6},\frac{2}{6},\frac{1}{6}\right]$ </td></tr><tr><td>I.</td><td>Transportation cost</td><td>{50,100,150,200}</td><td>Uniform</td></tr></table>

![](/api/attachments/J6ERGG8F/fulltext/images/3640b891fa3e591c5b65aca1296d0379cd1931e07d5e5579345db7337cd3310b.jpg)

(a) Current state; tasks filled green and brown have been performed; tasks with green and brown lining are enabled

<table><tr><td>Task</td><td>Variable</td><td>Value</td></tr><tr><td>Obtain Net Repair Cost</td><td>Net expected repair cost</td><td>1500</td></tr><tr><td>Obtain expected amount of repairs per year</td><td>Expected repairs per year</td><td>100</td></tr><tr><td>Check customer credibility</td><td>Customer creditworthiness</td><td>-</td></tr><tr><td>Estimate Current Market prices</td><td>Current mean market price</td><td>-</td></tr><tr><td>In-House Capability Check</td><td>In-house capability</td><td>-</td></tr><tr><td>Determine use of PMA/DER parts</td><td>PMA/DER possibilities</td><td>-</td></tr><tr><td>Determine Over and Aboves</td><td>Over and above options</td><td>0</td></tr><tr><td>Fix Contract Length</td><td>Contract period</td><td>3</td></tr><tr><td>Obtain transport cost</td><td>Transportation cost</td><td>-</td></tr></table>

(b) Case File

![](/api/attachments/J6ERGG8F/fulltext/images/88e7026db937fd477c8e1d48080b17cebd69d7677328ba082d6a00fdf21e436d.jpg)  
Fig. 6. Recommender view.  
(c) Recommendations

Table 5  
Comparison MDP vs Decision Tree.

<table><tr><td>Information</td><td>MDP</td><td>Decision tree</td></tr><tr><td>Expected profit</td><td>15,867.6</td><td>8226.0</td></tr><tr><td>Number of final states</td><td>136</td><td>1254</td></tr><tr><td>Average retrieval cost</td><td>143.5</td><td>100.06</td></tr><tr><td>Expected revenue</td><td>16,011.0</td><td>8125.94</td></tr></table>

The main comparison can be made based on the expected profit of both methods. The MDP is able to double the expected profit compared to this human decision tree. If we look at the final decision distribution in Fig. 7(a), clearly too many process instances are discarded in this decision tree. Also the distribution over the information sources that are acquired is, apart from the structurally enforced part, rather different. Furthermore, the decision tree also has a larger number of final states, meaning states where no more information is acquired. Together with the average retrieval cost, this implies that the decision tree is not complex enough to capture the dependencies between different attri butes as defined in the information structure.

In Table 6, we show the results for nine randomly selected instances of the Koffer case process. Hence, we can show how both algorithm work for those instances. There are five instances where both algorithms conclude it is not profitable to bid for the maintenance contract. Therefore, they make a loss on the pieces of information that are always required to acquire. However, looking at instance 8, the human-built decision tree actually makes a better final decision than the MDP or makes that decision with less acquired information. This instance is a good example why the introduced approach does not only use the MDP algorithm but always requires the final opinion of the decision maker, where they can use tacit knowledge to judge the instance. However, including the instances 2 and 4, where the MDP is clearly outperforming the decision tree, we can see that on average for those 9 instances the MDP does improve upon the decision tree.

The level of complexity is high for a human decision maker using the decision tree. However, the number of nodes in this tree (14) is marginal compared to the number of states of the MDP, which depends mainly on the state space. The size of the state space can be estimated by taking the product of the number of all possible values for all tasks. Hence, for the example we have five information-acquiring tasks with five possible values, four information-acquiring tasks with three possible values and five procedural tasks/ stages that can either be performed or not, i.e., 5<sup>5</sup> $3 ^ { 4 } \cdot 2 ^ { 5 } = 8 , 1 0 0 , 0 0 0$ states. Note that the procedural constraints can cause a part of those states not to be explored during optimization. The introduction of new tasks will cause the state space to increase exponentially, making it computationally hard to find an optimal solu tion. For the example, optimizing the MDP took 49 min on a Intel i5- 8365u CPU. In case of further scaling of the problem, one quickly runs into both memory and computation power problems. We plan to addres this issue in future work (Section 9).

![](/api/attachments/J6ERGG8F/fulltext/images/448523a1ac909057f3f6494de2023e6130c3ed56d96df2b3223ade228d200692.jpg)  
(a) Decisions

![](/api/attachments/J6ERGG8F/fulltext/images/cc97c4c7905fe9e1b5d9e25aef556e9480c054b1dbc8d8e7e27e36d3af79799a.jpg)  
(b) Tasks  
Fig. 7. Distributions.

Table 6  
Comparison of 9 instances.

<table><tr><td>Instance</td><td>Final Information State [A,...,I]</td><td>Profit MDP</td><td>Profit Decision tree</td></tr><tr><td>1.</td><td>[2100, 40, 1, 1900, 1, 100, 0, 1, 150]</td><td>1656</td><td>-122</td></tr><tr><td>2.</td><td>[1500, 100, 1, 2100, 0, 100, 1, 4, 100]</td><td>69,794</td><td>65,469</td></tr><tr><td>3.</td><td>[2100, 80, 1, 2100, 1, 200, 0, 1, 50]</td><td>-45</td><td>-45</td></tr><tr><td>4.</td><td>[2100, 40, 0, 2300, 0, 200, 0, 3, 150]</td><td>16,385</td><td>14,692</td></tr><tr><td>5.</td><td>[1900, 100, 0, 2300, 0, 200, 0, 4, 200]</td><td>-45</td><td>-45</td></tr><tr><td>6.</td><td>[1900, 40, 0, 2300, 0, 200, 0, 3, 150]</td><td>-45</td><td>-45</td></tr><tr><td>7.</td><td>[1500, 40, 1, 1900, 1, 100, 0, 1, 150]</td><td>-45</td><td>-45</td></tr><tr><td>8.</td><td>[1700, 80, 1, 1700, 1, 100, 0, 2, 200]</td><td>27,416</td><td>27,419</td></tr><tr><td>9.</td><td>[1900, 60, 0, 1900, 0, 100, 1, 1, 150]</td><td>-45</td><td>-45</td></tr></table>

For this specific example the statistics have proven the value of using our approach during deployment with a doubling of the expected profit. Together with the steps that have been followed during the design time approach in Section 7.2, the approach has been shown to be feasible and applicable in real-life process cases. Furthermore, by using a real-world case and by validating the approach with decision makers, we show that this approach is improving upon the current approach that is based on decision trees. Given the necessary constraints, we consider this approach valuable for many more DIPs in different areas of expertise, such as financial services or governmental tender procedures.

## 8. Related work

Process modeling languages like BPMN and UML Activity Diagrams offer basic support for modeling decision points. To enable reuse of such decision logic, the modeling language DMN was developed to declare recurring decision points in DMN decision tables that can be referenced in tasks of business processes [15]. DMN focuses on what information is needed to make decisions. The last few years, however, several authors have recognized that decisions often are an integrated part of the busi ness process that actually even controls the flow [10,12,14]. But there is no guidance for decision makers about which information to gather in order to perform DIPs both efficiently and effectively.

Hasic et al. [14] introduce five necessary principles to connect a process model and a decision model: The first principle states that the decision logic should be externalized as a service to the process. In this paper, we use a separate MDP tool that implements the decision logic, which could be realized as a service. A second principle is the need to model all data objects. Here, we use case file items, modeled as data attributes. The third principle of always modeling all possible decision outputs is followed in our approach. The fourth principle asks for ordering decision activities. By using a declarative language such as CMMN we allow the flexibility of deciding on the activity order and at the same time include any process constraints that define an order. The final principle involves making subdecisions. This specific extension to our current approach is discussed in Section 9.

DIPs have been modeled using declarative process modeling. Vaculin et al. [1] propose to model DIPs with declarative business artifacts. They develop design pattern support for the execution of DIPs. Guidance is modeled in the form of expert-defined constraints. Mertens et al. [12] develop DeciClare, a declarative process modeling language targeted for DIPs. The process perspective in DeciClare is modeled with Declare, the decision perspective with DMN. No guidance support is provided. The approach defined in this paper can be used in combination with Deci Clare, replacing DMN-related parts with the decision fragments defined in Section 5 and 6.

In general, the approach can be used in combination with other declarative process modeling languages, notably DCR graphs [21,22] and Declare [23]. For instance, in the context of Declare, recommen dation support has been developed, based on past process executions and their costs [24]. The approach in this paper is much more advanced, since it considers optimized decision making based on actual output data of tasks.

Next, there are approaches to guide the execution of informationintensive business processes, which produce information products [25,26]. The structure of the information products is specified in prod uct data models, which are tree structures that declaratively define how a data item is assembled from other data items. Different strategies exist to optimize the assembly of the informational products. Our approach focuses on optimizing decision making within the execution of DIPs. Therefore, we use information structures, which focus on the value of data items for decision making rather than their structure.

In earlier work [6,20] we discussed the value of using MDPs to support the execution of DIPs that are modeled in an artifact-centric process language. There we presented a detailed translation of Guard-Stage-Milestone process models into MDPs [20]. The present approach builds upon this translation by defining an approach that shows how DIPs expressed in CMMN can be configured such that decision makers are guided during execution of a process to optimize decision making.

AI planning has been used to support the execution of knowledge intensive processes [13,27,28]. A plan is a sequence of tasks such that a goal state is reached. Performing a task results in a new state. Tasks can be modeled at different levels of granularity. If the user deviates from the plan and ends up in a state that is not in the plan, a new plan is generated. While these approaches support the flexible ad-hoc execution of processes, they do not support decision making, especially making the trade-off between gathering more information and making final decisions.

For expert systems, several optimization approaches for information acquisition strategies have been proposed [29], for instance using dy namic programming [30]. However, none of these consider the relation with process models, such as CMMN and DIPs consisting of information acquiring tasks, procedural tasks, additional tasks, and decision-making tasks. Finally, we use the notion of an information structure which links the benefits and costs of gathering data for final decisions.

In sum, the main contribution of this paper is a flexible approach, based on optimization, for guiding decision makers in performing DIPs both efficiently and effectively.

## 9. Discussion

An important assumption for the CMMN user model is the use of one milestone, which concludes the process. However, milestones are part of the CMMN language as an opportunity of setting subgoals during the process. Related, CMMN allows to create hierarchy in a DIP. By using substages one can define different layers of tasks and decisions to meet subgoals. This structuring can actually be of great value to larger DIPs. By introducing more milestones and stages, one could create a hierarchy of smaller size decisions. This decreases the state space of the DIPs dramatically. For example, if we cut a 10 attribute process all with a domain of four values into two smaller size processes, we can go from as much as 1,048,576 states to 2048 states. The main reason why we did not include this in our approach is that one needs more information structures and a higher level decision making that oversees which sub goals have the highest priority. This requires a ‘two-level’ approach that would obfuscate the key ideas and principles underlying our solution.

The existence of an MDP solution relies on the availability of prob abilities and the assumption that those probabilities represent reality. Although frequencies of historical cases can give a good estimate, we know that in real-life things are always different. This is why we intro duce the MDP as an advisor to the decision maker. Tacit knowledge can recognize specific historical cases and see dependencies between those and the current process. Still, we show in Section 7.4 that in expectation the MDP has a higher profit. This does not rule out that for specific cases the decision maker can use additional information to create an even higher outcome by diverging from the ‘average’ advice. However, as back bone for the complete set of cases, this MDP model is shown to make a real difference.

An alternative approach to MDPs are attribution models. Using Shapley values or the removal effect in the Markov model, one could try to find the marginal contribution of each individual attribute. However, the dynamic adaptation to newly available information cannot be used in these techniques. This is a crucial part of our solution, as it allows us to make better final decisions at the right moment.

## 10. Conclusion

This paper introduced a new approach for decision support for in formation gathering in Decision Intensive Processes. The approach translates a CMMN process model into an MDP. Using the optimal so lution for the MDP model, a decision maker is given advised what in formation to gather in order to make a final decision that is both efficient and effective. The approach introduces a new CMMN plan fragment to let a decision maker use MDP advice to control the process execution. Using the approach, decision makers performing DIPs are supported in deciding what information to gather to optimize the final decisions. Although these information-gathering decisions could be automated, we value the opinion of the decision maker and view its role as essential to decide which information to gather for a specific case.

An exemplary case based on a real-world industrial scenario shows the feasibility of the approach. For this real-world scenario, we compared a basic implementation of the approach using an MDP opti mizer with a decision tree that was constructed by a decision maker from industry. We showed that the algorithm can double the expected profit compared to the decision tree. We also showed that there are still in stances where the decision maker can make better decisions, e.g., based on information that is not available to the model, which suggests that a human decision maker should be in the lead.

A main topic for further research is improving the scalability of the approach for problems where the state space explodes. We plan to use techniques such as deep reinforcement learning or segmenting the problem into smaller problems by using intermediate goals that are represented in the CMMN model as milestones. Deep reinforcement learning uses neural networks to learn the policy on a subset of the complete state space.

Further research can also be done in the direction of how to inform the decision maker. By putting constraints on the information structure, one might be able to give additional information about marginal con tributions or variance reduction per attribute.

## Credit author statement

1. Simon Voorberg: Conceptualization, Methodology, Software, Formal analysis, Writing - Original Draft

2. Rik Eshuis: Conceptualization, Methodology, Writing - Original Draft

3. Willem van Jaarsveld: Conceptualization, Writing - Review & Editing

4. Geert-Jan van Houtum: Supervision, Writing - Review & Editing

## Acknowledgements

This work was supported by the “Netherlands Organisation for Sci entific Research” (NWO). Project: Real-time data-driven maintenance logistics. Number: 628.009.012.

Appendix A. Decision tree

![](/api/attachments/J6ERGG8F/fulltext/images/0181942c225bb4e07ea6fdd4ce7a47228484fd229fe536516acbe08a06b19661.jpg)  
Fig. 8. Decision tree.

## References

[1] R. Vaculn, R. Hull, T. Heath, C. Cochran, A. Nigam, P. Sukaviriya, Declarative business artifact centric modeling of decision and knowledge intensive business processes, in: Proc. EDOC 2011, 2011, pp. 151–160.

[2] D. Bromberg, Bpm for knowledge workers: the structural foundations of decision intensive processes (dips), BPTrends, January 2007.

[3] P. Bossaerts, C. Murawski, Computational complexity and human decision-making, Trends Cogn. Sci. 21 (12) (2017) 917–929.

[4] J.-C. Pomerol, Artificial intelligence and human decision making, Eur. J. Oper. Res. 99 (1) (1997) 3–25.

[5] F.E. Horita, J.P. de Albuquerque, V. Marchezini, E.M. Mendiondo, Bridging the gap between decision-making and emerging big data sources: an application of a model-based framework to disaster management in Brazil, Decis. Support. Syst. 97 (2017) 12–22.

[6] R. Eshuis, Modeling decision-intensive processes with declarative business artifacts, in: Proc. ASSRI 2018. 2018. pp. 3–12

[7] C.D. Ciccio, A. Marrella, A. Russo, Knowledge-intensive processes: characteristics, requirements and analysis of contemporary approaches, J. Data Semantics 4 (1) (2015) 29–57.

[8] S.K. Venero, J.C. dos Reis, L. Montecchi, C.M.F. Rubira, Towards a metamodel for supporting decisions in knowledge-intensive processes, in: Proc. SAC 2019, 2019, pp. 75–84.

[9] R. Eshuis, M. Firat, Modeling uncertainty in declarative artifact-centric process models, in: Proc. BPM 2018 Workshops, 2018, pp. 281–293.

[10] A. Yousfi, A.K. Dey, R. Saidi, J. Hong, Introducing decision-aware business

[11] A. Yousfi, K. Batoulis, M. Weske, Achieving business process improvement via ubiquitous decision-aware business processes, ACM Trans Internet Technol 19 (1)

[12] S. Mertens, F. Gailly, G. Poels, Towards a decision-aware declarative process modeling language for knowledge-intensive processes, Expert Syst. Appl. 87 (2017) 316–334.

[13] S.K. Venero, B.R. Schmerl, L. Montecchi, J.C. dos Reis, C.M.F. Rubira, Automated planning for supporting knowledge-intensive processes, in: Proc. BPMDS 2020, Springer, 2020, pp. 101–116.

[14] F. Hasic, J.D. Smedt, J. Vanthienen, Augmenting processes with decision intelligence: principles for integrated modelling. Decis, Support, Syst, 107 (2018) 1–12.

[15] Object Management Group, Decision model and notation. version 1.3, 2020

[16] Obiect Management Group, Case management model and notation, version 1.1

[17] M.L. Puterman, Markov Decision Processes: Discrete Stochastic Dynamic Programming. Wiley Series in Probability and Statistics. Wiley. 1994.

[18] M.A. Marin, M. Hauder, F. Matthes, Case management: an evaluation of existing approaches for knowledge-intensive processes, in: Proc. BPM 2015 Workshops, 2015, pp. 5–16.

[19] A. Grudzińska-Kuna, Supporting knowledge workers: case management model and

[20] S. Voorberg, R. Eshuis, W. van Jaarsveld, G. van Houtum, Decision support fo declarative artifact-centric process models, in: Proc. BPM Forum 2019, 2019. pp. 36–52.

[21] T.T. Hildebrandt. R.R. Mukkamala. T. Slaats. Designing a cross-organizational case management system using dynamic condition response graphs, in: Proc. EDOC 2011, 2011, pp. 161–170

[22] S. Debois, T.T. Hildebrandt, T. Slaats, Hierarchical declarative modelling with refinement and sub-processes, in: Proc. BPM 2014, 2014, pp. 18–33.

[23] M. Pesic, H. Schonenberg, W.M.P. van der Aalst, DECLARE: full support for loosely structured processes, in: Proc. EDOC 2007, 2007, pp. 287–300.

[24] H. Schonenberg, B. Weber, B.F. van Dongen, W.M.P. van der Aalst, Supporting flexible processes through recommendations based on history, in: Proc. BPM 2008, 2008, pp. 51–66.

[25] I.T.P. Vanderfeesten, H.A. Reijers, W.M.P. van der Aalst, Product-based workflow support, Inf. Syst. 36 (2) (2011) 517–535.

[26] H. van der Aa, H. Leopold, K. Batoulis, M. Weske, H.A. Reijers, Integrated process and decision modeling for data-driven processes, in: Proc. BPM 2015 Workshops, 2015, pp. 405–417

[27] A. Marrella, M. Mecella, S. Sardina, ˜ Intelligent process adaptation in the smartpm

[28] I. Sid, M. Reichert, A.R. Ghomari, Enabling flexible task compositions, orders and granularities for knowledge-intensive business processes, Enterp. Inf. Syst. 13 (3) (2019) 376–423.

[29] V.S. Mookerjee, M.V. Mannino, Sequential decision models for expert system optimization, IEEE Trans. Knowl. Data Eng. 9 (5) (1997) 675–687.

[30] B.L. Dos Santos, V.S. Mookerjee, Minimizing information acquisition costs, Decis.

## S. Voorberg et al.

S. Voorberg is a PhD student at the department of Industrial Engineering and Innovation Sciences since November 2017. He received his BSc degree in Industrial Engineering and his MSc degree in Industrial and Applied Mathematics, both from Eindhoven University of Technology. Currently, he conducts research in a combined project between the fields of Business Process Management and Maintenance Logistics under the supervision of Geert-Jan van Houtum. Willem van Jaarsveld and Rik Eshuis. The proiect focuses on real-time decision support for semi-structured data-driven processes.

R. Eshuis works as an Associate Professor of Information Systems at Eindhoven University of Technology, The Netherlands. He has been a visiting researcher at IBM Thomas J. Watson Research Centre in New York and at CRP Henri Tudor in Luxembourg. He was the General Chair of the 7<sup>th</sup> IEEE European Conference on Web Services (ECOWS 2009) and the Programme Co-Chair of IEEE EDOC 2020. His main research interests is in data-driven business process management for knowledge and decision-intensive processes. He is and has been involved in several national and EU research projects together with industry that focus on developing advanced, flexible business process support. He is a senior member of the IEEE and member of the ACM.

W. van Jaarsveld is Associate Professor at Eindhoven University of Technology (TU/e), in the OPAC group. His main research interest is stochastic optimization, with applications in diverse areas including inventory control, supply chain management and maintenance logistics. He is also interested in spare parts demand forecasting in particular, and the use of data for decision making in general. Apart from working towards scientific impact, he aims to make an impact in practice by working closely with several companies to facilitate the implementation of the methods he develops in practice. His research on optimization of spare parts inventories has been applied at various companies, including Fokker Ser vices and Shell Global solutions

G.J. van Houtum is Full Professor and chair of Maintenance and Reliability at Eindhoven University of Technology (TU/e) since 2008. Since September 2017, he is also vice-dean IE of the Department IE&IS. His areas of expertise include maintenance optimization, spare parts inventory control, inventory theory in general, and operations research. Geert-Jan carries out research on the maintenance and reliability of capital goods. In particular, his focus is on design and control of spare parts networks, predictive maintenance con cepts, and product design choices that have a strong effect on system availability and TCO. In this research, also the value of remote monitoring data and other degradation data is investigated. Much of this research is carried out in cooperation with the industry, working with companies such as ASML, Dutch Railways, Philips, Oc´e, Marel, the Royal Dutch Airforce and Navy, and Vanderlande.
