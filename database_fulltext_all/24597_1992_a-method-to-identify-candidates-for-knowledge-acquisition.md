---
otero_id: 24597
otero_key: "3YJYB526"
title: "A Method to Identify Candidates for Knowledge Acquisition"
authors: "Eric W. Stein"
year: "1992"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1992.11517963"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Method to Identify Candidates for Knowledge Acquisition

Eric W. Stein

To cite this article: Eric W. Stein (1992) A Method to Identify Candidates for Knowledge Acquisition, Journal of Management Information Systems, 9:2, 161-178, DOI: 10.1080/07421222.1992.11517963

To link to this article: http://dx.doi.org/10.1080/07421222.1992.11517963

![](/api/attachments/3YJYB526/fulltext/images/5f5577392719392578f469545b3b16e767807dfb628602e5581d958b0e715440.jpg)

Published online: 16 Dec 2015.

![](/api/attachments/3YJYB526/fulltext/images/3fa377362a05f6dacfa3a78e9793a72cbb401c7371344f00ece4f02f7d4c3fcb.jpg)

Submit your article to this journal ↗

![](/api/attachments/3YJYB526/fulltext/images/feb69b266d8ff299193f100e86ec9ed78b03ef62cdb3d505d7aac24f5e72b845.jpg)

View related articles ↗

![](/api/attachments/3YJYB526/fulltext/images/2dfa1c77e3534efc69ae514abf8758f5421b064327db8389f83fd784df63a553.jpg)

Citing articles: 9 View citing articles ↗

# A Method to Identify Candidates for Knowledge Acquisition

ERIC W. STEIN

ERIC W. STEIN is Assistant Professor of MIS at the Pennsylvania State University. He earned his bachelor's degree in physics from Amherst College in 1979 and his Ph.D. in managerial science from The Wharton School of the University of Pennsylvania in 1989. His research focuses on the MIS aspects of organizational learning and memory. His current research interests include operationally defining and measuring organizational memory, developing MIS systems to support knowledge retrieval, identifying expertise in organizations, expert system development, case-based DSS, and environmental decision-making. He has published in the Proceedings of the International Symposium on Artificial Intelligence and the AORN Journal, and has presented at the Academy of Management, the Conference on Expert System Applications for the Electric Power Industry, the International Conference on Social Networks, and the International Academy of Business Disciplines.

ABSTRACT: The purpose of this work is to introduce a systematic method for identifying expertise (knowledge identification). The technique, borrowed from the social sciences and known as network analysis, may be used to identify human experts as well as documented sources of knowledge within organizational settings. Network analysis is simple to administer, cost-effective, and complements interview methods. Following a discussion of the theory underlying the technique, its application in a field setting is demonstrated. The results are checked against what would be expected due to chance, and cross-validated through interviews. To ensure the efficacy of the method, knowledge identification at a second site is briefly described. The work closes with some ideas for future management information systems research using network analysis.

KEY WORDS AND PHRASES: expert systems, knowledge acquisition, knowledge engineering, knowledge identification, network analysis.

## 1. Introduction

THE PROCESS OF BUILDING AN EXPERT SYSTEM begins with the difficult task of identifying both a domain of knowledge and sources of expertise. These early tasks of identification form part of the process known as knowledge acquisition [2, 10]. Criteria for domain selection are well documented and are driven by organizational considerations such as business strategy, scarcity of expertise, payback, and demand

Acknowledgment: The author expresses his thanks to Jane Webster, Vladimir Zwass, and to the anonymous reviewers at JMIS for helpful feedback on earlier drafts of this paper.

for knowledge [5, 20, 28] as well as factors intrinsic to the knowledge itself such as decomposability and stability [22].

In conjunction with domain selection, experts must be identified and selected: “part of the knowledge acquisition problem is identifying sources of knowledge,” according to McDermott [19]. Relatively less has been written about this issue. Keller [13] suggests “proving” expertise through specification of a performance metric. Prerau [23] suggests selecting an expert based on individual skills and abilities such as long-term task performance and communication ability, as well as social-psychological variables such as cooperativeness, affability, and commitment. In contrast, Waterman [29] suggests picking experts based on the opinions of knowledgeable members of the organization. While ad hoc interviews with managers can be conducted to identify experts, an alternative is to survey stakeholders of the organization (e.g., members of a department including managers and employees, or outside consultants) by asking them to nominate candidates for knowledge acquisition. This survey method is a form of network analysis, which is used in the social sciences.

This work provides a brief description of network analysis, justifies its use for knowledge identification, and describes how to collect and analyze network data. In the second half of the paper, the identification of expertise at two field sites is discussed. The paper closes with ideas for the application of network analysis to other areas of research in management information systems.

## 2. What Is Network Analysis?

NETWORK ANALYSIS EVOLVED FROM SOCIOGRAMS [21] TO THE graph theoretic notions of Harary et al. [9] to later models that measure multiple relations across several networks. Network analysis is based on the measurement of interactions or relations between individuals. Interactions may be of several types: communication (e.g., information), instrumental exchange (e.g., money); power; sentiment (e.g., trust); and kinship [15]. Communication interactions are typically expressed in terms of the absence or presence of ties (i.e., 0 or 1) or relative frequencies; monetary flows are expressed in dollars, and other relations in relative units. The quality of an exchange also may be specified. For example, information exchanges between individuals may be qualified in terms of importance, accuracy, and timeliness of the information sent or received [16].

