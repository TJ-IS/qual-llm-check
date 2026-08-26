---
otero_id: 12884
otero_key: "C2KBS86N"
title: "Managing architectural emergence: A conceptual model and simulation"
authors: "David Dreyfus; Bala Iyer"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.05.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Managing architectural emergence: A conceptual model and simulation

David Dreyfus <sup>a</sup>, Bala Iyer <sup>b,</sup>⁎

<sup>a</sup> Boston University School of Management, 595 Commonwealth Ave, Boston, MA 02215, United States

<sup>b</sup> Babson College, TOIM Division, Babson Hall, Babson Park, MA 02457-0310, United States

## a r t i c l e i n f o

Article history: Received 13 October 2006 Received in revised form 7 May 2008 Accepted 26 May 2008 Available online 10 July 2008

Keywords: Architecture Information systems Networks Control points Simulation Conceptual mode Case study

## a b s t r a c t

Information systems are increasingly interconnected. They evolve through a sequence of projects that are affected by, and subsequently modify, this interconnectedness. We suggest that decision makers can in<sup>fl</sup>uence emergent information systems by closely managing only a subset of their applications. We de<sup>fi</sup>ne this set of applications as the architectural control point (ACPs).

To help architects manage their architecture, we develop a conceptual model of information system architecture as a network comprising a set of nodes linked by dependencies. We use simulation and network analysis to identify and show the value of ACPs.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Enterprise information systems are comprised of a portfolio of applications. Each application is a component of a larger system. The speci<sup>fi</sup>c pattern of interconnection among these applications comprises the information system architecture [11]. Prior research suggests that the architecture of the information system affects the bene<sup>fi</sup>ts it affords to the enterprise [3,12,13,18,24,28,42].

Research on architecture often follows a design-buildevaluate framework [3,14,42] and is largely normative. It promotes the value of architecture and suggests how architecting can be accomplished and communicated. The architect is assumed to have complete control over the architecture. Simultaneously, research on implemented information systems generally ignores the details of the information system architecture [12,13]. Many IT departments also ignore the interconnections among their applications while developing or procuring new applications.

The emergent information system architecture [17] – the pattern of interconnections among the deployed software components – is frequently the result of multiple, imperfectly coordinated decision makers operating over time. Individual decision makers frequently make local design decisions regarding infrastructure and application design, deployment, updating, upgrading, and decommissioning that have enterprise-wide rami<sup>fi</sup>cations. The result is path-dependent [21] information system evolution.

When applications are not integrated, IT managers allocate scarce development and maintenance resources based upon the stand-alone value of the application. They may perform a cost-bene<sup>fi</sup>t analysis, or they may respond to political or power considerations. However, when applications are integrated, how should scarce resources be allocated? To what extent should the pattern of integration among applications in<sup>fl</sup>uence resource allocation decisions?

In order to explore these questions, we conceptualize information system architecture as the pattern of interconnections among applications and build a simple simulation. Applications are represented by nodes, and interconnections among the applications are represented as edges. (Network terms are provided in Glossary.) The edges represent dependencies that in<sup>fl</sup>uence subsequent decision-making by

IT managers and other organizational actors [33]. We then simulate the deployment, modi<sup>fi</sup>cation, integration, and retirement of applications by adding and removing nodes and edges.

Using the simulation, we evaluate IT managers' ability to in<sup>fl</sup>uence the shape of an information system architecture by controlling a small set of nodes using a few architectural principles. We de<sup>fi</sup>ne the set of nodes that collectively provide the greatest in<sup>fl</sup>uence over the subsequent evolution of the information system as the system's architectural control points (ACPs). The simulated results suggest that as an information system evolves, the ability of a few applications to in<sup>fl</sup>uence that evolution degrades, but certain principles can reduce the loss of control. The results also suggest that preservation of certain architectural topologies can be best accomplished through increased attention to particular important applications — the architectural control points.

The rest of the paper is organized as follows. In Section 2 we develop the concepts of architectural evolution and architectural control points. In Section 3 we develop propositions regarding architectural control. In Section 4 we set up the simulation, run the simulation under varying conditions, and then discuss the results. We validate the simulation in Section 5 through a case study at a <sup>fi</sup>nancial services company. Finally, we conclude in Section 6 with a discussion of limitations and future work.

## 2. Architectural evolution and architectural control points (ACPs)

Previous studies suggest that an IS architecture includes a group of shared, tangible IT resources (e.g., hardware, software, data, training, management, etc.) that provide a foundation to enable present and future business applications [13,18,24,38]. Architecture, as implemented through its IT infrastructure, should be <sup>fl</sup>exible, reliable, robust, scalable, and adaptable [12,13,18]. It should support the reuse of business components within a <sup>fi</sup>rm, while bolstering <sup>fi</sup>rm responsiveness, innovativeness, and economies of scope [18].

As Zachman [42] suggests, there are many views and representations of architecture; each one is suited to a particular purpose. Iyer and Gottlieb [17] identify two views through which we can examine architecture. The <sup>fi</sup>rst view – the espoused – derives from designing the planned dependencies between system components and is the province of the IS Architect (although there may be many stakeholders). The second view – the emergent – results from implementing individual projects. This is a descriptive view of the actual dependencies that exist amongst system components.

Organizations with information systems can evaluate projects with the intent to understand how the project will impact the emergent architecture, or they can evaluate projects without this architectural perspective [1]. An organization can develop an architecture, implement it according to plan, and then have a series of subsequent IT projects that, in response to speci<sup>fi</sup>c or general business requirements, modify it. As a result, the emergent architecture may be signi<sup>fi</sup>cantly different from the espoused. Iyer and Gottlieb [17] argue that the way architecture emerges may subsequently impact how well the <sup>fi</sup>rm can achieve IT/ business strategy alignment as well as the goals of <sup>fl</sup>exibility reliability, robustness, scalability, adaptability, and reusability [27,35].

The emergent architecture can signi<sup>fi</sup>cantly affect IT and organizational performance. IT project cost, success, and performance are the result of an interaction between system and organization, which is in<sup>fl</sup>uenced by system architecture [20]. Project cost and maintenance is directly related to complexity [4,31], which is a description of interdependency.

The emergent architecture enables particular organizational capabilities and constrains others. The existence of certain information conduits implemented in the IS system in<sup>fl</sup>uences communication and routines [25] among organizational groups both syntactically and semantically [2]. The tasks that are allocated to speci<sup>fi</sup>c applications – the architecture – represent the actions and responsibilities of speci<sup>fi</sup>c users. Changes to the emergent architecture change the dependencies among them [20,33].

At its core, architecture in<sup>fl</sup>uences the design decisions and investment behavior of an organization. When viewed from this perspective, dependencies within an architecture act as conduits through which ideas, norms, and meaning <sup>fl</sup>ow. IS architects in<sup>fl</sup>uence both the emergent architecture and the host organization through IT project guidelines. The challenge for IT management is multi-fold. First, information systems are increasingly integrated. As one IT director said, “Six years ago…nothing was connected…everything is connected now. And the mentality…I don't think it's really caught up.”<sup>1</sup> Second, information systems tend to be subject to distributed, decentralized management. Individual business units have responsibility for their applications, but because the applications are interconnected, local decisions have global rami<sup>fi</sup>cations. Third, central IT management does not have the staff or other resources to actively manage all applications. As multiple IT directors have commented, they often learn of the existence of new applications when they fail and users call the help desk.

Given this reality and limited organizational resources, the IT department is necessarily paying more attention to some applications than to others. The focus of this paper is on the selection process IT management uses to determine which applications get their attention and which inter-application dependencies are created.

