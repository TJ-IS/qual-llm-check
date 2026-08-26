---
otero_id: 6958
otero_key: "WU7EBXH9"
title: "Design and evaluation of improvement method on the web information navigation – A stochastic search approach"
authors: "Benjamin P.-C. Yen; Y.-W. Wan"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.12.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Design and evaluation of improvement method on the web information navigation – A stochastic search approach

Benjamin P.-C. Yen <sup>a,</sup>⁎, Y.-W. Wan <sup>b</sup>

<sup>a</sup> School of Business, The University of Hong Kong, Pokfulam Road, Hong Kong

<sup>b</sup> Graduate Institute of Global Operations Strategy and Logistics Management, National Dong Hwa University, Hualien, Taiwan

## a r t i c l e i n f o

Article history: Received 21 October 2008 Received in revised form 5 September 2009 Accepted 10 December 2009 Available online 16 December 2009

Keywords: Stochastic shortest path Web Navigation

## a b s t r a c t

With the advent of fast growing Internet and World Wide Web (the Web), more and more companies enhance the business competitiveness by conducting electronic commerce. At the same time, more and more people gather or process information by sur<sup>fi</sup>ng on the Web. However, due to unbalanced Web traf<sup>fi</sup>c and poorly organized information, users suffer from slow communication and disordered information. To improve the situation, information providers can analyze the traf<sup>fi</sup>c and Uniform Resource Locator (URL) counters to adjust the information layering and organization; nevertheless, heterogeneous navigation patterns and dynamic <sup>fl</sup>uctuating Web traf<sup>fi</sup>c complicate the improvement process. Alternatively, improvement can be made by giving direct guidance to the surfers in navigating the Web sites. In this paper, information retrieval on a Web site is modeled as a Markov chain associated with the corresponding dynamic Web traf<sup>fi</sup>c and designated information pages. We consider four models of information retrieval based on combination of the level of skill or experience of the surfers as well as the degree of navigation support by the sites. Simulation is conducted to evaluate the performance of the different types of navigation guidance. In addition, we evaluate the four models of information retrieval in terms of complexity and applicability. The paper concludes with a research summary and a direction for future research efforts.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Information plays an indispensable role in the world. The network and information systems have changed the way people communicate with each other as well as expedited the process to obtain the information that matches their interests. Everyday hundreds of millions of transactions <sup>fl</sup>ow through the network all over the world. Any information can be transferred from one place to another only within few seconds. Together with the growth of the needs of information, the web pages on the Internet grow explosively during the past few years and such increase is expected to be more acute going forward.

The abundance of the URL's apparently creates a great value for all the visitors by allowing them to retrieve comprehensive information from the Web. Web page owners, at the same time, bene<sup>fi</sup>t from the advertisement opportunities when visitors surf their web pages. However, any lack of organization of the voluminous information may encumber the searching performance. Visitors spend astounding amount of time in navigating through the useless or redundant pages. To tackle the problem, Web page owners need to invest to update and reorganize the information for their Web pages on an on-going basis. As a result, there are questions concerning both the visitors and Web page owners that need to be answered: What do Web page owners need to take into account in addition to the Web pages (i.e. information content) in the design of Web site? How can it be enhanced on the Web site to improve information retrieval? How to justify the requirement, necessity, and cost for such improvements? How to balance the cost and bene<sup>fi</sup>t of such improvements? In answering these questions, research has been conducted in three areas: (1) Web site customization based on the user access information; (2) agents based intelligence search for information retrieval and discovery; and (3) intelligence browser and the collection of user information.

Perkowitz and Etzioni [23,24] propose an Arti<sup>fi</sup>cial Intelligence approach to create the Adaptive Web Site, which can improve the site organization based on the user access log with the assumption that each originating computer corresponds to a particular user. Yan et al. [34] propose the use of access patterns to generate hyperlinks, which are captured in the access log and analyzed of<sup>fl</sup>ine in an interval basis, to improve the information access. Wang et al. [32] propose a personalized <sup>fi</sup>ltering model to <sup>fi</sup>lter and rank the product information with linear functions on the user preference. Chen and Kuo [6] propose a personalized information retrieval system based on the user pro<sup>fi</sup>le modeled as the Semantic Relevance (SR) and Co-occurrence (CO) of keywords to capture the real meaning of user query.

The research in the second area focuses on seeking for the information on the Internet. Cheung et al. [8] propose a model of four-level classi<sup>fi</sup>cation tool of learning the behavior of both information user and information source. Chang et al. [5] present a Site Traveling Algorithm (STA) to discover the relevant information, in which the relevance of the retrieved document is evaluated with the content popularity and richness (CPR). Yang et al. [35] present the development of intelligent personal Internet agent based on automatic textual analysis of Internet document and hybrid simulated annealing algorithm. Tu and Hsiang [31] propose an Interactive Information Retrieval (IIR) agent architecture to handle group knowledge and preference, and to keep track of the individual user pro<sup>fi</sup>le. Teng et al. [30] propose a scalable method for parallel processing in both information crawling/gathering and processing.

The third area of research concerns navigation assistance for user during the browsing process. Joachims et al. [14] introduce the Web-Watcher, based on a learning approach with user feedback to improve the quality of interactive navigation advice. Similarly, Liaberman [21] introduces the intelligent agent, Letiza, which works with conventional web browsers to keep track of the user browsing behavior and interests. Furthermore, Berghel et al. [2] present a web browser called the “Cyberbrowser” to customize the information access to the content within the web page, which include keyword and sentences extraction according to user selection. Lin et al. [22] describe an approach for capturing user access patterns on the Web by addressing the limitation of the Web servers which only recognize the proxy servers instead of the individual users. Richardson [27] does a comparison on the existing tools to gather the access information on the Internet, such as visitor counter and guest book.

The literature above shows the modeling of the information retrieval mostly is based on database models and data mining techniques. The analysis centers on the user behavior patterns largely for the global Web information retrieval. There are few studies for the analysis on site structure for information retrieval as optimization problems. There are two types of models for problem formulation — deterministic models and stochastic models.

Gibson et al. [12] and Chakrabarti et al. [4] de<sup>fi</sup>ne the Web sites as “authorities” and “hub” in isolation and conclude that a respected authority is a page that is referred to by many good hubs and a useful hub is a location that points to many valuable authorities. Donato et al. [9] mine the inner structure of the Web graph and propose a series of measurements on the Web. They <sup>fi</sup>nd that graph does not exhibit self similarity within its components and their inner structure is quite distinct. Chakrabarti et al. [3] develop algorithms that exploit the hyperlink structure of the Web for information discovery and categorization, the construction of high quality resource lists, and the analysis of on-line hyperlinked communities. Eiron and McCirley [10] investigate the construction of data models of the Web that capture the hierarchical nature of the Web and some crucial features of the link graph. Yen [36] de<sup>fi</sup>nes four types of Web page accessibility models proposes the guidelines to balance accessibility and popularity. Kleinberg et al. [15] describe two algorithms that operate on the Web graph, addressing problems from Web search and automatic community discovery.

