---
otero_id: 21411
otero_key: "8B3RCHQR"
title: "An intelligent agent community approach to knowledge sharing"
authors: "Greg Elofson; Peggy M. Beranek; Philomina Thomas"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00077-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An intelligent agent community approach to knowledge sharing

Greg Elofson $^{a,*}$ , Peggy M. Beranek $^{b}$ , Philomina Thomas $^{c}$

$^{a}$ Decision and Information Analysis, Emory University, 302 Rich Bldg., Atlanta, GA 30322, USA $^{b}$ Computer Information Systems dept., Georgia State University, Atlanta, GA 30303, USA $^{c}$ UCA and L, 325 Delaware Avenue, Buffalo, NY 14201, USA

## Abstract

This paper illustrates a community of intelligent agents and how they facilitate knowledge sharing in the process of environmental scanning. The main components of the distributive feature of the agent community are a manager that controls all processes at a node, a server to handle the inter-node communication requests and services, a planner to provide an efficient plan of communication, and a scheduler to use the resources effectively. Methodologically, these are detailed from a software engineering perspective as we present an example of the agent community in use: supporting a group working in disparate units of the organization. These units include new business acquisition at the strategic level and new services to increase market share units at the tactical level of the organization. © 1997 Elsevier Science B.V.

## 1. Introduction

Organizations attend to their environments. For example, Cargill receives about 14000 messages per day from its 250 branch offices. These are routed to the various trading desks at the Minneapolis headquarters for collection, synthesis, and use [1]. Motorola debriefs its business executives each time they return from overseas and domestic trips [1]. Frito-Lay Inc. uses information technology to track sales figures for specific regions on a daily basis $^{1}$ . Marriott Corp. sends its employees out to try its competitors' hotels $^{2}$ . According to Blaine Davis, Vice President of AT&T strategic and market planning, "We try to make data gathering part of everyone's job" $^{3}$ . Not surprisingly, intelligence gathering budgets range from 50 000 to 1.5M $^{4}$ [2].

The assignment of attentional responsibilities varies with the organization. At General Mills, all members of the organization have been given training in recognizing and tapping sources of competitive intelligence. The sales force has been trained to elicit customer perceptions of competitor product offerings. The R&D staff buys and analyzes competitor product offerings. And in-house focus groups discuss questions such as, "what makes company X effective [3]". NCR recently consolidated its primary and secondary environmental monitoring groups into a single unit, to promote better communication $^{5}$ .

Some organizations pay strong attention to relevant activities [1]:

"Motorola Corporation has set up a unit that bears a striking resemblance to the US government's National Intelligence Council. This unit has about a half-dozen professionals who, like the national intelligence officers in Washington, hold portfolios that match the profile of the company's key objectives and interests. One officer keeps track of European business developments in areas of particular interest to the company; another does the same for Asia. Yet another officer focuses exclusively on developments in specific fields of technology that the company has singled out for special corporate attention and investment. There is an officer who monitors the trade policies of key countries, including the US itself."

These organizations are all attending to their environments for some period of time, but often attend only inconsistently in both frequency and skill. While some similarities in attentional activities exist across organizations, significant differences exist between the prescriptions for attention and the descriptions of attention.

This paper considers the problems of an organization attending to both its external and internal environment. First, it examines the normative and descriptive literature on organizational attention. Next, it examines plausible explanations for the difficulties encountered in scanning. Following this, an approach to ameliorating an organization's attentional deficits is suggested that employs a multi-agent architecture to develop an organizational memory. And finally, an example of the architecture in use is given that includes the strategic evaluation of an emerging technology and its implementation risks to the organization.

## 1.1. Scanning and attention

As described in the academic literature, the normative characterization of an organization attending to its environment (scanning the external and internal environment for threats and opportunities) is one of controlled, continuous, and coordinated perceiving. This normative organization would process strategic, tactical, and operational intelligence [4,5]; comprehensively examine the market strategy of its competitors [6–9]; align its attending activities with its strategy [10,11]; involve all people in the firm [12]; learn to scan its environments and to understand it [13–16]; employ multiple forms of expertise in diagnoses, or radars [9], or collectors [17]; recognize patterns and early warnings [9]; process weak signals [6]; have continuous monitoring [9]; and employ a method of representing the environment and interrelated variables [18–20].

Interestingly, the empirical descriptions of organizational attention fall far short of this mark. For example, the early warning system group is typically in a non-operating department; most often sponsored by a top executive and disbanded when that executive leaves the firm [21]. Clearly, this does not involve all people in the firm, nor does it allow for continuous monitoring. Additionally, this discourages both tactical and operational level attention.

Another barrier to widespread continuous monitoring is the fact that formal group recommendations resulted in many more responses than informal group recommendations $[21]$ . But that is not all: proactive scanners are more likely to prefer a separate organization or to decentralize the activity at the product market or sbu level $[22]$ . Furthermore, 62% of corporations surveyed felt that a lack a intra-firm communications which prohibit dissemination of information from one department to another was at least somewhat important $[22]$ . And, having strategic decision made at the divisional level is the greatest obstacle to corporate-wide environmental scanning $[23]$ . This decentralized approach to attention can mean lost opportunities in comprehensively examining the market strategy of competitors. Furthermore, aligning decentralized attention with the strategy of the firm, where the emphasis is on divisional interests, is inherently problematic.

A further departure from the normative prescriptions for attention have been found in the scanning habits of executives. For example, one study showed that an executive's function is not necessarily related to his/her scanning interest or amount [24]. Thus, scanners operate outside their areas of expertise and are much less likely to understand the environment or serve as a competent collector of weak signals. And, to make matters worse, evaluating the performance of scanners is extremely difficult.

## 1.2. One cause of poor attention

Lenz and Engledow offer an explanation for these problems [2]. Their empirical work showed that the individuals attending to the business environment "...had no coherent concept of the environment to guide their scanning and analysis activities..." resulting from a lack of theory "...sufficient for guiding practitioners...". They go on to say that "broader conceptions of organizational environments concerning the general environment and its functional interdependencies with task-level phenomena are virtually non-existent".

