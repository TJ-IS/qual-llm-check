---
otero_id: 6986
otero_key: "U3V8GHMN"
title: "Post-retrieval search hit clustering to improve information retrieval effectiveness: Two digital forensics case studies"
authors: "Nicole Lang Beebe; Jan Guynes Clark; Glenn B. Dietrich; Myung S. Ko; Daijin Ko"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.01.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Post-retrieval search hit clustering to improve information retrieval effectiveness: Two digital forensics case studies

Nicole Lang Beebe <sup>a,</sup>⁎, Jan Guynes Clark <sup>a</sup>, Glenn B. Dietrich <sup>a</sup>, Myung S. Ko <sup>a</sup>, Daijin Ko

<sup>a</sup> Department of Information Systems and Technology Management, The University of Texas at San Antonio, TX, United State

<sup>b</sup> Department of Management Science and Statistics, The University of Texas at San Antonio (UTSA), TX, United States

## a r t i c l e i n f o

Available online 1 February 2011

Keywords: Digital forensics Clustering Information retrieval Self-organizing map Text string search

## a b s t r a c t

This research extends text mining and information retrieval research to the digital forensic text string search process. Speci<sup>fi</sup>cally, we used a self-organizing neural network (a Kohonen Self-Organizing Map) to conceptually cluster search hits retrieved during a real-world digital forensic investigation. We measured information retrieval effectiveness (e.g., precision, recall, and overhead) of the new approach and compared them against the current approach. The empirical results indicate that the clustering process signi<sup>fi</sup>cantly reduces information retrieval overhead of the digital forensic text string search process, which is currently a very burdensome endeavor.

© 2011 Elsevier B.V. All rights reserved

## 1. Introduction

Digital investigations seek to recover data from digital devices (e.g., personal computers, personal data assistants, telephones, digital cameras, networking devices, web servers, <sup>fi</sup>le servers, and email servers) to chronologically reconstruct events, con<sup>fi</sup>rm or refute allegations of wrong-doing, and/or obtain intelligence information. Digital forensics as a discipline encapsulates “…the preservation, collection, validation, identi<sup>fi</sup>cation, interpretation, documentation, and presentation of digital evidence derived from digital sources for the purpose of facilitation or furthering the reconstruction of events…” (page 16) [33].

Digital forensic searches are usually conducted at the physical level of the hard drive, and therefore include both logically allocated (saved) <sup>fi</sup>les and unallocated data (e.g., free disk space and deleted <sup>fi</sup>les). Text string searches are particularly worthwhile in digital forensics, because readable text and text-based documents are important artifacts in many investigations. Text string evidence may include an extremely high number of different data types, depending upon the contents of the drive, such as email, Internet communication (e.g., chats, instant messages, and blogs), word processing documents, spreadsheets, presentations, address books and contact lists, appointment and calendar data, web browsing history, and network/system activity logs. Thus, the typical digital forensic data set is extremely heterogeneous and unstructured. It also usually contains a very large amount of extraneous data not germane to the case. However, digital investigators must be able to review all evidence in order to determine their relevance, and noisy data sets frequently exceed the investigator's cognitive processing ability. More and more often, digital forensic investigators are simply unable to meticulously review all keyword search “hits,” <sup>fi</sup>les by <sup>fi</sup>le type, or all applicable system logs [36,48].

Although text string searches improve the ability to answer key investigative questions, current digital forensic search approaches exhibit poor information retrieval (IR) effectiveness [3]. IR effectiveness is a function of query precision, query recall, and IR overhead. Precision is the percentage of hits retrieved that are relevant to search objectives. Recall is the percentage of relevant hits that are retrieved in comparison to the total number of relevant hits in the data set. IR overhead is a combination of the computational time required to execute the search and the human analysis time spent reviewing irrelevant search hits. Precision is inversely related to IR overhead. More precise searches result in less IR overhead, due primarily to decreased human analysis time. However, it is usually dif<sup>fi</sup>cult to achieve high levels of precision and recall, due to the classic recallprecision trade-off problem.

The recall-precision trade-off problem is evident in the digital forensics context. Further, since achieving at or near 100% recall rates is an investigative and evidentiary concern, and is often a requirement in the digital forensics context [20], current digital forensic text string search approaches suffer from extremely low precision rates. The impact of poor precision is mitigated when the organization of the output enables the investigator to locate and attend to hits that are more relevant to the investigation before those that are literal string matches, but false positives relative to investigative goals. Search hit output ranking algorithms are the most common way this is accomplished in commonplace search and retrieval tasks, but advanced output organization mechanisms have yet to be developed for the digital forensics text string search problem.

Current industry standard digital forensics tools and search processes are incapable of handling large data sets (i.e. gigabytes and terabytes) in an ef<sup>fi</sup>cient manner [5,17,37,44]. As a result, important evidence can be overlooked [1]. However, little research exists on how to improve IR effectiveness, while conducting digital forensic text string searches [2]. Focus should be on decreasing human analysis time by shifting part of the analytical burden to the computer, thereby improving query precision and reducing the analytical impact of non-relevant search hits.

The purpose of this paper is to develop and test a new text string search process for digital forensic investigations by applying proven text mining and information retrieval (IR) approaches. Our goal is to decrease IR overhead by reducing investigator time spent reviewing non-relevant search hits, while ensuring all instances of search strings are located (100% recall rates).

## 2. Related research

IR effectiveness is greatest when both precision and recall are maximized (i.e., all relevant hits are retrieved, but no irrelevant hits are retrieved). However, in most instances, precision decreases as recall increases. In contexts where recall cannot be sacri<sup>fi</sup>ced, increased average precision is sought. Average precision is a score that considers the order in which relevant versus non-relevant hits are presented to the user. Unlike precision, the average precision is not degraded when non-relevant hits are returned, except when they are presented and viewed by the user before relevant hits. Approaches to increasing average precision include relevancy ranking algorithms, meta-searching, relevancy feedback systems, topical mapping, and visualization. These approaches fall into two basic categories — relevancy ranking and clustering techniques. The following is a brief discussion of each technique and related research.

## 2.1. Relevancy ranking

Rank-ordered lists are traditionally used to reduce the human analysis portion of IR overhead. Ranking algorithms vary, but most are based on Salton's vector space model [42] which measures the mathematical distance between queries and documents. However, vocabulary differences, short query length, and underspeci<sup>fi</sup>ed search goals tend to result in rank-ordered lists with a large number of mathematically similar search hits that are not relevant to the information seeking goals. As such, ranking algorithms have been augmented with other variables, such as query term order, proximity measures, metadata, and link/citation ranking.

Meta-searching is an alternative designed to improve average precision over traditional ranked lists. Meta-searching leverages ensemble ranking, and is most commonly applied to web-searching. Meta-search engines search multiple standard search engines, and a competitive voting algorithm ranks the search hit results based on the rank given to each hit by each engine. The primary goal is to leverage varied ranking algorithms. Theoretically, meta-searching produces improved rank-ordered lists, but this has yet to be empirically con<sup>fi</sup>rmed. Two studies [10,13] demonstrated improved precision using meta-searching, however, both included post-retrieval clustering of the search hits. Hence, we do not know the portion of precision improvement attributable to meta-searching versus search hit clustering.

Researchers have also sought to improve rank-ordered lists through the incorporation of user relevancy feedback mechanisms. Leuski and Allan [29] developed and empirically evaluated two user relevancy feedback models, one of which combined clustering and relevancy feedback. Both showed an improvement in IR effectiveness, with the combined clustering–relevancy feedback model showing a 36.7% increase in IR effectiveness. Roussinov and Chen [40] designed and empirically tested an adaptive search engine that combined traditional rank-ordering, information summarization, and relevancy. They too demonstrated improved IR effectiveness through the use of relevancy feedback.

Although technically feasible, relevancy ranking is not yet a practical method of increasing IR ef<sup>fi</sup>ciency in digital forensics. Given the nature of digital forensics data, many ranking variables are not applicable, or yield little bene<sup>fi</sup>t in the digital forensic text string search context. Meta-searching is also not yet a viable option, because there are very few digital forensic text string search engines, those that exist are expensive, and the computer processing time associated with each search is prohibitive. Finally, while relevancy feedback solutions are intriguing, research suggests hundreds of relevancy judgments are required to achieve suf<sup>fi</sup>cient predictive power in categorizing documents via relevancy feedback [52].

## 2.2. Clustering

The second major approach to increasing average precision, and thus IR effectiveness, is clustering. Prior to the 1990s, clustering algorithms were applied to textual IR as pre-retrieval mechanisms to: 1) reduce the search space (thereby improving query execution and ranking ef<sup>fi</sup>ciency) and 2) overcome vocabulary difference problems (thereby improving query recall) [51]. More recent research employs clustering to increase average precision. For example, clustering applied to textual IR better facilitates browsing [12,19], and it can automate concept space mapping [6].

Text clustering serves three unsupervised functions: 1) text categorization, 2) semantic relationship identi<sup>fi</sup>cation, and 3) visualization. The utility of text categorization rests on the cluster hypothesis [50], which suggests that conceptually similar documents will cluster together using standard similarity measures between document vectors and query vectors. The cluster hypothesis holds true in web environments [8,13,18,41,49,53] and non-web, textual environments [19,26–29,39].

