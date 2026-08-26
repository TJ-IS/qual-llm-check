---
otero_id: 3300
otero_key: "EDWUWJ32"
title: "Broken Ties: The Impact of Organizational Restructuring on the Stability of Information-Processing Networks"
authors: "Dowan Kwon; Wonseok Oh; Sangyong Jeon"
year: "2007"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222240106"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Broken Ties: The Impact of Organizational Restructuring on the Stability of Information-Processing Networks

Dowan Kwon , Wonseok Oh & Sangyong Jeon

To cite this article: Dowan Kwon , Wonseok Oh & Sangyong Jeon (2007) Broken Ties: The Impact of Organizational Restructuring on the Stability of Information-Processing Networks, Journal of Management Information Systems, 24:1, 201-231

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222240106

![](/api/attachments/EDWUWJ32/fulltext/images/a66b8e5100023f9e05c434c93311853f73fcf5c110790edf2c6a30bc947a148b.jpg)

Published online: 08 Dec 2014.

![](/api/attachments/EDWUWJ32/fulltext/images/7f939ad4c4e9e958f78de34cea6845dc8f314dca199e73ff83ef69a7f1aee845.jpg)

Submit your article to this journal

![](/api/attachments/EDWUWJ32/fulltext/images/5472463913593c3a883fa1e2e1b9e74ccef701fae5fd1d56d33655656a4bb778.jpg)

Article views: 19

![](/api/attachments/EDWUWJ32/fulltext/images/09b4384f9e0abd8e1e70633f325a916e2bc0d917bb92b51384ede82da9f89bed.jpg)

View related articles

# Broken Ties: The Impact of Organizational Restructuring on the Stability of Information-Processing Networks

DOWAN KWON, WONSEOK OH, AND SANGYONG JEON

DOWAN KWON is an Assistant Professor of MIS at the John Molson School of Business, Concordia University. He received his Ph.D. from Case Western Reserve University and holds an MBA from George Washington University. His research interests include business values and organizational consequences of information and communication technologies. His work experience includes consulting for telecommunication startups and designing information systems for a major South Korean financial firm. He has published papers in the Journal of Strategic Information Systems, Information Technology and People, and Journal of Business Research.

WONSEOK OH is an Assistant Professor of Information Systems in the Desautels Faculty of Management at McGill University. He received his Ph.D. in Information Systems from the Stern School of Business at New York University. His research interests include network theory, social networks, IT outsourcing, business value of information systems, and economic aspects of e-commerce. His research has been published or is forthcoming in Information Systems Research, International Journal of Electronic Commerce, Journal of Management Information Systems, MIS Quarterly, and Management Science.

SANGYONG JEON is an Assistant Professor in the Department of Physics at McGill University. He earned his Ph.D. in Theoretical Physics from the University of Washington. His current research interests include the physics of quark-gluon plasma, heavy ion collision phenomenology, and nonequilibrium quantum field theory. His research has appeared in numerous journals, including Nuclear Physics A, Physical Review A, Physical Review C, Physical Review D, Physical Review E, Physical Review Letters, and Physics Letters B.

ABSTRACT: Information-processing networks (IPNs) denote dynamic network-based information-processing structures that operate as coordination mechanisms that transcend formal hierarchies. Despite growing interest in information technology–enabled IPNs, the literature has been silent in exploring the various ontological structures of IPNs and the structural efficiency embedded in each IPN, especially in the event of radical organizational changes. To fill this gap, this study identifies, from the perspective of graph theory, four ontological IPN archetypes that can serve as blueprints for information processing within and across organizations—random, small world, moderate scale free (MSF), and Barabasi. We then assess how each structure reacts to corporate restructuring (e.g., downsizing) and investigate, based on computer simulation, the extent to which each structure preserves a worker’s efficiency and the stability of the network structure in the event of downsizing. Two moderating variables are included in the model—that is, scale of downsizing and the reconnection strategy in the presence of downsizing. In this study, downsizing is viewed not only as the simple elimination of individual workers but also as the elimination of the communication and information-processing conduits necessary for effective communication and coordination. We find that when firms implement a relatively small-scale workforce reduction, centralized coordination structures such as MSF and Barabasi are generally more resilient and facilitate better coordination. However, when the downsizing strategy involves massive and severe layoffs, decentralized coordination structures such as random and small world are more durable, and tend to provide a stronger safety net, irrespective of the strategies employed to create new ties. Although this study focused exclusively on the context of downsizing, the results of the study have important implications for other types of organizational restructuring (e.g., organizational expansion and merger and acquisition) that reconfigure IPNs.

KEY WORDS AND PHRASES: computer simulation, information-processing networks, network theory, organizational restructuring, social networks.

TRADITIONALLY, MOST ORGANIZATIONS ARE ESTABLISHED and maintained through formal hierarchies by which locus of control and flow of information are determined. In recent years, however, many organizations have adopted highly flexible and responsive structures (e.g., network-based or cluster structures) in an effort to effectively facilitate information processing, communication, and knowledge sharing [1, 21, 34, 53, 72]. Information technology (IT) and other communication media have made these lateral and network-based communications possible by enabling effective informationprocessing networks (IPNs) through which organizational members cooperatively integrate business processes and cross-functional activities [1, 31, 42, 76].

Over the past few decades, researchers and practitioners have made substantial progress in understanding the important role IT plays in creating and maintaining IPNs within and across firm boundaries [32, 38, 42, 77]. Nevertheless, little research has been conducted on the structural configuration or the inherent stability of a firm’s IPN [1], especially in the context of major organizational change (e.g., organizational downsizing). For example, in response to competitive pressure and environmental uncertainty, many organizations routinely undertake large-scale corporate downsizing, which subsequently results in the reconfiguration of information-processing protocols within and across firm boundaries [9, 62]. These organizational changes, therefore, can have a profound impact on the efficiency and stability of a firm’s IPN.

Drawing on network theory [3, 49], this study explores several ontological forms of IPN structures and assesses, through computer simulation, the structural efficiency and stability embedded in each identified IPN in the face of organizational restructuring. More specifically, we first identify several network-based archetypes of informationprocessing mechanisms that can serve as formalized blueprints for IPNs—random, small world, moderate scale free (MSF), and high scale free (HSF or Barabasi<sup>1</sup>). We then proceed to investigate the extent to which each type of IPN buffers the downsizing-induced impediments to information flows. Network theory provides a constructive conceptual venue for identifying an assortment of information-processing structures, and analyzing the structural stability attached to IPN structures. This is because the shape and structure of a network depict the patterns through which organizational communication is facilitated and information is processed [1, 60]. Computer simulations are used as the principal analytical tools to assess holistically how these IPN structures differ in terms of their ability to dampen downsizing effects.

We pay special attention to the structural capability of each IPN in the context of corporate downsizing, because downsizing is a common phenomenon in contemporary organizations that dynamically reconfigures the means by which people process information both within and across firm boundaries. Moreover, emphasis is placed on the specific contexts in which workforce reduction leads to concomitant increases in informationprocessing and communication responsibilities for those remaining (i.e., “survivors”), and may thus produce adverse effects such as work overload and “burnout.”

In contrast to prior research, which has focused primarily on the impact of downsizing on the psychological states of “surviving” individuals (e.g., [10]), this study assesses the strategic consequences of radical organizational changes at the network level by examining the structural and efficiency changes that occur in IPNs. In this respect, downsizing is viewed not just as the simple elimination of individual workers but also as the elimination of the communication and information-processing conduits necessary for effective communication and coordination. In other words, downsizing is likely to reshuffle the significant elements of IPNs by breaking existing ties and creating new ties. Among other issues, we pay particular attention to the following two research questions:

RQ1: Under which IPN structure is employees’ efficiency maximized and network integrity best preserved in the event of corporate downsizing?

RQ2: To what extent do different “reconnection strategies” (e.g., random or planned) following workforce reduction affect the performance of an IPN?

This study makes several contributions to both research and practice. In terms of practice, the present study provides managers with insight into the effective planning, design, and reconfiguration of an IPN that will help them, in the event of downsizing, to minimize impediments to information processing. In addition, the implications drawn from the moderating role of downsizing scale and workload redistribution tactics (i.e., how to “reconnect” an IPN after downsizing has taken place) offer managers effective downsizing and restructuring strategies. As noted earlier, coordination through IPNs has emerged as an important linking component in the integration of intra- and interorganizational business activities. The results of this study, therefore, can be applied to a broad range of organizations, particularly those in which IT plays a significant role as a coordination apparatus. Finally, although this study focused exclusively on downsizing, the results of the study can be applicable to other types of organizational changes that affect existing IPNs. For example, the results derived from a reverse process of our simulation can provide insights into the impact of organizational expansions on IPNs.

From a research perspective, we investigate the intersection of two recent frequent organizational phenomena—the IPN and downsizing—both of which are artifacts arising to a large degree from the proliferation of IT. This study provides researchers with network-related conceptual underpinnings necessary for understanding various aspects of an IPN, including its ontological structure, efficiency, and stability. The application of network theory to the analysis of IPNs is an important contribution to the growing literature that deals with lateral and network-based information processing. In terms of methodological contributions, this study develops rigorous computer simulations to investigate information-processing patterns of various network forms. Network simulations offer a means by which to holistically assess the structural efficiency of IPNs, while validating theoretical propositions that are difficult to evaluate through conventional methods (e.g., survey analysis). In summary, our efforts to offer fresh theoretical insights through the use of advanced methodological tools will help improve researchers’ as well as practitioners’ understanding of IPNs, particularly in the event of radical organizational restructuring.

