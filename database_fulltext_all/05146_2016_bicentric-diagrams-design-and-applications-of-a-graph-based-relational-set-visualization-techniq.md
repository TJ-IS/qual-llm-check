---
otero_id: 5146
otero_key: "5PD2S5P5"
title: "Bicentric diagrams: Design and applications of a graph-based relational set visualization technique"
authors: "Hyunwoo Park; Rahul C. Basole"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2016.02.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Bicentric diagrams: Design and applications of a graph-based relational set visualization technique

Hyunwoo Park <sup>a,</sup>⁎<sup>,1</sup>, Rahul C. Basole <sup>b,1</sup>

<sup>a</sup> Tennenbaum Institute, Georgia Institute of Technology, 85 Fifth Street NW, Atlanta, GA 30308, USA

<sup>b</sup> School of Interactive Computing & Tennenbaum Institute, Georgia Institute of Technology, 85 Fifth Street NW, Atlanta, GA 30308, USA

## a r t i c l e i n f o

Article history: Received 20 February 2015 Received in revised form 22 December 2015 Accepted 2 February 2016 Available online xxxx

Keywords: Bicentric diagram Set visualization Network visualization Strength of ties

## a b s t r a c t

In an era where data on social, economic, and physical networks are proliferating at a rapid pace, the ability to understand the underlying complex structural connections, discover prominent entities, and identify clusters is becoming increasingly important. It is also well-established that interactive visualizations can amplify human cognition and augment decision making. Motivated by a practical need articulated by corporate decision makers and limitations of existing visual representations, this research presents our journey in designing and implementing bicentric diagrams, a novel graph-based set visualization technique. A bicentric diagram enables simultaneous identi cation of sets, set relationships, and set member reach in integrated egonetworks of two focal entities. Our technique builds on the well-established sociological theory of tie strength to visually group and position nodes. We illustrate the broad applicability of bicentric diagrams with examples from four diverse sample domains: university collaboration, technology co-occurrence, health app purchases, and interfirm alliance networks. We assess the value of our technique using an expert-based evaluation approach. The paper concludes with implications and a discussion of opportunities for implementation in real-world decision support settings.

© 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

Humans are visual thinkers [1]. We use visualizations to solve problems, explore opportunities, communicate ideas, recognize patterns, and understand complexity [2]. The foundational challenge in information visualization research is to transform and map raw data into appropriate symbolic and spatial visual representations and couple it with effective and intuitive interaction techniques [3]. It also requires a deep understanding on the user and the task/decision context in which the visualization will be used. Visualization is thus both an art and a science. When done correctly, however, visualizations can significantly amplify human cognition [4].

In an era where data on social, economic, and physical networks are produced at a rapid pace, the ability to visually understand underlying complex structural connections, discover prominent entities, and identify clusters is becoming increasingly important [5,6]. It is thus not surprising to see the research community call for a greater integration of visual network analytics into decision support systems (DSS) [7]. The study of visual decision support is not entirely new. Prior work has incorporated visualization into DSS and evaluated its efficacy in various fields such as personal finance [8], healthcare [9,10], and national power system [11]. More recently, studies have shown the particular value of visual analytics for complex business ecosystem decision making [12,13].

Despite these notable attempts, several important challenges remain. Most network analysis studies still use relatively common visualization layout algorithms, such as circular or force-directed, to represent complex networks [14]. These layouts, however, often result in cluttered representations that are hard to analyze and interpret. The cluttered representation is particularly problematic for large networks because the number of edges increases much faster than the number of nodes. The DSS and information systems literature has recognized and confirmed the importance of representation in managerial problem solving and decision making [15,16]. Existing studies, however, predominantly compare existing classic representations such as table, list, and line chart [17,18]. Novel visual representations for specific types of decision-making problems are rarely developed, despite their importance to problem solving. Motivated by this literature gap and the practical need of corporate executives and investors to map global innovation networks of competing firms, and our discovery of the significant shortcomings of existing visualization techniques to help address questions related to sets (i.e., firm clusters), members of sets, relationships between sets, and reach (i.e., distance from focal node or relationship tier), we designed a visualization layout called the bicentric diagram.

Overlaying two concentric layouts in a clever way, a bicentric diagram fuses ideas from graph and set visualization to depict sets, relationship between sets, and the reach of set members in the integrated egonetworks of two focal entities [19]. The concentric layout is arguably the best layout for depicting an egonetwork [20]. It places the focal node at the center of a set of concentric circles. All neighboring nodes are placed around the circumference of one of the circles based on how many steps they are away from the focal node at the center. Although the concentric layout works well when displaying a single focal node's egonetwork, it falls short when it comes to comparing or merging two focal nodes' egonetworks. A great deal of ambiguity arises when one attempts to portray two egonetworks in the same canvas such as where to place a node that has direct connection to both focal nodes. The bicentric diagram we propose in this paper provides specific visual encodings for simultaneous display of two egonetworks when the interest lies in identifying shared and exclusive components between the two networks.

During our early design discourse [21], it became increasingly evident that analysis of such set-related issues are not just pervasive in business network contexts, but also in sociology, economics, healthcare, politics, and engineering. In social networks, for instance, a researcher may be interested in identifying the overlap and exclusion of friends and acquaintances; in the healthcare context [22], patients may be interested in understanding the co-occurrence structure of drug side effects.

The contribution of our study is multifold. To the best of our knowledge, there are no existing techniques that enable simultaneous identification of sets, set relationships, and set member reach in integrated egonetworks of two focal entities. By developing a unique graph-based set visualization technique with broad application appeal, we contribute to information visualization and human–computer interaction in decision making. Moreover, building on the well-established theory of tie strength [23], we classify shared sets in the bicentric diagram into four types: (i) strong/strong, (ii) weak/weak, (iii) strong/weak or weak/strong, and (iv) exclusive-strong or exclusive-weak. This classification enables us to formally characterize the different types of questions one may address with a bicentric diagram. Our implementation of bicentric diagrams also contributes to the decision making and DSS literature. Considering decision making as an iterative multi-step process [24,25], our study focuses on improving the perspective development and synthesis step. Moreover, many comtemporary relational and network decisions involve identification of specific key nodes (e.g. structural holes) and exclusive assets in the overall network [26]. Our novel representation immediately supports such tasks. The DSS community also calls for further work on web-based DSS [25]. Our system is deployed on the web and accessible for a wide range of users, enabling greater democratization of decision making. By considering an appropriate layout and visual encodings, we also contribute to the aesthetic aspect of DSS design [24].

We illustrate the broad applicability of bicentric diagrams with examples from four diverse sample domains: university collaboration, technology co-occurrence, health app purchases, and global strategic alliances network. Lastly, we assess an interactive prototype version of the bicentric diagram using a value-driven expert evaluation approach and discuss opportunities for implementation in real-world settings. Overall, respondents give above-average scores to all surveyed aspects of our system. In particular, we find that survey respondents with higher visualization literacy levels tend to give higher scores to our implementation of bicentric diagrams in performance areas of time reduction, insight generation, and essence extraction. Even respondents with relatively lower visualization expertise give satisfactory scores in most aspects, indicating that experience and expertise are not a strict prerequisite to appreciate the value of our system.

The remainder of the paper is organized as follows. Section 2 provides an overview of the key related literature from information visualization, business analytics, and network analysis. Section 3 explains the detailed machineries of the bicentric diagram. Section 4 showcases various domains where the bicentric diagram can be a useful tool. Section 5 presents our user study that confirms value of the bicentric diagrams in four key performance areas. Section 6 concludes the paper.

## 2. Related work

In the DSS literature, the decision-making process has been modeled as an iterative process of problem recognition, perspective development, perspective synthesis, actions, and results [24]. The role of DSS is to facilitate human decision-making parts by providing structured views about information pertaining to the decision-making problem space [25]. As more network-centric data emerges, many decisionmaking contexts are now also network related. Given that the choice of representation of data influences decision-making outcomes [15,16], DSS must take this shift in decision-making contexts into account and novel representations are potentially needed.

Data visualization is a well-established method to support decision making in a wide variety of domains. For instance, a visualization approach was adopted to display geographic distribution and market power structure of the U.S. electric power system [11] and a visualization model of adjacency data illustrated college selection decisions [27]. Recent studies show how visualization affects and supports user decision making in the context of financial services [8] and healthcare delivery [9], respectively. Thanks to technological advancements in personal computers, the role of interactivity in visualizations has been highlighted in the literature. An interactive version of self-organizing map visualizations is shown to reduce the cognitive load during Internet browsing tasks [28] and a suite of interactive visualizations was developed and used to explore auction databases [29]. Departing from the decision-making context, a visualization approach is also shown to be useful in the strategic planning process as well [30].

Pending the nature of the data and use context, many different forms of visual representation and interactions exist [31,2]. Multivariate datasets are often visualized using parallel coordinates, starplots, or glyph-based techniques [32]. Hierarchical data are often depicted using a variety of space-filling techniques, such as treemaps, sunbursts, and circle packing [33,34].