It is important to identify a subset of applications that architects can choose to control or more directly in<sup>fl</sup>uence. An application can be deemed valuable for two reasons. First, it can be intrinsically important because of its attributes or the stand-alone value it provides to the <sup>fi</sup>rm. For example, an accounting application may be important because it holds speci<sup>fi</sup>c data, performs critical tasks, represents large investments, or has a large number of users. Second, an application can be deemed important because of its position within a larger network of interdependent applications. Positionally important applications derive their status from their in<sup>fl</sup>uence on the emergence of the architecture, the ideas that <sup>fl</sup>ow through it, and the dependencies it creates and re<sup>fl</sup>ects. For example, a data mart may be important because it integrates and transforms data from multiple other applications [23,41].

The data mart requirements may in<sup>fl</sup>uence the upstream collection of data and the downstream evaluation and interpretation of that data. Having control of these applications may allow decision makers to in<sup>fl</sup>uence the evolution of the architecture to support the enterprise's business goals.

We introduce the term architectural control point (ACP) to refer to these positionally important nodes. An ACP is one component within a network that, due to its position therein, can potentially control the network to a greater extent than the network's other components. Such control can be used to in<sup>fl</sup>uence network evolution, value creation, and value appropriation.

It is important to note that the ACPs and intrinsically important applications are not necessarily the same. An ACP is important because it in<sup>fl</sup>uences the subsequent evolution of the information system. Applications with high stand-alone value are important but might not in<sup>fl</sup>uence information system evolution; however, applications with high stand-alone value might also become in<sup>fl</sup>uential if they are integrated with other applications to achieve positional importance.

Stand-alone value and positional value are complementary ideas. Some applications may have high stand-alone value and low positional value. For example, a clinical trial database may be extremely important to a pharmaceutical company even if that database is not integrated with any other application. Other applications may have low standalone value and high positional value. For example, a search engine's value derives from its connection to the other applications on the network — its positional value. Disconnected from other applications, it has little value. Windows has value due to its position in the software stack, not because of its stand-alone value [39]. Windows exerts control over the software ecosystem by being the integration point for layered applications. Although the Windows operating system has intrinsic value, its positional value enables control. Conversely, some applications have high stand-alone and high positional value. For example, database applications often have both high stand-alone value due to the data they store and high positional value due to the database's role as a data conduit among applications sharing the same data. An ACP can, in effect, become a gateway or bottleneck through which information <sup>fl</sup>ows.

ACPs can in<sup>fl</sup>uence subsequent network evolution whether or not they are actively managed. IT management can choose to ignore ACPs, actively manage existing ACPs, or manage non-positionally important nodes so that they become ACPs. A <sup>fi</sup>rm's management may be missing an opportunity to increase in<sup>fl</sup>uence over the emergent architecture when it ignores ACPs. They can also implement policies and make changes that leverage and increase the control afforded by the ACPs. Finally, they can make changes to non-positionally important nodes and increase other applications' dependency on these non-positionally important nodes, thereby increasing the nodes' positional importance so they become ACPs. As an example of a network operating at an industry level, one could argue that the managers of the Netscape Browser in the 1990s sought to increase the positional importance of their products within the software ecosystem at Microsoft's expense. Netscape sought to have application developers build on top of the browser instead of on top of the operating system. The expectation was that Netscape would manage the necessary interactions with the operating system. If Netscape had succeeded, it might have diminished Microsoft's ability to in<sup>fl</sup>uence the software ecosystem through its operating system. Perceiving this threat, Microsoft responded by bundling its own browser into the operating system, thereby preserving Microsoft's positional importance [10].

## 3. Architectural propositions

In the previous section we described ACPs as positionally important components that in<sup>fl</sup>uence the evolution of the information system. We suggested that managerial action can lead to the creation of new ACPs, the preservation of existing control points, or diminished control for some components. In this section we develop a set of propositions that concern the impact of system change on ACPs and the value of architectural thinking in creating, preserving, and enhancing them.

In order to develop the propositions, we need to de<sup>fi</sup>ne two new terms: architectural thinking and structured architecture. Architectural thinking is designing components to support multiple integrations while minimizing the constraints that such integrations may entail, and then encouraging other component owners to integrate their components with the focal component. Architectural thinking is designing for reuse [7,19]. It requires a clean separation between what the component does and how it does it [3], which leads to separation of interface from implementation.

Structured architectures are ones in which greater integration (coupling) exists within clusters of components than between them (see the right-hand network in Fig. 2 for an example) [30]. In a structured architecture of interconnected components, certain components may be designed to be more highly connected than others. These more highly connected components may be designed to be, in effect, ACPs.

Each component in the information system – including ACPs – has a set of stakeholders affected by that component. Over time, the impact of an ACP, and the durability of its in<sup>fl</sup>uence, depends upon the actions of each component's stakeholders. These actions include appropriating value, investing resources, educating consumers, marketing to new consumers, and designing improvements to the component and its integrations. At the component level, design activities include re-architecting, enhancing, and porting [3]. At the system level, they encompass whether integration with the focal component should be encouraged or not, and if so, through which APIs.

Components in<sup>fl</sup>uence others by the functionality they provide, the APIs used to access the functionality, and the complementary components that integrate with them. As the information system evolves through the addition and decommissioning of components and integrations among them, an ACP can grow or diminish in importance. As the information system grows, the absolute in<sup>fl</sup>uence of any one component on all others may diminish. Not all components will be similarly dependent on a particular set of functionality or APIs. As the information system grows, the relative importance of existing components may also change. If the interconnectedness among components is random – not subject to architectural thinking – there may be a reversion to the mean in which previously positionally unimportant components increase in importance and vice versa. This leads us to our <sup>fi</sup>rst proposition:

Proposition 1. Change to an architecture over time without architectural thinking results in reduced influence of positionally important components.

Architectural thinking involves designing components for easier integration, providing functionality that is useful to other components, and encouraging the reuse of such components. Architectural thinking involves designing architectural policies that encourage a speci<sup>fi</sup>c pattern of interconnectedness among the components rather than acquiescing to a random pattern. Although information system growth may diminish the absolute level of in<sup>fl</sup>uence on the information system of any one component, the relative importance of a component can be manipulated by managing the pattern of interconnectedness. This leads us to our second proposition:

Proposition 2. Architectural thinking reduces the decline in influence of positionally important components.

There is a tension between protecting important components from undue outside interference [32] and encouraging preferential attachment [5] so that other components link to the focal component. The logic of protecting core components is that increasing the number of components depending upon the focal, core component will increase the demands on the focal component. Modifying the focal component to support the varying requirements of other components leads to problems caused by diverse understandings of task requirements, which in turn are due to differences in world views [43]. Minimizing such integrations protects the conceptual integrity of the component.

The logic of encouraging attachment is that the owners and stakeholders of the attaching component become dependent on the focal component and adopt its data interpretation by using its data structures and task divisions, through use of this focal component's API. This dependency gives the focal component's owners both value appropriation opportunities and in<sup>fl</sup>uence over the future development and evolution of attaching components. Of course, a component with many attachments may be constrained in the changes that can be made to it, because its owners must be concerned with maintaining compatibility with the installed base.

Structured architectures attempt to balance the demands of protecting core components and encouraging reuse [14]. The connections on a few components are concentrated so that the constraints due to integration are minimized on other components. Architectural thinking, by considering the pattern of interconnectedness among components, will preserve structured architectures better than unconstrained integrations among components, and thus will reduce architectural drift [28]. In a service oriented architecture (SOA), architectural thinking will lead to the design of interface components and encouragement of their use. The components that implement the service will be less constrained, because components outside the domain will integrate with the interface component rather than the underlying implementation components. This leads us to our third, and <sup>fi</sup>nal, proposition:

