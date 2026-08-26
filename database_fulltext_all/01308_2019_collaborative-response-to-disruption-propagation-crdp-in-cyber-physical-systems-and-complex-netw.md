---
otero_id: 1308
otero_key: "SAJ2AQVK"
title: "Collaborative response to disruption propagation (CRDP) in cyber-physical systems and complex networks"
authors: "Win P.V. Nguyen; Shimon Y. Nof"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.11.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
<table><tr><td>PII:</td><td>S0167-9236(18)30196-9</td></tr><tr><td>DOI:</td><td>https://doi.org/10.1016/j.dss.2018.11.005</td></tr><tr><td>Reference:</td><td>DECSUP 13013</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>20 August 2018</td></tr><tr><td>Revised date:</td><td>17 November 2018</td></tr><tr><td>Accepted date:</td><td>29 November 2018</td></tr></table>

## Accepted Manuscript

Collaborative response to disruption propagation (CRDP) in cyber-physical systems and complex networks

Win P.V. Nguyen, Shimon Y. Nof

![](/api/attachments/SAJ2AQVK/fulltext/images/1ad54a049fd156e2f55c5b83476e7b98e2cbf794a39df9c04277a725476c756e.jpg)

Please cite this article as: Win P.V. Nguyen, Shimon Y. Nof , Collaborative response to disruption propagation (CRDP) in cyber-physical systems and complex networks. Decsup (2018), https://doi.org/10.1016/j.dss.2018.11.005

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Collaborative Response to Disruption Propagation (CRDP) in Cyber-physical Systems and Complex Networks

Authors:

Win P. V. Nguyen, PRISM Center and School of Industrial Engineering, Purdue University

Shimon Y. Nof, PRISM Center and School of Industrial Engineering, Purdue University

## Abstract

Disruptive events, such as natural disasters and manmade coordinated attacks, have inspired greater interests in the concept of disruption propagation and disruption response in cyber-physical systems (CPSs) and complex networks. Due to the high interconnectedness and complex interactions within and between CPSs, disruptions are not isolated events, and can propagate with severe impacts both locally and remotely, and must be contained lest catastrophic and irreversible damages occur. Responding agents are often employed to tackle the disruptions, and the agents’ effectiveness becomes a critical concern, which is addressed in this article. Although the phenomenon of disruption propagation in CPSs and complex networks is becoming better understood, the interactions between the responding agents and the disruption propagation have not yet been investigated and studied in detail. In this work, the Collaborative Response of Disruption Propagation (CRDP) model is introduced as a general approach to the network disruption propagation problem. The CRDP model captures the important components of the problem: The client network, the agent network, the disruptions, and their interactions. Three system awareness analytics and two novel online scheduling protocols have been developed based on the analysis of the interactions. The analytics and protocols seek to provide insights into the system’s conditions, and guide the response agents and their management to contain and eliminate the disruption propagation. The CRDP model, together with its developed analytics and protocols, can be applied to different network types,

different disruption scenarios, and different response mechanisms available due to the generality of the model.

Keywords: cyber-physical systems, complex networks, collaborative response, disruption propagation, disruption response mechanism.

Note about the use of color for figures in print: no.

## 1. Introduction

## 1.1. Motivations for this work

Disruptive events during recent decades have inspired greater interest in the concept of disruption and disruption response in cyber-physical systems (CPSs) and complex networks: networks of supply, manufacturing, computers, transportation, utility and other infrastructure (Crucitti, Latora, & Marchiori, 2004). Due to the complex interactions and interdependencies of a CPS, disruptions can propagate to multiple parts of a CPS, affecting the performance and viability of the components of the entire system. In computer networks and sensor networks, malware can spread to connected nodes, compromising the performance of a system and possibly forcing an entire system to shut down (Snediker, Murray, & Matisziw, 2008; Kim, Chen, & Linderman, 2015; Liu et al., 2016). Computer networks and social networks are observed to be scale-free, which means the characteristic path lengths of the networks are relatively short. It can enable the disruptions and malware to propagate quickly from one end of the network to another (Albert & Barabasi, 2002; Liu et al., 2016). The propagation of disruptions is also relevant to advanced supply networks and manufacturing networks, where disruptions can negatively affect preceding and succeeding nodes, due to unfulfilled demands and/or supplies. Externally, natural disasters and security issues can disrupt production of certain raw materials and intermediate production steps; damage or destroy infrastructure, which can negatively impact manufacturing processes and product quality (Day, 2014; Gong, Mitchell, Krishnamurthy, & Wallace, 2014). Internally, supply networks and manufacturing networks are subjected to disruption by uncertainties, human errors, and by equipment and machinery breakdowns (Sajadi, Esfahani, & Sorensen, 2011).

While the increasing connectivity of CPSs and complex networks enables greater levels of quality of service and customization, it also brings about the important challenges of ensuring security, resilience, and providing effective response against disruptions (Snediker et al., 2008). In these cases, effective decision-making of response to disruption propagation is particularly important due to the involvement of advanced, flexible manufacturing equipment and complex machines that are controlled and augmented by

# ACCEPTED MANUSCRIPT

cyber. The impacts of disruptions can be devastating. Supply disruptions in supply networks can lead to raw materials and intermediate components shortage, resulting in severe revenue losses for enterprises. Cyber-attacks on computer networks and information networks can lead to the immediate compromises of sensitive information and service denials, as well as the long-term equipment damage, loss of customer’s trust and strategic advantages. Therefore, response activities are generally managed by human operators and managers. This approach, however, is largely hampered by the size and complexity of the CPSs and complex networks involved. Thus, cyber-augmented decision-making and decision support systems are necessary to effectively coordinate response activities (Snediker et al., 2008) to overcome the disruption propagation.

A literature survey reveals significant interest and progress with respect to disruptions in CPSs and complex networks disruption propagation and cascading failures, and research questions of disruption propagation modeling in different network types. These developments enable the capabilities of predicting and assessing the impacts of disruption propagation on CPSs and complex networks. In many applications, however, the mere presence of response mechanisms to disruption already affects the propagation of the disruptions, and therefore, limits the applicability of the aforementioned methodologies. Examples include firemen vs. fire spreading; countermeasures vs malware propagation; quarantine vs disease spreading. Understanding and utilizing these interactions between responses and disruption propagation in decision-making can significantly improve recovery probability and recovery time of CPSs facing disruption propagation. In a highly connected and interdependent CPSs, disruption propagation not only further damages the CPS, it also increases the information processing workload, decision-making workload, and response workload. Therefore, effective decision-making and response strategies are required to limit the propagation of disruption. The literature survey also reveals a large variety of network types, disruption propagation mechanisms, response mechanisms, and response strategies. This necessitates a general modeling and decision-making approach to organizing and managing response activities against disruption propagation (Qiu, Wang, Ye, Liu, & Dong, 2014; Kumar, Gupta, & Bhasker, 2017).

# ACCEPTED MANUSCRIPT

## 1.2. The CRDP model

In this work, the Collaborative Response of Disruption Propagation (CRDP) model, which is one original contribution, is introduced and formulated to illustrate the effects of disruption propagation and response to disruption on a CPS, modeled as a weighted and directed complex network. The CRDP model provides a general modeling approach to the network disruption propagation response problem. The second contribution is the introduction of three system awareness analytics (SAA) and two novel online scheduling protocols (OSP) that can be adapted for similar applications. The CRDP model is inspired by the SmaRTA project at Purdue’s PRISM Center. SmaRTA stands for Smart Response-Task Allocation. SmaRTA has so far delivered the Dynamic Lines of Collaboration model (DLOC) and the Teamwork Integration Evaluation/Dynamic Lines of Collaboration (TIE/DLOC) simulator (Nof, 2013a, 2013b; Zhong, Nof, & Filip, 2014; Zhong & Nof, 2015; Zhong, 2016). The CRDP model is also developed based on the principle of emergent lines of collaboration and command (ELOCC) as specified by the Collaborative Control Theory (Nof, 2007; Nof, Ceroni, Jeong, & Moghaddam, 2015), and augments the ELOCC principle. The decision support aspects of CRDP are inspired by the Purdue’s PRISM Center’s works on emergency response and error/conflict prevention (Yoon, Velasquez, Partridge, & Nof, 2008; Yoon & Nof, 2010; Landry, Chen, & Nof, 2013), which draw similarities with CRDP. In general, the CRDP model can be applied to network disruption propagation response problems and applications, although the modeling, analytics, and decision-making protocols could require modifications to be reflective of reality. The accompanying system awareness supporting analytics and online scheduling protocols are designed to be general, and can be adapted to conform to different applications and problems.

In CRDP, a CPS is represented as a network of nodes with directed and weighted edges, with the nodes subjected to random initial disruptions that can propagate if left without response. A centrally controlled set of agents work together to respond to remove/repair the disruptions and to prevent immediate propagation of disruption. Three system awareness analytics and two online scheduling protocols are

# ACCEPTED MANUSCRIPT

employed for decision-making. The three SAAs, which include the total disruption strength, node’s response task analytics, and total response workload, provide supporting information for the response activities. The two OSPs, which include the minimizing neighbor disruption propagation (MNDP) protocol and the minimizing additional task workload (MATW) protocol, are proposed to effectively respond to the disruption propagation. These two protocols are proposed to effectively plan and respond to disruptions’ propagation. Moreover, their general decision-making principles can be adapted for similar network types, disruption propagation mechanisms, and response mechanisms. The three AAs and the two OSPs are developed based on the analysis of the interaction between the response agent network, and the disruption propagation and three supporting analytics that are developed for decision support. The two proposed online scheduling protocols are compared with two baseline online scheduling protocols, firstcome-first-serve (FCFS) and shortest processing time (SPT). The CRDP model is then validated using two experiments: one experiment with predetermined client network and one experiment with an adapted Barabasi-Albert (BA) random network. The results of the experiments indicate that the two originally developed OSPs have superior performance compared to the traditional OSPs, and that the CRDP model is worthy of applications and further researches.