One context in which data visualizations are becoming increasingly pervasive is in the analysis of networks. Virtually any aspect of our economic, technical, and social contexts can be described using networks [35]. Node-link diagrams and adjacency matrices are the preferred visualization method for network and graph data [14]. Such visualizations of network evolution can complement and even enhance the associated statistical analysis [36].

Network visualizations have been used to help identify global supply network risks [20], examine criminal networks [37], and understand the evolution of digital communication networks [38].

Following the recognition that many contexts of decision making involve analysis of networks, recent DSS studies have paid attention to the network perspective [39,20]. However, it is the inherent complexity of network data that often hinders the conversion of data into decisionmaking insights; this is amplified when the scope and size of the underlying data are large and wide [40,13]. Visualizations can help users overcome this issue by providing a graphical representation of the underlying network data structure [41]. When coupled with interaction techniques, network visualizations can facilitate the knowledge construction and sharing process and provide confirmatory and new insights [42,43]. Visual analytic systems that afford interactive visual exploration and analysis are thus invaluable for supporting decisionmaking processes.

Real-world networks are often characterized by sets, groups, and clusters. Visualizing sets and set-typed data has also been a topic of substantive interest in the information visualization community [44]. Sets are common data structures in information visualization and are characterized as a group of elements sharing a given property, inherently present in the data, or generated by an algorithm. Terms such as set, group, and cluster are often used interchangeably.

Set visualizations are motivated by tasks associated with elements (e.g. finding elements belonging to a set, finding sets containing a specific element), sets and set relations (e.g. finding total number of sets in the data, analyzing inclusion/exclusion/intersection relations, finding set similarities), and element attributes (e.g. finding the attribute value of a specific element, finding the distribution of an attribute in a certain set/subset).

To address these tasks, many different techniques have been developed including Venn and Euler diagrams, variants of Euler diagrams (e.g. fan diagrams and region-, line-, and glyph-based overlays), node link representations, matrix representations, as well as aggregation-based techniques. An excellent state-of-the-art overview to set visualizations by [45] covers different techniques sampled in Fig. 1.

Set visualizations commonly consist of spatially arranged clusters of set members [46]. In non-fragmented datasets, these clusters are often overlayed with a layer of convex hulls [47]; in contexts where datasets are fragmented, concave boundaries are often used [48]. In contexts where the connectedness between set members and sets matter, relations are generally modeled as edges of a bipartite graph. Prominent examples include parallel lists [49], anchored maps [50], Circos [51], and RadialSets [45]. Anchored maps use a circular layout to visualize bipartite graphs by placing set nodes around a circle and element nodes depending on their set membership. Elements belonging exclusively to a set are placed as a cluster of nodes outside the circle corresponding to the respective set node. Nodes that are shared between multiple sets are placed inside the circle relative to their set nodes. Circos also uses a circular layout for set nodes and uses the thickness of stripes connecting the nodes to encode the number of elements falling into each category. A similar set encoding approach is used by RadialSets. In this approach, however, links originate from the same location, emphasizing that elements in a particular set overlap can also belong to other sets.

## 3. Bicentric diagram

## 3.1. Design goals

Our main objective when designing the bicentric diagram was to support simple readability tasks in egonetworks of two focal entities not available through other set visualization techniques. An egonetwork is a graph of nodes having direct or indirect connections to the focal node. By definition, the concentric layout is well suited when visualizing an egonetwork. However, it does not allow comparison between two egonetworks by itself. Thus, we focused on five design goals:

• Allow users to efficiently identify shared direct connections (G1).

• Allow users to efficiently identify the set membership of each data element (G2).

• Allow users to efficiently identify shared indirect connections (G3).

• Allow users to efficiently identify the distribution of data elements within a set and by level of reach (G4).

• Provide users an intuitive visual metaphor to identify sets and data elements (G5).

![](/api/attachments/5PD2S5P5/fulltext/images/3b7f16cfe6ce2b4f3bf9d8931b3e3f44528599503cced564910b1f1880da860d.jpg)  
Fig. 1. Relevant set visualizations are shown in close-up views. From left-to-right: (1) A multi-set Venn diagram [71] shows all possible logical relations between a finite collection of different sets. Position and color-encoding shows the overlaps; (2) untangled Euler diagrams [72] provide a simplified, compact representation and improve readability of sets and set elements; (3) bubble sets [48] are a visualization technique for dynamically creating bubble™ borders around sets of visual objects, while avoiding inclusion of items not in the set; (4) Kelp diagrams [73] depict set relations over points, where elements have predefined positions. The graphs are designed to take aesthetic quality, efficiency, and effectiveness into account; (5) PivotPaths [74] exposes facets and relations as interactive visual paths. Facets and items are spatially arranged and connected by subtle curves indicating facet–item–facet relationships; (6) RadialSets [45] uses a scalable frequency- and graph-based representation to enable quick identification and analysis of overlapping sets.

Please cite this article as: H. Park, R.C. Basole, Bicentric diagrams: Design and applications of a graph-based relational set visualization technique, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.02.001

H. Park, R.C. Basole / Decision Support Systems xxx (2016) xxx–xxx

A direct connection refers to nodes that are directly connected (i.e. neighbors) to one of the focal nodes. An indirect connection refers to nodes that are not directly connected to the focal nodes but are connected to neighbors of the focal nodes. In graph-theoretic terms, these connection types are captured by the concept of reach. It is also referred to as degree of separation, popularized by the small world experiment by [52]. Direct and indirect connections thus are first and second level of reach away from one of the focal nodes, respectively.

## 3.2. Design motivation

The idea of the bicentric diagram was stimulated by discussions we had with corporate decision makers who were interested in visually comparing their global innovation networks to their competitors [21]. We considered many different visualization approaches. While forcedirected graph layout techniques allowed an understanding of the overall network structure and pockets of collaboration [53], it failed to clearly identify shared direct and indirect partners. Force-directed layouts also did not allow determining what network tier partners belonged to, limiting the understanding how partners were distributed. Similarly, while existing set visualization approaches were able to depict groups, clusters, and relationships, they generally fell short in considering relationships between members and sets as well as differentiating the results by reach from the focal entities. Concentric network layouts were the most effective in depicting a single firm's egonetwork but did not allow a simultaneous examination of two focal firms of interest [20].

Fig. 2 showcases the evolution of our design considerations. Given the intuitive understanding of concentric network visualizations, we recognized that cleverly overlaying two concentric layouts (see Fig. 3a) to create a bicentric diagram (Fig. 3b) would provide possible value. We presented our idea to these decision makers in a series of brainstorming sessions, involving multiple paper sketches and white board drawings, and found that it addressed exactly those questions involving sets, relationships, and tiers.

## 3.3. Layout

The bicentric diagram layout builds on the concentric network visualization and uses ideas from set visualization [45]—specifically node-link and overlay techniques—to provide an effective representation of two focal nodes as well as their shared direct and indirect nodes while organized by tier. A conceptual representation of this layout is shown in Fig. 3c. The bicentric layout provides a graph-based set visualization of two focal nodes (A and B) positioned at a distance d apart. Two concentric circles with radii d/2 and d are drawn around each focal node, where other non-focal nodes are placed. Each circle represents a tier from the focal node. The inner circle contains the focal node's 1st-tier nodes (1-step away neighbors). Similarly, the outer circle contains 2nd-tier nodes (2-steps away). Thus, a node that is connected/related with a 1st-tier node but not with a focal node would be 2 steps away from the focal node in the outer circle.

The shaded arcs and intersecting points of the concentric circles represent areas for positioning nodes corresponding to the various combinations of set membership. Nodes directly connected to both focal nodes (i.e. are 1 step away) are placed in a cluster at the center of the focal dyad (area 1). Nodes that have direct or indirect connection to only one of the focal nodes are positioned on the arcs (i.e., semicircle) on the side of that focal node. Those connected directly to only focal node A (or B) are placed on the inner arcs—area A1 (or area B1), while connections to only those 1st-tier nodes (i.e., indirectly connected to the focal nodes) are placed on the outer arcs—areas A2 and B2. Nodes one step apart from Node A and two steps away from Node B are placed around area 2a and 2b. We differentiate nodes placed at the top (area 2a) and the bottom (area 2b) by whether they belong to the main component.

The main component refers to the largest connected component of an undirected graph and the largest weakly connected component of a directed graph, where all nodes within that component can reach each other through some paths [54]. The notion of connected components has been known in graph theory from early days [55]. For example, suppose that we have a graph consisting of ten nodes. Five, three, and two nodes are connected to each other, respectively. In graph theory, each group is called a connected component. Among three groups, the group that contains the most nodes is the main component. Distinguishing the main component is of great interest in network analysis research [56,57]. In our system, visually differentiating the main component from other components allows us to further disentangle the sub-tier activities and reduce the number of edge crossing and long edges in the visualization. This differentiation is also in accordance with the visual design principle because it minimizes the number of vertically crossing edges which clutters the overall visualization. Nodes two steps apart from both Node A and B are placed at areas 4a and 4b. The same top (area 4a) and bottom (area 4b) differentiation by membership to the main cluster applies.

