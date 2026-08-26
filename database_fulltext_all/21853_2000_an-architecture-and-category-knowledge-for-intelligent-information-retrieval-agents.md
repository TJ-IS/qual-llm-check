---
otero_id: 21853
otero_key: "JM2P32DB"
title: "An architecture and category knowledge for intelligent information retrieval agents"
authors: "Hsieh-Chang Tu; Jieh Hsiang"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00089-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An architecture and category knowledge for intelligent information retrieval agents

Hsieh-Chang Tu, Jieh Hsiang )

Department of Computer Science and Information Engineering, National Taiwan UniÕersity, Taipei, Taiwan

## Abstract

Information overload has become a serious problem for users of the World Wide Web. In this paper, we propose to use intelligent information retrieval IIR agents as a solution to this problem. We identify desirable features of an IIR agent,Ž . including intelligent search, navigation guide, auto-notification, personal information management, dynamic personalized Web pages, and tools for page reading-aide. We propose a modularized agent architecture, describe the responsibility of each component and discuss how to combine these components to perform various tasks. We point out that group knowledge, acquired from preferences of other users in the same group, may be useful. The agent’s knowledge on user preference is primarily represented by category profiles. Several applications of category profiles are also investigated. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Information retrieval; Agent; Category; Personalization; Navigation; Notification

## 1. Introduction

In a few short years, the World Wide Web has become one of the most important media with which people share information resource. Web information is primarily exhibited through Web pages designed and written by content providers. The enormous amount of available information induces the problem of information overload, that there is too much information for people to digest. To alleviate this problem, one needs better information retrieval IR soft-Ž . ware to serve as a filter between the user and the information retrieved over the Web. Such software should provide a better search capability that can find more interesting Web pages and fewer uninteresting ones. When the user is surfing the net, the software should also be able to suggest interesting URLs to visit. Finally, there may be ‘‘hot pages’’ whose contents change frequently. The IR system should be able to notify the user about such changes automatically.

Attempts have been made to reduce the problem of information overload. There are browsers that are not only equipped with user-friendly interface but also support Java and other powerful languages. Web directories, such as Yahoo!, <sup>1</sup> organize ‘‘important’’

Web pages into a hierarchical structure similar to yellow pages. Search engines such as Alta Vista,<sup>2</sup> Excite,<sup>3</sup> Infoseek,<sup>4</sup> and Lycos<sup>5</sup> use indexing techniques for users to retrieve potentially relevant pages through queries. Intelligent agents, programs that are supposed to exhibit human behavior, are also proposed to help users retrieve, locate, and manage Web information 4,15 . Examples include Pointcast Net-<sup>w</sup> <sup>x</sup> work<sup>6</sup> and Pathfinder,<sup>7</sup> which offer personalized news and information, Firefly,<sup>8</sup> which makes movie and music recommendations, and Web-Watcher 2<sup>w</sup> <sup>x</sup> which interactively helps users locate information. Moukas and Maes 21 develop a system that makes <sup>w</sup> <sup>x</sup> use of search engines and filtering techniques to discover interesting Web pages. There are also softbots 9 aiming at providing integrated solutions to<sup>w</sup> <sup>x</sup> effectively explore Internet resources. Other interesting Internet agents can be found in Ref. 6 .<sup>w</sup> <sup>x</sup>

Most of the agents described above address one issue or another related Web IR. In this paper, we propose an architecture of intelligent<sup>r</sup>interactive information retrieval IIR agents to integrate severalŽ . Web IR features. We first discuss what we think are desirable features of a good IIR agent. We describe the notion of an agent community in Section 3 and identify an IIR agent as one agent in the community. We propose an integrated architecture to carry out features of an IIR agent. We further decompose an IIR agent into components called subagents, each of which can be regarded as an independent module to perform a specific function. We also discuss cooperation among subagents. Section 4 discusses the issue of category information. Category information, represented by category profiles, plays a crucial role in an agent’s knowledge. We distinguish the meaning of a category from the well-known definition of a cluster. Several applications of category profiles are addressed next. A concluding remark about IIR agents is given at the end.

## 2. Essential features of Web IIR agents

Before designing an appropriate agent architecture, it is essential to first decide what an IIR agent should do. To answer this question, one should examine what kind of difficulty people encounter when they try to get information over the Web. Some of these obstacles come from the difficulty of using a software, but most problems are caused by information overload — there is too much information for the user to retrieve. Since the purpose of an IIR agent is to assist people retrieve and manage information on the Web, it should have the following features:

Ž . 1 Intelligent<sup>r</sup>interactive search. An effective and efficient search of information from a database is a major issue on the research of IR. When people start to search for information from the Web, they often become frustrated when the search result contains too little useful information or too much garbage .Ž . An intelligent agent should give the user an interactive environment so that the user’s information need can be pinpointed exactly.

Ž . 2 Navigational guide. When surfing through the Web, it is easy to ‘‘go astray’’ in cyberspace. A good IIR agent should provide guides or roadmaps so that users can get assistance when stuck in their navigation on the Web. For instance, the agent may analyze pages recently read by the user in order to suggest related subject areas and pages. Another kind of navigational guide is to highlight potentially interesting hyperlinks.

Ž . 3 Information auto-notification. It is tedious for people to check whether a page has been updated. After the user specifies the kind of information he needs, an IIR agent should be able to detect updated information or even download them automatically. Messages may be sent to the user to notify that new data have become available. Furthermore, it is worthwhile for an agent to analyze the user’s reading preference so that it may prompt interesting pages to the user automatically. On-line subscribed news notification is also useful.