## Research Background

VARIOUS THEORETICAL LENSES, such as environmental determinacy [35], structural contingency between organizations and environments [26, 67], organizational capabilities for economic controls [56], managerial decision making [18, 63], and institutional arrangements [23, 45], have been adopted to study organizational survivability in response to environmental turbulence. Yet one underlying presumption shared by these various conceptual approaches is that organizations are information-processing entities whose survival and longevity largely depend upon how efficiently and effectively they handle information within and across firm boundaries [33, 70]. In this respect, an organization’s health is understood in terms of its capability to process, distribute, exchange, and coordinate the information. Therefore, the information-processing view of an organization is particularly useful for understanding and analyzing structural forms that organizations develop to process information and proactively react to environmental changes [70]. For example, in order to adjust to uncertain and rapidly changing environments, intense information-related activities in the form of distribution and coordination of information are required. In this context, organizational designs that allow decision autonomy at a local level, while maintaining a flat structure, are preferred to structures that embrace centralized decision making and hierarchical bureaucracy.

The recent development of network concepts has provided significant additional insights into organizational information processing. In particular, network-related concepts, such as nodes (e.g., individuals, groups of people), connecting links (or network ties), and several network topologies (e.g., small world, scale free), help researchers to better understand generalizable behavioral patterns with respect to organizational information processing. For example, a certain type of structure of ties and connections between intra- and interorganizational nodes could be essential for effective information processing, knowledge creation, and innovation, whereas other typological formations may be susceptible to node failure and cascading collapse of the network.

## Organizations as the Nexus of IPNs

This study draws on three streams of research that use the network perspective of information processing. The first stream focuses on how the structure of a network influences information and knowledge transfer, while the second places great emphasis on network robustness and channel stability in situations of environmental turmoil. Finally, the third stream pays particular attention to the performance and stability of IT-enabled virtual communities.

## Network Effects on Information/Knowledge Transfer

Networks often serve as backbones that facilitate information and knowledge-based activities within as well as across organizations [43, 57]. Efficient functioning and information processing of a network is essential for survival and competence [40]. For this reason, networks should be established and refined in ways that maintain an optimal information flow. Owen-Smith and Powell [57] posit that organizational forms fundamentally influence the flow of information through a network. A centralized network could be considered efficient when information interactions occur vertically (e.g., information sent from central nodes to peripheral nodes) [1, 69]. Depending on various contexts of informational requirements, however, less centralized network formation (e.g., smaller hubs) is preferred [73], especially when task-related environments are highly uncertain and tight clustering and autonomy of work groups are necessary. This structural design enhances information exchange at the work group level, and can effectively facilitate mutual adjustments among peripheral local nodes [69]. Furthermore, such local cluster arrangements reduce the processing load assigned to the central node, as peripheral nodes do not need to communicate directly with the central authority whenever a decision-making situation arises [73].

Recently, several network forms that vary from the two extremes (e.g., highly centralized or decentralized) have been applied extensively to the analysis of the patterns of organizational information processing. For example, the “small-world” network, in which a high degree of local clustering and only a small number of links between any two nodes exist, was found to enhance mutual dependence among cluster nodes and facilitate routine communications among actors, especially when tight collaboration is necessary for connecting value chains within the organization [51, 59]. The availability of such short paths for “bridging” nodes enhances coordination and adaptation of the network, particularly when transferring information across heterogeneous or between distant groups [5]. Moreover, such network properties are effective when diffusing new ideas and innovation in complex organizations [8].

## Network Robustness and Channel Stability in Environmental Turmoil

The second stream of research focuses on how organizations reconfigure their information-processing protocols in the event of environmental destruction [24, 51, 62]. Environmental changes influence the patterns through which organizations process information and thus often result in undesirable consequences, such as concentration of information traffic, excessive overload, bottlenecks, slowdown of flow, and even failure. For example, when one of its essential suppliers, Aisin, was faced with a destructive crisis [51],<sup>2</sup> Toyota and its partners formed an emergent interorganizational information network that enabled them to dampen unexpected “shocks,” supply resources with minimal delays, and recover systems in short periods of time [17]. The informational infrastructures across firm boundaries helped mitigate potential information overload, delays, and congestion-related failure, while protecting the network from complete disintegration [24].

Although this case is an illustration of an interorganizational network, such disruptions or impediments in information flow could also occur within an organization, especially when certain members do not perform their information-processing responsibilities, or voluntarily or involuntarily leave the organization. Similarly, when certain nodes in the network experience information overload, the flow of the rest of the network can be affected and often severely damaged.

## Stability and Performance of Online Communities

Based on a case study, Ahuja and Carley [1] found that the fit between network structure and task routines influences member perceptions of performance. More specifically, this study showed that the degree to which network-based coordination is centralized or decentralized in relation to task characteristics is associated with several perceived performance dimensions. Butler [12] investigated the stability of online communities in terms of membership loss and membership gain, both of which affect the form of network-based coordination. Our study extends this line of research by exploring the ways in which such coordination structures are reconfigured following membership loss. Based on over 2.6 million postings extracted from 600 Usenet groups, Jones et al. [39] found that members of online communities tend to stop their active participation as the overloading of mass interaction increases. This finding suggests that as the number of participants increases, the level of activity of existing online members decreases. Finally, Oh and Jeon [55] demonstrated that the stability and integrity of online open source communities are influenced by the herding propensity of their members. They argued that the herding behavior of online community participants in terms of their membership decisions could significantly alter the structure of the community network through which they communicate and exchange knowledge. Building on these studies, we propose a research framework by which one can identify various ontological structures of IPNs and explore their inherent strengths under conditions of organizational restructuring.

## Organizational Downsizing

Because of the industrial and economic importance of downsizing and structural redesign, as well as their obvious impact on the fabric of society, a significant body of literature has tapped into a variety of issues related to these phenomena. Typical topics include antecedents [11, 30] and consequences of corporate downsizing [14], the process of an effective job layoff plan [22, 30], the psychological effects of layoffs on remaining employees [10], and the impact of staff reduction on the structure of social networks [62].

When organizational restructuring takes place in the form of downsizing, workload transfers from laid-off employees to surviving employees are almost inevitable. Although IT and other communication mechanisms may replace laid-off employees to a certain extent by facilitating coordination and control among the various organizational components [58], a large portion of tasks will likely be redistributed to the “survivors” who remain in the company [48]. Consequently, the change in workforce composition may require a fine-tuning of work processes and repartitioning of workloads, and as a result, the volume and nature of survivors’ job responsibilities will change [10, 30]. Although much has been written about the consequences of downsizing, its impact on information processing among organizational members has been relatively ignored, especially in regard to those who are linked and highly dependent on IT for communication and information processing. To address this gap, this study approaches the issue from the perspective of IPN-based coordination.

## Ontological Structures of IPNs

IN THE LITERATURE, NETWORK STRUCTURE has been generally defined as “the arrangement of the differentiated elements that can be recognized as the patterned flows of information in a communication network” [61, p. 82]. Network structures are physically manifest conduits of coordination that illustrate specific patterns of communication and information processing [53]. Several studies (e.g., [1, 55]) suggest that the structure of coordination can vary in response to different internal and external uncertainties. Similar to the characteristics observed in traditional organizational designs, the structures of IPNs manifest either centralized or decentralized formations [1]. Variations in degree of centralization suggest different levels of efficiency and efficacy embedded in the management of information-processing requirements. Based on the literature on network theory (e.g., [2]), we further decompose each structure into two categories (see Figure 1). For example, random and small-world network structures are classified as decentralized IPN designs, whereas MSF and HSF or Barabasi structures represent centralized forms of IPN. We offer detailed descriptions of these classifications and delineate the unique characteristics of each IPN based on the discussion of Dorogovtsev and Mendes [25].

Two important characteristics of network-based information processing are described in order to distinguish one type of structure from another. One of the most obvious and widely discussed characteristics of networks is the probability that a node (i.e., employee) will have k connections. This is usually denoted as P(k), which can also depend on the total number of nodes, N, and the total number of edges (connections), M. If P(k) is highly peaked at a single finite value,<sup>3</sup> almost all the nodes will have approximately the same number of “neighbors.” Hence, in this case the network is homogeneous and decentralized. In contrast, if P(k) has no obvious peak, then the number of connections will vary widely from node to node, leading to a heterogeneous and centralized structure. In addition, if there exists a relatively small number of nodes that hog large chunks of connections, then the information-processing structure is considered centralized. Therefore, the heterogeneity or homogeneity of network structures depends on the distribution of connections, which has significant implications for effective information processing.

![](/api/attachments/EDWUWJ32/fulltext/images/eed35ea71288bd7667edb5f1a4084b8ad0980548e548925b832c10a9229ad0e2.jpg)  
Figure 1. A Topology of Information-Processing Networks

## Decentralized Networks