Clustering algorithms can identify semantic relationships, thereby facilitating browsing. IR tasks are deemed ‘browsing’ when the search goal is loosely speci<sup>fi</sup>ed. The automated discovery of semantic relationships enables users to hone in on their search goals, as well as locate topically related documents that did not contain prespeci<sup>fi</sup>ed query terms. In this way, clustering helps overcome vocabulary difference problems. Semantic relationship discovery also aids in concept space mapping, which helps achieve measures of semantic similarity, rather than simple vector space similarity. By mapping concept spaces, similarity measures can include ‘context sensitive similarity discovery’ [41]. A fair amount of research has demonstrated the utility of this approach [6,9,18,34,41].

Clustering techniques also play a role in common visualization schemes (e.g., document maps — hierarchical, network, scatter, or geographical region). Visualization techniques are based on two basic arguments: 1) human decision making is aided by visual stimuli, and 2) humans can effectively process more simultaneous information visually than through the other senses [46]. If we can make better decisions via visual information processing, then visual output displays should improve IR effectiveness.

Clustering research has focused on web domain and user-level Internet browsing applications, as opposed to business intelligence, digital library, knowledge base, and digital forensics applications. Although evidence suggests that post-retrieval clustering improves average precision, independent of data type, the exact cause of improved average precision is unknown. It may be due to clustering as a topical mapping tool, or due to the visualization aspect of clustering, or due to a cumulative effect of both factors. Most of the studies to date have measured performance from search platforms that include a multi-dimensional visualization display. The few studies that measured performance via a one-dimensional list display either confounded their results by incorporating multiple performance enhancing search/ retrieval techniques [10,40], or did not measure average precision in the traditional sense [40,49]. Furthermore, all of these studies involved webbased data. Table 1 summarizes the empirical research on clustering textual data and their impact on average precision.

## 2.3. Conclusions drawn from related research

Given the nature of digital forensic data, we conclude that clustering has a higher probability of success than a relevancy ranking approach. This is based on the false positives, or investigatively irrelevant hits, produced by the digital forensic text string search process, as well as the inapplicability of most traditional relevancy ranking variables. Further, we conclude it is best to begin our research by applying clustering solely as an automated text categorization tool, without an information visualization component. This is motivated, in part, by the desire to purely measure the impact ‘clustering as a topical mapping tool’ on IR overhead, speci<sup>fi</sup>cally in a digital forensic text string search context.

## 3. New digital forensic text string search approach

The proposed process includes four major steps: 1) searching, 2) cluster pre-processing, 3) clustering, and 4) search hit analysis. The current process is comprised of steps One and Four. Step Four is modi<sup>fi</sup>ed in the proposed process, but we hypothesize that it is equally effective, more ef<sup>fi</sup>cient, and less analytically laborious than the status quo. Steps Two and Three are new additions to the process. Fig. 1 highlights the four-step process, and each step is discussed in the following sections

## 3.1. Searching step

The searching step remains the same in both the current and proposed processes. It encompasses a literal string search at the physical level of the media (i.e., a byte-for-byte search, independent of <sup>fi</sup>le system, operating system, or partitioning). The search retrieves all instances of the search string(s) on the media regardless of data type, allocation status, context, etc.

## 3.2. Cluster pre-processing step

The purpose of Cluster Pre-Processing is to create document vectors for those ‘documents’ (logically allocated <sup>fi</sup>les and unallocated logical blocks) that contain search hits from Step One. This entails four sub-steps: 1) determine the document set vocabulary, 2) reduce the vocabulary dimensionality, 3) calculate term frequencies, and 4) produce document vectors.

## 3.2.1. Document set vocabulary

The document set vocabulary contains the ‘words’ found in the document set. In the digital forensic context, the concept of a ‘word’ is different from the typical IR contexts. We de<sup>fi</sup>ne a ‘word’ as an alphanumeric string, with no maximum length, a minimum length of four bytes, and terminated by non-alphanumeric bytes. Although traditional text mining implementations often exclude numerical data from the vocabulary, content bearing information in computer data is much more likely to be in alphanumerical form than in other data sets. The four-byte “word” minimum is needed to ensure the “document” set vocabulary remains reasonably sized and that its constituent terms are useful classi<sup>fi</sup>ers. This tends to increase the ‘signal to noise ratio, and is a frequent search process speci<sup>fi</sup>cation in digital forensics.

## 3.2.2. Reduce vocabulary dimensionality

The next sub-step reduces computational complexity by reducing the vocabulary set to only those ‘words’ considered useful classi<sup>fi</sup>ers. Our process uses two very common dimension reduction mechanisms: stop word removal and stemming. Stop words are non-content bearing words and/or those words that do not tend to facilitate document differentiation (e.g., with, that, this and about). Stemming reduces the vocabulary to the smallest canonical set by replacing words with their in<sup>fi</sup>nitive (e.g., replace delivers, delivering, and delivered with a single instance of deliver).

## 3.2.3. Calculate term frequencies

The next sub-step calculates the number of ‘documents’ in which each ‘word’ resides. Prior IR research shows that the most frequently occurring terms in a document set (after the application of standard dimension reduction techniques) are the best differentiators with respect to document content [45].

## 3.2.4. Produce document vectors

The <sup>fi</sup>nal pre-processing step produces document vectors for each of the “documents” containing search hits. The dimensions of the document vectors equate to the most frequently occurring terms in the reduced dimension document set vocabulary, with dimension value being a function of the rate of occurrence.

## 3.3. Clustering step

The clustering step uses a clustering algorithm to calculate the mathematical similarity of the document vectors, and thereby derive conceptual document clusters. The output of the clustering component consists of thematically clustered documents, along with documentcluster similarity measures that can be used to priority-rank documents within each cluster. If the cluster represents some speci<sup>fi</sup>c latent thematic

## Table 1

Empirical Clustering Studies — Impact on Average Precision.

<table><tr><td>Data type</td><td>Reference</td><td>Clustering algorithm</td><td>Output type</td><td>Improvement in average precision</td></tr><tr><td rowspan="4">Text</td><td>Leuski [27]</td><td>Hierarchical (multiple)</td><td>Visualization (hierarchical map)</td><td>Approximately 12%</td></tr><tr><td>Leuski and Allan [29]</td><td>Hierarchical (multiple)</td><td>Visualization (hierarchical map)</td><td>13.61%</td></tr><tr><td>Georgakis et al. [16]</td><td>Bootstrapped SOMs (Kohonen)</td><td>Not applicable (simulation)</td><td>Improved precision-recall curves</td></tr><tr><td>Schuff et al. [43]</td><td>Hierarchical (Ward&#x27;s)</td><td>Visualization (hierarchical map)</td><td>Not measured; no change in perceived effort by users</td></tr><tr><td rowspan="9">Web</td><td>Zamir and Etzioni [53]</td><td>Partitional (STC)</td><td>Visualization (network map)</td><td>Approximately 30%</td></tr><tr><td>Chen et al. [8]</td><td>SOM (Kohonen)</td><td>Visualization (geograph. map)</td><td>No significant improvement in precision; Thesaurus use improved recall without degrading precision</td></tr><tr><td>Zamir and Etzioni [54]</td><td>Partitional (STC)</td><td>Clustered list</td><td>Not measured; users viewed fewer docs, however</td></tr><tr><td>Chen et al. [6]</td><td>SOM (Kohonen)</td><td>Clustered list</td><td>Approximately 25% improvement over Northern Light)</td></tr><tr><td>Roussinov and Chen [40]</td><td>SOM (Kohonen)</td><td>Clustered list</td><td>Not measured; decreased search time and fewer docs viewed</td></tr><tr><td>Chung et al. [11]</td><td>Recursive partitions (Genetic Algorithm)</td><td>Visualization (hierarchical map)</td><td>Approximately 8%</td></tr><tr><td>Chung et al. [11]</td><td>Recursive partitions (Torgerson&#x27;s MDS)</td><td>Visualization (scatter map)</td><td>Approx 18% degradation</td></tr><tr><td>Turetken and Sharda [49]</td><td>Hierarchical (Ward&#x27;s)</td><td>Clustered list (zoomable)</td><td>Not measured; approximately 12–17% improvement in retrieval speed</td></tr><tr><td>Ferragina and Gulli [13]</td><td>Hierarchical (SnakeT)</td><td>Visualization (hierarchical map)</td><td>Not measured; subjects preferred it over rank-ordered lists</td></tr></table>

[11,16,43].

![](/api/attachments/U3V8GHMN/fulltext/images/69cdbc4c231dbe5de99b2a9fe703ae87ac50f1590741cef3c866ce42de9c32c8.jpg)  
Fig. 1. Proposed digital forensic text string search process.

that differs from that of other clusters, then the document listed last in the cluster, having the lowest priority-ranking, is the most dissimilar document in the cluster's thematic. For example, a murder investigation may yield two clusters associated with the word “kill.” One cluster will likely contain documents related to computer processing data (e.g., “system kill” and “process kill”), while the other contains documents related to human dialog about murder (e.g., “I want to kill her”). As you move further down the prioritized hits within a ‘kill’ cluster, the hits will become less similar to the cluster's main thematic and potentially closer to another cluster's main thematic (e.g., “help kill”).

## 3.4. Search hit analysis

The search hit analysis step exists in both the current and proposed processes. However, in the proposed process, the search hits are grouped by thematic cluster. The investigator selects a cluster and examines the search hits within that cluster in the order in which they are presented. When the investigator expects a low probability of encountering more relevant hits within the cluster, the investigator selects another cluster to review. In this manner, the investigator can quickly review and evaluate clusters for similarity to the investigative objectives and by-pass large groups of search hits that are precise matches for the query, but that are unlikely to possess evidentiary utility.

## 4. Experimental methodology

## 4.1. Overview of experimental procedure

We instantiated our new text string search process into a working search engine prototype, named dfGrouper, and compared results against two commercial digital forensic search engines: EnCase™ and FTK™. EnCase™ used a string matching/scanning algorithm (e.g. Boyer–Moyer, Rabin–Karp, Knuth–Morris–Pratt, Aho–Corasick, or Shift-Or) to locate all instances of the query terms (or strings) by searching the digital media byte by byte at the physical level. The query results (“hits”) are presented to the investigator grouped by query term and ordered within groups according to physical location on the evidence. Conversely, FTK™ used a physical level, full-text indexing approach and subsequent Boolean search and retrieval strategy. The query results are presented to the investigator grouped by Boolean query, sub-grouped according to <sup>fi</sup>le item (logical <sup>fi</sup>le and compound <sup>fi</sup>le item) or data type (free space, <sup>fi</sup>le slack, etc.), and then ordered within groups according to physical location on the evidence.

We studied two cases: 1) a real-world investigation and associated data set, and 2) a mock investigation and experimental data set. Within each case, we held the queries, datasets, and test platforms constant and varied search tool and results display. Experienced digital forensic investigators created the queries and analyzed the output, looking for evidence relevant to the investigation. We compared dfGrouper output against EnCase™ and FTK™ output, measuring the IR effectiveness of each tool.