Once nodes are placed, we adopt various visual encodings for nodes and edges to enhance user understanding of the data. An edge between two nodes represents a relationship/connection between those two nodes. For instance, in product networks, one product i is connected to another one j if it was recommended or co-purchased. The thickness of an edge corresponds to the number of times the nodes were connected/related in the dataset. The node diameter is sized proportionally to the square root of the number of node occurrences. The larger the node, the more common the node is in the dataset. The node color corresponds to the category the node belongs to. The edge color is gray on default and switches into corresponding color of the hovered over node. Within each arc, nodes are grouped by category (counter-

![](/api/attachments/5PD2S5P5/fulltext/images/b3cab31edf045ea42595b873f4de84bdf350addd4055d23a2c90458b97448799.jpg)  
Fig. 2. Our design consideration evolved over a series of brainstorming sessions.

Please cite this article as: H. Park, R.C. Basole, Bicentric diagrams: Design and applications of a graph-based relational set visualization technique, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.02.001

H. Park, R.C. Basole / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/5PD2S5P5/fulltext/images/9f8321d4a2149ad99a5aa5ec4502c6d3cea03077cb30e541bf82185d1425eac9.jpg)  
Fig. 3. (a, b) The bicentric layout builds on the concentric network visualization to provide an efficient representation of two focal nodes as well as their shared direct and indirect nodes while organized by tier. (c) This schematic provides an overview of node placements in the bicentric layout. (d) Classification of relationship types identifies four combinations of tie strength.

)clockwise for (left or) right focal nodes, respectively. To further reduce visual clutter and improve readability and aesthetics, we apply a “no overlap” and node jittering rule. Such a rule adds random perturbation to the position of all nodes until every node is not overlapped with another.

## 3.4. Decision-making tasks using bicentric diagrams

The bicentric diagram is particularly suited to address questions related to sets of strong, weak, and exclusive ties of two focal entities. Strong ties refer to direct connections of a focal entity (i.e. friends); weak ties refer to indirectly connected entities (i.e. friends-of-friends or acquaintances) [23]. Consider the 3 ×3 tie type matrix shown in Fig. 3d. Direct connections shared by two focal entities refer to strong/strong ties (Cell I). These represent the common ties of two focal entities. In the case of friendship networks, this would be a shared friend. In product recommendation networks, this would represent a product that was co-purchased by both. At the opposite end are indirect connections to both focal entities. We refer to these as weak/weak ties (Cell III). Cells II represent a direct connection to one focal entity, and an indirect connection to the other (and vice versa). We refer to these as strong/weak and weak/strong ties, respectively. Cells IV represent those direct and indirect ties exclusive to each focal node, respectively. We refer to these as strong-exclusive and weak-exclusive ties.

The intersecting and exclusive node placement areas in our bicentric diagram thus correspond to one of these tie types. The visual separation enables rapid identification of these tie types and examination of a wide range of questions for making decisions in the network context. For instance, a corporate strategy manager may search the next potential alliance partner that has been exclusively collaborating with the competitor firm. Another more everyday-level example is a consumer considering to buy another video game. One has a few favorite games and wants to discover what other people purchase together with the focal favorite games. The bicentric diagrams help quickly identify and generate candidate choice set for this type of decisionmaking problems.

## 3.5. UI implementation

The user interface (UI) for our prototype consists of two main areas: the selection pane and the visualization pane (see Fig. 4). The selection pane contains multiple drop-down lists that contain the data context list (Panel A) and the node lists for the chosen context (Panel B). We introduce the available contexts in more detail in the applications section. The number next to each list entry indicates its occurrence frequency in the dataset (Panel B). For this example, “Videoconferencing Software” was mentioned 35 times. Since the number of nodes can be over the thousands, it is an important design consideration to make sure that the lists are scrollable and searchable (Panel B). Once a user has selected two focal nodes of interest, the “Compare” button updates the visualization screen with the corresponding bicentric diagram (Panel G). The UI provides several interactive tools to manipulate the visualization. Users can collapse and expand the visualization window as well as zoom-and-pan the bicentric diagram (Panel C). To maximize readability, users can show/hide edges, layout gridcircles, node labels, and the color category legend (Panel D). Users can also locate specific nodes in the visualization using a quick search box function (Panel F). Hovering over a node provides detailed information in a label (Panel E). It also highlights its directly connected edges and nodes (while fading others). Clicking on a node will fix the highlights for convenient path tracking. Clicking on the background cancels the current selection. Keyboard shortcuts for these UI functions are also provided. Lastly, we setup five tutorial pages to assist first-time bicentric diagram users.

The interactive front-end UI is developed and implemented using D3.js [58] and Bootstrap. The back-end is written in Python and NetworkX [59]. The back-end Python script returns initial node positions based on node attributes and network metrics (e.g., connected components) upon request from the front-end. The front-end implements interactivity and adjusts node positions to minimize overlaps. The application was hosted and made available to users on the Heroku platform at http://bicentric.herokuapp.com. For purposes of this study, we did not develop a public data import tool, mainly due to concerns of data security, authentication, and intellectual property rights. However, we envision to implement one for a future release.

## 3.6. Beta Testing

Prior to releasing our interactive UI to participants for evaluation, we conducted a rigorous iterative beta test with four experienced visualization users. The aim was to get in-depth feedback on the overall usability and usefulness of the tool, the steps of our tutorial, and the specific wording of our evaluation survey. The feedback was generally favorable in both visual representation and interactivity of our implementation. Specific suggestions included elaboration of the tutorial with concrete examples, resolution of ambiguous domain-specific terms (e.g. “tier” versus “reach”) and graph-theoretic concepts (e.g. “what is a main component?”), and learning tasks to get familiar with the UI rather than a free exploration. We revised the UI, tutorial, and instructions accordingly.

## 4. Applications

The bicentric diagram layout can be used in numerous different contexts. We focus our discussion to four diverse specific application

H. Park, R.C. Basole / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/5PD2S5P5/fulltext/images/898fd10d762977907d0b746d513d6222846c715aa915c4ac7e8c42ddac38011e.jpg)  
Fig. 4. A screenshot of the system UI is presented. The current context is set as Technology Co-Occurrence (Panel A). Two technologies (videoconferencing software and operations support systems) in the technology co-occurrence dataset are selected (Panel B). Various controls help users zoom and pan the diagram (Panel C). The bicentric diagram shows the technologies that co-occur with these two technologies; nodes are positioned at the appropriate set location (Panel G). The color legend (Panel D) and help guidelines are turned on (Panel F) to aid users with reading the diagram. The user hovers over a second-tier technology (i.e. virtual private networks). Its connections are highlighted and the label shows details (Panel E).

areas: university collaborations, technology co-mentions, health app purchases, and interfirm alliance network.

We chose the first three use cases to demonstrate the universal value and applicability of bicentric diagrams beyond the business setting that motivated this paper. We conclude with an example explicitly in the business domain.

Each use case represents a different network data context. The university collaborations network, for instance, captures an institutional social network aggregating individual collaborations. Other potential examples that could have been used include Facebook friendship or Twitter follower networks. The technology keyword dataset is a co-occurrence network context. Other examples include the tag co-occurrence network in StackOverflow questions, daily deals in Groupon [60], or movie recommendations in Netflix. The health app network represents an example of a commerce network. Other examples of such a network may be related products in Amazon or restaurant reviews in Yelp.

Lastly, the interfirm alliance network is also a type of organizational collaboration network similar to the university collaborations network. However, it is an important example for the bicentric diagram as it links back to our original motivation of designing this diagram: the intelligence needs of corporate decision makers.

We must stress that the application areas introduced in this section should merely be interpreted as possibilities rather than limiting constraints. Bicentric diagrams can prove valuable to any contexts in which comparing two entities' relationship structure matters. Table 1 highlights some of the possible application areas. We identify six potential application domains. Beside business decision making and social network application domains, product and software design are notable domains that can benefit from applying the bicentric diagram.

Possible application areas of bicentric diagrams.

<table><tr><td>Domain</td><td>Example</td><td>Nodes</td><td>Edges</td></tr><tr><td rowspan="5">Business and economics</td><td>Supply network</td><td>Supplier, customers</td><td>Exchange of products and money</td></tr><tr><td>Alliances</td><td>Firms</td><td>Formed alliance</td></tr><tr><td>Venture capital</td><td>Investors</td><td>Co-invested experience</td></tr><tr><td>Patent citation</td><td>Patents</td><td>Citation direction</td></tr><tr><td>Global trade</td><td>Countries</td><td>Flow of import and export</td></tr><tr><td rowspan="3">Commerce</td><td>Product comparison</td><td>Products</td><td>Similarity</td></tr><tr><td>Reviews</td><td>Users</td><td>Co-review behavior</td></tr><tr><td>Music</td><td>Songs, albums, artists</td><td>Co-purchase or similarity</td></tr><tr><td rowspan="2">Healthcare and life sciences</td><td>Process maps</td><td>Activities, medications</td><td>Flow of resource</td></tr><tr><td>Systems biology</td><td>Molecules</td><td>Chemical reaction</td></tr><tr><td rowspan="3">Social networks</td><td>Friendship network</td><td>People</td><td>Friendship</td></tr><tr><td>Follower network</td><td>Twitter IDs, Facebook</td><td>Follower-following relationship</td></tr><tr><td>Political network</td><td>Politicians</td><td>Co-sponsor of a bill</td></tr><tr><td rowspan="2">Manufacturing and Engineering and computer science</td><td>Product design</td><td>Components</td><td>Mechanical/electrical link</td></tr><tr><td>Software design</td><td>Objects, classes</td><td>Inheritance</td></tr></table>