Sarukkai [28] uses a Markov Chain model based on the user access information for link prediction and path analysis. Levene et al. [19] derive Zipf's rank frequency law from an absorbing Markov chain model of surfers' behaviour assuming that less probable navigation trails are, on average, longer than more probable ones. Levene and Loizou [17,18] formulate a hypertext database as a graph and propose a probability approach to <sup>fi</sup>nd the trail to match the query. Kumar et al. [16] propose a stochastic model of the web graph to show additional properties of the random graph. Levene et al. [20] extend the evolutionary model of the Web graph by including a nonpreferential component and viewing the stochastic process in terms of an urn transfer model. Zin and Levene [37] propose that information on the topology is important for useful exploration and can also help to reduce the feeling of disorientation that users may experience.

From the review above, it should be noted that there lacks the consideration of dynamic factors (such as dependent reverse links and user familiarity with Web navigation) of assessing information from the Web in analyzing and evaluating the access models. In this research, we propose a graph-based structure with stochastic properties (such as traf<sup>fi</sup>c conditions and navigation information) and various dynamic policies to guide the users in accessing information. The proposed approach captures the essence of the sur<sup>fi</sup>ng process: A surfer surfs among web pages of a site according to the structure of pages as re<sup>fl</sup>ected from the hyperlinks, waiting for the loading of new web pages as he triggers hyperlinks. The process is similar to an entity jumping from the source to the destination node of a graph, with web pages as nodes, hyperlinks as arcs, loading times as distances among nodes, and some stochastic properties and dynamic policies as the sur<sup>fi</sup>ng behavior and some as the navigation guidance provided by web pages. All these web structures and routing policies are modeled discrete-time Markov chains, and the expected time for a surfer to arrive at his destination is calculated based on both dynamic and stochastic shortest paths.

The level of skill or experience of the surfers as well as the degree of guidance supported by the sites is two of the major issues for information retrieval on the Web. Four models are considered in our research to re<sup>fl</sup>ect these two issues: inexperienced surfers on guidance-less sites (ISL), where totally inexperienced surfers sur<sup>fi</sup>ng among web pages that do not provide any navigation guidance, leading to surfers randomly moving among pages; experienced surfers on guidance-less sites (ESL), where the web pages do not provide guidance but the surfers are experienced, i.e., they only trigger unvisited pages as they search for their required information; sites with the Mean-Path Guidance (MPG), where the navigation guidance of a site is in terms of static values of the mean loading times of web pages; and sites with the Known-First-Arc Guidance (KFA), where the navigation guidance of a site considers the real-time loading time of the next page with mean loading times for future pages.

The rest of the paper is organized as the following. Section 2. contains the problem description and formulation. Section 3 sets out the discussion on the four searching models of navigation guidance. Section 4 demonstrates the simulation result and comparison on complexity and applicability for the four proposed models. The paper concludes with a research summary and a direction for future research efforts.

## 2. Preliminary — problem description

Consider a situation where data are distributed over a computer network that is composed of switches and cables. A switch contains information about (i) the cable capacity; and (ii) the estimated time for the packet going from each neighboring switch to the destination (typically in the form of look-up table). Whenever a data-packet arrives at a switch, the switch to visit next needs to be determined based on the real time information on the network capacity. A routing strategy is used to utilize the real-time information to form dynamically a path of minimized costs for data delivery. We, therefore, proposed to improve the path for data delivery by way of adding cables (the aggressive approach) and/or deleting cables (the passive approach) in between the respective switches to improve the data delivery performance. By the same token, we propose to improve the structure of the Web site by adding or deleting hyperlinks on the Web pages, so that the Web surfers can navigate to the destination page most ef<sup>fi</sup>ciently. In this section, we <sup>fi</sup>rst model the Web navigation as graph traverse problem. We further classify the problems based on various Web structure properties. The model is extended based on the “explorative transformation”.

## 2.1. Problem formulation

A Web site comprises a number of Web pages and each Web page may have a number of hyperlinks connecting to other pages. Each Web page is associated with a loading time, which varies in proportion to the page content and the network traf<sup>fi</sup>c conditions. Vertices and arcs are denoted as follows:

Vertices: $V { = } \{ v _ { 1 } , v _ { 2 } , . . . v _ { n } \}$ . Each $\nu _ { i } ( i = 1 , 2 , \dots n )$ refers to one page.

Arcs: $E = \{ [ v _ { i } , v _ { j } ]$ or $e _ { i j }$ | There is a hyperlink in page i pointing to page j}. The arc connecting v<sub>i</sub> to v<sub>j</sub> denotes a hyperlink from page i to page j.

The hyperlinks are directed, so is the network. Since each Web page has a loading time, the corresponding vertex in the network is assigned a weight representing such loading time. Naturally, the loading time of a Web page is directly determined by the size of the page contents, such as text, images and sound/video clips, and network conditions. Among these factors, the page size (x ) is the most dominating one. Hence, it is assigned as the weight of vertex to re<sup>fl</sup>ect the download time:

$$
\begin{array}{l} w: V \to R ^ {+} \\ w (v _ {i}) = x _ {i} \end{array}
$$

Therefore, the network is denoted as $\vec { G } = ( V , E , w )$ , which is a directed graph in which a weight is associated with each vertex. For example, let A be the start and L the destination page for a surfer on a site of web structure as shown in Fig. 1. There are many ways to reach the destination L from A. Not only that there are multiple paths from A to L, there are loops in the seemingly directed graph. All web browsers provide the function to return to the previous page, i.e., a path from A to L can actually be of the form A–C–A–C–G–L. The length of the path depends not only on the sequence of nodes, but also on whether the cache function is enabled or not. If it is enabled, the length of loading time for each reverse link becomes zero; otherwise, each reverse link bears the same loading time for the previous page.

In short, the actual time taken for a surfer to move from A to L depends on the web structure, the experience of the surfer, and the type of navigation guidance provided for the surfer. For a given web structure, the time is determined by the latter two factors. For the web structure as shown in Fig. 1, suppose that based on historical record, on average A–C–G–L is the shortest path from A to L. If the surfer is inexperienced and the web does not provide any navigation guidance, the surfer may take a random walk on the network, with the pageback function as the means to move in the opposition direction of the directed arcs. If the surfer is experienced, his search will be more careful; pages visited before will not be re-visited unless there is no choice. With navigation guidance provided by the web, the surfer may be guided to select A–C–G–L based on the long-term average loading times of pages, or different paths according to the traf<sup>fi</sup>c jam during navigation. In case the surfer needs more than one destination, the problem becomes multi-destination, i.e., we need to <sup>fi</sup>nd the shortest collection of paths that cover all the destination nodes. If the hyperlinks on web pages can be changed, no matter as a static web design problem that changes once for a long while, or a dynamic problem that hyperlinks are highlighted according to traf<sup>fi</sup>c condition, then effectively the web structure is changed with the change in hyperlinks.

## 2.2. Problem properties