Relations between individuals may be represented either as directed graphs (i.e., digraphs) or matrices [8, 9]. For example, if A seeks knowledge from B, then that relation can be represented on a digraph by drawing an arrow from A to B. Alternatively, the same information can be represented as a “1” in a matrix of senders and receivers. Whole organizations can be represented as aggregates of dyadic relations. Once in matrix form, the data may be analyzed several ways. $^{1}$ Network analysis offers system-level, group-level, and individual-level metrics. The interested reader is referred to appendix 1 for a more extensive discussion of network measures. The most important construct relative to this discussion is individual member centrality. Centrality is a measure of the prominence of an individual in a network [8] based on the number of paths passing through that individual [17]. Degree centrality is measured in terms of the number of direct links between an individual and other individuals and is interpreted in terms of “communication activity” [8]. The outdegree of an individual indicates the number of paths out from that individual to all others in the network [15]. The indegree is the number of paths in to an individual from all others. Individuals with the highest indegree or outdegree measures are considered most central to the network (figure 1). Indegree and outdegree measures may also be scaled in terms of intensity (e.g., frequency of information interactions per week) as well as quality (e.g., importance, timeliness, and accuracy). The assumption made in this work is that individuals with high indegree centrality based on retrieval scores are sources of expertise for the organization.

## 3. Justification

## 3.1. Characteristics of Expertise

NETWORK ANALYSIS IS A JUSTIFIABLE TECHNIQUE FOR the identification of expertise because expertise is a social variable [29] known to members of the organization. Members of organizations (managers and employees) know where expertise is because they depend on these sources to solve problems and to make decisions. The views of several members of the organization are considered more accurate in identifying expertise than the views of a few managers based on the observation that managers may not accurately perceive employee abilities, skills, and knowledges. Applied behavioral research has shown that employees adept at image management are perceived by their superiors as better than they actually are and receive higher performance ratings [30]. On the other hand, race [7] and grievance activity [14] can negatively affect performance ratings of employees by managers. More subtly, managers discriminate between employees in terms of being in-group or out-group. For instance, Heneman, Greenberger and Anonyuo [12] found that leaders attributed positive qualities to in-group members and negative qualities to out-group members, which were at variance with objective measures. For these reasons, it is best to poll all the members of the organization regarding expertise. $^{2}$ Network analysis is an effective survey method for this purpose.

Another justification for using network analysis is that that expertise is assumed to be a function of the frequency that individuals retrieve information from others or from documented sources to solve problems and make decisions. Retrieval rates are believed to be correlated with actual expertise based on long-term testing and validation. Members of organizations do not seek out other members who give poor advice. Knowledge sources that do not contribute to member success will be retrieved from less often over time since the value of their knowledge will decline. Sources that contribute to member success in the choice of appropriate courses of action will be retrieved from more often, and these will emerge as sources of expertise. Network analysis is efficient at capturing this type of information. While it is true that retrieval frequency may also be an indication of other factors (e.g., accessibility), experts are chosen for what they know; that is, by type of knowledge. Therefore, one would expect different retrieval rates for different types of knowledge, especially if the knowledge is highly specialized. What may not be apparent under these assumptions is the degree to which comparable experts are better or worse than each other. It is possible that more accessible experts score higher in terms of retrieval rates than other equally qualified but less approachable experts. However, accessibility and other factors are important in expert selection [22]. This inherent bias of the method is therefore believed to be in the knowledge engineer's favor.

![](/api/attachments/3YJYB526/fulltext/images/5c9c45e9b7b0be0c2e51b24a2cd20c9b1ad12c16ab0ae4a6d2e85fe7fc3c6469.jpg)  
Figure 1. Illustration of Member with High In-Degree Centrality. Key: Thickness of line indicates frequency of retrieval. Arrow points to member from whom information is retrieved. Size of circle indicates centrality. Large circles indicate high centrality for a particular type of knowledge.

## 3.2. Characteristics of Network Analysis

There are several benefits to selecting network analysis as a technique for knowledge identification. For one, the method is useful because it identifies documented sources of knowledge as well as human expertise. Second, network analysis is systematic and objective, and it produces reproducible results each time. Third, it is comprehensive in that it is based on information collected from the whole social unit, not just from one or two individuals. A consequence of the comprehensiveness of the method is that human expertise is identified fairly and unobtrusively. Fourth, network analysis is robust because other important information can be obtained about members of the organization by asking different questions. For example, we may ask: "Who do you consider to be most cooperative?" These data can be used to build a profile of potential candidates for knowledge acquisition on variables other than just expertise. Another benefit of the method is that it complements other methods of data collection. For example, in a large organization, a network survey can be used to identify candidates for knowledge acquisition, who are subsequently interviewed. Alternatively, the network survey can be used to discriminate between comparable candidates in terms of cooperativeness, affability, commitment, and other variables. The bottom-line benefit of the method is that it can be administered easily, saving many hours of interviews.

## 3.3. Other Benefits

Network data can also provide the knowledge engineer with a picture of information dependencies that exist between the expert and the rest of the organization, dependencies of which even the expert might be unaware. Understanding the expert's knowledge from the perception of the expert's user community can improve the quality of the systems created. Network analysis can help the knowledge engineer design the expert system to function in the context of socially defined information roles and structures, all of which help in the implementation phase.

## 3.4. Caveats

The primary caveat to applying network analysis is pragmatic. The method is recommended for departments of 15 to 100 people. The method is not appropriate for application to very small organizations, that is, fewer than ten people. In these cases, it would be better to conduct interviews. The technique may be applied to large organizations (i.e., more than 100 people) if sufficient time, money, and resources are available. Another factor determining the scope of study is the number of relations profiled. Management may require that factors such as trust and cooperation be considered in addition to retrieval rates when identifying candidates for knowledge acquisition. It may be argued that if retrieval rates are the sole criterion for expert selection, then an expert might emerge that management does not trust. Information systems, either implicitly or by design, reflect organizational values. An expert system built by an employee who is not trusted could result in disaster. However, this situation may be avoided by assessing trust on the network survey (e.g., “Who do you trust most in the organization?”) or via other methods (e.g., by interviewing managers). Multi-relational surveys require proportionately more resources (e.g., time) than single-relation surveys.

## 4.1. How to Collect and Analyze Network Data

TO PERFORM A NETWORK ANALYSIS, A QUESTIONNAIRE must be constructed and administered. A department of 30 to 40 people can be surveyed in less than a day; 100 people can be surveyed in a few days. Network questionnaires can be completed in three to five minutes by pen and paper or one to three minutes by telephone, and the data are easily tabulated in a spreadsheet. Companies networked via electronic mail are able to survey employees with less effort.