Please cite this article as: H. Park, R.C. Basole, Bicentric diagrams: Design and applications of a graph-based relational set visualization technique, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.02.001

Even these highly technical design areas are increasingly adopting various novel visualization approaches to enhance alignment among stakeholders in different levels [61].

## 4.1. University collaborations

## 4.1.1. Context and data

Institutional collaboration between universities and corporations is a common phenomenon in scholarly research. Those institutional collaborations are macro patterns aggregated from the underlying finer-grained individual researchers' collaboration network. Locating the right set of collaborators is a great career concern for scholars. If a target institution is too far from reach, knowing a close collaborator of the target may help connect to the target eventually. Identifying potential collaborators and a path to reach them is equally important at the organization level. Such organizational search problem in the network context has been characterized through the sociological lens [23] and studied extensively in organization science [62].

We source our data from the ACM Digital Library that contains a list of co-authoring institutions as well as their profiles. After collecting the profiles of top 1000 institutions by publication count, we construct a network based on the co-authorship among them as of September 15, 2014. Thus, a node represents an institution and an edge between two nodes indicates that they co-authored a publication. Nodes are sized by the institution's total publications count and colored by geographic region. All nodes are categorized into five regions—Europe, North America, Asia, Australia, and Others. Europe has the greatest number of institutions in the dataset while North American institutions are much larger in terms of per-institution publications. Edge thickness corresponds to the total number of co-authored publications between the two institutions.

The original dataset tracks a full list of collaborators for each institution. Even a pair of institutions that co-author only a single publication is thus captured as an institutional collaboration. We therefore applied a mix of relative and absolute thresholds to filter out collaboration relationships with minimal significance. We set the relative threshold to 20% of the maximum edge weight for each node. For instance, if an institution published 1000 articles with its most frequent collaborator, all edges starting from this institution having less than 200 co-authored publications would be dropped. The absolute threshold was set to five publications so as to drop any collaborations resulting in less than five co-authored articles.

## 4.1.2. Example

We incorporate the aforementioned dataset into our interactive bicentric diagram generator. As an illustrative example, consider the bicentric diagram of the two focal universities—Seoul National University (SNU) and Carnegie Mellon University (CMU)—shown in Fig. 5. SNU and CMU directly share (Type I ties) only two collaborators, University of Southern California (USC) and University of Illinois at Urbana–Champaign (UIUC) (see Fig. 6 for the magnified version). One striking observation of the bicentric diagram is SNU's virtually exclusive collaboration (Type IV ties) with institutions from Asia (depicted by nodes in green). Another immediate observation is that CMU's direct network consists of institutions primarily from North America; its twostep network, however, is substantially larger than that of SNU and regionally diverse. CMU's Type II ties form a large interconnected cluster with Tsinghua University, resulting to be the only Asian connection. Following [23], the institutions in this cluster have weak (or indirect) ties with SNU but strong (or direct) ties with CMU. In addition to UIUC and USC, these institutions thus play a potential bridging role between CMU and SNU because from SNU's perspective it would be easier to establish connection with its weak ties than with the Israeli universities shown in the zoomed-in version in Fig. 6. Another confirmatory evidence that deserves mentioning is the connection intensity between CMU and the University of Pittsburgh. The collaboration is thicker than any other direct connections that CMU has suggesting that the two universities would probably collaborate more frequently given the geographic proximity.

## 4.2. Technology co-mentions in press releases

## 4.2.1. Context and data

Market researchers and analysts are frequently interested in understanding how different technologies relate to each other. Changes and trends in technological landscape influence strategic planning and positioning for companies from start-ups to large corporations alike, and thus they are essential to the decision-making process for corporate technology management. Although press releases and news articles contain a wealth of information on emerging technologies, search

![](/api/attachments/5PD2S5P5/fulltext/images/cdb9900d83c1461b6f20819ce1fdac20b6df43e1ba41f7be233220df51b8518b.jpg)  
Fig. 5. A screenshot of institutional collaboration network between Seoul National University (green focal node) and Carnegie Mellon University (orange focal node) is presented. Labels and color legend are added externally using separate annotation software after capturing the screenshot.

Please cite this article as: H. Park, R.C. Basole, Bicentric diagrams: Design and applications of a graph-based relational set visualization technique, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.02.001

H. Park, R.C. Basole / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/5PD2S5P5/fulltext/images/2b3a32249722806962f095d69aeee765f0c077c78515a289955f26af5bca3b54.jpg)  
Fig. 6. Zoomed-in snapshot of the collaboration network between Seoul National University and Carnegie Mellon University. User has selected CMU as the focus. Label indicates detailed information; edge thickness reveals the extent of institutional collaboration.

results can be overwhelming and their linear presentation format does not always provide necessary systemic insights. We use the data from Northern Light SinglePoint (http://www.northernlight.com) portal to build a co-occurrence network of technologies mentioned in the press over the past year from September 10, 2014. We identify 834 unique technologies (e.g., “Smartphones,” “Cloud Computing and Storage,” “Predictive Analytics”) and classify them into 10 categories adapted from [12]. For each technology, we collect co-occurrence data with other technologies. Technologies thus represent nodes in the network. An edge between two nodes indicates that they co-occurred in a document. Nodes are sized by the frequency of occurrences and colored by category. Edge thickness corresponds to the number of co-occurrences between two technologies.

Note that we model the technology co-mention network as a directed graph in a similar way for the institutional collaboration data set used in the previous section. For instance, suppose we have a frequent/popular technology (e.g., “Smartphones”) and a relatively infrequent one (e.g., “Smart Fabric”). It may be the case that whenever Smart Fabric is mentioned, it is also mentioned with Smartphones. However, the reverse statement may not necessarily be true. The main technologies that are co-mentioned with Smartphones also are likely to be broad and popular technologies such as “Android Operating Systems” or “iOS.” In sum, Smart Fabric can mainly co-occur with Smartphones, but from Smartphones' perspective co-occurrences with Smart Fabric can be ignored.

## 4.2.2. Example

Consider a start-up company working on tangible media and information visualization. Leveraging its own expertise, it considers to expand into an adjacent technology space that can potentially provide additional traction to the company. The decision thus relates to what technology path it should possibly explore. Fig. 7 shows the zoomedin and labels-on bicentric diagram of two technologies—wearables and data visualization. We first notice that these two technologies share a range of different technology categories (Type I ties), including platforms (pink), mobile (olive green), and networking and communications (orange). Interestingly, Type II ties of wearable technologies are far less (Bluetooth, Home Automation, GPS, and PC) while the application category (blue) dominates Type II ties for Data Visualization. By selecting the two focal technologies, then seeing which ones are directly and indirectly related, the decision maker gains an overview of the overall related technology space and can then make more informed decision which technology path to pursue.

## 4.3. Health app purchases on Amazon.com

## 4.3.1. Context and data

Product recommendation is a pervasive feature on e-commerce sites. A multitude of individual consumers make purchase decisions relying on such recommendation data. However, most sites only provide long scrollable lists that are hard to navigate. List format does not afford exploration beyond the immediate related apps not to mention comparison. A visual comparison of related or co-purchased products beyond the immediately related apps will be helpful for consumers to generate candidate apps for potential purchase. To demonstrate the effectiveness of bicentric diagrams in this type of consumer decision-making context, we collect data of all Android health apps from Amazon.com. For each app, Amazon provides a list of (up to 100) related apps. Related apps are determined based on consumers' co-purchasing behavior. If consumers frequently purchased both apps A and B, for instance, we consider these two apps related to each other. Each health app is categorized by Amazon into one of six categories (Diet, Medical, Exercise, Meditation, Pregnancy, and Sleep). For illustrative purposes, we

Please cite this article as: H. Park, R.C. Basole, Bicentric diagrams: Design and applications of a graph-based relational set visualization technique, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.02.001

H. Park, R.C. Basole / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/5PD2S5P5/fulltext/images/fb6e753adc94a5eaf14455bc85371936d398d4b52579a56e211923c35687d42e.jpg)  
Fig. 7. Technology co-occurrence in press releases related to wearable technology (turquoise focal node) and data visualization (red focal node) is shown.

filtered out those apps with less than five reviews to focus on the ones that have some established user base. This resulted in a final set of 711 health apps.