We elaborate the model for the Web-based information retrieval by two dimensions — structure properties and navigation properties. The structure properties concern the static properties of the Web site structure, including the server capacity and the cache mechanism. The navigation properties refer to the dynamic aspects of information retrieval, including single or multiple root pages and destination pages, constraints on the navigation path, etc. Both dimensions have signi<sup>fi</sup>cant impact on problem modeling and problem solving.

## 2.2.1. Structure properties

The sever performance might be inversely proportional to the number of the users making simultaneous page requests. This is valid both for an individual page and for a number of pages forming the whole or part of a Web site. One particular characteristic for the Web site structure is the “conditional reverse link” — the hyperlink visited enables the corresponding reverse link. If we consider the cache function to be enabled, the length of loading time for each reverse link becomes zero; otherwise, each reverse link bears the same loading time as the previous page. The cache, depending on its size constraint or time limit constraints, can store both the address and the content of a Web page. Furthermore, hyperlinks can be bi-directional (i.e. the links in both directions are valid in the original graph) and multiple (i.e. multiple identical or non-identical links between nodes).

## 2.2.2. Navigation properties

Navigation can start from a single root page (entry page) or multiple root pages (direct page address). Similarly, the destination page can also be a single page or a group of the pages. Navigation can be constrained by path length or browsing time. Objectives of navigation may include minimizing retrieval time, maximizing information quality (completeness and relevancy) and minimizing path length (radical distance form the root and number of pages visited). The decision making during navigation process can be of static or dynamic. In the static model, all the nodes along the navigation path are determined at once from the beginning of the navigation process; however, in the dynamic model, the next node to visit is only determined one at a time from the immediate proceeding node.

![](/api/attachments/WU7EBXH9/fulltext/images/a3eccf514e1da52213e6b24f69fe5143e6bfe52bafb7e51b8cef45f3f9d190ba.jpg)  
Fig. 1. Example — a Web site and its graph structure.

## 2.3. Problem transformation

In addition to the structure and navigation properties, we adopt the explorative expansion approach to address the cache capability of a navigation process. The explorative expansion approach for conditional reverse link is based on the graph traversal (either breath <sup>fi</sup>rst or depth <sup>fi</sup>rst search) on a link by link basis. The process starts with the root node as an initial component. For each traverse on the new link, we consider the source node, the destination node, and the link between them. A component is de<sup>fi</sup>ned as a graph. A new expansion component is constructed for the destination part and it is the combination of a replica of the original component, the links of both direction as the newly explored links, and the destination node if it is not included in the original component. The exploring link will connect the source node in the original component to the destination node in the new expansion component.

For example, Fig. 2(A) shows an original Web site graph. To start the expansion process, we construct an initial component with only root node (i.e. node A) as shown on the top of Fig. 2(B). If we explore the link $e _ { \mathsf { A B } }$ in the next, we construct the new expansion component with node A, node B, the link $e _ { \mathsf { A B } }$ and the link $e _ { \mathrm { B A } } .$ . A link is added between the source node (i.e. node A) in original component to the destination node (i.e. node B) in the newly generated expansion component. The whole process will complete after all the links are explored. Fig. 2(B) is the complete expansion of the original Web graph in Fig. 2(A). The reverse link in the expansion components represents the “back” function. All the distances in the expansion components are zero and the length of a link between any two components is the same as that in the original Web graph. For the purpose of simplicity, no subscript is added in the expansion components to differentiate one node from another.

![](/api/attachments/WU7EBXH9/fulltext/images/ef213a59301c75e4ce4e64578146b612a41ced8e14f39aff3bdc80f0a0e6447d.jpg)  
Fig. 2. Example of explorative expansion.

The process can be described as an algorithm as follows. For simplicity, we assume the original Web graph $G ^ { 0 } = ( V , A )$

Step 1. The original component $G ^ { \mathrm { e } } = ( V ^ { \mathrm { e } } , A ^ { \mathrm { e } } )$ only consists of the root node, i.e. $G = ( \{ \nu _ { 0 } \} , \{ \} )$

Step 2. The set of the links to be explored $A ^ { x } { = } A .$

Step 3. {e<sub>ij</sub> | v<sub>i</sub> $V ^ { \mathrm { e } }$ and $e _ { i j } { \in } A ^ { x } \}$

Step 4. {G′| Quali<sup>fi</sup>ed components with $\nu _ { i }$ but without $e _ { i j } \}$

Step 5. Construct the new expansion component $G ^ { \prime \prime } = G ^ { \prime } + \{ e _ { i 2 j 2 } ,$ $e _ { j 2 i 2 } \} + \{ \nu _ { j 2 } \}$

Step 6. If exists already, then ${ \cal G } = { \cal G } + \{ e _ { i 1 j 2 } \}$

Step 7. Otherwise, include new expansion component $G = G ^ { \prime } + G ^ { \prime \prime } +$ $\{ e _ { i 1 j 2 } \}$

Step 8. Go to Step 4 if there is any $G ^ { \prime }$

Step 9. Go to Step 3 if there is any $e _ { i j }$

Step 10. $A ^ { x } { = } A ^ { x } { - } e _ { i j }$

Step 11. Go to Step $3 { \mathrm { ~ i f ~ } } A ^ { x } \neq 0$

(Remark: In Step $6 , 7 ,$ and $8 , i _ { 1 }$ and $j _ { 1 }$ are the node subscripts in the original component; $i _ { 2 }$ and $j _ { 2 }$ are the node subscripts in the new component).

The number of the expansion components is dependent on the number of the links in the original graph. Two extreme examples, namely chain structure and star structure, represent the lower bound $( \mathrm { i . e . ~ } n \times ( n + 1 ) / 2 = ( n ^ { 2 } + n ) / 2 )$ and upper bound $( { \mathrm { i . e . ~ } } n ^ { 2 } \times n = n ^ { 3 } )$ respectively, where n is the number of nodes. In this study, we focus on cases with the assumption of single-destination and disabled cache.

## 3. Searching models

The level of skill or experience of the surfers as well as the degree of navigation support by the sites may vary. An inexperienced surfer may browse randomly and load repeated pages, while an experienced one may browse systematically and only load a page again if necessary. An immature site may not provide any navigation information for surfers, while a well-designed one may provide navigation information about the site structure and the expected loading time of the respective pages. A sophisticated site may even provide real-time navigation information changing simultaneously with the traf<sup>fi</sup>c of the Web.

For simplicity, we assume that the cache function is disabled and that the surfer has only one destination in mind. Enabled cache function and multiple destinations are intended for future extension works. We consider four simulation models based on the combination of the level of skill or experience of the surfers as well as the degree of navigation support by the sites: inexperienced surfers on guidanceless sites (ISL), experienced surfers on guidance-less sites (ESL), sites with the Mean-Path Guidance (MPG), and sites with the Known-First-Arc Guidance (KFA). The classi<sup>fi</sup>cation of the four models is based on the navigation guidance and repeatable navigation as shown in the Fig. 3. The information retrieval on the Web site in these four models can be described as discrete Markov Chains as follows [28]. A discrete Markov chain model can be de<sup>fi</sup>ned by the tuple (S, T, λ). S corresponds to the state space (set of pages of Web site), T is a matrix representing transition probabilities from one state to another (i.e. from one page to another page), and λ is the initial probability distribution of the states in S. The detail is discussed in the following the subsections. The modeling is mainly based on the work of Glover et al. [13], Shier and Witzgall [29], Psaraftis and Tsitsiklis [26], Geetha and Nair [11], Polychronopoulos and Tsitsiklis [25] and Cheung [7].