The rest of the article is organized as followed: Section 2. Background with the literature review of related works; Section 3. Methodology and Theory with the CRDP model, the three supporting analytics for system awareness, and the two newly developed online scheduling protocols; Section 4. Experiments, Results, and Discussions with the two experiments and results; Section 5. Conclusion and Discussion of Applications. The abbreviations are listed in Table 1.

Table 1. Abbreviations

<table><tr><td>BA</td><td>Barabasi-Albert</td></tr><tr><td>CPS</td><td>Cyber-physical system</td></tr><tr><td>CRDP</td><td>Collaborative Response of Disruption Propagation</td></tr><tr><td>ELOCC</td><td>Emergent Lines of Collaboration and Command</td></tr><tr><td>FCFS</td><td>First-come-first-serve</td></tr><tr><td>MATW</td><td>Minimizing additional task workload</td></tr><tr><td>MNDP</td><td>Minimizing neighbor disruption propagation</td></tr><tr><td>OSP</td><td>Online scheduling protocol</td></tr><tr><td>SAA</td><td>System awareness analytics</td></tr><tr><td>SmaRTA</td><td>Smart Response Task Allocation</td></tr><tr><td>SPT</td><td>Shortest processing time</td></tr><tr><td>TIE/ELOCC</td><td>Teamwork Integration Evaluator/Emergent Lines of Collaboration and Command</td></tr></table>

## 2. Background

In this section, the relevant literature is discussed and classified. This review is not exhaustive, it is intended to provide an overview of recent research surrounding disruption propagation in CPSs; response mechanisms; resilience and performance metrics; and response strategies, analytics, and protocols. The review of the related works is summarized in Table 2.

Table 2. Summary of literature review

<table><tr><td>Disruption</td><td>Propagation</td><td>Response mechanism</td><td>Response protocol</td><td>Response vs propagation</td><td>Work</td></tr><tr><td>Node and/or edge removal</td><td>Yes</td><td>No</td><td>No</td><td>No</td><td>a</td></tr><tr><td>Node, IN</td><td>Yes</td><td>No</td><td>No</td><td>No</td><td>b</td></tr><tr><td>Node</td><td>Yes</td><td>Yes</td><td>Yes, by attribute</td><td>Yes</td><td>c</td></tr><tr><td>Node, load-based</td><td>Yes</td><td>No</td><td>No</td><td>No</td><td>d</td></tr><tr><td>Node, general function</td><td>Yes</td><td>No</td><td>No</td><td>No</td><td>e</td></tr><tr><td>Node, load-based</td><td>Yes</td><td>Undisrupted node re-distribution</td><td>Yes, by target</td><td>Yes</td><td>f</td></tr><tr><td>Node, edge, binary</td><td>Node to edge, edge to node</td><td>Response agents</td><td>Yes, by distance</td><td>Yes</td><td>g</td></tr><tr><td>Node, edge</td><td>Yes</td><td>No</td><td>No</td><td>No</td><td>h</td></tr><tr><td>Edge, IN</td><td>Yes</td><td>No</td><td>No</td><td>No</td><td>i</td></tr><tr><td>Node</td><td>Yes</td><td>Rewiring edges</td><td>Yes</td><td>No</td><td>j</td></tr><tr><td>Node, binary</td><td>Yes, by edgedirection and weight</td><td>Responseagents</td><td>Yes, by target</td><td>Yes, MNDPand MATW</td><td>This work</td></tr><tr><td colspan="6">IN: interdependent network</td></tr><tr><td colspan="6">a: (Albert, Jeong, &amp; Barabasi, 2000)</td></tr><tr><td colspan="6">b: (Buldyrev, Parshani, Paul, Stanley, &amp; Havlin, 2010)</td></tr><tr><td colspan="6">c: (Buzna, Peters, Ammoser, Kuhnert, &amp; Helbing, 2007)</td></tr><tr><td colspan="6">d: (Motter &amp; Lai, 2002; Crucitti et al., 2004)</td></tr><tr><td colspan="6">e: (Liu et al., 2016; Guariniello &amp; DeLaurentis, 2017)</td></tr><tr><td colspan="6">f: (Chaoqi, Ying, &amp; Xiaoyang, 2017; Chaoqi, Ying, Yangjun, &amp; Xiaoyang, 2017; Chaoqi, Ying, Kun, &amp; Yangjun, 2018)</td></tr><tr><td colspan="6">g: (Zhong &amp; Nof, 2015; Zhong, 2016)</td></tr><tr><td colspan="6">h: (Shen, Smith, &amp; Goli, 2012; Shen, 2013)</td></tr><tr><td colspan="6">i: (S. L. Wang, Hong, Ouyang, Zhang, &amp; Chen, 2013)</td></tr><tr><td colspan="6">j: (Levalle &amp; Nof, 2015b, 2015a, 2017)</td></tr></table>

Cyber-physical systems are typically systems of systems, and can be modeled as complex networks to represent the complex interdependencies of their components and subsystems. The components and subsystems can be modeled as nodes, and the dependencies ca e modeled as edges. For example, in a production network or supply network, nodes can represen panies and edges can represent demand/supply relationship. In manufacturing networks, nodes can represent machines, tools, and workstations, and edges can represent flows of materials, products, or information. Within the context of CPSs and networks, disruptions can be defined as: “Any unexpected, and often negative, changes to any entity in the network, including but not limited to: the nodes, the attributes of the nodes, the edges, and the attribute of the edges”. Among the plethora of research on disruptions in networks, the nature and mechanisms of the disruptions are highly diverse and dependent on the network defined by the respective researchers. One type of network disruption is defined as the removal of nodes and edges from the network (Barabasi & Albert, 1999; Albert et al., 2000; Shen et al., 2012; Shen, 2013; T. Y. Wang, Zhang, Sun, & Wandelt, 2017). With respect to this type of network disruption, an important class of networks, called scale-free networks, including the Internet, cells and metabolic networks, exhibits a very high degree of resistance against nodes and edges removal (Albert et al., 2000). Due to the low characteristic path length of these scale-free networks, however, they are more vulnerable to disruptions that propagate through the networks (as opposed to those that remove the nodes and edges). Several algorithms and

# ACCEPTED MANUSCRIPT

strategies are developed to allocate node/edge removal disruptions in networks to optimize certain objectives, including maximizing the number of graph components and minimizing largest component size (Shen et al., 2012; Shen, 2013). It should be noted that the researches surrounding node/edge removal disruptions are highly related to graph theory and network theory, particular to the concepts of node degree, degree distribution.

Other researches are focused on the disruptions concerning the attributes of the nodes and edges of the network. From a modeling perspective, the attributes of the nodes and edges can be freely designed, giving researchers the capability to model the actual physical networks and their operations more accurately. In supply networks, disruptions mainly concern the attributes of production capabilities of the nodes, which in turns affect the supply/demand relationships (attributes of edges). One type of disruption reduces the quality of service and the outputs of the nodes, affecting succeeding nodes (Levalle & Nof, 2015b, 2015a, 2017). Such disruptions reduce output flows of the nodes, requiring succeeding nodes to have contingent sources or face reduced production rate and affecting other succeeding nodes (Seok, Kim, & Nof, 2016). Traffic disruptions in road networks are concerned with the attribute traffic density of the edges (Zhang, Gier, & Garoni, 2014). Another type of disruption is concerned with the attribute failure status of the nodes and edges (Zhong et al., 2014; Zhong & Nof, 2015; Zhong, 2016), which occurs initially and targets nodes, and can propagate to the connected edges, which in turns propagate the disruptions to other nodes. Different disruptions targets are investigated in the works of S. L. Wang et al. (2013).

Due to the complex interactions and interdependencies within a network, disruptions can propagate from a node/edge to other nodes/edges. For example, a disruption propagation mechanism by load-based mechanism, in which disrupted nodes reduce the load of their connected nodes, is developed by Motter and Lai (2002). The load-based disruptions (which are node removals) affect the loads of the nodes, and when a node fails due to insufficient load, it is removed from the network, which reduces the load of its neighbor nodes (Yin, Liu, Liu, & Li, 2016). A more general version of the load-based disruption involves the propagation of the impacts to other nodes through relationships and functions that can be customized

# ACCEPTED MANUSCRIPT

to individual nodes (Guariniello & DeLaurentis, 2017). Other researches that investigate disruption propagation include (Crucitti et al., 2004; Buzna et al., 2007; Buldyrev et al., 2010; Chaoqi, Ying, & Xiaoyang, 2017; Chaoqi, Ying, Yangjun, et al., 2017; Chaoqi et al., 2018). In general, the mechanisms of propagation of disruptions are specific to the networks modeled by the researchers. Two main observations are made: (1) for unweighted networks, the disruption propagations are generally related to are generally related to both the degree of the nodes and the attributes of the nodes and edges as defined by the networks concerned.

