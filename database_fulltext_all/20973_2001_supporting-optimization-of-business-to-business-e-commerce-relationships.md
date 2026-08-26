---
otero_id: 20973
otero_key: "DYVKWHSW"
title: "Supporting optimization of business-to-business e-commerce relationships"
authors: "William Kuechler; Vijay K Vaishnavi; David Kuechler"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00142-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Supporting optimization of business-to-business e-commerce relationships

William Kuechler Jr. <sup>a,)</sup>, Vijay K. Vaishnavi <sup>b</sup>, David Kuechler <sup>b</sup>

<sup>a</sup> Department of Accounting and Computer Information Systems, UniÕersity of NeÕada at Reno, Reno, NV 89557, USA b Department of Computer Information Systems, Georgia State UniÕersity, Atlanta, GA, USA

## Abstract

Much current e-commerce subscribes to very simple interaction models. Many of the potentialities of e-commerce are identical to those that have been under study for some time in the field of automated workflow management systems. In this paper, we describe a new workflow interoperability model, the monitored–nested model MNM( ), and show that it can support optimized, extended e-commerce transactions that are not supported by current models.

Like other interoperability models, MNM is dependent on process activities, and thus is brittle under real-world conditions of process evolution. This is overcome by augmenting the model with goal-based meta-data and the use of a coordination inferencing algorithm. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Workflow; E-commerce; E-business; Inter-organizational systems

## 1. Introduction

Recent studies by technology consulting groups predict more than one fourth of all business to business B2B purchases will be transacted on theŽ . Internet by 2004—a dollar volume 10 times that of Internet consumer purchases. The explosion in Internet-based B2B is driven by economics—the Internet offers the potential for reduced prices for goods and reduced transaction costs, but this is not simply derived from the Internet as a communications infrastructure. The capability for relatively inexpen- Ž . sive electronic B2B communications has existed for some time in highly evolved form, as witnessed by

EDI. Newer, Internet based e-marketplaces as they are currently conceived overcome some of the problems encountered with traditional EDI, and constitute essentially a better–cheaper-EDI.

As business-to-business e-commerce moves closer to its full potential, it will progress beyond a better–cheaper-EDI to the support of business relationships that match or exceed the dimensionality of non-electronic relationships. However, support and optimization of such relationships require more sophisticated models of interaction than those currently in use.

## 1.1. Beyond EDI to online trading communities

Traditional EDI is a one-to-one technology: buyer and seller must locate each other and then perform substantial work to link their systems. The new

Internet-based online trading communities, such as Ariba 1 , i2 7 , and CommerceOne 3 , in addition<sup>w x</sup> <sup>w x</sup> <sup>w x</sup> to enabling B2B transactions so facilely that they have been termed e-commerce vending machines <sup>w</sup> <sup>x</sup> 12 , are true markets. Within each community, an ontology—common business processes and electronic documents including product definitions and pricing—is defined in a standard language XML Ž . and published for universal access. Product offerings and prices from multiple suppliers can be electronically scanned and processed at very low error rates leading to predictions of billions of dollars per year in procurement cost savings.

## 1.2. ImproÕing online trading communities

The efficiency of many operations in e-commerce transactions is less than optimal because they operate from Õery simple relationship models. Essentially, current online trading communities automate the most basic order–receiÕe–pay scenario:

v The purchaser electronically scans the marketplace and chooses a product

v The price, quantity and a delivery date are agreed upon using standardized XML-described order documents.

v An electronic invoice is sent from supplier to purchaser at or about the time of deliveryŽ .

v The purchaser schedules automated payment on confirmation of delivery

Notice that there is no proÕision in this scenario for multi-party transactions and no proÕision for exceptions. As e-commerce matures, we believe online trading partner relationships will rapidly push toward the sophistication and complexity found in non-automated business relationships, which are desirable precisely for their ability to integrate the efforts of multiple legally independent entities while accommodating exceptions and changes.

In the basic order–receive–pay scenario, transactions between companies are considered to be atomic, that is, no detail on the execution of the transaction is available. The lack of detail makes it impossible for companies to interact with the richness that current manual relationships possess. For example, delays in production are hidden until the delivery date is exceeded. Or, changes in specification that appear minor to one party but are significant to another remain unknown until the delivered product is closely inspected, possibly on the assembly line floor!

## 1.3. Workflow management system concepts and ecommerce

Workflow management systems WfMS are soft-Ž . ware systems that facilitate, augment and sometimes control the flow of work within and for our pur-Ž poses especially between organizations. As interor- . ganizational WfMS become increasingly common and as the interaction between WfMS becomes increasingly web-based, much automated workflow enactment becomes by definition electronic commerce <sup>w</sup> <sup>x</sup> 22 .

The notion that automated business processes, executed oÕer the Internet between multiple organizations, are the future of electronic commerce is at the core of the visions of authors from many fields. It also figures prominently in the literature of many commercial Internet marketplace-hosting organizations see Fig. 1 . According to Sheth et al. 17 ,Ž . <sup>w</sup> <sup>x</sup>