## Random Structure

In the early 1960s, Erdos and Renyi [27] introduced, based on graph theory, random network models in which node connections are evenly distributed and no single node dominates all the connections (see Figure 2a). In their theoretical derivation, regardless of the complexity of the network, all nodes are roughly equal in terms of their importance in a given network. In this network structure, nodes are distributed according to a Poisson distribution, which results in small path lengths and sparse concentrations.

Theoretically, there are two types of random coordination structures—equilibrium and nonequilibrium. The nonequilibrium random network refers to a growing network in which nodes and edges are simultaneously added. Consider the growth process in which nodes are added to an existing network at regular time intervals. Each new node is then randomly connected to several existing nodes. On the surface, this process should result in a random network in the sense that the connections are distributed according to a Poisson distribution. However, this may not be the case when older nodes accumulate more nodes than the newer ones, because they have had more opportunity to “get connected.” Ultimately, this pattern of growth results in an exponential type of edge distribution P(k) \~ exp(–ak), in which the coefficient a depends on the average number of connections per node. An equilibrium (static) situation can be reached when growth stops (i.e., the number of nodes and edges are fixed) and random “rewiring” takes over. When sufficient random rewiring has taken place, then the distinction between newer and older nodes disappears and the distribution of edges becomes Poissonian. As will be explained below, in our simulation, either of these situations can occur in both the formation of an initial IPN structure and in the reconnection of nodes following a downsizing episode. In the equilibrium random network, it is well known that edge distribution follows the Poissonian form:

(a) Random Coordination  
(b) Small-World Coordination  
![](/api/attachments/EDWUWJ32/fulltext/images/e22dd377711bead2c2c80d4754c28c47482723359c772acae7768235abd19a2a.jpg)  
Figure 2. Four Types of Information-Processing Networks

$$
P (k) = e ^ {- <   k >} <   k > ^ {k} / k!\tag{1}
$$

where <k> is the average number of connections per node [27]. For this informationprocessing design, the clustering coefficient is also easy to determine. Because, by definition, there is no correlation in the connection of any two given nodes in this type of network, the clustering coefficient, or the probability that A and B are connected to each other when they are both connected to C, is simply given by the ratio of the total number of edges M and all possible connections between N nodes:

$$
c = M / [ N (N - 1) / 2 ].\tag{2}
$$

Although this information-processing structure may not be as common as other forms, it can be seen in a purely decentralized structure in which all employees within the organization communicate laterally, process a fairly similar amount of information, and have an equal share of responsibility (Table 1). Hinds and Kiesler [37] argue that technical workers (e.g., software engineers) rely extensively on lateral communication because of the nature of the work they perform and the way they are organized. Similarly, Ahuja and Carley [1] posit that nonroutine tasks can be better performed through lateral communication and under the nonhierarchical coordination form. These random network designs may therefore be more suitable for knowledge-intensive industries, such as biotechnology, software engineering, R&D, and consulting [46], in which people rely heavily on lateral communication and information processing for collaborative tasks.

## Small-World Structure

During the late 1960s, Stanley Milgram (e.g., [68]) conducted an interesting experiment that uncovered some intriguing results concerning the characteristics of “human networks.” The results showed that it may only take six intercessors to link all the people on earth. Terms such as small-world networks or six degrees of separation are used metaphorically to refer to the close proximity of all the human nodes on the planet. More recently, Watts and Strogatz [74] made a crucial discovery regarding the theoretical characteristics of small-world networks. They demonstrated that smallworld networks fall into a category between a regular network and a random network with respect to their degree of randomness. On one hand, each node in a small-world structure is embedded in a local cluster, and thus the small-world network possesses a higher clustering coefficient than does the random network (see Figure 2b). On the other hand, short paths that directly connect two nodes located spatially distant from each other, a characteristic typically seen in random networks, are also present in small-world networks. For example, an employee in the sales department can easily coordinate with someone in the production department (Figure 2). These shortcuts provide easy access to most of the nodes in the network, while local clustering tends to foster reliable accessibility [75]. In terms of degree of centralization, small-world networks are more centralized than random networks due to the high number of local clusters, but not at the level inherent to centralized networks.

This type of network structure can represent an efficient form of IPN, especially in situations in which employees use IT to work closely together as team members. Characteristically, these information-processing archetypes are similar in spirit to “organic” or “matrix” type structures [19] in that they allow both autonomy and redundancy in task design. However, small-world networks as information-processing structures are not as constraining as traditional mechanical designs due to their decentralized, lateral, and flat design (see Figure 2b). Moreover, this information-processing pattern allows liaison devices to connect across different groups, similar to the traditional “adhocracy” structure [47] that aims to encourage mutual adjustment and collaboration among members. Typically, a small-world network can be formed either by randomly rewiring a portion of an existing regular network [74] or attaching each new node to a “neighborhood” that already exists. A network formed in the first manner would resemble an adhocracy, whereas a network formed in the second manner would consist of concentrated neighborhoods with only a few bridges between the neighborhoods.

<table><tr><td colspan="4">Table 1. The Network Structures and Organizational Contexts</td></tr><tr><td>Network structure</td><td>Network characteristics</td><td>Organizational contexts</td><td>Examples</td></tr><tr><td>Random network</td><td>Many distant connections between nodes (cross-cut moves)Shortcuts to allow messages to pass quickly</td><td>Shortcuts to find target specialtyLong-distance collaborationKnowledge businessesDriven by information, network technologyCoordination of knowledgeSimilar to “cellular organization” [46]</td><td>Knowledge-intensive biotechnology firmsConsulting, softwareVirtual teamsSmall-sized Internet start-up firmsNetworked expert groups</td></tr><tr><td>Small world</td><td>Short connection between nodesLocal clusteringMultiple redundant edges, pathways</td><td>Team based, autonomic“Organic” structure (e.g., flat, decentralized)Liaison to connect different teamsCombination of expertise of market and function (matrix)</td><td>AdhocracyMatrix organization [19, 47]</td></tr><tr><td>Moderate scale free</td><td>Local centralized hubsLess centralized cliquesLower centralization</td><td>Multiple cliquesMature and professional groupsTechnocrats</td><td>Law firmsUniversitiesProfessional bureaucracies</td></tr><tr><td>Barabasi</td><td>Highly centralized cliquesHigh centrality of connectionsDirect supervision</td><td>Strong command base, efficientMechanistic (simpler) structureYoung, emerging organization</td><td>Entrepreneurial organizationsR&amp;D centers with a few strong leaders</td></tr></table>

## Centralized Networks

## Scale-Free Structure

This study considers two types of scale-free structures—moderate and high. These two structures differ in terms of their degree of centrality—MSF and HSF or Barabasi. Barabasi structures exhibit a much higher level of centrality than do MSF structures (see Figures 2c and 2d). Unlike decentralized networks, these centralized networks form a stratified structure in which the node connections are inhomogeneously distributed and concentrated on certain key nodes. In contrast to random or small-world networks, in which each node has a similar degree of importance, these hub nodes serve as primary information conduits that carry much higher importance in the network than do regular nodes. Interestingly, the scale-free network promotes a cumulative advantage, through which key nodes attract new nodes in large numbers [16]. The idea underlying this preferential attachment phenomenon stems from the “Matthew effect,” in which success breeds success [44]. Barabasi [3] also observes a similar trend, in which 80 percent of all World Wide Web connections are “occupied” by only 20 percent of “hub” Web sites. Mathematically, a scale-free network is defined by its power law connection probability

$$
P (k) = C k ^ {- \gamma},\tag{3}
$$

where C is the normalization constant that depends on the minimum and the maximum number of nodes allowed. The name scale free derives from the fact that in such a power law function, any portion of the function looks exactly the same as the whole function, except for the overall normalization constant. This is particularly apparent in a log-log plot, where the plot of P(k) is a straight line with a slope of –γ.

In general, the majority of nodes in such network structures have a small number of connections, similar to exponential distribution. What is different in the case of scale-free networks, however, is the nonnegligible probability that a node will possess a large number of connections. Therefore, in a large scale-free network, the central nodes are directly connected to a large portion of the whole population. The exponent γ is a parameter that controls what portion of the nodes in the network can be regarded as central nodes. For a small γ whose value is much lower than 1, P(k) does not change noticeably as k changes. The existence of central nodes for a small γ is therefore not important. In nature and human society alike, the typical range for γ is between about 1.5 and 4.

As illustrated earlier, we constructed and analyzed two scale-free structures—MSF (γ = 2) and Barabasi (γ = 2.7). The degrees of γ are determined by the number of nodes and connections employed in the simulation. Because the MSF network design integrates local centralized hubs, organizations with specialty-based expert groups, such as universities, hospitals, and law firms, may use this type of IPN (Table 1). These organizations represent local cliques centering on elite professionals, and are usually less standardized and less centralized than administrative bureaucracies. The Barabasi network represents a form of highly centralized scale-free network, showing a power law distribution much higher than that seen in a typical scale-free network. This type of IPN is subject to the preferential attachment effect, in which the idea that “the rich get richer” applies to the connection of new nodes to existing ones. In practice, this type of structure is likely to be found in companies in which a few key individuals dominate most communication and information-processing activities. These key nodes can be considered the leaders of each unit, whose responsibilities include overseeing all work processes, and exchanging and distributing all the information required by their functional areas. Similar design structures can be observed in organizations that are managed via strong commands from key people, such as entrepreneurs. Important decisions will be highly dependent upon communication with these key people. This type of coordination is therefore characterized by a centralized authority who oversees and manages the entire operation by means of direct supervision and control. Many small-sized, less-established companies with a low level of formalization (i.e., entrepreneurial firms) may use this type of information processing until they grow and mature to a point at which differentiation and integration processes become necessary.