## 4.2. Data set and query development

Since a publicly available, standard test data set suitable for this evaluation did not exist, we used a non-publicly available test data set. To maximize generalizability and reliability of <sup>fi</sup>ndings, we used real-world evidence for the first of two cases. The case was a civil suit (a divorce case<sup>1</sup>), described brie<sup>fl</sup>y as follows. “Petitioner” requested a divorce, at least in part, on the grounds of marital misconduct of “Spouse.” The misconduct was extra-marital in nature. Petitioner requested a digital forensic examination of their family computer to uncover evidence of extramarital behavior on the part of Spouse. The evidence itself was a physical level, digital forensic image of a 40 gigabyte (GB) hard drive. The search involved a 17-term query (prioritized string search list — see Appendix A).

Since we did not have access to another real-world case, we used a mock case created by students enrolled in a graduate digital forensics class at a large Southwestern university for the second case. The mock case involved the murder of a man (“Tom Smith”) by poison, orchestrated by his wife (“Suzy”), but made to look like natural causes, so that she could obtain his life insurance upon his death. The wife was having an affair (with “Justin”). The search involved a 19- term query (see Appendix A) of a 10 GB hard drive.<sup>2</sup>

## 4.3. Test platforms

We measured elapsed time associated with each portion of the new search approach, to ensure the decrease in human analysis time exceeded (in absolute terms) the increase in computer processing time, and thereby decreased net IR overhead. Since we measured the elapsed computer processing time, the test platform speci<sup>fi</sup>cations are relevant to keep experimental elapsed time in perspective. We executed the searching, cluster pre-processing, and clustering components on a relatively old (vintage 2004), user-class PC.<sup>3</sup> We used other comparable or slightly better user-class platforms for other aspects of the experiment, including non-timed activities and the user interface.<sup>4</sup> Although the user interface component did involve a time measurement – human analysis time – it was a real-time measure versus a computational processing measure, and is therefore independent of platform. We observed no interface latency that might bias this measurement.

## 4.4. User interface and task

We designed and developed a user interface to facilitate user task performance (analysis of digital forensic text string search hits), as well as to record key experimental measures. Fig. 2 shows a screen shot of the interface, which is described as follows. The “Cluster” drop-down box lists clusters available for analysis. They are identi<sup>fi</sup>ed by number, which bears no theoretical meaning. Documents associated with the selected cluster are listed under “Cluster Details” in rank order according to similarity to the cluster's node vector (representative of the cluster's thematic). Search hits constituent to the selected document are located in the “Document Details” window. Users record their relevancy determination for each search hit via a checkbox to the left of each search hit's context. Relevancy determinations and their corresponding date/ time stamps are then recorded in the interface's underlying database.

![](/api/attachments/U3V8GHMN/fulltext/images/d2cb27d085e7813eb9fbf4bbc1e6bf99532ce432c1decf9543dd0ae0b5eb65b7.jpg)  
Fig. 2. User interface screen shot.

## 4.5. Process instantiation — search engine architecture

Following the four major steps in Fig. 1, we instantiated the process. The following is discussion of the design and implementation of each system component.

## 4.5.1. Searching component

For the searching component, we used two open source digital forensic tools: The Sleuth Kit (http://www.sleuthkit.org) and Autopsy (http://www.sleuthkit.org/autopsy). In order to maintain consistency in the search component across all tools, the system did not accept extended search options, such as phonetic similarity, synonyms, and common spelling variations. Resultant search hit data included the hit, its surrounding context (60 bytes preceding and succeeding the hit text), and the <sup>fi</sup>le item's metadata (location information, allocation status, and <sup>fi</sup>le/path names if allocated). This basic approach is the standard hit display format in digital forensics tools. It is conceptually similar to ‘snippets’ in the web-browsing domain, where the hit is highlighted and surrounded by the actual content of the web page.

## 4.5.2. Cluster pre-processing

We used strings, a built-in Linux binary, to extract ASCII strings from the document set and create a document set vocabulary. We then used a series of programs written in C to remove ‘words’ that did not conform to our de<sup>fi</sup>nition of a ‘word,’ created the reduceddimension vocabulary, calculated term frequencies, and created the document vectors. We used Bow's (AKA libbow) stop word list and Porter's stemming algorithm [35] to reduce vocabulary dimensionality. We then created and used 75-dimension, binary document vectors<sup>5</sup> for each of the documents containing search hits. Binary document vectors are frequently used in Self Organizing Map (SOM) text classi<sup>fi</sup>cation and clustering processes [30–32,38]. This is because binary vectors enable sparse vector manipulation during the map learning and documenting process. Thus, they are much more computationally ef<sup>fi</sup>cient than the weighted vectors.<sup>6</sup>

## 4.5.3. Clustering component

We used Roussinov and Chen's Scalable Self-Organizing Map (SSOM) algorithm [38], based on the Kohonen SOM algorithm [21], to cluster post-retrieval search hits. Extensive research shows that a variety of clustering algorithms can effectively cluster both text and web document bases. Consistently superior performers include group average and Ward's hierarchical algorithms [27], the Stemming Tree Clustering (STC) partitional algorithm [54], and Kohonen SOMs [7,14,15,23,32,34,39]. Partitional clustering algorithms typically yield lower cluster quality than hierarchical clustering and Kohonen SOM algorithms. Stemming Tree Clustering (STC) algorithm is one notable exception. However, a phrase-based algorithm like STC presents a problem for the physical level digital forensics text string search context. Hierarchical algorithms consistently outperform partitional algorithms relative to cluster quality. However, they present scalability issues, as they typically scale quadratically $O ( n ^ { 2 } )$ to the number of inputs. Some research speci<sup>fi</sup>cally addresses the scalability concern [15], but we still feel scalability is a concern, and thus selected Kohonen SOMs as our clustering algorithm. Extensive research has demonstrated the superior scalability of Kohonen SOMs [15,22,24], particularly Roussinov and Chen's [38] SSOM algorithm, due to its use of binary document vectors.

In the experiment, we initialized the SSOM node vectors using a standard C++ pseudo-random number generator function. We applied a seed number to ensure reproducibility of the results. We set the learning rate to 0.05 in the training phase and 0.01 in the tuning phase. We set the neighborhood radius to seven (7) during the training phase, and three (3) during the tuning phase. We initially set the SSOM map size to $7 \times 7 ,$ but found that a larger map (20×10) was needed to effectively cluster the search hit results in the mock murder case. Our parameter selection prioritized cluster quality over operational ef<sup>fi</sup>ciency and risked map convergence. However, the parameters performed ef<sup>fi</sup>ciently, the maps converged, and we obtained quality maps. We used Euclidean distance as the similarity measure.

## 4.5.4. Search hit analysis component

To facilitate the search analysis step, we designed and developed a prototype user interface using Microsoft Access 2003™, (described previously in Section 4.4). The interface design included experimentation functionality that would not be necessary in production systems. For example, users would not input a relevancy determination in a production system, unless, of course, relevancy feedback mechanisms are integrated into the process. Unlike traditional tools, including EnCase™ and FTK™, dfGrouper presents search hits in thematic cluster format. Cluster detail is presented in rank order of similarity to the node vector of that given cluster. This rank ordering of search terms enables the investigator to review and evaluate clusters for similarity to the investigative objectives and by-pass large groups of search hits that have a low probability of possessing evidentiary utility.

## 4.6. Variables and measures

For the purpose of this research, the primary dependent variable of interest is IR effectiveness. IR effectiveness is impacted by a change in computer processing time from the clustering and pre-processing steps, and by a change in human search hit analysis time. The human search hit analysis time is a function of average precision, another important variable in this analysis. To assign values to these variables, several measures are important, including: 1) computer processing time of the clustering pre-processing step, 2) computer processing time of the clustering step, 3) search hit relevancy, 4) per-hit human analysis time, 5) cluster navigation order, 6) precision, and 7) recall. Each is described in the sections that follow.

## 4.6.1. Computer processing time