![](/api/attachments/DYVKWHSW/fulltext/images/e0de3c50eb6ea996df54225dd399f555a3e033f620b2df0f2722dbb8173b9c50.jpg)  
Fig. 1. Commercial e-commerce service providers view of interorganizational workflow. A composite view taken directly from the marketing literature of commercial e-marketplace hosting organizations 1,3,7 .<sup>w</sup> <sup>x</sup>

A . . . we see processes as an organic component of any enterprise application integration or e-commerce solution. In this sense, workflow-process technology will conduct the emerging networked economy from behind the scenes.B Jain et al. 8 see agent enacted<sup>w</sup> <sup>x</sup> workflows and a form of intention-driven e-commerce transaction similar to the one presented in this paper as the enabling technology for virtual corporations. These visions propose workflow-as-e-commerce in the near future since by definition the automation of formal process definitions is workflow management. Charles Petrie, executive director of the Stanford Networking Research Center, writing with Sunhil Sarin, a commercial WfMS developer and researcher, state the case even more strongly: AInternet mediated workflow will be the most important technology of the early 21st centuryB <sup>w</sup> <sup>x</sup> 14 .

We propose that many of the problems and potentialities that exist for e-commerce are exactly those that have been under research for some time in inter-organizational WfMS. Workflow interoperability models provide the foundation for the study of relationships between autonomous workflows and for the technology to model and enact such relationships.

## 2. Workflow interoperability models and business scenarios

Although they are not complex, workflow interoperability models are best discussed in relation to business scenarios that give depth and concreteness to the concepts. This is the approach taken by the Workflow Management Coalition, an international group of commercial WfMS producers and WfMS researchers. The order fulfillment example given here Ž . see Fig. 2 is a minor variation on a benchmark used in Workflow Management Coalition documents to give a standard for comparisons. The example is simple, but is capable of illustrating most points that arise in far more complex real world interactions. We will later expand this example to illustrate desired optimizations of B2B e-commerce relationships that go beyond the order–receive–pay model implicit in EDI type interaction. We propose two expansions of the base scenario as part of a benchmark suite for extended WfMS interoperability.

In the base scenario illustrated in Fig. 2, all participants are assumed to have a WfMS. Retailer sells an item of furniture that must be custom-made and drop-shipped from Manufacturer. Manufacturer is responsible for contracting for shipping the item to customer. Each column of the figure represents the progression of high-level tasks required for that portion of order fulfillment processing required of each of the cooperating business entities. The high-level tasks, such as Schedule Production may be instantiated in the Manufacturer’s workflow by a series of lower-level activities that accomplish the higher-level task; this detail has been omitted for clarity. Each entity’s tasks are interleaved, taking place in parallel. The events proceed in the conventional WFMC scenario as they have been numbered in Fig. 2, from 1 to 10. The shaded segment of the figure depicts the optimized workflow discussed below.

For even the base scenario to proceed, the WfMS in each of the cooperating organizations require information on:

1. the location of contractors on which it depends Ž . interoperates

![](/api/attachments/DYVKWHSW/fulltext/images/7757e1aeaa688b20fd5dbda4f321bc2e1ff7ee0199af539369ea770ca47405a1.jpg)  
Fig. 2. Basic and optimized order fulfillment via interoperating processes.

2. a format for the communications requests forŽ service that will be understood by the other. WfMS

3. how the workflow that is requesting service is to behave during the performance of service

4. an expectation of and format for a return communication s indicating various states of the re-Ž . quested service s .Ž .

Information items 2, 3, and 4 can be abstracted to a workflow interoperability model; reference to common interoperability models will be useful in discussing improvements to the ordering process. The Workflow Management Coalition defines three interoperability models in its interoperability document <sup>w</sup> <sup>x</sup> 21 : chained interoperating processes, nested interoperating processes, and parallel-synchronized interoperating processes see Fig. 3 . Ž .

The Chained Interoperability Model is the least complex in that it requires a WfMS to possess the least information about cooperating WfMS. Chained processes or subprocesses are invoked by one Ž . WfMS in another WfMS and no further interaction takes place with the subprocess. In Workflow Management Coalition terms, they are ‘trusted’ processes and delegation to them is total. Chained processes are defined in WPDL the Workflow ManagementŽ

Coalition’s process description language as activi-. ties whose type is subprocess and whose execution mode is asynchronous.

In a Nested Interoperability Model, once the call is made by a process to a subprocess, the calling process suspends operations until the subprocess completes. Nested subprocesses are defined in WPDL as activities whose type is subprocess and whose execution mode is synchronous. Note that since WPDL supports multiple threads in a workflow, the overall workflow that issues the nested subprocess call need not suspend; only the calling thread suspends. Nesting may recurse.

In the parallel-synchronized Interoperability Model, workflows run in parallel on different WfMS and are required to achieve periodic synchronization points. Parallel-synchronized interoperability has been designated by the Workflow Management Coalition as outside the scope of their current interoperability specifications. This is due to the complexity involved in generalizing this type of interaction between systems, and its lack of robustness under activity changes, a problem detailed in Section 4.

The workflow interaction in the order fulfillment scenario is modeled by the nested interoperability model. Nested subprocesses correspond exactly in the example to the calls for service from the Retailer to the Manufacturer and from the Manufacturer to Shipper.