Ž . 4 Personal information management. Categories, directories, or folders are familiar ways for people to manage tree-structured hierarchical data. It is useful for an IIR agent to manage personal categories in an intelligent<sup>r</sup>interactive way. For instance, the agent may provide suggestions to build a personal category tree for each user. This category information can later be used to help user search or navigate on the Web. Another example of information management is to automatically organize bookmarks 19 so that<sup>w</sup> <sup>x</sup> the user may handle bookmarks more easily.

Ž . 5 Dynamic personalized Web pages. If possible, an IIR agent should interact with content providers to dynamically produce Web pages appropriate to the user. For instance, the agent may give content providers the user’s preference on interface setting Žsuch as user’s background, preferred languages, font size, background color, etc. . The content providers . may then produce Web pages likely to be more interesting to the user.

Ž . 6 Tools as reading-aide. A good IIR agent may also provide tools to help the user with reading retrieved papers. Such tools may include an on-line dictionary, an on-line encyclopedia, and some translation programs. These programs are usually standalong agents themselves. The IIR agent should allow easy incorporation of such tools.

## 3. An agent architecture

## 3.1. Agent community

We consider an agent as a goal-oriented program with some learning ability. An agent can dynamically adapt to individual users and can perform certain tasks autonomously. An agent community is a group of agents working together to serve a group of users. In an agent community, agents interact with each other and cooperate to solve problems if necessary. It is also convenient to further divide agents into task agents and interface agents. Each task agent offers a specific service and they communicate with each other to execute more advanced functions. For instance, a typical IIR agent may not support functions such as looking up dictionaries or translating page contents into another language. These functions are done by other task agents sayŽ . <sub>T</sub> . An IIR agent should be able to communicate with <sub>T</sub> to offer such services to the user. Interface agents are responsible for keeping and updating the user profiles and communicating a user’s need to the task agents.

Among the task agents in the agent community, there is a resource management agent, called managent, which plays a special role. The managent keeps the list of the services provided by agents in the community. If a new user joins the group, the managent announces it to all task agents. Functions offered by agents can then be automatically prompted to the new user. This allows the user easy access to services available in the agent community. An interface agent acts like the Desk Top Manager in most systems with a graphics user interface. A browser, which allows all possible Web information to be properly displayed, can also be regarded as an interface agent. An example of architecture of agent community is illustrated in Fig. 1 all figures are Ž shown at the end of this paper ..

## 3.1.1. Group and personal agents

An IIR agent needs to keep two types of preferences; each user’s own preference about search and navigation, and the preference of each group of users. The latter is needed because web pages that are interesting to most users in a group are likely to be interesting to others in the group. Thus, some kind of group preference, computed from profiles of users in the group, is required. Furthermore, in order to reduce network traffic load, web pages requests by users in the same group should be handled by the same program. These considerations motivate the design of an IIR agent into two layers. Each user has his own personal agent PA that keeps a profile of Ž . user preference, and there is a group agent GA thatŽ . handles group knowledge and preference. Intuitively, PA offers all anticipated features and learns personal preference from the user it serves. GA accumulates the knowledge about personal preferences it obtains from the PAs, transforms it into the collective group preference, finds interesting pages that reflect the group preference, and monitors web pages that the users wish to be watched. The various functions of the GA and PA are captured in modules, which we call subagents. We shall describe these subagents and their collaboration in detail in the Section 3.2. Meanwhile, the proposed IIR agent architecture is presented in Fig. 2.

## 3.2. Agents and subagents

Similar to decomposing a program into modules, an agent can also be organized as subagents. Each subagent, working independently, performs some

![](/api/attachments/JM2P32DB/fulltext/images/82def287e9f07a84bf2f5dff362e9fdbd9cde6aa627dff0a5d7d437303eda863.jpg)  
Fig. 1.

prescribed feature of the agent. Subagents have their own local databases and share the same knowledge base with other subagents in the same agent. A finer architecture of the IIR agent is described in Fig. 3, in which GA and PA are enclosed in dashed, rounded rectangles. Boxes within agents represent subagents, which are separate, independent program modules. Subagents work together to form GA or PA. We brief the functions of each subagent as follows.

![](/api/attachments/JM2P32DB/fulltext/images/654c309fbae93bd64f7a4930c76492ebb527fc9bfcd32a15b822180cd1e6480b.jpg)  
Fig. 2.

![](/api/attachments/JM2P32DB/fulltext/images/5ef9f34acc2911910a7fa50274d58637704d95710949e923b233c8b54c0b7a36.jpg)  
Fig. 3.

<sup>Ø</sup> Communication subagent. Each group or per- Ž sonal agent has a communication subagent which. takes the responsibility of sending, receiving, and possibly interpreting messages from the external world. A communication subagent may be regarded as a program listening to certain communication ports in conventional network programming, except that the former can actively watch request queues. It is also desirable to equip the communication subagents with some learning capability or with a uniform and flexible protocol such as KQML, so that collaborations between agents can become more effective.