Since report query generation and search execution time were presumed the same across all tools, we did not measure it. Instead, we were interested in the incremental addition to computer processing time due to the clustering process. We incorporated real-time clocks into the pre-processing and clustering components to measure and report elapsed time for dfGrouper.

## 4.6.2. Human search hit analysis time

Three measures are important here — search hit relevancy, per-hit human analysis time, and cluster navigation order. For dfGrouper, we recorded binary user relevancy determinations via the user interface. We measured and recorded per-hit human analysis time automatically via the user interface as well, by recording date/time stamps of relevancy determinations. We calculated a per-hit average, accounting for investigator breaks. We measured the cluster navigation order via the date/time stamps associated with relevancy determinations. The review chronology equates to the cluster navigation order.

To produce comparable measures for EnCase™ and FTK™, we mapped and transferred relevancy determinations from dfGrouper to equivalent hits produced by the other tools. The same user evaluated the relevancy of any search hits produced by the commercial tools that were not recalled by dfGrouper. We also held per-hit search hit analysis time constant across all tools. As such, the value measured via dfGrouper was transferred to the commercial simulations and IR effectiveness evaluations.

We presumed the search hit review order for EnCase™ and FTK™ to minimize experimental error. Fatigue and learning affects preclude the use of a single evaluator across tools. Having multiple evaluators, on the other hand, introduces error due to expected variability in subjective relevancy determinations. We presumed an investigator would review all hits associated with the highest priority search term <sup>fi</sup>rst, in the order presented by the tool, and then move on to the next highest priority search term, and so on. Experience suggests that many users of the two industry standard search engines review search hits in this manner.

## 4.6.3. Average precision

Given the search hit review order and per-hit relevancy, average precision can be calculated. Average precision is a score that considers the manner (i.e. order) in which relevant versus non-relevant hits are presented to the user. A score of 1.0 is ideal and means the search engine retrieved all relevant documents and ranked them perfectly (i.e., all non-relevant documents are ranked lower than relevant documents, and thus not reviewed until all relevant documents are reviewed).

$$
\text { Average   Precision } (A v g P) = \frac {\sum_ {r = 1} ^ {N} P (r) \times r e l (r)}{R}\tag{1}
$$

where

$$
\begin{array}{l l} \text {r} & \text {rank} \\ \text {N} & \text {number hits retrieved} \\ \text {rel} (r) & 0 \text {or 1 (relevancy of hit)} \\ \text {P} (r) & \text {total precision up to this point} \\ \text {R} & \text {total number of relevant hits.} \end{array}
$$

The average precision score clearly depends on precision at cut-off points [19]. We selected 10% incremental cut-off points. As previously discussed, precision is the ratio of relevant hits to the number of hits retrieved. The equation is shown below.

$$
\text { Precision } = \frac {\text { Number   of   Relevant   Hits   Retrieved }}{\text { Total   Number   of   Hits   Retrieved }}\tag{2}
$$

4.6.4. Recall

Query recall is traditionally de<sup>fi</sup>ned as the ratio of relevant hits retrieved to the total number of relevant hits in the data set. In the current context, the true total number of relevant hits in the data set is not known, because of the subjective nature of relevance, the use of real-world data, and slight variation in search algorithms between the tools.<sup>7</sup> As such, the denominator in the current research is de<sup>fi</sup>ned as the total number relevant hits found by the respective tool. Thus, 100% recall was eventually achieved by all three tools. The equation is shown below.

$$
\text { Recall } = \frac {\text { Number   of   Relevant   Hits   Reviewed }}{\text { Total   Number   of   Relevant   Hits   Retrieved   by   Tool }}\tag{3}
$$

Table 2  
Precision (real-world case).

<table><tr><td>Cut-off point</td><td>EnCaseTM</td><td>FTKTM</td><td>dfGrouper</td></tr><tr><td>10%</td><td>36.10%</td><td>38.00%</td><td>79.70%</td></tr><tr><td>20%</td><td>18.80%</td><td>19.10%</td><td>84.00%</td></tr><tr><td>30%</td><td>22.00%</td><td>23.50%</td><td>84.40%</td></tr><tr><td>40%</td><td>17.40%</td><td>18.60%</td><td>77.60%</td></tr><tr><td>50%</td><td>22.90%</td><td>33.40%</td><td>71.70%</td></tr><tr><td>60%</td><td>35.70%</td><td>44.50%</td><td>76.40%</td></tr><tr><td>70%</td><td>44.80%</td><td>52.40%</td><td>79.70%</td></tr><tr><td>80%</td><td>51.70%</td><td>58.30%</td><td>77.60%</td></tr><tr><td>90%</td><td>57.00%</td><td>63.00%</td><td>77.80%</td></tr><tr><td>100%</td><td>61.30%</td><td>66.70%</td><td>70.90%</td></tr></table>

## 5. Empirical evaluation

In this section, we present the empirical results pertaining to the real-world case study. Following that, we discuss the implications of these <sup>fi</sup>ndings on the digital forensic text string search process. Results and implications pertaining to the simulated mock case are then presented.

## 5.1. Experimental results

We searched the real-world evidence drive for all instances of the search strings. The following is the discussion of IR effectiveness measures and overall conclusions drawn from the case study.

## 5.1.1. Recall and precision

The 17 query terms used in the <sup>fi</sup>nal search produced an average of 24,852 search hits (25,587 hits retrieved by EnCase™; 24,438 hits retrieved by FTK™; and 24,262 hits retrieved by dfGrouper). Table 2 and Fig. 3 summarize the precision rates for each tool, whereas Table 3 and Fig. 4 summarize recall rates for each tool. As shown, the thematically clustered list produced by dfGrouper resulted in signi<sup>fi</sup>cantly higher precision and recall rates at all cut-off points, relative to both EnCase™ and FTK™.

## 5.1.2. Average precision

Table 4 shows the calculated average precision (AvgP) scores for all tools. As shown, dfGrouper signi<sup>fi</sup>cantly out-performed both EnCase™ and FTK™ (a score of 1.0 is ideal). dfGrouper clustering resulted in an approximate 41% improvement in average precision over current approaches.

## 5.1.3. Time

Last, we evaluated the impact on the search query execution time due to the cluster pre-processing and clustering components of dfGrouper. The elapsed time of the cluster pre-processing component was 18.1 minutes, while the clustering component took a mere 8 seconds. Thus, the total increase in computer search execution time to facilitate clustered search hit output was less than 20 minutes,<sup>8</sup> and as previously stated, this was achieved on relatively old, slow, user-class computing platforms.

Investigative Precision  
![](/api/attachments/U3V8GHMN/fulltext/images/26149bddfd8541cf2aa27fb7b48a898811ca71d76a7e1f5e8a337d84db4b1759.jpg)  
Fig. 3. Precision rate curve (real-world case).

## 5.2. Discussion

In this section, we discuss the implications of the empirical <sup>fi</sup>ndings as they relate to IR effectiveness and IR overhead. We then discuss a post-hoc analysis we conducted to better understand and frame the practical implications of our research. Last, we discuss and explain some unexpected <sup>fi</sup>ndings pertaining to the two commercial forensics tools we evaluated dfGrouper against.

## 5.2.1. IR overhead reduction — human analytical time

As shown, precision and recall rates of dfGrouper were better than either EnCase™ or FTK™. The curves associated with the precision and recall rates of dfGrouper show marked improvement over current tools and perform as expected, for the most part. The precision curve is a generally decreasing function, although there was a noticeable dip in precision at the 50% cut-off point. We suspect this is likely due to the cluster quality of the cluster(s) being reviewed at and around the 50% cut-off point. However, this is a conjecture that must be examined with further analysis. We did observe a small, but expected deviation in precision between tools at the 100% cut-off point. This is because the three tools did not return the same set of search hits. Since each tool used a different searching component, small variations in absolute precision were anticipated and observed. This difference does not affect IR overhead measures, however, which is the focus of this study.

We expected the query recall rate function to generally resemble a power function — increasing quickly at the beginning and asymptotically approaching the maximum absolute query recall rate as the number of hits reviewed approached the total hits retrieved. Although the recall curve was not as concave as we anticipated (it did not increase as quickly at the beginning as we expected), it was better than a random distribution of relevant search hits throughout the output, and it signi<sup>fi</sup>cantly outperformed EnCase™ and FTK™.

Table 3  
Recall (real-world case).

<table><tr><td>Cut-off point</td><td>EnCaseTM</td><td>FTKTM</td><td>dfGrouper</td></tr><tr><td>10%</td><td>5.90%</td><td>5.70%</td><td>11.20%</td></tr><tr><td>20%</td><td>6.10%</td><td>5.70%</td><td>23.70%</td></tr><tr><td>30%</td><td>10.80%</td><td>10.60%</td><td>35.70%</td></tr><tr><td>40%</td><td>11.30%</td><td>11.20%</td><td>43.80%</td></tr><tr><td>50%</td><td>18.60%</td><td>25.10%</td><td>50.60%</td></tr><tr><td>60%</td><td>34.90%</td><td>40.00%</td><td>64.70%</td></tr><tr><td>70%</td><td>51.10%</td><td>55.00%</td><td>78.80%</td></tr><tr><td>80%</td><td>67.40%</td><td>70.00%</td><td>87.60%</td></tr><tr><td>90%</td><td>83.70%</td><td>85.00%</td><td>98.80%</td></tr><tr><td>100%</td><td>100.00%</td><td>100.00%</td><td>100.00%</td></tr></table>