A positive result of organizational attention arises from the ability to modify activities at the task level based on an interpretation of information about the environment with resulting positive outcomes for the firm. If there is poor understanding of either the environment or the link between states of the environment and appropriate task level activities, then there will be problems realizing the normative goals of organizational attention.

This perspective seems to explain many of the issues raised thus far:

Management control of organizational attention is problematic because there is little discipline or consistent set of relationships around which to make evaluations.

Organizational attention rarely succeeds at the corporate-wide level because there is no corporate-wide agreement on the relationship between environment and task.

Organizational attention tends to be organized under a few executive champions with control of discretionary resources adequate for limited scanning who have their own models that link only part of the environment to only part of the task domain in the organization. The champion contracts for limited environmental analysis in an attempt to confirm his/her model and guide task activity within the range of tasks under his/her control.

Many other executives do not contract for organizational attention within their area of expertise because they see such theory-poor activity as having low marginal value.

Unassigned organizational attention amounts to little because of the general foggy understanding of the environment, and of how environment and task are related.

These theory-poor endeavors of organization attention can be categorized according to the levels of knowledge within the organization. That is, Leonard Barton [25] characterizes processes according to stages of knowledge: "The more unpredictable and ill-understood" a process, the closer it resembles an art form, tempered by human observation and judgement rather than by well-understood and proven relationships of a scientific nature. The more predictable and proceduralized the process, the more scientific it is and, consequently, amenable to control by technologies with a specialized range of responses.

As an increase in understanding takes place concerning some given process, a concomitant increase in the level of knowledge also takes place (Table 1). Many of the problems currently found in organizational attention are, then, the result of a low level of knowledge in this area. Empirical evidence suggests that the highest level of knowledge concerning attention-oriented theories falls around level 3 or 4 (recognition of attributes within prototypes or measurement of attributes). But, the consistency provided by levels 5 and 6, repeatable performance and process mechanization, are seldom found outside the areas of financial evaluations.

Changing the underlying causes of this problem is best addressed, then, through increasing the level of knowledge of the organization in its endeavor to attend to the environment. While a simplistic view of the nature of the Catch 23 problem would suggest that increasing the organization's ability to respond to a greater number of contingencies would prompt the organization to better attend to its environment, the organization's sense-making abilities would not be any better than before. Thus, increased flexibility would increase costs without increasing congruence. Alternatively, increasing an organization's ability to sense and interpret the environment would give greater precision to its adaptive moves and result in a successfully flexible organization that could better find congruence in its impacts and structure with the turbulent environment.

The question that must be answered, then, is "How can the organization learn higher levels of knowledge in attending to the environment?"

## 2. Organizational learning and organizational memory

Duncan and Weiss [26] stress that organizational learning involves the learning done by a given individual that can be shared, evaluated and integrated with that done by others, creating a synergistic effect. Weick [27] indicates that organizational memory is an intrinsic component of in organizational learning. Walsh and Ungson [28] argue that organizational memory can facilitate the integration of information across organizational boundaries, aid in organizational decision making and formalization of organizational experiences and procedures can decrease transactional costs and enable decisions to be implemented more efficiently. Currently, information systems that support organizations do a good job of storing and processing data. However, what these systems lack in the organizational memory is information about the decisions that were taken in the past.

Past research has classified existing computer-based systems with organizational memory characteristics into two classes: 1) information integration, and 2) decision support [29]. Information integration systems provide support for storing, searching, indexing and retrieving information not traditionally conducive to relational databases, but these provide little ad-hoc or dynamic information searches. Decision support systems provide limited dynamic access to outside data, but do not tend to support data integration over time. The AC architecture presented in this paper provides support for storing, searching, indexing and retrieving information not traditionally conducive to relational databases, as well as ad-hoc or dynamic information searches to support distributed decision making.

To illustrate the use of such a system, consider an example which entails technology transfer and implementation within an organization. Implementation of new technologies is widely viewed as a competitive weapon $[30,31]$ and may change the way a firm competes in its industry. A decision of this nature may involve experts at several locations within the organization, and may be based on several risks such as: organizational risk, investment risk and technical risk.

For instance, if we view the implementation of a new information technology as a competitive weapon, the organizational risk can be evaluated in terms of the impact the technology can have on the competitiveness of the organization. Organization risk experts form their evaluations based on industry analysis factors such as the potential of the technology to build barriers against new entrants, the ability of the technology to change the basis of competition, the likelihood that the technology can be used to generate new services or products, and the ability of the technology to build switching costs within the industry [32].

Likewise factors to be considered when determining investment risks might be interest rate risks, the value of foregoing other investments, the marketability of the technology, opinions of the stockholders regarding the investment, and the impact the implementation of the new technology will have on the organization's stockholders. Evaluating these factors increases in difficulty if the technology is new and relatively immature, and little base knowledge exists for its use and implementation.

The risks mentioned above are just a sub-set of risks an organization may face when considering the adoption of new technology. Many possibilities exist for modeling these risks. For example, in the evaluation of implementation of new technologies the methods may include: personal opinions of experts on the use and potential of new technologies, complex econometric techniques for managing a portfolio of implementation investments or technological forecasting techniques used when little or no historical data exists on the use of a technology. These methods help the experts arrive at a decision based on their knowledge and experience. However measured, these risks are an indicator of the probability of the success of an event, providing valuable inputs to the final decision maker.

A system designed to support decisions such as those mentioned above should support organizational memory as well as organizational learning. Information from experts should be accumulated on a regular basis by intelligent agent software, equipped with an efficient learning algorithm and search heuristics. The agents should be able to help the organization by acting as an aid to the decision-making process, especially in the absence of the expert. To support organizational memory the accumulated expertise should be available to the entire organization and there should be an effective method to distribute the expertise.