## 3.1. Inexperienced surfers on guidance-less sites (ISL)

Consider a totally inexperienced surfer on a site without any navigation guidance. The surfer moves randomly, possibly back and forth, among the pages, and picks links in a page arbitrarily. The movement of such a surfer can be modeled by a random walk on a connected graph, and the page search process can be modeled as a discrete-time Markov chain [28].

<table><tr><td rowspan="3">Repeatable Navigation</td><td>No</td><td>Yes</td></tr><tr><td>No</td><td>ESLExperienced surferson guidance-less sites</td></tr><tr><td>Yes</td><td>ISLInexperienced surferson guidance-less sites</td></tr></table>

Fig. 3. Classi<sup>fi</sup>cation of the four models.

Refer to the site structure in Fig. 1. Let $X _ { n } = s$ if the surfer is at page s after the nth move (page loading). Take $X _ { 1 } = A ,$ because A is the root page. In general, if a surfer starts from page s with probability $p _ { s } ,$ , the following argument still goes through by taking weighted average of outcomes from page s with probability $P ( X _ { 1 } = s ) = p _ { s }$ . Let $S = \{ A , B , . . . , L \}$ be the state space of $\{ X _ { n } \}$ . From the description on the above paragraph, $\{ X _ { n } \}$ is a discrete-time Markov chain. The transition probabilities can be found from the number of links on a page. For example, if the surfer is on page G of the site shown in Fig. 1, he will next visit sites $C , K , J ,$ and L with probability 0.25 (providing that he decides to continue his sur<sup>fi</sup>ng). It is straightforward to show that $\{ X _ { n } \}$ is an absorption chain with L as the absorbing state.

For any page $s \neq L ,$ let $N _ { s }$ be number of visits to page s before visiting page L and $T _ { s }$ be the loading time of page $s . E [ N _ { s } ]$ is found from the <sup>fi</sup>rst passage time argument from state A to state L for the chain $\{ X _ { n } \}$ (please see [33], pp 152 and pp. 172) and the expected searching time of $L = \sum _ { i \neq L } E [ N _ { s } ] E [ T _ { s } ]$

## 3.2. Experienced surfer on guidance-less sites (ESL)

Consider an experienced surfer visits, for the <sup>fi</sup>rst time, a site that does not provide any navigation guidance. The surfer randomly picks up unvisited links in a page. As far as possible, he will not re-visit a page that he has previously visited. However, he still needs to re-visit some pages when he goes into a dead end during the process of searching for his destination.

Such a search behavior cannot be modeled by the random walk in Section 3.1 above. We can still formulate it as a discrete-time Markov chain, but the size of the state space will be astronomically big: for N pages, to keep track of the identi<sup>fi</sup>cation of the pages visited, the state space is of size ${ \cal O } ( N \times 2 ^ { N } )$ . The expected searching time will be the <sup>fi</sup>rst-passage time from <sup>fi</sup>rst entering page A, to any state such that page L is visited for the <sup>fi</sup>rst time. The size of the chain precludes any sensible study through this approach on sites of practical size. Fortunately, we can still easily build up simulation models to estimate the expected searching time for this approach. In each replication of simulation, the simulation program traces the pages visited by the surfer, with the probability of visiting an unexplored page changed along the course. The mean time to reach page L across all simulated replications is an estimate of the mean time for ESL.

## 3.3. Sites with Mean-Path Guidance (MPG)

From this section onwards we consider sites that provide various types of navigation guidance. The navigation guidance may be static or dynamic, ranging from long-term mean to real-time loading time, with all possible combinations of means and exact values lying between the two extremes. Because of the navigation guidance, the difference in the expected searching time between the experienced and inexperienced surfers is minimal and hence is ignored.

In this section, we consider navigation map guidance constructed from the mean path (loading) time. To do so, we de<sup>fi</sup>ne the loading time of the destination page as the length of the directed arc. For example, the length of arc A→B is $E ( T _ { B } )$ , which is the expected time to load page B. Other arcs are treated similarly. After the directed arcs are formed using the mean loading time, we get a directed graph with positive cycle length. Standard algorithms, such as Dijkstra's algorithm (or its variations) [1] can be used to <sup>fi</sup>nd the shortest path from A to L.

In a site that provides the Mean-Path Guidance, a surfer is given a sequence of pages identi<sup>fi</sup>ed using the above procedure. The average time taken for the surfer to reach his destination is the value as identi<sup>fi</sup>ed by the Mean-Path Guidance. While the calculation is simple and straightforward, without considering the real-time page loading times, the path from the Mean-Path Guidance may be suboptimal. For example, take the destination page to be page L in Fig. 1 and suppose that the Mean-Path Guidance suggests the path $A { \mathrm { - } } C { \mathrm { - } } G { \mathrm { - } } L .$ . However, at any epoch, due to the instantaneous traf<sup>fi</sup>c, the actual loading time for an alternative path A–B–E–L could be less than that of the suggested path $A { \mathrm { - } } C { \mathrm { - } } G { \mathrm { - } } L$

## 3.4. Sites with Known-First-Arc (KFA)

The Mean-Path Guidance can be readily extended to the Known-First-Arc Guidance, which considers real-time loading time. At page A, a surfer may choose from three pages, namely, pages B, C, and D. If the system can estimate the loading time of each of pages B, C, and D, then in the calculation of the shortest path from A to L, the actual exact loading time can be used in arc A–B, A–C, and A–D, while the mean loading time are used in the remaining arcs of the paths. Such a method is called the Known-First-Arc Guidance. This Known-First-Arc Guidance is considered more advanced than the Mean-Path Guidance, and the difference is even more noticeable when loading time have large variance.

The Know-First-Arc Guidance can be applied repeatedly. Suppose a surfer moves to page C based on the Known-First-Arc approach. At C, the loading times of pages A, F, and G become known quantities at the moment when the surfer leaves page C. A system can repeatedly apply the Known-First-Arc approach to determine the loading time of the next page to visit, with an objective to moving to page L in the shortest possible time. The guidance provides by this method is dynamic. Generally speaking, once the surfer loads the root page and enters his detention, the system will guide him through the site to the destination by informing him dynamically which page to load next.