![](/api/attachments/U3V8GHMN/fulltext/images/0626b7c7cf647f04d973f6720cceffe4609c648085860b3864343d4a44c8946a.jpg)  
Fig. 4. Recall rate curve (real-world case).

One of our primary research objectives was to empirically determine whether Kohonen SOMs could effectively cluster digital forensic text string search hits, in a manner that reduced IR overhead for investigators. The improved precision and recall curves suggest this is indeed possible. The calculation of average precision scores provides even clearer evidence that Kohonen SOMs can be used to reduce IR overhead for investigators, since average precision scores nearly doubled.

The marked improvement in average precision for dfGrouper over EnCase™ and FTK™ is also notable. Both commercial tools cluster their output according to query term and/or <sup>fi</sup>le time or data type, whereas our approach clusters the output based on thematic content. Further, since our presumed search hit review order for EnCase™ and FTK™ took query term priority into consideration, the marked improvement in our approach is even more notable, because we observed that post-retrieval search hit clustering based on thematic content signi<sup>fi</sup>cantly outperformed a clustering–ranked list hybrid approach.

## 5.2.2. Satisficing analysis

Another important consideration is that, although we designed the proposed process and system to achieve 100% recall from a legal perspective, the overall goal of clustering the output was to help investigators locate relevant evidence more quickly and obviate the need to review all search hits retrieved. This is important, since many real-world investigations are time constrained — the investigator may only be permitted to spend a <sup>fi</sup>nite and potentially suboptimal amount of time on the investigation. Thus, it is imperative that their search system maximizes average precision. Time is limited, so the investigator must locate the more relevant search results as soon as possible.

Even when such <sup>fi</sup>rm time constraints do not exist, investigators often discontinue their search after they <sup>fi</sup>nd “enough” evidence to support decision making. They need to <sup>fi</sup>nd digital artifacts that support legal elements of proof, satisfy the applicable burden of proof, and/or provide enough information to inform a business decision, depending on the context. Considering resource constraints, fatigue effects, and the rate of duplicity that often occurs with digital forensic artifacts, investigators often discontinue their search after “enough” evidence is located in support of investigative objectives. This approach is a natural decision making process, according to Herbert Simon's notion of satisficing [47]. Time constraints and information overload issues cause people to make decisions that are good enough to meet requirements, rather than optimizing decisions, particularly in the face of complexity. Experience suggests that although legal requirements frequently necessitate 100% recall, investigators and prosecutors often follow the natural decision making process described by Simon.

Table 4  
Average precision scores (real-world case).

<table><tr><td>Tool</td><td>AvgP Score</td></tr><tr><td>EnCaseTM</td><td>0.432</td></tr><tr><td>FTKTM</td><td>0.483</td></tr><tr><td>dfGrouper</td><td>0.781</td></tr></table>

Accordingly, we conducted a post-hoc satis<sup>fi</sup>cing analysis on the data for all three tools. We de<sup>fi</sup>ne the satis<sup>fi</sup>cing point as the point in the human analysis process when all critical digital artifacts are encountered. For the purpose of this study, the satis<sup>fi</sup>cing point is based on: 1) the digital artifacts which are critical to the case and 2) the search hits that correspond to those artifacts. We asked a highly experienced digital forensic examiner to review the relevant search hits produced by the clustering process, presented in the order reviewed (i.e. cluster navigation order), and identify the satis<sup>fi</sup>cing point. We then derived the key digital artifacts, based on previously determined relevancy evaluations. We identi<sup>fi</sup>ed ninety-<sup>fi</sup>ve (95) speci<sup>fi</sup>c search hits directly attributable to six key digital artifacts. Example artifacts include: user interaction with websites pertaining to extramarital activity and text fragments of activity (i.e. communications) related to extramarital affairs.

For the new process using dfGrouper, the satis<sup>fi</sup>cing point is equivalent to the literal point in the cluster navigation-ordered search hit output where the research volunteer indicated he would stop the analysis. For EnCase™ and FTK™, we de<sup>fi</sup>ned the satis<sup>fi</sup>cing point as the cut-off point in the ordered search hit ouput at which all 95 search hits referenced above were encountered. The results are:

• dfGrouper satis<sup>fi</sup>cing point: 21.99% (all 95 critical search hits found after reviewing 5335 hits out of 24,262 total search hits)

• EnCase™ satis<sup>fi</sup>cing point: 99.15% (all 95 critical search hits found after reviewing 25,370 hits out of 25,587 total search hits)

• FTK™ satis<sup>fi</sup>cing point: 99.08% (all 95 critical search hits found after reviewing 24,213 hits out of 24,262 total search hits)

Next, we considered satis<sup>fi</sup>cing as a function of human analysis time savings. We measured the mean time to view and consider each hit to be 0.909 s. In other words, it took just less than one second to review a single search hit, which appears reasonable. If the investigator can conclude the analysis after reviewing only 21.99% of the clustered 24,262 hits returned, then 80 minutes would be spent on analysis. In contrast, the satis<sup>fi</sup>cing point is not achieved with EnCase™ until after 384 minutes (6.41 h) of analysis, or 367 minutes (6.11 h) of analysis using FTK™. As shown, dfGrouper permits a more ef<sup>fi</sup>cient analysis, netting a near 80% decrease in IR overhead relative to human analysis time spent reviewing search output. This is a result of the improved average precision of the new process.

The satis<sup>fi</sup>cing analysis helps put the average precision score into a practical frame of reference. In this scenario, the investigator does indeed conclude the analysis before all relevant search hits are located and reviewed. However, the remaining search hits are believed to be duplicative, or more circumstantial in nature than the critical relevant search hits encountered prior to the satis<sup>fi</sup>cing point. Furthermore, the search engine still retrieves the full set of search hits, in case further analytical effort is required or desired. This type of time savings is critical to digital forensic text string searches when the output often numbers in the hundreds of thousands, if not millions.

Reviewing a million search hits would take over 250 labor hours. Not only is this simply unrealistic, it impedes timely decision making.

Note, satis<sup>fi</sup>cing is a relative variable. Different investigators may have different levels of satis<sup>fi</sup>cing. Different cases and different queries will net different satis<sup>fi</sup>cing levels, as well. However, when holding case, query, and investigator constant, the satis<sup>fi</sup>cing point will vary across search/analysis approaches and tools. Although the values will likely differ, this research empirically shows the satis<sup>fi</sup>cing point can be signi<sup>fi</sup>cantly reduced when digital forensic text string search output is thematically clustered.

## 5.2.3. Computer information processing time

An increase in computer processing time can negatively impact IR overhead. The key is to achieve net positive changes in overall IR overhead when considering the combined effects of increased computer processing time and decreased human analysis time. We expected the savings in human analysis time would eclipse the additional computational expense associated with the clustering process, but we were not certain to what extent this would hold true. As it turns out, the clustering process was extremely fast — taking only eight seconds in this case. Further, it took only 18 minutes to prepare the data for clustering. While both processes will certainly take longer with larger data sets, the proposed approach's scalability potential is evident. In this particular experiment, the additional 18.13 minutes is more than made up for by a savings of approximately <sup>fi</sup>ve hours of human analysis time. Furthermore, from a business and organizational resource perspective, computer processing time and human analytical time do not hold equal value. It is often more cost effective to have computers run longer, than expend labor hours associated with highly skilled and highly paid digital forensic investigators.

## 5.2.4. Unexpectedly poor performance of industry tools

We made two unexpected observations regarding EnCase™ and FTK™ precision and recall. Because the presumed search hit review order for these tools was a function of search term priority, we expected to see generally decreasing precision curves for EnCase™ and FTK™. While we expected dfGrouper to outperform EnCase™ and FTK™, we expected both EnCase™ and FTK™ to outperform a random distribution of relevant search hits. What we saw, however, was generally increasing precision curves for EnCase™M and FTK™. Arguably, randomly distributed search hits would have outperformed the search list that grouped hits by query term and then by <sup>fi</sup>le item, with the analyst reviewing hit groups in order of search term priority.

Examining the case more closely, we believe these unexpected observations are due to the speci<sup>fi</sup>c search strings selected and the order in which they were prioritized. In short, the investigator who generated and prioritized the query did so purely with investigative objectives in mind. He did not consider the “noise” potential associated with various search strings. In this case, the higher priority search strings were actually “noisier” than the others. This is a function of these search strings being frequently used in human dialog and/or during the course of system (i.e. non-user) activity.

In this case, the highest priority search string (“affair”) accounts for approximately 7% of the total search hits and is a word that is relatively common in human discourse. Thus, it is a low precision search string, generally speaking. The query precision rates are also highly impacted by the second and <sup>fi</sup>fth highest priority search strings. These search strings (“separated” and “nude”) account for approximately 30% of the total search hits. They are particularly problematic with respect to query precision rates, because they result in a high number of hits related to non-user, system activity<sup>9</sup> that is not relevant to the investigation. A few examples of such system related, non-relevant search hits are as follows:

“…LanguageList of decimal language Ids, comma-separated if more than one.Sequence with respect…”

“…arguments for starting services. The arguments are separated by null characters (\~). For example…”

“…0000121;SC2,\*.SC210333\TsvDosTab Separated Values (DOS);DTVZ;Desk;DelD;TSVD…”

“…s\_prop13=PE\_MA;//Mopar accessories – should be a comma separated list…”

“…-Xbootclasspath:bdirectories and zip/jar files separated by;N…”

“…?AVCMDIMenuDecorateion@@...”

“…/”begin\_bbMenuDefs”/…”

“…?GetMenuDelay@XPNButton@@QAEKXZ…”