We conclude, from this, that there are areas of decision making in the organization that can be reasonably characterized as being highly distributed, involving expertise, benefiting from increased learning, that could feasibly be addressed by the AC, or at least the promise of AC. But the framework for implementing such solutions has been largely absent, and this provides the motivation for the next section that elaborates on an AC approach for solving such difficulties.

## 3. System architecture

The focus of our architecture is to promote learning and share the knowledge gained across all units that require it. With this goal, the AC can be conceptually viewed as a collection of nodes (one or more at each functional unit), interconnected by a well established communications network. Each node consists of one or more intelligent agents, a manager, a scheduler, a server, a planner, knowledge sources and relevant data structures (Fig. 1). Each of the sub-parts in a node is explained in the following section.

![](/api/attachments/8B3RCHQR/fulltext/images/f4850a47884895fb05d8140b5a9ee5ec50da3deead98f82edbfdaa9cdcccee07.jpg)  
Fig. 1. System architecture at each node.

## 3.1. Intelligent agents

The class of intelligent agents (IA) include software entities that carry out a set of operations on behalf of a user with some degree of independence or autonomy, and in so doing, employ some knowledge or representation of the user's goals or desires. They are designed to learn from examples or patterns using learning algorithms, thereby using and applying the knowledge and experience gained with each decision-making session.

Intelligent agents can be described by the three dimensions of agency, intelligence, and mobility [33]. Agency is the degree of autonomy and authority vested in the agent, and can be measured at least qualitatively by the nature of the interaction between the agent and other entities in the system. At a minimum, an agent must run asynchronously. The degree of agency is enhanced if an agent represents a user in some way. This is one of the key values of agents. A more advanced agent can interact with other entities such as data, applications, or services. Further advanced agents collaborate and negotiate with other agents.

Intelligence is the degree of reasoning and learned behavior: the agent's ability to accept the user's statement of goals and carry out the task delegated to it. At a minimum, there can be some statement of preferences, with an inference engine or some other reasoning mechanism to act on these preferences. Higher levels of intelligence include a user model or some other form of understanding and reasoning about what a user wants done, and planning the means to achieve this goal. Further out on the intelligence scale are systems that learn and adapt to their environment, both in terms of the user's objectives, and in terms of the resources available to the agent. Such a system might discover new relationships, connections, or concepts independently from the human user, and exploit these in anticipating and satisfying user needs [33].

Networked agent applications add a third dimension to the picture $[34]$ . Mobility is the degree to which agents themselves travel through the network. Some agents may be static, either residing on the client machine or at the server. Mobile scripts may be composed on one machine and shipped to another for execution in a suitably secure environment: in this case, the program travels before execution, so no state data need be attached. Finally, agents may be mobile with state, transported from machine to machine in the middle of execution, and carrying accumulated state data with them. Mobility brings a host of security, privacy, and management challenges $[35]$ .

Based on these qualities of agency, intelligence and mobility, an IA can learn from another IA's decision process by contacting another functionally homogenous agent, when it is not able to provide a classification on its own. For instance, in the area of financial planning, when a financial risk IA at one location in an organization is not able to provide a classification based on the extent of its own knowledge, it contacts the financial risk agent at another location within the organization.

## 3.2. Intelligent agent architecture

The IA is made up of three layers—concept formation, knowledge source and blackboard layer.

The concept formation layer makes use of groups of attribute-value pairs, together with the classifications provided by the expert, to form generalizations based on regularities in those groups. The knowledge source layer receives knowledge from the output of the concept formation layer. Specifically, the tree generated by the concept formation layer is parsed to yield a distinct set of concepts that become the knowledge sources for the agent. The blackboard layer acts as the inference engine for the agent, using search information provided by the knowledge sources to opportunistically query the user for specific values of chosen attributes. A description of the nature and functionality of each of the agent's layer is given below.

## 3.2.1. Concept formation

The algorithm used to learn concepts is Unimem [36]. Briefly described, Unimem is a similarity based learning algorithm that creates a hierarchy of feature vectors from inputs of labeled sets of attribute-value pairs. With each new piece of data, Unimem updates its hierarchy. The classifications of the feature vectors are identified by either a single label or a disjunction of labels. Within the hierarchy created by Unimem, those feature vectors close to the root are more general than those nearer the leaves. Also, the arcs pointing to the nodes in the Unimem's hierarchy have predictive attribute-values associated with them. These predictive values provide heuristic search information to the blackboard.

Unimem gathers its new inputs of classified attribute-value pairs from the question answer dialogue between the bank's risk expert and an analyst. The question posed by the expert to the analyst is the attribute, and the answer given by the analyst is the value. The classification of this information, the judgment call made by the bank's risk expert, becomes the label of the attribute-value data.

## 3.2.2. Knowledge sources

The knowledge source level is constructed by parsing the hierarchy formed from Unimem. The result is a number of feature vectors or hypotheses that correspond to each of the hierarchy's nodes, together with the arc labels pointing to them. Thus, a given hypothesis will contain a number of predictive and predictable attribute-values, as well as the classification given to it. The presence and values of predictive values suggests the presence and values of the predictable. Using this as a hypothesis the classification value can be determined. The representation of the knowledge source of a task risk agent monitoring the likelihood of acceptance of a new technological innovation appears as follows.

Predictive Values
[(4)(SPD:low)(SUC:high)(VAL:high)(VIS:high)]
Predictable Values
[(8)(SPD:low)(SUC:high)(VAL:high)(VIS:high)]
(MIN:high)(LAC:high)(PLV:high)]
Classification
[(1)(Highly likely)]

This hypothesis consists of three groups: 1) four predictive values, 2) seven predictable values, and 3) one classification label. In this example, the predictive values indicate that if the speed at which the innovation can be implemented is low (SPD), the level of success with which the innovation can be implemented is high (SUC), the value of the innovation to the organization is high (VAL), and visibility of the implementation is high (VIS). The presence of the predictive values suggest the presence of the predictable values which indicate that it is likely that managerial influence on the acceptance of the innovation is high (MIN), level of acceptance of the innovation will be high (LAC), and the performance level of users is high (PLV). Therefore, the classification indicates the likelihood of success of this innovation for the defined task is high.