Figure 2 is a schematic representation of the four types of IPN structures that exist in contemporary organizations. In random and small-world networks, the network connections are generally sparse and relatively evenly distributed, whereas in centralized networks (particularly in Barabasi networks), only a few nodes dominate a significant portion of all the information connections. It should be noted that the goal of this study is not to empirically validate in which organizations or contexts each IPN structure tends to be observed but rather to conceptually articulate various ontological forms of network structures and the stability of each structure in the event of downsizing.

## Organizational Restructuring and IPNs

THERE HAS BEEN MUCH ANECDOTAL EVIDENCE demonstrating the perils of organizational shrinkage [66]. However, most scholarly literature thus far has focused mainly on the consequences of downsizing at the individual level (e.g., psychological effects [such as anxiety, depression, or cynicism] of downsizing on survivors who remain at the firm). Through the network framework, we provide a different perspective on the effects of downsizing by investigating, at the network level, the changes occurring in IPNs as a result of workforce reduction. If the main objective of downsizing is not to reduce output but rather to contain costs and improve organizational efficiencies through enhancement of employees’ work productivity, then surviving employees can be significantly affected by such organizational interventions. Because fewer employees remain to do the same amount of work, management must reallocate resources and work processes, forcing the surviving employees to process or transfer higher amounts of information [13]. Kozlowski et al. [41] noted that when workforce reduction occurs, those who have survived tend to experience “burnout” as their workload typically doubles or triples. This burnout through increased workload is the particular situation on which we focus in this paper.

For any given coordination structure, there is a corresponding information network similar to the one shown in Figure 3. Each person in this coordination design is an information conduit. The importance of a person’s position in the IPN can be quantified by various measures, such as the number of connections and the degree of “betweenness.” In any well-functioning IPN, the importance of a person should be well within his or her capacity to deal with the demands of the position (Figure 3a). When the coordination network is downsized, the information paths connecting the downsized nodes must be rerouted to the surviving members of the coordination design. For example, when $N _ { _ 1 }$ is laid off and $N _ { _ 2 }$ takes over the tasks previously performed by $N _ { \mathrm { { } _ { 1 } } } ,$ the communication and information-processing structure will be shifted, resulting in a network similar to Figure 3b. This reorganization is likely to change the structure of the coordination network, as well as the importance of various nodes. If the newly acquired importance is within a person’s abilities, then he or she will still function adequately and the connections will be kept “alive.”

In contrast, if the newly acquired importance in terms of information processing exceeds a person’s capacity, then “burnout” may result, and the person will do the minimum required as an information conduit. This, in turn, can lead to a cascading failure, much like the failure of an overloaded electric power grid. The connections that pass through a burned-out node will have difficulty properly carrying or processing information. This will then provoke another round of rerouting and another shift in the relative importance of various nodes. In turn, this can lead to another bout of burnouts, which causes another rerouting cycle. This iteration scenario may not be seen or detected within a company over a short period of time, but it is more likely to occur over a long period. In cases in which downsizing is a recurring phenomenon within the company, the probability that this vicious cycle will occur is not negligible. When this process of rerouting and burnout eventually terminates, the IPN will still be functioning, but on a much smaller scale. If this process does not terminate, then eventually the outcome will be a totally fractured IPN in which no passing of information between nodes is possible. Assuming that the vicious cycle of downsizing does occur, we examine whether IPN structures (centralized or decentralized) matter in terms of reducing the damage created by the vicious cycle.

We also considered two alternative mechanisms by which the nodes (i.e., surviving employees) may be reconnected in the occurrence of workforce shrinkage. The two reconnection modes can be construed implicitly as either “planned” (preferential) or “unplanned” (random) tactics [1]. Some downsizing projects may be well thought out, fully planned, and smoothly executed over a long-term time horizon, whereas others may take place abruptly and in an unplanned manner, primarily in the form of a “discontinuous change” [30] as a response to rapid market shifts. Through the use of the preferential attachment mechanism—as observed in centralized coordination structures—the tasks performed by those dismissed prior to downsizing are likely to be reassigned to the nodes with maximum information-processing capacity. Conversely, when firms are not well prepared for downsizing, they may not know the most productive way of reconnecting the “detached wires,” and hence they may arbitrarily reassign them to existing nodes. Below are propositions that are empirically tested through carefully designed computer simulations, which will be described in the next section.

![](/api/attachments/EDWUWJ32/fulltext/images/d978b1c12fdd3c66666c031dd303f7aab43f154bf2e9f9edcb27127b7858e1d1.jpg)  
Figure 3. Reallocation of Workload After Downsizing

Proposition 1: Downsizing influences employee efficiency and integrity of the IPN.

Proposition 2: The structure of the IPN mediates the impact of downsizing on employees’ efficiency and network integrity.

Proposition 3: The reconnection strategy following downsizing (i.e., random versus preferential) and the magnitude of downsizing matter with respect to employee efficiency and the integrity of coordination.

## Research Methods

A COMPUTER SIMULATION METHOD WAS CHOSEN as a primary research tool to answer the underlying questions at hand for several reasons. First, computer simulation is a robust method that provides a holistic approach to the analysis of a real-world situation [65]. Such controlled experimental designs enable us to assess the patterns through which IPNs evolve and how the overall performance of each structure changes in the event of downsizing. Second, simulation modeling offers flexibility and robustness in terms of validating various aspects of theoretical propositions. In particular, computer simulations have been considered suitable tools for understanding the details of complex network properties [15].

To carry out the simulation, it is crucial that we accurately quantify the importance of a position as well as the skills of the individual holding the position within the structure of the IPN. Many traditional measures are used to assess the importance of a node in a given network, including number of connections and various betweenness measures such as geodesics and flow betweenness [71]. Each of these measures has its own strengths and weaknesses in cases in which the information passed between two nodes does not necessarily follow a set pattern. In this study, we use a recently proposed measure called “random walk betweenness,” which remedies some of the shortcomings of previous betweenness measures [51]. Until recently, the most popular betweenness measure was geodesic betweenness, which is defined as the ratio of the number of geodesics (i.e., the shortest path between two nodes in a given network) that pass through a given node to the number of all possible pairs. This measure is generally a legitimate indicator of the importance of a node, except when there are nearly geodesic paths that could also be potentially important. Random walk betweenness, in contrast, is illustrated as follows: suppose that every node in the IPN sends a message to everyone else. Further, suppose that each message knows only its destination and does not have any information on how to get there. Then each message has to perform random walks through the coordination network until it finds the destination. In this respect, “random walk betweenness” can be defined as the number of times that the message passes through i on its journey, averaged over a large number of trials of the random walk [50, 51]. It can be shown that this result is equivalent to the sum of currents that pass through each node in an equal-strength resistor network. Hence, the tools of circuit analysis (e.g., [7]) can be directly used to calculate random walk betweenness once the adjacency matrix is given.

Geodesic betweenness and random walk betweenness are well correlated as shown by Newman [51]; however, random walk betweenness is more robust in the sense that the nearly geodesic paths that should be important in any real-world situation are also correctly accounted for. For this reason, therefore, we use random walk betweenness to assess the importance of a given node (person) in IPN, as well as to quantify the skills of the person.

## Network Simulation Procedures

As noted earlier, this study considers four ontological IPN structures that exist in various organizations—random, small world, MSF, and Barabasi. To construct a random IPN structure, we first determined the number of nodes and the total number of connections. In our case, we chose 100 nodes and 200 connections (an average of four neighbors per node). This size is considered “sufficiently” large to reflect real-world situations. We then randomly chose a “not-yet-connected” pair 200 times and connected them with a link. The resulting distribution of the number of neighbors is known to be a Poisson distribution, as illustrated earlier. It peaked at four by construction, and most nodes fell within the range of two to six. It is worth noting that a node with a large number of neighbors is exponentially rare in this type of IPN structure. The small-world network was constructed as follows: similar to the procedures specified in designing random networks, we first constructed a regular network of 100 nodes arranging it in a $1 0 \times 1 0$ square form. To make all the nodes retain the same number of connections, the square’s opposing edges are connected to each other. In this way, all nodes have four connections. We then randomly removed 20 percent of the connections and randomly rewired the same number of connections. Compared to the regular network, these random connections (“shortcuts”) reduce the average distance between pairs of nodes, for example, from 5.05 (regular network) to 3.71 (small-world network) in our simulation.