The response mechanisms and strategies investigated in the literature are also specific to the networks modeled by the researchers. For instance, a response mechanism using gradually increasing amounts of response capability is developed by Buzna et al. (2007). This increasing amount is determined by a function, with the response strategies considering the status of the nodes. Another response mechanism involving balancing energy loads of nodes is developed, and the response decisions are concerned with which nodes, edges, and the amount (Chaoqi, Ying, & Xiaoyang, 2017; Chaoqi, Ying, Yangjun, et al., 2017; Chaoqi et al., 2018). Both centralized and decentralized algorithms are investigated and compared in preventing errors and conflicts in complex networks, which can propagate throughout the network if left undetected and without response (Chen & Nof, 2012; Landry et al., 2013). Another response mechanism uses agent-based and semi-centralized decision making to re-route supply/demand flows to sustain network performance during disruptions (Levalle & Nof, 2015b, 2015a, 2017). One response mechanism focuses on the initial allocation of response agents based on centrality (Zhong & Nof, 2015), and this mechanism is further improved with better online scheduling protocols (Zhong, 2016). Another response mechanism explores the dimension of configurations of various repair teams and equipment in electrical networks (Landegren, Johansson, & Samuelsson, 2016).

Due to the importance of the response activities to the resilience and recovery of the CPSs, response activities are typically coordinated by human operators and managers. The large scale and complexity of the CPSs necessitate the use of cyber-augmented decision-making and decision support systems in

# ACCEPTED MANUSCRIPT

disruption response. For instance, the decision support based on different network disruption scenarios is developed by Snediker et al. (2008). Important supporting analytics for network analysis and disruption response are discussed in the works of Burgholzer, Bauer, Posset, and Jammernegg (2013), Basole and Bellamy (2014), Shao, Shi, Choi, and Chae (2018), and Basole (2016). Decision support for effective resource allocation is emphasized in the work of Arora, Raghu, and Vinze (2010). A related topic to network propagation disruption response is emergency response and emergency manage nt. These topics highlight the importance of decision support, communication, and collaboration in responding to emergencies, of which network disruption propagation is a subset (Novak & Sullivan, 2014; Xu, Du, & Chen, 2015; Khalemsky & Schwartz, 2017).

From the literature survey, it is observed that most related works do not specifically investigate the disruption-propagation-limiting effect of the response activities. The literature survey also reveals a large variety of network types, disruption propagation mechanisms, response mechanisms, and response protocols/strategies. Therefore, a general approach to modeling, decision-making, and decision support are appropriate in addressing the network disruption propagation response problem. This knowledge gap is addressed by the CRDP model, which is discussed in the next section.

## 3. Methodology and Theory

## 3.1. The CRDP model – framework and formulation

![](/api/attachments/SAJ2AQVK/fulltext/images/31b961f7aeed66d989009d0b0520c92e3f8b44c03eb7d9415e60d150a8e2aa08.jpg)  
Figure 1. The CRDP model

In this section, the CRDP model is presented, as seen in Figure 1. The CRDP model has 3 main components: D1 – the client network; D2 – the agent network; and D3 – the disruptions. The component D1, the client network, represents the CPS concerned. Within the scope of this work, the client network is a network of nodes and weighted, directed edges. The direction of the edge denotes the direction of the disruption propagation, while the weight of the edge denotes the time taken for a disruption to propagate.

The component D2, the agent network, represents the agents responsible for responding to the disruptions. The component D3 consists of the disruptions, which target and propagate throughout the client network. Within the scope of the CRDP model, the disruptions are assumed to occur initially, only in nodes, and can propagate within the client network through the directions and weights of the edges. Should edge disruption modeling be required, the CRDP model can be applied by converting the edges to created to reflect the relationship between the original nodes and original edges.

The edges of the triangle represent the interaction between the main components: E12 – the client-agent interaction; E13 – the client-disruption interaction; and E23 – the agent-disruption interaction. The edge E12, the client-agent interaction, represents the interaction between the client network and the agent network. Broadly speaking, the interaction and relationship include any emergent behavior resulting from the involvement of both the client network and the agent network. Within the scope of this work, each agent may have different response times for different nodes, which is represented by a response requirement matrix. The edge E13, the client-disruption interaction, represents the interaction between the client network and the disruptions. In this work, E13 defines that the disruption propagations follow the directions of the edges of the client network and have the propagation times defined by the weights of the edges. The edge E23, the agent-disruption interaction, represents the interaction between the agent network and the disruptions. In this work, E23 defines that the presence of a response activity at a node from an agent will stop all disruption propagation from and to the node involved. Once the agent ends the response, however, possible future disruption propagation involving this node may still occur. The decision-making aspect (online scheduling protocols), system awareness analytics, and system performance metrics are discussed in Section 3.2. The features of the CRDP model are summarized in Table 3.

Table 3. Summary of the CRDP model

<table><tr><td>Aspect</td><td>Features</td><td>Details</td></tr><tr><td rowspan="2">CRDP components</td><td>D1 – Client network</td><td>Network of nodes with directed and weighted edges.</td></tr><tr><td>D2 – Agent network</td><td>Network of agents that respond to disruptions.</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td>Aspect</td><td>Features</td><td>Details</td></tr><tr><td></td><td>D3 – Disruptions</td><td>Initial disruptions that target nodes and propagate through edges.</td></tr><tr><td rowspan="3">CRDP interactions</td><td>E12 – Client-agent interaction</td><td>Each agent can have different response times for different nodes.</td></tr><tr><td>E13 – Client-disruption interaction</td><td>Disruption propagates through the directions of edges and with propagation times defined by the weights of edges.</td></tr><tr><td>E23 – Agent-disruption interaction</td><td>The agent responding to a node automatically stop any propagation from and to the node, but disruption can start propagating again after the response is over.</td></tr></table>

This representation provides a robust framework for analyzing and simulating the CRDP model and provides a solid platform for future works. Future works can utilize this representation to introduce further variations and generalization of the CRDP model.

In the CRDP model, the disruptions propagate unidirectionally via the edges of the network. When a node is disrupted, its succeeding edges propagate the disruption to their end nodes after the time denoted by the weights of the edges. An example of client-disruption interaction is shown in Figure 2. The agent-

t = 0, node 0 disrupted

t = 1, node 1 disrupted

t = 1.25, node 3 disrupted

![](/api/attachments/SAJ2AQVK/fulltext/images/c588389994febc1fbdcd2d862db60efb8d11ff4f3f1a1c404d6b627baecc4915.jpg)  
Figure 2. Disruption propagation example

![](/api/attachments/SAJ2AQVK/fulltext/images/77785876a5d8049e22ad4f314afbf36954674fbae5d804f343ca101ea2d04ea7.jpg)  
Figure 3. Response mechanism example

The next step is to develop the simulation of the CRDP model. The CRDP model is simulated through the use of C# and an adapted discrete-event simulation programming, which culminates in the Purdue PRISM Center’s Teamwork Integration Evaluator/Emergent Lines of Collaboration and Command (TIE/ELOCC) software. The terms and their attributes are defined in Table 4.

Table 4. Entities and attributes of the CRDP model

<table><tr><td>Type</td><td>Entity/Attribute</td><td>Explanation</td><td>Correspond to</td></tr><tr><td colspan="4">The following entities are defined for the CRDP model</td></tr><tr><td>Input</td><td colspan="2"> $CRDP = (CN, AL, DNL, RRM)$ </td><td>CRDP model</td></tr><tr><td>Input</td><td> $CN = (NL, EL)$ </td><td>The client network, subjected to disruptions.</td><td>D1</td></tr><tr><td>Input</td><td> $NL = \{n_0, n_1, n_2 \ldots\}$ </td><td>The set of nodes in the client network.</td><td>D1</td></tr><tr><td>Input</td><td> $EL = \{e_0, e_1, e_2 \ldots\}$ </td><td>The set of weighted and directed edges, which represent the directions and time taken for disruptions to propagate from one node to other nodes connected to it.</td><td>D1</td></tr><tr><td>Input</td><td> $AL = \{a_0, a_1, a_2 \ldots\}$ </td><td>The set of weighted agents, which is responsible for responding to disruptions.</td><td>D2</td></tr><tr><td>Input</td><td> $DNL \subset NL$ </td><td>The set of nodes subjected to initial disruptions.</td><td>D3</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td>Type</td><td>Entity/Attribute</td><td>Explanation</td><td>Correspond to</td></tr><tr><td>Input</td><td> $RRM = (r_{i,j}) \in \mathbb{R}_{>0}^{|AL| \times |NL|}$ </td><td>The response requirement matrix, whose rows correspond to the agents in  $AL$ , and columns correspond to the nodes in  $NL$ .  $r_{i,j}$  indicates the time taken for agent i to respond to node j.</td><td>E12</td></tr><tr><td colspan="4">The following attributes are defined for each node n ∈ NL</td></tr><tr><td>Dynamic</td><td> $NOS(n) \in \{0,1\}$ </td><td>The operational status of node n.  $NOS(n) = 1$  means the node is not disrupted.  $NOS(n) = 0$  means the node is disrupted and can propagate disruptions to its successor nodes.</td><td>E13</td></tr><tr><td>Dynamic</td><td> $NAA(n) \in AL$ </td><td>Node n&#x27;s currently assigned response agent for responding to its disruption.</td><td>E23</td></tr><tr><td>Dynamic</td><td> $NFCFS(n) \in \mathbb{R}_{\geq 0}$ </td><td>Node n&#x27;s last disrupted time, which is used in the first-come-first-serve scheduling protocol.</td><td>E13</td></tr><tr><td>Derived</td><td> $NIEL(n) \subset EL$ </td><td>Node n&#x27;s set of incoming/preceding edges.</td><td>D1</td></tr><tr><td>Derived</td><td> $NOEL(n) \subset EL$ </td><td>Node n&#x27;s set of outgoing/succeeding edges.</td><td>D1</td></tr><tr><td colspan="4">The following attributes are defined for each edge e = ( $n_i$ ,  $n_j$ ) ∈ EL</td></tr><tr><td>Derived</td><td> $ENI(e) \equiv n_i \in NL$ </td><td> $n_i$  denotes the start node of edge e.  $ENI(e)$  is the alternative notation for  $n_i$  of e.</td><td>D1</td></tr><tr><td>Derived</td><td> $ENJ(e) \equiv n_j \in NL$ </td><td> $n_j$  denotes the end node of edge e.  $ENJ(e)$  is the alternative notation for  $n_j$  of e.</td><td>D1</td></tr><tr><td>Input</td><td> $EDPT(e) \in \mathbb{R}_{>0}$ </td><td>Edge e&#x27;s disruption propagation time. Suppose node  $n_i$  is disrupted at time t, then at time t + EDPT(e), node  $n_j$  will become disrupted if both node  $n_i$  and node  $n_j$  have not been responded to by an agent. If  $EDPT(e) = 0$ , both  $n_i$  and  $n_j$  can be treated as the same node, and their response requirement in  $RRM$  should be updated accordingly.</td><td>E13</td></tr><tr><td>Dynamic</td><td> $EDPS(e) \in \{0,1\}$ </td><td>Edge e&#x27;s disruption propagation status, mainly used for simulation.  $EDPS(e) = 1$  means the disruption propagation along edge e will occur as planned.  $EDPS(e) = 0$  means the disruption propagation is halted, due to the intervention of an agent.</td><td>E13</td></tr><tr><td colspan="4">The following attributes are defined for each agent a ∈ AL:</td></tr><tr><td>Dynamic</td><td> $ABS(a) \in \{0,1\}$ </td><td>Agent&#x27;s busy status.  $ABS(a) = 0$  means the agent is idle, and  $ABS(a) = 1$  means the agent is busy (currently responding to a disruption).</td><td>D2</td></tr><tr><td colspan="4">Simulation-specific parameters are defined for the CRDP model:</td></tr><tr><td>Dynamic</td><td>t</td><td>The current time of the simulation.</td><td>Simulation</td></tr><tr><td>Dynamic</td><td> $t_{last}$ </td><td>A variable mainly used for recording performance metrics.</td><td>Simulation</td></tr><tr><td>Input</td><td>simLen</td><td>Simulation length. Once t = simLen or  $\sum_{n}^{NL} NOS(n) = |NL|$ , the simulation ends.</td><td>Simulation</td></tr><tr><td>Input</td><td>selPro</td><td>Selected protocol for the replication.</td><td>E23</td></tr></table>