Proposition 3. Architectural thinking minimizes changes to structured information system architectures.

## 4. Simulation model

We develop a simulation model to emphasize the concept of ACPs, explore the impact of architectural evolution on ACPs, and test the propositions presented in the last section. A simulation can test the implications of some of our basic assumptions [29]. In a simulation, we create an abstraction of an underlying reality – an information system – that is too complicated to evaluate directly. As in all abstractions, the simulation enables us to hide some details while focusing on the variables in which we are interested — the addition of components and connections. Simulation also enables us to manipulate those variables for which the means of doing so may be too impractical or too uneconomical through <sup>fi</sup>eld research methods, and to suggest areas for future qualitative and quantitative research.

In this paper we represent information system architecture as a network consisting of nodes and edges. A node represents a software component (i.e., an independent application, program, or executable unit of construction) [16]. An edge represents the data or processing dependencies between a pair of nodes. A simple network representation has the advantages of an existing body of tools, methods, and theory to support the visualization and analytics of the simulated architecture [6,9,36]. Network representations have a very simple grammar – nodes and edges – that hides the design process semantics of languages such as UML and allow us to focus only on the process of architectural evolution. Finally, network representations enable us to represent relationships between components and elevate those relationships to <sup>fi</sup>rst-class units of observation.

## 4.1. Nodes represent software components

Within our abstraction, we use a single node type, emphasizing the relationship between nodes and not speci<sup>fi</sup>c business functions, APIs, or tasks. We assume that all nodes have the same stand-alone value, are equally attractive reuse or integration candidates, and are added or dropped from the network independently of other nodes.

4.2. Edges represent data or processing dependencies between software components

An edge in our simulation represents a data or processing dependency between two nodes. Although there are many types of dependencies [22,32], we do not distinguish among them – all dependencies are represented by a single edge type. A data dependency exists between two nodes when node A depends on node B for data. Node B de<sup>fi</sup>nes the data structure and data semantics for node A. For example, when node A accesses node B's database, there is a data dependency between them. A processing dependency exists between two nodes when node A depends on node B for processing. For example, node A could depend on node B to process sales orders. In this case, node B de<sup>fi</sup>nes the semantics of a sales order and the business logic required to process it.

Dependencies are both direct and indirect. The examples above were of direct dependencies. However if there is a node C on which node B depends, then node A is indirectly dependent on node C. Node C indirectly in<sup>fl</sup>uences node A by in<sup>fl</sup>uencing B, which in tern in<sup>fl</sup>uences A. In this case, the in<sup>fl</sup>uence of C on A is mediated by B. We assume that the direct in<sup>fl</sup>uence of C on B is greater than the in<sup>fl</sup>uence of C on A, and that the in<sup>fl</sup>uence of B on A is greater than that of C on A. More generally, we assume that, all else being equal, the in<sup>fl</sup>uence of one node on another diminishes as the path length between them increases.

## 4.3. Projects change the architecture

Earlier we argued that IS architectures evolve through the implementation of IT projects. Based on the work of Baldwin and Clark [3], we simulate three basic project types: linking, augmenting, and splitting. While not a comprehensive list, we believe they represent the most common projects affecting the IS architecture. We validate this claim in the case study presented in the next section. A linking project integrates two existing components, an augmenting project augments the architecture by integrating a new component into the IS, and a splitting project splits an existing component into two more internally cohesive ones [30] and redistributes the integration points. We exclude those projects that join or delete existing components because we believe that these operations are rare in practice. We exclude projects that modify existing components and integrations but do not change the IS architecture because the focus of this paper is on the structural aspects of architecture. We exclude adding a node without an edge because our interest concerns only complex architectures in which components are interdependent.

The IT projects are simulated as atomic operations. In Fig. 1, a link operation adds an edge between nodes 2 and 3, increasing the edge count by 1. In Fig. 1, an augment operation adds node 6 to the base network and adds an edge between nodes 6 and 1, increasing the node and edge counts by 1 each. In Fig. 1, a split operation splits node 1, thereby creating node 6. In addition, an edge is created between nodes 1 and 6, and the 4 edges touching node 1 in the base case are redistributed between nodes 1 and 6 in the split case. The split operation increases the node and edge counts by 1 each.

The simulations are run under two sets of rules with two different starting conditions. The rules re<sup>fl</sup>ect the presence or absence of architectural thinking. In the <sup>fi</sup>rst set of rules, the position of the node in the network is ignored when evaluating the probability of an operation being permitted (i.e., no architectural thinking). In the second set of rules, the probability of an operation being permitted on a node is proportional to the normalized degree centrality of the node. (Here, the probability is d/N, where d is the number of edges adjacent to the node, and N is the total number of nodes in the network.) We characterize the use of degree centrality as a basis for operation approval by an organization as evidence for the presence of architectural thinking — resource sharing. In fact, sharing resources is considered a key dimension for evaluating the presence of architecture within <sup>fi</sup>rms [26].

The two starting conditions concern the shape of the espoused network (see Fig. 2): in one set of simulations the initial condition is a random network; in the other the initial condition is a small world network. These two starting conditions represent unstructured and structured architectures, respectively. When we have a small world starting condition, we assume that the <sup>fi</sup>rm has created domains of services or systems (say customer related or product related) that are highly connected with one another and loosely connected with other domains of systems. This style of architectural thinking is prevalent today in service oriented architectures (SOA) in general and Web Services in particular.

Both networks start with 48 nodes and 212 edges. (Approximately 20% of all possible edges among nodes exist in the networks.) The starting node and edge count is not important, except that to evaluate change to a network it should have a non-trivial node count; however, the networks are constructed to have the same node and edge count to facilitate subsequent analysis.

Network evolution progresses according to the following logic. At each simulation clock-tick, one of the three operations is chosen at random. (The probability that a particular operation is chosen varies across simulation runs.) It is then either accepted or rejected according to the acceptance criteria described below. The simulation is run until 100 sequential operations are performed on the network.

When a link operation is proposed, and the probability of approval is architecturally informed, the probability of approval is (d1+d2)/N, where d1 and d2 are the cardinality of edges adjacent to randomly selected nodes 1 and 2 respectively, and N is the total number of nodes in the network. When an augment operation is proposed and the probability of approval is architecturally informed, the probability of approval is d/N, where d is the cardinality of edges adjacent to a randomly selected target node. When a split operation is proposed, it is rejected out-of-hand if there are not more than two links adjacent to the randomly selected node. If this test is passed, the probability of approval is d/N. When operation approval isn't architecturally informed approval is guaranteed.

![](/api/attachments/C2KBS86N/fulltext/images/d3b7addd08847ee82aba9f60765e1fba12f36f6a5a8a89e6f1075db8b0818995.jpg)

![](/api/attachments/C2KBS86N/fulltext/images/2205d6f380d0abb79af458e448e4c12a5ef5f024d3bb2094d2b9edee405f9793.jpg)

![](/api/attachments/C2KBS86N/fulltext/images/bd01513ec54a07ed6f3a8ea4121bb59a2daad0d9be77dcb39a76608e89a6dde6.jpg)

![](/api/attachments/C2KBS86N/fulltext/images/f815ceea100f21a92633d93bae7f7495b4db685224cfa8ed434311845c4977d0.jpg)  
Fig, 1. Simulation operations, Linking adds an edge: augmenting adds a node and an edge: and splitting involves adding a node, redistributing existing edges, and adding an edge.