CLSID\_MenuDeskBar= {ECD4FC4F-521C-11D0-B792

“…GetMenuDefaultItem…”

In short, the extremely experienced investigator in this case prioritized the generally “noisier” search strings higher than the less noisy, more case speci<sup>fi</sup>c search strings. This does not mean the investigator generated a poorly prioritized query; it simply re<sup>fl</sup>ects his belief that relevant hits with “affair,” “separated,” and/or “nude” would yield better evidence of extramarital activity than the lower priority search strings (email addresses and websites, generally speaking). As a result, the prioritization order re<sup>fl</sup>ects the investigator's willingness to wade through more non-relevant search hits to locate more salient evidence. This philosophical viewpoint is common in digital forensic investigations. However, the overwhelming number of search hits and time constraints can preclude this in practice. In real-world cases, investigators often omit high-value, but noisy search terms for investigative expediency (e.g., “kill” in a murder case).

This case and analytical scenario further exemplify the need for clustered search hit output. Clustering the “nude” search hits, for example, can separate the hits related to Windows™ menus from those hits pertaining to human nudity. The investigators can quickly disregard the “menu” cluster and focus their attention on the “nudity” cluster. At this juncture, the reader might be thinking a simple “NOT” Boolean expression would suf<sup>fi</sup>ce to exclude the unwanted hits. Although true in theory, it is very dif<sup>fi</sup>cult for the average investigator to exhaustively think of such hit classes to exclude before conducting the search. An unsupervised clustering process obviates the need for such critical thinking during the query generation process, which arguably requires extensive digital forensics experience and knowledge of low-level, system related data.

## 5.3. Second case study

The second case involved a simulation experiment using a mock case and experimental data (see Section 4.2). We followed the same procedure and used the same test platforms as the real-world case. The 19 query terms produced an average of 118,387 search hits (124,520 hits retrieved by EnCase™; 122,313 hits retrieved by FTK™; and 108,329 hits retrieved by dfGrouper). Using the same SSOM parameters, we found dfGrouper performed much more poorly than EnCase™ and FTK™ (Table 5). The clustering approach (dfGrouper) netted lower levels of query precision and recall at nearly all cut-off points compared to current approaches. A poor average precision score for dfGrouper relative to current approaches followed (0.087 for dfGrouper, compared to 0.326 and 0.383 for EnCase™ and FTK™ respectively).

Post-hoc analysis disclosed two reasons for this poor performance. First, the digital forensic investigators who prioritized the search string list for each case considered different factors. The investigator for the real-world divorce case prioritized search strings according to probable evidentiary value, regardless of potential “noise” that yields high false positive rates. Conversely, the investigator for the mock murder case took probable ‘noise’ into account when prioritizing the search strings. Thus, he penalized search strings he believed would net a large number of false positives. This signi<sup>fi</sup>cantly biased the performance toward EnCase™ and FTK™.

Second, we discovered the 7×7 SOM map provided insuf<sup>fi</sup>cient granularity for the larger search hit set (100,000+ search hits in the mock murder case compared to approximately 25,000 search hits in the real-world case). Over 87% of the relevant search hits were clustered into one very large and extremely heterogeneous cluster. Neither a large cluster, nor a single cluster containing a vast majority of the relevant search hits is a problem in and of itself, so long as the cluster is relatively homogeneous and/or the hits are prioritized such that the relevant hits are presented <sup>fi</sup>rst. This was not the case, however. The single cluster AvgP score for the referenced cluster was only 0.372, which caused the investigator to erroneously conclude the cluster was not relevant to the investigation. Clearly, appropriate SOM granularity in<sup>fl</sup>uences the effectiveness of post-retrieval search hit clustering.

When we re-ran the experiment with a larger SOM map (20×10), the large heterogeneous cluster split into six better performing and more homogeneous clusters. With a more appropriately sized SOM, we again found the clustering approach (dfGrouper) outperformed EnCase™ and FTK™. Table 5 summarizes the empirical results. We observed a 40% decrease in the satis<sup>fi</sup>cing point for dfGrouper upon resizing the SOM map.

It is important to note that this analysis was conducted via simulation. Due to the laborious nature of the human analytical task (requiring 30+ hours for a single research volunteer), we simulated the cluster navigation behavior. We made several very conservative assumptions regarding cluster navigation behavior based on observations from the two previous cluster navigation experiments. For example, our simulation presumed the analyst considered the 181 clusters where AvgPb0.5 before getting to any of the 19 clusters with higher AvgP scores. We presumed the analyst reviewed 75 nonrelevant search hits before switching clusters, whereas real-world navigators seemed to switch clusters after 20–30 non-relevant hits. Several other similarly conservative assumptions were made. In spite of our highly conservative assumptions regarding the dfGrouper search hit review order and search hit prioritization bias that considered “noise” in the presumed search hit review order for EnCase™ and FTK™, post-retrieval search hit clustering of digital forensics string search output (i.e. dfGrouper) signi<sup>fi</sup>cantly outperforms current approaches when the SOM map is appropriately sized.

Satis<sup>fi</sup>cing analysis (mock case).

<table><tr><td rowspan="2"></td><td rowspan="2">EnCaseTM</td><td rowspan="2">FTKTM</td><td>dfGrouper</td><td>dfGrouper</td></tr><tr><td>(Map size: 7×7)</td><td>(Map size: 20×10)</td></tr><tr><td>Satisficing cut-off point</td><td>58.5%</td><td>58.4%</td><td>75.9%</td><td>32.6%</td></tr><tr><td>Precision</td><td>15.0%</td><td>15.7%</td><td>10.2%</td><td>31.2%</td></tr><tr><td>Recall</td><td>93.7%</td><td>94.2%</td><td>65.3%</td><td>85.4%</td></tr><tr><td>HIP-1 time</td><td>1457.4 min. (24.29 h)</td><td>1394.2 min. (23.24 h)</td><td>1544.46 min. (25.74 h)</td><td>663.4 min. (11.06 h)</td></tr></table>

## 6. Contributions and limitations

## 6.1. Contributions

The primary purpose of this research was to apply text mining techniques to the digital forensics domain to reduce IR overhead, while continuing to achieve at or near 100% recall rates. A secondary purpose pertains to the general IR domain. We sought to determine whether post-retrieval clustering, solely as an unsupervised text categorization tool, reduces IR overhead by increasing average precision. The following is a discussion of our contribution to each domain.

## 6.1.1. Contribution to digital forensics domain

As shown, information retrieval and text mining algorithms can significantly improve the information retrieval effectiveness of digital forensic text string searches, while retaining 100% absolute recall rates. To the best of our knowledge, this study is the <sup>fi</sup>rst academic work to theorize and empirically examine an improved process for conducting digital forensic text string searches. The academic contribution stems from the extension of research in the information and computer science disciplines to the digital forensics context. Although it was reasonable to suspect that such extension was possible, the dissimilarity of the underlying data made the feasibility and utility of such an extension questionable. Since the utility of clustering algorithms has only been demonstrated on logical level data (i.e. <sup>fi</sup>le content), demonstrating that the same algorithms can effectively and ef<sup>fi</sup>ciently be used to cluster physical level computer data is an important contribution.

The practical implications are signi<sup>fi</sup>cant as well. Digital forensics is an extremely fast growing <sup>fi</sup>eld with mounting importance in sensitive business matters, criminal investigations, as well as government and military operations. Textual artifacts are critical to knowledge acquisition in these arenas, as much user activity is textual in nature. Currently, digital forensic text string searches are effective in the sense that they produce at or near 100% recall rates, but they are very inef<sup>fi</sup>cient in the sense of extremely high IR overhead. This research empirically demonstrates that post-retrieval search hit clustering greatly improves ef<sup>fi</sup>ciency of digital forensic text string searches, by reducing the human information processing portion of IR overhead associated with reviewing non-relevant search hits. This is particularly true when investigators prioritize their search string list according to investigative utility without concern for probable ‘noise’ associated with certain search strings. Therefore, clustering text string search hits will enable the investigator to get to the relevant search hits much more quickly than is currently possible, and enables them to include all desired search strings in their query without concern for ‘noise.’ This impacts all investigations, but is particularly helpful in time constrained investigations.

## 6.1.2. Contribution to general IR domain

Although previous studies (Table 1) report marked improvements in average precision, thus reducing IR overhead, the vast majority of the studies include a multi-dimensional visualization technique in their approach. While clustering is the foundation for the resultant visual display, the two are inextricably linked from the standpoint of empirical measurement. Thus, the impacts of topical mapping versus data visualization techniques are not separately identi<sup>fi</sup>ed.

Visualization techniques in IR have had two major motivations: 1) enabling decision makers to attend to a greater amount of information, and 2) facilitating search tasks that are more ‘browsing’ oriented (exploratory; lesser search goal speci<sup>fi</sup>city). IR tasks that are more explicit search and retrieval tasks, rather than decision making or browsing tasks may not need, nor necessarily bene<sup>fi</sup>t to the same degree from such visualization techniques. However, in today's business intelligence, digital library, and knowledge base contexts, the signal to noise ratio is continually decreasing as data stores increase in size and heterogeneity. Thus, algorithmically simple, literal search techniques are likely to be problematic. As with the digital forensics context, the resultant output leads to signi<sup>fi</sup>cant IR overhead. Clustered list output may be a viable solution to this problem.