![](/api/attachments/DYVKWHSW/fulltext/images/1c4cdb2e675559e8e44b3de48faab108b80a78141ef9bd36ac5b967d83ba9af1.jpg)  
Parallel Synchronized  
Fig. 3. Workflow interoperability models.

## 2.1. Optimizing B2B relationships: proposal for a benchmark scenario

As presented in WFMC literature the order fulfillment scenario requires confirmation from both Shipper and Manufacturer before the Retailer invoices the client. Suppose, however, that Shipper’s performance became predictable. A desirable optimization under such conditions one first widely demonstratedŽ by the Japanese would be to use that predictability. to decrease the overall business cycle time by invoicing the client at an earlier point—say when the shipping of the item was scheduled—to improve cash flow. However, the invoice must come from the Retailer, and using simple nested interaction, the Retailer is two levels removed from the information required. That is, the Retailer invoked the Manufacturer’s process and has no information on that process state until it completes. The Manufacturer’s process invoked the Shipper’s process, and has no information on that process state till it completes. There are thus two levels of isolation using the nested workflow interoperability model from the information required to optimize the overall process.

The suggested improvement in overall workflow is shown in the shaded section of Fig. 2. The dashed arrow from activity 5 Manufacturer’s Schedule Shipping directly to Retailer’s activity 10 InÕoice Customer graphically illustrates this modification. Invoicing under the optimized scenario takes place prior to activities 6 through 9 in the original scenario. This scenario constitutes the first of our proposed suite of scenarios for extended WfMS interoperability; the second scenario is described in Section 5.

The suggested optimization, however, requires a more sophisticated interaction model than any existing interoperability model. A key functionality of the required model is that the processes of cooperating business partners be at least partially visible to each other. This allows each cooperating business partner to modify its processes, including the initiation timing of all of its activities and all other external workflows for which it is responsible, in an optimal manner.

## 3. Monitored–nested interoperability model

A slight increase in conceptual complexity over simple nested processes confers considerable potential for flexibility and optimizability of WfMS Fig.Ž 4 . We call this new interoperability model the. monitored–nested model Ž . MNM ; in it the tasks of the calling activity have been expanded to include monitoring the state of the subprocess it has invoked, and the initiation of new process activity in its own workflow environment when a monitored subprocess state has been reached. Implementation of the activity initiation portion of the new model can be a simple Java-like event registration:

Ž .a the monitored state in workflow B is registered with B and as a precondition for a workflow activity in A

Ž . b on achievement of state, a message is sent from B to A

The simple nested model is a limited special case of the monitored–nested model in which the only condition monitored by workflow engine A is the end point of the task invoked by A in workflow engine B. The monitored–nested model is similar to the parallel-synchronized model in that the synchronization points of the parallel-synchronized model may be considered equivalent to monitored state communications. The models are different in that in the parallel-synchronized model workflow engine A is not responsible for initiating the workflow in workflow engine B. Moreover, synchronization communications do not explicitly initiate other workflow threads as state communications between workflows do in the monitored–nested model. Finally, in both of the nested models, activity in the workflow thread in engine A that initiated the external workflow suspends for the duration of the invoked activity whereas in the parallel-synchronized model activities proceed continuously in both workflows.

![](/api/attachments/DYVKWHSW/fulltext/images/ee6383629f22c2460581fb4d70051c14f48b6bb3a35403e2a7f15b2e8692ce45.jpg)  
Fig. 4. Monitored–nested interoperability model.

## 3.1. Use and benefits of MNM

According to information-processing-based organization theory 5 , certain forms of organizational<sup>w</sup> <sup>x</sup> structure or in this case, transaction structureŽ . emerge whenever multiple tasks involving uncertainty must be coordinated efficiently. A common name for one frequently observed such form is the contractor–subcontractor relationship in which a complex process is accomplished by multiple entities Ž . the subcontractors under the monitoring and supervision of an entity responsible for the overall result Ž . the contractor . This situation is ubiquitous in business; entire industries are currently based on the contractor–subcontractor relation, which is formally modeled by the MNM model. The construction industry is prototypical; different aspects of construction are handled by specialized subcontractors working under the supervision monitoring of a generalŽ . contractor. Airplanes, missiles, ships, large software systems and many other complex, assembled products are constructed using this coordination model.

The primary benefit of MNM type transactions over simple nested task interoperation is efficiency in the face of high natural and unavoidable variability in the completion times for the individual activities that comprise the workflow. By monitoring the status of activities, as the uncertainty of those activities becomes progressively lower, it is possible to continuously re-plan the overall process and optimize the result relative to simply waiting for each activity to complete.

An example of MNM type transactions in current business practice though established ‘manually’ is Ž . the much cited Wal-Mart WMŽ .<sup>r</sup>Proctor & Gamble Ž . P & G alliance. In this example, status information from WM’s normal inventory and procurement workflow is opened to its trading partner, P&G. P & G actively monitors sales information in WM’s system and this information triggers in P & G’s production and supply workflow the ordering, and actual restocking on WM’s shelves, of P&G products. The interaction is illustrated in Fig. 5.

## 3.2. Implementation problems and solutions