![](/api/attachments/C2KBS86N/fulltext/images/c1e7ec826d8910fcbc6da4c0b3461ddb6c67084203ddd37f0683b70930179b7a.jpg)  
Fig. 2. Networks before emergence. The random network is on the left; the small world network is on the right

## 4.3.1. Dependent variables

Broadly speaking, we are interested in two characteristics of the emergent architecture. First, how well the initially selected set of ACPs' in<sup>fl</sup>uence is preserved. This will help us evaluate Propositions 1 and 2. Second, how well the initial network topology is preserved. This will help us evaluate Proposition 3.

In the simulation, ACPs are those nodes that collectively have the shortest path lengths to all other nodes. We assume that one node's in<sup>fl</sup>uence on another node is proportional to the reciprocal distance between the two. Therefore, we assume that IT managers, in order to maximize in<sup>fl</sup>uence, will want to minimize the distance between the nodes they manage intensively and all other nodes. In terms of this simulation, we want to <sup>fi</sup>nd the ACP set that maximizes the sum of reciprocal distances.

To select the ACPs, and measure the in<sup>fl</sup>uence of the selection on the other nodes in the network, we make the simplifying assumption that in<sup>fl</sup>uence in the network travels along shortest paths, and then we calculate KeyPlayer metric KPP-POS [8]. The metric is computed by summing the reciprocals of the lengths of the shortest paths between each non-ACP node and the closest ACP node to it, and then dividing the sum by the number of non-ACP nodes. The initial set of ACP nodes is computed by searching for the set of N nodes (where N is the number of nodes allowed in the ACP set) that has the highest KPP-POS score. We measure preservation of in<sup>fl</sup>uence by comparing the KPP-POS score of the initially selected ACPs before and after each simulation run.

The measure of network topology preservation is created by comparing the starting and ending networks' Small World Quotients [34]. The Small World Quotient (SWQ) is a measure of the topographical characteristics of the network. The SWQ is a ratio of the network's small world measure (SW) to the SW of a random network with the same node and edge count. The SW measure is calculated as the network's cluster coef<sup>fi</sup>cient (NCC) divided by the network's average path length (APL) [37].

At the beginning of each simulation run, we determine the ACP sets of size 3 through 10. For each ACP set we calculate the KPP-POS metric at the beginning and end of the simulation run. The difference between the starting and ending KPP-POS measure represents the loss of architectural control. We also calculate the best KPP-POS metric obtainable with a new set of ACP nodes and the overlap between the new ACP set and the original set.

## 4.3.2. Summary of results

The simulation was run 10 times for each of the 2 starting networks (random and small world), 2 decision logics (random and architectural thinking), and 231 combinations of operation probabilities (each of link, augment, and split can vary between 0 and 100% in increments of 5 such that the sum of the probabilities equals 100) for a total of 9240 simulation runs. For each simulation run the number of ACPs varied between 3 and 10 in increments of 1. The resulting data set, therefore, consists of 8 rows for each simulation run, for a total of 73,920 rows. Each contains the variables in Table 1.

Table 1 consists of the descriptive statistics for the dependent and independent variables. Starting KPP-POS is the KPP-POS metric for the best initial set of ACPs in the network prior to the simulation run. Ending KPP-POS is the KPP-POS metric for the initial ACPs after 100 operations updated the network through the simulation. Best KPP-POS is the KPP-POS metric for the best set of ACPs in the network after the simulation ran. The number of ACPs in the best set is identical to the number of ACPs in the initial set. Init SWQ is the initial SWQ for the network prior to the simulation run. Ending SWQ is the SWQ for the network after the simulation run. Delta SWQ is the difference between the ending and initial SWQ (Ending SWQ−Init SWQ). ACP Overlap represents the number of ACPs in both the initial set of ACPs and the set of ACPs that produce the Best KPP-POS.

Dependent variable descriptive statistics

<table><tr><td>Variable</td><td>Mean</td><td>Std. dev.</td><td>Min</td><td>Max</td></tr><tr><td>Starting KPP-POS</td><td>.973</td><td>.05</td><td>.82</td><td>1</td></tr><tr><td>Ending KPP-POS</td><td>.649</td><td>.14</td><td>.11</td><td>1</td></tr><tr><td>Best KPP-POS</td><td>.745</td><td>.12</td><td>.37</td><td>1</td></tr><tr><td>Init SWQ</td><td>2.10</td><td>1.2</td><td>.67</td><td>3.31</td></tr><tr><td>Ending SWQ</td><td>1.97</td><td>1.2</td><td>.12</td><td>6.36</td></tr><tr><td>Delta SWQ</td><td>-.131</td><td>.76</td><td>-2.28</td><td>3.05</td></tr><tr><td>ACP Overlap</td><td>1.52</td><td>1.2</td><td>0</td><td>8</td></tr></table>

N=73,920.

Table 2 Regression

<table><tr><td>Ending KPP-POS</td><td>Coef.</td><td>Std. err.</td><td>t</td><td>Beta</td></tr><tr><td>Starting KPP-POS</td><td>.576</td><td>.00669</td><td>86.44</td><td>.190</td></tr><tr><td>ACP Count</td><td>.0172</td><td>.000130</td><td>131.83</td><td>.289</td></tr><tr><td>Small World Network</td><td>-.0119</td><td>.000376</td><td>-31.68</td><td>-.0437</td></tr><tr><td>Arch. Thinking</td><td>.0175</td><td>.000374</td><td>46.80</td><td>.0643</td></tr><tr><td>Link Prob.</td><td>.00256</td><td>.0000589</td><td>43.48</td><td>.475</td></tr><tr><td>Aug. Prob.</td><td>-.00125</td><td>.0000589</td><td>-21.17</td><td>-.232</td></tr><tr><td>Split Prob.</td><td>-.00217</td><td>.0000589</td><td>-36.82</td><td>-.403</td></tr></table>

No constant. N= 73,920. Adjusted R<sup>2</sup> = .99 and PN t is 0 for all coef<sup>fi</sup>cients.

## 4.3.3. Proposition support

Support for the propositions was tested by analyzing the data set with OLS regressions. The <sup>fi</sup>rst proposition is supported by the simulation — change to an architecture over time without architectural thinking results in reduced in<sup>fl</sup>uence of positionally important components. In general, the initial ACPs lost in<sup>fl</sup>uence: Starting KPP-POS is greater than Ending KPP-POS. Moreover, the ACPs with the most in<sup>fl</sup>uence in the changed architecture were generally not the original ACPs. In 175 simulation runs the initial ACPs gained in<sup>fl</sup>uence, while in 376 simulation runs Best KPP-POS was greater than Starting KPP-POS. To evaluate the importance of operation selection on changes in ACP in<sup>fl</sup>uence, we ran an OLS regression to predict Ending KPP-POS.

Table 2 presents the results of regressing Ending KPP-POS on Starting KPP-POS, the number of ACP nodes in the ACP set (ACP Count), whether the initial network was a small world network (Small World Network), whether the operation approval depends on a node's degree centrality (Arch. Thinking), the probability of a link operation (Link Prob.), the probability of an augment operation (Aug. Prob.), and the probability of a split operation (Split Prob.). The in<sup>fl</sup>uence of the initial ACPs has only a slight impact on the in<sup>fl</sup>uence of those ACPs after running 100 operations (beta=.190). Of much greater importance is the mix of approved operations. Operations that increase the number of edges relative to the number of nodes (i.e., the link operator) increase the in<sup>fl</sup>uence of the ACPs because they decrease the path lengths between the set of ACPs and the non-ACP nodes. Operations that increase the number of nodes relative to the number of edges (i.e., the augment and split operators) increase the path lengths between the ACPs and other nodes, thus decreasing the in<sup>fl</sup>uences of the ACPs (see Fig. 3).

