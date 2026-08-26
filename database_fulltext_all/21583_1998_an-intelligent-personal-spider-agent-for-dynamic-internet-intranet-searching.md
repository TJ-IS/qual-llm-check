---
otero_id: 21583
otero_key: "GFWSAVC5"
title: "An intelligent personal spider (agent) for dynamic Internet/Intranet searching"
authors: "Chen Hsinchun; Chung Yi-Ming; Marshall Ramsey; Christopher C. Yang"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00035-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An intelligent personal spider agent for dynamicž / Internet<sup>r</sup>Intranet searching

Chen Hsinchun <sup>a,)</sup>, Chung Yi-Ming <sup>a,1</sup>, Marshall Ramsey <sup>a,2</sup>, Christopher C. Yang <sup>b,3</sup>

<sup>a</sup> MIS Department, Karl Eller Graduate School of Management, UniÕersity of Arizona, McClelland Hall 430Z, Tucson, AZ 85721, USA ECE Department, UniÕersity of Arizona, Tucson, AZ 85721, USA

## Abstract

As Internet services based on the World-Wide Web become more popular, information overload has become a pressing research problem. Difficulties with search on Internet will worsen as the amount of on-line information increases. A scalable approach to Internet search is critical to the success of Internet services and other current and future National Information Infrastructure NII applications. As part of the ongoing Illinois Digital Library Initiative project, this research proposes anŽ . intelligent personal spider agent approach to Internet searching. The approach, which is grounded on automatic textualŽ . analysis and general-purpose search algorithms, is expected to be an improvement over the current static and inefficient Internet searches. In this experiment, we implemented Internet personal spiders based on best first search and genetic algorithm techniques. These personal spiders can dynamically take a user’s selected starting homepages and search for the most closely related homepages in the web, based on the links and keyword indexing. A plain, static CGI<sup>r</sup>HTML-based interface was developed earlier, followed by a recent enhancement of a graphical, dynamic Java-based interface. Preliminary evaluation results and two working prototypes available for Web access are presented. Although the examples andŽ . evaluations presented are mainly based on Internet applications, the applicability of the proposed techniques to the potentially more rewarding Intranet applications should be obvious. In particular, we believe the proposed agent design can be used to locate organization-wide information, to gather new, time-critical organizational information, and to support team-building and communication in Intranets. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Agents; Machine learning; Spider; Evolutionary programming; Information retrieval; Semantic retrieval; Java; World-Wide Web; Internet; Intranet

## 1. Introduction

Although network protocols and software such as HTTP and Netscape<sup>r</sup>Mosaic support significantly ease importation and fetching of on-line information sources, their use is accompanied by the disadvantage of the users’ not being able to explore and find what they want in an enormous information space <sup>w</sup> <sup>x</sup> 1,2,20 . While the Internet services are popular and appealing to many on-line users, difficulties with search are expected to worsen as the amount of on-line information increases. This is mainly due to the problems of information overload and vocabulary differences 11,4 . Many researchers consider that<sup>w</sup> <sup>x</sup> devising a scalable approach to Internet search is critical to the success of Internet and Intranet services and other current and future National Information Infrastructure NII applications 21,6 .Ž . <sup>w</sup> <sup>x</sup>

The main information retrieval mechanisms provided by the prevailing Internet WWW-based software are based on either keyword search e.g., Ly- Ž cos, AltaVista, and Yahoo servers or hypertext . browsing e.g., NCSA Mosaic, Netscape Navigator, Ž and Microsoft Internet Explorer . Keyword search. often results in low precision, poor recall, and slow response time due to the limitations of indexing and communication methods bandwidth , controlled lan-Ž . guage-based interfaces the vocabulary problem andŽ . the inability of searchers themselves to fully articulate their needs. Furthermore, browsing allows users to explore only a very small portion of the large Internet information space. An extensive information space accessed through hypertext-like browsing can also potentially confuse and disorient its user, the ‘embedded digression problem,’ and it can cause the user to spend a great deal of time while learning nothing specific, the ‘art museum phenomenon’ 3 .<sup>w</sup> <sup>x</sup>

Our proposed approach, which is grounded on automatic textual analysis of Internet documents and general-purpose search algorithms, aims to address the Internet search problem by creating dynamic and ‘intelligent’ personal spiders agents that take usersŽ . requests and perform real-time, customized searches. In particular, best first search was adopted for a local search personal spider and a genetic algorithm was used to develop a global, stochastic personal spider. These personal spiders agents could dynamically Ž . take users’ selected starting homepages and search for the most closely related homepages in the web, based on the links and keyword indexing. Extensive algorithmic revisions and interface development based on CGI<sup>r</sup>HTML and Java have been performed. This paper summarizes our current research effort.

We believe that the applicability of the proposed techniques to the potentially more rewarding Intranet applications is promising and specifically includes adoption of the proposed agent design in the following Intranet-related areas.

<sup>Ø</sup>Locating organization-wide information. By restricting the agent to search on servers within the organizational Intranet boundary i.e., selected URLsŽ or domain names , the proposed agent can be used to. help users find only related Intranet sites instead of wandering through the Internet. For large corporations and government agencies, the need to explore and search effectively within their own loosely-connected Intranet sites is real and pressing. By restricting the search space of the proposed agent, the tool could be used to locate organization-wide Intranet information.

<sup>Ø</sup> Gathering new, time-critical organizational information. The value of the agent-based spider strongly relies on its ability to perform exhaustive and real-time Internet or Intranet searches. Obsolete and dead Web sites can be avoided—the proposed agent imposes a time-out component to avoid connecting to dead sites. Such design is believed to enable the agent to gather new, time-critical organizational information.

<sup>Ø</sup>Team-building and communications. In our discussion with several Webmasters, it has been suggested that the tool could be used in Intranets for team-building and communication. By launching their own spiders within Intranets, different teams and groups, previously unknown to each other in large corporations, would be able to find Cyberspace collaborators and colleagues, thereby using it effectively as an organizational communication tool.

## 2. Literature review: Internet spiders

At its inception as the ARPANET, the Internet was conceived primarily as a means of remote log-in and experimentation with telecommunication 2 .<sup>w</sup> <sup>x</sup> However, the predominant usage quickly became e-mail communication. This trend continues into the present form of the Internet, but with increasingly diverse support for collaborative data sharing and distributed, multimedia information access, especially using the World-Wide Web WWW . ManyŽ . people consider the Internet and the WWW the backbone of the information superhighway and the window to the cyberspace.