The problems involved in the actual implementation of workflow-based B2B e-commerce transactions and specifically MNM type transactions derive from the difficulty in coordinating WfMS from dif ferent manufacturers. Like many coordination problems, these are communications problems derived from differences in WfMS architectures, process models, communication protocols, and so on. In the workflow community all such problems fall under the heading of interoperability: the ability of heterogeneous WfMS to work together to monitor, coordinate and to some degree, control each other in working toward a common goal.

![](/api/attachments/DYVKWHSW/fulltext/images/263303a47595ea14cd1261b0b6cf449d5fd3ca293d62f97c4391e5652c0e8a1c.jpg)  
Fig. 5. MNM optimized trasaction: Procter & Gamble monitors Wal-Mart’s sales-tracking workflow.

Much recent research on workflow management systems from both universities and WfMS manufacturers has been focused on interoperability. This research has been quite successful and practical solutions have been found for many early interoperability problems. The problems that have been solved, those currently under research and those raised by the MNM interoperability model presented in this paper are best understood with reference to a protocol stack model see Fig. 6 . The model partitions inter-Ž . operability issues into levels of abstraction. At each level of the stack above the physical, incompatibilities at one level are overcome by meta-level information supplied by the next higher level.

Physical and communications level interoperability issues have been effectively solved by standardization on the WWW as the communications infrastructure and low level communications protocol set Ž . TCP<sup>r</sup>IP and HTTP . Early efforts at linking WfMS engines, the next higher level of abstraction in coordinating workflows, were directed at a standardized API’s for the engines. Many of these efforts were based initially on remote procedure call RPC syn-Ž . tax and later on CORBA and IIOP standards. However, these direct and closely coupled enactment engine links have been largely superseded by higher level XML based protocols—effectively, high level languages by which one WfMS may request services of another. Specifically, the interoperability problems introduced by different WfMS software architectures are overcome by Wf-XML, a high level protocol proposed for standardization by the WfMC.

However, Wf-XML assumes a single process definition is shared by coordinating agents. When this assumption is violated, that is, when processes change dynamically and autonomously, then interoperability problems arise at the level of process definition seeŽ Fig. 6 . Several solutions to interoperability prob- .

![](/api/attachments/DYVKWHSW/fulltext/images/da535f01137e5550ef0cf8d88f3d64a5ed4d3dca9d8414adce952ee678672fbd.jpg)  
Fig. 6. WfMS interoperability layers 19 . <sup>w</sup> <sup>x</sup>

lems at this level have been proposed 10,15,20 ,<sup>w</sup> <sup>x</sup> each aimed at solving a different portion of the broader issue. What all solutions implicitly share is the notion that the process definition language must be augmented with additional information to support dynamic modification. In our research, information on process intention is used to support robust MNM interoperability; MNM thus remains a research model, currently implemented only in our prototype, pending widespread adoption of a solution to the dynamic process change problem. However, the ubiquity of the model in manual commercial transactions argues strongly for its adoption into workflow enabled e-commerce once remaining implementation problems are solved. In the next section, the problem of dynamically changing processes is presented in detail to facilitate a discussion of our solution to the problem.

## 4. The dynamic process evolution problem

The monitored–nested interoperability model can easily support the desired transaction optimizations we have suggested for the order fulfillment example discussed above. Since all activities in subordinate workflows are visible to Retailer, sufficient information is available to optimize the overall process. There is, however, a significant practical problem with the deployment of the model or any model Ž dependent on process states : it is brittle under real . world conditions of dynamic process evolution. The logic to illustrate this is straightforward:

v The monitored–nested model depends on knowing the states of processes

v The state of a process in a WfMS is inevitably linked to specific activities

v But the processes being monitored take place outside the control of the monitoring agent and may change at any time

v And when an activity is changed, even to a simple equivalent activity, WfMS do not have sufficient information to link the monitored state Žwhat is important to the new activity..

Relative to our example, the Manufacturer and the Shipper are autonomous and may change suppliers and internal operations activities at any time for aŽ . variety of beneficial and necessary reasons. In Fig. 2, the optimization of early inÕoicing is dependent on Retailer receiving notice that shipment of the product has been scheduled. The completion of Schedule Shipping is effectively a high-level process state, which can be satisfied in any number of ways. In the specific workflow being used, however, the state is linked to the specific actiÕity Schedule UPS pickup. Now suppose that Regional Shippers RSI offers theŽ . Manufacturer a better price on shipping its goods. The specific activity in the workflow that indicates the state completion of<sup>w</sup> <sup>x</sup> Schedule Shipping now becomes Schedule RSI pickup. Due to the lack of knowledge about work processes inherent in most WfMS, this simple replacement of one activity by an equivalent is sufficient to confuse the monitoring on which the optimized process coordination depends— the state communication between workflow engines will never be sent. Of course, in the general case, the changes to a work process can be much more complex than the simple substitution of an activity.

The interrupted coordination will undoubtedly be brought to human notice eventually. Likewise, coordination can be reestablished through human intervention—specifically, by reprogramming the system to link the state achievement notification called aŽ trigger in WfMS terms to the new activity. How-. ever, the driving intention behind e-commerce is to automate transactions to the highest degree possible. A more ideal situation would be to incorporate into the WfMS the ability to:

1. link triggers to high-level states of the process