We construct the co-purchase network of health apps. Health apps (nodes) are connected when co-purchased (edge). Nodes are sized by the total number of reviews and colored by the health app category defined by Amazon. Edge thickness proxies how many people co-purchased both apps by inversing the order of appearance in the list of related apps. Suppose an app A has two related apps: B and C. B appears in the first page of the list of related apps, while C appears in the last page in the list. We interpret B to be co-purchased more frequently with A than C.

![](/api/attachments/5PD2S5P5/fulltext/images/5c8c0cc71d131eea53b1bd378757026ed79780bf01921f460e828ecd1d3a118c.jpg)  
Fig. 8. Bicentric diagram of fat-burning yoga and diabetic recipes apps with labels turned off is shown.

Please cite this article as: H. Park, R.C. Basole, Bicentric diagrams: Design and applications of a graph-based relational set visualization technique, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.02.001

## 4.3.2. Example

Consider the example of an individual who loves yoga but is a diabetic. She currently owns apps related to each of these issues. Fig. 8 shows the bicentric diagram of her two apps: a fat-burning yoga app on the left and the diabetics recipes on the right. Most apps exclusively associated (Type IV ties) with the yoga app are exercise related (as depicted by the green nodes). Most common apps (Type I ties) are related to meditation (depicted by red nodes). Not surprisingly, diet apps are more frequently co-purchased with the diabetic recipes app (Type II tie). This bicentric diagram provides clear visual demarcation among different sets of related apps that she may find interesting. If she wants to explore apps exclusively related to her yoga app not to her recipe app, she can easily direct her attention toward the left semicircle.

## 4.4. Global strategic alliances network

## 4.4.1. Context and data

We conclude with an example from the business domain. Today, firms rarely create value alone. They form strategic alliances to access complementary resources while focusing on their core competencies. In this increasingly complex and interconnected business environment, corporate decision makers are interested in understanding the structure of complex strategic alliance networks of competing organizational entities, enabling them to identify key shared direct and indirect partners and determine which partners are exclusive to them. Using the SDC Platinum dataset and following [53], we construct a global strategic alliances network of firms in the information and communications technology (ICT) industry from 1990 to 2012. Firms are categorized into five broad industry segments based on their primary standard industrial classification (SIC) code: hardware components, hardware equipment, software, telecommunications, and media. Filtering out firms with less than five alliances, the final sample contains 1755 firms. Entities directly connected to the focal entity are considered first-tier partners. Those indirectly connected are second-tier partners. As hierarchy prevails in business settings, the notion of a tiered network structure makes clear sense. Entities are color coded by industry segment they belong to.

Node size and edge thickness encodes weighted degree of a firm and the number of alliances between a specific pair of firms, respectively.

## 4.4.2. Example

Consider the bicentric diagram of Hewlett–Packard (HP) (left) and Intel (right) shown in Fig. 9. Edges and help gridcircles are turned off for comparison if having them on creates bias or helps interpretation. A decision maker may be interested in identifying a potential future software alliance partner based on their extended alliance networks. The visualization reveals stark difference between the two firms' egonetworks. HP is larger than Intel, suggesting HP has more alliances than Intel. Indeed, many of shared direct partners of the two firms are larger than other nodes. However, HP does not have any exclusive direct partners that does not have connection with Intel. We can see that only a few indirect partners of HP are exclusive. On the other hand, not only does Intel have many direct and indirect exclusive partners, but those exclusive partners are relatively equally distributed across all five industry segments compared to the indirect exclusive partners of HP. The large green node prominent on the right-hand side of Intel is Microsoft. It provides a refreshing insight that Intel has a direct connection with Microsoft, while Microsoft does not even have an indirect connection to HP.

## 5. Value-driven evaluation

There is an open, rich, and perhaps even heated discussion in the broader HCI community on how to best evaluate novel visualization techniques [63,64]. Some researchers argue that only a controlled laboratory experiment provides valid insights. Others advocate a longitudinal, “in the wild” approach. Unquestionably, each evaluation approach has advantages and disadvantages. Comparing individual visualization techniques to each other—for usefulness or performance benchmarks—is increasingly advised against as it essentially compares apples to oranges and reduces the potential of understanding the true unique value and purpose of each technique [65,66,67]. Given our study context, we follow Stasko's value-driven evaluation approach to understand bicentric diagrams [67]. This evaluation approach consists

![](/api/attachments/5PD2S5P5/fulltext/images/d72e3f593db9bd290b7f8fb8775cdad37788ad909ff82815df49a687ef07e61c.jpg)  
Fig. 9. Global inter rm alliances network of Hewlett–Packard and Intel without gridcircles is shown.

Please cite this article as: H. Park, R.C. Basole, Bicentric diagrams: Design and applications of a graph-based relational set visualization technique, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.02.001

of an assessment of four key components: time, insight, essence, and confidence. For each component, we develop a set of questions to which respondents answer on a five-point Likert scale (1 is labeled as “Strongly Disagree” and 5 as “Strongly Agree”).

Time refers to the visualization's ability to minimize the total time needed to answer a wide variety of questions about the data. An effective visualization allows a person to identify many values from a data set and answer different questions about the data simply by viewing and interacting with the visualization. Effective visualizations assist users to rapidly answer “low-level” questions such as finding nodes, retrieving values, and characterizing distributions [68]. We use four statements to evaluate time:

• T1: The visualization reduced the time I needed to find nodes shared by the focal nodes.

• T2: The visualization reduced the time I needed to find sets of nodes related to the focal nodes.

• T3: The visualization reduced the time I needed to find how nodes were distributed by tier.

• T4: The visualization reduced the time I needed to find how nodes were connected.

Insight refers to the visualization's ability to spur and discover insights and/or insightful questions about the data. An effective visualization allows a person to learn about and make inferences from a data set that would be much more difficult to achieve without it. Insight does not necessarily only equate to the unexpected or the “aha!” moment, but also to knowledge building and confirmation. Insight can thus be considered a by-product of exploration facilitated by the visualization [69].

• I1: The visualization enabled me to discover insights about the data.

• I2: The visualization enabled me to ask insightful questions about the data.

Essence refers to the visualization's ability to convey an overall essence as well as a take-away sense of the data. An effective visualization allows a person to gain a “broad, total sense of a potentially large data set beyond what can be gained from learning about each individual data case and its attributes.” [67].

• E1: The visualization conveyed an overall essence of the data.

• E2: The visualization provided a take-away sense of the data.

Confidence refers to the visualization's ability to generate confidence, knowledge, and trust about the data, its domain, and context. An effective visualization allows a person to learn and understand more than just the raw information; it promotes a broader understanding of and trust about the data. It can help identify embedded problems in the data set, such as missing, erroneous, or incomplete values, or highlight areas where additional data are needed.

• C1: The visualization helped me generate confidence about the data, the domain, and context.

• C2: The visualization helped me generate knowledge about the data, the domain, and context.

• C3: The visualization helped me generate trust about the data, the domain, and context.

## 5.1. Participants and procedure

As our goal was to evaluate the benefits of the visualization, and not the specific content domain, we recruited experienced academics and practitioners from the information visualization community. We contacted 28 experts by email and sent them links to the web-based visualization tool, tutorial, and post-use survey. 4 declined to participate, 9 did not respond, and 15 completed the evaluation, for a net response rate of 54%. Participants hold positions such as professor (full, associate, assistant), postdoctoral researcher, PhD candidate, lecturer, user experience manager, and vice president of data analytics. Our sample consists of 11 participants from academia and 4 participants from industry. We administered the survey over 10 days.

## 5.2. Results

Table 2 and Fig. 10 shows the result of our value-driven evaluation. Table 2 tabulates the 11 survey questions and the summary statistics of responses for all questions along with self-assessment on expertise in information visualization. Each question is answered on a five-point Likert scale. The greater the average of responses is, the more agreeable respondents find the question. Fig. 10 provides a histogram summary of results corresponding to each evaluation statement; the thick vertical black line in each histogram marks the mean score for each statement.

Overall, our visualization scored high in both reducing time to conduct common tasks (T1: 4.6, T2: 4.5, T3: 4.4, T4: 4.5) and providing insight (I1: 4.5, I2: 4.3). On the other hand, our visualization scored somewhat lower in providing essence (E1: 4.0, E2: 3.9) and generating sufficient confidence (C1: 3.7, C2: 3.9, C3: 3.7). All mean scores are significantly greater than 3 (pb0.01 from one-sample t-tests), so we statistically confirm above-average scores to all questions. The particularly favorable evaluation of our time criteria (T1–T4) corresponds directly to our design goals of creating a visualization that enables efficient identification of shared direct connections (G1), set memberships (G2), indirect connections (G3), and distribution (G4). This finding is encouraging as it provides support for our underlying hypothesis of the value of bicentric diagrams. Users commented that our tool was particularly helpful in “rapidly identifying shared nodes” of two focal entities and enabled a quick scan of the sets embedded in the structure.