## 3.2.3. Hybrid blackboard

The blackboard layer uses an opportunistic search strategy to take advantage of the predictive information offered by the concept formation layer [37]. With each value obtained from the analyst, it changes the focus of attention to the most promising direction. The attributes, values and classification arrived at by a bank's risk expert are used as a learning instance by the IA.

## 3.3. Server process

The presence of multi-agent requests and responses combined with multi-processes justifies the presence of a server process in our design. The server process handles all inter-node communications. Additionally, it creates reliable communication by addressing error checking, re-transmissions, time-outs, and lost messages. The servers communicate with each other using a command inter-node protocol (CIP). The message format is given in Fig. 2.

![](/api/attachments/8B3RCHQR/fulltext/images/f342a8c900edfe3460646b436ac7cd8636086e653db9c51bf35cf83d27ff319f.jpg)  
Fig. 2. Message format.

## 3.4. Manager process

During inter-agent communication tasks are decomposed in such a way that each agent at one level can work independently of others at that level: reporting results only to the immediate superior—which takes care of the necessary interfacing [38]. The hierarchical structure in our framework is implemented with the manager process at the top.

The function of the manager process is to control all sub-processes. Control is implemented by 'context switching', whereby when agents wait for an input, the state of the process is stored and the resources are released for another agent's request. When the input for the IA is received by the manager process, the state of the IA is restored and the problem solving continues. The implementation of the hierarchical structure and context switching are illustrated in Fig. 3.

![](/api/attachments/8B3RCHQR/fulltext/images/5b65afd9e22c1089f27cf3086130363f9ee0f394cb6dad626d72f64b4ba45d15.jpg)  
Finance Department  
Fig. 3. Structure of context switching.

During a problem solving session, while the strategic planning (SP) agent waits for a response through the hierarchical levels, the manager process stores the process state of that SP agent and releases the computer resources (including the knowledge sources) for any other task which we refer to as 'context switching'. When the response is received, the state of the SP agent is restored and the process reactivated.

The manager process is initiated as soon as the node is switched on. For purposes of simplicity, we have assumed that the node is a dedicated agent community (AC) node. It operates on its process table which is stored in 'shared memory'. When a user requests an IA session, the appropriate IA is initiated and an entry is created in the process table. The structure of the table is given as follows:

## (Process #|IA|Owner|State|Att:Val|Time|Pointer to copy)

When the IA needs a value from another agent, it updates the process table with the attribute name and its state to 'wait' and waits for an input. The manager checks the table periodically and when it finds this process in a 'wait' state, the planner is executed. Based on the planner's output, the appropriate agent is contacted through the server. The context (data structures) of the current process is stored and the process state updated to 'sleep'.

When the scheduler contacts the manager with the task request which contains the input value, it reactivates the process, restores the blackboard status from its copy, and updates the process's state to 'go'. When the IA process completes the job, it updates its state to 'idle' in the process table before coming to an end. The manager removes all 'idle' processes after informing the processes that requested the results. The transition states of the processes are shown in Fig. 3. The pseudo-code for the manager process is given below.

```txt
man_process()
{
    initialize all process;
    update process states;
    while true
    {
    if (process state = 'idle')
    {
    check IPC message;
    if (no message)
    check process table;
    if (IA state = 'wait')
    { man_interrupt = IA_wait; man_int();
    else sleep();
    else if (message from scheduler)
    { man_interrupt = scheduler; man_int(); }
    else { man_interrupt = IA_init; man_int() }
    }
}
```

```txt
man_int()
{
case (type of interrupt)
{
    IA_initiate: update process table;
    execute IA process;
    update state = 'go'; }
    {
    scheduler: update process table;
    execute IA process;
    copy black board values to IA process;
    update state = 'go'; }
    {
    IA_wit: execute planner;
    copy black board values to process table;
    update IA state = 'sleep'
    if (remote agent)
    {
    add request to server;
    send message to server process;
    }
    else execute IA_initiate;
    update manager state = 'go'; }
}
```

When a message is to be sent to another node, the server contacts all relevant nodes, using a broadcast method, with a REQT message based in the plan. When it receives a positive acknowledgment (ACKN), it sends a CANC message to all the other nodes that have been contacted earlier and establishes a communication session with the node that acknowledged the request. If it does not receive any acknowledgment, it re-transmits the same request after a specified interval. This re-transmission is done based on the 'retry' and 'time limits' that are pre-set by the manager. It then sends a DATA message containing the attribute--values known to it. The receiving node acknowledges it, processes it, and sends back a REST message. A negative acknowledgment is sent when the agent is in the 'go' or 'sleep' state.

## 3.5. Scheduler process

Efficient utilization of resources is an important issue to be addressed by any multi-tasking systems. The presence of multiple agents at a node, coupled with requests from other nodes, warrants the presence of an efficient scheduler to service all task requests in some pre-defined order. There are several scheduling algorithms in use today (round robin algorithm, multi queuing, priority queuing) [39]. Since problem solving in AC is the focus here, there are two approaches to assigning priorities: 1) organizational queuing—ordered by the importance of the agent's role in the organization; and 2) functional queuing—each unit considers tasks initiated by it to have the highest priority. We have adopted scheduling based on functional priority queuing.

Table 2  
Functional priority queuing

<table><tr><td colspan="2">A</td><td colspan="2">B</td></tr><tr><td colspan="2">Task owner</td><td colspan="2">Task owner</td></tr><tr><td>SP</td><td>N1</td><td>SP</td><td>N1</td></tr><tr><td>PR</td><td>N2</td><td>IR</td><td>N1</td></tr><tr><td>IR</td><td>N1</td><td>PR</td><td>N2</td></tr></table>

For example, 3 tasks pending at node N1 in Table 2 (A) will be scheduled for execution in the order shown in (B), since tasks initiated by N1 have a higher priority.

## 3.6. Planner