2. have the system recognize which activities correspond to achievement of the high-level states, even when activities are changed.

Naturally such automatic adjustment would be subject to human approval, but given a sufficiently high reliability for such a system, human intervention could be minimal and coordination-cost savings of the overall system significant. We have developed a technique for automating the re-coordination of activity-based process state notification under process change that makes use of goal meta-data about the process.

## 4.1. HOPI and goal based meta-data for processes

Conventional workflow management systems contain no information about their processes other than <sup>w</sup> <sup>x</sup> 11 :

v The activity

v The role actor type required to perform the activ-Ž . ity

v Resources needed to perform the activity

v Precedence information, frequently in the form of pre and post conditions for the activity

The monitored–nested model requires more information about the process than that shown in the above list since the activities may change at any time. The flexibility we seek for the monitored–nested model is enabled by meta-data, essentially data about data, which can be used by systems to reason about changes in the activities that constitute a work process. The more meta-data is available in standardized form such as XML descriptions for incorporationŽ . into inter-organizational information systems, the more sophisticated and efficient are the automated relationships that are practically realizable. From an information-theoretic perspective, meta-data and the sophisticated B2B relationships, it enables lower uncertainty in those relationships and thus permit a variety of cost-saving efficiencies.

Our research has shown that one type of information about processes, the goals of the process and its activities, when properly structured, allow inferences to be made about changed processes. Goal information permits these inferences because goals are far more stable than activities 9 . Our technique essen- <sup>w</sup> <sup>x</sup> tially attaches coordinating triggers to goals, which at some level remain constant even as activities to achieve the goal are dynamically changing. That is, the set of subgoals, functions, and activities originating from a goal are always recognizable as Athe same asB in some important sense, any other set of subgoals, functions and activities that also satisfy that goal 2 . It is precisely the ability of an inten-<sup>w</sup> <sup>x</sup> tional structure to change its instantiation while retaining the explanatory power of the higher-level nodes that gives our technique its utility.

A Hierarchical OÕerlay of Process Intention model Ž . HOPI is a tree structure of goals and subgoals intentions terminated by the activities that Ž . actualize the goals which are attached to generalized functions, as shown in Fig. 7. The general applicability of HOPI derives from its basis in the widely accepted decomposition model of problem solving activity 18 . With reference to Fig. 7, all processes<sup>w</sup> <sup>x</sup> begin as a high level intention to accomplish a complex multi-activity action. This intention is Ž . called the root goal in HOPI. The root goal is hierarchically decomposed during the design process into progressively less abstract sub-goals. The decomposition takes place recursively in a problem domain or problem space. At some point in a successful decomposition, the goals are sufficiently concrete that techniques for accomplishing the sub-goals can be assigned to them.

![](/api/attachments/DYVKWHSW/fulltext/images/974919f9e5017d79b7237ed0c27f6903600d1bdcdb09a9c42ef43110ca0c0fd0.jpg)  
Fig. 7. A hierarchical structure of intentions as an overlay of process representations.

The path from the root goal R to any activity inŽ . a work representation is termed the intentional context of the activity since tracing a path from activity to root goal explains the activity at progressively higher levels of abstraction. For example when we ask why the activity is performed, we explain that it is necessary to implement the generalized function to which it is attached. The reason for the enactment of the generalized function is the operationalization Ž . satisfaction of the sub-goal to which it is attached, and so on.

HOPI does not provide a process description or representation. Rather, HOPI captures additional information that can be used in conjunction with a process representation for reasoning about processes, and especially for drawing inferences about process changes. As such, it is general and applicable to any representation. Naturally HOPI and the coordination model based on it depend on the availability of intentional information. Today a strong case can be made from a review of the knowledge management literature that such information is being sought and captured for its considerable value even when it is not structured into a formalism such as HOPI 4 . At<sup>w</sup> <sup>x</sup> least one other workflow architecture has incorporated goal information into its process descriptions <sup>w</sup> <sup>x</sup> 13 . This system uses goals for dynamic re-planning of a workflow within a single organizational entity rather than for coordination of multiple workflows, but the increased functionality of that system supports the high utility of goal information about process.

Several other mechanisms are under research as potential solutions to the interoperability problems at the process definition level. These typically involve graph theoretic methods with formal logic, e.g. Petri nets, to infer the similarity of changed to original process models 15,20 . While each technique has its<sup>w</sup> <sup>x</sup> merits, we believe the hierarchical nature of HOPI is more flexible in the sense that more radically altered process descriptions can be recognized as AsimilarB using this scheme.

## 4.2. How it works

In a WfMS using HOPI, each workflow, described in virtually any format, is linked to its goal structure. The triggers that indicate the states of process that should be monitored are linked to specific activities and portions of the goal structure that indicate the meaning of the state see Fig. 8 . In anyŽ . process model, the process state must also be linked to a specific activity, since it is only by receiving confirmation that a concrete activity has been started or finished that the state can be observed. Within the HOPI conceptualization the completion of a set of activities linked to a goal is said to satisfy the goal and goal satisfaction takes the process to a new state. If a new altered process is substituted for the original process, providing the new process has a HOPI also, an intelligent subsystem can compare the two process descriptions and determine the new concrete activity to monitor to indicate achievement of a high level state.