<sup>Ø</sup> Proxy subagent. According to Request for Ž .<sup>9</sup> Comments No. 1945 RFC1945 , a proxy is an intermediary program, which acts as both a server and a client for the purpose of making requests on behalf of other clients. For instance, if several users connect to the same Web site through a proxy Ž . server , each page of the site will be downloaded Ž . from the site to the proxy only once and then provided to all the users. A proxy subagent is a special program that intercepts messages between the user and the Web. It also serves as a communication subagent between the user and the PA. If the user wishes to set his own personal preference, he must interact with the profile manager via the proxy subagent. Since the proxy subagent knows which pages have been accessed by the user, it provides necessary information for the IIR agent to learn about user preference. A proxy subagent caches frequently accessed pages so that unnecessary network traffic can be reduced. It may also be desirable for the IIR agent to pre-fetch pages that may be interesting to the user. Although pre-fetching pages may increase network traffic, good interaction between the proxy subagent and the managent may allow pre-fetching to be done when the network traffic is light.

<sup>Ø</sup> Search subagent. There are already many search engines on the Web. Instead of designing its own, an IIR agent may act as a ‘‘meta search engine’’, which collects results obtained from sending user queries to existing search engines. Since search engines may require different query formats, the search subagent is responsible for interacting with the user so that the user can format his queries properly. The subagent translates user queries to the formats acceptable by Ž . a pre-defined set of search engines; issues formatted queries to these engines and collects returned results to the user. The subagent may ask the user for some category information discussed in detail in Ž Section 4 so that better searching results can be . presented to him.

<sup>Ø</sup> Navigation subagent. Given a set of pages recently read by the user, the navigation subagent attempts to classify these pages into pre-defined categories. If the user gets lost in cyberspace, he may ask the navigation subagent to suggest interesting hyperlinks. The subagent will prompt categories, which are related to the current page being browsed, to the user. Each category contains hyperlinks as well as titles or descriptions about the corresponding Web pages. Some hyperlinks may be manually coded Ž . such as important Web sites , and some are obtained from recently browsed pages. Categorized hyperlinks thus provide the user ways to jump to other pages, which are related to pages currently being browsed.

<sup>Ø</sup> Notification subagent. The user may ask the notification subagent to monitor frequently changed pages. If these pages are changed, the subagent will notify the user automatically. On the other hand, the user may ask the IIR agent to search through the Web to find pages fulfilling requirements specified by the user. The notification subagent should provide the user with a comprehensive way to specify his information needs. The notification subagent does not monitor or search Web pages itself. Instead, it sends monitor or search requests to the GA. The monitor subagent and Web spider described later inŽ . the GA are responsible for handling these requests.

<sup>Ø</sup> Profile manager. The profile manager modifies the user preference, either by interacting with the user directly or by communicating with the GA, to obtain group preference. It contains a knowledge explainer so that the user can read knowledge stored in the profile. Some knowledge, such as the pages to be monitored or to be searched by the Web spider, can be specified simply by a form or a table. Statistical knowledge, such as a user’s category preference, is more difficult to interpret. Since we will represent such knowledge by a set of keywords, the agent needs to let the user know the role of such keywords in the representation. It is also important to allow an experienced user to edit category preference manually. Details about categories will be addressed in Section 4.

<sup>Ø</sup> Web spider. A Web spider is a subagent of the GA and searches through the Web with the fishsearch algorithm 8 to find Web pages likely to be<sup>w</sup> <sup>x</sup> interesting. To bootstrap the search algorithm, we provide the spider with a list of index pages, which contains hyperlinks to related pages. The spider uses these hyperlinks to reach other pages, and in turn uses hyperlinks in the resulting pages to obtain more pages. A pre-defined search width, search depth, and search time are required so that the spider will not lose its original searching goal by following a chain of pages too deeply. A control strategy similar to best-first search 22 is adopted so that pages hyper- <sup>w</sup> <sup>x</sup> linked by an interesting page can be explored before those directed by an uninteresting one. In general, a Web page is regarded as more interesting if it matches more specifications indicated by the user profile. The spider may also interact with the user so that search goals can be modified dynamically 5 . If the spider<sup>w</sup> <sup>x</sup> finds pages that may be interesting to all users in the group, these pages will be sent to corresponding PAs so that the users can be notified.

<sup>Ø</sup> Monitor subagent. This subagent takes requests from PAs and monitor specified pages to see if their contents have been modified. Monitoring can be done by downloading the page and checking it with an older version of the same page. The main reason for putting the monitor subagent as part of the GA instead of the PA is to reduce network traffic sinceŽ many users may want to monitor the same pages. and to reduce the complexity of PAs.

<sup>Ø</sup> Group-knowledge manager. Group knowledge is information pertinent to the interests of a group of users. There are basically two kinds of knowledge known to the GA. The first kind is more of a record keeping nature. It includes pages specified by the users to monitor the number of pictures or voice files in a page and pages satisfying certain conditions Ž . such as containing at least two image files . The second kind of knowledge is obtained from statistics of pages accessed or read by the users. This knowledge is represented by a set of attributes and weights, which can be interpreted using notions from fuzzy sets of probability. A simple statistical knowledge is the histogram, which counts the times of a page accessed by the users. Pages frequently requested may be regarded as ‘‘hot pages’’. Another statistical knowledge, namely the category information, plays a central role of knowledge to our IIR agents.

![](/api/attachments/JM2P32DB/fulltext/images/2e6aed0713722ba30714ceb21b87eaa03e31701a42b4f37327fb7d659b4e333e.jpg)  
Fig. 4.

## 3.3. Collaboration among subagents

Subagents collaborate to perform functions of an IIR agent. In the rest of the section, we describe how the collaboration is done for the processes of intelligent search, auto-notification, navigation guide, and personal information management.

## 3.3.1. Process of intelligent search