The function of the planner is to provide an efficient plan of communication in order to maintain focus and achieve high performance. The planning algorithm could be based on various factors such as cost, distance between nodes, efficiency, time etc. Since our focus is on learning, the plan is created based on the level of expertise. For example, if two organizational risk agents in different locations with level 1 and level 2 expertise are available to solve a problem, the level 2 expert is always contacted first. The level of expertise could be generated by implementing a learning algorithm to monitor the accuracy of an agent's prediction. At present, we assume that the level of expertise is available in the global directory.

## 3.7. Global agent directory

This directory is stored in a pre-defined node (master node) and contains information about the IAs—address, capabilities etc. Distributed systems store knowledge about the network in some form. Yang et al. presents this information as metaknowledge in their paper on distributed systems $[40]$ . During the initialization of a node, a copy of this directory is brought to the local processing area using a cached scheme $[41]$ . This scheme exploits locality of reference and reduces network traffic and communication overhead between the nodes; the cached copies are updated using a read-only policy whereby all updates are sent to the master node, which propagates changes to all nodes. Since a copy is available on all active nodes, in the event of a failure at the master node, the copy can be obtained from another active node.

Agent directory format

<table><tr><td>Fields</td><td>Remarks</td></tr><tr><td>Agent name</td><td>The name of the agent</td></tr><tr><td>Description</td><td>A brief description of the agent</td></tr><tr><td>Node address</td><td>The node at which the KS are stored</td></tr><tr><td>Level of expertise</td><td>Level of expert</td></tr></table>

## 3.8. Interaction between the components

The manager process is reactive, triggered by the arrival of requests from a local user or incoming communications from the server. After initiating all processes the manager then goes into a 'wait' state, waiting for the user or scheduler to contact it. Once the manager is contacted, the appropriate intelligent agent process is initiated and manager changes both its own state and the IA's process state to 'go'. When the intelligent agent requires the expertise of another agent during the problem solving session, it contacts the manager process and goes into the 'wait' state. The manager process then contacts the planner module which provides the communication plan. Based on this plan, if the manager has to contact a remote agent, it adds a request to the server's queue and then stores all the necessary data structures and values of the process, and releases the resources by ending the IA process. It updates the state of the IA process to 'sleep' and its own state to 'idle'. When the IA process's request is serviced by the remote node, the server enters it as a task in the task queue and when it is scheduled for execution, the manager process initiates the IA process, restores all the values to the previous state, and updates the IA process and its own state to 'go'. The IA process then continues with the processing and informs the manager of its completion by updating its state to 'wait'. When the manager is in the 'idle' state, the scheduler can contact it with other task requests from remote intelligent agents and these are also processed in a similar way. The transition states of the processes is shown in Fig. 4.

![](/api/attachments/8B3RCHQR/fulltext/images/624220abb6fd9bcc7c5ea8862033211e912e3904b76175093ad8561962cb3ca4.jpg)  
Fig. 4. Transition states.

## 4. Example of problem solving using the AC architecture

To illustrate the distributive characteristics of the architecture, an example of decision making with experts is given. The example is adopted from the Harvard Business School case study, "Bank of Boston's Expert Systems (A)", by John Sviolka [42]. The BoB is considering the adoption of a new technology, expert systems, within the bank. Normally the bank would identify a problem and then identify a technology that could be used to solve it. But in this case the bank saw the new technology, that of expert systems, as an opportunity to be exploited. This decision involves strategic decision making as well as tactical decision making. At the strategic level BoB needs to evaluate the technology in terms of organizational risk and investment risk. At the tactical level BoB needs to evaluate possible implementation opportunities to determine which is optimal.

## 4.1. Evaluation of pursuit of ES technology at BoB

Information systems (IS) offer a unique opportunity for competitive advantages $[30]$ , but identifying which technologies to implement involves various types of risk assessments and requires evaluations of those risks from various experts within the organization. BoB needs to evaluate the pursuit of the potential of ES technology to improve performance and decision-making capability and its ability to enhance the competitiveness within the banking industry. The assessment will be made by evaluating the risks and other factors associated with this type of decision, at the strategic level two risks are prominent: 1) organizational risk; and 2) investment risk. Factors associated with these risks are shown in Table 3. In order to simplify the example we will discuss the interaction of three agents, the strategic planning agent at node 1, the organization risk agent at node 2, and the investment risk at node 3 and 4.

The manager initiates all needed processes and structures and goes into an 'idle' state when the node is turned on. When a user initiates a problem solving session with the strategic planning agent, the manager initiates the agent process and creates an entry in the process table. During the course of the problem solving session, the strategic planning agent requires an input from the investment risk attribute. Since it does not have the expertise to solve the problem, it updates the process table with the investment risk agent's attribute and goes into the 'wait' state. The process table status is shown in Table 4a.

<table><tr><td>Table 3Strategic decision risks</td></tr><tr><td>Organization risk</td></tr><tr><td>PBE — potential of the technology to build barriers against new entrantsCCO — the ability of the technology to change the basis of competitionNSP — the likelihood that the technology can generate new servicesSWC — the ability of the technology to build switching costs</td></tr><tr><td>Investment risk</td></tr><tr><td>IRR — Interest rate riskSES — salability of the technology once developedOSH — opinion of the stockholders regarding the investmentVOO — the value of foregoing other R&amp;D options</td></tr></table>

Table 4  
Process table

<table><tr><td></td><td>Process #</td><td>IA</td><td>Owner</td><td>State</td><td>Attribute</td><td>Value</td><td>Time BB</td><td>Ptr to</td></tr><tr><td>a)</td><td>1</td><td>SP</td><td>N1</td><td>wait</td><td>IR</td><td>?</td><td></td><td></td></tr><tr><td>b)</td><td>1</td><td>SP</td><td>N1</td><td>sleep</td><td>IR</td><td>?</td><td></td><td>ptr1</td></tr><tr><td>c)</td><td>1</td><td>SP</td><td>N1</td><td>go</td><td>IR</td><td>high</td><td></td><td>ptr1</td></tr></table>