![](/api/attachments/DYVKWHSW/fulltext/images/2b132858eb3902ef3a84956592cb6b5620ec7278df855056f7dedec98d3605ed.jpg)  
Fig. 8. Intentional specification of activity monitoring cf. Fig. 2 . Ž .

The HOPI inferencing algorithm 10 works by <sup>w</sup> <sup>x</sup> finding the best match in the new process goal tree to the path from the root goal to the original trigger activity in the original process. Fig. 8 shows the algorithm graphically as it relates to the order fulfillment scenario of Fig. 2. In both figures and the scenario, the activity that indicates the state of Completion of Schedule Shipping is the activity descended from that goal. Irrespective of how that activity changes, or even how many activities are required to satisfy the goal under different process implementations, an appropriate concrete activity to monitor to alert cooperating workflows of the achievement of state can always be located.

The Original Process of Fig. 8 corresponds to the Manufacturer’s workflow as both Manufacturer and Retailer understood it at one time say, Ž $t _ { 0 } )$ in their relationship. However, at some future time $\left( t _ { 1 } \right)$ the Manufacturer changes vendors Shippers and re-in- Ž . stantiates the actual activities of the workflow as shown in the Changed Process segment of Fig. 8. Without the HOPI interpreter, coordination between the Manufacturer and all business partners who depend on the specific activity Schedule UPS Pickup<sub>– –</sub> to trigger activities in their workflows is disrupted until all parties have been formally notified and their WfMS reprogrammed. This is a high cost modification. With HOPI, the change is detected, corrections made automatically, and human supervisory personnel notified of the change. Human high cost inter-Ž . vention required for process changes is, in many cases, limited to quickly assessing, and then accepting the modification suggested by the system.

## 5. Enabling more complex business relationships with monitored–nested workflows

From the ability to correct for minor coordination disruptions arising from dynamic process change Ž . via HOPI emerges the potential for more sophisticated e-business relationships than are now possible. Consider again the base order fulfillment scenario depicted in Fig. 2. Even greater time efficiencies than those that result from the optimization shown in Fig. 2 are possible if the Retailer serves as a coordinating contractor for both the Manufacturer and the Shipper. This changes the relationship between service providers entirely, as one WfMS is now the coordination nexus for multiple services. This type of coordinating relationship is frequently termed a contractor–subcontractor relationship and appears as the basic interaction model for business areas as old as the construction industry and as new as virtual corporations. The order fulfillment scenario reorganized under a contractor–subcontractor model is shown in Fig. 9.

Three of the many business reasons for adopting this arrangement are quality control, leverage with suppliers and single-source service delivery to the customer. We propose this as the second scenario in our suite of benchmark WfMS scenarios.

![](/api/attachments/DYVKWHSW/fulltext/images/abce3697c1978b503267d4e5e14374d490ea3c123d95b3be4a0b92854341b16e.jpg)  
Fig. 9. Order fulfillment via a contractor–subcontractor relationship.

The Retailer center column is now the instigat-Ž . ing force—the primary contractor—in control of the initiation of the sub-processes in Shipper and Manufacturer. With the ability to monitor the workflows of its subcontractors and preserve their autonomy Žthat is, monitor while not limiting their ability to modify their internal processes the Retailer can. orchestrate the entire multi-entity process. Scheduling of shipping has been taken over in this scenario by the Retailer who monitors the Manufacturer’s process to observe Schedule Production before activating its Schedule Shipping activity. Retailer then monitors the Shipper’s workflow to determine when the activity Schedule Van has been completed. This initiates the InÕoice Customer task in its own workflow. In proposing this scenario as an optimization, we make certain assumptions that may not be true in all business environments. However, the value of HOPI is its ability to allow any desirable interorganizational workflow to be put in place and then maintained at a relatively low cost under conditions of gradual autonomous process evolution.

## 5.1. LeÕeraging today’s online trading communities with HOPI

We discussed at the beginning of this paper how the recent development of online trading communities has been responsible for much of the increase in e-commerce. These same Internet sites can be easily leveraged to more sophisticated trading relationships using the techniques we have described as well as other meta-data enabled methods. The key technology underlying this capability is the nearly universal use of the meta-description language XML eXtensi-Ž ble Markup Language in these new trading commu-. nities 6 .<sup>w</sup> <sup>x</sup>

XML-izing HOPI is a simple matter of specifying a tree or more generally a directed-acyclic graph— Ž see Fig. 7 in XML. Fig. 10 shows a complete XML . document type definition DTD for HOPI, as it isŽ . implemented in our prototype. We believe the fundamental structure of HOPI and thus of the DTD is unlikely to change. However, as additional richness is added to the model, we can foresee attributes being added to each element specifying XML-LINKs —hypertext references—to lower level XML documents which give structure to each of the currently atomic nodes.

![](/api/attachments/DYVKWHSW/fulltext/images/ebca7c38ac74316dfe19a7048e297fe50b5593ebd76e5e494a4d398d505b80c4.jpg)  
Fig. 10. XML document type definition for HOPI.