To construct an MSF network with $\gamma = 2$ , we first assigned the number of connections to each node according to the $\gamma = 2$ distribution and connected the nodes so that no loose ends remained. More specifically, similar to the procedures described earlier, we started with 100 nodes. To each node, we first assigned the number of neighbors according to $P ( k )$ so that the total number of connections was approximately 200. Then, starting from the most connected node, random connections between the nodes were made until each node was connected to the assigned number of neighbors. Finally, the Barabasi network was constructed through the use of a simple set of “the rich get richer” rules. The preferential attachment principle (an instance of the Matthew effect) was used to construct the Barabasi network. Specifically, we adhered to the following rules [2] at each time step: (1) with the probability $p ,$ we randomly picked an existing node and linked it to another existing node with the probability that it is proportional to the number of neighbors (preferential attachment); (2) with the probability q, we randomly relinked an existing connection; and (3) with the probability of $1 - p - q$ , we added a node with m connections to the existing nodes, again attaching preferentially. The result, with $p = 0 . 1$ and $q = 0 . 3$ , was a Barabasi network with $\gamma = 2 . 7$

The simulation started at $t = 0$ by constructing one of the four networks described above. The random walk betweenness for the initial network configuration was then calculated using the tools of circuit analysis as described by Newman [51]. Assuming that such a network is well functioning, we set the ability (capacity) of each node to be 1.5 times its initial betweenness value. $\mathrm { A t } \ t = 1$ , we then downsized the coordination network by removing nodes from the bottom of the betweenness ranking (i.e., employees who do not add much value to the company). The links that the removed nodes had occupied were then reconnected to the existing nodes either preferentially (i.e., “the rich get richer”) or randomly (this reconnection strategy is discussed below). The betweenness values were then recalculated. $\mathbf { A } \mathbf { t } \ t = 2$ , the first stage of burnout sweeps through the existing clusters. Any node whose betweenness exceeded its capacity to handle it would burn out and thus be unable to efficiently coordinate work processes. In contrast to downsizing, the links of a burned-out node were not reattached to the existing nodes, because a burned-out node is still technically a part of an existing network. After the first stage of burnout, we again calculated betweenness, and then repeated the burnout procedure until either no more burnout occurred or every node was burned out (see the Appendix for detailed simulation procedures).

## Performance Measures

Two performance measures (i.e., employee efficiency and network integrity) were employed to analyze the simulation-generated data. Employee efficiency, measured by workload performed divided by his or her capacity, indicates the extent to which an employee handles information-processing workload vis-à-vis his or her capacity. In general, a low number (say, below 0.5) indicates that a worker is not performing at his or her best, while a high number (say, over 1) suggests that a person is exceeding his or her workload capacity. In other words, low numbers indicate slack resources, while high numbers indicate resource shortages and potential employee burnouts. The other measure adopted—network integrity—shows the level of integrity of the IPN. A high ratio suggests that nodes within the IPN are well connected to each other, while a low ratio suggests fragmentation. Therefore, the higher the ratio of this measure, the greater the level of integrity of the IPN. It should be noted that while employee efficiency measures the effect of downsizing from an individual perspective, the integrity variable identifies its impact on the network as a whole. Therefore, the two results should be interpreted as complementary rather than competing.

## Moderating Variables

To reflect real-world situations more precisely, we added two moderating variables that might influence the results. The first represents the scale of downsizing, which was divided into two categories—“light” (10 percent) and “heavy” (40 percent) downsizing. It is reasonable to assume that the magnitude of downsizing significantly influences the restructuring outcome. Typically, a light downsizing strategy is driven by a desire to achieve “incremental benefits,” such as operational efficiencies without high risk; a heavy downsizing strategy, in contrast, is intended to refine entire key organizational components such as strategy, mission, and structure [30]. It is important to note that because downsizing is likely to be a recurring phenomenon [64], it is necessary to understand its magnitude over a longer time horizon.

Finally, as discussed earlier, we considered two options a company might have in terms of reconnecting the “broken” nodes that resulted from downsizing (e.g., planned and unplanned reconnection strategies). With regard to specific downsizing decision rules, we assumed that companies lay off “rummies” who are the least efficient and underperform in their assigned tasks (i.e., those who have low value based on random walk betweenness) [66].

## Results and Discussion

AS EXPLAINED ABOVE, THE SIMULATION MODEL consists of several variables: (1) four network designs (i.e., random, small world, MSF, and Barabasi), (2) two moderating variables (i.e., the downsizing magnitude and reconnection tactics), and (3) two performance measures (i.e., employee efficiency and network integrity). We first show the results as they pertain to employee efficiency and then explain how network structure affects the stability of an IPN in the event of downsizing.

## Reconnection Strategy and Employee Efficiency

The simulation test yielded mixed results with regard to the impact of workforce reduction on the performance of an IPN. Figures 4a and 4b show that when a company undergoes light downsizing in which only a small fraction of employees (in this case, 10 percent) are forced to leave, an employee’s average work efficiency, as measured by workload/capacity, increases initially and then remains constant over time in centralized IPN structures. When light downsizing occurs, adverse effects (i.e., burnouts) appear to be less severe in centralized network structures. However, light downsizing seems to bring about unintended negative consequences for decentralized IPNs. Although only small reductions in work productivity were observed for the random IPN, the small-world IPN suffered from a sharp decrease in work productivity immediately following downsizing. In addition, in the event of light downsizing, centralized IPN structures perform in a manner superior to that of decentralized counterparts in terms of operational efficiency improvement.

We observed a certain peculiarity in the small-world structure in the presence of light downsizing. Recall that the measure “betweenness” reflects the degree of importance of the node under consideration. Consider a situation in which a certain number of original nodes (employees) are taken out (laid off). The issue is now whether reconnection increases the importance of each remaining node. In a random structure, all nodes are considered equally important in conveying information from one end of the network to the other. If, however, we rip out 20 percent of them and reconnect the “wires” in a more or less random order to create a “small world,” the importance of the existing nodes that are connected to the rewired shortcuts rises substantially. Interestingly, the importance of the rest of the nodes in the IPN actually goes down, because in a relative sense, they are no longer as important as before in conveying information between nodes. Hence, if the number of reconnected nodes is much smaller than the number of not-reconnected nodes, average efficiency may diminish. A smallworld IPN, in this regard, is reasonably close to a regular network. We believe that this is one of the main reasons for the poor performance observed in the small-world structure under conditions of light downsizing.

One explanation for the superior performance of centralized structures is that they are inherently less ambiguous in determining the relative importance of actors. Therefore, the elimination of the least important actors (“rummies”) would clearly enhance the overall work efficiency of employees in organizations. In random or small-world structures, in contrast, it is not as clear who are the most important actors, because degree and betweenness are distributed more or less evenly. In other words, managers are unsure as to whom they should dismiss, given that all individuals have more or less the same value to the organization. Consequently, eliminating some of the employees is not likely to result in an improvement in efficiency. Even worse, downsizing and reconnecting a small number of nodes in an IPN can make overall efficiency go down, because a small number of nodes are made more important than others.

(a)  
![](/api/attachments/EDWUWJ32/fulltext/images/f9b0a1981d2c4fc4d7c346f4f6d2047ece27d55aace8761c2ed1e9441a45eb6e.jpg)

(b)  
![](/api/attachments/EDWUWJ32/fulltext/images/3d8a9b35bc7eecc5cfdbc678a9656273e266a71047b324c165460dd93ca81e7b.jpg)  
(d)

(c)  
![](/api/attachments/EDWUWJ32/fulltext/images/54fc5d3f19667f83326da1d4152f0945248b2b25db7917dc54c3089047e16f0f.jpg)

![](/api/attachments/EDWUWJ32/fulltext/images/58d932f2925fd5fd94f3f0d82cde16d19f7bdc1dbdafd72603d0ca1ea94d23ed.jpg)  
Figure 4. Results of the Simulation (Dependent Variable: Employee Efficiency)

In contrast to light downsizing, heavy downsizing initially brings about a striking performance improvement in the short term, but results in rapid performance decline over time. This result may not be surprising given that burnouts are likely to be provoked in the event of a severe workforce reduction. What is intriguing, though, is that heavy downsizing can in fact be more effective than light downsizing in maximizing employee efficiency up to a certain point, but will eventually lead to substantial performance drops in certain IPN structures once the level of burnouts passes a threshold point. Further, while random and MSF structures appear to be stable over time, the Barabasi structure, the most centralized form of the four, is extremely vulnerable to burnout: it is the superior structure in terms of eliciting maximum worker efficiencies during the initial stage, but it loses efficiency dramatically once the peak point is passed. Based on these results, this type of IPN structure may fail to survive under conditions of repeated downsizing.

Rational intuition suggests that if a substantial number of nodes are eliminated concurrently, the central issue becomes the possibility of overload of the central nodes. In the event of heavy downsizing, the central nodes will burn out easily simply because their importance and responsibility become much greater as the density of the connections rapidly increases. If the downsizing percentage is small, the central nodes can, without much difficulty, accommodate the increase in density. However, when the downsizing percentage becomes large, the central nodes can no longer handle the increase in the number of rewired connections. In this respect, a highly centralized network is a risky form of IPN, because when a centralized node burns out, its connections are not rerouted to other nodes, and the IPN may quickly disintegrate. In contrast, when an IPN does not contain one, there is a higher likelihood of structural survival.