Assume that each time the actual exact loading time are random draws of the corresponding T . The Known-First-Arc Guidance discussed above is exactly the Dynamic Stochastic Shortest Path (DSSP) problem considered in Cheung [7] that studies the formulation of a dynamic shortest path in a network and proposes a routing policy to compute the expected path cost by mimicking the classical labelcorrecting approach. The DSSP allows the surfers to retreat from a wrongly chosen path, when real-time rather than the excepted mean loading time is revealed. However, the surfer may cycle around pages before he reaches the destination. Refer to Fig. 4 below which shows part of the site structure in Fig. 1. For simplicity, we use arcs with two arrows to represent the two directional <sup>fl</sup>ows. Here we assume that the loading time of all pages are $i . i . d .$ (Independent and Identically-Distributed) random variables, distributing uniformly in {1, 2, 3, 10}, whether or not a page is visited for the <sup>fi</sup>rst time. Suppose that the surfer wants to go from page A to L. At the moment when the surfer leaves A, whether the surfer will visit page B or C next depends on the current loading times of page B and page C at that time. If the loading time of page B is of one unit and that of page C of 10 units, then it is more desirable to load page B next, in which case it is possible for the surfer to be directed to page A or page E later on. If, however, page C is loaded next, then the surfer will be directed to page G later on. Similarly, at page E, the surfer may be directed next to page B or page L.

![](/api/attachments/WU7EBXH9/fulltext/images/4ee0dbe862a1c83c7280364ee149b90fd8451b14220507e285e5ff035922560c.jpg)  
Fig. 4. Cycling in DSSP guidance.

The movement of a surfer based on the DSSP can be modeled as a discrete-time Markov chain. Provided that there are not many links from one page to another, the <sup>fi</sup>rst-passage analysis of such a chain is feasible for pages of all reasonable sizes. Consider the same example in Fig. 1 going from page A to page L. De<sup>fi</sup>ne a Markov chain $\{ X _ { n } \}$ with the same state and state space as in Section 3.1 above. The transition probabilities are found from DSSP. Let S(i) be the set of successor pages that are possible to visit next when the surfer is at page i. It is straightforward to <sup>fi</sup>nd $p _ { i j } { = } P ( X _ { n + 1 } { = } j | X _ { n } { = } i )$ and $E [ T _ { j } | \{ X _ { n } \}$ moves from i to j] from the joint distribution of $\{ T _ { j } , j { \in } S ( i ) \}$ . Hence, the time from A to L is given by $\sum _ { k = 1 } ^ { N _ { A L } } T _ { k } ,$ where $N _ { A L }$ is the <sup>fi</sup>rst-passage time (number of transitions) from page A to page L, and $T _ { k }$ is the time taken in loading the kth page. $N _ { A L }$ can be expressed as the sum of the $i \to j$ transitions before reaching page L, and giving the i→j transition, the expected loading time is given by the set of conditional expected loading time $\{ E [ T _ { j } | \{ X _ { n } \} ] \}$ . Consequently, we can compute the expected searching time $E \left[ \sum _ { k = 1 } ^ { N _ { A L } } T _ { k } \right]$

## 4. Example, evaluation, and extension

In this section, we compare the expected searching time of the four models discussed in Section 3. While some of these models can be reviewed analytically, we have examined all four by simulation. We simulate the page searching performance of surfers of different skill levels on sites of different degrees of guidance support. In our simulation, the loading times are random. Such an approach is a <sup>fi</sup>rstorder approximation that captures the variation of the loading time in relation to the traf<sup>fi</sup>c of the Web site. We illustrate the models with a site structure shown in Fig. 1. The nodes are the pages and the arcs are the hyperlinks of a page. We take page A as the root and page L as the destination, and we will compare the total expected time for a surfer to get to page L after page A has been loaded. All loading time are assumed to be independent. We also compare the four models on complexity and applicability. The implementation issue of Known-First-Arc Guidance approach is also discussed at the end of the section.

To highlight the effect of searching and navigation guidance, we only consider the page loading times and ignore time taken to read information of a page. It is easy to incorporate the page reading time in the simulation models. However, this additional factor only blurs our focus — the percentage differences of times among models are certainly reduced by long page reading times.

The arcs in Fig. 1 appear as directed, however, in reality there are possibly loops traced by the surfer as he searches from page A to page L. The page-return function of any browser ensures the looping possibility in ISL, ESL, and KFA. On the other hand, no matter for any web structure, with intrinsic loops or not, MPG simply suggests one straight path without any loop for a surfer. Taking all these considerations together, it does not change the inferences and insights deduced from the numerical run even if we take the web structure as shown in Fig. 1. Along the same line, a different set of parameter values for the numerical runs certainly changes the values of numerical results, but it will not change the general trend of the inferences and insights gained from simulation.

## 4.1. Numerical examples

The underlying processes of all the four methods can be modeled as discrete-time Markov chains. Generally, the one-step transition probability matrix of MPG is the easiest to deduce, and that of ESL the most tedious. Consider web structure as shown in Fig. 1. By de<sup>fi</sup>nition, MPG suggests a single path and its one-step transition probabilities are equal to one for arc along the suggested path and are zero otherwise. For ISL, if page j being adjacent to page $\ d _ { i } , P ( X _ { 1 } = j | X _ { 0 } = i ) = 1 / n$ , where n is the number of pages adjacent to page i. For KFA, conceptually, given the distribution of the loading times and the web structure, it is possible to deduce the probability that a path is shorter at a transition, which effectively gives the one-step transition probabilities. The deduction is simply a matter of notation and is not shown here. Similarly, should we put down a discrete-time Markov chain of $1 2 ^ { * } 2 ^ { 1 2 }$ states according to the current page and collection of pages visited or not, we can list the one-step transition probabilities of ESL. Certainly there is no point to do so. In fact, the simulation programs only follow the random mechanism of each model to generate the next move of a surfer. It is not necessary to explicitly know the one-step transition probability matrices.

In our simulation, all page loading times are assumed to be independent and identically distributed (i.i.d.) random variables distributing uniformly in {1, 2, 3, 10}. With this choice of loading time distribution, the Mean-Path Guidance will de<sup>fi</sup>nitely direct a surfer to the path either A–C–G–L or A–B–E–L, and the Known-First-Arc Guidance may do the same depending on the instantaneous loading time of pages B and C at the moment when the surfer leaves page A. Meanwhile, the DSSP gives the same result as the Known-First-Arc Guidance at the moment when the surfer leaves page A. However, at pages B, E, and any subsequent visits of page A, the page to visit next is determined by the real-time loading time as discussed in Section 3.4 above.

The underlying processes of the four models are of different sizes and complexities. They require different number of runs to achieve the same degree of accuracy; e.g., in MPG, the mean time to reach page L is given by a close-form expression without doing any simulation. However, to ensure that all simulation results are under the same set of random variates generated, which is a form of variance reduction by common random numbers, the four models are simulated for the same number of runs. With nearly 50,000 states in ESL, it takes a large number of runs to ensure enough precision and con<sup>fi</sup>dence on the estimates for the model. Consequently, a million replications are carried out for the four models. The simulation results are shown in Table 1 below.

As expected, an inexperienced surfer without navigation guidance takes the longest time to get to his destination. Our results show a ratio of more than 13 times between this random search and the guided searches. An experienced surfer without guidance can reduce his searching time by more than 50% when compared to an inexperienced surfer. The surfer only revisits a previous page if he has exhausted all the possible options in the current page. However, without the knowledge of site structure, it is inevitable for a surfer to visit a page repeatedly. Consequently, the mean searching time of unguided surfers is more than six times of that of guided surfers. The two guided searches give very similar results, in terms of the mean searching time. The mean searching time in Mean-Path Guidance is longer than that in DSSP, because Mean-Path Guidance does not use any real time information.