A HOPI tree formally terminates in leaf nodes that represent activities. However, in what is termed a generic HOPI, branches may terminate at function or even subgoal nodes. The level to which the HOPI is defined reflects the level of constraint on the enactment of the root goal. An infinite number of generic HOPIs can be specified for each root goal reflecting the degree of delegation of the process that is acceptable—the greater the specification, the less delegation. A generic HOPI in turn may be expressed by an infinite number of activity sets that implement its goal set the intentional process speci-Ž fication . The implementing activity sets are called. instantiations of the HOPI, and in practical use a generic HOPI is linked to an instantiation expressed in any process description language.

XML product, form i.e. invoice, receipt , andŽ . process definitions already exist on multiple freely accessible trading sites 16 . In fact, the nature of<sup>w</sup> <sup>x</sup> these electronic marketplaces is to encourage public registration of and access to these descriptions. This is the mechanism by which accurate machine comparison of price and product data proceeds. Although the HOPI XML document type definition that allows it to function as a process description overlay is process definition dependent, only minor changes are required in the HOPI template to link lowest level goals to the activity descriptions of any XML process description. This type of maintenance is very economical given the benefits that result. XML parsers capable of turning any well-formed HOPI XML specification into the data structure to be utilized by our inferencing algorithms are widely available as subroutines or dll’s or subprograms forŽ . virtually any programming environment. The inferencing algorithm itself, though outside the scope of this paper, is also easily implemented 10 .<sup>w</sup> <sup>x</sup>

Once generic HOPI overlays have been published for a process, organizations can use their WfMS to enact optimized MNM transactions with suppliers and customers. In another paper we have described how HOPI goal trees are easily translated to XML messages within the Wf-XML standard protocol Žhttp:<sup>rr</sup>stunt.cis.gsu.edu<sup>r</sup>process coordination <sub>–</sub> <sup>r</sup> xml hopi.pdf . Wf-XML itself contains the message . <sub>–</sub> primitives necessary for one compliant workflow enactment engine to start and monitor processes in another engine.

Given that the WfMS which will interoperate are all Wf-XML aware, then a simple and efficient HOPI implementation would be as a wrapper layer surrounding the existing commercial workflow enactment engine. The subsystem<sup>r</sup>layer would operate at the level of Wf-XML messages and at that high level of operation, the impact on efficiency would be acceptable except in the most demanding applications. The HOPI layer would examine all incoming Wf-XML messages for HOPI content, and perform translations if required, much as Message Oriented Middleware MOM is used to provide data and Ž . message translation between heterogeneous legacy systems. Messages involving non-HOPI aware processes or workflow systems, or messages that did not involve HOPI computation would be passed through to the enactment engine unchanged. HOPI specific messages would be translated to the appropriate Ž . series of AstandardB Wf-XML messages and then passed through to or from the enactment engine. Ž . Fig. 11 illustrates this process.

With reference to Figs. 8 and 9, our technique resolves the changed activity situation presented in Section 4 and illustrated in Fig. 8 as follows:

v Retailer, working from a published XML description of Manufacturer’s workflow, augmented with a HOPI overlay, determines it can optimize its process by monitoring when Manufacturer schedules shipping.

v Retailer issues a Wf-XML request to Manufacturer to monitor advise when it has started theŽ . activity Schedule–UPS–Pickup. Part of this request references the work definition Retailer believes is in operation at Manufacturer.

v Manufacturer’s HOPI subsystem intercepts the activity-monitoring request. It compares the work definition transmitted from Retailer with Manufacturer’s current workflow definition in which the shipping activity has changed see Fig. 8 . The sub- Ž . system translates Retailer’s request so that the monitored activity is the new, equivalent activity—the first activity descended from the Schedule Shipping<sub>–</sub> subgoal.

v The subsystem then advises administrative personnel at both sites of the change it has detected and the suggested correction.

![](/api/attachments/DYVKWHSW/fulltext/images/cde68180314377615ff1669eb5ae6109c831d555e2f8bb0a96541b09d958e237.jpg)  
Fig. 11. HOPI processing implemented as a middleware service layer.

Though simple, this example illustrates both the flexibility that derives from the MNM model, and the robustness that HOPI structured intentional information adds to the technique.

## 6. Conclusion and implications for practice

Many of the problems and the potentialities of e-commerce are identical to those that have been under study for some time in the field of automated workflow management systems. As e-commerce evolves, the relationships between agents supported by the underlying technology must also evolve. In the workflow community, the study of relationships between autonomous workflows and the technology to model and enact them is termed interoperability modeling. We have shown that common interoperability models are not sufficient to realize more complex commercial relationships, which involve multiple parties and provide for considerable exception handling. The monitored–nested model of workflow interoperability we developed enables considerable flexibility and is sufficient for our proposed benchmark scenarios. Goal data about the processes, when structured in a hierarchy that reflects the design of the process, can be interpreted by a workflow subsystem to overcome some of the practical problems that attend sophisticated interoperability models.

The advent of multiple interoperable XML-based repositories on the Internet greatly extends the possibilities for augmenting basic inter-organizational workflow architectures with meta-data. Once research such as ours has established the type of information required to enable a rich business relationship, an XML description of that data can be posted to a globally accessible repository and downloaded by any trading partner. In many instances, similar to our technique for enabling contractor–subcontractor relationships with an overlay to conventional process descriptions, the additions to current systems can be made incrementally. A HOPI aware subsystem can be implemented as a middleware shell around any commercial WfMS which supports the Wf-XML standard. In the same way, new e-commerce potentialities can be explored and evaluated, and the support technology debugged without large investments or disruption to existing processes.