Barabasi structures are characteristically unstable when the central nodes, which dominate most information processing, suffer from burnout. When none of the key hubs are active, the entire IPN structure will eventually be unable to function and cease the processing of information. Interestingly, such a radical “phase transition” does not occur in MSF structures, which are characterized by less heterogeneously distributed coordination connections. This contrasting result suggests that degree of centrality plays a significant role in determining burnout rates. IPN structures with high centralization are subject to burnout of members and to high levels of vulnerability under conditions of downsizing, while IPN structures with low centralization are better able to maintain stability and are less adversely affected by downsizing.

We also consider a downsizing situation in which firms reassign workloads to members in an arbitrary or unplanned manner. As described earlier, this scenario could occur when management implements downsizing with no specific plan during the course of the event. This situation is somewhat analogous to the creation of a random network as explained above. This scenario results in outcomes similar to those found in the case of preferential attachment, except for MSF structures. When heavy downsizing occurs, similar to Barabasi structures, MSF structures show highly volatile shifts over time from high to low efficiency. This suggests that even a low degree of centrality can result in disruptive upheaval. Therefore, decentralized IPN structures may be more stable than centralized structures and more able to cope with situations of understaffing and burnout when unplanned downsizing with an arbitrary reassignment of work processes is implemented.

## Reconnection Strategy and Network Integrity

Network integrity was employed as an alternative performance measure to test the extent to which downsizing fragments the unity of IPNs. The integrity of the IPN is necessary to maintain seamless information flow across the members of an organization. One of the critical effects of downsizing is that it not only eliminates a particular employee but also eliminates the informational conduit attached to that person. As a result, the elimination of an employee makes a survivor who is tightly linked to that person less efficient and productive in an organization. Figure 5 shows that when light downsizing occurs, all four coordination structures initially suffer from reduced network integrity, regardless of the reconnection strategy adopted; however, all stabilize over time. Interestingly, the results suggest that even a small reduction in workforce (say, 10 percent) can result in a large degree of fragmentation and loss of network integrity (say, 30 percent), as seen in Figure 5. However, due to their high degree of centrality, centralized IPN structures show superiority in maintaining cohesiveness when compared to their decentralized counterparts. In contrast, when firms implement heavy downsizing, network integrity declines rapidly, even in the early period of downsizing, and worsens as the incidence of burnout increases. Similar to the results pertaining to efficiency illustrated in Figures 4b and 4d, Barabasi–Albert structures are most volatile in the presence of burnouts.

(a)  
![](/api/attachments/EDWUWJ32/fulltext/images/4227b1e29e3c188a77782d93d7d834ea4c585898854d4b5304c154041a411265.jpg)  
(c)

(b)  
![](/api/attachments/EDWUWJ32/fulltext/images/2c2fdb7e20005cfda593135a570a39a77ac03678be89a8ae166d1c3dbf0a82aa.jpg)  
(d)

![](/api/attachments/EDWUWJ32/fulltext/images/ef74bbec0087102b5e3958cb9b39c56e402bdffdff177986d9220e1b25fbeab6.jpg)

![](/api/attachments/EDWUWJ32/fulltext/images/f64e678c1d1afd7045acc6ca910a30c978a21cb908b0b923b2ca1794fe72eff2.jpg)  
Figure 5. Results of the Simulation (Dependent Variable: Network Integrity)

When random assignment, rather than preferential attachment, was used as a reconnecting strategy, we found significantly different results among the four types of IPN structures in terms of network integrity in response to downsizing. First, regardless of IPN type, random reconnection resulted in much higher coordination fragmentation than preferential attachment for a given level of downsizing. The fact that random assignment tends to evenly redistribute the connections, irrespective of the capability of the nodes, could be the explanation for this negative outcome. When a less-efficient node takes on the additional workload, it will readily experience burnout and become nonfunctional. This suggests that managers should have a well-orchestrated plan for redistributing work processes within the IPN structure, and that this plan should be specified prior to downsizing; otherwise, there is a risk of significant disconnection in IPNs. Finally, when firms decide to implement heavy downsizing, they should be aware that centralized IPN structures are less robust than decentralized structures in terms of resisting network fragmentation.

Table 2 presents an overall performance comparison between centralized and decentralized IPN structures in the presence of downsizing. It should be noted that this comparison is made based on the two measures employed in the evaluation. Determining which IPN structure performs better in light downsizing is less complex, as the results clearly show striking differences regardless of the reconnection strategies involved. However, this is not the case for heavy downsizing, in which superior performance was observed in centralized IPN structures during early stages; however, these structures tend to be subject to a form of “phase transition” in which performance drops rapidly as the degree of burnout increases. Given that maintaining stability of IPN structures is very crucial, such erratic changes may be considered risky and undesirable.

These simulation results are in line with previous studies that posit that massive and unplanned layoffs lead to poor performance due to severe disruptions in work flow [54], communication difficulties [11], loss of knowledge and experience [20], and the lack of corrective feedback mechanisms [28]. For example, Foster [29] found that 75 percent of the firms that underwent heavy downsizing (33 percent or more) experienced a severe decline in profitability and sales. Similarly, more than half of the Fortune 1000 corporations that heavily downsized white-collar workers in the early 1990s reported a substantial drop in productivity [36].

## Implications and Future Research

THE RESULTS OF THE SIMULATION LEND SOME SUPPORT to the theory that light downsizing can indeed help firms improve operational efficiencies, but not all organizations may enjoy such benefits. IPNs with a small-world structure in place, for example, can experience slight performance degradation as a result of light downsizing. This adverse effect is, in part, brought about by an inefficient work-process redistribution strategy. When redesigning work process and information flow, managers should take into account the possibility that the importance of employees can change as the nature and volume of their job responsibilities change. As such, they should find an equilibrium at which the node redistribution will result in positive outcomes.

It is also worthwhile to note that operational efficiency can be improved with light downsizing, but potentially at the expense of network integrity, which reflects the degree of coordination. Our results suggest that although the impact may vary from structure to structure, a 10 percent reduction in workforce can lead to a reduction in information-processing-related coordination as high as 30 percent. Although the coordination problems resulting from network fragmentation may pose a less significant threat to the operation in the short term, companies may suffer from hidden administrative costs that arise from suboptimal information flow in the long term.

<table><tr><td rowspan="2">Performance measure</td><td colspan="4">Reconnection strategy</td></tr><tr><td colspan="2">Preferential attachment</td><td colspan="2">Random assignment</td></tr><tr><td>Downsizing magnitude</td><td>Light downsizing</td><td>Heavy downsizing</td><td>Light downsizing</td><td>Heavy downsizing</td></tr><tr><td>Worker efficiency</td><td>Centralized &gt; decentralized(BA &gt; MSF &gt; RA &gt; SW)</td><td>Decentralized &gt; centralized(RA &gt; SW &gt; MSF &gt; BA)</td><td>Centralized &gt; decentralized(BA &gt; MSF &gt; RA &gt; SW)</td><td>Decentralized &gt; centralized(RA &gt; SW &gt; MSF &gt; BA)</td></tr><tr><td>Network integrity</td><td>Centralized &gt; decentralized(BA = MSF &gt; RA &gt; SW)</td><td>Decentralized &gt; centralized(SW &gt; MSF &gt; RA &gt; BA)</td><td>Decentralized &gt; centralized(SW &gt; BA &gt; MSF = RA)</td><td>Decentralized &gt; centralized(SW &gt; RA &gt; BA = MSF)</td></tr><tr><td colspan="5">Notes: BA = Barabasi; MSF = moderate scale free; RA = random; SW = small world.</td></tr></table>

<sub>Summary</sub> <sup>of</sup> <sup>Key</sup> <sup>Findings</sup> <sup>from</sup> <sup>the</sup> <sup>Si</sup>

The results also indicate that although heavy downsizing involving severe job cuts can result in significant operational improvements for certain organizations, it can be difficult to sustain the operational continuity, integrity, and coordination of work processes under such conditions. The simulation shows that the initial performance gain may not last long for certain companies. At the extreme, IPNs in certain organizations may abruptly become dysfunctional within a short period of time, which requires a large-scale refinement and reconfiguration of information-processing protocols. However, regardless of work-process redesign strategies, decentralized IPN structures appear to be more durable under conditions of heavy downsizing. This result does not suggest that firms should implement heavy downsizing when they have a decentralized IPN in place, but rather provides insight into necessary precautions to take in situations wherein heavy downsizing is necessary (such as eroding market share, increased competition, etc.). To minimize any damage that may occur in the aftermath of downsizing, firms should carefully consider, in advance, refining their information-processing patterns in ways that lead to decentralized IPN structures. For instance, prior to downsizing, managers should identify key nodes (employees) who process an extremely large volume of information within the IPN and then redistribute some portion of their work to nodes less actively involved in processing information. Obviously, these key nodes will survive the heavy downsizing, but the redistribution will result in significant differences in terms of operational efficiency and network stability.