As Table 1 shows, we found <sup>fi</sup>ve studies that investigated the impact of clustered list output on average precision, without confounding the results with visualization displays [10,16,40,49,54]. However, [10] included meta-searching in the clustering algorithm, and [40] included relevancy feedback into an adaptive search and clustering algorithm. So, while the output was in fact a clustered list, the search algorithms integrated multiple IR techniques. Of the remaining studies, [49] used Ward's hierarchical clustering, and [54] used a phrase-based partitioning algorithm called Stemming Tree Clustering (STC). Neither study measured average precision formally. Only Ref. [16] used Kohonen SOMs, although they used an ensemble, bootstrapped approach. Further, their study measured clustering performance measures (recall and precision), rather than average precision. In other words, their study was not necessarily designed to improve, nor measure the improvement of average precision and reduction in the human analysis portion of IR overload. Last, an ensemble, bootstrapped approach is more likely to increase the computer processing portion of IR overload.

This leaves an important question unanswered by past research. Can post-retrieval clustering, solely as an unsupervised text categorization tool, reduce IR overhead by increasing average precision, independent from the IR bene<sup>fi</sup>ts achieved via multi-dimensional visual displays of search output, as well as semantic relationship discovery to overcome vocabulary differences problems? Our exploratory case studies lend support for an af<sup>fi</sup>rmative answer to that question. Thus, our approach has implications for search and retrieval tasks in the general IR domain, particularly those in highly heterogeneous data stores.

## 6.2. Limitations

The most obvious limitation of this study is generalizability. We applied our process to only two cases. However, one case consisted of real-world evidence, and the other contained real-world ‘noise,’ which bolsters validity and generalizability of the research. The use of a single evaluator per case also limits the generalizability of our <sup>fi</sup>ndings. Although the investigators were highly experienced, future studies should replicate these <sup>fi</sup>ndings with other evidence sizes and case types, as well as consider variation across evaluators pertaining to relevancy ranking and cluster navigation behavior.

Additionally, the technical dif<sup>fi</sup>culties experienced with the realworld evidence, as well as the relatively small size of both data sets (40 GB and 10 GB), resulted in a relatively low number of search hits (24,500–120,000) compared to typical digital forensic text string searches. Although this is a cause for some concern, previous research demonstrated the Kohonen SOMs are capable of clustering as many as 6–7 million ‘documents’ quickly [22,25].

Finally, this research did not signi<sup>fi</sup>cantly explore the impact of varying key Kohonen SOM parameters, including neighborhood size, annealing rate, and map size (two map sizes explored). These parameters certainly in<sup>fl</sup>uence the quality of the resultant clusters, both positively and negatively. While the performance measures reported here are suggestive of high cluster quality scores, F-scores should be formally measured under a variety of controlled map parameter conditions.

## 7. Suggestions for future research

Since this research was exploratory, involving two case studies, there is ample room for future research. We were able to demonstrate improved IR ef<sup>fi</sup>ciency of the digital forensic text string search involving one real-world case and one mock, experimental case. Since the cases involved relatively small hard drives running Windows™, future research should explore larger data sets with respect to media size, query size, and search result set size, as well as other <sup>fi</sup>le systems, operating systems, and search options.

Future research should also explore the impact of information visualization approaches on IR overhead in the digital forensic text string search context. Since the focus of the research was on testing the feasibility and utility of the proposed process, as well as the desire to separate the effects of visualization and topical clustering, we ignored the HCI design, ease of use, and task-technology-<sup>fi</sup>t considerations. Visualization is a human-computer interaction (HCI) issue, and it is important to measure the effects of clustering as a topical mapping tool versus the effects of clustering on visualization and its impact on cognitive information processing.

Another area for future research concerns cluster process optimization, which includes SOM design (i.e. map size and vector dimensionality), parameter optimization (i.e. learning rate, neighborhood radius, and annealing scheme), and document set reduction mechanisms (i.e. stop words and stemming). A framework should be established for systems and/or users to reliably predict the optimal map size, document vector size and/or type(s) (i.e. metadata and/or content-bearing terms), and parameters for various problem sets (types and sizes of data sets, queries, and search result sets). Researchers should also consider empirical study of parameter-less SOMs [4]. Regarding stop words, it is highly doubtful that the traditional stop word list is the best list to apply to digital evidence. Certainly, physical level computer media will have an additional set of stop words, related to system and <sup>fi</sup>le metadata.

Future research should also empirically study cluster navigation behavior and satis<sup>fi</sup>cing points. Little is known about how users navigate clustered search hits, or when they cease analytical efforts in the light of resource constraints and legal suf<sup>fi</sup>ciency considerations, especially in the digital forensics context. Such knowledge is critical in support of the other research areas mentioned. The methodological approach undertaken in this research is extremely burdensome on the part of the research volunteers, and does not necessarily coincide with the behavior of the resource constrained investigators and analysts in real-world investigations. Understanding cluster navigation behavior and satis<sup>fi</sup>cing point determination will aid future research in all areas mentioned by supporting methodological approaches involving modeling and simulation.

## Appendix A. Search query terms (in investigative priority order)

Real-world divorce case.

```txt
1. Affair 9.<string 1> 17.<website2>
2. Separated 10.<string 2> 18.<website3>
3. Divorce 11. Password 19.<email4>@aol.com
4. Swinging 12. Wife swapping 20.<email5>@aol.com
5.<type of automobile> 13.<email1>@aol.com 21.<email6>@aol.com
6.<spouse's name> 14.<email2>@aol.com 22.<email7>@netzero.com
7. Nude 15.<email3>@hotmail.com
8. Naked 16.<website1>
```

Note, the bracketed words in the string search list are masks for the actual strings, used to protect privacy and/or minimize offensive language in this article.

Note, the experiment utilized only 17 of the 22 strings. Strings 5, 6, 11, 14, and 16 were omitted from the analysis, due to unresolved technical issues encountered with the searching component pertaining to those terms. The problem involved extracting certain logical blocks from the physical evidence. We are con<sup>fi</sup>dent that the re<sup>fi</sup>nement of the query did not bias the experimental results in any way.

## Mock murder case.

<table><tr><td>1. Justin</td><td>6. Evidence</td><td>11. Chemical</td><td>16. Love</td></tr><tr><td>2. Nitrate</td><td>7. Murder</td><td>12. Autopsy</td><td>17. Smith</td></tr><tr><td>3. Insurance</td><td>8. Kill</td><td>13. Suzy</td><td>18. Money</td></tr><tr><td>4. Illness</td><td>9. Death</td><td>14. Suzie</td><td>19. Password</td></tr><tr><td>5. Poison</td><td>10. Policy</td><td>15. Gym</td><td></td></tr></table>

## References

[1] W. Alink, R. Bhoedjang, P. Boncz, A. de Vries, XIRAF — XML-Based Indexing and Querying for Digital Forensics, Digital Investigation 3 (2006)8 (2006).

[2] N.L. Beebe, J.G. Clark, Digital forensic text string searching: improving information retrieval effectiveness by thematically clustering search results, Digital Investi gation 4 (2007) S1.

[3] N.L. Beebe, G. Dietrich, A new process model for text string searching, in: S. Shenoi, P. Craiger (Eds.), Research Advances in Digital Forensics III, Springer, Norwell, 2007.