# ACCEPTED MANUSCRIPT

The entities and attributes provided in Table 4 are necessary to satisfy the CRDP model requirements as introduced in Table 3. The entities of interest in the system include the nodes, edges, agents, and disruptions. The attributes are characteristics of the entities. The entities and attributes are either input entities, input attributes, dynamic attributes, and derived attributes. The input entities and input attributes are given by the user or the case study and remain unchanged throughout the simulation. The derived attributes are derived from the input entities and input attributes, and also remain unchanged throughout the simulation. On the other hand, the dynamic attributes can be changed throughout the simulation. The discrete events necessary to simulate the CRDP model are given in Table 5.

Table 5. The discrete events used in CRDP

<table><tr><td>Event</td><td>Pseudocode</td></tr><tr><td> $Ndp(t,e)$ </td><td>if  $(EDPS(e) = 1 \text{ and } NOS(ENJ(e)) = 1)$ </td></tr><tr><td>Node disruption propagates</td><td> $NOS(ENJ(e)) \leftarrow 0;$  $NFCFS(ENJ(e)) \leftarrow t;$ foreach  $(e_{nj} \in NOEL(ENJ(e)) | EDPS(e_{nj}) = 0 \text{ and } NAA(ENJ(e_{nj}) = null)$ </td></tr><tr><td>Corresponds to E13, E23</td><td> $EDPS(e_{nj}) \leftarrow 1;$ Schedule event  $Ndp(t + EDPT(e_{nj}), e_{nj});$ </td></tr><tr><td>Aern(t,a,n)</td><td> $NOS(n) \leftarrow 1;$ </td></tr><tr><td>Agent ends responding node</td><td> $NAA(n) \leftarrow \text{null};$  $ABS(a) \leftarrow 0;$ If  $(\exists n \in NL|NOS(n) = 0 \text{ and } NAA(a) = \text{null})$ For each  $(e \in NIEL(n) | NOS(ENI(e)) = 0 \text{ and } NAA(ENI(e)) = \text{null})$ </td></tr><tr><td>Corresponds to E12, E13, E23</td><td> $EDPS(e) \leftarrow 1;$ Schedule event  $Ndp(t + EDPT(e), e);$ </td></tr></table>

The discrete events provided in Table 5 are necessary to satisfy the requirements of the CRDP model as stated in Table $3 . { \mathrm { T h e } } N d p ( t , e )$ event models the disruption propagation that occurs at time ?? and propagates along edge ??. The if-statement checks if either node associated with the edge ?? has been responded to or not (which will lead to $E D P S ( e ) = 1 { \mathrm { a n d } } N O S { \bigl ( } E N J ( e ) { \bigr ) } = 1 )$ . If the propagation can occur, it will update the status of operational status of the node, and schedule future propagation events at the end node of edge ??, which is ??????(??). The $A e r n ( t , a , n )$ event models the end of the response activity of agent ?? to node ?? at time ??. The if-statement at the end models the possible re-disruption once the

response activity ends. Note that the beginning of the response activity is combined with the main simulation logic, because this is a decision of the agent network. The simulation logic is given in Table 6.

Table 6. The CRDP simulation logic

<table><tr><td>Step</td><td>Pseudocode</td></tr><tr><td>Step 1</td><td>Initialize CRDP = (CN, AL, DNL, RRM) and simulation parameters, and t = 0</td></tr><tr><td>Step 2</td><td> $\forall n_{nd} \in NL - DNL, NOS(n_{nd}) \leftarrow 1;$ </td></tr><tr><td>Step 3</td><td>For each  $(n_d \in DNL)$ </td></tr><tr><td>Step 3.1</td><td> $NOS(n_d) \leftarrow 0; NFCFS(n_d) \leftarrow 0;$ </td></tr><tr><td>Step 3.2</td><td>foreach  $(e_{nj} \in NOEL(ENJ(e)) | EDPS(e_{nj}) = 0 \text{ and } NAA(ENJ(e_{nj}) = \text{null})$  $EDPS(e_{nj}) \leftarrow 1;$ Schedule event  $Ndp(t + EDPT(e_{nj}), e_{nj});$ </td></tr><tr><td>Step 4</td><td>while  $(t < simLen \text{ and } \sum_{n \in NL} NOS(n) < |NL|)$ </td></tr><tr><td>Step 4.1</td><td>Run all events Ndp at time t;</td></tr><tr><td>Step 4.2</td><td>Run all events Aern at time t;</td></tr><tr><td>Step 4.3</td><td>For each  $(a \in AL | ABS(a) = 0)$  $n \leftarrow AaP(selPro, a); NAA(n) \leftarrow a; ABS(a) \leftarrow 1;$  $tRF \leftarrow tRF + 1/|NL|;$ For each  $(e \in NIEL(n)) EDPS(e) \leftarrow 0;$ For each  $(e \in NOEL(n)) EDPS(e) \leftarrow 0;$ Schedule event  $Aern(t + RRM(a, n), a, n);$ </td></tr><tr><td>Step 4.4</td><td>Calculate performance metrics $pL \leftarrow \sum_{n}^{NL} \frac{1-NOS(n)}{|NL|}; tPL \leftarrow tPL + pL * (t - t_{last})/|NL|;$  $mDPF \leftarrow \max(mDPF, pL);$ </td></tr><tr><td>Step 4.5</td><td>Reorder event calendar based on time and event order; $t_{last} \leftarrow t;$  $t \leftarrow \text{ next minimum } t \text{ on event calendar};$ </td></tr></table>

In Table $^ { 6 , }$ step 1 initializes all the input entities and attributes. Step 2 sets the default operational status of all undisrupted nodes. Step 3 simulates the initial disruptions. Step 4 is the main loop of the simulation logic, which runs until ?? reaches ???????????? or when all nodes have been responded to, and no more disruption propagation can occur. Steps 4.1 and 4.2 execute all the events that can occur at time ??. Step 4.3 in calculates the response decision of all available agents via the statement $n  A a P ( s e l P r o , a )$ which is discussed in the next sub-section, 3.2. Step 4.3 also executes the beginning of the response activities, which prevent all the disruption propagation coming from and coming to the node selected. Step 4.4 calculates the performance metrics used to measure the response decisions of the agent network, which is discussed in Table 7. Step 4.5 reorder the event calendar and moves to the next time step ?? to continue the simulation.

Table 7. The CRDP performance metrics

<table><tr><td>System performance metric</td><td>Explanation</td></tr><tr><td>rF</td><td>For each experiment, rF, the recovery fraction, is defined as the fraction of the replications where the system fully recovers from the disruption propagation.</td></tr><tr><td>rT</td><td>For each replication, rT, the recovery time, is defined as the time taken for the agent network to fully recover the client network. When all nodes are at full operational status, disruptions are non-existent and no longer occur, and the simulation ends.if (NOS(n) = 1∀n ∈ NL) rT ← t, else rT ← simLen</td></tr><tr><td>tPL</td><td>For each replication, tPL, the total performance loss, is defined as the over-time average fraction of nodes that are disrupted. $tPL = \frac{\int_{t=0}^{simLen} pL(t) dt}{simLen}$  $pL(t) = \sum_{n}^{NL} \frac{1 - NOS(n)}{|NL|} \text{ at } t$ </td></tr><tr><td>mDPF</td><td>For each replication, mDPF, the maximum disruption propagation fraction, is defined as the largest fraction of the client network that was ever disrupted. $mDPF = \max_{t} pL(t)$ </td></tr><tr><td>tRF</td><td>For each replication, tRF, the total response fraction, is defined as the total number of responses divided by the total number of nodes.</td></tr></table>

The rationales for employing the performance measures given in Table 7 are as follows. Recovery fraction and recovery time are both related to the capability of the agent network to fully recover the client network to full operational status. As many CPSs are critical to the organizations that employ them, it is necessary to fully recover the CPSs as quickly and reliably as possible. The total performance loss measure is relevant in CPSs that still have to function when they are being disrupted. This measure is also relevant when the CPS cannot be quickly recovered, and indicates the fraction of the CPS that is still operational. The maximum disruption propagation fraction measure is relevant when the disruptions can be responded to and removed, but some permanent damage is left behind. For example, information and data contained in a computer network may be stolen by the disruption, even when the disruption is dealt

# ACCEPTED MANUSCRIPT

with. The final performance metrics, the total response fraction, is related to the total efforts exerted by the agent network and is relevant when response resources are scarce.

## 3.2. System awareness analytics and decision-making

Three system awareness analytics (SAA) within the scope of CRDP are developed to monitor the state of the system (including D1, D2, and D3). The analytics can be used to evaluate the performance of the system, and to support the decision-making process of the agent network. The SAAs are developed based on the modeling and simulation logic and reflect the state of the system.

The first SAA is the total disruption strength, denoted as $\begin{array} { r } { T D S ( t ) = \sum _ { n } ^ { N L } N O S ( n ) } \end{array}$ , which reflects the total

The second SAA is the node response task analytic. Each node ?? ∈ ???? is given an additional attribute, $N R T A ( n ) \in \mathbb { R } _ { > 0 }$ . Node ??’s response task analytic, which is the average of all the agents’ response times for this node, if it fails. The response task analytic is calculated as $\begin{array} { r } { N R T A ( n ) = \sum _ { \mathrm { a } } ^ { \mathrm { A L } } \frac { R R M ( a , n ) } { | A L | } . } \end{array}$

Based on the second SAA, a third SAA, which is called the total response workload, denoted as $\begin{array} { r } { T R W ( t ) = \sum _ { n } ^ { \{ n \in N L : N O S ( n ) = 0 \} } } \end{array}$ ????????(??). This SAA reflects the expected workload needed to respond to all disrupted nodes $\{ n \in N L \colon N O S ( n ) = 0 \}$ in the client network ????.

Four online scheduling protocols (OSP) are employed for the decision-making of smart agents in the CRDP model. The OSP determines the selected node for the function $A a P ( s e l P r o , a )$ discussed above. The first OSP, which is a baseline OSP, is the first-come-first-serve (FCFS) scheduling policy, which prioritizes disrupted nodes that were disrupted earlier. The tie-breaker for this rule is the lower node ID. The corresponding FCFS selection index of each node ?? is defined as $N F C F S ( n ) \in \mathbb { R } _ { \ge 0 }$ , which is recorded by the simulator.

The second OSP, which is also a baseline OSP, is the shortest processing (response) time (SPT) scheduling policy, which prioritizes the nodes with the shortest response time, for the agent being considered. The tie-breaker for this rule is the lower ??????????(??) and then the lower node ID. The corresponding SPT selection index of each node ??, for a given agent ??, is $R R M ( a , n )$ .

The third OSP is the minimizing neighbor disruption propagation protocol (MNDP), which prioritizes the nodes with lower average un-disrupted edge propagation time. This OSP is developed based on the first SAA, ??????(??), and seeks to minimize the growth of the total disruption strength, $\begin{array} { r } { \frac { d } { d t } T D S ( t ) } \end{array}$ . The MNDP protocol utilizes the important interaction between the response mechanism and disruption propagation: an agent’s response to a node halts all incoming and outgoing disruption propagation from that node. A more basic version of this index ?????????? is illustrated in Figure 4, where node B is prioritized because it has more succeeding nodes that have not been disrupted.

![](/api/attachments/SAJ2AQVK/fulltext/images/6ea3d8be7d36fb77de6670ebbba3089d64f00cba61333d2a292fcb88dad723a2.jpg)  
Figure 4. NMNDP protocol illustration

The undirected and unweighted version of ?????????? is discussed in (Zhong, 2016) as the activity-based priority scheduling protocol. The MNDP improves upon the activity-based priority scheduling protocol by (1) adjusting to the directed network by considering only succeeding undisrupted nodes; (2) prioritizing the nodes with lower (which means faster) disruption propagation time. The MNDP selection index of each node ?? is defined as $N M N D P ( n ) \in \mathbb { R } _ { > 0 }$ , which is calculated as followed:

$$
N M N D P (n) = \left\{ \begin{array}{l l} \sum_ {e} ^ {N O E L _ {M N D P}} \frac {E D P T (e)}{| N O E L _ {M N D P} |}, & \text {if |NOEL_{MNDP}| > 0} \\ \infty , & \text {if |NOEL_{MNDP}| = 0} \end{array} \right.\tag{Equation 1}
$$

$$
N O E L _ {M N D P} \leftarrow N O E L (n) | N O S \bigl (E N J (e) \bigr) = 1 \mathrm{and} N A A \bigl (E N J (e) \bigr) = \mathrm{null}
$$

Nodes with no un-disrupted succeeding node receive a very large value to $N M N D P ( n )$ , and are with the lowest response priority, because disruption cannot propagation from them. The tie-breaker for this rule is the lower processing time for the agent ?? being considered $R R M ( a , n )$ , then the lower ??????????(??) and then the lower node ID.

The fourth OSP is called the minimizing additional task workload rule (MATW), which improves upon MNDP. This OSP is developed based on the second and third SAA, ??????(??), and seeks to minimize the growth of the total response workload, $\ { \frac { d } { d t } } T R W ( t )$ . Similar to MNDP, the MATW protocol utilizes the important interaction between the response mechanism and disruption propagation: an agent’s response to a node halts all incoming and outgoing disruption propagation from that node. With MATW, the agent will prioritize the node that, if disrupted, will lead to the most additional workload on the agent network. Compared to the other three OSPs, the MATW protocol provides a balance of minimizing disruption propagation as well as the agent network’s processing times.

Then, the corresponding MATW selection index of each node ?? is defined as $N M A T W ( n ) \in \mathbb { R } _ { > 0 }$ , which is calculated as followed:

$$
N M A T W (n) = \left\{ \begin{array}{l l} \sum_ {e} ^ {N O E L _ {M N D P}} \frac {E D P T (e)}{N R T A (E N J (e))}, & \text {if |NOEL_{MNDP}| > 0} \\ \infty , & \text {if |NOEL_{MNDP}| = 0} \end{array} \right.\tag{Equation 2}
$$

$$
\text {with} N O E L _ {M N D P} \leftarrow N O E L (n) | N O S \bigl (E N J (e) \bigr) = 1 \text {and} N A A \bigl (E N J (e) \bigr) = \text {null}.
$$

Nodes with no un-disrupted succeeding node receive a very large value to ??????????(??). The tie-breaker for this rule is the lower processing time for the agent ?? being considered $R R M ( a , n )$ , then the lower ??????????(??) and then the lower node ID.

## 4. Experiments, Results, and Discussions

In this section, two numerical experiments are conducted to illustrate the CRDP model, and the results are presented and discussed.

# ACCEPTED MANUSCRIPT

## 4.1. The first experiment

The first experiment involves a predetermined 26-node directed and weighted network (DWN) illustrated in the Appendix A – Figure A.1. The DWN has 4 clusters of nodes: top-left (nodes 0-7), top-right (nodes 8-14), bottom-left (nodes 15-20), and bottom-right (21-25). The DWN has a total of 50 edges, with average weight 2.17 units. In this DWN, a disruption in a certain cluster can propagate unidirectionally very quickly within the cluster, but slowly and bidirectionally to other clusters. To add rigor to the experiment, 20 cases are created with variations on the weight of the edges, with each edge receiving a +/- 25% adjustments to its base weight. Four cases of agent network are investigated and are listed in the Appendix A – Table A.1, with the response requirement matrix of each case adjusted so the four teams are equal in $\textstyle \sum _ { a } ^ { A L } \sum _ { n } ^ { N L } 1 / R R M ( a , n )$ . Six cases of disruptions are investigated with the number of initial failures ranging from 5 to 10, and the nodes subjected to initial disruptions are randomly picked. The four online scheduling protocols discussed above are used and the results with five performance metrics are presented. With each experiment setting, 20 replications are conducted. The comparisons are made between the factors of disruptions and protocols. Table 8 summarizes the experiment setup. The graphical results with 95% confidence intervals are presented in Figure 5, with overlapping confidence intervals denoting statistical significance at $\alpha = 0 . 0 5$ . The comparison between the baseline and the MNDP and MATW online scheduling protocols are provided in Table 9.

Table 8. Experiment 1 – variations summary.

<table><tr><td>Factor</td><td># variations</td><td>Details</td></tr><tr><td>Client network</td><td>1</td><td>The DWN base case or its variations.</td></tr><tr><td>Agent network</td><td>4</td><td>One small team of strong agents, one large team of weak agents, one mixed team, and one cluster-specific team</td></tr><tr><td>Disruptions</td><td>6</td><td>Number of initial failures ranging from 5 to 10.</td></tr><tr><td>Protocols</td><td>4</td><td>FCFS (baseline) vs SPT (baseline) vs MNDP vs MATW</td></tr></table>

![](/api/attachments/SAJ2AQVK/fulltext/images/c757a7562d847b5ee6e8357789a1c446e39ea73b1e8a14ccfdbbd46f1440b146.jpg)

![](/api/attachments/SAJ2AQVK/fulltext/images/d557f725338c26235c2f1de59dbba248a5f0f95781d48cc5a698439d54f52033.jpg)

![](/api/attachments/SAJ2AQVK/fulltext/images/81151a74905fad2ace757f01a970845fef75d5397a9f8f0c8a70e3a838497228.jpg)

![](/api/attachments/SAJ2AQVK/fulltext/images/9b3b5794f08c4597677aec01006255c140a488691b0b8784c1b12b0694a43781.jpg)

![](/api/attachments/SAJ2AQVK/fulltext/images/28342fca09bda7a20e68be0984f96085463956172443192659aaa260cf90ee07.jpg)  
Figure 5. Experiment 1 – results

Table 9. Experiment 1 – MNDP and MATW comparison

<table><tr><td>Performance measure</td><td>Number of failures</td><td>MNDP vs (FCFS &amp; SPT)</td><td>MATW vs MNDP</td><td>Number of failures</td><td>MNDP vs (FCFS &amp; SPT)</td><td>MATW vs MNDP</td></tr><tr><td rowspan="3">Recovery Fraction</td><td>5</td><td>Same</td><td>Same</td><td>8</td><td>+150%</td><td>Same</td></tr><tr><td>6</td><td>Same</td><td>Same</td><td>9</td><td>+400%</td><td>Same</td></tr><tr><td>7</td><td>+33%</td><td>Same</td><td>10</td><td>+566%</td><td>Same</td></tr><tr><td rowspan="3">Recovery Time</td><td>5</td><td>-1.1%</td><td>+6.6%</td><td>8</td><td>-5.9%</td><td>+24%*</td></tr><tr><td>6</td><td>+4.4%</td><td>+7.5%</td><td>9</td><td>-16.5%</td><td>+29%*</td></tr><tr><td>7</td><td>+2.3%</td><td>+10%*</td><td>10</td><td>-14.6%</td><td>+30%*</td></tr><tr><td rowspan="3">Total Performance Loss</td><td>5</td><td>-2.4%</td><td>+8.5%</td><td>8</td><td>+482%*</td><td>+54%*</td></tr><tr><td>6</td><td>+317%*</td><td>+21%*</td><td>9</td><td>+357%*</td><td>+97%*</td></tr><tr><td>7</td><td>+583%*</td><td>+40%*</td><td>10</td><td>+294%*</td><td>+84%*</td></tr><tr><td>Max</td><td>5</td><td>+0.2%</td><td>+1.7%</td><td>8</td><td>+79%*</td><td>+9.8%*</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td>Performance measure</td><td>Number of failures</td><td>MNDP vs (FCFS &amp; SPT)</td><td>MATW vs MNDP</td><td>Number of failures</td><td>MNDP vs (FCFS &amp; SPT)</td><td>MATW vs MNDP</td></tr><tr><td rowspan="2">Disruption Propagation</td><td>6</td><td>+37%*</td><td>+2.8%</td><td>9</td><td>+86%*</td><td>+15%*</td></tr><tr><td>7</td><td>+84%*</td><td>+4.6%</td><td>10</td><td>+76%*</td><td>+15%*</td></tr><tr><td rowspan="3">Total Response Fraction</td><td>5</td><td>-0.4%</td><td>+7.6%*</td><td>8</td><td>+142%*</td><td>+45%*</td></tr><tr><td>6</td><td>+70%*</td><td>+13%*</td><td>9</td><td>+127%*</td><td>+45%*</td></tr><tr><td>7</td><td>+145%*</td><td>+21%*</td><td>10</td><td>+107%*</td><td>+44%*</td></tr><tr><td colspan="3"></td><td colspan="4">+ indicates better results; - indicates worse results; * indicates statistical significance at α = 0.05</td></tr></table>

With respect to the recovery fraction, the OSPs MNDP and MATW perform significantly better than the baseline protocols FCFS and SPT when the number of failures is high. This implies that MNDP and MATW are more efficient in terms of number of agents used. When the number of failures is 10, FCFS and SPT result in 15% chance of full recovery, while MNDP and MATW result in 100% chance of full recovery. The recovery time performances of the four OSPs are not significantly different in most cases. It is important, however, to note that the protocol MATW generally performs better compared to MNDP. Regarding total performance loss, MATW performs significantly better compared to MNDP, which in turns perform significantly better than FCFS and SPT. While employing MNDP and MATW would result in 100% chance of full recovery, employing MATW would result is lower average performance loss (with lower variation of performance loss also). With respect to maximum disruption propagation, both MNDP and MATW results in significantly lower disruption propagation, which means these two OSPs effectively contained the disruptions and prevent them from spreading throughout the system. With respect to total response fraction, MATW results in significantly better performance compared to MNDP, which in turns performs better than FCFS and SPT.

## 4.2. The second experiment

The second experiment involves a random directed and weighted network adapted from the Barabasi-Albert (BA) random network model from the works of Barabasi and Albert (1999). The undirected and unweighted network is generated following the BA random network model. Then, the procedure is

# ACCEPTED MANUSCRIPT

adapted to add directions and weights to the edges. Each edge receives a probability of 1/3 to be bidirectional, 1/3 to be directional towards the node with lower node ID, and 1/3 to be directional towards the node with higher node ID. Then, each edge independently and randomly receives a weight with distribution Uniform (0.5, 1.5). The response requirement matrix is also randomly generated with each agent receiving an inherent value from Uniform (0.5, 1.5). Then for each agent, the response time to the nodes receive values from Uniform (0.5, 1.5) multiplied by its inherent value as well. The size of the client network is 400 nodes. A total of 9 disruption scenarios, presented in Table 10, are run, with 4 different online scheduling protocols, and 400 replications each. The graphical results with 95% confidence intervals are presented in Figure 6, with overlapping confidence intervals denoting statistical significance at ?? = 0.05.

![](/api/attachments/SAJ2AQVK/fulltext/images/2259fd7e34b397f38e15da9fc1d5b15e4be04b51b7cd8ae58f4be94c200aeffd.jpg)

![](/api/attachments/SAJ2AQVK/fulltext/images/a3f57339777db4ec52d8e65027feb311eeaa770a488ab3600269f3a84911821f.jpg)

![](/api/attachments/SAJ2AQVK/fulltext/images/d2d3e3df1cce080d09e1205a440cad335af3da79ea70af0ce533d9066afc0e68.jpg)

![](/api/attachments/SAJ2AQVK/fulltext/images/777cddc0b0e90ebf4c458c00a7d6f039e46eeb0f4704ca038b3d472540918b26.jpg)

![](/api/attachments/SAJ2AQVK/fulltext/images/02b4e40fe0a4b76748df066ce9d415dc5d617158851d6b542c9f3ba64549891f.jpg)

Figure 6. Experiment 2 – results  
Table 10. Experiment 2 – disruption scenarios

<table><tr><td>Scenario</td><td>Number of disruptions</td><td>Number of agents</td></tr><tr><td>1</td><td>25% of node count = 100</td><td>10% of disruption count = 10</td></tr><tr><td>2</td><td>25% of node count = 100</td><td>20% of disruption count = 20</td></tr><tr><td>3</td><td>25% of node count = 100</td><td>30% of disruption count = 30</td></tr><tr><td>4</td><td>50% of node count = 200</td><td>10% of disruption count = 20</td></tr><tr><td>5</td><td>50% of node count = 200</td><td>20% of disruption count = 40</td></tr><tr><td>6</td><td>50% of node count = 200</td><td>30% of disruption count = 60</td></tr><tr><td>7</td><td>75% of node count = 300</td><td>10% of disruption count = 30</td></tr><tr><td>8</td><td>75% of node count = 300</td><td>20% of disruption count = 60</td></tr><tr><td>9</td><td>75% of node count = 300</td><td>30% of disruption count = 90</td></tr></table>

The OSPs MNDP and MATW perform significantly better than the baseline protocols FCFS and SPT in cases 1-7, and the same for cases 8 and 9. This implies that MNDP and MATW are more efficient in terms of number of agents used. With respect to recovery time, some ixed results are seen, but FCFS performs worst in all cases. Regarding total performance loss, M generally performs better compared to MNDP, which in turns perform significantly better than FCFS and SPT. In the cases with more agents (cases 3, 5, 6, 8, 9), however, the results are significantly different between the three OSPs SPT, MNDP and MATW. With respect to maximum disruption propagation, except with cases 2 and 3, the OSPs do not perform significantly different from each other. Regarding total response fraction, both MNDP and MATW generally performs better than SPT and FCFS.

It can be concluded that the online scheduling protocols MNDP and MATW perform better in the majority of the performance metrics compared to the baseline protocols FCFS and SPT. It is also observed that SPT, MNDP, and MATW performs better than FCFS for most cases and performance metrics. The cases where SPT performs better than MNDP and MATW, however, indicate that more investigation is needed to improve the performance of the agent network’s response decisions.

## 5. Conclusion and Discussion of Applications

In this work, the Collaborative Response of Disruption Propagation (CRDP) model is introduced and formulated to illustrate the effects of disruption propagation and the effects of collaborative disruption

# ACCEPTED MANUSCRIPT

response on a CPS. The CRDP model provides a general framework to categorize the three components of a network disruption propagation response problem: D1 – client network, D2 – agent network, D3 – the disruptions, and their interactions. Three system aware supporting analytics and two online scheduling protocols to support decision-making are proposed and validated. The SAAs and OSPs are developed based on the analysis of the interaction between the response agent network and the disruption propagation. The two proposed OSPs are compared with two baseline OSPs, first-come-f -serve (FCFS) and shortest processing time (SPT). The CRDP model is then validated using two e periments: one experiment with predetermined client network and one experiment with an ada Barabasi-Albert (BA) random network. The performance differences between the two experimental cases indicate that caution is necessary in analyzing different network types, dynamics, and topologies. The CRDP model and the two OSPs are contributions to the broader SmaRTA research a of decision support for disruption propagation prevention in general, and in CPSs in particular. Practitioners, including emergency response managers and s managers, face the challenges of diverse network types, disruption propagation mechanisms, and response mechanisms, as discussed in Section 2. To address this challenge, the CRDP model provides a general framework for practitioners to categorize the important components of the network disruption propagation response problem: D1, D2, and D3. Then, the interactions E12, E13, and E23 can be investigated and comprehended. Then, the system awareness analytics provided by the CRDP model can be used, adapted, and/or expanded as necessary, to capture the states of the system. Furthermore, the two online scheduling protocols, MNDP and MATW, can be employed and/or adapted to coordinate effective response against disruption propagation. An important limitation of this work is that the CRDP model is a general approach to the many different network types, disruption response mechanisms, and response mechanisms that happen in practical situations. More complex modeling features can be included as appropriate for more specific problems. Possible applications of CRDP and possible adaptations to the CRDP model are summarized in Table 11.

Table 11. Summary of CRDP applications and modeling adaptations

<table><tr><td>Aspect</td><td>Practical application examples</td><td>Modeling adaptations</td></tr><tr><td>D1 – Nodes</td><td>Machines, computers, subsystems, enterprises...</td><td rowspan="4">Changes to entities’ attributes as necessary</td></tr><tr><td>D1 – Edges</td><td>Flows, connections, roads, pipes...</td></tr><tr><td>D2 – Agents</td><td>Human agents, autonomous agents, robots...</td></tr><tr><td>D3 – Disruptions</td><td>Supply disruptions, cyber-attacks, diseases</td></tr><tr><td>E12 – Client-agent interaction</td><td>Agent travel time, repair time, virus removal time...</td><td>Modifications to response requirement matrix and/or other modeling changes</td></tr><tr><td>E13 – Disruption propagation</td><td>Supply shortage propagation, cascading system failures, virus spread...</td><td>Modifications to the modeling of disruption propagation mechanism</td></tr><tr><td>E23 – Agent-disruption interaction</td><td>Supply backup and/or supply reroute, virus removal and firewall update, disease quarantine...</td><td>Modifications to the modeling of propagation prevention mechanism</td></tr></table>

Based on this work, emerging researches are recommended to investigate the following directions:

(1) Decision support analytics that capture the complex tradeoff between different response decisions can be developed to support the response decisions.

(2) The long-term aspect of decision-making and online scheduling protocols can be investigated.

(3) More complex and detailed modeling of different network types, disruption propagation mechanisms, and response mechanisms can be developed further from the foundations of the CRDP model. Examples include water network with time-varying edges’ weights, computer networks with existing defense mechanism for nodes, fire spread network with response choice limitation…

(4) Similar to above, different specific algorithms for different network types, disruption propagation mechanisms, and response mechanisms can be developed and expanded.

## Acknowledgment

This research is supported in part by the PRISM Center for Production, Robotics, and Integration Software for Manufacturing & Management at Purdue University.

## ACCEPTED MANUSCRIPT

## References

Albert, R., & Barabasi, A. L. (2002). Statistical mechanics of complex networks. Reviews of Modern Physics, 74(1), 47-97. doi:DOI 10.1103/RevModPhys.74.47

Albert, R., Jeong, H., & Barabasi, A. L. (2000). Error and attack tolerance of complex networks. Nature, 406(6794), 378-382. doi:10.1038/35019019

Arora, H., Raghu, T. S., & Vinze, A. (2010). Resource allocation for demand surge mitigation during disaster response. Decision Support Systems, 50(1), 304-315. doi:https://doi.org/10.1016/j.dss.2010.08.032

Barabasi, A. L., & Albert, R. (1999). Emergence of scaling in random networks. Science, 286(5439), 509-512. doi:10.1126/science.286.5439.509

Basole, R. C. (2016). Topological analysis and visualization of interfirm collaboration networks in the electronics industry. Decision Support Systems, 83, 22-31. doi:https://doi.org/10.1016/j.dss.2015.12.005

Basole, R. C., & Bellamy, M. A. (2014). Visual analysis of supply network risks: Insights from the electronics industry. Decision Support Systems, 67, 109-120. doi:https://doi.org/10.1016/j.dss.2014.08.008

Buldyrev, S. V., Parshani, R., Paul, G., Stanley, H. E., & Havlin, S. (2010). Catastrophic cascade of failures in interdependent networks. Nature, 464(7291), 1025-1028. doi:10.1038/nature08932

Burgholzer, W., Bauer, G., Posset, M., & Jammernegg, W. (2013). Analysing the impact of disruptions in intermodal transport networks: A micro simulation-based model. Decision Support Systems, 54(4), 1580-1586. doi:https://doi.org/10.1016/j.dss.2012.05.060

Buzna, L., Peters, K., Ammoser, H., Kuhnert, C., & Helbing, D. (2007). Efficient response to cascading disaster spreading. Physical Review E, 75(5 Pt 2), 056107. doi:10.1103/PhysRevE.75.056107

Chaoqi, F., Ying, W., Kun, Z., & Yangjun, G. (2018). Complex networks under dynamic repair model. Physica A: Statistical Mechanics and its Applications, 430, 323-330. doi:10.1016/j.physa.2017.08.071

Chaoqi, F., Ying, W., & Xiaoyang, W. (2017). Research on complex networks’ repairing characteristics due to cascading failure. Physica A: Statistical Mechanics and its Applications, 482, 317-324. doi:10.1016/j.physa.2017.04.086

Chaoqi, F., Ying, W., Yangjun, G., & Xiaoyang, W. (2017). Complex networks repair strategies: Dynamic models. Physica A: Statistical Mechanics and its Applications, 482, 401-406. doi:10.1016/j.physa.2017.04.118

Chen, X. W., & Nof, S. Y. (2012). Conflict and error prevention and detection in complex networks. Automatica, 48(5), 770-778. doi:10.1016/j.automatica.2012.02.030

Crucitti, P., Latora, V., & Marchiori, M. (2004). Model for cascading failures in complex networks. Physical Review E, 69(4 Pt 2), 045104. doi:10.1103/PhysRevE.69.045104

Day, J. M. (2014). Fostering emergent resilience: the complex adaptive supply network of disaster relief. International Journal of Production Research, 52(7), 1970-1988. doi:10.1080/00207543.2013.787496

Gong, J., Mitchell, J. E., Krishnamurthy, A., & Wallace, W. A. (2014). An interdependent layered network model for a resilient supply chain. Omega, 46, 104-116. doi:10.1016/j.omega.2013.08.002

Guariniello, C., & DeLaurentis, D. (2017). Supporting design via the system operational dependency analysis methodology. Research in Engineering Design, 28(1), 53-69. doi:10.1007/s00163-016-0229-0

Khalemsky, M., & Schwartz, D. G. (2017). Emergency Response Community Effectiveness: A simulation modeler for comparing Emergency Medical Services with smartphone-based Samaritan response. Decision Support Systems, 102, 57-68. doi:https://doi.org/10.1016/j.dss.2017.07.003

Kim, Y., Chen, Y.-S., & Linderman, K. (2015). Supply network disruption and resilience: A network structural perspective. Journal of Operations Management, 33-34, 43-59. doi:10.1016/j.jom.2014.10.006

Kumar, P., Gupta, S., & Bhasker, B. (2017). An upper approximation based community detection algorithm for complex networks. Decision Support Systems, 96, 103-118. doi:https://doi.org/10.1016/j.dss.2017.02.010

Landegren, F. E., Johansson, J., & Samuelsson, O. (2016). A Method for Assessing Margin and Sensitivity of Electricity Networks With Respect to Repair System Resources. IEEE Transactions on Smart Grid, 7(6), 2880-2889. doi:10.1109/Tsg.2016.2582080

Landry, S. J., Chen, X. W., & Nof, S. Y. (2013). A decision support methodology for dynamic taxiway and runway conflict prevention. Decision Support Systems, 55(1), 165-174. doi:https://doi.org/10.1016/j.dss.2013.01.016

Levalle, R. R., & Nof, S. Y. (2015a). A resilience by teaming framework for collaborative supply networks. Computers & Industrial Engineering, 90, 67-85. doi:10.1016/j.cie.2015.08.017

Levalle, R. R., & Nof, S. Y. (2015b). Resilience by teaming in supply network formation and reconfiguration. International Journal of Production Economics, 160, 80-93. doi:10.1016/j.ijpe.2014.09.036

Levalle, R. R., & Nof, S. Y. (2017). Resilience in supply networks: Definition, dimensions, and levels. Annual Reviews in Control, 43, 224-236. doi:10.1016/j.arcontro1.2017.02.003

Liu, W. P., Liu, C., Yang, Z., Liu, X. Y., Zhang, Y. H., & Wei, Z. X. (2016). Modeling the propagation of mobile malware on complex networks. Communications in Nonlinear Science and Numerical Simulation, 37, 249-264. doi:10.1016/j.cnsns.2016.01.019

Motter, A. E., & Lai, Y. C. (2002). Cascade-based attacks on complex networks. Physical Review E, 66(6 Pt 2), 065102. doi:10.1103/PhysRevE.66.065102

Nof, S. Y. (2007). Collaborative control theory for e-Work, e-Production, and e-Service. Annual Reviews in Control, 31(2), 281-292. doi:10.1016/j.arcontrol.2007.08.002

Nof, S. Y. (2013a). Research Advances in Manufacturing with Service-oriented e-work and Production. Proceedings of International Federation of Automatic Control Intelligent Manufacturing Systems. doi:10.3182/20130522-3-BR-4036.00111

Nof, S. Y. (2013b). Sustainability and resiliency in supply networks. Plenary Talk—14th Asia Pacific Industrial Engineering and Management Society.

Nof, S. Y., Ceroni, J., Jeong, W., & Moghaddam, M. (2015). Revolutionizing Collaboration through e-Work, e-Business, and e-Service: Berlin, Heidelberg : Springer Berlin Heidelberg : Imprint: Springer.

Novak, D. C., & Sullivan, J. L. (2014). A link-focused methodology for evaluating accessibility to emergency services. Decision Support Systems, 57, 309-319. doi:https://doi.org/10.1016/j.dss.2013.09.015

## ACCEPTED MANUSCRIPT

Qiu, J., Wang, Z., Ye, X., Liu, L., & Dong, L. (2014). Modeling method of cascading crisis events based on merging Bayesian Network. Decision Support Systems, 62, 94-105. doi:https://doi.org/10.1016/j.dss.2014.03.007

Sajadi, S. M., Esfahani, M. M. S., & Sorensen, K. (2011). Production control in a failure-prone manufacturing network using discrete event simulation and automated response surface methodology. International Journal of Advanced Manufacturing Technology, 53(1-4), 35-46. doi:10.1007/s00170-010-2814-0

Seok, H., Kim, K., & Nof, S. Y. (2016). Intelligent contingent multi-sourcing model for resilient supply networks. Expert Systems With Applications, 51, 107-119. doi:10.1016/j.eswa.2015.12.026

Shao, B. B. M., Shi, Z., Choi, T. Y., & Chae, S. (2018). A data-analytics approach to identifying hidden critical suppliers in supply networks: Development of nexus supplier index. Decision Support Systems, 114, 37-48. doi:https://doi.org/10.1016/j.dss.2018.08.008

Shen, S. Q. (2013). Optimizing designs and operations of a single network or multiple interdependent infrastructures under stochastic arc disruption. Computers & Operations Research, 40(11), 2677-2688. doi:10.1016/j.cor.2013.05.002

Shen, S. Q., Smith, J. C., & Goli, R. (2012). Exact interdiction models and algorithms for disconnecting networks via node deletions. Discrete Optimization, 9(3), 172-188. doi:10.1016/j.disopt.2012.07.001

Snediker, D. E., Murray, A. T., & Matisziw, T. C. (2008). Decision support for network disruption mitigation. Decision Support Systems, 44(4), 954-969. doi:https://doi.org/10.1016/j.dss.2007.11.003

Wang, S. L., Hong, L., Ouyang, M., Zhang, J. H., & Chen, X. G. (2013). Vulnerability analysis of interdependent infrastructure systems under edge attack strategies. Safety Science, 51(1), 328-337. doi:10.1016/j.ssci.2012.07.003

Wang, T. Y., Zhang, J., Sun, X. Q., & Wandelt, S. (2017). Network repair based on community structure. Europhysics Letters, 118(6). doi:10.1209/0295-5075/118/68005

Xu, X.-h., Du, Z.-j., & Chen, X.-h. (2015). Consensus model for multi-criteria large-group emergency decision making considering non-cooperative behaviors and minority opinions. Decision Support Systems, 79, 150-160. doi:https://doi.org/10.1016/j.dss.2015.08.009

Yin, R. R., Liu, B., Liu, H. R., & Li, Y. Q. (2016). Research on invulnerability of the random scale-free network against cascading failure. Physica A: Statistical Mechanics and its Applications, 444, 458-465. doi:10.1016/j.physa.2015.08.017

Yoon, S. W., & Nof, S. Y. (2010). Demand and capacity sharing decisions and protocols in a collaborative network of enterprises. Decision Support Systems, 49(4), 442-450. doi:https://doi.org/10.1016/j.dss.2010.05.005

Yoon, S. W., Velasquez, J. D., Partridge, B. K., & Nof, S. Y. (2008). Transportation security decision support system for emergency response: A training prototype. Decision Support Systems, 46(1), 139-148. doi:10.1016/j.dss.2008.06.002

Zhang, L., Gier, J. d., & Garoni, T. M. (2014). Traffic disruption and recovery in road networks. Physica A: Statistical Mechanics and its Applications, 401, 82-102. doi:doi.org/10.1016/j.physa.2014.01.034

Zhong, H. (2016). Dynamic lines of collaboration in e-Work systems: Ann Arbor : ProQuest Dissertations & Theses.

Zhong, H., & Nof, S. Y. (2015). The dynamic lines of collaboration model: collaborative disruption response in cyber–physical systems. Computers & Industrial Engineering, 87, 370-382. doi:doi.org/10.1016/j.cie.2015.05.019

Zhong, H., Nof, S. Y., & Filip, F. G. (2014). Dynamic lines of collaboration in CPS disruption response. International Federation of Automatic Control Proceedings Volumes, 47(3), 7855-7860. doi:10.3182/20140824-6-ZA-1003.02403

# ACCEPTED MANUSCRIPT

## Appendix A

![](/api/attachments/SAJ2AQVK/fulltext/images/3579571c8fd4266f8f26d6027307bffb582f2b944befb2c0532dd91f895a93fe.jpg)  
Figure A.1. First experiment – client network

Table A.1. First experiment – response requirement matrix

<table><tr><td rowspan="2">Case</td><td rowspan="2">Agent</td><td colspan="4">Response requirement matrix</td></tr><tr><td>Nodes 0-7</td><td>Nodes 8-14</td><td>Nodes 15-20</td><td>Nodes 21-25</td></tr><tr><td>0</td><td>0, 1</td><td>0.875</td><td>0.875</td><td>0.875</td><td>0.875</td></tr><tr><td>1</td><td>0, 1, 2, 3</td><td>1.75</td><td>1.75</td><td>1.75</td><td>1.75</td></tr><tr><td rowspan="2">2</td><td>0, 1</td><td>0.875</td><td>0.875</td><td>0.875</td><td>0.875</td></tr><tr><td>2</td><td>1.75</td><td>1.75</td><td>1.75</td><td>1.75</td></tr><tr><td rowspan="4">3</td><td>0</td><td>1</td><td>2</td><td>2</td><td>2</td></tr><tr><td>1</td><td>2</td><td>1</td><td>2</td><td>2</td></tr><tr><td>2</td><td>2</td><td>2</td><td>1</td><td>2</td></tr><tr><td>3</td><td>2</td><td>2</td><td>2</td><td>1</td></tr></table>

## Biographical Notes

![](/api/attachments/SAJ2AQVK/fulltext/images/c5f65b1f7d758b883c386dbeae5bccd4b39f3ebbde4e7c36c7a7282a0769a4db.jpg)  
Win P. V. Nguyen received the B. S. degree in Industrial Engineering at Purdue University in 2014, and the M. S. degree in Engineering Technology at Purdue University in 2015. He is currently a Ph. D. candidate in Industrial Engineering at Purdue University. Since 2017, he has been a research assistant with the PRISM Center, Purdue University. His research interests include network resilience, network disruption propagation, collaborative response to network disruptions, collaborative control theory in production systems.

![](/api/attachments/SAJ2AQVK/fulltext/images/b4dd75b02af7ed6a4376299a7e6af2b6ce7d122712d88d807228b9f8b811d45e.jpg)  
Shimon Y. Nof, Ph.D., D.H.C., is Professor of Industrial Engineering, Purdue University, and held visiting positions at MIT and at universities in Chile, EU, Hong Kong, Israel, Japan, Mexico, and Taiwan. He is the Director of the NSF- and industry-supported PRISM Center (Production, Robotics and Integration Software for Manufacturing & Management) linked with PGRN (PRISM Global Research Network); recent Chair of the IFAC Coordinating Committee “Manufacturing & Logistics Systems”; recent President, Secretary General, and current Board member of IFPR (International Federation of Production Research), Fellow of IFPR and of the IISE (Institute of Industrial & Systems Engineers), and inaugural member of Purdue's Book of Great Teachers. He is co-inventor of five automation patents; the author, co-author and editor of fourteen books, including the Handbook of Industrial Robotics 1st and 2nd

editions, the International Encyclopedia of Robotics, (both winners of the “Most Outstanding Book in Science and Engineering” Award,) Information and Collaboration Models of Integration, Industrial Assembly, Springer Handbook of Automation, and Revolutionizing Collaboration through e-Work, e-Business, and e-Service.

# ACCEPTED MANUSCRIPT

Graphical abstract  
![](/api/attachments/SAJ2AQVK/fulltext/images/f758ae572c7a821e556f1d9d85d71174f11244ab0b7cb5a73c860d4848d78b69.jpg)

Note about the use of color for figures in print: no.

## Research Highlights

 Disruptions can quickly propagate within highly connected cyber-physical systems.

 The presence of response mechanism can prevent disruptions from propagating.

 The propagation-response interaction can be utilized to optimize response.

 A general model captures collaborative response to disruption propagation.

 This model and its analytics & protocols can be adapted to support decision making.