Fig. 3 highlights the importance of operation selection on the changing information system. The initial condition for both networks is the small world network from Fig. 2. The left-hand network re<sup>fl</sup>ects 100 link operations; the righthand network re<sup>fl</sup>ects 100 augment operations. The best set of 5 ACPs after 100 operations are represented by squares. On average, for simulations represented by the network on the right with 5 ACPs, the initial KPP-POS measure dropped from 1 to .52. The selection of a new, optimal set of 5 ACPs resulted in a Best KPP-POS score of .58. The drop in in<sup>fl</sup>uence for the ACPs on the right is due to an increase in average path lengths.

The second proposition, that architectural thinking reduces the decline in in<sup>fl</sup>uence of positionally important components, is supported by the data presented in Table 2. The positive beta associated with Arch. Thinking suggests that a decision logic that favors reusing existing nodes improves the Ending KPP-POS metric. An improved ending value implies a reduction in the decline of the ACPs' KPP-POS metric. The impact of Arch. Thinking varies by operation type. When the regression from Table 2 is re-executed with the addition of interaction terms Arch. Thinking⁎Link Prob., Arch. Thinking⁎Aug. Prob., and Arch. Thinking⁎Split Prob., the betas are .0015, .19, and −.098 respectively. Adding edges between otherwise well connected nodes does not improve the KPP-POS metric much more than adding edges between less connected nodes. A policy that favors reuse of frequently reused nodes when adding a node has a signi<sup>fi</sup>cant impact on the KPP-POS metric. Splitting highly integrated nodes increases the deterioration in the KPP-POS metric because it increases average path lengths between nodes.

![](/api/attachments/C2KBS86N/fulltext/images/85cb66b52ffa41a24b15f82334d7b6fd0ce58ed90d469314c0adac7384c61609.jpg)  
Fig. 3. Small world networks after 100 operations. The best ACPs (5) represented by squares.

Table 3 Regression

<table><tr><td>Delta SWQ</td><td>Coef.</td><td>Std. err.</td><td>t</td><td>Beta</td></tr><tr><td>Aug. Prob.</td><td>.0190</td><td>.0000667</td><td>284.18</td><td>.496</td></tr><tr><td>Split Prob.</td><td>-.0139</td><td>.0000667</td><td>-208.32</td><td>-.364</td></tr><tr><td>Link Prob.</td><td>-.0148</td><td>.0000667</td><td>-221.79</td><td>-.387</td></tr><tr><td>Arch. Thinking * Aug. Prob.</td><td>.00196</td><td>.0000944</td><td>20.75</td><td>.0496</td></tr><tr><td>Arch. Thinking * Split Prob.</td><td>-.00632</td><td>.0000944</td><td>-66.99</td><td>-.160</td></tr><tr><td>Arch. Thinking * Link Prob.</td><td>.000860</td><td>.0000944</td><td>9.11</td><td>.0218</td></tr></table>

N=36,960. Adjusted R<sup>2</sup> =.90 and PNt is 0 for all coef<sup>fi</sup>cients.

The third proposition, that architectural thinking minimizes changes to structured information system architectures, is tested with an OLS regression of Delta SWQ on the operation probabilities and the interaction of those probabilities with Arch. Thinking for those cases where the starting condition was a small world network. (The results are shown in Table 3.) A positive Delta SWQ means that either that network's cluster coef<sup>fi</sup>cient (NCC) increased or that the network's average path length (APL) decreased. A negative Delta SWQ means the opposite.

In general, augment operations increase, and split and link operations decrease, the SWQ of an architecture. (See Table 3.) Architectural thinking in conjunction with augmentation further increases the SWQ (beta .0496), architectural thinking in conjunction with splitting increases the erosion in the SWQ metric (beta −.160), and architectural thinking in conjunction with linking partially offsets the decrease in the SWQ measure due to linking operations. Architectural thinking clearly impacts the shape of the emergent architecture; however, it is only in the case of linking operations that architectural thinking minimizes the changes that would otherwise have occurred to the SWQ.

Fig. 4 highlights the difference in the emergent architecture as a result of applying architectural thinking during the simulation run. The initial network is on the left, the network in the middle resulted from 100 augment operations without architectural thinking, the network on the right resulted from

100 augment operations with architectural thinking, and the squares represent the optimal ACPs in each network. The original architecture seems to be retained best with architectural thinking.

## 5. FinServ case study

To validate the basic assumptions in our simulation, we present a case study of a <sup>fi</sup>nancial services company, FinServ. FinServ provides processing services to the investment management industry; manages over a trillion dollars in assets; and provides global, full service, transfer agency and accounting services. The key assumptions in the simulation are that 1) IS architectures evolve over time, 2) operators we selected re<sup>fl</sup>ect a signi<sup>fi</sup>cant percentage of actual IT projects, 3) the simulated decision logic re<sup>fl</sup>ects real-world decision logic, 4) positionally important software components in<sup>fl</sup>uence subsequent changes to architecture through IT project implementation, 5) our network representation provides analytical utility, and 6) architectural in<sup>fl</sup>uence is proportional to network-based distance measures. Access consisted of six interviews with the chief architect and reviews of reports detailing their application portfolio and the dependencies among the constituent applications. In addition to our own primary data collection, we used details listed in [40] to inform our case study.

## 5.1. Architectural evolution

Over the last couple of decades, FinServ has grown rapidly, primarily through mergers and acquisitions but also by launching new services and entering new regions. As companies were acquired, each line-of-business (LOB) maintained much of the decision rights to control most aspects of their (line-of) business, including design, sales, back-end processing, and IT services. The resulting enterprise architecture has duplication of functionality, limited integration, and a wide variety of user interfaces. Each LOB was empowered to focus on, and independently respond to, speci<sup>fi</sup>c opportunities and needs.

The application procurement and deployment processes at FinServ represent the distributed, imperfectly coordinated activities that we earlier described as leading to architectural evolution. The resulting architecture at FinServ is an example of the emergent architecture over which architects have some in<sup>fl</sup>uence, but little control. The architecture re<sup>fl</sup>ects prior strategies (rapid growth) and constrains future choices.

![](/api/attachments/C2KBS86N/fulltext/images/982674462975de409177e7713bd4c1d06d4b2504886de59cf32bcd557d57e84a.jpg)  
Fig. 4. Small world networks after 100 operations. The best ACPs (5) represented by squares.

![](/api/attachments/C2KBS86N/fulltext/images/0aabb769a61ce64f13077cea144aab7c44bde8b65c97728c07435f2169b22420.jpg)  
Fig. 5. FinServ enterprise architecture (main component). 158 nodes.

Fig. 5 represents the emergent architecture at FinServ. We built this representation from the application portfolio and dependency reports mentioned earlier. The nodes in the <sup>fi</sup>gure represent applications, and the edges represent datasharing dependencies between them. As shown, FinServ's systems are not isolated: FinServ has 158 interconnected applications (nodes) in their enterprise architecture (network). It has a few highly integrated applications and many sparsely integrated applications.

The FinServ architecture had several characteristics that prevented the company from quickly responding to changing market conditions. These characteristics included tight coupling between applications, monolithic solutions (often not well documented), and the duplication of functionality (as noted above). This was sustainable during the economic growth phase of the 90s, but became a problem needing resolution.