A typical working scenario of intelligent search is described in Fig. 4. In order to make the search ‘‘intelligent’’, the GA needs some initial knowledge <sup>10</sup> about categories which amounts to the initial Ž knowledge about group preference . It announces the. category knowledge to PAs so that each PA will have the same initial category knowledge. The left part of the off-line preference processing shown in Fig. 4 illustrates this idea. After a user sends a query, the search subagent receives this message from the proxy subagent. It then translates the user query to queries that are acceptable to existing search engines on the Web and gathers results returned from sending translated queries to the search engines. The search sub-agent uses category knowledge to filter out pages that it deems uninteresting, and presents the final result via the proxy subagent to the user.Ž . The user marks pages as interesting, uninteresting, or no comment. These labeled pages, which indicate the types of pages interesting to the user within certain categories, will be used later in the learning process. After a pre-set period of time, the PA communicates with the GA about what it has learned from the user. This makes it possible for the GA to modify its category knowledge from the user preference. The GA then communicates back its newly gained knowledge to the PAs.

We remark that the user has control over personal preference learned. This is illustrated in Fig. 4 as the off-line preference processing between profile manager and the user profile. The profile manager should explain, as most as it can, what preference it has learned to the user. If the user is experienced enough, he can modify the preference to match his information need.

## 3.3.2. Processes of auto-notification, naÕigation guide, and personal information management

We illustrate the process of auto-notification in Fig. 5. At the beginning, the user specifies what he needs to the notification subagent. One possible specification simply indicates page patterns, and pages satisfying these patterns can be regarded as interesting. The notification subagent sends pattern messages to the group knowledge manager so that personal requests can be stored in the group preference database. The Web spider analyzes group requests from the group preference database so that Ž . Web pages interesting to group users acquire more attention. As soon as interesting pages are found, they will be put into the group document database. Similarly, the monitor subagent watches specified

Web pages to see if they have been changed. It writes messages to the group document database if it wants to inform group users that some pages are changed. The group knowledge manager checks personal requests with notifiable documents and transmits necessary information to the corresponding notification subagent. The user receives prompting message once the notification subagent decides to notify him.

To perform navigation guide, the navigation subagent consults user preference and the documents stored in the PA. It analyzes pages recently read by the user and prompts related categories to the user. Hyperlinks stored in categories allow the user to visit related pages. The process of navigation guide, not including propagation of knowledge e.g., category Ž knowledge from the GA to PA is shown in Fig. 6a. .

Fig. 6b pictures the process of personal information management. The profile manager consults the user profile and displays stored knowledge to the user. User preference includes personalized interface, interesting categories and their representations, interesting page patterns, and other system settings e.g.,Ž cache size used by the proxy subagent . Personal. information management allows an experienced user to control his own preference profile.

![](/api/attachments/JM2P32DB/fulltext/images/b8e7afeb890da60e969faefb689f8751dbadc70ddce7f59752a48f12d791df5a.jpg)  
Fig. 5.

![](/api/attachments/JM2P32DB/fulltext/images/32e51506b3b3d13695420c5bb8cca4ad5d4ddfd1a7fca097e780d6c32d94272e.jpg)  
Fig. 6.

## 4. The formulation of category knowledge

Web pages normally contain multimedia information. However, it is difficult to handle information stored in non-text form. One solution is to describe multimedia information by a sequence of words 10 so that it can be treated as normal texts, and use conventional IR techniques to handle the text information. In this section, we assume that information stored in Web pages can be processed via text processing. We call a page a document to emphasize that the retrieval is done by text processing.

Human beings are familiar with using classification techniques to manage a large amount of objects. Similar objects are collected into the same group so that they can be retrieved conveniently. One of the most popular methods is clustering, which puts documents with similar features or keywords into the same cluster. However, since features or keywords may not reveal semantic information of a document, a cluster may contain too much noise to be truly useful. A more effective way is to group documents according to semantic concept. We call a group of documents that captures certain semantic concept a directory. The use of directories, although intuitively reasonable, is not feasible computationally since it is extremely difficult to compute the semantic information of a document precisely. We therefore introduce a notion of category, which computes an approximation of a directory of documents. In the following subsections, we first review the definition of document vector model, which is a popular method in document processing and will also be used in our method. We then discuss the relationship among a cluster, a directory, and a category in more detail in Section 4.2. A special category called User-Category is then introduced to capture a user’s recent browsing preference. Finally, we examine possible applications of category knowledge in an IIR agent.

## 4.1. The document Õector model

Allowing inputs in natural language is one way to make an IR system friendly. However, natural language understanding is a notoriously difficult task. Therefore it is common to employ some ‘‘approximation’’ method to analyze the queries and documents. One popular method for processing documents is the vector model 23 , which regards each document as a vector. Let $\mathcal { V }$ be a finite vocabulary of words and let $v = | \mathcal { V } |$ <sup><</sup>. The word space $\mathcal { W }$ is the Õ dimensional vector space over real numbers. Each document in a given database is represented by a vector d Ž . called a document vector in $\mathcal { W }$ . For convenience, from now on we use d to denote both a document and the associated document vector. We regard the set of all ‘‘valid’’ Web pages i.e., pagesŽ known or accessible by the IIR agent as a database. $\mathcal { D }$ Žwhich is also regarded as a subset of $\mathcal { W } )$ Informally, the value of the ith component of a vector d is computed from some statistical property which is a function of the ith word in $\mathcal { V }$ , the document d and the database $\mathcal { D }$ . Given a vector $ { \mathbf { p } } = ( p _ { 1 } , \ \dots , \ p _ { v } ) \in \mathcal { W }$ , we use $\begin{array} { r }  \mathbf { | p | = ~ \} \sqrt { \sum _ { i = 1 } ^ { v } p _ { i } ^ { 2 } } } \end{array}$ to denote the length of $\mathbf { p } .$ For simplicity, we normalize each document vector $\mathbf { d } \in \mathcal { D }$ so that $| \mathbf { d } | = 1$ . We remark that, in the vector model, it is possible to have the same document vector representing different documents.