The design of the questionnaire requires several specifications. First, the researcher must select the type of relation to be profiled (e.g., information exchange, trust). Second, the researcher must consider scaling issues. The researcher may simply detect the presence of a tie between two actors (e.g., as 0 or 1), scale the interaction nominally (e.g., high, medium, or low), or scale it via an interval scale (e.g., 1–10). If knowledge retrieval is the relation profiled, then the researcher must select the type of knowledge exchanged. When constructing an expert system, the domain of knowledge is usually known with great specificity. Questions are then constructed to measure the strength of the interaction. For example, if we want to know from whom people retrieve information about marine underwriting, we would ask the following question: "From whom do you retrieve information about marine underwriting?" To complete the construction of a questionnaire, the researcher should obtain lists of members in the organization and other sources (e.g., information systems) being profiled by the study. Major categories of systems include: Electronic Databases (DB); Manual Databases (DBm); Personal Computers (PC's); Personal Files and Training Manuals. The inclusion of the list of members (as recommended by Burt et al. [4] and Alba [1]) and systems on the questionnaire facilitates answering the questions. See appendix 2 for an example of a network questionnaire.

Network data may be tabulated and analyzed through specialized programs (e.g., UCINET), statistical packages, and spreadsheets. In all cases, one sets up a matrix of communication pairs. If a spreadsheet is utilized (a simple and effective tool for analyzing degree centrality scores), the following procedure may be used. Each respondent (Ni) is assigned an identification number (ID#). These identification numbers are listed across the top row of the spreadsheet and correspond to what is often referred to as the “ego” of a communications pair [1]. In the left-hand column the names of members or information resources (Rj) identified by the ego are listed—these correspond to the “alter” of a communication pair [1]. $^{3}$ Scores for each ego–alter (NiRj) pair are located in the corresponding cells of the matrix. Frequency-scaled indegree and outdegree scores for each resource (Rj) are obtained by calculating the row and column sums. Row sums represent the indegree centrality scores and column sums represent the outdegree scores. The row sums, which indicate retrieval centrality, are then ordered from the highest to the lowest. Members with the highest scores are primary sources of knowledge for the organization.

## 4.2. An Illustration of the Identification of Expertise at a Field Site

The purpose of this section is to illustrate how the techniques may be applied to identify sources of knowledge. The illustration is based on research conducted at a small business library where expertise was identified as one phase of a larger study $[27]$ . Both human experts and sources of documented knowledge that supported decision making and problem solving were identified using network analysis. Expertise was assumed to be a function of the frequency that organization members retrieved information from peers or from documented sources to solve problems and make decisions. Expertise was measured by first determining indegree scores of centrality, which were scaled in terms of frequencies per week, and then ranking the results. The higher the centrality score, the greater the assumed level of expertise.

## 4.2.1. Types of Knowledge Measured

The knowledge base of the twenty-one-person department was partitioned into five general types of work-related knowledge $^{4}$ :

\- Services. Service support was defined as technical processing and cataloging of books, serials, and periodicals. Public services were defined as the circulation of books and periodicals, reference consulting, etc.

\- Administrative matters were defined as budget activities, personnel matters, etc.

\- Historical information was defined as former events, stories, etc.

\- Rules and norms were defined as matters of policy—i.e., what one ought to do.

These categories of knowledge were chosen because they represented the core of the organization's knowledge base. The types were distinguished using a framework by Stein [27], which classifies knowledge in terms of level of abstraction and normative orientation. The distinction between the two types of service knowledge was determined via interviews.

## 4.2.2. Sources of Knowledge

Sources of knowledge included full-time members of the department being surveyed and manual and computer-based information systems. Full-time members ranged in experience from one to thirty-seven years. Of the twenty-one employees surveyed, ten were clerical union employees, ten were nonunion professionals, and one was an administrative assistant. Staff had access to three electronic databases: DB1, an on-line electronic catalog accessible through multiple terminals; DB2, a commercial database system also accessible through multiple terminals; and DB3, a shared holdings database accessible through a single terminal. Staff also had access to three manual database files (DBm1, DBm2, DBm3). Additional information was stored in personal computers (PCs), training manuals, and personal files.

## 4.2.3. Scaling, Tabulation, and Response Rate

Respondents were asked to indicate the frequency of retrieval from other members of the organization or from documented sources on a five-point nominal scale similar to the one shown in appendix 2. Respondents were presented with a complete list of people in the organization and a list of files, databases, and the like from which to choose. Lists were prepared from organization records and initial interviews. Interaction frequencies between a respondent and other individuals or with documented sources (files, databases, etc.) were arrayed in an ego-alter matrix. All network tabulations and calculations were performed using a spreadsheet. The response rate on the network questionnaire was 100 percent—all members of the department returned completed questionnaires. Because each category of knowledge investigated was broadly defined, sufficient responses were obtained across all categories despite the department's small size.

## 4.2.4. Results

A summary of the data is shown in Table 1. Total retrievals per week per resource for all types of knowledge ranged from 11 to 159 for members and ranged from 2 to 188 for information systems. The average score per member was about half that for information systems.

The stacked bar representation provided an effective way to view the data. The centrality scores of the top twelve members of the organization and all twelve information systems is shown in figure 2. Each bar segment shows the centrality score for a particular type of knowledge and the entire bar shows total retrievals. For example, members no. 12 and 17 show high degrees of shading for administrative knowledge. The graph also provides a quick comparison of retrievals among members and between members and information systems.

The centrality scores were then normalized to facilitate the identification of expertise. Each score was normalized by the maximum retrieval score for each category of knowledge. For example, the maximum score for Services among the members was 100. This score was normalized to 1.00. The next score was 0.84, and so on. The maximum scores and normalized scores are displayed in Table 2. Scores greater than 0.75 (which are at least one standard deviation above the mean) are highlighted in bold type. Normalized scores were rank-ordered by totals. $^{5}$

## 4.2.5. Interpreting the Results

Several observations can be made with regard to the results presented in Table 1. Three types of sources are present in the organization:

1. Sources that score high for one category of knowledge only

2. Sources that score high for more than one category of knowledge

3. Sources that score low-medium for all categories of knowledge

Table 1 Summary of Centrality Data for Knowledge Resources (Retrievals per Week)

<table><tr><td></td><td>Service</td><td colspan="2">Administrative History</td><td>Norms</td><td>Totals</td></tr><tr><td colspan="6">Members</td></tr><tr><td>Min</td><td>1</td><td>0</td><td>0</td><td>0</td><td>11</td></tr><tr><td>Max</td><td>100</td><td>39</td><td>20</td><td>25</td><td>159</td></tr><tr><td>Mean</td><td>35.2</td><td>8.1</td><td>4.0</td><td>6.6</td><td>54.0</td></tr><tr><td>S.D.</td><td>24</td><td>11</td><td>6</td><td>7</td><td>39</td></tr><tr><td colspan="6">Information systems</td></tr><tr><td>Min</td><td>1</td><td>0</td><td>0</td><td>0</td><td>2</td></tr><tr><td>Max</td><td>173</td><td>33</td><td>21</td><td>16</td><td>188</td></tr><tr><td>Mean</td><td>65.3</td><td>5.6</td><td>5.0</td><td>3.3</td><td>79.1</td></tr><tr><td>S.D.</td><td>61</td><td>10</td><td>7</td><td>5</td><td>65</td></tr></table>

Person no. 12 is the best example of the first type of source. While he ranks first for what he knows about administrative matters, he ranks last for what he knows about services. It is unlikely that members retrieve information from Person no. 12 because he is accessible for one type of knowledge (e.g., administration) and not another (e.g., services). It is more likely that retrieval is a function of what he knows. The manual database (DB1m) is the primary source of knowledge regarding historical matters. The three electronic databases (DB1, DB2, DB3) are clearly key sources of information about services but not about other types of knowledge.

Persons no. 20, 5, and 17 are central to the network for more than one type of knowledge and thus represent the second type of knowledge source. We may interpret these individuals as being “superexperts” or highly influential members of the organization. If their knowledge is accurate, then they will be candidates for knowledge acquisition for more than one type of knowledge. If their knowledge is not accurate, then their identification by the knowledge engineer is equally important; it may be necessary for management to challenge and realign the way “things are done” to ensure the success of the expert system. In terms of documented sources, personal files provide strong support for knowledge retrievals concerning administration, history, and norms.

Remaining sources scored low to mid-range for all categories of knowledge. Based on the assumption that centrality scores are related to expertise for the reasons given earlier, it is highly unlikely that these are suitable candidates for knowledge acquisition; sources with low to medium scores are likely to possess only a modicum of expertise.

To summarize, the prime candidates for knowledge acquisition include Person no. 20 as a source of knowledge about services, history, and norms, and Person no. 5 for services and history. The three electronic databases (DBs 1–3) support retrievals pertaining to services, whereas the manual database (DB1m) is a source of knowledge concerning historical matters. Person no. 17 is a candidate for knowledge acquisition for administrative matters and norms. Person no. 12 is also a candidate for knowledge acquisition concerning administrative matters. Personal files support retrievals pertaining to administrative matters, history and norms. Developing an expert system would promote the sharing and distribution of that knowledge.

![](/api/attachments/3YJYB526/fulltext/images/2af5ec55547d058d2f1a176631338c04f96afad37b44ee44d65d03922b59e084.jpg)  
Figure 2. Retrieval Rates from Members and Information Systems by Type of Knowledge

## 4.2.6. Evaluating the Results against Chance

To verify that the results differed significantly from what would be expected by chance, the following test was conducted. It was assumed that if people were indifferent about whom they retrieved information from, then each person would receive approximately the same retrieval score. A chi-square test was run comparing the observed scores against the number of responses expected from a uniform distribution (i.e., the mean retrieval score). The chi-square values indicated that the observed retrieval scores for people were significantly different $p < 0.001$ than what would have occurred under an assumption of uniformity (see Table 3).

Table 2 Normalized Centrality Scores by Knowledge Type (Sorted by Total Scores)

<table><tr><td>Description</td><td>ID#</td><td>Service</td><td>Administrative</td><td>History</td><td>Norms</td><td>Total</td></tr><tr><td colspan="7">Members</td></tr><tr><td>Clerical union</td><td>p-20</td><td>1.00</td><td>0.41</td><td>1.00</td><td>0.92</td><td>3.33</td></tr><tr><td>Prof. staff</td><td>p-5</td><td>0.84</td><td>0.28</td><td>0.85</td><td>0.68</td><td>2.65</td></tr><tr><td>Prof. staff</td><td>p-17</td><td>0.47</td><td>0.97</td><td>0.05</td><td>1.00</td><td>2.49</td></tr><tr><td>Clerical union</td><td>p-6</td><td>0.46</td><td>0.26</td><td>0.55</td><td>0.48</td><td>1.75</td></tr><tr><td>Prof. staff</td><td>p-9</td><td>0.71</td><td>0.13</td><td>0.55</td><td>0.32</td><td>1.71</td></tr><tr><td>Admin. assist</td><td>p-12</td><td>0.01</td><td>1.00</td><td>0.15</td><td>0.32</td><td>1.48</td></tr><tr><td>Clerical union</td><td>p-10</td><td>0.42</td><td>0.03</td><td>0.55</td><td>0.44</td><td>1.44</td></tr><tr><td>Prof. staff</td><td>p-8</td><td>0.37</td><td>0.36</td><td>0.05</td><td>0.48</td><td>1.26</td></tr><tr><td>Prof. staff</td><td>p-2</td><td>0.31</td><td>0.21</td><td>0.25</td><td>0.20</td><td>0.97</td></tr><tr><td>Prof. staff</td><td>p-15</td><td>0.36</td><td>0.15</td><td>0.00</td><td>0.28</td><td>0.79</td></tr><tr><td>Clerical union</td><td>p-18</td><td>0.32</td><td>0.28</td><td>0.00</td><td>0.04</td><td>0.64</td></tr><tr><td>Prof. staff</td><td>p-4</td><td>0.34</td><td>0.08</td><td>0.05</td><td>0.16</td><td>0.63</td></tr><tr><td>Clerical union</td><td>p-21</td><td>0.29</td><td>0.03</td><td>0.05</td><td>0.12</td><td>0.49</td></tr><tr><td>Prof. staff</td><td>p-1</td><td>0.33</td><td>0.03</td><td>0.00</td><td>0.04</td><td>0.40</td></tr><tr><td>Clerical union</td><td>p-7</td><td>0.16</td><td>0.13</td><td>0.00</td><td>0.04</td><td>0.33</td></tr><tr><td>Clerical union</td><td>p-19</td><td>0.23</td><td>0.03</td><td>0.00</td><td>0.04</td><td>0.30</td></tr><tr><td>Prof. staff</td><td>p-14</td><td>0.22</td><td>0.03</td><td>0.00</td><td>0.00</td><td>0.25</td></tr><tr><td>Clerical union</td><td>p-11</td><td>0.20</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.20</td></tr><tr><td>Clerical union</td><td>p-16</td><td>0.13</td><td>0.00</td><td>0.05</td><td>0.00</td><td>0.18</td></tr><tr><td>Prof. staff</td><td>p-13</td><td>0.12</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.12</td></tr><tr><td>Clerical union</td><td>p-3</td><td>0.11</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.11</td></tr><tr><td colspan="7">Information systems</td></tr><tr><td>Personal files</td><td>Files</td><td>0.28</td><td>1.00</td><td>0.81</td><td>1.00</td><td>3.09</td></tr><tr><td>Manual DB</td><td>DB1m</td><td>0.53</td><td>0.30</td><td>1.00</td><td>0.63</td><td>2.45</td></tr><tr><td>Electronic DB</td><td>DB2</td><td>1.00</td><td>0.30</td><td>0.24</td><td>0.00</td><td>1.54</td></tr><tr><td>Desk computer</td><td>PC2</td><td>0.21</td><td>0.00</td><td>0.48</td><td>0.38</td><td>1.07</td></tr><tr><td>Electronic DB</td><td>DB3</td><td>0.78</td><td>0.00</td><td>0.24</td><td>0.00</td><td>1.02</td></tr><tr><td>Electronic DB</td><td>DB1</td><td>0.98</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.98</td></tr><tr><td>Office computers</td><td>PC1</td><td>0.13</td><td>0.39</td><td>0.00</td><td>0.00</td><td>0.53</td></tr><tr><td>Training manual</td><td>Manual1</td><td>0.02</td><td>0.03</td><td>0.05</td><td>0.38</td><td>0.47</td></tr><tr><td>Manual DB</td><td>DB2m</td><td>0.46</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.46</td></tr><tr><td>Manual DB</td><td>DB3m</td><td>0.04</td><td>0.00</td><td>0.05</td><td>0.00</td><td>0.09</td></tr><tr><td>Training manual</td><td>Manual2</td><td>0.09</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.09</td></tr><tr><td>Training manual</td><td>Manual3</td><td>0.01</td><td>0.00</td><td>0.00</td><td>0.06</td><td>0.07</td></tr></table>

Notes: All scores greater than 0.75 (more than one standard deviation above the mean) for each category of knowledge are highlighted in bold.

A chi-squared analysis of centrality scores for the information systems produced similar results $p < 0.001$ . These results support the contention that members of organizations are not indifferent about from whom (or what) they retrieve information.

## 4.2.7. Verifying the Results

The results of the first exploratory network study were cross-checked by conducting interviews both before and after data collection. Several members of the organization confirmed that Person no. 20 was a key source of quality information. It was also not surprising that training manuals were hardly used at all because of remarks made in an interview that they were “out of date.” On the other hand, some managers were largely unaware of the loci of knowledge within the department (which was only twenty-one persons), thus demonstrating the need for the network survey. Another surprise concerned the defensiveness of one senior manager whose relative centrality rankings were low. This reaction demonstrates the power of the technique and the tendency for managers to have distorted perceptions of themselves or others in the organization. It also reinforces the need to exercise care in preserving confidentiality when presenting results.

Table 3 Comparison of Observed Retrieval Scores among Members to Mean Score Expected under Assumption of Uniform Distribution of Knowledge

<table><tr><td>Type of knowledge</td><td>Range of observed scores</td><td>Mean score (uniform distribution)</td><td>Chi-squared</td><td>p value</td><td>df</td></tr><tr><td>Services</td><td>1–100</td><td>35.2</td><td>339</td><td>&lt; 0.001</td><td>20</td></tr><tr><td>Administration</td><td>0–39</td><td>8.1</td><td>312</td><td>&lt; 0.001</td><td>20</td></tr><tr><td>History*</td><td>0–20</td><td>4.0</td><td>190</td><td>&lt; 0.001</td><td>20</td></tr><tr><td>Norms</td><td>0–25</td><td>6.6</td><td>176</td><td>&lt; 0.001</td><td>20</td></tr><tr><td>All knowledge</td><td>11–159</td><td>54</td><td>605</td><td>&lt; 0.001</td><td>20</td></tr></table>

\*Chi-squared test for historical knowledge may not be valid due to low mean scores.

## 4.3. Validating the Method at a Second Field Site

To ensure the efficacy and efficiency of the method, it was applied to a second field site, again as part of a larger study [27]. These results are described briefly here. The second site was a small management consulting firm that provided expertise in human resources planning, QWL (Quality of Working Life), strategic planning and other areas of management consulting. The company was approximately the same size ( $n = 19$ ) as the first site and included five principals, six support staff, and eight project consulting staff. Project consultants were hired on a part-time basis, the population consisting of graduate business students at a local university. The typical project consultant worked for one to two years. The average staff worker's tenure in the organization was 2.2 years and the average tenure for principals was 10 years. Information systems consisted of paper files, books, and a dozen personal computers distributed throughout the offices that were not networked. There were no shared database systems. The main problem in this case was to show that most of the expertise of the firm was contained in the minds of a few principals who traveled frequently, and that the firm was weakly supported by information technology. It was hoped that the results of the study would motivate the development of information systems to make the core knowledge more widely available. As in the previous case, expertise was identified for four major types of knowledge: services, administration, history, and norms. Services were defined as being theory-based or practice-based:

\- Theoretical Aspects of Project Consulting—techno-scientific knowledge, management theory, motivation theory, group process, etc.

\- Practical Aspects of Project Consulting—team management, client relations, etc.

The other categories were defined as in the previous case.

The questionnaire administered to the consulting group was similar to the one used at the library, with minor changes. The only modifications were in the names of personnel, the listings of organization files and information systems, and the definition of services. A two-hour interview was conducted with one of the principals to make the appropriate adjustments to the questionnaires and no other interviews were necessary. The respondents reported that it took only one to two minutes to complete the network portion of the questionnaire (seven network questions on information transmission, retrieval, communication, and reporting) and ten to twelve minutes to fill out a standard questionnaire on other issues for a total of ten to fifteen minutes. This result demonstrated that data could be collected without incurring heavy costs in terms of staff time. Furthermore, the manager of this second site and several other members of the organization said that responding to the questionnaire was a valuable “learning experience.” The response rate was better than 90 percent.

In brief, the analysis showed that members were specialized according to information type. The member with the highest overall centrality score was a member of staff. Retrievals regarding administrative matters for this person alone were greater than total retrievals for any other person in the organization. Members depended on this individual for information concerning norms and history as well.

The second most central member was a senior principal and all types of information were retrieved from this individual. The member with the third highest centrality score was a member of staff and was consulted most often regarding administrative matters and rules and norms. The remaining principals were central to the organization for knowledge about services. The bottom half of the distribution was populated with project consultants, the organization's temporary part-time work force. The organization's memory was clearly a function of its five principals and a few staff members.

Information systems support was much less important at the management consulting firm than the research library based on overall retrieval rates. The centrality scores for documented sources revealed that paper work files were the most important sources of information regarding administrative matters and services. Personal work files were most frequently consulted about services. Workgroup files (e.g., current and past project files) were ranked next most important. Personal computers (distributed but not networked) were frequently used to retrieve information regarding administrative matters. Historical information was retrieved from files and PCs. Documented sources did not support the retrieval of information concerning company rules and norms.

The application of the method to the second field site verified that the method could be applied in a cost-efficient manner. The network questionnaire was constructed with modest input from the researcher's liaison at the site. The survey took a few minutes of each member's time to complete. Once tabulated, key sources of expertise were identified without having to conduct interviews. The limited use of information technology was validated.

## 5. Implications and Conclusions

## 5.1. Other Avenues of MIS Research Using Network Analysis

ALTHOUGH IT IS BEYOND THE SCOPE OF this paper, it is worth noting that the network retrieval data can be used to test various hypotheses about information patterns in organizational settings. For example, one can ask: To what extent did organization members rely on their peers for knowledge to support problem solving and decision making or on documented sources of knowledge? The null hypothesis is that members of organizations retrieve information from their peers as often as from documents. If an organization is very supportive of the use of information technologies, one would expect that retrievals from documents would exceed retrievals from the members. We could test the hypothesis that members of an organization with substantial commitment to information technology depend on documented sources of information more than on their peers for problem solving and decision making.

Another interesting hypothesis concerns the relationship between expertise (as measured by centrality) and other variables. Conventional wisdom indicates that expertise develops as a function of time. If that is the case, then the more senior members of the organization (the organization's institutional memory), will be the most frequently cited experts. Therefore, we could test the hypothesis that expertise is positively correlated with organizational experience. In the first study discussed in this paper, the most frequently retrieved from individual in the organization was not the most experienced individual in the organization. On the other hand, experience seemed to count for something: the correlation between retrieval and years in the organization was 0.672 ( $R^{2} = 0.452$ ). Thus, another area of future research would be to explore this relationship in other organizations, as well as to look at the relationship between retrieval rates and other independent variables such as position, education level, accessibility, and so on.

Network analysis can also be useful to MIS professionals working in areas other than knowledge engineering. For example, network analysis can reveal much about processes of information transmission and retrieval, and the informal communication structures that guide and constrain patterns of information use within organizations. Maps of information exchanges within an organization may be extremely useful in the design and development of office systems, group decision support systems, and communications networks.

## 5.2. Conclusion

In conclusion, network analysis can help the knowledge engineer and managers identify candidates for knowledge acquisition, an important issue according to McDermott [19].

Instead of focusing on variables intrinsic to the individual, experts can be identified based on their centrality as information providers within the organization. Centrality is measured by computing the frequency-scaled indegree scores of individuals and documented sources of knowledge. Experts are identified by ranking centrality scores. The knowledge engineer thus has a new method for profiling the knowledge base of an organization, one that can identify human expertise as well as documented knowledge. Given that current practice in this area is essentially ad hoc, it is believed that this work provides a valuable contribution to current methodology in knowledge engineering.

## NOTES

1. Computer programs and algorithms are available today to do much of the tedious work associated with the method. The reader is referred to Rogers and Kincaid [25] or Richards and Rice [24] for a description of Richards' NEGOPY algorithm, Burt [3] for a description of his STRUCTURE program, or Freeman et al. [6] for a description of UCINET.

2. It is best to assume that managers and employees are equal in their abilities to identify expertise. However, the method allows the knowledge engineer to weight responses from particular individuals within or external to the organization if necessary.

3. It should be noted that this choice of axes is not in keeping with standard convention in the United States. Ego's are usually listed down the page in the first column and alters across the page. However, this break with convention may be pursued because it enables the researcher to utilize the spreadsheet more effectively. It is also easier to read down the page than across several sheets when the list of alters exceeds the list of egos.

4. When building an expert system, the domain of knowledge is likely to be known with great specificity. In other instances, it may be desirable to profile more general categories of organizational knowledge, as is the case here. Either way, the method remains the same.

5. This paper does not suggest that scores on one dimension can be simply added to scores on other dimensions. However, high scores across several types of knowledge suggest broad-based expertise or influence in the organization. The total score helps identify these individuals.

## REFERENCES

1. Alba, Richard D. Taking stock of network analysis. Research in the Sociology of Organizations, 1 (1982), 39–74.

2. Buchanan, Bruce G.; Barstow, David; Bechtal, Robert; Bennett, James; Clancy, William; Kulikowski, Casimir; Mitchell, Tom; and Waterman, Donald A. Constructing an expert system. In Hayes-Roth et al. (cds.), Building Expert Systems, vol. 1. Reading, MA: Addison-Wesley, 1983, 127–167.

3. Burt, Ronald S. Structure (3.2). New York: Center for the Social Sciences, Columbia University, 1987.

4. Burt, Ronald S., et al. Applied Network Analysis: A Methodological Introduction. Beverly Hills, CA: Sage Publications, 1983.

5. Feigenbaum, Edward A., and McCorduck, Pamela. The Fifth Generation: Artificial Intelligence and Japan's Computer Challenge to the World. Reading, MA: Addison-Wesley, 1983.

6. Freeman, Linton, et al. UCINET Manual. Irvine: University of California, 1987.

7. Greenhaus, Jeffrey H.; Parasuraman, Saroj; and Wormley, Wayne M. Effects of race on organizational experiences, job performance evaluations, and career outcomes. Academy of Management Journal, 33, 1 (March 1990), 64–86.

8. Hage, Per, and Harary, Frank. Structural Models in Anthropology. New York: Cambridge University Press, 1983.

9. Harary, Frank; Norman, Robert Z.; and Cartwright, Dorwin. Structural Models: An

Introduction to the Theory of Directed Graphs. New York: John Wiley, 1965.

10. Harmon, Paul, and King, David. Expert Systems. New York: John Wiley, 1985.

11. Hayes-Roth, Frederick; Waterman, Donald A.; and Lenat, Douglas B., eds. Building Expert Systems, vol. 1. Reading, MA: Addison-Wesley, 1983.

12. Heneman, Robert L.; Greenberger, David B.; and Anonyuo, Chigozie. Attributions and exchanges: the effects of interpersonal factors on the diagnosis of employee performance. Academy of Management Journal, 32, 2 (1989), 466–476.

13. Klaas, Brien S., and DeNisi, Angelo, S. Managerial reactions to employee dissent: the impact of grievance activity on performance ratings. Academy of Management Journal, 32, 4 (1989), 705–717.

14. Knoke, David, and Kuklinski, James H. Network Analysis. Beverly Hills, CA: Sage Publications, 1982.

15. Keller, Robert. Expert Systems Technology. Englewood Cliffs, NJ: Yourdon Press (Prentice-Hall), 1987.

16. Krebs, Valdis E. Planning for information effectiveness. Unpublished paper, August 1988.

17. Lincoln, James R. Intra- (and inter-) organizational networks. Research in the Sociology of Organizations, 1 (1982), 1–38.

18. Lorrain, François, and White, Harrison C. Structural equivalence of individuals in social networks. Journal of Mathematical Sociology, 1 (1971), 49–80.

19. McDermott, J. Building expert systems. In Walter Reitman (ed.), Artificial Intelligence Applications for Business. Norwood, NJ: Ablex Publishing, 1984, 13.

20. Mockler, Robert J. Knowledge-based Systems for Management Decisions. Englewood Cliffs, NJ: Prentice-Hall, 1989.

21. Moreno, J.L. Who Shall Survive? Washington, DC: Nervous and Mental Disease Publishing, 1934.

22. Prerau, David S. Selection of an appropriate domain for an expert system. AI Magazine, 4, 2 (1985), 26–30.

23. Prerau, David S. Knowledge acquisition in the development of a large expert system. AI Magazine, 8, 2 (Summer 1987), 43–51.

24. Richards, William D., and Rice, Ronald E. The NEGOPY network analysis program. Social Networks, 3 (1981), 215–223.

25. Rogers, Everett M., and Kincaid, D. Lawrence. Communication Networks: Toward a New Paradigm of Work. New York: Free Press, 1981.

26. Simon, Herbert. Administrative Behavior. New York: Free Press, 1957.

27. Stein, Eric W. Organizational memory: socio-technical framework and empirical research. Ph.D. dissertation, The University of Pennsylvania, 1989.

28. Turban, Efraim. Decision Support and Expert Systems, 2d ed. New York: Macmillan, 1990.

29. Waterman, Donald A. A Guide to Expert Systems. Reading, MA: Addison-Wesley, 1986.

30. Wayne, Sandy J., and Kacmar, Michele K. The effects of impression management on the performance appraisal process. Organizational Behavior and Human Decision Processes, 48 (1991), 70–88.

## APPENDIX 1: Analyzing Network Data

SYSTEM-LEVEL INDICES ARE COMPUTED AS FOLLOWS. Size is defined as the number of actors, N, in a network. The number of links is found by counting the number of entries in the network matrix. In studies in which respondents indicate interaction according to frequency, total network interaction can be computed by summing the strength of each link across the network. The data may be converted to flows of information sent, received, or exchanged per unit time if the relation profiled relates to information exchange. The density of a network (connectedness) is the number of actual direct links recorded between actors in a network divided by the possible number of such links given as N (N-1), where N stands for the number of individuals in the network. $^{1}$ Reachability and connectivity can be determined by measuring the path distances across the network. Path distances indicate the arrangement of the members of the network in addition to the absence or presence of links. If two people say they communicate, then they record a path distance of one. However, sometimes people are able to reach others through mutual acquaintances. Information that must travel two or more path lengths to reach a destination is considered an indirect link. Radial networks have shorter path distances between any two individuals than circular networks. Path distance across an entire network can be determined using matrix multiplication techniques. By squaring a binary form of the communication matrix, two-step links are revealed; cubing the same network reveals three-step links, etc. The reader is referred to Harary et al. [9] for a complete description of the techniques for computing path distances in matrices.

Detecting cliques is another use of network analysis. Communication cliques are identified as groups of individuals that tend to share information and have more extensive in-group communication than out-group communication $[15]$ . Cliques can be detected based on measures of communication proximity $[25]$ . Individuals who are “near” one another in the communication sense have overlapping personal networks, sharing many of the same direct and indirect links. $^{2}$ There are several criteria for identifying cliques. In brief, criteria are based either on graph theory measures or measures of structural equivalence. Graph theory measures are the most stringent. “The most restrictive and formal definition of a clique is a maximal complete subgraph, a set of completely linked points not contained within a larger, completely linked set” $[15, p. 56]$ . This criterion was later relaxed to the maximal strong component. Other criteria include n-cliques and k-cliques. The reader is referred to $[9]$ and $[8]$ for more extensive treatment of these graph theoretic notions of proximity. Another criterion for classifying cliques is based on the notion of structural equivalence. Two individuals are structurally equivalent if they have “a common set of linkages to other system actors” $[15, p. 59]$ , or are substitutable $[18]$ . Structural equivalence is the measure used in Burt’s STRUCTURE program $[3]$ based on an algorithm developed by Johnson. Another approach to detecting cliques is offered by Richards’s NEGOPY program using matrix manipulation methods (see $[24, 25]$ ). The reader is referred to $[15]$ for a complete description of the various types.

The most important individual measure is centrality. Centrality may be measured three ways in terms of degree, distance (closeness), and betweenness according to Hage and Harary [8]. Degree centrality is discussed in the text. The two other ways to measure centrality are based on the notions of distance and betweenness. Distance centrality refers to the sum of the shortest paths between a node and all other nodes in a network and is interpreted in terms of “communication efficiency” [8]. The advantage of this measure of centrality is that it considers indirect links as well as direct links between a node and other nodes. Betweenness centrality refers to the frequency of occurrence of a node between all pairs of other nodes and is interpreted as the “potential for control of communications.” Individuals with high betweenness scores are believed to mediate communication flows in networks.

## Notes

1. This is the expression for asymmetrical communications, such as retrieval or transmission. The expression for symmetric relations (e.g., “With whom do you communicate?”) is one-half this amount or $N(N-1)/2$ .

2. Direct links represent admitted lines of communication between individuals, that is, a direct link is simply the absence or presence of a relation. Indirect links are communication paths through connecting individuals, that is, mutual colleagues.

<table><tr><td colspan="6">Network Survey of a Management Consulting Organization</td></tr><tr><td colspan="6">I am interested in the process of information retrieval from files or from organization members for the purposes of making decisions, accomplishing tasks, or solving problems.For each question, indicate frequency of interaction below.</td></tr><tr><td>LESS THAN EVERY 2 WKS</td><td>ONCE EVERY TWO WEEKS</td><td>ABOUT ONCE PER WEEK</td><td>A FEW TIMES PER WEEK</td><td>ABOUT ONCE PER DAY</td><td>MORE THAN ONCE /DAY</td></tr><tr><td>0</td><td>0.5</td><td>1</td><td>3</td><td>5</td><td>0</td></tr><tr><td colspan="6">Q.1 From whom do you retrieve information about the Practical Aspects of Consulting Services?</td></tr><tr><td>Name</td><td colspan="5">Answer</td></tr><tr><td>John Smith</td><td colspan="5">—</td></tr><tr><td>Sally Johnson</td><td colspan="5">—</td></tr><tr><td>Bill Tims</td><td>—</td><td colspan="4">etc....</td></tr><tr><td colspan="6">Q.2 From which files, databases, computers do you retrieve information about the Practical Aspects of Consulting?</td></tr><tr><td>Answer</td><td>Resource Name</td><td>Location</td><td colspan="3">Description/Contents</td></tr><tr><td>—</td><td>Active Work Files</td><td>staff offices</td><td colspan="3">project notes</td></tr><tr><td>—</td><td>REFERENCE FILES:</td><td></td><td colspan="3"></td></tr><tr><td></td><td>Center Author</td><td>near photocopier</td><td colspan="3">manuscripts, article</td></tr><tr><td></td><td>Center Marketing</td><td>near photocopier</td><td colspan="3">CV&#x27;s, resumes</td></tr><tr><td></td><td>Center Proposal</td><td>near photocopier</td><td colspan="3">current and aged</td></tr><tr><td>—</td><td>Slide Presentation files</td><td>John&#x27;s office</td><td colspan="3">executive education</td></tr><tr><td>—</td><td>Center Financial files</td><td>Sam&#x27;s office</td><td colspan="3"></td></tr><tr><td>—</td><td>REFERENCE FILES:</td><td></td><td colspan="3"></td></tr><tr><td></td><td>Subject files</td><td>storage room</td><td colspan="3"></td></tr><tr><td></td><td>Author files</td><td>storage room</td><td colspan="3"></td></tr><tr><td>—</td><td>Technical library</td><td>hall shelves</td><td colspan="3">management theory</td></tr><tr><td>—</td><td>Diskette library</td><td>computer room</td><td colspan="3">work information</td></tr><tr><td>—</td><td>Computers (PC&#x27;s)</td><td>computer room</td><td colspan="3">work information</td></tr><tr><td>—</td><td>Computers (PC&#x27;s)</td><td>each office</td><td colspan="3">work information</td></tr><tr><td>—</td><td>Personal files</td><td>each office</td><td colspan="3">work information</td></tr><tr><td>OTHER:</td><td></td><td></td><td colspan="3"></td></tr><tr><td>—</td><td>—</td><td>—</td><td colspan="3">—</td></tr></table>