Table 1  
Simulation results.

<table><tr><td>Models</td><td>Mean searching timesa</td></tr><tr><td>Inexperienced surfer on guidance-less Sites (ISL)</td><td>161.50</td></tr><tr><td>Experienced surfer on guidance-less Sites (ESL)</td><td>73.47</td></tr><tr><td>Mean-Path Guidance (MPG)</td><td>12.01</td></tr><tr><td>Known-First-Arc or DSSP guidance (KFA)</td><td>11.95</td></tr></table>

a The loading time of page A for the <sup>fi</sup>rst time is excluded.

## 4.2. Evaluation

All four models work similarly in terms of providing (or not) navigation guidance for the purpose of information retrieval; however, they differ in terms of applicability and complexity. Complexity refers to the performance of the model in the various scenarios, such as conditional reverse links, motivation guidance, decisionmaking, algorithm complexity, and structure modi<sup>fi</sup>cation. Applicability concerns the capability of problems types, such as cache option, multiple root nodes, multiple destination nodes, and concurrency. The following sets out the comparison of the four models based on these two aspects.

A. Complexity

(1) Conditional reverse links. The original graph needs to be extended by explorative transformation for the models ISL, ESL and MPG; however, it only adds the reverse links dynamically to the graph for model KFA.

(2) Navigation guidance. The <sup>fi</sup>rst two models, ISL and ESL, do not have the guidance, whereas the other two, MPG and KFA, bene<sup>fi</sup>t from the guidance of site structure and loading time for navigation decision.

(3) Decision-making. Both ISL and MPG models focus on the static decision-making, i.e. one-pass decision process. Meanwhile, ESL and KFA models concern dynamic information for decisionmaking.

(4) Algorithm complexity. For ISL model, the main task is to compute the <sup>fi</sup>rst passage time; the complexity for each node is $0 ( N ^ { \hat { 2 } } )$ and the total complexity is $0 ( N ^ { \hat { 3 } } )$ . Because of the state space of the Markov chain for ESL model, the total complexity is $\hat { \mathrm { O } } ( N ^ { 4 } { \times } 2 ^ { N } )$ . The complexity of MPG model depends on that for Dijkstra's algorithm, which is O(N<sup>2</sup>). KFA model cannot be solved in polynomial time unless it is acyclic. If we take into account the conditional reverse links, the complexity of all four models are non-polynomial.

(5) Structure modi<sup>fi</sup>cation. The structure modi<sup>fi</sup>cation involves addition or modi<sup>fi</sup>cation of links/nodes. For non-guidance models, ISL and ESL, are not affected by the changes in structure formulation; guidance-based models, MPG and KFA, need to update the guidance information. Meanwhile, static models, ISL and MPG, need to re-compute the solution by taking into account the new information; but dynamic models, ESL and KFA, only consider the new information during every dynamic decision process.

## B. Applicability

(1) Cache option. The cache option decides the loading time for the conditional reverse links, which range between 0 (cache enabled) and the loading time of the original node (cache disabled). The cache option (either enabled or disabled) is applicable for all four models. There may be time (life span) constraints on the cache content. These time constraints, however, are only applicable to KFA model.

(2) Multiple root nodes. The navigation may start from different root nodes in different sessions. All four models are capable of handling multiple root nodes (without any further modi<sup>fi</sup>cation).

(3) Multiple destination nodes. Unlike the case of multiple root nodes, the multiple destinations need to be covered in the same session. In ISL model, navigation is independent from the destination nodes and the calculation is additive as a linear function. Similarly, MPG model can also take the destination nodes as independent in the graph and calculate the result as a linear function. On the contrary, the calculation becomes much more complicated for ESL and KFA models, which might take non-additive calculation as non-linear functions.

(4) Concurrency. The concurrency involves both multiple roots and destinations for different session (for different users) simultaneously. Since KFA model needs real-time information for stepby-step decision-making, the multiple sessions might interfere with each other. For the other models (ISL, ESL, and MPG), the sessions can be independent.

The summary of the comparison is listed in Table 2. We may also include other evaluation criteria in order to investigate the impact of adding links on accessibility ef<sup>fi</sup>ciency of an individual Web page or that of the Web site as a whole. From the comparison result, the suitable models can be adopted and adapted based on the problem properties.

## 4.3. Implementation approach

We have illustrated in Section 4.1 that navigation guidance can signi<sup>fi</sup>cantly reduce the searching time of the surfers. The guidance can be implemented in (at least) two forms: (1) an explicit navigation map is provided with the shortest path highlighted for surfers to follow; and (2) sites structure is dynamically generated to suit the needs of surfers. The implementation of the <sup>fi</sup>rst form is straightforward and its detail is deliberately omitted. We will discuss as follows the implementation issues of the second form.

Refer to Fig. 1 for the structure of the site for illustration. Remember that page A is the root and page L is the destination. The structure indicates the hierarchical arrangement of information: Page A contains links to pages B, C, and D, in the order of the links arranged in page A; other pages and links are interpreted in the same fashion. Given the known destination page L provided by the surfer, the system provides navigation guidance based on the real-time information at the moment when the surfer <sup>fi</sup>nishes a page. Suppose that the guidance directs the surfer to page C, and, by the same token, next to page G. So that for the surfer, the site structure is as if that in Fig. 5, all the relevant links being arranged in the most convenient top (right) position for the surfer.

In Section 4.1 above, we use simulation to evaluate the performance of the different guidance methods. In real-life, it is hard to simulate on real time for each surfer to determine his best virtual site structure.

![](/api/attachments/WU7EBXH9/fulltext/images/7499db47f4a6aa4ad5e7cc7537e0a966ac0d3173bbe89a7c5fa723d3d7536d80.jpg)  
Fig. 5. The virtual site structure experienced by a surfer

Fortunately, there are polynomial time algorithms to calculate the shortest paths. The standard shortest path algorithms for deterministic arc lengths give the shortest path for the Mean-Path Guidance, as long as we set the arc lengths to their mean values. There is a family of similar algorithms to determine the shortest paths with real-time information on path length. In the following, we give the algorithm suggested in Cheung [7].

Any site structure is an undirected graph as shown in Fig. 1. Let (G, N) be such a graph, where $\mathsf { G } = \{ A , . . . , L \}$ be the set of nodes and N be the set of arcs of the graph. Node L is the destination. Let

S(i) be the set of successor nodes of node i;

$B ( j )$ be the set of predecessor nodes of node j;

$T _ { i j }$ be the (random) cost of arc $( i , j ) ; ( T _ { i j }$ is the loading time of page j in our application);

$\overline { { V } } _ { i }$ be the expected distance from i to L.

As stated above, all the arc costs are assumed to be independent. Then