In response to this predicament, FinServ hired a new CIO and created a new corporate initiative to address the problems. The IT organization was changed, creating an enterprise architecture team, an architecture review board, a management oversight committee, and an organization to provide companywide shared application services. A FinServ enterprise architecture strategy was created, and a Global Platform, SOA-based, enterprise architecture was de<sup>fi</sup>ned. These organizational elements can in<sup>fl</sup>uence the evolution of the information system by in<sup>fl</sup>uencing the various LOBs; however, they cannot replace the existing information system, mandate the use of particular products, or dictate a particular architecture.

## 5.2. IT project types

Our interviews validated the operations we used in the simulation model by showing that they are a reasonable division of the types of projects implemented at FinServ. The interviews identi<sup>fi</sup>ed the following operations that a project could implement:

1. Linking: Adding an integration between two existing applications to support new functionality. An example of this is the creation of a new report that requires access to previously un-accessed data.

2. Augmentation: Adding a new application because a line of business (LOB) has a new requirement. A FinServ example is the need to maintain a Sarbanes-Oxley requirement. The new project involves the building or buying of a new application and the creation of integration points with existing applications.

3. Splitting: Re-architecting an existing application. As a result of multiple integrations the functionality of the application increases beyond its original scope. It becomes too complex to support the diversity of integrations. At some point, the designers re-architect the application so that its components can evolve semi-independently. In practice, this situation seems to occur in at least three variations. In some cases applications (e.g., at FinServ, the legacy mainframe applications) are enhanced over time to a point where further enhancement becomes increasingly dif<sup>fi</sup>cult due to the interdependencies between functions. In a second set of cases, the re-architecting occurs because the company acquires another company with similar functionality, and the similar applications need to be rationalized. To merge the distinct functions and eliminate the duplicates, the original application may need to be split into constituent pieces. In a third set of cases, applications are cloned because the original application (e.g., a frontend application) is application-speci<sup>fi</sup>c (e.g., to a particular back-end application), yet its general functionality is desired across multiple applications. Cloning an application and then modifying it to support a new purpose may be quick in the short-run, but it doesn't scale and it imposes long-term maintenance costs. The collection of the set of clones can be considered a single application (until each clone diverges beyond recognition) that can be re-architected into a single, <sup>fl</sup>exible application in which the general functionality is maintained once and application-speci<sup>fi</sup>c functions are isolated.

4. Enhancements: Change an existing application (i.e., component or application) without creating new integrations. These projects generally extend the functionality of the existing application to meet new business needs or modify the application because an underlying application (e.g., Oracle) is upgraded.

Applications are sometimes retired and taken out of service. Generally, this happens in conjunction with the augmentation and re-architecting of existing applications and is properly accounted for in the splitting operation described above. In other cases, the retired application is replaced by another application but the general pattern of integrations between applications – the sharing of data between applications – is unchanged. In yet other cases, the retired application is eliminated because the supported business function is no longer performed, or the client no longer exists. This function is outside the scope of the simulation.

At FinServ, the rough breakdown of projects by resources used is 25% for linking, 25% for augmentation, 10% for splitting, and 40% for enhancements. These estimates are based on the chief architect's position as a project reviewer in the architecture review board. In our simulation, we ignore enhancements because they do not change the node/edge representation. However, to the extent that the architecture affects the cost and effectiveness of subsequent enhancements, it is signi<sup>fi</sup>cant that 40% of the <sup>fi</sup>rm's resources go towards enhancements. Scaling the remaining 60% of the resources that affect the enterprise architecture to 100%, the breakdown of operations is 42% linking, 42% augmentation, and 16% splitting.

## 5.3. Decision logic

In our simulation model, we adopted one of two types of decision logic that in<sup>fl</sup>uence project acceptance. Firms either execute projects without regard to the long-term impact of the project on system architecture, or they evaluate projects on both the short-term business objectives and the long-term architectural impact. The choice of decision logic is in<sup>fl</sup>uenced both by the costs of engaging architects for evaluation and the history and experience of the business leadership. This decision logic is validated by the FinServ experience:

At FinServ some of the leadership recognizes the importance of architectural thinking. Other elements of the leadership are focused on short-term objectives and the need to meet the immediate concerns of customers. Finally, the formative experiences of some of the leadership occurred at a time and place where applications were far less integrated. If the applications are isolated, thinking of them as such is perfectly appropriate.

The decision logic in the simulation that doesn't incorporate architectural thinking is evident at FinServ when a project is evaluated on its own merit, without regard to the impact on other applications or the evolution of the overall information system. The integrations between applications either supply valuable data or support important stakeholders. The speci<sup>fi</sup>c integrations do not affect project authorization.

The decision logic in the simulation that incorporates architectural thinking is evident at FinServ when a project is evaluated both on its own merit and on its impact on the future architecture of the information system. In particular, projects that link applications that are designed or intended for reuse are given preference. Sometimes this means the architects encourage additional integration with highly integrated applications. Other times the architects develop or acquire new applications that are designated as preferred applications to link to before they become highly linked (e.g., enterprise system bus components, data warehouses, or data marts).

## 5.4. Architectural control

A key assumption in this paper is that architects cannot actively manage all the applications in an enterprise. They, therefore, select a few and let the decentralized LOB managers handle the rest. Within FinServ there are about 150 IT projects per year, into 20% of which the architecture team has some visibility. The number of projects with which the architects get actively involved is limited by their staf<sup>fi</sup>ng level to 8. This validates the limited size of the ACP set in our simulation.

Architects select the applications they monitor based upon what they think is important. Another key assumption in this paper is that certain applications are valuable not because of their data or functionality, but because of their position in the network of applications within the enterprise.

This assumption is borne out by the following example. FinServ has three mainframe applications that feed data into a data warehouse. As the data are fed into the warehouse they are transformed. This leads to data quality issues due to conversion, completeness, and timeliness problems. The warehouse also feeds data to a data mart to provide ef<sup>fi</sup>cient reporting to a fourth tier of applications. The transfer from the warehouse to the data mart also involves data transformation and quality issues. Because the warehouse data is suspect, the data mart data is also suspect. Moreover, there aren't enough data marts. As a result, there is pressure from the LOB managers that use the DSS applications to bypass the data marts and warehouses and go directly to the mainframe data sources. However, this would severely strain the mainframes and limit subsequent modi<sup>fi</sup>cation of the mainframe applications due to the constraints imposed by dependent applications.

The warehouse has some stand-alone value due to its data processing and transforming capabilities, but its more signi<sup>fi</sup>cant value is in its position between the mainframe applications and downstream data consumers. By focusing on this positionally important application (i.e., the data warehouse) the architects can better preserve the architecture of the entire information system. Moreover, by controlling the data de<sup>fi</sup>nitions in the warehouse, the architects can in<sup>fl</sup>uence how the data is interpreted in downstream applications.

## 5.5. Network representation utility

The biggest challenge that FinServ's architects face, however, is not within their technical domain. Instead, the problem involves explaining to senior managers why IT is expensive, why failing to invest in architecture will become increasingly costly, and why outsourcing the support and provision of applications does not address the failure to invest in architecture. Outsourcing may affect where the application resides and who is responsible for its maintenance, but it does not affect the integration of that outsourced application with the other enterprise applications that either feed or require data. Only by staying on top of the applications that drive the number and complexity of the integrations between applications, can FinServ manage the cost, <sup>fl</sup>exibility, and risks in their evolving enterprise architecture.

The simulation emphasizes the emergent nature of the enterprise architecture and the need to adjust the <sup>fi</sup>rm's resources in response to changes in the architecture. As the case at FinServ highlights, the challenges are not strictly technical. The biggest challenges are communicating the nature of the information system, gaining the necessary resources, and identifying risks.