An intuitive way to represent the similarity between two document vectors is by the distance between them. A smaller distance means that the two vectors are closer and therefore the associated documents are more similar. Let p, q be two points $( \mathrm { i . e . }$ document vectors in. $\mathcal { D }$ , and let $\mathbf { p } = ( p _ { 1 } , \ . . . , \ p _ { v } )$ and $\mathbf { q } = ( q _ { 1 } , \ \ldots , \ q _ { v } )$ . One commonly used formula to measure document similarity is the inner product of p and q <sup>w</sup> <sup>x</sup> 7,21,23

$$
s (\mathbf {p}, \mathbf {q}) = \mathbf {p} \cdot \mathbf {q} = \sum_ {i = 1} ^ {v} p _ {i} q _ {i}.
$$

Intuitively, $s ( \mathbf { p } , \mathbf { q } )$ is the cosine value of the angle between the two unit vectors. A largerŽ . $s ( \mathbf { p } , \mathbf { q } )$ means that the two documents represented by p and q are more similar. We define the distance $d ( \mathbf { p } , \mathbf { q } )$ of the two document vectors p and q by

$$
d (\mathbf {p}, \mathbf {q}) = 1 - s (\mathbf {p}, \mathbf {q}) = 1 - \sum_ {i = 1} ^ {v} p _ {i} q _ {i}.
$$

In order to automatically classify similar document vectors into the same group, one needs a definition to measure the distance between two sets of document vectors. Let $P ,$ Q be two sets of points in the word space, there are various definitions of $d ( P , Q )$ , the distance between P and $Q .$ Two popular definitions are the single-link distance and the complete-link distance 12,23 . The former defines <sup>w</sup> <sup>x</sup> dŽ $P , Q )$ by $\begin{array} { r } { \operatorname* { m i n } _ { p \in { \cal P } , q \in \mathcal { Q } } d ( { \bf p } , { \bf q } ) } \end{array}$ , while the latter defines $d ( P , Q ) { \stackrel { } { = } } \operatorname* { m a x } _ { p \in P , q \in Q } d ( \mathbf { p } , \mathbf { q } )$ . Intuitively, the single-link distance is the distance between the most similar pair of points from the two sets one fromŽ each set , while the complete-link distance refers to. the distance of the least similar pair of points in $P$ and $Q .$ Koller and Sahami 14 have reported that, in <sup>w</sup> <sup>x</sup> many cases, relatively few keywords are sufficient to classify documents into categories.

## 4.2. Clusters, directories and categories

Recall that $\mathcal { D }$ denotes a set of document vectors representing pages on the Web. A cluster X Ž . of <sub>D</sub> is a subset of $\mathcal { D }$ such that there is a high degree of association measured by a chosen distance function Ž . between members in X. In practice, we also require that members from different clusters have low degrees of association. Clusters are generated by unsupervised learning techniques, which means that the learning is performed without labeled training examples. By a labeled training example, we mean that the classification result i.e., whether a documentŽ belongs to a cluster is explicitly specified in ad- . vance. Some commonly used clustering methods include the c-means algorithm 24 , the learning vector <sup>w</sup> <sup>x</sup> quantization LVQ 20 , and the fuzzy clusteringŽ . <sup>w</sup> <sup>x</sup> techniques 26 . Clustering techniques have been ap-<sup>w</sup> <sup>x</sup> plied to discover Web information 21 , and it has <sup>w</sup> <sup>x</sup> been shown that the cluster-based approaches can be helpful for the user to browse large document collections 7 . However, clusters generated automatically<sup>w</sup> <sup>x</sup> are difficult to interpret, since ‘‘similar documents’’ defined from a distance measure may not be meaningful to most people.

Like a cluster, a directory is a subset of points in ${ \mathcal { D } } .$ . The main difference between a cluster and a directory is that the former is a ‘‘syntactical’’ group of documents, while the latter is a ‘‘semantical’’ group of documents. A directory is pre-defined by the retrieval system often manually by the designer , Ž . and its semantical content means that we can name it in a way familiar to most people. For instance, we may group documents semantically related to com-Ž . puters by a directory call<sup>r</sup>computer, and organize documents semantically related to computer archi- Ž .

tecture by a sub-directory call<sup>r</sup>computer<sup>r</sup>architecture. In the real world, people have a lot of experiences in handling information with this kind of naming structure. For instance, in a computer system, users are familiar with attaching a mnemonic path name to each file directory.

The main problem with using directories in a Web database is that its construction is almost impossible to automate.<sup>11</sup> Thus, in this paper, we propose a notion of a category, which is an approximation of a directory. Given a directory r, we denote an associated category by $C _ { r } . \mathrm { ~ A ~ }$ category is also a subset of points in $\mathcal { D } . ^ { 1 2 }$