We were also encouraged to see the results for insight (I1-I2). While these did not directly correspond to one of our main goals, it is the aim of any visualization to provide insight. Each use context generated some interesting “aha!” moments.

For instance, in the institutional collaboration context, one user discovered that her institution does not collaborate directly with any non-U.S. institutions, while a counter top institution in her field does (e.g., “No wonder they recruit so well from China.”). However, she also identified that both institutions collaborate with the same corporate partners, highlighting their head-to-head competition for industry research grants. In the technology co-occurrence context, one user explored what topics relate to iOS and Android. Confirming his intuition, shared topics included smartphones and tablet computing. However, counterintuitively, social networking was only co-mentioned with iOS, while next-generation hardware-related topics were co-mentioned with Android, possibly suggesting diverse platform strategies. Topics related to data and analytics were surprisingly only indirectly connected to both operating systems.

Perhaps the more disappointing outcomes of our value-driven evaluation was the poor performance on essence (E1–E2) and confidence (C1–C3). We speculate that this was partially due to the application contexts we made available to the users

We certainly agree that prior domain knowledge or a vested interest in the domain matters. We also believe that if we had used the bicentric diagram with business users and our innovation network data exclusively, our evaluation for essence and confidence would have been much higher.

Additionally, the Min and Max columns in Table 2 advocate our system from a different perspective. The values in these columns are meant to show extreme values in the survey responses. We have all 5 s in the Max column, which means at least one respondent found our tool strongly agreeable for each survey question. On the other hand, Min values vary from 2 to 4. We rarely see a 2 in this column. The mean score to question 3 is fairly high at 4.4, while that to question

Evaluation questions and results (N=15).

<table><tr><td>No.</td><td>Area</td><td>Question</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Max</td></tr><tr><td>1</td><td>T</td><td>The visualization reduced the time I needed to find nodes shared by the focal nodes.</td><td>4.60</td><td>0.51</td><td>4</td><td>5</td></tr><tr><td>2</td><td>T</td><td>The visualization reduced the time I needed to find sets of nodes related to the focal nodes.</td><td>4.47</td><td>0.52</td><td>4</td><td>5</td></tr><tr><td>3</td><td>T</td><td>The visualization reduced the time I needed to find how nodes were distributed by tier.</td><td>4.40</td><td>0.83</td><td>2</td><td>5</td></tr><tr><td>4</td><td>T</td><td>The visualization reduced the time I needed to find how nodes were connected.</td><td>4.53</td><td>0.64</td><td>3</td><td>5</td></tr><tr><td>5</td><td>I</td><td>The visualization enabled me to discover insights about the data.</td><td>4.53</td><td>0.64</td><td>3</td><td>5</td></tr><tr><td>6</td><td>I</td><td>The visualization enabled me to ask insightful questions about the data.</td><td>4.33</td><td>0.62</td><td>3</td><td>5</td></tr><tr><td>7</td><td>E</td><td>The visualization conveyed an overall essence of the data.</td><td>4.00</td><td>0.85</td><td>3</td><td>5</td></tr><tr><td>8</td><td>E</td><td>The visualization provided a take-away sense of the data.</td><td>3.93</td><td>0.80</td><td>3</td><td>5</td></tr><tr><td>9</td><td>C</td><td>The visualization helped me generate confidence about the data, its domain and context.</td><td>3.73</td><td>0.59</td><td>3</td><td>5</td></tr><tr><td>10</td><td>C</td><td>The visualization helped me generate knowledge about the data, its domain and context.</td><td>3.87</td><td>0.83</td><td>3</td><td>5</td></tr><tr><td>11</td><td>C</td><td>The visualization helped me generate trust about the data, its domain and context.</td><td>3.73</td><td>0.80</td><td>2</td><td>5</td></tr><tr><td>N/A</td><td>N/A</td><td>Please rate your level of visualization expertise.</td><td>4.47</td><td>0.64</td><td>3</td><td>5</td></tr></table>

Note: Respondents were given a five-point Likert scale to answer each question (1 as “Strongly Disagree” and 5 as “Strongly Agree”). The greater the number is, the more agreeable respondents find the question. The legend for the performance area shorthand notations is as follows. T: Time, I: Insight, E: Essence, C: Confidence.

11 is relatively low at 3.7. This finding suggests that our system may need to improve in terms of trust and confidence-related aspects.

Correlation analysis between participants' expertise in information visualization and four performance area average scores supports our interpretation above. Pairwise correlation coefficients between expertise and average scores in time, insight, essence, confidence are 0.34, 0.22, 0.17, -0.08, respectively. Thus, the greater the respondent's expertise, the higher the scores in time, insight, essence, and the lower three confidence scores. Particularly, time performance receives highly favorable scores from participants with high expertise.

The reason for choosing visualization “experts” for evaluating our system was to ensure that our system was not just easy-to-use but also conforms to visualization principles. Experts will be much more versed in understanding the nuances of visualization principles. They will also be able to comment on the relative strengths of the system compared to other visualization approaches. This does not mean that

![](/api/attachments/5PD2S5P5/fulltext/images/0e4e4e40eea536c83eb23712e83feb6de6ed7c864e767fa24b8cf677e49235a7.jpg)  
Fig. 10. Value-driven evaluation results are shown in the form of histograms by four performance areas. The vertical black thick line in each histograms denotes the respective mean value

Please cite this article as: H. Park, R.C. Basole, Bicentric diagrams: Design and applications of a graph-based relational set visualization technique, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.02.001

our tool is inaccessible to people with less experience, in fact, our analysis shows that users with lower expertise scores still rated the tool quite favorably. We acknowledge that the sample size is small, and we plan to conduct a broader user study with wide range of characteristics in future work.

We also received informal feedback from our users after the evaluation phase regarding the overall ease of use, aesthetics, and applicability of our visualization. With regards to ease of use, for instance, one respondent commented, “I can quickly figure out which of the two focal nodes has more relationships by comparing the number of nodes and their distributions. I can get to know how a certain node has closer relationships among two focal nodes. I can see how category affects relationships and which nodes have more cross-category relationships.” Users complimented the look-and-feel of our visualization (e.g., “Overall, beautiful tool!” and “The implementation feels very professional.”). Lastly, users commented the generalizability of our visualization to other decision-making contexts (e.g., “I loved the visualization, very clever way of showing the connections between two things.” and “I can see this visual representation applied to my own dataset!”).

## 6. Conclusion

Visualizations amplify human cognition and augment decision making. As data on social, economic, business, and physical networks are proliferating at an accelerating pace, the ability to engage with such data interactively is becoming ever critical to explore underlying complex structural connections, discover prominent entities, and identify clusters. Motivated by a practical need articulated by corporate decision makers and limitations of existing visual representations, this research presented our journey in designing and implementing bicentric diagrams, a novel graph-based set visualization technique that can be used for perspective development in the loop of decision-making process [24].

Bicentric diagrams enable simultaneous identification of sets, set relationships, and set member reach in integrated egonetworks of two focal entities. Thus, it helps quickly generate potential solution candidates for organizational decision-making problems locating structure holes from the network perspective. Our technique builds on the well-established sociological theory of tie strength to visually group and position nodes. In contrast to traditional network layout approaches, our technique provides an aesthetically appealing way to visualize the intersections of weak and strong ties between two entities. We demonstrate the broad applicability of bicentric diagrams with examples from four diverse sample domains: university collaboration, technology co-occurrence, health app purchases, and interfirm alliance networks.

The results of our value-driven expert evaluation revealed several interesting results and offered suggestions for future research. First, bicentric diagrams enable decision makers to rapidly identify key players and their roles and positions in egonetworks of two focal entities. Second, our technique also facilitates gaining new insights and led to various “aha!” moments, which helps form perspectives for a decision-making problem. Third, users appreciated ease of use, aesthetics, and broad applicability of the bicentric layout to different decision-making domains.

Our expert user study, however, also revealed a few limitations. For instance, depending on the size of networks, visual cluttering can be an issue. Fisheye focus + context techniques [70] or intelligent labeling could be used to overcome this. Individual user competencies may also impact performance. Examining how visual perception and literacy affects a user's understanding will be another interesting path of inquiry. Others commented that a more comprehensive user study in one specific domain, such as e-commerce product recommendations, could provide additional insights. We are considering a large-scale mechanical turk study to explore this further. Contexts such as restaurant co-review networks (e.g. Yelp) or start-up investment’ networks (e.g. Crunchbase) may be of interest. Each of these limitations presents exciting future research and their pursuit will help further refine the usefulness and utility of bicentric diagrams. We hope that bicentric diagrams can serve as a guide for other researchers and practitioners to develop novel representations for specific decision-making problems and implement them into a web-based DSS.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at http://dx. doi.org/10.1016/j.dss.2016.02.001.

## References

[1] K. Aspelund, Designing: An Introduction, Fairchild Books, New York, NY, 2014.

[2] J. Heer, B. Shneiderman, Interactive dynamics for visual analysis, Communications of the ACM 55 (2) (2012) 45, http://dx.doi.org/10.1145/2133416.2146416.