[4] E. Berglund, The parameter-less SOM algorithm, Proceedings of the The Eighth Australian and New Zealand Intelligent Information Systems Conference (ANZIIS'2003), December 10–12, 2003, Sydney, Australia, 2003.

[5] E. Casey, Network traf<sup>fi</sup>c as a source of evidence: tool strengths, weaknesses, and future needs, Digital Investigation 1 (2004)8 2004.

[6] H. Chen, K.J. Lynch, Automatic construction of networks of concepts characterizing document databases, IEEE Transactions on Systems, Man, and Cybernetics 22 (1992) 5.

[7] H. Chen, C. Schuffels, R. Orwig, Internet categorization and search: a selforganizing approach, Journal of Visual Communication and Image Representation 7 (1) (1996).

[8] H. Chen, A.L. Houston, R.R. Sewell, B.R. Schatz, Internet browsing and searching: user evaluations of category map and concept space techniques, Journal of the American Society for Information Science 49 (1998) 7.

[9] H. Chen, Y. Zhang, A.L. Houston, Semantic indexing and searching using a Hop<sup>fi</sup>eld net, Journal of Information Science 24 (1998) 1.

[10] H. Chen, F. Fan, M. Chau, D. Zeng, MetaSpider: meta-searching and categorization on the web Journal of the American Society for Information Science and Technology 52 (2001)13.

[11] W. Chung, H. Chen, J.F. Nunamaker, Discovery on the web: an empirical study of business intelligence exploration, Journal of Management Information Systems 21 (2005) 4.

[12] D.R. Cutting, D.R. Karger, J.O. Pedersen, J.W. Tukey, Scatter/Gather: a cluster-based approach to browsing large document collections, Proceedings of the 15th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, Copenhagen, Denmark, 1992.

[13] P. Ferragina, A. Gulli, A personalized search engine based on Web-Snippet hierarchical clustering, Proceedings of the International World Wide Web Conference, Chiba, Japan, 2005.

[14] R.T. Freeman, H. Yin, Tree view self-organisation of web content, Neurocomputing 63 (2005)8 January.

[15] B.C.M. Fung, K. Wang, M. Ester, Hierarchical document clustering using frequent itemsets, Proceedings of the Third SIAM International Conference on Data Mining, San Francisco, California, 2003.

[16] A. Georgakis, H. Li, M. Gordan, An ensemble of SOM networks for document organization and retrieval, Proceedings of the AKRR'05, International and Interdisciplinary Conference on Adaptive Knowledge Representation and Reasoning, June 15–17, 2005, Espoo, Finland, 2005.

[17] J. Giordano, C. Maciag, Cyber forensics: a military operations perspective, International Journal of Digital Evidence 1 (2002) 2.

[18] X. He, C.H.Q. Ding, H. Zha, H.D. Simon, Automatic topic identi<sup>fi</sup>cation using webpage clustering, Proceedings of the IEEE Conference on Data Mining, November 29–December 2 2001, San Jose California 2001

[19] M.A. Hearst, J.O. Pedersen, Reexamining the cluster hypothesis: scatter/gather on retrieval results Proceedings of the 19th ACM International Conference on Research and Development in Information Retrieval, ACM Press, Zurich, Switzerland, 1996.

[20] E.E. Kenneally, C.L.T. Brown, Risk sensitive digital evidence collection, Digital Investigation 2 (2005) 2.

[21] T. Kohonen, The self-organizing map, Proceedings of the IEEE, 78, 1990, p. 9.

[22] T. Kohonen, S. Kaski, K. Lagus, J. Salojarvi, J. Honkela, V. Paatero, A. Saarela, Self organization of a massive document collection, IEEE Transactions on Neural Networks 11 (3) (2000).

[23] K. Lagus, T. Honkela, S. Kaski, T. Kohonen, WEBSOM for textual data mining, Arti<sup>fi</sup>cial Intelligence Review 13 (1999).

[24] K. Lagus, S. Kaski, T. Kohonen, Mining massive document collections by the WEBSOM method, Information Sciences 163 (2000) 1–3.

[25] K. Lagus, S. Kaski, T. Kohonen, Mining massive document collections by the WEBSOM method, Information Sciences 163 (2004) 1–3.

[26] A.V. Leouski, W.B. Croft, An Evaluation of Techniques for Clustering Search Results, Computer Science Department, University of Massachusetts at Amhers, Amherst, MA, 1996, pp. 1–19.

[27] A. Leuski, Evaluating document clustering for interactive information retrieval, Proceedings of the Tenth International Conference on Information and Knowledge Management, ACM Press, Atlanta, Georgia, 2001.

[28] A. Leuski, J. Allan, Improving interactive retrieval by combining ranked lists and clustering, Proceedings of the RIAO, College de France, 2000.

[29] A. Leuski, J. Allan, Interactive information retrieval using clustering and spatial proximity, User Modeling and User-Adapted Interaction 14 (2004) 2–3.

[30] X. Lin, D. Soergel, G. Marchionini, A self-organizing semantic map for information retrieval, Proceedings of the Fourteenth Annual International ACM/SIGIR Conference on Research and Development in Information Retrieval, October 13-16 1991 ACM Press Chicago IL. 1991

[31] C. Lin, H. Chen, J.F. Nunamaker Jr., Verifying the proximity and size hypothesis for self-organizing maps, Journal of Management Information Systems 16 (3) (1999).

[32] R. Orwig, H. Chen, J.F. Nunamaker Jr., A graphical, self-organizing approach to classifying electronic meeting output, Journal of the American Society for Information Science 48 (2) (1997).

[33] G.L. Palmer, A Road Map for Digital Forensics Research — Report from the First Digital Forensics Research Workshop (DFRWS) (Technical Report DTR-T001-01 Final), Air Force Research Laboratory, Rome Research Site: Utica, 2001, pp. 1–48.

[34] M. Pendergast, R. Orwig, Quantitative measures for evaluating knowledge network node clusters: preliminary results, Proceedings of the 39th Hawaii International Conference on System Sciences, Hawaii, 2006

[35] M.F. Porter, An algorithm for suf<sup>fi</sup>x stripping, Program 14 (1980) 3.

[36] D. Radcliff, Inside the DoD's crime lab, NetworkWorldFusion, 2004, pp. 1–5.

[37] V. Roussev, G.G. Richard III, Breaking the performance wall: the cases for distributed digital forensics, Proceedings of the Digital Forensics Research Workshop (DFRWS) 2004, August 11–13, Linthicum, Maryland, USA, 2004.

[38] D. Roussinov, H. Chen, A scalable self-organizing map algorithm for textual classi<sup>fi</sup>cation, A Neural Network Approach to Thesaurus Generation, Communication Cognition and Arti<sup>fi</sup>cial Intelligence 15 (1998) 1–2.

[39] D. Roussinov, H. Chen, Document clustering for electronic meetings: an experimental comparison of two techniques, Decision Support Systems 27 (1999) 1–2.

[40] D. Roussinov, H. Chen, Information navigation on the web by clustering and summarizing query results, Information Processing & Management 37 (2001) 6.

[41] D. Roussinov, J.L. Zhao, Automatic discovery of similarity relationships through web mining, Decision Support Systems 35 (1) (2003).

[42] G. Salton, A. Wong, C.S. Yang, A vector space model for automatic indexing, Communications of the ACM 8 (1975) 11.

[43] D. Schuff, O. Turetken, J. D'Arcy, A multi-attribute, multi-weight clustering approach to managing “E-Mail Overload”, Decision Support Systems 42 (2006) 3.

[44] M. Schwartz, Cybercops need better tools, Computerworld, 2000, p. 1.

[45] F. Sebastiani, Machine learning in automated text categorization, ACM Computing Surveys 34 (1) (2002).

[46] B. Shneiderman, The eyes have it: a task by data type taxonomy for information visualizations, Proceedings of the IEEE Symposium on Visual Languages, September 3–6, 1996, Boulder, CO, 1996.

[47] H.A. Simon, Administrative Behavior, The Macmillan Company, New York, 1947.

[48] P. Sommer, The challenges of large computer evidence cases, Digital Investigation (2004) 1.

[49] O. Turetken, R. Sharda, Clustering-based visual interfaces for presentation of web search results: an empirical investigation, Information Systems Frontiers 7 (2005) 3.

[50] C.J. van Rijsbergen, Information Retrieval, 2nd edButterworths, London, 1979.

[51] P. Willett, Recent trends in hierarchic document clustering: a critical review, Information Processing & Management 24 (1988) 5.

[52] K.L. Yu, W. Lam, A new on-line algorithm for adaptive text <sup>fi</sup>ltering, Proceedings of the CIKM-98, 7th ACM International Conference on Information and Knowledge Management, Bethesda, MD, 1998.

[53] O. Zamir, O. Etzioni, Web document clustering: a feasibility demonstration, Proceedings of the 19th International ACM SIGIR Conference on Research and Development of Information Retrieval, ACM Press, Melbourne, Australia, 1998.

[54] O. Zamir, O. Etzioni, Grouper: a dynamic clustering interface to web search results, Proceedings of the 8th World Wide Web Conference, May, 1999, Toronto, Canada, 1999.

Nicole Lang Beebe is an Assistant Professor in the Department of Information Systems & Technology Management at the University of Texas at San Antonio (UTSA) She received a BS in Electrical Engineering from Michigan Technological University, an MS in Criminal Justice from Georgia State University, and a PhD in Business Administration (Information Technology) from UTSA. She has over ten vears experience in information security and digital forensics, in both the commercial and government sectors. She is a Certi<sup>fi</sup>ed Information Systems Security Professional (CISSP) and holds two digital forensics certi<sup>fi</sup>cations (ACE and EnCE). Her research interests include digital forensics, information security, and data mining. She has published several journal articles related to information security in digital forensics in The DATABASE for Advances in Information Systems, Communications of the AIS, Digital Investigation, and Journal of Information System Security (JISSEC).

Jan Guynes Clark is a Professor in the Department of Information Systems & Technology Management, at the University of Texas at San Antonio (UTSA). She holds a PhD (Management of Information Systems) from the University of North Texas. She is a Certi<sup>fi</sup>ed Information Systems Security Professional (CISSP). Her research interests include: the impact of information technologies on productivity and performance, information security, and IS strategies. Her publications have appeared in leading journals such as Communications of the AIS, Communications of the ACM, IEEE Transactions on Engineering Management, and Information & Management.

Glenn Dietrich is the Chair of the Department of Information Systems & Technology Management, at The University of Texas at San Antonio (UTSA). He holds a PhD (Information Systems) from The University of Texas at Austin. He is one of the founding directors of the Center for Infrastructure Assurance and Security at UTSA. His research interests include: information assurance, technology management information systems strategy and adoption of new technologies. His publications have appeared in leading journals such as Communications of the AIS, and IEEE Transactions on Engineering Management.

Myung Ko is an Associate Professor in the Department of Information Systems & Technology Management at the University of Texas at San Antonio (UTSA). She received her PhD from Virginia Commonwealth University. Her research interests include impact of IT on organization, data mining, and economics of security breach. Her work has been published in refereed journals such as Information & Management, Information Systems Journal, Information and Software Technology, Information Resources Management Journal, Journal of Information Technology Theory and Application (JITTA), and Information Technology & Management.

Daijin Ko is a Professor in the Department of Management Science and Statistics, at the University of Texas at San Antonio (UTSA). He holds a PhD (Statistics) from the University of Washington. His research interests include: Bioinformatics, Data Mining, and Biostatistics. His publications have appeared in leading journals such as Annals of Statistics, JASA, Biometrics, Journal of Multivariate Analysis, Statistical Science, Molecular Systems Biology, Journal of Biological Chemistry, Neurology, and Information Resources Management Journal.