Assume that we are given a set of possibly Ž hierarchical directory names. Since in practice, di-. rectories exist only in an abstract sense, we approximate them using a training set $T \subseteq { \mathcal { D } }$ . Each sample in the training set T is explicitly labeled as belonging to one or more directories. Our task, then, is to create, for each directory r, a category C from the information provided by T. Since categories are generated by a computer, we shall introduce a vector representation of categories in the Section 4.3.

## 4.3. Category representation

Hierarchical categories can be represented by a tree structure. We call each node in such a tree a category node. A category node is labeled by a category name, which is the path starting from the root of the tree to that tree node. We use $\nu ( C )$ to denote the category node of the category C. A category $C ^ { \prime }$ is said to be a subcategory of C if Ž . C is an ancestor of the $\nu ( C ^ { \prime } )$ . It is called a proper subcategory if $\nu ( C )$ is the parent of $\nu ( C ^ { \prime } )$ . A category without subcategories is a leaf category. A category, which is neither root nor leaf, is an intermediate category.

A category C is represented by a category profile which contains a prototype vector $\mathbf { c } \in { \mathcal { W } }$ and a positive radius $\varepsilon ( C )$ . The interpretation of a category profile is given as follows. If C is a leaf category, C is defined as the set of document vectors d’s such that $d ( \mathbf { c } , \mathbf { d } ) \leq \varepsilon ( C )$ . If C is an intermediate category, C is defined as the union of its subcategories and the document vectors d’s such that $d ( \mathbf { c } , \mathbf { d } )$ $\leq \varepsilon ( C )$ . If C is the root category, its radius is set to 1 so that it consists of all document vectors in the database. Intuitively, a category should have a radius bigger than those of its subcategories.

Notice that a parent category is defined from its subcategories. This is different from conventional hierarchical categorization techniques where a subcategory is defined only when its parent category is defined. Our ‘‘bottom-up’’ definition is inspired from the observation that the vector representation of a subcategory is normally more precise than that of a parent category.

The generation of the categories which approxi- Ž mate the intended directories is done using super- . vised learning techniques from the labeled training set T. Several methods are known, such as the least square functional approximations 25 or the training <sup>w</sup> <sup>x</sup> algorithms for linear text classifiers 17 . Some ear-<sup>w</sup> <sup>x</sup> lier experiments show that a prototype vector learned from specific user interests achieves encouraging results in selecting interesting Web pages 3 . In<sup>w</sup> <sup>x</sup> practice documents, satisfying a user interest may be defined as a personal directory. We remark that the allowance of one document vector to be classified into several directories may complicate the learning process.

Once appropriate category representations are computed from the training set, they can be used to perform document classification. That is, we may classify a document vector d Žwhich may not belong to the training set into an existing category. C, if one of the following holds:

1. C is a leaf category and $d ( \mathbf { d } , \mathbf { c } ) \leq \varepsilon ( C )$

2. C is an intermediate category, and either d is classified to some subcategory of C, or $d ( \mathbf { d } , \mathbf { c } ) \leq$ $\varepsilon ( C )$

3. C is the root category.

## 4.4. A special category: User-Category

Interesting pages browsed by a user usually reveals information about the user preferences. Such information can be used to form a special category called User-Category<sup>13</sup>, which is represented by a vector u and radius Ž . u . We assume that the radius Ž .or threshold $\varepsilon ( \mathbf { u } )$ is set by the user. The agent adopts the following rules to modify the prototype vector u automatically.

Ž . 1 Let d be the vector representing the browsing page, which is assumed to be interesting. Intuitively, we want to move the vector u toward d so that keyword features in d make contribution to the new prototype vector. We use a simple form of descent methods 13 to adjust <sup>w</sup> <sup>x</sup> u by

$$
\mathbf {u} \leftarrow \frac {\mathbf {u} + \eta \mathbf {d}}{| \mathbf {u} + \eta \mathbf {d} |},
$$

where the denominator is used to normalize the prototype vector so that it has a length of one , andŽ . is a positive number called the learning rate.

Ž . 2 After some period of time, the agent may decide to ‘‘forget’’ information collected from pages browsed a long time ago. Let J be the set of pages recently browsed by the user. For any document vectors p and q, we use p±q to denote a vector whose ith element is $p _ { i } - q _ { i }$ if $p _ { i } - q _ { i } > 0$ , and is 0 otherwise. We construct a vector $\mathbf { w } = ( w _ { 1 } , \ \dots , \ w _ { v } )$ $\in { \mathcal { W } }$ by setting $w _ { i } = 0$ if the ith word appears in J, and $w _ { i } = 1$ if otherwise. The vector u is adjusted by

$$
\mathbf {u} \leftarrow \frac {\mathbf {u} \ominus \tau \mathbf {w}}{| \mathbf {u} \ominus \tau \mathbf {w} |},
$$

where $\tau \leq 1$ is a positive number called the discarding rate. Intuitively, the formula u± w says that the weights of words which appear in J are unchanged, while those of words which does not appear in J are decreased by $\mathrm { ~ a ~ } \tau$ level if the original weight is lessŽ than , the new weight is set to zero . Again, we. take normalization to guarantee that $| \mathbf { u } | = 1$

Knowledge of User-Category can be used in the auto-notification process to filter out uninteresting pages. On the other hand, the group recent preference may be built from each user’s User-Category knowledge so that the Web spider can tune its search direction to find more interesting pages. We have implemented a prototype system, which makes use of user categories to help a user search interesting Web pages 11,16 . On the other hand, based on the<sup>w</sup> <sup>x</sup> above formulae, we have taken some early experiments on the effectiveness of creating personal category profiles. An interesting result of the experiment reports that a small training set which contains three to ten webpages is usually sufficient to produce a good category profile 18 .