Regarding performance variation between centralized and decentralized networks, we found that when firms implement a relatively small scale workforce reduction, centralized IPNs appear to be generally more resilient in terms of hedging against the adverse effects of downsizing (i.e., burnouts), and to better facilitate informationprocessing activities. However, when the downsizing strategy involves massive and severe layoffs, decentralized IPNs are characteristically more robust and provide a stronger safety net by which damage can be kept to a minimum, irrespective of workprocess redesign strategies. We also observed that in the event of light downsizing, network performance is driven by the choice of reconnection strategy: A higher level of network integrity is observed in centralized IPNs when preferential attachment is used as the primary reconnecting mechanism, while decentralized IPNs demonstrate superiority in the case of random reassignment. Therefore, managers should understand the relationship between IPN structures and the effectiveness of reconnection strategies.

The redesign of work processes as reflected in the reconnection of nodes after downsizing is indeed of paramount importance to corporate managers, because it leads to significant differences in outcome. Due to the volatility of the market environment, layoffs must often be implemented in the short term without thorough planning. It is not an easy task to determine whom to dismiss, to whom work should be transferred, and to what extent the work process should be redesigned. In the absence of strategic planning, downsizing can in fact become “dumbsizing” [6]. Our results reveal that managers who arbitrarily employ an unplanned work-process redesign strategy will pay a higher price, especially in the area of coordination, than managers who implement strategies with more systematic planning (Figure 5). Compared to a preferential attachment strategy, an ad hoc workload repartitioning strategy can quickly destroy the coherence of the network and produce negative consequences in the context of heavy downsizing. In summary, the results of the simulation offer several transition methods by which redesign of work processes and redistribution of workloads can be achieved smoothly and at minimal cost.

This study could be extended in several ways. First, future research should be carried out to empirically validate, from the perspective of information processing, the consequences of “broken ties” that result from downsizing. Surveys that contain several performance measures (i.e., delays in work coordination, complaints from customers, level of employee burnouts due to broken ties, etc.) could be used to assess the consequences of downsizing from the information-processing view. Second, in our simulation model, the direction of information flow was not specified. In fact, network studies, including social network analysis, do not often incorporate the specific directions between nodes, especially when dealing with large networks. Considering flow directions in a simulation model requires many assumptions, while making the interpretations of the results quite complicated. Nevertheless, the direction of information flow provides additional details concerning network stability and therefore should be included when analyzing small networks. Finally, we encourage researchers to explore the context in which networks grow instead of shrink through major expansions and acquisitions. This study focuses exclusively on the specific context in which downsizing increases the workload of survivors. It has been acknowledged that many organizations hire new employees following a major downsizing initiative, by which new ties are created [77]. Moreover, mergers and acquisitions have become an important organizational strategy that dramatically changes the patterns of IPNs. Our framework can offer valid insights into such network expansions and provide effective means of creating new ties in ways that result in optimal information processing.

## Conclusion

IN THIS STUDY, WE ASSESSED THE STABILITY AND EFFICIENCY of IPNs in the presence of workforce reduction, and offered a general framework to help improve understanding of the structural integrity and resiliency embedded in each form of IPNs. Although organizational researchers have scrutinized the outcomes of downsizing, one area that has remained relatively unexplored is the impact of organizational restructuring on the efficacy of IPNs. In the midst of organizational shrinkage, the paths through which information and knowledge flow, and the mechanisms through which work processes are designed and redesigned, change dramatically, resulting in a substantial reconfiguration of IPN structures. Our results show that the overall impact of organizational restructuring on the efficiency and integrity of IPNs is determined by a multitude of factors, including the size of the reorganization, the reconnection strategy, and the ontological structure of the information processing itself. In particular, massive layoffs implemented in an unplanned manner could be detrimental to the integrity of IPNs, causing workflow disruptions and coordination difficulties. It is hoped that our study serves as a prelude to the development of a more comprehensive framework by which we can further determine, from the perspective of IPNs, the consequences of organizational restructuring, whether in the form of downsizing or of expansion.

Acknowledgments: Wonseok Oh thanks Fonds de Recherche sur la Société et la Culture (FQRSC 2006-NP-105602) for providing financial support for the completion of this project. Sangyong Jeon is supported in part by the Natural Sciences and Engineering Research Council of Canada and by le Fonds Nature et Technologies of Quebec. He also thanks RIKEN-BNL Center and U.S. Department of Energy (DE-AC02–98CH10886) for providing facilities essential for the completion of this work.

## NOTES

1. Barabasi networks exhibit highly centralized scale-free structures. These network structures are named after the discovery of such structures by Albert and Barabasi [4].

2. In 1997, a fire erupted at Aisin’s facility. Aisin was the sole supplier of valves and brakerelated parts.

3. To a certain extent, the probability P(k) reflects the first moment of the underlying distribution of edges and hence misses important correlation information. One important local correlation measure is the “clustering coefficient,” c, defined as the probability that two nodes are directly connected given that these nodes share a common nearest neighbor. For example, suppose A and B are connected to C. We then ask, what is the probability that A and B are also connected themselves? If this probability is high, then the network is highly cliqued.

## REFERENCES

1. Ahuja, M., and Carley, K. Network structure in virtual organizations. Organization Science, 10, 6 (1999), 741–757.

2. Albert, R., and Barabasi, A. Topology of evolving networks: Local events and universality. Physical Review Letter, 85, 24 (2000), 5234–5237.

3. Barabasi, A.-L. Linked: How Everything Is Connected to Everything Else and What It Means for Business, Science, and Everyday Life. New York: Plume, 2002.

4. Barabasi, A.-L., and Albert, R. Emergence of scaling in random networks. Science, 286 (October 1999), 509–512.

5. Baum, J.A.C.; Rowley, T.J.; and Shipilov, A.V. The small world of Canadian capital markets: Statistical mechanics of investment bank syndicate networks. Canadian Journal of Administrative Sciences, 21, 4 (2004), 307–325.

6. Baumohl, B. When downsizing becomes “dumbsizing.” Time (March 15, 1993), 55.

7. Boylestad, R. Introductory Circuit Analysis. Upper Saddle River, NJ: Prentice Hall, 2002.

8. Braha, D., and Bar-Yam, Y. Information flow structure in large-scale product development organizational networks. Journal of Information Technology, 19, 4 (2004), 234–244.

9. Brass, D.; Galaskiewicz, J.; Greve, H.; and Tsai, W. Taking stock of networks and organizations: A multilevel perspective. Academy of Management Journal, 47, 6 (2004), 795–817.

10. Brockner, J.; Grover, S.; O’Malley, M.; Reed, T.; and Glynn, M. Threat of future layoffs, self-esteem and survivors’ reactions: Evidence from the laboratory and the field. Strategic Management Journal, 14, Special Issue (1993), 153–166.

11. Budros, A. A conceptual framework for analyzing why organizations downsize. Organization Science, 10, 1 (1999), 69–82.

12. Butler, B. Membership size, communication activity, and sustainability: A resource-based model of online social structures. Information Systems Research, 12, 4 (2001), 346–362.

13. Cameron, K.S. Strategies for successful organizational downsizing. Human Resource Management, 33, 2 (1994), 189–211.

14. Cameron, K.S.; Kim, M.U.; and Whetten, D.A. Organizational effects of decline and turbulence. Administrative Science Quarterly, 32, 2 (1987), 222–240.

15. Carley, K. Computational and mathematical organization theory: Perspective and directions. Computational and Mathematical Organization Theory, 1, 1 (1995), 39–56.

16. Cole, J.R., and Cole, S. Social Stratification in Science. Chicago: University of Chicago Press, 1973.

17. Comfort, L.K.; Ko, K.; and Zagorecki, A. Coordination in rapidly evolving disaster response systems: The role of information. American Behavioral Scientist, 48, 3 (2004), 295–313.

18. Cyert, R.M., and March, J.G. A Behavioral Theory of the Firm. Upper Saddle River, NJ: Prentice Hall, 1963.

19. Daft, R.L. Organization Theory and Design, 2d ed. St. Paul, MN: West, 1986.

20. Daugherty, D., and Bowman, E. The effects of organizational downsizing on product innovation. California Management Review, 37, 4 (1995), 28–44.

21. DeSanctis, G., and Jackson, B. Coordination of information technology management: Team-based structures and computer-based communication systems. Journal of Management Information Systems, 10, 4 (Spring 1994), 85–110.

22. DeWitt, R.-L. The structural consequences of downsizing. Organization Science, 4, 1 (1993), 30–40.

23. Dimaggio, P.J., and Powell, W.W. The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. American Sociological Review, 48, 2 (1983), 147–160.

24. Dodds, P.S.; Watts, D.J.; and Sabel, C.F. Information exchange and the robustness of organizational networks. Proceedings of the National Academy of Science, 100, 21 (2003), 12516–12521.

25. Dorogovtsev, S.N., and Mendes, J.F. Evolution of networks. Advances in Physics, 51, 4 (2002), 1079–1187.

26. Drazin, R., and Van de Ven, A.H. Alternative forms of fit in contingency theory. Administrative Science Quarterly, 30, 4 (1985), 514–539.

27. Erdos, P., and Renyi, A. On the evolution of random graphs. Publications of the Mathematical Institute of the Hungarian Academy of Sciences, 5, A (1960), 17–61.

28. Filatotchev, I., and Toms, S. Corporate governance, strategy and survival in a declining industry: A study of UK cotton textile companies. Journal of Management Studies, 40, 4 (2003), 895–920.