The WWW was developed initially to support physicists and engineers at CERN, the European Particle Physics Laboratory in Geneva, Switzerland <sup>w</sup> <sup>x</sup> 1 . In 1993, when several browser programs mostŽ noticeably the NCSA Mosaic became available for. distributed, multimedia, hypertext-like information fetching, Internet became the preview for a rich and colorful information cyberspace 22 . However, as <sup>w</sup> <sup>x</sup> Internet services based on WWW have become more popular, information overload has become a pressing research problem 2 . The user interaction paradigm <sup>w</sup> <sup>x</sup> on Internet has been shifted from simple hypertextlike browsing Žhuman-guided activity exploring the organization and contents of an information space to. content-based searching Ža process in which the user describes a query and a system locates information that matches the description . Many researchers and. practitioners have considered Internet<sup>r</sup>Intranet searching to be one of the more pressing and rewarding areas of research for future NII applications.

Internet searching has been the hottest topic at recent World-Wide Web Conferences. Two major approaches have been developed and experimented with: 1 the client-based search spider agent and Ž . Ž . Ž . 2 the on-line database indexing and searching. However, some systems contain components of both approaches.

## 2.1. Client-based search spiders agents( )

Broadly defined, an ‘agent’ is a program that can operate autonomously and accomplish unique tasks without direct human supervision similar to human Ž counterparts, such as real estate agents, travel agents, etc. . The basic idea of agent research is to develop . software systems which engage and help all types of end users 19 . Such agents might act as ‘spiders’ on<sup>w</sup> <sup>x</sup> the Internet and look for relevant information 10 ,<sup>w</sup> <sup>x</sup> analyze meeting output on behalf of executives 5 , <sup>w</sup> <sup>x</sup> or filter newsgroup articles based on ‘induced’ orŽ learned users’ profiles 14 . Many researchers have. <sup>w</sup> <sup>x</sup> focused on developing scripting and interfacing languages for designers and users such that they can create mobile agents of their own 24 . Some re-<sup>w</sup> <sup>x</sup> searchers attempt to address the question: ‘‘How should agents interact with each other to form digital teamwork?’’ Other researchers are more concerned about designing agents which are ‘intelligent’ 19,5 .<sup>w</sup> <sup>x</sup>

Several software programs based on the concept of spiders, agents, or softbots software robots haveŽ . been developed. TueMosaic and the WebCrawler are two prominent early examples. Both of them use variations of conventional best first local searchŽ . strategies 17 . DeBra and Post 9 reported tueMo-<sup>w</sup> <sup>x</sup> <sup>w x</sup> saic v2.42, modified at the Eindhoven University of Technology TUE using the ‘fish search’ algorithm,Ž . at the First WWW Conference in Geneva. Using tueMosaic, users can enter keywords, specify the depth and width of search for links contained in the current homepages displayed and request the spider agent to fetch homepages connected to the current homepage. The fish search algorithm is a modified best first search method. However, potentially relevant homepages that do not connect with the currently active homepages cannot be retrieved and, when the depth and breadth of search become large Ž . an exponential search , the search space becomes enormous. The inefficiency and local search characteristics of BFS<sup>r</sup>DFS-based spiders and the communication bandwidth bottleneck on Internet severely constrained the usefulness of such a local search approach. At the Second WWW Conference, Pinkerton reported a more efficient spider crawler . TheŽ . WebCrawler extends the tueMosaic’s concept to initiate the search using its index and to follow links in an intelligent order. Webcrawler evaluates the relevance of a link based on its similarity to the anchor texts of the user’s query. However, problems with local search and communication bottleneck persist.

Due to the proliferation of WWW sites, many newer spiders with different functionalities recently have been developed. The TkWWW robot was developed by Spetka and funded by the Air Force Rome Laboratory 23 . TkWWW robots are dis-<sup>w</sup> <sup>x</sup> patched from the TkWWW browser and are designed to search Web neighborhoods to find logically related homepages and return a list of ‘hot’ links. However, their search process is limited to one or two local links from the original homepages. TkWWW robots can also be run in the background to build HTML indexes, compile WWW statistics, collect a portfolio of pictures, or perform any other functions that can be described by TkWWW Tcl extensions. WebAnts, developed by Leavitt at Carnegie Mellon University, investigates the distribution of information collection tasks to a number of cooperating agents ants . The goal of WebAnts is toŽ . create cooperating agents that share searching results and indexing load without repeating each other’s effort. The RBSE Respository-Based Software En-Ž gineering spider was developed by Eichmann and. funded by NASA. RBSE spider was the first spider to index documents by content. It uses the Mite program to fetch documents and uses four local search mechanisms: 1 breadth first search from aŽ . given URL, 2 limited depth first search from a Ž . given URL, 3 breadth first search from unvisited Ž . URLs in the database and 4 limited depth firstŽ . search from unvisited URLs in the database. For aŽ complete review of other similar Internet spiders<sup>r</sup>agents, readers are referred to Ref. 8 .<sup>w</sup> <sup>x</sup> .

## 2.2. On-line database indexing and searching

An alternative approach to Internet resource discovery is based on the database concept of indexing and keyword searching. Such systems collect complete or partial Web documents and store them on the host server. These documents are then keyword indexed on the host server to provide a searchable interface. Most popular Internet databases such as Lycos, AltaVista, and Yahoo are based on such a design.

Lycos, developed at CMU 15 , uses a combina-<sup>w</sup> <sup>x</sup> tion of spider fetching and simple owner-registration. Internet servers can access the Lycos server and complete registration in a few simple steps. In addition, Lycos uses spiders based on the connections to the registered homepages to identify other un-registered homepages. With this suite of techniques, Lycos has acquired an impressive list of URLs on the Internet. Lycos adopted a heuristics-based indexing approach for these homepages that indexes them based on title, headings and subheadings, 100 most important words, first 20 lines, size in bytes and number of words. However, the success of Lycos also illustrates the vulnerability of the approach and the daunting task of creating ‘intelligent’ and efficient Internet search engines. Its popularity has caused a severe degradation of information access performance, due to the communication bottleneck and the task of finding selected documents in an all-in-one database of Internet homepages.

AltaVista, developed at Digital’s Research Laboratories in Palo Alto, combines a fast Web crawler with scalable indexing software to build a large index of the Web. It was made public on 15 December 1995 and has quickly become one of the most comprehensive searchable databases on the Internet. It also provides a full-text index that is updated in real-time for over 13 000 news groups. Although based on similar local search spider algorithms, the AltaVista server has been successful due to its superior hardware platforms and high-end communication bandwidth.