The manager periodically checks the table and when it sees the process in a ‘wait’ state, executes the planner, which checks the directory and provides a communication plan based on the level of expertise and location.

Since the agent to be contacted does not reside in the local node, the manager adds a request to the server's send queue. It then updates the process table by changing the agent's state to 'sleep', copies the relevant blackboard values and places a pointer value in the table. The updated table is shown in Table 4b. When the state of the strategic planning agent process is changed to 'sleep', the process has ended and the state of the manager process is changed to 'idle'.

To obtain the investment risk information the server at N1 contacts the server at N3 by sending a REQT message. During the problem solving session, the investment risk agent at N3 is not able to arrive at a solution based on its knowledge, it then updates its process table and goes into a 'wait' state. The manager at N3 executes the planner module. Since the only other agent capable of solving it is in N4, the manager process at N3 constructs the message and adds it to the server's queue at N3. The server then sends a request message to N4, and assuming that the investment risk agent at N4 solves the problem, it sends the result back to N3. This information is used by the agent at N3 as an input to its learning module, and updates its knowledge base. The result is passed back to N1 which made the original request.

Although it would be possible for the server at N4 to send the needed information directly to N1, the server sends the needed information to N3. This allows the agent at N3 to update its knowledge base with the new information and thereby enhance its learning. Fig. 5 is a shows the communications between the three nodes. The explanation of each communication is given in Table 5.

![](/api/attachments/8B3RCHQR/fulltext/images/fe7272949f3884e9a71afc8f87219aa4617bba9af4d3cc8b6c6a6f7bce812b9c.jpg)  
Fig. 5. Inter-node communication.

The manager process reactivates the SP agent process by initiating the process again and restoring the values from its copy. The status of the process table is shown in Table 4c. The strategic planning agent process checks the process table att-val field and, if it is not empty, picks up the value and stores it in its blackboard and continues processing from where it had stopped. When it requires an input for the organization risk attribute, the same process is repeated. Although this seems like a continuous dialog, in actual cases, it may be interspersed with requests from other nodes (Fig. 6).

## 4.2. Tactical decision making

Once BoB had decided to move ahead with the implementation of ES technology the next decision to be made was to determine a task area for implementation. Three areas emerged as avenues for ES implementation: 1) repurchase agreements; 2) federal funds trading; and 3) market monitors and foreign exchange.

Initial implementation of a new technology is a dynamic process of mutual adaptation between the technology and its environment. Implementation problems of new technologies are as challenging as the invention of these technologies, and the initial implementation stage is especially critical $[25]$ . During the early stages of working with a new technology the risk can be high since there is little experience to draw on.

This tactical level decision has risk and other factors associated with it. Two major risk factors are listed in Table 6. The choice of implementation area was to be based on several factors including: how fast the option could be implemented (SPD); how successful the implementation was likely to be (SUC); what value the implemented task would have to BoB (VAL); the level of visibility of the imple-

Table 5  
Dialog between the nodes

<table><tr><td>Time</td><td>Explanation</td></tr><tr><td>1</td><td>Node N1 sends a message to node N3 requesting the investment agent&#x27;s expertise</td></tr><tr><td>2</td><td>Node N3 receives the message and sends back an acknowledgment</td></tr><tr><td>3</td><td>Node N1 sends a message containing data (attribute values known to it) to N3</td></tr><tr><td>4</td><td>Node N3 receives it, checks it and acknowledges it</td></tr><tr><td>5</td><td>Node N3 is not able to solve it, so it sends a request to Node N4</td></tr><tr><td>6</td><td>Node N4 receives the message and acknowledges it</td></tr><tr><td>7</td><td>Node N3 sends a message containing data (attribute values known to it) to N4</td></tr><tr><td>8</td><td>Node N4 receives it, checks it and acknowledges it</td></tr><tr><td>9</td><td>Node N4 sends a message containing the result to N3</td></tr><tr><td>10</td><td>Node N3 receives it, checks it and acknowledges it and updates its knowledge base</td></tr><tr><td>11</td><td>Node N3 sends the result back to N1</td></tr><tr><td>12</td><td>Node N1 receives it, checks it and acknowledges it</td></tr></table>

![](/api/attachments/8B3RCHQR/fulltext/images/aaaa6aa7fe0e61c84f3784fee53b4558424d057a213378ef2336777ebd1149a4.jpg)  
Fig. 6. Strategic planning problem solving tree.

mented task within BoB (VIS); and the design uncertainty of the task (DUN). Whenever an organization takes on the challenge of implementing a new technology, whether it be expert systems, client server technology, object-oriented databases or the use of intelligent agents, the cost will likely be high if the technology is new to the organization and might be very high if the technology is new in general and experts are few. The technical implementation risk reflects these levels and costs of expertise as well as task–technology fit.

Table 6

<table><tr><td>Tactical decision risks</td></tr><tr><td>Task risk</td></tr><tr><td>SPD — speed at which the option can be implemented</td></tr><tr><td>SUC — level of success at which the option can be implemented</td></tr><tr><td>VAL — value of this option, once implemented,to the organization</td></tr><tr><td>VIS — level of visibility of the implementationwithin the organization</td></tr><tr><td>DUN — design uncertainty</td></tr><tr><td>Technical implementation risk</td></tr><tr><td>LEX — level of expertise within the organizationon this technology</td></tr><tr><td>CEX — cost of expertise (consultants, outsourcing, etc.)</td></tr><tr><td>TTF — task technology fit</td></tr></table>

Our example will demonstrate the interaction of the tactical planning agent at node 1 and the task risk agent which is located at nodes 2, 3 and 4. The setup phase and the development and updating of the process tables are similar to the strategic planning example. However, the communication of the nodes is more complex in this example. To obtain the task

![](/api/attachments/8B3RCHQR/fulltext/images/08904806cf7c9ff4065bafdf6604ab20f12dacdd36e942af618a86c238b0cd62.jpg)  
Fig. 7. Inter-node communication.