29. Foster, K.R. Downsizing: An examination of the consequences of mass layoffs. Journal of Private Enterprise, 17, 2 (2002), 109–130.

30. Freeman, S.J., and Cameron, K. Organizational downsizing: A convergence and reorientation framework. Organization Science, 4, 1 (1993), 10–29.

31. Fulk, J., and DeSanctis, G. Electronic communication and changing organizational forms. Organization Science, 6, 4 (1995), 337–349.

32. Fulk, J., and DeSanctis, G. Articulation of Communication Technology and Organizational Form. London: Sage, 1999.

33. Galbraith, J.R. Organizational design: An information processing view. Interfaces, 4, 3 (1974), 28–36.

34. Griffith, T.; Sawyer, J.; and Neale, M. Virtualness and knowledge in teams: Managing the love triangle of organizations, individuals, and information technology. MIS Quarterly, 27, 2 (2003), 265–287.

35. Hannan, M.T., and Freeman., J.H. The population ecology of organizations. American Journal of Sociology, 82, 5 (1977), 929–964.

36. Henkoff, R. Getting beyond downsizing. Fortune, 10 (January 1994), 58–64.

37. Hinds, P., and Kiesler, S. Communication across boundaries: Work, structure, and use of communication technologies in a large organization. Organization Science, 6, 4 (1995), 373–393.

38. Jarvenpaa, S.L.; Knoll, K.; and Leidner, D.E. Is anybody out there? Antecedents of trust in global virtual teams. Journal of Management Information Systems, 14, 4 (Spring 1998), 29–64.

39. Jones, Q.; Ravid, G.; and Rafaeli, S. Information overload and the message dynamics of online interaction spaces: A theoretical model and empirical exploration. Information Systems Research, 15, 2 (2004), 194–210.

40. Kodama, M. How two Japanese high-tech companies achieved rapid innovation via strategic community networks. Strategy & Leadership, 33, 6 (2005), 39–47.

41. Kozlowski, S.W.; Chao, G.T.; Smith, E.M.; and Hedlund, J. Organizational downsizing: Strategies, interventions, and research implications. In C.L. Cooper and I.T. Robertson (eds.), International Review of Industrial and Organizational Psychology. New York: John Wiley & Sons, 1993, pp. 263–332.

42. Kraut, R.; Steinfield, C.; Chan, A.; Butler, B.; and Hoag, A. Coordination and virtualization: The role of electronic networks and personal relationships. Organization Science, 10, 6 (1999), 722–740.

43. Lin, L., and Kulatilaka, N. Network effects and technology licensing with fixed fee, royalty, and hybrid contracts. Journal of Management Information Systems, 23, 2 (Fall 2006), 91–118.

44. Merton, R. Social Theory and Social Structure. New York: Free Press, 1968.

45. Meyer, J.W., and Rowan, B. Institutional organizations: Formal structure as myth and ceremony. American Journal of Sociology, 83, 2 (1976), 340–363.

46. Miles, R.E.; Snow, C.C.; Mathews, J.A.; Miles, G.; and Coleman, H.J. Organizing in the knowledge age: Anticipating the cellular form. Academy of Management Executive, 11, 4 (1997), 7–24.

47. Mintzberg, H. The Structuring of Organizations. Englewood Cliffs, NJ: Prentice Hall, 1979.

48. Mishra, K.E.; Spreitzer, G.M.; and Mishra, A.K. Preserving employee morale during downsizing. Sloan Management Review, 39, 2 (1998), 83–95.

49. Motter, A.E. Cascade control and defense in complex networks. Physical Review Letter, 93, 098701 (2004), 1–4.

50. Newman, M.E.J. A measure of betweenness centrality based on random walks. Working paper (available at http://arxiv.org/abs/cond-mat/0309045).

51. Newman, M.E.J. Fast algorithm for detecting community structure in networks. Physical Review E, 69, 6 (June 2004), 1–5.

52. Nishiguchi, T., and Beaudet, A. The Toyota group and the Aisin fire. Sloan Management Review, 40, 1 (1998), 49–59.

53. Nohria, N. Is a network perspective a useful way of studying organizations? In N. Nohria and R.G. Eccles (eds.), Networks and Organizations: Structure, Form, and Action. Boston: Harvard Business School Press, 1992, pp. 1–22.

54. Nutt, P.C. Organizational de-development. Journal of Management Studies, 41, 7 (2004), 1083–1103.

55. Oh, W., and Jeon, S. Membership herding and network stability in the open-source community: The Ising perspective. Management Science (forthcoming).

56. Ouchi, W.G. The transmission of control through organizational hierarchy. Academy of Management Journal, 21, 2 (1978), 173–192.

57. Owen-Smith, J., and Powell, W.W. Knowledge networks as channels and conduits: The effects of spillovers in the Boston biotechnology community. Organization Science, 15, 1 (2004), 5–22.

58. Pinsonneault, A., and Kraemer, K. Exploring the role of information technology in organizational downsizing: A tale of two American cities. Organization Science, 13, 2 (2000), 191–208.

59. Porter, M.E. Competitive Advantage: Creating and Sustaining Superior Performance. New York: Free Press, 1985.

60. Rice, R.E. Relating electronic mail use and network structure to R&D work networks and performance. Journal of Management Information Systems, 11, 1 (Summer 1994), 9–30.

61. Rogers, E., and Kincaid, D. Communication Networks: Towards a New Paradigm for Research. New York: Free Press, 1981.

62. Shah, P. Network destruction: The structural implications of downsizing. Academy of Management Journal, 43, 1 (2000), 101–112.

63. Simon, H.A. The New Science of Management Decision. New York: Harper & Row, 1970.

64. Spitzer, T., and Tobia, P. Has cost cutting gone too far. Across the Board, 31, 4 (1994) 54–55.

65. Starbuck, W. Vita contemplativa: Why I stopped trying to understand the real world. Organization Studies, 25, 7 (2004), 1233–1254.

66. Sutton, R.I.; Eisenhardt, K.M.; and Jucker, J.V. Managing organizational decline: Lessons from Atari. Organizational Dynamics, 14, 2 (1986), 17–29.

67. Thompson, J.D. Organizations in Action. New York: McGraw-Hill, 1967.

68. Travers, J., and Milgram, S. An experimental study of the small-world problem. Sociometry, 32, 4 (1969), 425–443.

69. Tushman, M.L. Work characteristics and subunit communication structure: A contingency analysis. Administrative Science Quarterly, 24, 1 (1979), 82–98.

70. Tushman, M.L., and Nadler, D.A. Information processing as an integrating concept in organizational design. Academy of Management Review, 3, 3 (1978), 613–624.

71. Wasserman, S., and Faust, K. Social Network Analysis, Methods and Applications. Cambridge: Cambridge University Press, 1994.

72. Watson Fritz, M.B.; Narasimhan, S.; and Rhee, H. Communication and coordination in the virtual office. Journal of Management Information Systems, 14, 4 (Spring 1998), 7–28.

73. Watts, D.J. Six Degrees: The Science of a Connected Age. New York: W.W. Norton, 2003.

74. Watts, D.J., and Strogatz, S. Collective dynamics of “small-world” networks. Nature, 393, 6684 (June 1998), 440–442.

75. White, D., and Houseman, M. The navigability of strong ties: Small worlds, tie strength, and network topology. Complexity, 8, 1 (2003), 82–86.

76. Wiesenfeld, B.; Raghuram, S.; and Garud, R. Communication patterns as determinants of organizational identification in a virtual organization. Organization Science, 10, 6 (1999), 777–790.

77. Zwass, V., and Veroy, B. Capacity expansion for information flow distribution in multipath computer communication networks. Journal of Management Information Systems, 5, 2 (Fall 1988), 57–70.

Appendix. Simulation Procedures: The Pseudo-Code for One Event in the Simulation

Main // Start the program.

Construct\_Network // Construct a network structure according to // the given parameters such as the number of nodes, // network type, average number of neighbors, etc.

Calculate\_Initial\_Betweenness // Initialize the network by calculating // the initial workload (betweenness) of each node.

Assign\_Capacity // Assign the work capacity of each note // as a constant (in our case, 1.5) times the initial betweenness.

Downsize\_and\_Relink // Remove nodes from the network // according to the downsizing strategy and relink the remaining nodes // according to the reconnection strategy.

Identify\_Clusters // See if any part of network became isolated // from the rest. If there are isolated clusters, // identify them and classify them according to the size.

Calculate\_Betweenness // Calculate the betweenness (workload) // of each node according to the new network structure.

Burn\_Out // Apply burnout process according to the new workload.

Analyze // Analyze the results.

End Main

## Function Burn\_Out

For each node // Begin node burnout.

If(betweenness > capacity)

Then Remove\_Node // If the workload (represented by the betweenness) // exceeds the capacity of the node, that node burns out.

Done // End node burnouts.

Identify\_Clusters // The structure of the network may have changed. // We need to identify the clusters again.

If(no burnout) // If nothing burned out, the network is stable.

Then Return // Break from this Burn\_Out function.

Else // Burnouts occurred.

Calculate\_Betweenness // Calculate the workload of each node again // according to the new network structure.

Burn\_Out // Apply the burnout process recursively.

EndIf // End this If-Else statement.

Return

End Burn\_Out