$$
\begin{array}{l} \overline {{V}} _ {L} = 0, \\ \overline {{V}} _ {i} = E [ \min _ {j \in S (i)} (T _ {i j} + \overline {{V}} _ {j}) ], \forall i = A,... K. \end{array}\tag{1}
$$

Note that $T _ { i j } { } ^ { \prime } S$ are known quantities whenever we compute the expected for node i. {V̅ } are found by solving the equation set simultaneously, which can only be done numerically. However, Cheung suggested the following modi<sup>fi</sup>ed generic Label-correction method. It is an approximation in alternate to what we give in Section 3.4 above. Let

Q be the set of nodes (typically in the form of queue) whose distance from node L have been known;

Table 2  
Summary of comparison for searching models.

<table><tr><td></td><td>ISL</td><td>ESL</td><td>MPG</td><td>KFA</td></tr><tr><td colspan="5">Complexity</td></tr><tr><td>Conditional reverse links</td><td>Extend graph</td><td>Extend graph</td><td>Extend graph</td><td>Add links</td></tr><tr><td>Navigation guidance</td><td>No guidance</td><td>No guidance</td><td>Guidance</td><td>Guidance</td></tr><tr><td>Decision-making</td><td>Static</td><td>Dynamic</td><td>Static</td><td>Dynamic</td></tr><tr><td> $Algorithm\ complexity^a$ </td><td>Polynomial</td><td>Non-polynomial</td><td>Polynomial</td><td>Non-polynomial</td></tr><tr><td>Structure modification</td><td>Re-compute</td><td>No changes</td><td>Update/re-compute</td><td>Update</td></tr><tr><td colspan="5">Applicability</td></tr><tr><td> $Cache\ option^b$ </td><td>Not applicable</td><td>Not applicable</td><td>Not applicable</td><td>Applicable</td></tr><tr><td>Multiple roots</td><td>Applicable</td><td>Applicable</td><td>Applicable</td><td>Applicable</td></tr><tr><td>Multiple destinations</td><td>Linear</td><td>Non-linear</td><td>Linear</td><td>Non-linear</td></tr><tr><td>Concurrency</td><td>Independent</td><td>Independent</td><td>Independent</td><td>Dependent</td></tr></table>

<sup>a</sup> If taking into account conditional reverse links, the complexity becomes non-polynomial for all four models.  
<sup>b</sup> In the case of time-constraint cache option.

$\hat { V } _ { i }$ be an estimate of ${ \overline { { V } } } _ { i } { \mathrm { : } }$

$V _ { i } ^ { \mathrm { { m a x } } }$ maximum value of $\operatorname* { m i n } _ { j \in S ( i ) } ( T _ { i j } + { \hat { V } } _ { j } ) .$

Step 1. Initialize $\hat { V } _ { i } = \infty , \forall i \in { \mathrm { G } } , i \neq L ; \hat { V } _ { L } .$

Step 2. Initialize Q.

Step 3. Remove a node i from Q and compute $\hat { V } _ { i } = E [ \operatorname* { m i n } _ { i \in \mathsf { C } ( i ) } ( T _ { i j } + \hat { V } _ { j } ) ]$

Step 4. For each node $j { \in } B ( i ) , \operatorname { i f } V _ { j } ^ { \operatorname* { m a x } } { < } T _ { j i } + \hat { V } _ { i }$ and $\mathrm { i f } i \not \in { \cal Q }$ then add i to Q.

Step 5. Repeat steps 3 to 4 until $Q = \phi .$

The ways to initialize Q (in Step 2) and to add i to Q are implementation speci<sup>fi</sup>c. See Cheung [7] for an implementation example that reduces computational effort.

## 5. Conclusions and future directions

With the advent of the Internet technology, the information crawling/gathering on the Web is highly demanded and important in various applications. For example, users need to surf on the Web for sourcing in procurement process. However, dynamic traf<sup>fi</sup>c and poorly organized Web pages lead the users to navigate through irrelevant and redundant pages. In this paper, we adopt a stochastic searching approach to provide users with dynamic guidance for information access on the Web. We consider four models: inexperienced surfers on guidance-less sites, experienced surfers on guidanceless sites, sites with the Mean-Path Guidance, and sites with the Known-First-Arc Guidance (which are generalized as sites with Dynamic Stochastic Shortest Path Guidance (DSSP)). From the simulation result, we conclude that providing navigation guidance reduces web page search time, and dynamic guidance improves the access performance.

The results provide insights to design and administrate web pages. Navigation guidance can take different forms. They can be explicit information built in as text or images of a page, or implicit information hidden under menu bars and choice options. In all cases the design of the site, from its structure to presentation, is important. For small sites or sites that generally entertain limited number of surfers, the real-time traf<sup>fi</sup>c information of the site is not really essential on the access performance. On the other hand, for trans-continental portals that possibly entertain huge number of surfers simultaneously, the realtime information can direct and divert surfers according to needs. The simplest example may be a page directing surfers to different downloading sites according to the real-time utilization and traf<sup>fi</sup>c of sites. The realization of the insights gained from this study would be an interesting synergy of web page design and information technology.

We can further extend this research in the following directions:

(1) Multiple-destination. The dynamic guidance algorithm needs to be extended to cover a minimum spanning tree, if the user wants to visit multiple pages in a Web site.

(2) Oscillation avoidance. Since the dynamic guidance takes into account the traf<sup>fi</sup>c condition, we may need to add a “stopping rule” or a learning mechanism to avoid the oscillation in selecting the remaining path.

(3) Enabled cache. The traverse information can be kept in the cache for “go-back” function. In this case, we need to add a reverse link with zero length or change its length to zero if it exists in the original graph.

(4) Dynamic information content. If the pages are generated dynamically, such as ASP (Active Server Page), we can split/ merge the pages and re-organize information links/content.

(5) Personalized information space. The dynamic information content can be further extended for personalization that each user will surf on the customized Web information space based on his preference of information and security requirement.

## References

[1] R.K. Ahuja, T.L. Magnanti, J.B. Orlin, Network <sup>fl</sup>ows — theory, algorithms, and applications, Prentice-Hall International, New Jersey, 1993.

[2] H. Berghel, D. Berleant, T. Foy, M. McGuire, Cyberbrowsing: information customization on the Web, Journal of the American Society for Information Science 50 (6) (1999) 505–513.

[3] S. Chakrabarti, B. Dom, S.R. Kumar, P. Raghavan, S. Rajagopalan, A. Tomkins, D. Gibson, J.M. Kleinberg, Mining the web's link structure, IEEE Computer 32 (8) (1999) 60–67.

[4] S. Chakrabarti, B. Dom, S.R. Kumar, P. Raghavan, S. Rajagopalan, A. Tomkins, J.M. Kleinberg, D. Gibson, Hypersearching the Web, Scienti<sup>fi</sup>c American 280 (6) (1999) 54–60.

[5] C.H. Chang, C.C. Hun, C.L. Hou, Exploiting hyperlinks for automatic information discovery on the Web, Proceedings of 10th IEEE International Conference on Tools with AI, 1998, pp. 156–163.