## Acknowledgements

This work is partially supported by NSF Research Grants, IIS-9810901 and IIS-9811248, and a research grant to the second author from the Robinson College of Business, Georgia State University.

## References

<sup>w</sup> <sup>x</sup> 1 Ariba Corporation, Ariba Commerce Center Architecture, commercial white-paper, http:<sup>rr</sup>www.Ariba.com<sup>r</sup>corp<sup>r</sup> AribaSolutions<sup>r</sup>ariba commerce center architecture.asp <sub>– – –</sub> Ž . 2000 .

<sup>w</sup> <sup>x</sup> 2 L. Barsalou, Ad hoc categories, Memory and Cognition 11 Ž .1983 211–217.

3 CommerceOne Corporation, Direct Materials E-Commerce via Multi-Enterprise Trading Exchanges, marketing whitepaper: http:<sup>rr</sup>www.commerceone.com<sup>r</sup> Ž . 2000 .

4 R. Dove, Knowledge management, response ability and the agile enterprise, Journal of Knowledge Management 3 1Ž . Ž .1999 54–61.

<sup>w</sup> <sup>x</sup> 5 J.R. Galbraith, Organization Design, Addison-Wesley, Reading, MA, 1977.

<sup>w</sup> <sup>x</sup> 6 R. Glushko, J. Tenenbaum, B. Meltzer, An XML framework for agent-based e-commerce, Communications of the ACM 42 3 1999 106–114.Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 i2 Corporation, Marketplace Services: Vision,marketing white paper: http:<sup>rr</sup>www.i2.com<sup>r</sup>marketplaces<sup>r</sup>vision.htm Ž .2000 .

<sup>w</sup> <sup>x</sup> 8 A.K. Jain, M. Aparicio, M. Singh, Agents for process coherence in virtual enterprises, Communications of the ACM 42 Ž . Ž . 3 1999 62–69, March.

<sup>w</sup> <sup>x</sup> 9 W.L. Johnson, M.S. Feather, D.R. Harris, Representation and presentation of requirements knowledge, IEEE Transactions on Software Engineering 18 10 1992 853–869.Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 W. Kuechler, V. Vaishnavi, A goal-based model of coordination in interoperating workflows, in: March, Bubenko Eds. ,Ž . Proceedings of WITS ’98, 1998, pp. 85–94.

<sup>w</sup> <sup>x</sup> 11 Y. Lei, M. Singh, A comparison of workflow metamodels, in: S.W. Liddle Ed. , Proceedings of the ER’97 Workshop Ž . on Behavioral Models and Design Transformations: Issues and Opportunities in Conceptual Modeling, 1997, http:<sup>rr</sup> osm7.cs.byu.edu<sup>r</sup>ER97<sup>r</sup>workshop4<sup>r</sup>ls.html.

<sup>w</sup> <sup>x</sup> 12 T. Lewis, Service: the next inflection point, IEEE Computer Ž . 2000 126–128, January.

<sup>w</sup> <sup>x</sup> 13 D.E. Mahling, R.C. King, A goal-based workflow system for multiagent task coordination, Journal of Organizational Computing and Electronic Commerce 9 1 1999 57–82.Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 C. Petrie, S. Sarin, Beyond documents: sharing work, IEEE Concurrency 7 3 2000 34–36, May–June. Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 M. Reichert, P. Dadam, A framework for dynamic changes in workflow management systems, Proceedings of the 8th International Workshop on Database and Expert Systems Applications, 1997, pp. 42–48.

<sup>w</sup> <sup>x</sup> 16 RosettaNet URL: http:<sup>rr</sup>www.rosettanet.org.

<sup>w</sup> <sup>x</sup> 17 A. Sheth, W. van der Alst, I. Arpinar, Processes driving the networked economy, IEEE Concurrency 7 3 1999 18–31,Ž . Ž . July–September.

<sup>w</sup> <sup>x</sup> 18 H.A. Simon, The New Science of Management Decision, Revised Edition, Prentice Hall, New York, 1977.

<sup>w</sup> <sup>x</sup> 19 S.L. Star, The structure of ill-structured solutions: boundary

objects and heterogenous distributed problem solving, in: L. Gasser, M.H. Huns Eds. , Distributed Artificial Intelligence, Ž . Morgan Kaufmann, San Mateo, 1989.

<sup>w</sup> <sup>x</sup> 20 W. van der Alst, Generic workflow models: how to handle dynamic change and capture management information, Proceedings of the 4th IECIS International Conference on Cooperative Information Systems, 1998, pp. 1–13.

<sup>w</sup> <sup>x</sup> 21 Workflow Management Coalition, Workflow Management Coalition Workflow Standard—Interoperability Abstract Specification, Document Number WFMC-TC-1012 1996Ž . www.wfmc.org.

<sup>w</sup> <sup>x</sup> 22 Workflow Management Coalition, Workflow Interoperability —Enabling E-Commerce April 1999 www.wfmc.org.Ž .