[3] S.K. Card, J.D. Mackinlay, B. Shneiderman, Readings in Information Visualization: Using Vision to Think, Morgan Kaufmann, San Francisco, CA, 1999.

[4] J.-d. Fekete, J.J.V. Wijk, J.T. Stasko, C. North, The value of information visualization, Information Visualization 4950 (2008) 1–18, http://dx.doi.org/10.1007/978-3-540- 70956-5\_1.

[5] A.-L. Barabási, Linked: how everything is connected to everything else and what it means for business, Science, and Everyday Life, Plume (2003)arXiv:0806.1610, http://dx.doi.org/10.1146/annurev.soc.30.020404.104342.

[6] D.J. Watts, The new science of networks, Annual Review of Sociology 30 (1) (2004) 243–270, http://dx.doi.org/10.1146/annurev.soc.30.020404.104342.

[7] C. Holsapple, A. Lee-Post, R. Pakath, A unified foundation for business analytics, Decision Support Systems 64 (2014) 130–141, http://dx.doi.org/10.1016/j.dss. 2014.05.013.

[8] O. Ben-Assuli, Assessing the perception of information components in financial decision support systems, Decision Support Systems 54 (1) (2012) 795–802, http://dx.doi.org/10.1016/j.dss.2012.09.007.

[9] B. Kamsu-Foguem, G. Tchuenté-Foguem, L. Allart, Y. Zennir, C. Vilhelm, H. Mehdaoui, D. Zitouni, H. Hubert, M. Lemdani, P. Ravaux, User-centered visual analysis using a hybrid reasoning architecture for intensive care units, Decision Support Systems 54 (1) (2012) 496–509, http://dx.doi.org/10.1016/j.dss.2012.06.009.

[10] R.C. Basole, M.L. Braunstein, V. Kumar, H. Park, M. Kahng, D.H.P. Chau, A. Tamersoy, D.A. Hirsh, N. Serban, J. Bost, B. Lesnick, B.L. Schissel, M. Thompson, Understanding variations in pediatric asthma care processes in the emergency department using visual analytics, Journal of the American Medical Informatics Association (2015), http://dx.doi.org/10.1093/iamia/ocu016 (ocu016).

[11] T.J. Overbye, J.D. Weber, K.J. Patten, Analysis and visualization of market power in electric power systems, Decision Support Systems 30 (3) (2001) 229–241, http://dx.doi.org/10.1016/S0167-9236(00)00101-9.

[12] R.C. Basole, C.D. Seuss, W.B. Rouse, IT innovation adoption by enterprises: knowledge discovery through text analytics, Decision Support Systems 54 (2) (2013) 1044–1054, http://dx.doi.org/10.1016/j.dss.2012.10.029.

[13] R.C. Basole, Visual business ecosystem intelligence: lessons from the field, IEEE Computer Graphics and Applications 34 (5) (2014) 26–34, http://dx.doi.org/10.1109/ MCG.2014.104.

[14] I. Herman, G. Melancon, M. Marshall, Graph visualization and navigation in information visualization: a survey, IEEE Transactions on Visualization and Computer Graphics 6 (1) (2000) 24–43, http://dx.doi.org/10.1109/ 2945.841119.

[15] C. Speier, The influence of information presentation formats on complex task decision-making performance, International Journal of Human-Computer Studies 64 (11) (2006) 1115–1131, http://dx.doi.org/10.1016/j.ijhcs.2006.06.007.

[16] J. Gettinger, S.T. Koeszegi, M. Schoop, Shall we dance? - the effect of information presentations on negotiation processes and outcomes, Decision Support System 53 (1) (2012) 161–174, http://dx.doi.org/10.1016/j.dss.2012.01.001.

[17] W. Hong, J.Y. Thong, K.Y. Tam, The effects of information format and shopping task on consumers' online shopping behavior: a cognitive fit perspective, Journal of Management Information Systems 21 (3) (2004) 149–184.

[18] J. Gettinger, E. Kiesling, C. Stummer, R. Vetschera, A comparison of representations for discrete multi-criteria decision problems, Decision Support Systems 54 (2) (2013) 976-985 http://dx.doiorg/10.1016/i.dss.2012.10.023

[19] H. Park, R.C. Basole, Bicentric diagrams: design of a graph-based relational set visualization technique, Proceedings of the 33rd Annual ACM Conference Extended Abstracts on Human Factors in Computing Systems—CHI EA ‘15, ACM Press, New York, New York, USA 2015, pp. 1815–1820, http://dx.doi.org/10.1145/ 2702613.2732752

[20] R.C. Basole, M.A. Bellamy, Visual analysis of supply network risks: insights from the electronics industry, Decision Support Systems 67 (2014) 109–120, http://dx.doi. org/10.1016/j.dss.2014.08.008.

[21] R.C. Basole, M.G. Russell, J. Huhtamäki, K. Still, N. Rubens, K. Still, H. Park, Understanding business ecosystem dynamics: a data driven approach ACM Transactions on Management Information Systems 6 (2) (2015) 1–32, http://dx. doi.org/10.1145/2724730

[22] R.C. Basole, H. Park, V. Kumar, M.L. Braunstein, J. Bost, D.H. Chau, M. Kahng, Bicentric visualization of pediatric asthma care process activities, Proceedings of IEEE VIS 2014 Workshop of Electronic Health Records, IEEE, 2014.

[23] M.S. Granovetter, The strength of weak ties, American Journal of Sociology 78 (6) (1973) 1360–1380, http://dx.doi.org/10.2307/2776392.

[24] J.F. Courtney, Decision making and knowledge management in inquiring organizations: toward a new decision-making paradigm for DSS, Decision Support Systems 31 (1) (2001) 17–38, http://dx.doi.org/10.1016/S0167-9236(00)00117-2.

[25] J. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2) (2002) 111–126, http://dx.doi.org/10.1016/S0167-9236(01)00139-7.

[26] G. Ahuja, Collaboration networks, structural holes, and innovation: a longitudinal study, Administrative Science Quarterly 45 (3) (2000) 425–455.

[27] E. Condon, B. Golden, S. Lele, S. Raghavan, E. Wasil, A visualization model based on adjacency data, Decision Support Systems 33 (4) (2002) 349–362, http://dx.doi. org/10.1016/S0167-9236(02)00003-9.

[28] C.C. Yang, H. Chen, K. Hong, Visualization of large category map for internet browsing, Decision Support Systems 35 (1) (2003) 89–102, http://dx.doi.org/10. 1016/S0167-9236(02)00101-X.

[29] G. Shmueli, W. Jank, A. Aris, C. Plaisant, B. Shneiderman, Exploring auction databases through interactive visualization, Decision Support Systems 42 (3) (2006) 1521–1538, http://dx.doi.org/10.1016/j.dss.2006.01.001.

[30] M.J. Eppler, K.W. Platts, Visual strategizing, Long Range Planning 42 (1) (2009) 42–74, http://dx.doi.org/10.1016/j.lrp.2008.11.005.

[31] J. Heer, M. Bostock, V. Ogievetsky, A tour through the visualization zoo, Communications of the ACM 53 (6) (2010) 59, http://dx.doi.org/10.1145/ 1743546.1743567.

[32] P.C. Wong, R.D. Bergeron, 30 Years of multidimensional multivariate visualization, Scientific Visualization, Overviews, Methodologies, and Techniques, IEEE Computer Society 1994, pp. 3–33.

[33] T. Asahi, D. Turo, B. Shneiderman, Using treemaps to visualize the analytic hierarchy process, Information Systems Research 6 (4) (1995) 357–375.

[34] J. Stasko, R. Catrambone, M. Guzdial, K. McDonald, An evaluation of space-filling information visualizations for depicting hierarchical structures, International Journal of Human-Computer Studies 53 (5) (2000) 663–694, http://dx.doi.org/10. 1006/ijhc.2000.0420.

[35] A. Sundararajan, F. Provost, G. Oestreicher-Singer, S. Aral, Research commentaryinformation in digital, economic, and social networks, Information Systems Research 24(4) (2013) 883–905.

[36] N. Venkatraman, C.-H. Lee, Preferential linkage and network evolution: a conceptual model and empirical test in the US video game sector, Academy of Management Journal 47 (6) (2004) 876–892, http://dx.doi.org/10.2307/20159628

[37] J. Xu, H. Chen, Criminal network analysis and visualization, Communications of the ACM 48 (6) (2005) 100–107, http://dx.doi.org/10.1145/1064830.1064834.

[38] M. Trier, Research note-towards dynamic visualization for understanding evolution of digital communication networks, Information Systems Research 19 (3) (2008) 335–350.

[39] M. Keith, H. Demirkan, M. Goul, The influence of collaborative technology knowledge on advice network structures, Decision Support Systems 50 (1) (2010) 140–151, http://dx.doi.org/10.1016/j.dss.2010.07.010.

[40] L. Bizzi, A. Langley, Studying processes in and around networks, Industrial Marketing Management 41 (2) (2012) 224-234. http://dx,doi.org/10.1016/j. indmarman,2012.01.007.