Instead of taking the all-in-one database approach adopted by Lycos and AltaVista, the Yahoo server represents an attempt to partition the Internet information space to provide meaningful subject categories e.g., science, entertainment, engineering, Ž etc. . However, its manually-created subject cate-. gories are limited in their granularity and the process of creating such categories is cumbersome and timeconsuming. The demand to create up-to-date and fine-grained subject categories and the requirement that an owner place a homepage under a proper subject category has significantly hampered Yahoo’s success and popularity.

## 3. Research design and algorithms

Funded by the ongoing Illinois Digital Library Initiative project 21,7 , this research aims to create<sup>w</sup> <sup>x</sup> ‘intelligent’ Internet personal search agents that can be deployed on the Web for efficient, timely, and optimal searches. We planned to answer the following two general research questions: 1 Can an Inter-Ž . net spider be designed to take individual users’ requests and perform a global, optimal search on the Internet i.e., not restricted by the links connected to Ž the starting<sup>r</sup>anchor homepages ? and 2 Can a dy-. Ž . namic, agent-based interface be designed to allow users to present requests, evaluate intermediate results and perform analysis during personal spider search sessions?

After a careful evaluation of many general-purpose search algorithms, a genetic algorithm GA ,Ž . which featured a global, stochastic search process, was examined in detail. The complex and dynamic nature of the Internet<sup>r</sup>WWW appears to be suited for application of such an algorithm. A comparison of a GA-based personal spider and a conventional best first search BFS spider was performed in ourŽ . experiment.

An earlier version of a CGI<sup>r</sup>HTML interface for GA<sup>r</sup>BFS spiders revealed the inadequacy of the stateless, static HTML interface. A prototype interface based on Java was, therefore, designed to allow dynamic interactions between users and personal agents.

In this section, we describe the search algorithms implemented. Our CGI<sup>r</sup>HTML and Java interface will be illustrated in the next section.

## 3.1. Determining score<sup>r</sup>fitness: the Jaccard’s function

In order to determine the ‘goodness’ or fitness,Ž using GA terminology of a given new homepage, a. Jaccard’s similarity function was adopted 18 . Each<sup>w</sup> <sup>x</sup> homepage was represented as a weighted vector of keywords, that had been automatically indexed by our system and connecting links. A new homepage fetched by the system was compared with the anchor<sup>r</sup>starting homepages to determine whether or not it was promising. A new homepage which is more similar to the starting homepages was considered more promising, thus, it was explored first. The Jaccard’s functions adopted were based on the combined equal weights of the Jaccard’s score from Ž . links and the Jaccard’s score from keywords.

<sup>Ø</sup> Jaccard’s scores from links. Given two homepages, A and B, and their connected links<sup>r</sup>URLs, $X = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { m } )$ and $Y = ( y _ { 1 } , y _ { 2 } , \dots , y _ { n } ) .$ , the Jaccard’s score between A and B based on links was computed as follows:

$$
J _ {\text { link }} (\mathrm{A}, \mathrm{B}) = \frac {\# (X \cap Y)}{\# (X \cup Y)},\tag{1}
$$

where aŽ . S indicates the cardinality of set S.

<sup>Ø</sup> Jaccard’s scores from keywords. For a given homepage, terms were identified based on an automatic indexing procedure developed in our previous research 7 . Term frequency tf and inverse docu-<sup>w</sup> <sup>x</sup> Ž . ment frequency idf , term weighting heuristics alsoŽ . adopted in such popular searchable databases as Lycos, were then computed. Term frequency, $\mathrm { t f } _ { i j } ,$ represents the number of occurrences of term j in document homepage Ž . i. Homepage frequency, $\mathrm { d f } _ { j } ,$ represents the number of homepages in a collection of N homepages in which term j occurs. The combined weight of term j in homepage i, $d _ { i j } .$ was computed as follows:

$$
d _ {i j} = \operatorname{tf} _ {i j} \times \log \left(\frac {N}{\operatorname{df} _ {j}} \times w _ {j}\right),\tag{2}
$$

where $w _ { j }$ represents the number of words in term j and N represents the total number of homepages connected to the starting homepages.Representing each homepage as a weighted vector of keywords, the Jaccard’s score between homepages A and B based on keyword was computed as follows:

$$
\begin{array}{l} J _ {\text { keyword }} (\mathrm{A}, \mathrm{B}) \\ = \frac {\sum_ {j = 1} ^ {L} d _ {\mathrm{A} j} d _ {\mathrm{B} j}}{\sum_ {j = 1} ^ {L} d _ {\mathrm{A} j} ^ {2} + \sum_ {j = 1} ^ {L} d _ {\mathrm{B} j} ^ {2} - \sum_ {j = 1} ^ {L} d _ {\mathrm{A} j} d _ {\mathrm{B} j}}, \end{array}\tag{3}
$$

where L is the total number of terms.

The combined Jaccard’s score between any two homepages, A and B, was a weighted summation of the above two Jaccard’s scores, i.e.,

$$
J (\mathrm{A}, \mathrm{B}) = 0. 5 \times J _ {\text { link }} (\mathrm{A}, \mathrm{B}) + 0. 5 \times J _ {\text { keyword }} (\mathrm{A}, \mathrm{B}).\tag{4}
$$

## 3.2. Best first search algorithm

Two search algorithms, best first search and a genetic algorithm, were investigated in detail. The best first search algorithm was developed to simulate the various client-based spiders developed in earlier studies and were used as a benchmark for comparison. The genetic algorithm was adopted to enhance the global, optimal search capability of existing Internet spiders.

Best first search is a serial state space traversal method 17 . In our implementation, the algorithm<sup>w</sup> <sup>x</sup> explored the best based on Jaccard’s score of new Ž homepage vs. anchor homepages homepage at each . iteration and terminated when the system had identified the desired number of homepages requested by a user. A sketch of the best first search algorithm adopted in our personal agent is presented below.

## 3.2.1. Input anchor homepages and initialize

Initialize an iteration counter k to 0. Obtain a desired number of homepages from users and a set of input anchor homepages, $( \mathrm { i n p u t } _ { 1 } , \mathrm { i n p u t } _ { 2 } , \ldots ,$ , in-$\mathrm { p u t } _ { m } ) .$ These input homepages represent the users’ preferred starting points for Internet search and their interests. Texts of homepages are fetched over the network in real time via Lynx HTTP communication software and homepages URLs connected fromŽ . these input homepages are extracted and saved in the unexplored homepage queue, H, where $H = { { \left( { { h _ { 1 } } } \right. } }$ $h _ { 2 } , \ldots , h _ { n } )$

## 3.2.2. Determine the best homepage

Based on the Jaccard’s function described earlier, determine the best homepage, p, in H, which has the highest Jaccard’s score among all the homepages in H and save it as output . This homepage is considered most similar to the anchor homepages in both keywords and links, thus, it should be explored first.

## 3.2.3. Explore the best homepage

Fetch the best homepage using Lynx and add its connected homepages to the unexplored homepage queue, H. Increment iteration counter k by one.

## 3.2.4. Iterate until a desired number of homepages is obtained

Repeat the above steps until k is equal to the total number of homepages requested by the user.

## 3.3. Genetic algorithm

Genetic algorithms GAs 12,16,13 areŽ . <sup>w</sup> <sup>x</sup> problem-solving systems based on principles of evolution and heredity. Genetic algorithms perform a stochastic evolution process toward global optimization through the use of cross-over and mutation operators. The search space of the problem is represented as a collection of individuals, which are referred as chromosomes. The quality of a chromosome is measured by a fitness function Jaccard’sŽ score in our implementation . After initialization,. each generation produces new children based on the genetic cross-over and mutation operators. The process terminates when two consecutive generations do not produce noticeable population fitness improvement i.e., reach a small threshold value or converge .Ž . A sketch of the genetic algorithm adopted for Internet client-based searching is presented below.

## 3.3.1. Initialize the search space

The GA spider attempts to find other most relevant homepages in the entire Internet search space using the user-supplied starting homepages. Initially, the system saves all the input homepages in a set called Current Generation, $\mathbf { C G } = ( \mathbf { c g } _ { 1 } , \mathbf { c g } _ { 2 } , \ldots , \mathbf { c g } _ { m } ) .$

## 3.3.2. Cross-oÕer

A heuristics-based cross-over operation is then used. New homepages connected to starting homepages in CG set are extracted. Homepages that have been connected to multiple starting homepages i.e.,Ž multiple parents are considered Cross-over Home-. pages and saved in a new set, $C = \{ c _ { 1 } , c _ { 2 } , \ldots \}$

## 3.3.3. Mutation

In order to avoid trapping in the local minimum that might result from adopting a simple cross-over operator, we have added a heuristics-based mutation procedure to add diversity to the homepage population. A Yahoo spider created in our previous research is used to traverse Yahoo’s 14 high-level subject categories e.g., science, business, entertain- Ž ment, etc. and collect several thousands of ‘muta-. tion seed’ homepages in each category. These homepages are indexed using the Web indexing freeware, SWISH Simple Web Indexing System for Humans .Ž . When the GA search algorithm requests a mutated homepage, the system retrieves the top-ranked homepage from homepages in the user-specified category based on the keywords presented in the anchor homepages. This process is similar to performing a search on the Yahoo database in order to suggest new, promising homepages for further exploration.

New mutated homepages are saved in the set of Mutation Homepages, $M = \{ m _ { 1 } , m _ { 2 } , . . . \}$

The probabilities of mutation and cross-over can vary depending on user needs. Higher cross-over probabilities generally support exploitation of local linkages, while higher mutation probabilities support exploration of the global landscape. Exploitation and exploration are two powerful features of genetic programming 16 . Our default settings for both<sup>w</sup> <sup>x</sup> cross-over and mutation probabilities are 50%.

## 3.3.4. Stochastic selection scheme based on Jaccard’s fitness

Each new cross-over and mutation homepage is evaluated based on the same Jaccard’s function. Based on an ‘elicit selection’ procedure 16 , home- <sup>w</sup> <sup>x</sup> pages which obtain higher fitness values are selected stochastically. A random number generator controlled by a homepage’s fitness value is used to select ‘fitter’ homepages for the new generation. Homepages that ‘survive’ the nature selection pro-Ž . cedure become the new population for the new generation.

## 3.3.5. ConÕergence

Repeat the above steps until the improvement in total fitness between two generations is less than a small threshold value empirically determined . The Ž . final converged set of homepages is then presented to users as the output homepages.

## 4. Benchmarking experiment

In an attempt to examine the quality of results obtained by best first search and genetic algorithm, we performed a set of benchmarking experiments, which compared the performances and efficiency of the best first search and genetic algorithm-based personal spiders. Using a test set of 40 search scenarios, each composed of one to three homepages in different subject areas, we examined the final Jaccard’s scores of the BFS<sup>r</sup>GA-suggested top 10 Ž . homepages and their corresponding CPU times and wall clock times. Higher Jaccard’s scores of new homepages would suggest a closer match to a user’s stated query interests i.e., the anchor Ž <sup>r</sup>starting homepages ..

Detailed benchmarking results are presented in Table 1. Figs. 1–3 show statistical analyses of the final fitness score, CPU time and wall clock time of testing 40 cases.

Table 1  
Detailed statistics of the benchmarking results for 40 test cases

<table><tr><td colspan="2">Final Jaccard&#x27;s score</td><td colspan="2">CPU time (s)</td><td colspan="2">Wall clock time (s)</td></tr><tr><td>GA</td><td>BFS</td><td>GA</td><td>BFS</td><td>GA</td><td>BFS</td></tr><tr><td>0.064111</td><td>0.171631</td><td>355</td><td>449</td><td>3677</td><td>3361</td></tr><tr><td>0.037873</td><td>0.033949</td><td>390</td><td>428</td><td>13053</td><td>4371</td></tr><tr><td>0.116297</td><td>0.030918</td><td>121</td><td>31</td><td>722</td><td>772</td></tr><tr><td>0.084534</td><td>0.086722</td><td>181</td><td>67</td><td>1890</td><td>535</td></tr><tr><td>0.078234</td><td>0.078808</td><td>203</td><td>48</td><td>4840</td><td>551</td></tr><tr><td>0.172200</td><td>0.169866</td><td>111</td><td>375</td><td>2334</td><td>2861</td></tr><tr><td>0.055612</td><td>0.067690</td><td>267</td><td>14</td><td>3226</td><td>175</td></tr><tr><td>0.038149</td><td>0.049555</td><td>209</td><td>59</td><td>4636</td><td>1539</td></tr><tr><td>0.139013</td><td>0.121848</td><td>260</td><td>15</td><td>1646</td><td>448</td></tr><tr><td>0.142467</td><td>0.140435</td><td>239</td><td>167</td><td>13684</td><td>1800</td></tr><tr><td>0.084445</td><td>0.081548</td><td>198</td><td>95</td><td>1868</td><td>641</td></tr><tr><td>0.039268</td><td>0.041037</td><td>149</td><td>35</td><td>2865</td><td>497</td></tr><tr><td>0.073365</td><td>0.047864</td><td>201</td><td>110</td><td>1474</td><td>526</td></tr><tr><td>0.105819</td><td>0.084379</td><td>132</td><td>62</td><td>502</td><td>1081</td></tr><tr><td>0.124926</td><td>0.116992</td><td>294</td><td>111</td><td>2659</td><td>1970</td></tr><tr><td>0.223007</td><td>0.211883</td><td>246</td><td>41</td><td>3663</td><td>698</td></tr><tr><td>0.060740</td><td>0.061900</td><td>140</td><td>160</td><td>540</td><td>2384</td></tr><tr><td>0.067829</td><td>0.055259</td><td>263</td><td>195</td><td>1470</td><td>1678</td></tr><tr><td>0.077254</td><td>0.037858</td><td>160</td><td>105</td><td>1134</td><td>679</td></tr><tr><td>0.089374</td><td>0.052490</td><td>139</td><td>148</td><td>1095</td><td>6215</td></tr><tr><td>0.076198</td><td>0.089744</td><td>116</td><td>4</td><td>2181</td><td>1219</td></tr><tr><td>0.069978</td><td>0.094988</td><td>164</td><td>20</td><td>2265</td><td>201</td></tr><tr><td>0.075281</td><td>0.084414</td><td>198</td><td>28</td><td>2314</td><td>536</td></tr><tr><td>0.146929</td><td>0.198999</td><td>212</td><td>22</td><td>1862</td><td>111</td></tr><tr><td>0.156446</td><td>0.170072</td><td>139</td><td>206</td><td>1505</td><td>1260</td></tr><tr><td>0.096210</td><td>0.130226</td><td>156</td><td>16</td><td>2125</td><td>139</td></tr><tr><td>0.059283</td><td>0.055598</td><td>114</td><td>137</td><td>2498</td><td>1684</td></tr><tr><td>0.065573</td><td>0.050638</td><td>110</td><td>22</td><td>2016</td><td>193</td></tr><tr><td>0.045675</td><td>0.058230</td><td>173</td><td>44</td><td>1851</td><td>372</td></tr><tr><td>0.072970</td><td>0.069212</td><td>129</td><td>60</td><td>1716</td><td>6033</td></tr><tr><td>0.075478</td><td>0.055161</td><td>314</td><td>190</td><td>6452</td><td>1890</td></tr><tr><td>0.072598</td><td>0.079657</td><td>197</td><td>29</td><td>2898</td><td>513</td></tr><tr><td>0.096236</td><td>0.130226</td><td>158</td><td>17</td><td>2249</td><td>140</td></tr><tr><td>0.033593</td><td>0.024276</td><td>106</td><td>43</td><td>811</td><td>788</td></tr><tr><td>0.060900</td><td>0.038381</td><td>127</td><td>200</td><td>1148</td><td>1861</td></tr><tr><td>0.030297</td><td>0.019969</td><td>144</td><td>143</td><td>896</td><td>1107</td></tr><tr><td>0.083009</td><td>0.049055</td><td>111</td><td>19</td><td>1001</td><td>167</td></tr><tr><td>0.149195</td><td>0.133777</td><td>407</td><td>396</td><td>2848</td><td>4944</td></tr><tr><td>0.065770</td><td>0.105248</td><td>245</td><td>22</td><td>1636</td><td>533</td></tr><tr><td>0.075966</td><td>0.026925</td><td>98</td><td>121</td><td>2384</td><td>508</td></tr><tr><td>0.087053</td><td>0.085186</td><td>191.9</td><td>111.3</td><td>2741</td><td>1425</td></tr></table>

<table><tr><td colspan="6">ANALYSIS OF VARIANCE</td></tr><tr><td>SOURCE</td><td>DF</td><td>SS</td><td>MS</td><td>F</td><td>p</td></tr><tr><td>FACTOR</td><td>1</td><td>0.00007</td><td>0.00007</td><td>0.03</td><td>0.857</td></tr><tr><td>ERROR</td><td>78</td><td>0.16535</td><td>0.00212</td><td></td><td></td></tr><tr><td>TOTAL</td><td>79</td><td>0.16541</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td colspan="2">INDIVIDUAL 95 PCT CI&#x27;S FOR MEAN BASED ON POOLED STDEV</td></tr><tr><td>LEVEL</td><td>N</td><td>MEAN</td><td>STDEV</td><td colspan="2">- - - - - - + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -</td></tr><tr><td>BFS</td><td>40</td><td>0.08519</td><td>0.04996</td><td colspan="2">(- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - )</td></tr><tr><td>GA</td><td>40</td><td>0.08705</td><td>0.04176</td><td colspan="2">(- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - )</td></tr><tr><td colspan="2">POOLED STDEV =</td><td>0.04604</td><td></td><td>0.080</td><td>0.090</td></tr></table>

Fig. 1. Statistics of the average Jaccard’s scores obtained from 40 test cases by best first search and genetic algorithm.

<table><tr><td colspan="6">ANALYSIS OF VARIANCE</td></tr><tr><td>SOURCE</td><td>DF</td><td>SS</td><td>MS</td><td>F</td><td>p</td></tr><tr><td>FACTOR</td><td>1</td><td>129766</td><td>129766</td><td>12.81</td><td>0.001</td></tr><tr><td>ERROR</td><td>78</td><td>790235</td><td>10131</td><td></td><td></td></tr><tr><td>TOTAL</td><td>79</td><td>920001</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td colspan="2">INDIVIDUAL 95 PCT CI&#x27;S FOR MEAN BASED ON POOLED STDEV</td></tr><tr><td>LEVEL</td><td>N</td><td>MEAN</td><td>STDEV</td><td colspan="2">+----+----+----+----+----</td></tr><tr><td>BFS</td><td>40</td><td>111.3</td><td>118.4</td><td colspan="2">(----*----)</td></tr><tr><td>GA</td><td>40</td><td>191.9</td><td>79.0</td><td></td><td>(----*----)</td></tr><tr><td></td><td></td><td></td><td></td><td colspan="2">+----+----+----+----</td></tr><tr><td colspan="2">POOLED STDEV =</td><td>100.7</td><td></td><td>80</td><td>120</td></tr></table>

Fig. 2. Statistics of the CPU time for 40 test cases by best first search and genetic algorithm.

## 4.1. Complementary searches through exploitation and exploration

The results show that the output homepages obtained by genetic algorithm had a slightly higher fitness score than those obtained by best first search, but the difference is not significant. The averages of 40 Jaccard’s scores for the genetic algorithm and the best first search were 0.08705 and 0.08519, respectively. Although the Jaccard’s scores showed no significant difference between the performances of genetic algorithm and best first search, we noticed that about 50% of the homepages obtained from the genetic algorithm were the result of the mutation operation cross-over and mutation probabilities wereŽ set to 50% and 50%, respectively . We found that . these homepages, although promising, had never been linked to the starting homepages, thus, they could not have been obtained by any local search spiders Ž . including our best first search spider . This suggests the potential usefulness of the genetic algorithm spider to supplement the local best first search spider, i.e., by permitting combination of the results in both sets.

![](/api/attachments/GFWSAVC5/fulltext/images/d5c27f86daaeb78c370627937982900f5da23566bd691064bb5d3eeb3368743f.jpg)  
Fig. 3. Statistics of the wall clock time for 40 test cases by best first search and genetic algorithm.

During our experimentation, we also found that the genetic algorithm performed very similarly to best first search when the mutation probabilities were set low say 5% and cross-over probabilitiesŽ . were high say 95% . With limited mutation opera-Ž . tions, the cross-over operation in genetic algorithm accomplished a local exploitation process similar to that of a local best first search. The mutation process appears to have been instrumental in allowing our personal spider to get out of the local search minimum.

## 4.2. Sparse link constraint

In addition, we also noticed that starting homepages played an important role in determining system output. If starting homepages contained very few and sparsely connected links, best first search spiders tended to get trapped quickly in the Internet search space because of lack of traversal paths. The genetic algorithm, however, was not restricted by such a sparse link constraint because of its mutation operator. On the other hand, for starting homepages that contained rich and dense connections, best first search often resulted in a fruitful final search set. The genetic algorithm only added limited diversity in such a scenario.

![](/api/attachments/GFWSAVC5/fulltext/images/142e959e3cd33f2f241b8d502eb389c02cd730f6738ce2ccaad2d2836020c89b.jpg)  
Fig. 4. The CGI<sup>r</sup>HTML spider homepage.

![](/api/attachments/GFWSAVC5/fulltext/images/3249163b7038318988b610ee9aa0aa046c2856d7e21598deda042d7a09c1470d.jpg)  
Fig. 5. The input homepage of the local best first search spider.

![](/api/attachments/GFWSAVC5/fulltext/images/d618b2680e9d867c68d1996f849bd703d07fe05b7ef362f5a2f5974a5f69449a.jpg)  
Fig. 6. The input homepage of the global genetic algorithm search spider.

4.3. Exploration and communication are time consuming

The genetic algorithm-based spider was significantly more time-consuming than the best first search spider, as shown in Figs. 2 and 3. The average CPU times for best first search and genetic algorithm were 3 min and 11 s and 1 min and 51 s, respectively. However, due to the communication bottleneck, the average wall clock time for best first search and genetic algorithm were 45 min and 41 s and 23 min and 45 s, respectively. The SWISH keyword search procedure implemented in the genetic algorithm spider caused a significant CPU time requirement. The elite selection procedure and multiple generations also consumed significant CPU cycles.

![](/api/attachments/GFWSAVC5/fulltext/images/1730ac7fcfdca6d9c2f55197b5d4dd441daede28cfd04322607d83c7a16ccafc.jpg)  
Fig. 7. The output homepage of the global genetic algorithm search spider.

However, the communication bandwidth i.e., theŽ actual time to fetch a remote homepage seemed to. be the most significant bottleneck of the entire process for both the best first search spider and the genetic algorithm spider. This deficiency can only be resolved when the current Internet backbones are upgraded.

## 5. Dynamic, agent-based interface

Currently, we have developed two interfaces for our spiders. One is based on CGI<sup>r</sup>HTML and the other is based on Java. The CGI<sup>r</sup>HTML implementation enables image maps and fill-out forms to interact with the HTTP server. However, it is static and does not support dynamic display and interaction during the search process.

![](/api/attachments/GFWSAVC5/fulltext/images/c97a26fd40e523c4f228e8b6458bcebdc0870296f1a7c25700e59d5cd5b15db3.jpg)  
Fig. 8. The Java spider homepage.

On the other hand, Java is an object-oriented, platform-independent, multi-threaded, dynamic, graphical, general-purpose programming environment for the Internet, Intranet and any other complex, distributed network. The Java interface allows us to display lively intermediate spider search results and accept changes of input parameters e.g., cross- Ž over and mutation probabilities dynamically. These. dynamic, interactive features of Java are crucial to the design of customizable and ‘intelligent’ agents <sup>w</sup> <sup>x</sup> <sub>5 .</sub>

The two prototype interfaces are summarized below. Readers are encouraged to connect to the University of Arizona Artificial Intelligence Group homepage http: Ž . <sup>rr</sup>ai.bpa.arizona.edu<sup>r</sup> for actual demonstrations.

## 5.1. CGI-based user interface

The CGI-based user interface provides fill-in forms that let users submit input to the spiders. Users may request local or global search, as shown in Fig. 4. Invoking the local search spider, as shown in Fig. 5, users are requested to provide up to five starting URLs. Users also need to indicate the desired number of searched homepages and preferred types of servers.

Similarly, invoking the global search spider results in a fill-in form as shown in Fig. 6. The

![](/api/attachments/GFWSAVC5/fulltext/images/5d91c6a5c56eaab8b7f4e2dc686b139f49201ca37dc78e062bb5e01b7df79d64.jpg)  
Fig. 9. The control panel for initiating a Java-based genetic algorithm spider.

evolution-based option activates the genetic algorithm spider. The probability-based option activates a simulated annealing-based spider developed earlier in our research. In addition to providing starting URLs and the desired number of homepages, users also need to indicate their preferred ‘mutation seed database to draw new mutation homepages.

After submitting the search request, Fig. 7 shows an output homepage which displays the system-suggested relevant homepages, with a title and keyword summary. Each homepage can then be clicked on for closer examination. Due to the real-time nature of our spiders, all homepages retrieved are ‘alive,’ unlike many ‘dead’ homepages often found in other all-in-one searchable homepage databases.

![](/api/attachments/GFWSAVC5/fulltext/images/d96f24093d43803ae5a90593dfbfecc4386cdd4962139115a31b923f07d27713.jpg)  
Fig. 10. The display window shows the result of the search process dynamically. Animation is displayed on the upper right-hand corner. Control panel which allows user to change parameters during the process is located at the upper portion. Search results are summarized at the center of the window.

## 5.2. JaÕa-based user interface

Despite these ‘intelligent’ and customized search processes, the CGI<sup>r</sup>HTML interface is severely hampered by its lack of dynamic display and interaction. A Java-based user interface was designed to alleviate these problems.

The Java interface homepage is shown in Figs. 8 and 9. When ‘global evolution-based search’ is clicked on, the system displays a dialog block similar to that designed for the CGI<sup>r</sup>HTML genetic algorithm spider interface. In addition, users can set their preferred cross-over and mutation probabilities. A time-out mechanism was also introduced to avoid the system from time-consuming, unfruitful connections.

Fig. 10 shows the window which displays the result of the entire search process dynamically and graphically. The control panel is displayed at the top of the window. All input parameters can be changed during an ongoing search process, producing different search results. The fetched URLs are displayed during each generation instead of the final results atŽ the last generation and can be clicked on for real-. time evaluation. The system also graphically displays the Jaccard’s link score, keyword score and fetch time score for each homepage in three different Ž colors, not shown in the attached screen dump . A . spider-chasing-fly animation is displayed dynamically when our ‘spider’ is out chasing a new homepage fly . Ž .

Since we placed our Java-based spider on our server in Summer 1996, the response from our initial test subjects was overwhelming. Users found the Java-based interface to be more interactive, lively and friendly than our earlier CGI<sup>r</sup>HTML interface. They have reported our spider to be a dynamic, intelligent personal agent, instead of a static, noncustomizable Internet database search engine.

## 6. Discussion and Conclusion

The results from our current experimentation of Internet personal spiders are encouraging. In response to Research Question 1 designing a global Ž optimal search spider , although the genetic algo- . rithm spider did not out-perform the best first search spider, we found both results to be comparable and complementary. The mutation process introduced in genetic algorithm allows users to find other potential relevant homepages that cannot be explored via a conventional local search process. Regarding Research Question 2, we found the Java-based interface to be a necessary component for designing an interactive and dynamic Internet agent. The CGI<sup>r</sup>HTML interface is simply too restrictive for such a task.

Although the examples and evaluations presented are mainly based on Internet applications, the applicability of the proposed techniques to the potentially more rewarding Intranet applications should be obvious. In particular, we believe that the proposed agent design can be used to locate organization-wide information, to gather new, time-critical organizational information and to support team-building and communication in Intranets.

In our ongoing effort in the Illinois Digital Library Initiative project, we are in the process of exploring other general-purpose search and classification algorithms for Internet resource categorization and search. Several neural network-based algorithms have been explored, including the Hopfield network and the Kohonen self-organizing map, both are under development in Java.

## Acknowledgements

We would like to thank University of Arizona Artificial Intelligence Group members for their participation in our experiment. We also thank Prof. Jerome Yen of Hong Kong University and Prof. Pai-chun Ma of Hong Kong University of Science and Technology for their comments and involvement during system development and testing. This project was supported mainly by the following grants: NSF<sup>r</sup>ARPA<sup>r</sup>NASA Digital Library Initiative, IRI-9411318, 1994–1998 B. Schatz, H. Chen et al., Ž Building the Interspace: Digital Library Infrastructure for a University Engineering Community ; NSF . CISE, IRI-9525790, 1995–1998 H. Chen, Concept-Ž based Categorization and Search on Internet: a Machine Learning, Parallel Computing Approach ; AT. &T Foundation Special Purpose Grants in Science and Engineering, 1994–1995 H. Chen ; and Na-Ž . tional Center for Supercomputing Applications Ž . NCSA , High-performance Computing Resources Grants, 1994–1996 H. Chen .Ž .

## References

<sup>w</sup> <sup>x</sup> 1 T. Berners-Lee, R. Cailliau, A. Luotonen, H.F. Nielsen, A. Secret, The World-Wide Web, Commun. ACM 37 8 1994Ž . Ž . 76–82.

<sup>w</sup> <sup>x</sup> 2 C.M. Bowman, P.B. Danzig, U. Manber, F. Schwartz, Scalable internet resource discovery: research problems and approaches, Commun. ACM 37 8 1994 98–107.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 E. Carmel, S. Crawford, H. Chen, Browsing in hypertext: a cognitive study, IEEE Trans. Syst., Man Cybernetics 22 5Ž . Ž . 1992 865–884.

<sup>w</sup> <sup>x</sup> 4 H. Chen, Collaborative systems: solving the vocabulary problem, IEEE Computer, 27 5 58–66, Special Issue on Com-Ž . puter-Supported Cooperative Work CSCW , May 1994.Ž .

<sup>w</sup> <sup>x</sup> 5 H. Chen, A. Houston, J. Yen, J.F. Nunamaker, Toward intelligent meeting agents, IEEE Computer 29 8 1996Ž . Ž . 62–70.

<sup>w</sup> <sup>x</sup>6 H. Chen, B.R. Schatz, Semantic retrieval for the NCSA Mosaic, Proceedings of the Second International World-Wide Web Conference 1994, Chicago, IL, October 17–20, 1994.

<sup>w</sup> <sup>x</sup> 7 H. Chen, B.R. Schatz, T.D. Ng, J.P. Martinez, A.J. Kirchhoff, C. Lin, A parallel computing approach to creating engineering concept spaces for semantic retrieval: the Illinois Digital Library Initiative Project, IEEE Trans. Pattern Anal. Machine Intelligence 18 8 1996 771–782.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 F. Cheong, Internet Agents, New Riders Publishing, Indianapolis, IN, 1996.

<sup>w</sup> <sup>x</sup> 9 P. DeBra, R. Post, Information retrieval in the World-Wide Web: making client-based searching feasible, Proceedings of the First International World-Wide Web Conference 1994, Geneva, Switzerland, 1994.

<sup>w</sup> <sup>x</sup> 10 O. Etzioni, D. Weld, A softbot-based interface to the Internet, Commun. ACM 37 7 1994 72–79.Ž . Ž .

<sup>w</sup> <sup>x</sup> 11 G.W. Furnas, T.K. Landauer, L.M. Gomez, S.T. Dumais, The vocabulary problem in human–system communication, Commun. ACM 30 11 1987 964–971.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 D.E. Goldberg, Genetic Algorithms in Search, Optimization and Machine Learning, Addison-Wesley, Reading, MA, 1989.

<sup>w</sup> <sup>x</sup> 13 J.R. Koza, Genetic Programming: on the Programming of Computers by Means of Natural Selection, MIT Press, Cambridge, MA, 1992.

<sup>w</sup> <sup>x</sup> 14 P. Maes, Agents that reduce work and information overload, Commun. ACM 37 7 1994 30–40.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 Mauldin, Leavitt, Web-agent related research at the CMT, Proceedings of the ACM Special Interest Group on Networked Information Discovery and Retrieval SIGNIDR-94 ,Ž . August 1994.

<sup>w</sup> <sup>x</sup> 16 Z. Michalewicz, Genetic Algorithms<sup>q</sup>Data Structures<sup>s</sup> Evolution Programs, Springer-Verlag, Berlin, 1992.

<sup>w</sup> <sup>x</sup> 17 J. Pearl, Heuristics: Intelligent Search Strategies for Computer Problem Solving, Addison-Wesley Publishing, Reading, MA, 1984.

<sup>w</sup> <sup>x</sup> 18 E. Rasmussen. Clustering algorithms. In Information Retrieval: Data Structures and Algorithms, W.B. Frakes and R. Baeza-Yates, Editors, Prentice Hall, Englewood Cliffs, NJ, 1992.

<sup>w</sup> <sup>x</sup> 19 D. Rieken. Intelligent agents. Communications of the ACM, 37 7 :18–21, July 1994.Ž .

<sup>w</sup> <sup>x</sup> 20 B.R. Schatz, A. Bishop, W. Mischo, and J. Hardin. Digital library infrastructure for a university engineering community. In Proceedings of Digital Libraries ’94, pages 21–24, June 1994.

<sup>w</sup> <sup>x</sup> 21 B.R. Schatz and H. Chen. Building large-scale digital libraries. IEEE COMPUTER, 29 5 :22–27, May 1996.Ž .

<sup>w</sup> <sup>x</sup> 22 B.R. Schatz and J.B. Hardin. NSCA Mosaic and the World Wide Web: global hypermedia protocols for the internet. Science, 265:895–901, 12 August 1994.

<sup>w</sup> <sup>x</sup> 23 S. Spetka. The TkWWW robot: Beyond browsing. In Proceedings of the Second World Wide Web Conference, October 17–20 1994.

<sup>w</sup> <sup>x</sup> 24 M.M. Waldrop. Software agents prepare to sift the riches of cyberspace. Science, 265:882–883, 12 August 1994.

![](/api/attachments/GFWSAVC5/fulltext/images/b34c6bc51fa51b0a0f0dc61a9f1b54e9299d3cd97a26671f5651d74721326b09.jpg)

Hsinchun Chen is a Professor of Management Information Systems at the University of Arizona and head of the UA<sup>r</sup>MIS Artificial Intelligence Group. He is also a Visiting Senior Research Scientist at the National Center for Supercomputing Applications NCSA . HeŽ . received an NSF Research Initiation Award in 1992, the Hawaii International Conference on System Sciences HICSSŽ . Best Paper Award and an AT&T Foundation Award in Science and Engineer-

ing in 1994 and 1995. He received the PhD degree in Information Systems from New York University in 1989. Chen has published more than 30 articles covering semantic retrieval, search algorithms, knowledge discovery and collaborative computing. He is a PI of the Illinois Digital Library Initiative project, funded by NSF<sup>r</sup>ARPA<sup>r</sup>NASA, 1994–1998 and has received several grants from NSF, DARPA, NASA, NIH and NCSA. He is the guest editor of IEEE Computer special issue on ‘Building Large-Scale Digital Libraries’ and the Journal of the American Society for Information Science special issue on ‘Artificial Intelligence Techniques for Emerging Information Systems Applications.’ His recent work was featured at Science Computation Cracks ‘SemanticŽ Barriers’ Between Databases, June 7, 1996 , NCSA Access Maga-. zine, HPCWire and Business Week.

![](/api/attachments/GFWSAVC5/fulltext/images/604bee390f40594aa1db508dd53d6b979bca8594120d516bc40cb44b70ad22fa.jpg)

Yi-Ming Chung received her MS degree in Management Information Systems from the University of Arizona in 1996. Her thesis explored the use of genetic algorithms and neural networks for Internet search and vocabulary switching. She continues her research at the CA-NIS-Community Systems Laboratory, University of Illinois at Urbana-Champaign as a research programmer. Currently, she is working on automatic subject indexing, concept mapping and

![](/api/attachments/GFWSAVC5/fulltext/images/85e7caaf36b25ab2ea775a8e398c9db40dda5eb2b4c58913f0a5b42436668ec5.jpg)

Christopher C. Yang is an assistant professor in the Department of Computer Science and Information Systems at the University of Hong Kong. He was born in Hong Kong. He received his BS, MS and PhD in Electrical Engineering from the University of Arizona, Tucson, AZ, in 1990, 1992 and 1997, respectively. From 1995 to 1997, he was a research scientist in the UA<sup>r</sup>MIS Artificial Intelligence Group in the Department of Management Information Systems at the

vocabulary switching across community repositories in the Internet. Her research interests include digital libraries, neural networks, intelligent agents, object-oriented design and design patterns.

![](/api/attachments/GFWSAVC5/fulltext/images/5931b003b5c33eddb624b0062366e26fc63b9aa7e60885a96815f830c4a9297a.jpg)

Marshall Ramsey is a PhD student at the University of Arizona’s Department of Management Information Systems and a member of the UA<sup>r</sup>MIS Artificial Intelligence Group. He received his BS degree MIS in 1993 and MS degreeŽ . Ž . MIS in 1997 from the University of Arizona. He was awarded a Research Fellowship from the National Library of Medicine 1996 to 1997 for work inŽ . semantic retrieval for large collections of medical documents. His research in-

terests are cross-media and translingual semantic retrieval, data visualization and digital libraries.

University of Arizona. From 1992 to 1997, he was a research associate in the Intelligent Systems Laboratory in the Department of Electrical and Computer Engineering. His current research interests are digital library, Internet agent, visualization, color image processing, constraint network and computer integrated manufacturing and inspection. He was a member of program committee for the 1997 IEEE International Conference on Systems, Man and Cybernetics, a member of organizing committee for 1998 3rd Asian Conference on Computer Vision and a member of program committee for the 1998 1st Asian Digital Library Workshop.