Applications with high positional value may be important because they in<sup>fl</sup>uence many other applications. They can also be important because they are outside the <sup>fi</sup>rm's control. At FinServ, this point is illustrated with two examples. Some of the applications with high positional value are 3rd party applications. This makes FinServ dependent on other companies' applications. At least one key application was developed twenty-plus years ago by two consultants, now in their sixties, who are still responsible for its maintenance. The application is undocumented. In both of these cases, FinServ has positionally important nodes effectively outside of its control. When these applications were either stand-alone applications or used by only one other application, the risks associated with these applications may have been low. However, as these applications became more embedded through direct and indirect integrations, their positional importance and associated risks increased.

## 5.6. Case summary

This brief case summary validates the core assumptions in this paper and the simulation. However, based on this single study, we cannot make more general claims about how closely this case applies to a broader population, the completeness of the types of IT projects that exist in practice, the ratio of different project types, the diverse types of decision logics used by decision makers, or the utility of the network representation.

## 6. Conclusions, limitations, and future work

This research builds on theoretical and empirical support for the proposition that the dependencies among software components are important conduits of in<sup>fl</sup>uence. This in<sup>fl</sup>uence can affect the relationships among the internal groups within an organization and the relationships between an organization and its external stakeholders. We've shown that under a set of simple assumptions certain components within an information system can exert greater in<sup>fl</sup>uence than other components. These components, the Architectural Control Points (ACPs), are in<sup>fl</sup>uential due to their positions within the information system. We've also shown that an IS project approval decision logic that takes into account the positions of components within the information system can in<sup>fl</sup>uence the subsequent evolution of the information system.

Our simulations support three propositions regarding the emergent nature of information systems. First, network growth results in a deterioration of the network in<sup>fl</sup>uence of an initial set of control points. Second, architectural thinking in the form of rules that guide emergence can reduce the degradation of in<sup>fl</sup>uence. Third, preferred designs are best maintained through architecturally informed rules that guide emergence.

The main managerial implication suggested by the simulations is that a sequence of IS projects can have a radical impact on an information system's architecture. Therefore, architects and other decision makers might derive value from actively monitoring their information system architecture. IS architecture is not something that can be designed once and forgotten. A second implication follows from the <sup>fi</sup>rst: individual projects might be more pro<sup>fi</sup>tably evaluated in terms of their stand-alone value, their position within the overall information system, and their impact on the information system architecture. A third implication is that the set of important components within an information system changes over time due to variance both in the relative stand-alone value and in the relative position of each component within the overall architecture. As a result, architects unable to focus their attention on all the components in their information system might consider adjusting the components to which they devote resources as the architecture changes.

As part of the simulation we made some contributions to the IS literature. First, we introduced the representation of an information system architecture as a simple network abstraction in which software components are represented by nodes and dependencies between them are represented by links or edges. Such an abstraction has the advantage of providing a useful visualization, scaling well as the architecture grows, supporting multiple levels of granularity, and being subject to network analysis methods. We also introduced, as a method for identifying potentially important software components, the use of the Key Player metrics into the analysis of IS architectures. These metrics extend the network analytics that focus on single nodes to incorporate sets of nodes. Finally, we introduced the use of simulated network evolution in order to evaluate the impact of different types of projects and project acceptance logics.

According to the chief architect at FinServ, the conceptual model, network visualization, and associated simulation is “a powerful communication tool to gain the support of people to do the right thing.” The big issue is being able to visualize what is happening to the architecture and then to show others without “wading through reams of spreadsheet data…. Communications with decision makers and stakeholders at a senior level is notoriously dif<sup>fi</sup>cult. They live in an old world where things were not complicated.” The decision makers take an attitude that “IT is dif<sup>fi</sup>cult. So, I will buy it from outside. There is still very much the silo model.”<sup>2</sup>

From FinServ's perspective, the simulation would serve them better if it were further calibrated with speci<sup>fi</sup>c project costs and application performance metrics to better illuminate the effect of architectural control on cost, application stability, and application ef<sup>fi</sup>ciencies. As the chief architect stated, “Everyone wants to reinvent the wheel. We need metrics for the cost of adding applications, transforming data, and moving data. People want to know when the architecture will be <sup>fi</sup>nished. The architecture is done only when the business is closed. Architecting is a process that maintains some level of control over the architecture and produces better outcomes for the organization than would occur in its absence.”

This simulation highlights the effect of system evolution on the changing importance of positionally important applications. Adhering to a preference for application reusability can limit the speed with which the list of important applications changes, but it can't halt change. The simulation serves to highlight the implications of certain assumptions; it doesn't represent the full complexity of information system architectures, the processes by which they evolve, or the intentional activities of organizational actors that change the architecture.

Project approval processes in practice will necessarily be more complex and nuanced than the one used in the simulation [15]. The in<sup>fl</sup>uence of one component on another is a function of many more attributes than a network measure. Whereas in our simulation we treated all components as having equivalent stand-alone value, in practice this is not the case.

Subsequent extensions to this work include additional simulations, empirical tests, and the incorporation of decision rights, power, and politics into the general framework. Subsequent simulations can explore the impact of different and more nuanced assumptions. Empirical examinations can tie system evolution and architectural guidance to speci<sup>fi</sup>c business and IS outcomes. We anticipate showing in subsequent research that the position of software components within the overall information system architecture can also impact their maintenance costs, IS project predictability, and perceptual measures of their application quality.

Decision rights, power, and politics seem to be an integral part of information system architectures. We focused our attention on the emergent view of architecture because the emergent architecture seems both to re<sup>fl</sup>ect past interorganizational interdependencies and to in<sup>fl</sup>uence future ones. The impact of one component on another, in practice, may also re<sup>fl</sup>ect the decision rights conferred on the owners of those components. In<sup>fl</sup>uence is not just a result of speci<sup>fi</sup>c technologies and design choices; it is also a result of the components' owners' ability to appropriate value, control access, and negotiate change. The ACPs occupy key positions in a network and, more importantly, confer unique decision rights on their owners. It is, in part, through these decision rights and this relative bargaining power that organizational actors in<sup>fl</sup>uence each other.

## Acknowledgements

The authors thank the anonymous reviewers for their comments and guidance, which have signi<sup>fi</sup>cantly improved the quality of the manuscript. Boston University School of Management's Institute for Leading in a Dynamic Economy (BUILDE) provided research support for the study. The interpretations, conclusions, and errors are our own.

## References

[1] C. Alexander, Notes on the Synthesis of Form, Harvard University Press, Cambridge, MA, 1964

[2] N.S. Argyres, Technology Strategy, Governance Structure and Interdivisional Coordination, Journal of Economic Behavior and Organization 28 (1995).

[3] C.Y. Baldwin, K.B. Clark, Design Rules: The Power of Modularity, MIT Press, Cambridge, MA, 2000.

[4] R.D. Banker, et al., Software Complexity and Maintenance Costs, Communications of the ACM 36 (11) (1993)

[5] A.-L. Barabasi, Linked: The New Science of Networks, Perseus Publishing, Cambridge, MA, 2002.

[6] V. Batagelj, A. Mrvar, Pajek, 1996

[7] B. Boehm, Managing Software Productivity and Reuse, Computer 32 (9) (1999).

[8] S.P. Borgatti, in: R.L. Breiger, et al., (Eds.), The Key Player Problem, in Dynamic Social Network Modeling and Analysis: Workshop Summary and Papers, National Academy of Sciences Press, Washington, D.C., 2003.

[9] S.P. Borgatti, M.G. Everett, L.C. Freeman, Ucinet for Windows: Software for Social Network Analysis, Analytic Technologies, Harvard, MA, 2002.