## 4.5. Utilizing category knowledge in an IIR agent

Since categories are obtained via supervised learning with a training set, it contains more semantic information and closer resembles the intended directories than clusters. The knowledge contained in the categories is beneficial to IIR. It enables us to do document classification, which implies that we may use categories as filters to exclude documents that do not belong to categories that interest a specific user. In the following, we describe how category knowledge can be used in different aspects of an IIR agent.

<sup>Ø</sup> Intelligent search. Category knowledge can be used to filter out uninteresting documents. In addition to the normal query, the agent may ask the user to provide category information e.g., specify inter-Ž esting categories so that documents not belonging to. the specified categories can be filtered out. To be more specific, let P be the set of documents returned by search engines. If $C _ { 1 } , \ldots , C _ { m }$ are interesting categories, a document $d \in P$ will be presented to the user if d is classified as belonging to $C _ { i } ,$ where $1 \leq i \leq m$

<sup>Ø</sup> Navigation guide. Let us assume that each category contains sample documents stored in GAŽ . which come from either training samples or pages identified by users to belong in the category. When a user needs navigation guide, the agent first analyzes recently browsed pages to determine which categories sayŽ $\mathcal { C } )$ are related to the user’s recent interest. A category tree, with categories in $\mathcal { C }$ highlighted or ranked high, is prompted to the user. After the user clicks an interesting category, pages stored in the selected category can be prompted to the user as suggested pages.

<sup>Ø</sup> Auto-notification. The use of category knowledge in auto-notification is similar to that in intelligent search, namely to use categories to filter out uninteresting documents. To be more specific, the user sets document criteria so that documents foundŽ by the Web spider matching the constraints can be. suggested to the user. The constraints specified typically consist of natural language queries, shallowŽ . multimedia information i.e., number of pictures, Ž images, or voice files in a page , plain document. information such as document location, documentŽ size, number of hyperlinks, or possibly document author , and interesting categories. .

<sup>Ø</sup> Personal information management. A user may preserve interesting pages as bookmarks. Storing bookmarks hierarchically is valuable to manage pages that are identified as interesting to the user. People may simply store bookmarks under hierarchical categories offered by the PA. The user can rename, add, delete, or modify the category names stored in the PA. If the PA finds that there are too many documents or bookmarks stored, it may group them into several clusters and then ask the user to give a name to each cluster. In this way, categories may grow semi-automatically since the user has to give namesŽ to them and cluster analysis will be helpful to. construct personal categories.

A profile manager is responsible for explaining the meaning of category knowledge to the users. Explanation of category knowledge is helpful to a naıve user to understand what has been stored in the¨ PA. Recall that a category C is represented by a vector c and a radius Ž . C . Adjusting the ith component of c corresponds to tuning the ‘‘importance’’ of the ith word inŽ . Ž . <sub>V</sub> to C, while modifying C amounts to changing the size or range of C. An experienced user can probe whether the adjustment of weights satisfies his demand by classifying sample documents into adjusted categories.

## 5. Concluding remarks

The growing popularity of the World Wide Web worsens the problem of information overload. IIR agents are proposed as one possible solution to assist people manage Web information. We point out desirable features of an IIR agent and propose an agent architecture, which supports the implementation of these features. Subagents of an IIR agent are also identified so that they can be designed and implemented separately. Collaboration among subagents are illustrated and discussed.

We then turn to the question of classification of Web documents. We introduce a notion of categories, which capture better the informal but ‘‘conceptually ideal’’ notion of directories. We describe how the categories can be represented by vector models and can be obtained through supervised learning with a training set of documents. Our notion of categories can be automated and seems better than the more common approach of clusters, which are built via unsupervised learning harder to understand by human. How categories can be utilized in an IIR agent is also described.

Clustering analysis has attracted much attention in traditional IR research 1 . There is, however, little<sup>w</sup> <sup>x</sup> study about hierarchical categories and their representations. It is imperative to encourage more theoretical, as well as experimental, studies about categories.

## Acknowledgements

This work was partly supported by Grant NSC 87-2213-E-002-012 of the National Science Council of the Republic of China.

## References

<sup>w</sup> <sup>x</sup> 1 M.R. Anderberg, Cluster Analysis for Applications, Academic Press, New York, 1973.

<sup>w</sup> <sup>x</sup> 2 R. Armstrong, D. Freitag, T. Joachims, T. Mitchell, in: Web Watcher: A Learning Apprentice for the World Wide Web, AAAI Spring Symposium on Information Gathering from Heterogeneous, Distributed Environments, 1995.

<sup>w</sup> <sup>x</sup> 3 M. Balabanovic, Y. Shoham, in: Learning Information Re-´ trieval Agents: Experiments with Automated Web Browsing, AAAI-95 Spring Symposium on Information Gathering from Heterogenous, Distributed Environments, 1995.

<sup>w</sup> <sup>x</sup> 4 H. Berghel, Cyberspace 2000: dealing with information overload, Communications of the ACM 40 2 1997 19–24,Ž . Ž . February.

<sup>w</sup> <sup>x</sup> 5 H. Chen, Y.M. Chung, M. Ramsey, C.C. Yang, P.C. Ma, J. Yen, Intelligent spider for internet searching, in: Proceedings of the 30th Hawaii International Conference on System Sciences, HICSS-30 41997, pp. 242–252.