[6] P.M. Chen, F.C. Kuo, An information retrieval system based on user pro<sup>fi</sup>le, Journal of System and Software 54 (2000) 3–8.

[7] R.K. Cheung, Iterative methods for dynamic stochastic shortest path problems, Naval Research Logistics 45 (1998) 769–789.

[8] D.W. Cheung, B. Kao, J. Lee, Discovering user access patterns on the World Wide Web, Knowledge-Based Systems 10 (7) (1998) 463–470.

[9] Debora Donato, Stefano Leonardi, Stefano Millozzi, Panayiotis Tsaparas, Mining the inner structure of the web graph, 8th International Workshop on the Web and Databases (WebDB), June 16–17, 2005, Baltimore, Maryland, 2005.

[10] Nadav Eiron, Kevin S. McCurley, Links in hierarchical information networks, Lecture Notes in Computer Science, vol. 3243, Springer, 2004, pp. 143–155.

[11] S. Geetha, K.P.K. Nair, On stochastic spanning tree problem, Networks 23 (1993) 675–679.

[12] D. Gibson, J. Kleinberg, P. Raghavan, Structural analysis of the World Wide Web, WWW Consortium Web Characterization Workshop, November 1998.

[13] F. Glover, D. Klingman, N. Phillips, A new polynomially bounded shortest path algorithm, Operations Research 33 (1985) 65–73.

[14] T. Joachims, D. Freitag, T. Mitchell, WebWatcher: a tour guide for the World Wide Web, Proceedings of IJCAI-97, Nagoya, Japan, 1997, pp. 770–775.

[15] J. Kleinberg, S.R. Kumar, P. Raghavan, S. Rajagopalan, A. Tomkins, The Web as a graph: measurements, models and methods, International Conference on Combinatorics and Computing, LNCS 1627 Springer-Verlag, (1999) 1–17

[16] R. Kumar, S. Rajagopalan, D. Sivakumar, A. Tomkins, E. Upfal, Stochastic models for the web graph, Proceedings of the IEEE Symposium on Foundations of Computer Science (2000) 57–65.

[17] M. Levene, G. Loizou, A probabilistic approach to navigation in Hypertext, Information Sciences 114 (1999) 165–186.

[18] M. Levene, G. Loizou, Navigation in Hypertext is easy only sometimes, SIAM Journal on Computing 29 (1999) 728–760.

[19] M. Levene, J. Borges, G. Loizou, Zipf's law for web surfers, Knowledge and Information Systems an International Journal 3 (2001) 120–129.

[20] M. Levene, T. Fenner, G. Loizou, R. Wheeldon, A stochastic model for the evolution of the web Computer Networks 39 (2002) 277-287

[21] H. Liaberman, Letizia: an agent that assists Web browsing, Proceedings of the Fourteenth International Joint Conference on Arti<sup>fi</sup>cial Intelligence (IJCAI-95). 1 (1995) 924-929

[22] I.-Y. Lin, X.M. Huang, M.S. Chen, Capturing user access patterns in the Web for data mining, Proceedings 11th International Conference on Tools with Arti<sup>fi</sup>cial Intelligence, 1999, pp. 345–348.

[23] M. Perkowitz, O. Etzioni, Towards adaptive Web sites: conceptual framework and case study, Arti<sup>fi</sup>cial Intelligence 118 (1–2) (2000) 245–275.

[24] M. Perkowitz, O. Etzioni, Adaptive Web Sites, Communication of ACM 43 (8) (August 2000).

[25] G.H. Polychronopoulos, J.N. Tsitsiklis, Stochastic shortest path problems with recourse, Networks 27 (1996) 133–143.

[26] H.N. Psaraftis, J.N. Tsitsiklis, Dynamic shortest path in acyclic networks with Markovian arc costs, Operations Research 41 (1993) 91–101.

[27] O. Richardson, Gathering accurate client information from World Wide Web sites, Interacting with Computers 12 (6) (2000) 615–622.

[28] R.R. Sarukkai, Link prediction and path analysis using Markov chains, Computer Network 33 (2000) 377–386.

[29] D. Shier, C. Witzfall, Properties of labeling methods for determining shortest path trees, Journal of Research of the National Bureau of Standards 86 (1981) 317–330.

[30] S.-H. Teng, Q. Lu, M. Eichstaedt, D. Ford, T. Lehman, Collaborative team crawling: information gathering/processing over Internet, Hawaii International Conference on System Sciences: HICSS32, 1999.

[31] H.C. Tu, J. Hsiang, An architecture and category knowledge for intelligent information retrieval agents, Decision Support Systems 28 (2000) 255–268.

[32] Z. Wang, C.K. Siew, X. Yi, A new personalized <sup>fi</sup>ltering model in Internet commerce, Proceedings of SSGRR (Scuola Superiore G. Reiss Romoli), Rome, Italy, 2000.

[33] R.W. Wolff, Stochastic modeling and the theory of queues, Prentice-Hall, New Jersey, 1989.

[34] T.W. Yan, M. Jacobsen, H. Garcia-Molina, U. Dayal, From user access patterns to dynamic hypertext linking, Computer Networks & ISDN Systems 28 (7–11) (1996) 1007–1014.

[35] C.C. Yang, J. Yen, H. Chen, Intelligent Internet searching agent based on hybrid simulated annealing, Decision Support Systems 28 (2000) 269–277.

[36] B.P.-C. Yen, The design and evaluation of accessibility on web navigation, Decision Support Systems 42/4 (2006) 2219–2235.

[37] N. Zin M. Levene Constructing web views from automated navigation sessions ACM Digital Library WOWS, Berkeley, Ca., August 1999, pp. 54–58.

![](/api/attachments/WU7EBXH9/fulltext/images/f45c8e890d4f44fd4aead011c38124dada0f6d643cad54fede95173b2d59658d.jpg)  
Yen, Benjamin P.-C. is an Associate Professor in School of Business of The University of Hong Kong. He received his PhD degree in Industrial Engineering and Operations Research from Columbia University. His research interests include Web information retrieval, electronic commerce, and IT-based supply chain management. He has papers published in journals including IEEE Transactions on Systems, Man, and Cybernetic, Decision Support Systems, Information & Management, Journal of Organizational Computing and Electronic Commerce, Journal of Information Technology, Electronic Commerce Research Journal, Information Processing Letters, Annals of Operations Research, European Journal of Operations Research, etc.

![](/api/attachments/WU7EBXH9/fulltext/images/ba0f742b9077c7af179dc573e1fb22ce4c0f1e652e30f2e59d1c401902010b22.jpg)  
Wan, Yat-wah is a Professor at Graduate Institute of Global Operations Strategy and Logistics Management, National Dong Hwa University, Taiwan. He received his PhD degree in Industrial Engineering and Operations Research, University of California at Berkeley. His research interests include applied stochastic processes, stochastic modelling and scheduling, and transportation logistics. He has papers published in major journals including Decision Support Systems, European Journal of Operational Research, IIE Transactions, Naval Research Logistic, Operations Research Letters, Probability in the Engineering and Informational Sciences, Transportation Research – Part B, etc.