risk information the server at N1 contacts the server at N3. Even though there are three task risk agents (TA) at nodes 2, 3, and 4. The TA at N3 has the highest level of expertise as indicated in the global agent directory. The TA at N3, while processing the request from N1, is not able to arrive at a solution. It requires more information and contacts the TA at N4—which has the second highest level of expertise. The TA at N4, while processing the request, requires information from the TA at N2. The TA at N2 sends the results back to N4, and the TA at N4 updates its knowledge base using the information from N2. The server at N4 then sends the results of the request back to N3 which also updates its knowledge base with the new information, and then sends the completed results of the request back to N1. In the process, the knowledge bases of the TA at both N4 and N3 have been enhanced, thus providing for organizational learning. Fig. 7 shows the inter-node communication of this process. Fig. 8 shows the tactical planning solving tree.

![](/api/attachments/8B3RCHQR/fulltext/images/b188684d3317a9b6fed27ef34eb0744d747ba0e77f678e6d9683c177a69ffd7c.jpg)  
Fig. 8. Tactical planning problem solving tree.

## 5. Discussion

The agent community illustrated in this paper show how the use of an IA in a distributed communication network can support distributed decision making. Several organizational trends and needs, such as decision support systems to support organizational restructuring, the importance of organizational learning and organizational memory, drive this research. And several recent technology innovations, advances in communication technology, artificial intelligence and its relationship to decision support system, support the architecture.

The quality of an organizational decision is largely a combination of the quality of the organization's intelligence, acquired through learning and memory, and the quality of the decision-making process. The main premises in the design of this AC framework are the support of distributed decision making, and the support of organizational learning and organizational memory.

Through the support for distributed decision making, the AC framework enhances both the access to information and knowledge and the sharing of information and knowledge. Such a design facilitates the efficient use of the organization's intelligence by distributing it throughout the organization.

The system is also designed to support organizational learning and organizational memory. Organizational memory facilitates the integration of information across organizational boundaries, aids in organizational decision making and can decrease transactional costs and enable efficient decision making $[28]$ . Organizational memory is an intrinsic facet of organizational learning. Organizational learning involves the learning of an individual that can be shared, evaluated and integrated with that of others $[26]$ . To support learning, the decision-making information used by experts is accumulated on a regular basis by intelligent agent software. When processing information for use, if an agent is not able to arrive a solution, it needs to contact another agent to provide supplemental information. The agent, after contacting a second or even a third agent, will update its knowledge base with the newfound information—thus providing for organizational learning.

## 6. Conclusions

With advances in software, hardware and communication technology and restructuring of organizations, the focus of decision support has shifted to the entire organization. A higher integration of organizational knowledge and organizational learning and memory have become imperative for organizations who wish to remain competitive.

This paper presented an approach to an agent community that supports group decision making over a multi-agent network, designed to enhance organizational memory and organizational learning. By using this framework, an organization's expertise is automatically accumulated and classified. The approach taken in this paper was technical—providing a description of the AC architecture.

The paper had three main foci. First, the knowledge is distributed across an organization. This supports the analysis of complex problems that involve continuous monitoring and interpretation by multiple distributed experts. The knowledge of the experts is automatically available to any of the units that require it. Second, the system provides for organizational memory. Knowledge from experts within the organization is automatically accumulated and classified, and is made available to the entire organization. Third, the AC provides for organizational learning by assisting an expert in predicting results based on the extent of its knowledge. An agent also learns from another agent's expertise when it is not able to solve a problem.

Although this paper addresses several important issues in the use of IA to support distributed decision making, there are several technical, design and organizational issues that remain unexplored. Technical issues include security and integrity, errors in communication, and network reliability. Design issues include the linking of heterogeneous agents, such as expert systems or neural networks, or the design of an interface that would allow these various kinds of software to communicate with this AC. Organization issues include ideas such as ownership of data, longevity and relevance of decision-making information. These issues may provide fertile grounding for future research.

## References

[1] R. Amit, I. Domowitz, C. Fershtman, Thinking One Step Ahead: The Use of Conjectures in Competitor Analysis, Strategic Management Journal 9 (1988).

[2] A.G. Badein, Contemporary Challenges in the Study of Organizations, Journal of Management 12 (2) (1986).

[3] C.S. Bates, Mapping the Environment: An Operational Environmental Analysis Model, Long Range Planning, 18 (5) (1985).

[4] D. Chess, B. Grosof, C. Harrison, D. Levine, C. Parris, G. Tsudik. Itinerant Agents for Mobile Computing. IEEE Personal Communication Services Magazine 5 (1995) 34–49.

[5] R.L. Daft, G.P. Huber, How Organizations Learn: A Communication Framework, Research in the Sociology of Organizations, 5 (199X) 1–36.

[6] R.L. Daft, K.E. Weick, Toward a Model of Organizations as Interpretation Systems, Academy of Management Review 9 (2) (1984).

[7] B.W. Denning, Strategic Environmental Appraisal, Long Range Planning (1973).

[8] R.B. Duncan, A. Weiss, Organizational Learning: Implication for Organization Design, in: B. Staw (Ed.), Research in Organizational Behavior, JAI Press, Greenwich, CT, 1979, pp. 75–123.

[9] R.B. Duncan, Modifications in Decision Structure in Adapting to the Environment: Some Implications for Organizational Learning, Decision Sciences (1974) 705–725.

[10] G.S. Elofson and B.R Konsynki, Delegation Technologies: Environmental Scanning with Intelligent Agents, Journal of Management Information Systems 4 (2) (1991).

[11] T. Gilad and B. Gilad, SMR Forum: Business Intelligence — The Quiet Revolution, Sloan Management Review, Summer 1986.

[12] D. Gilbert, Intelligent Agent Strategy, IBM White Paper, IBM Corporation, 1995.

[13] D.C. Hambrick, Specialization of Environmental Scanning Activities Among Upper Level Executives, Journal of Management Studies 18 (3) (1981).