[411 P. Fox. I. Hendler, Changing the equation on scientific data visualization, Science 331 (6018) (2011) 705–708, http://dx.doi.org/10.1126/science.1197654.

[42] J. Thomas, K. Cook, A visual analytics agenda, IEEE Computer Graphics and Applications 26 (1) (2006) 10–13, http://dx.doi.org/10.1109/MCG.2006.5.

[43] W.A. Pike, J. Stasko, R. Chang, T.A. OConnell, The science of interaction, Information Visualization 8 (4) (2009) 263–274, http://dx.doi.org/10.1057/ivs.2009.22.

[44] B. Alsallakh, L. Micallef, W. Aigner, H. Hauser, S. Miksch, P. Rodgers, Visualizing sets and set-typed data: state-of-the-art and future challenges. Eurographics Conference on Visualization (EuroVis), 2014

[45] B. Alsallakh, W. Aigner, S. Miksch, H. Hauser, Radial sets: interactive visual analysis of large overlapping sets, IEEE Transactions on Visualization and Computer Graphics 19 (2013) 2496–2505, http://dx.doi.org/10.1109/TVCG.2013.184.

[46] N. Watanabe, M. Washida, T. Igarashi, Bubble clusters: an interface for manipulating spatial aggregation of graphical objects, ACM Symposium on User Interface Software and Technology 2007, pp. 173–182, http://dx.doi.org/10.1145/1294211.1294241.

[47] J. Heer, D. Boyd, Vizster: visualizing online social networks, IEEE Symposium on Information Visualization (InfoVis) 2005, pp. 33–40, http://dx.doi.org/10.1109/ INFVIS.2005.1532126.

[48] C. Collins, G. Penn, S. Carpendale, Bubble sets: revealing set relations with isocontours over existing visualizations, IEEE Transactions on Visualization and Computer Graphics 15 (2009) 1009–1016, http://dx.doi.org/10.1109/TVCG.2009.122.

[49] J. Stasko, C. Görg, Z. Liu, R. Spence, Jigsaw: supporting investigative analysis through interactive visualization, Information Visualization 7 (2) (2008) 118–132, http://dx. doi org/10.1057/palgrave ivs 9500180

[50] K. Misue, Anchored maps: visualization techniques for drawing bipartite graphs, Human–Computer Interaction, Interaction Platforms and TechniquesSpringer, Berlin Heidelberg 2007 pp. 106–114.

[51] M. Krzywinski, J. Schein, I. Birol, J. Connors, R. Gascoyne, D. Horsman, S.J. Jones, M.A Marra, Circos: an information aesthetic for comparative genomics, Genome Research 19 (9) (2009) 1639–1645, http://dx.doi.org/10.1101/gr.092759.109.

[52] S. Milgram, The small-world problem, Psychology Today.

[53] R.C. Basole, H. Park, B.C. Barnett, Coopetition and convergence in the ICT ecosystem, Telecommunications Policy 39 (7) (2015) 537–552, http://dx.doi.org/10.1016/j. telpol.2014.04.003.

[54] S.H. Strogatz, Exploring complex networks, Nature 410 (6825) (2001) 268–276 http://dx.doi.org/10.1038/35065725.

[55] J. Hopcroft, R. Tarjan, Algorithm 447: efficient algorithms for graph manipulation, Communications of the ACM 16 (6) (1973) 372–378, http://dx.doi.org/10.1145/ 362248.362272

[56] M.A. Schilling, C.C. Phelps, Interfirm collaboration networks: the impact of large-scale network structure on firm innovation, Management Science 53 (7) (2007) 1113–1126.

[57] L. Rosenkopf, M.A. Schilling, Comparing alliance network structure across industries: observations and explanations, Strategic Entrepreneurship Journal 1 (3–4) (2007) 191–209, http://dx.doi.org/10.1002/sej.33.

[58] M. Bostock, V. Ogievetsky, J. Heer, D3: data-driven documents, IEEE Transactions on Visualization and Computer Graphics 17 (12) (2011) 2301–2309, http://dx.doi.org/ 10.1109/TVCG.2011.185.

[59] A. Hagberg, P. Swart, D.S. Chult, Exploring Network Structure, Dynamics, and Function Using NetworkX, Tech. rep. Los Alamos National Laboratory (LANL), 2008

[60] H. Park, K. Lee, Dependence clustering, a method revealing community structure with group dependence, Knowledge-Based Systems 60 (2014) 58–72, http://dx. doi.org/10.1016/j.knosys.2014.01.004.

[61] R. Basole, A. Qamar, H. Park, C. Paredis, L. McGinnis, Visual analytics for early-phase complex engineered system design support, IEEE Computer Graphics and Applications 35 (2) (2015) 41–51, http://dx.doi.org/10.1109/MCG.2015.3.

[62] G. Vasudeva, A. Zaheer, E. Hernandez, The embeddedness of networks: institutions, structural holes, and innovativeness in the fuel cell industry, Organization Science

[63] S. Carpendale, Evaluating Information Visualizations, in: Information Visualization, Springer Berlin Heidelberg, Berlin, Heidelberg, 2008 19–45, http://dx.doi.org/10. 1007/978-3-540-70956-5\_2

[64] H. Lam, E. Bertini, P. Isenberg, C. Plaisant, S. Carpendale, Empirical studies in information visualization: seven scenarios, IEEE Transactions on Visualization and Computer Graphics 18 (9) (2012) 1520–1536, http://dx.doi.org/10.1109/ TVCG.2011.279.

[65] M. Tory, User studies in visualization: a reflection on methods, Handbook of Human Centric Visualization, Springer 2014, pp. 411–426.

[66] B. Shneiderman, C. Plaisant, Strategies for evaluating information visualization tools: multi-dimensional in-depth long-term case studies, Proceedings of the 2006 AVI Workshop on Beyond Time and Errors: Novel Evaluation Methods for Information Visualization, ACM 2006, pp. 1–7.

[67] J.T. Stasko, Value-Driven Evaluation of Visualizations, in: Proceedings of the Workshop: Beyond Time and Errors—Novel Evaluation Methods for Visualization (Paris, France, November 2014), 2014.

[68] R. Amar, J. Eagan, J. Stasko, Low-level components of analytic activity in information visualization, IEEE Symposium on Information Visualization (InfoVis) 2005, pp. 111–117, http://dx.doi.org/10.1109/INFVIS.2005.1532136.

[69] R. Chang, C. Ziemkiewicz, T.M. Green, W. Ribarsky, Defining insight for visual analytics, IEEE Computer Graphics and Applications 29 (2009) 14–17, http://dx. doi.org/10.1109/MCG.2009.22.

[70] J. Lamping, R. Rao, P. Pirolli, A focus + context technique based on hyperbolic geometry for visualizing large hierarchies, Proceedings of the SIGCHI Conference on Human Factors in Computing Systems - CHI '95 ACM Press New York New York, USA 1995, pp. 401–408, http://dx.doi,org/10.1145/223904.223956

[71] L. Wilkinson, Exact and approximate area-proportional circular Venn and Euler diagrams, IEEE Transactions on Visualization and Computer Graphics 18 (2012) 321–331, http://dx.doi.org/10.1109/TVCG.2011.56

[72] N.H. Riche, T. Dwyer, Untangling Euler diagrams, IEEE Transactions on Visualization and Computer Graphics 16 (2010) 1090 1099, http://dx.doi.org/10.1109/TVCG. 2010.210.

[73] K. Dinkla, M.J. van Kreveld, B. Speckmann, M.a. Westenberg, Kelp diagrams: point set membership visualization, Computer Graphics Forum 31 (2012) 875–884, http://dx.doi.org/10.1111/j.1467–8659.2012.03080.x.

[74] M. Dork, N. Henry Riche, G. Ramos, S. Dumais, PivotPaths: strolling through faceted information spaces, IEEE Transactions on Visualization and Computer Graphics 18 (12) (2012) 2709–2718, http://dx.doi.org/10.1109/TVCG.2012.252.

Hyunwoo Park is a postdoctoral fellow of the Tennenbaum Institute at the Georgia Institute of Technology. His research interests include technological innovation, platform strategy, visual analytics, and computational strategy science. Park has a PhD in industrial engineering from the Georgia Institute of Technology and a master's in information management and systems from the University of California, Berkeley. Contact him at, hwpark@gatech.edu.

Rahul C. Basole is an associate professor in the School of Interactive Computing, the associate director for Enterprise Transformation in the Tennenbaum Institute/IPaT, and an affiliated faculty member in the GVU Center at the Georgia Institute of Technology. He is also a visiting scholar in HSTAR at Stanford University and a Fellow of the Batten Institute at the Darden School of Business. He is also the editor-in-chief of the Journal of Enterprise Transformation, His research and teaching focuses on computational enterprise science, information visualization, and strategic decision support. He holds a PhD in industrial and systems engineering from the Georgia Institute of Technology. Contact him at basole@gatech edu