<sup>w</sup> <sup>x</sup> 6 F.-C. Cheong, Internet Agents: Spiders, Wanderers, Brokers, and Bots, New Riders Publishing, Indianapolis, IN, 1996.

<sup>w</sup> <sup>x</sup> 7 D.R. Cutting, D.R. Karger, J.O. Pedersen, J.W. Tukey, Scatter<sup>r</sup>Gather: A Cluster-Based Approach to Browsing Large Document Collections, SIGIR ’92, 1992.

<sup>w</sup> <sup>x</sup> 8 P. De Bra, R. Post, Information retrieval in the World Wide Web: making client-based searching feasible, in: 1st WWW Conference, Geneva, April, 1994.

<sup>w</sup> <sup>x</sup> 9 O. Etzioni, D. Weld, A softbot-based interface to the internet, Communications of the ACM 37 7 1994 72–76, July.Ž . Ž .

10 E.J. Guglielmo, N.C. Rowe, Natural-language retrieval of images based on descriptive captions, ACM Transactions on Information Systems 14 3 1996 237–267, July.Ž . Ž .

<sup>w</sup> <sup>x</sup> 11 J. Hsiang, H.-C. Tu, Personalized web retrieval: three agents for retrieving web information, in: The 1st Pacific Rim International Workshop on Multi-Agents, PRIMA ’98, 1998.

<sup>w</sup> <sup>x</sup> 12 A.K. Jain, R.C. Dubes, Algorithms for Clustering Data, Prentice-Hall, 1988.

<sup>w</sup> <sup>x</sup> 13 J.-S.R. Jang, C.-T. Sun, E. Mizutani, Neuro-Fuzzy and Soft Computing, Prentice-Hall, 1997, Chap. 6.

<sup>w</sup> <sup>x</sup> 14 D. Koller, M. Sahami, Hierarchically classifying documents using very few words, in: Proceedings of the 14th International Conference on Machine Learning ML , July, 1997.Ž .

<sup>w</sup> <sup>x</sup> 15 J.K.W. Lee et al., Intelligent agents for matching information providers and consumers on the World Wide Web, in: Proceedings of the 13th Annual Hawaii International Conference on System Sciences, IEEE, 1997.

<sup>w</sup> <sup>x</sup> 16 M.-0H. Lee, Java-based Personal Proxy Server and its Applications, Master Thesis, National Taiwan University, 1997.

<sup>w</sup> <sup>x</sup> 17 D.D. Lewis, R.E. Schapire, J.P. Callan, R. Papka, Training Algorithms for Linear Text Classifiers, ACM SIGIR ’96, 1996.

<sup>w</sup> <sup>x</sup> 18 S.-H. Liao, Personal Category Profiles for WWW Information Retrieval, Master Thesis, National Taiwan University, 1998.

<sup>w</sup> <sup>x</sup> 19 Y.S. Maarek, I.Z. Ben Shaul, Automatically organizing bookmarks per contents, in: 5th International World Wide Web Conference, May, 1996.

<sup>w</sup> <sup>x</sup> 20 J. Makhoui, S. Roucos, H. Gish, Vector quantization in speech coding, Proceedings of IEEE 73 11 1985 1551–Ž . Ž . 1588.

<sup>w</sup> <sup>x</sup> 21 A. Moukas, P. Maes, Amalthaea: an evolving multi-agent information filtering and discovery system for the WWW, Autonomous Agents and Multi-Agent Systems 1 1 1998Ž . Ž . 59–88.

<sup>w</sup> <sup>x</sup> 22 S. Russell, P. Norvig, Artificial Intelligence: A Modern Approach, Prentice-Hall, 1995.

<sup>w</sup> <sup>x</sup> 23 G. Salton, Automatic Text Processing: The Transformation, Analysis, and Retrieval of Information by Computer, Addison-Wesley, 1989.

<sup>w</sup> <sup>x</sup> 24 R. Schalkoff, Pattern Recognition: Statistical, Structural and Neural Approaches, Wiley, 1992.

<sup>w</sup> <sup>x</sup> 25 J. Schurmann, Pattern Classification: A Unified View of¨ Statistical and Neural Approaches, Wiley, 1996.

<sup>w</sup> <sup>x</sup> 26 H.-J. Zimmermann, Fuzzy Set Theory — and Its Applications, 2nd revised edn., Kluwer Academic Publishing, 1991.

Jieh Hsiang received a BS degree in Mathematics from the National Taiwan University in 1976 and a PhD degree in Computer Science from the University of Illinois at Urbana-Champaign in 1982. He is currently the Dean of the College of Science and Technology of the National Chi-Nan University, and a Professor of Computer Science at the National Taiwan University. Before returning to Taiwan in 1993, he was a Professor at the Department of Computer Science of the State University of New York at Stony Brook. Jieh Hsiang has done extensive research on automated deduction, term rewriting, and the logics of programming. He is the founder and chair of IFIP WG1.6, Working Group on Term Rewriting. In recent years, he has also been working on intelligent agents and digital libraries. Currently, he is in charge of a large-scale project on digitizing historical archives of Taiwanese history.

Hsieh-Chang Tu received a BS degree in Electrical and Electronic Engineering from the National Taiwan University in 1989 and a Master degree in Computer Science from the University of Maryland at College Park in 1994. He is currently a PhD candidate of the Department of Computer Science and Information Engineering at the National Taiwan University.