[10] T.F. Bresnahan, S. Greenstein, Technological Competition and the Structure of the Computer Industry, Journal of Industrial Economics 47 (1) (1999).

[11] F.P. Brooks, The Mythical Man-Month: Essays on Software Engineering, Addison-Wesley Pub. Co., Reading, Mass., 1975.

[12] T.A. Byrd, D.E. Turner, Measuring the <sup>fl</sup>exibility of information technology infrastructure: exploratory analysis of a construct, Journal of Management Information Systems 17 (1) (2000).

[13] N.B. Duncan, Capturing <sup>fl</sup>exibility of information technology infrastructure: a study of resource characteristics and their measure, Journal of Management Information Systems 12 (2) (1995).

[14] M. Fowler, Patterns of Enterprise Application Architecture, Addison-Weslev, Boston. 2003

[15] F. Ghasemzadeh, N.P. Archer, Project Portfolio Selection through Decision Support, Decision Support Systems 29 (1) (2000).

[16] J. Hopkins, Component Primer, Communications of the ACM 43 (10) (2000).

[17] B. Iyer, R.M. Gottlieb, The four-domain architecture: an approach to support enterprise architecture design, IBM Systems Journal 43 (3) (2004).

[18] T.R. Kayworth, D. Chatterjee, V. Sambamurthy, Theoretical justi<sup>fi</sup>catio for IT infrastructure investments, Information Resources Management Journal 14 (3) (2001).

[19] C.W. Krueger, Software reuse, ACM Computing Surveys 24 (2) (1992).

[20] R. Leifer, Matching computer-based information systems with organi zational structures, MIS Quarterly 12 (1) (1988).

[21] S.J. Liebowitz, S.E. Margolis, Path dependence, lock-in, and history, Journal of Law, Economics, and Organization 11 (1) (1995).

[22] T.W. Malone, K. Crowston, The interdisciplinary study of coordination, ACM Computing Surveys 26 (1) (1994).

[23] S.T. March, A.R. Hevner, Integrated decision support systems: a data warehousing perspective, Decision Support Systems 43 (3) (2007).

[24] D. McKay, D. Brockway, Building IT Infrastructure for the 1990s, Stage by Stage 9 (3) (1989).

[25] R. Nelson, S. Winter, An Evolutionary Theory of Economic Change, Harvard University Press, Cambridge (MA), 1982.

[26] D.L. Parnas, On the criteria to be used in decomposing systems into modules, Communications of the ACM 15 (12) (1972).

[28] D.E. Perry, A.L. Wolf, Foundations for the Study of Software Architecture, ACM SIGSOFT Software Engineering Notes 17 (4) (1992)

[29] H.A. Simon, The Sciences of the Arti<sup>fi</sup>cial, 3rd ed.The MIT Press, Cambridge, MA, 1996.

[31] D.P. Tegarden, S.D. Sheetz, D.E. Monarchi, A software complexity mode of object-oriented systems, Decision Support Systems 13 (3–4) (1995).

[32] J.D. Thompson, Organizations in Action: Social Science Bases of Administrative Theory, McGraw-Hill, New York, 1967.

[33] J. Tillquist, J.L. King, C. Woo, A representational scheme for analyzing information technology and organizational dependency, MIS Quarterly 26 (2) (2002).

[34] D.J. Watts, Small Worlds: The Dynamics of Networks between Order and Randomness, Princeton University Press, Princeton, N.J., 1999.

[35] R.Y. Wang, D.M. Strong, Beyond accuracy: what data quality means to data consumers, Journal of Management Information Systems 12 (4 (1996).

[36] S. Wasserman, K. Faust, Social Network Analysis: Methods and Applications, Cambridge University Press, Cambridge, 1994.

[37] D.J. Watts, Networks, dynamics, and the small-world phenomenon, American Journal of Sociology 105 (2) (1999).

[38] P. Weill, M. Broadbent, Leveraging the New Infrastructure: How Market Leaders Capitalize on Information Technology, Harvard Business Schoo Press, Boston, 1998.

[39] G. Westerman, R. Walpole, PFPC: building an IT risk management competency, CISR Working Paper, 2005.

[40] J. West, J. Dedrick, Innovation and control in standards architectures: the rise and fall of Japan's PC-98, Information Systems Research 11 (2) (2000).

[41] B.H. Wixom. H.I. Watson, An empirical investigation of the factors affecting data warehousing success, MIS Quarterly 25 (1) (2001).

[42] J.A. Zachman, A framework for information systems architecture, IBM Systems Journal 26 (3) (1987).

[43] R.W. Zmud, Management of large software development efforts, MIS Quarterly 4 (2) (1980).

## Glossary

APL: The Average Path Length (APL) for a network is the average length of the shortest path between each pair of nodes in the network

CC: The Cluster Coef<sup>fi</sup>cient (CC) of a node is the number of edges among the neighbors of that node divided by the maximum possible number of edges.

Edge count: Edges are bidirectional links between pairs of nodes. The edge count is the number of such edges in the network.

KPP-POS: A metric representing the closeness of a set of nodes – the Key Player (KP) nodes – to the other nodes in the network. The metric is computed by summing the reciprocals of the length of the shortest path between each non-KP node and the KP node with the shortest path to it, and then dividing the sum by the number of non-KP nodes.

NCC: The Network Cluster Coef<sup>fi</sup>cient (NCC) is the mean of the cluster coef<sup>fi</sup>cients for each node in the network.

Neighbors: Nodes connected to a focal node by a single edge. Path: A path is an alternating sequence of nodes and edges

that begins on a node and ends on a node in which sequential nodes in the path are connected by an edge in the path and in which no node or edge in the path is touched more than once.

Node count: The number of nodes in the network.

Path length: The number of edges in the path.

Shortest path: The path between two nodes that has the fewest edges. There may be multiple shortest paths between two nodes.

SWQ: The Small World Quotient (SWQ) is a ratio of the network's small world measure (SW) to the SW of a random network with the same node and edge count. The SW measure is calculated as the network's cluster coef<sup>fi</sup>cient (NCC) divided by the network's average path length (APL).

David Dreyfus is completing his doctoral dissertation at the Information Systems Department at Boston University's School of Management. He holds a Master's degree in Business and a Bachelor's degree in Arts, with a concentration in Computer Science, from the University of California, Berkeley, California. Prior to his doctoral studies he worked in the database management and document publishing sectors of the software industry in multiple capacities for over 20 years. His research interests include the impact of information and information system complexity in organizational settings, software complexity measurement, and network analysis. His dissertation explores the relationship between information system architecture and information system <sup>fl</sup>exibility, as well as issues related to the measurement and visualization of information systems. He has published multiple papers in the proceedings of the International Conference on Information Systems and the Hawaii International Conference of Systems Sciences.

Bala Iyer is an associate professor in the Technology, Operations, and Information Management Division at Babson College. Professor Iyer received his Ph.D. from New York University with a minor in computer science. His research interests include exploring the role of IT architectures in delivering business capabilities, designing knowledge management systems using concepts from systems design, hypertext design and work<sup>fl</sup>ow management, querying complex dynamic systems, hypermedia design and development and model management systems. Over the last several years, he has been analyzing the software industry to understand the logic and patterns of emergence of architecture and platforms. Recently, he has been visiting and observing companies in Indian IT services industry to understand their core capabilities and how we can learn from them.

He has published papers in JMIS, California Management Review, Harvard Business Review, CACM, CAIS, Decision Support Systems, Annals of Operations Research, Journal of the Operational Research Society, International conference on Information Systems and in several proceedings of the Hawaii International Conference of Systems Sciences.