[14] B. Ives, G.P. Learmonth, The Information System as a Competitive Weapon, Communications of the ACM, 27 (12) (1984).

[15] S.C. Jain, Environmental Scanning in US Corporations, Long Range Planning, 17 (1984).

[16] A. Kefalas, P. Schroderbek, Scanning the Business environment — Some Empirical Results, Decision Sciences, 4 (1973).

[17] H. Klein, W. Newman, How to Use Spire: a Systematic Procedure for Identifying Relevant Environments for Strategic Planning, Journal of Business Strategy, 5 (1980).

[18] D. Lebell, O.J. Krasner, Selecting Environmental Forecasting techniques from business planning requirements, Academy of Management Review, July 1977

[19] M. Lebowitz, Generalization from Natural Language Text, Cognitive Science, 7 (1983).

[20] R.T. Lenz, J.L. Engledow, Environmental Analysis Units and Strategic Decision Making: A Field Study of Selected "Leading-edge" Corporations, Strategic Management Journal, 7 (1986).

[21] D. Leonard-Barton, Implementation as Mutual Adaptation of Technology and Organization, Research Policy, 17 (1988) 251–267.

[22] J. Martin, Information Engineering: A Trilogy, Vols. 1–3, Prentice Hall, Englewood Cliffs, NJ, 1989.

[23] F.W. McFarlan, IS and Competitive Strategy, Note 0-184-055. Harvard Business School, Cambridge, MA, 1983.

[24] H.E. Meyer, Real World Intelligence, Weidenfield and Nicolson, New York, NY, 1987.

[25] J. Morrison, Team Memory: Information Management for Teams, Proceedings of The Hawaiian International Conference of Systems Sciences, Vol. IV p. 122-131. Jan 4–9, 1993.

[26] R.M. Narchal, K. Kittappa, P. Bhattacharya, An Environmental Scanning System for Business Planning, Long Range Planning, 20 (6) (1987).

[27] F.T. Pearse, Business Intelligence Systems—the Need for Development and Integration, Industrial Marketing Management, (1976) 115–138.

[28] W.A. Reinhardt, An Early Warning System for Strategic Planning, Long Range Planning, 17 (5) (1984).

[29] S.P. Roy, J.K. Cheung, Early Warning Systems: A Management Tool for Your Company, Managerial Planning, March/April 1982.

[30] S.M. Sanderson, G.A. Luffman, Strategic Planning and Environmental Analysis, European Journal of Marketing, 22 (2) 1986.

[31] E. Segev, How to Use Environmental Analysis in Strategy Making, Management Review, March 1977.

[32] P. Seiber, M. Clements, Monitoring Competitors' Promotional Activities to Obtain Marketing Data", International Trade Forum, July–September, 1985.

[33] W. Skinner, The Productivity Paradox, Harvard Business Review, 86 (4) (1986).

[34] D.C. Smith, J. Prescott, Demystifying Competitive Analysis, Planning Review, Sept/Oct, 1987.

[35] R.G. Smith, A Framework for Problem Solving in a Distributed Processing Environment, STAN-CS-78-700, Stanford University, 1978.

[36] C. Stubbart, Are Environmental Scanning Units Effective?, Long Range Planning, 15 (1982).

[37] J. Sviolka, Harvard Business School case study, Bank of Boston's Expert Systems (A)", Harvard Business School.

[38] A.S. Tanenbaum, Operating Systems, Macmillan, New York, NY, 1991.

[39] S. Virdhagriswaran, D. Osisek, P. O'Connor, Standardizing Agent Technology, ACM Standard View (1995).

[40] J.P. Walsh, G.R. Ungson, Organizational Memory, Academy of Management Review, 16 (1) (1991) 57–91.

[41] K.E. Weick, The Social Psychology of Organizing, Addison-Wesley, Reading, MA, 1979.

[42] J.D. Yang, M.N. Huhns, L.M. Stephens, An Architecture for Control and Communications in DAI Systems, IEEE Transactions on Systems, Man, and Cybernetics, SMC-15 (3) (1985).

Greg S. Elofson received his PhD in MIS from the University of Arizona and is currently on the Decision and Information Analysis faculty at the Emory University Goizueta School of Business. His research interests include the use and effects of intelligent information technologies in competitive intelligence and organization design. He has published many articles in scholarly journals such as the Journal of Management Information Systems, IBM Systems Journal, Decision Support Systems, Expert Systems with Applications, The Group Decision and Negotiation Journal, and Information and Software Technology. Formerly, Dr. Elofson conducted SDI research as a staff scientist in the artificial intelligence architectures group of Science Applications International and was engaged as a consultant in many IS related capacities on behalf of Arthur Andersen and Co.

![](/api/attachments/8B3RCHQR/fulltext/images/dff6690942773d429e74e4e9cd58c64f0f33f82bd5683c522b91f904c4261967.jpg)

Dr. Beranek received her PhD in Management Information Systems from the University of Arizona in 1991 and is currently an assistant professor in the Computer Information Systems department at Georgia State University. Her research interests include the use of Group Decision Support Systems in business, facilitation issues for GDSS, and distributed GDSS. She has published papers on facilitation skills of GroupWare facilitators, the use of dis-

tributed GDSS technology, and usefulness and ease of use issues in the design of computer interfaces. She has previously published in Management Information Systems Quarterly, Decision Support Systems, as well as other Information Technology journals.

Philomina Thomas-Hosdurg is a Bueinss Architect at UCA and L. a company that provides outsourcing services to high technology companies such as Microsoft, Apple, Sony, etc. She is currently working on an enterprise-wide systems re-engineering effort using object-oriented technology. She received a bachelor's degree in science (1983) from the University of Madras, India, and a master's degree in Computer Information Systems (1993) from the University of Miami. During her graduate studies her focus was on studying organizational decision support systems. She has worked on many commercial systems software products in capacities ranging from programmer to project leader at Wipro Information Systems, Bangalore, India.
