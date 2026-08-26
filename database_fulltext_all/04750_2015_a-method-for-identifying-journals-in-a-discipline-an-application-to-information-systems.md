---
otero_id: 4750
otero_key: "BHTZJBD8"
title: "A method for identifying journals in a discipline: An application to information systems"
authors: "Hock Chuan Chan; Varsha Guness; Hee-Woong Kim"
year: "2015"
journal: "Information & Management"
doi: "10.1016/j.im.2014.11.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A method for identifying journals in a discipline: An application to information systems

Hock Chuan Chan <sup>a</sup>, Varsha Guness <sup>a</sup>, Hee-Woong Kim <sup>b,</sup>\*

<sup>a</sup> Department of Information Systems, National University of Singapore, 13 Computing Drive, Singapore 117417, Republic of Singapore <sup>b</sup> Graduate School of Information, Yonsei University, 50 Yonsei-ro, Seodaemun-gu, Seoul 120-749, Republic of Korea

## A R T I C L E I N F O

Article history: Received 18 October 2013 Received in revised form 17 October 2014 Accepted 12 November 2014 Available online 4 December 2014

Keywords: IS journals AIS basket of journals Journal citation reports Method

## A B S T R A C T

It is a perennial interest of the information systems community to identify a set of information systems journals. The primary approaches to achieving this identification are surveys of academics, article-level citation, and senior scholar consensus. An example of the last approach is the basket of eight journals identified by senior scholars of the Association for Information Systems (AIS). A different and efficient approach is afforded by the publication of data from Journal Citation Reports (JCR). This provides aggregate citation data across individual journals. While the findings provide general empirical support for the choice of the AIS basket of eight journals, they also indicate that five additional journals qualify as core information systems journals. Each of these journals has numerous citations of journals within this set and low citations of individual journals outside this set. Furthermore, a network centrality analysis of this set of journals reveals a high correlation between in-degree centrality and the perceived importance of journals. Overall, the study demonstrates the suitability of this method for identifying core journals in a discipline.

\- 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

There is a perennial interest among the information systems (IS) community in identifying a set of IS journals [29]. Having a commonly agreed set of journals can serve as a guide for where to publish our research [22,23]. It can also serve to increase submissions to the journals. A commonly employed approach to identifying a set of journals is the opinion survey method, whereby IS academics are asked to rank journals based the journal’s emphasis, its value and significance to the IS field. An example is the study by Walstrom and Hardgrave [32], which asked IS faculties in the US and Canada for their perceptions of the discipline emphasis of 51 identified journals. This approach has also been applied in other studies [3,24,25,33,34]. Data collected through such surveys are primarily a reflection of the participants’ perceptions of the journals. Thus, the survey approach may be affected by the subjective views of the participants [24] and by inherent measurement biases [7]. Furthermore, individual notions of the IS discipline differ, and there are no clear objective boundaries to identify which journals are purely IS, partially IS or non-IS. Another approach is adopted by the Association for Information Systems (AIS), in which the association’s senior scholar consortium agreed on a set of eight IS journals. This is also a subjective identification, based on AIS members who are deeply engaged in the publication selection process, e.g., as editors-in-chief, or conference and track chairs.

The primary objective of this study is in developing an objective method to identify a set of core journals for any discipline. This method is applied to identify a set of IS journals by developing and applying an objective empirical method. The proposed method can be used to validate the set of journals identified through the subjective processes, e.g., by a survey of general IS academics or by agreement among senior IS scholars. In particular, we examine citation behavior across journals. This is an aggregation of the behaviors of individual IS academics as manifested in their research references. The use of citation analysis is noteworthy and is purported to be more objective than using respondent perceptions [28]. We assume that if an IS journal cites ‘‘substantially’’ from another journal, then the other journal is also an IS journal. Culnan and Swanson [8] reported that, on average, a publication in a discipline will cite more from its own discipline than from those from another discipline. In a more general context, if a journal cites ‘‘substantially’’ from another journal, then both journals belong to the same discipline. The application of JCR data, available from the Journal Citation Reports (JCR), has the potential to track changes in the citation relationship between journals.

The identification process begins with the basket of 8 journals (J8) recommended by the AIS senior scholars<sup>1</sup>. This set is used to estimate a level representing ‘‘substantial’’ citation numbers for citations within a discipline. The set of journals is expanded by considering journals published in other studies, e.g., that by Walstrom and Hardgrave [32]. Following their classifications of pure IS, hybrid IS and non-IS journals, we use citation behavior to confirm and reclassify the journals according to these categories. Through this process, we obtain an expanded set of IS journals (JExp) that show high citation behavior within the set and low citations of individual journals outside the set.

In addition, we compare the network centrality values of journals from JExp with their respective subjective journal ratings as published in Walstrom and Hardgrave [31], Whitman et al. [34], and Peffers and Tang [25]. The analysis reveals that network centrality has strong and significant correlations with subjective perceptions of journal quality.

## 2. Literature review

The identification of IS journals is one of the fundamental issues in studies of IS journals. For example, in the study of journal quality by Lowry et al. [23], the first issue is the identification of IS journals. A number of studies have attempted to identify and classify IS research journals. To support their studies, measures such as citation analysis and gathering perceptions from a sampled group of researchers were the most commonly employed approaches. Some of the earlier studies that used citations include Hamilton and Ives [15], Vogel and Wetherbe [30], Cooper et al. [7], and Holsapple et al. [19]. Hamilton and Ives [15] analyzed the number of references in 15 journals that publish IS research (1970–1979) to identify major journal sources of information for IS researchers. Vogel and Wetherbe [30] used citation-based methods to evaluate IS research outlets to determine the preferences among journals regarding the publication of IS research. Cooper et al. [7] analyzed citation patterns across 14 journals to provide insights into the influence of journals in communicating IS research. Holsapple et al. [19] performed citation-based studies to determine the relative importance of journals used by academics for research and scholarly discourse and to the business computing field.

Studies that adopted a subjective approach, e.g., surveys of academics, include Doke and Luke [10], Gillenson and Stutz [14], Whitman et al. [34], Walstrom et al. [31], Hardgrave and Walstrom [17], Walstrom and Hardgrave [32], and Peffers and Tang [25]. Doke and Luke [10] reported a survey of business school deans’ ratings of the top 10 IS journals. Walstrom and Hardgrave [32] reported a series of studies to determine the appropriateness of various journal outlets for IS publication. Whitman et al. [34] conducted a nationwide survey in which participants were asked to rate 80 publications with respect to their value in reviews of research and performance. Similarly, Peffers and Tang [25] used a survey instrument and asked researchers to rate the value of IS publication outlets and categorize them into IS journals and other allied disciplines. Because IS is multidisciplinary, many IS research works appear in traditionally non-IS journals. Polites and Watson [27] adopted the IS classification from prior studies and analyzed citation behavior regarding journals from other disciplines.

Walstrom and Hardgrave’s [32] journal category list was derived based on a questionnaire survey sent to a group of research scholars. Respondents were asked to indicate whether a journal primarily published IS research. All of the responses (scores) were averaged, and based on the results, journals figuring in the top 75% were categorized as ‘Pure’ IS journals; the next break was set at 0.5, and journals within this range was classified in the ‘Hybrid’ IS journal category; ‘Partial’ IS journals were those falling into the next range, with a lower bound at 0.25; and finally, journals having a score below 0.25 were categorized as ‘Non-IS journals.

Although all of the above approaches contribute to the categorization of IS journals, they also have limitations. Regarding the citation pattern analysis approach, as the number of journals has increased over time, it has become increasingly difficult to perform citation studies for all of them. Thus, researchers have to limit themselves to a set of pre-selected journals from which they collect citation numbers. However, there is a growing concern regarding subjectivity involved in the surveys. Different sample populations will likely lead to different outcomes.

With the comprehensive journal citation data available from JCR, it is now possible to conduct an analysis using complete datasets and to compare the results with the journal classification obtained from the survey approach. Studying the journals’ citation behavior allows us to observe the knowledge transfer process that occurred across journals [29]. The details of the analysis are provided in the following sections.

The identification of IS journals is quite different from the determination of journal quality, which is also highly important for a discipline [9]. According to Straub and Anderson [29], citationbased metrics have become the ‘‘preferred means of assessing journal quality’’, although they may not be the best. For example, Katerattanakul and Han [20] used citations at the article level to derive journal quality measures. A typical objective measure of journal quality is the impact factor. Journal quality could also be measured through a subjective survey, and such an evaluation could be based on evaluations of journal, editor and publisher characteristics [12]. In the study by Lowry et al. [23], a weighted combination of various factors was used to group journals by quality. In the analysis section, we conduct a correlation analysis of citation behavior and subjective perceptions of journal quality.

## 3. Research methodology

## 3.1. Data collection

First, the citation numbers for each journal are gathered from the Thompson Reuters (formerly ISI) Web of Knowledge’s JCR. A JCR contains citation data from one journal to another journal and from one journal to all other journals. It also has data in the opposite directions. Data from ‘‘all years’’ up to 2012 are used to provide a complete picture. Future studies could consider a ‘‘time series’’ view of the citation behavior.

We begin with the AIS Journal Basket (J8). The journals are: European Journal of Information Systems (EJIS), Information Systems Journal (ISJ), Information Systems Research (ISR), Journal of the AIS (JAIS), Journal of Information Technology (JIT), Journal of Management Information Systems (JMIS), Journal of Strategic Information Systems (JSIS), and MIS Quarterly (MISQ). We identify the citation pattern among the J8 set of journals, the citation numbers, specifically the ‘Citing’ values from the ISI Web of Knowledge’s Journal Citation Reports, and the total citation number for the target journal from its beginning until 2012. Citing journal numbers indicate the number of times that one journal cites another. For example, if the citing value from

Information Systems Research to MIS Quarterly is 227, this means that Information Systems Research cites MIS Quarterly 227 times.

We consider what percentage of the citations (%-citations) are from within the J8 journals. For example, a sample data collection for the Information & Management (IM) journal reveals that IM cites all journals 920 times and, of these, 178 citations are made to the J8 journals. The %-citation for IM is 19.3% (178/920). Using the %- citations numbers as a guide, we extend the analysis to all of the journals in Walstrom and Hardgrave [32]. Note that only the journals indexed by the JCR were considered.

## 3.2. AIS journal basket %-citation results

The steps for calculating the %-citation value are outlined below.

(a) We gather the number of citations made from a selected journal to ‘all journals’ from JCR.

(b) We collect the number of citations made from the selected journal to the 8 journals in the AIS Journal Basket (excluding self-citations). Because the focus is on citation relationships between journals, self-citation is excluded, as it does not represent a relationship with another journal. However, selfcitation plays a role when we consider citations to IS journals because self-citations are also citations to IS journals once the journal is classified as an IS journal. To allow a more detailed understanding, we have provided the analysis including selfcitation data in Appendix 1

(c) We sum the citation values of the 8 journals to determine the total number of citations made from the selected journal to the 8 AIS journals.

(d) We now have the total number of citations made from the selected journal to all journals and the total number of citations made from the selected journal to the AIS journals.

(e) Based on these 2 values, we compute the %-citation as follows: [(c)/(a)]

Sample %-citation calculation:

\- MISQ cites all journals 4822 times.

\- MISQ cites the 8 journals in J8 428 times, excluding self-citations to MISQ.

\- Therefore, the citations made from MISQ to J8 as a percentage of the total citations made to all journals is: [428/4822] = 8.9%.

Table 1 reports the %-citation numbers for the J8 journals. The values range from 8.8% to 21.5%, with JAIS having the highest %-citation value of 21.5% and ISR having the lowest %-citation of 8.8%. To derive a citation index that mirrors the citation pattern of pure IS journals, the minimum %-citation value, 8.8%, is used as a threshold. This value provides an approximation of the %-citations that flow among pure IS journals and serves as a threshold to segregate pure IS journals from others.

Table 1  
Citations of the AIS set of 8 journals.

<table><tr><td>Citing journal</td><td>To all journals</td><td>To J8 journals (exclude self-citation)</td><td>%-Citation</td></tr><tr><td>ISR</td><td>4568</td><td>403</td><td>8.8</td></tr><tr><td>MISQ</td><td>4822</td><td>428</td><td>8.9</td></tr><tr><td>JMIS</td><td>2156</td><td>293</td><td>13.6</td></tr><tr><td>JIT</td><td>1696</td><td>258</td><td>15.2</td></tr><tr><td>ISJ</td><td>1243</td><td>190</td><td>15.3</td></tr><tr><td>JSIS</td><td>1909</td><td>317</td><td>16.6</td></tr><tr><td>EJIS</td><td>3037</td><td>534</td><td>17.6</td></tr><tr><td>JAIS</td><td>2228</td><td>478</td><td>21.5</td></tr></table>

Note: European Journal of Information Systems (EJIS), Information Systems Journal (ISJ), Information Systems Research (ISR), Journal of Association for Information Systems (JAIS), Journal of Information Technology (JIT), Journal of Management Information Systems (JMIS), Journal of Strategic Information Systems (JSIS), and MIS Quarterly (MIQ).

## 3.3. Journal classification

We apply the %-citations to classify the journals from Walstrom and Hardgrave [32]. From the previous section’s data analysis, we adopt a rule to identify the set of pure IS journals: each journal should have more than an 8.8%-citation value from the J8 set.

The %-citation value (based on the total number of citations made to J8) was calculated for all the journals from Walstrom and Hardgrave [32]. Five journals have a %-citation value of 8.8% and above. They are Information & Management, Journal of Global Information Management, Information Systems Management, Journal of Computer Information Systems, and DATA BASE for Advances in Information Systems. Therefore, the pure IS journals form an expanded set of 13 journals (JExp).

Next, we consider the hybrid IS, partial IS and non-IS journals in the lists compiled by Walstrom and Hardgrave [32]. For simplicity, we included the partial IS journals in the hybrid list. For this hybrid list, the median %-citation value is 0.8%. The non-IS journals have %-citation numbers that are close to 0.8%. That is, in the Walstrom and Hardgrave lists, there is no clear distinction between the hybrid and non-IS lists with respect to %-citation numbers. Therefore, using the median of 0.8% of the hybrid list, we reorganize the journals into hybrid-IS (those with at least a 0.8%-citation value from J8 journals) and non-IS (those with less than 0.8% of citations from J8 journals). The new list of hybrid-IS journals includes some journals from the original hybrid list (Journal of Systems and Software, International Journal of Human-Computer Studies, and Decision Sciences) and one from the origina pure-IS list (Decision Support Systems). The new lists of ‘Pure IS’, ‘Hybrid IS’ and ‘Non-IS’ journals are presented in Tables 2–4. We observe a substantial deviation from the lists compiled by Walstrom and Hardgrave [32].

## 4. Centrality analysis

Using the citation behavior connecting the IS journals in a network, we can analyze the correlation between the centrality of a journal in the network and its reported rankings from Walstrom and Hardgrave [32], Whitman et al. [34], and Peffers and Tang [25]. Our main interest is whether centrality correlates with subjective rankings of journal importance.

Table 2  
Citations of pure-IS journals.

<table><tr><td>Pure IS journals (%-citation ≥ 8.8%)</td><td>%-Citation</td><td>W&amp;H category</td></tr><tr><td>Information Systems Research</td><td>8.8</td><td>Pure</td></tr><tr><td>MIS Quarterly</td><td>8.9</td><td>Pure</td></tr><tr><td>Journal of Computer Information Systems</td><td>10.9</td><td>Pure</td></tr><tr><td>Information Systems Management</td><td>11.0</td><td>Pure</td></tr><tr><td>Journal of Global Information Management</td><td>13.1</td><td>Pure</td></tr><tr><td>Journal of Management Information Systems</td><td>13.6</td><td>Pure</td></tr><tr><td>DATA BASE for Advances in Information Systems</td><td>13.8</td><td>Pure</td></tr><tr><td>Journal of Information Technology</td><td>15.2</td><td>-</td></tr><tr><td>Information Systems Journal</td><td>15.3</td><td>-</td></tr><tr><td>Journal of Strategic Information Systems</td><td>16.6</td><td>Pure</td></tr><tr><td>European Journal of Information Systems</td><td>17.6</td><td>Pure</td></tr><tr><td>Information &amp; Management</td><td>19.3</td><td>Pure</td></tr><tr><td>Journal of the Association for Information Systems</td><td>21.5</td><td>-</td></tr></table>

Note: W&H category is the category given by Walstrom and Hardgrave [32].

Table 3  
Citations of hybrid-IS journals.

<table><tr><td>Hybrid journals(0.8% ≤ %-citation &lt; 8.8%)</td><td>%-Citation</td><td>W&amp;H category</td></tr><tr><td>Organization Science</td><td>0.8</td><td>Non-IS</td></tr><tr><td>Management Science</td><td>0.8</td><td>Non-IS</td></tr><tr><td>Journal of System Software</td><td>1.5</td><td>Hybrid</td></tr><tr><td>International Journal of Human Computer Studies</td><td>2.4</td><td>Hybrid</td></tr><tr><td>Decision Sciences</td><td>6.2</td><td>Partial</td></tr><tr><td>Behavior and Information Technology</td><td>6.2</td><td>Hybrid</td></tr><tr><td>Decision Support Systems</td><td>7.3</td><td>Pure</td></tr></table>

Social network analysis has long been applied to study social actors and their network connections [4,16]. It has been used to analyze static connections, such as friendship or work relationships, and flows, such as the flow of information or money over a network [4]. Because citation is a human behavior, social network analysis has also been applied to the behavioral networks formed by journals, articles, authors and citations [5,23,27,29].

In social networks, the centrality of a node in a network is a measure of its structural importance in the complex interaction occurring in the network [13]. There are numerous measures of the centrality of a node [13]. The most common centrality measures are degree centrality, closeness centrality and betweenness centrality [4,16,27]. A few recent studies also used a centrality measure called Bonacich’s Power centrality<sup>2</sup>, which is designed to account for the relative power of neighboring journals [23,27].

For a journal and citation network, a journal’s degree centrality is a measure of the journal’s direct connection to other journals. A degree centrality measure that does not consider the connection weight (i.e., number of citations to/from another journal) will be simply the number of journals directly cited by or citing this journal. Degree centrality can also count the connection weights. This weighted measure is also called Freeman degree centrality [4]. In contrast to degree centrality, which only considers directly related journals, closeness centrality and betweenness centrality are based on the entire network. For example, closeness centrality is an average value of how close a journal is to all the other journals in the network, while betweenness centrality is a measure of the extent to which a journal serves as an intermediary between other journal pairs. Betweenness centrality and closeness centrality will be very important in situations in which information has to travel from a journal to another journal across a network.

Because we consider the pure-IS journals, researchers are likely to have direct access to journals and articles, especially with modern digital libraries and search technology. That is, researchers do not have to proceed from one tie to another tie. Thus, the most important centrality measure to consider regarding a journal’s importance is Freeman degree centrality, the degree centrality that considers the connection weights, i.e., the number of citations. ‘‘Freeman degree is commonly used for determining journal ranking’’ [27, p. 603]. It is also one of the centrality measures used by Lowry et al. [23] and Polites and Watson [27].

Table 4  
Citations of non-IS journals.

<table><tr><td>Non IS journals (%-citation &lt; 0.8%)</td><td>%-Citation</td><td>W&amp;H category</td></tr><tr><td>Harvard Business Review</td><td>0</td><td>Non-IS</td></tr><tr><td>Academy of Management Journal</td><td>0</td><td>Non-IS</td></tr><tr><td>Administrative Science Quarterly</td><td>0</td><td>Non-IS</td></tr><tr><td>Academy of Management Review</td><td>0</td><td>Non-IS</td></tr><tr><td>ACM Transactions on Database Systems</td><td>0</td><td>Hybrid</td></tr><tr><td>IEEE Transactions on Knowledge and Data Engineering</td><td>0</td><td>Hybrid</td></tr><tr><td>INFOR</td><td>0</td><td>Partial</td></tr><tr><td>Interfaces</td><td>0</td><td>Partial</td></tr><tr><td>Operations Research</td><td>0</td><td>Non-IS</td></tr><tr><td>Expert Systems with Applications</td><td>0.01</td><td>Hybrid</td></tr><tr><td>Organizational Behavior</td><td>0.04</td><td>Non-IS</td></tr><tr><td>OMEGA</td><td>0.10</td><td>Non-IS</td></tr><tr><td>ACM Computing Surveys</td><td>0.12</td><td>Hybrid</td></tr><tr><td>Communications of the ACM</td><td>0.60</td><td>Hybrid</td></tr><tr><td>Knowledge Based Systems</td><td>0.70</td><td>Hybrid</td></tr></table>

First, we use in-degree centrality, which measures the incoming citation values toward each node. It is an objective measure of the node’s academic impact or influence [5] and its contribution to other journals. Second, we determine out-degree centrality, in which the outgoing citation values from the nodes are computed. This reveals the frequency with which a journal references other journals in the field, and thus out-degree centrality serves as a measure of the impact of other journals on the target journal.

A correlation analysis is performed to determine the relationship between the centrality values of JExp journals and the journal perception ratings in published studies. The centrality values are calculated for citations within the 13 journals in JExp, excluding self-citations. In Table 5, reporting citations from other journals, the correlations are high (>0.8) and significant (p < 0.01). These results indicate that the perception of a journal is strongly linked to how frequently the journal is cited by JExp.

In Table 6, reporting citations made to other journals, although the correlation coefficients are positive, the p-values (except for that related to Whitman et al. [34]) are all greater than 0.05, indicating that the correlation is not statistically significant. Thus, the perception of a journal is not linked to how frequently the journal cites from JExp. This could be because the citations are more guided by the nature or content of the research.

In summary, when a journal is well perceived, there is substantial citation of the journal. For the first 5 journals, there is an exact match in the rankings from in-coming citation numbers and all of the subjective rankings. In descending order, the first 5 journals are MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Information & Management, and European Journal of Information Systems. Compared with the rankings from Walstrom and Hardgrave [32], there is a nearly perfect match with the rankings based on in-coming citations. In other words, author citation behavior closely follows perceptions of journal prestige.

However, a strong perception of the journal does not mean that the journal articles will make more citations to the JExp list. This may be an indicator of a multidisciplinary field. An additional analysis of the degree centralities with impact factors is reported in Appendix 3. As expected, in-degree centrality is highly correlated with impact factors because impact factors are specialized measures of incoming citations. However, when we compare the impact factor ranking and the subjective rankings, there are numerous substantial mismatches. For example, Journal of Information Technology has a ranking of 2nd place based on impact factors but is ranked 7th based on in-degree centrality.

Table 5  
Journal rating and in-degree centrality (citations from other journals).

<table><tr><td rowspan="2">JExp journal</td><td rowspan="2">In-degree citations</td><td rowspan="2">In-degree centrality</td><td colspan="3">Rating</td></tr><tr><td>Walstrom and Hardgrave [30]</td><td>Whitman et al. [32]</td><td>Peffers and Tang [23]</td></tr><tr><td>MIS Quarterly</td><td>1488</td><td>1.00</td><td>3.76</td><td>4.57</td><td>489.1</td></tr><tr><td>Information Systems Research</td><td>727</td><td>.49</td><td>3.71</td><td>4.13</td><td>418.3</td></tr><tr><td>Journal of Management IS</td><td>471</td><td>.31</td><td>3.42</td><td>3.95</td><td>317.4</td></tr><tr><td>Information &amp; Management</td><td>269</td><td>.18</td><td>2.92</td><td>3.45</td><td>303.8</td></tr><tr><td>European Journal of IS</td><td>268</td><td>.18</td><td>2.79</td><td>N/A</td><td>303.8</td></tr><tr><td>Journal of the Association for IS</td><td>188</td><td>.12</td><td>N/A</td><td>N/A</td><td>184.4</td></tr><tr><td>Journal of Information Technology</td><td>156</td><td>.10</td><td>N/A</td><td>N/A</td><td>68.0</td></tr><tr><td>Information Systems Journal</td><td>139</td><td>.09</td><td>N/A</td><td>3.45</td><td>168</td></tr><tr><td>Journal of Strategic IS</td><td>111</td><td>.07</td><td>2.70</td><td>3.03</td><td>130.2</td></tr><tr><td>DATA BASE for Advances in IS</td><td>66</td><td>.04</td><td>2.64</td><td>3.31</td><td>248.3</td></tr><tr><td>Journal of Computer IS</td><td>39</td><td>.03</td><td>2.66</td><td>3.20</td><td>132.8</td></tr><tr><td>Information Systems Management</td><td>39</td><td>.03</td><td>2.66</td><td>3.1</td><td>68.9</td></tr><tr><td>Journal of Global IM</td><td>27</td><td>.02</td><td>2.52</td><td>N/A</td><td>115.1</td></tr><tr><td></td><td></td><td rowspan="2">Correlation coefficient p-Value</td><td>0.89</td><td>0.94</td><td>0.85</td></tr><tr><td></td><td></td><td>0.001</td><td>0.001</td><td>0.001</td></tr></table>

N/A: journal was not rated in that particular study.

Table 6  
Journal rating and out-degree centrality (citations made to other journals).

<table><tr><td rowspan="2">JExp journal</td><td rowspan="2">Out-degree citations</td><td rowspan="2">Out-degree centrality</td><td colspan="3">Rating</td></tr><tr><td>Walstrom and Hardgrave [30]</td><td>Whitman et al. [32]</td><td>Peffers and Tang [23]</td></tr><tr><td>European Journal of IS</td><td>605</td><td>1.00</td><td>2.79</td><td>N/A</td><td>303.8</td></tr><tr><td>Journal of the Association for IS</td><td>508</td><td>.84</td><td>N/A</td><td>N/A</td><td>184.4</td></tr><tr><td>MIS Quarterly</td><td>480</td><td>.79</td><td>3.76</td><td>4.57</td><td>489.1</td></tr><tr><td>Information Systems Research</td><td>433</td><td>.72</td><td>3.71</td><td>4.13</td><td>418.3</td></tr><tr><td>Journal of Strategic IS</td><td>337</td><td>.56</td><td>2.70</td><td>3.03</td><td>130.2</td></tr><tr><td>Journal of Management IS</td><td>321</td><td>.53</td><td>3.42</td><td>3.95</td><td>317.4</td></tr><tr><td>Journal of Information Technology</td><td>278</td><td>.46</td><td>N/A</td><td>N/A</td><td>68.0</td></tr><tr><td>Information Systems Journal</td><td>216</td><td>.36</td><td>N/A</td><td>3.45</td><td>168</td></tr><tr><td>Journal of Global IM</td><td>220</td><td>.36</td><td>2.52</td><td>N/A</td><td>115.1</td></tr><tr><td>Information &amp; Management</td><td>190</td><td>.31</td><td>2.92</td><td>3.45</td><td>303.8</td></tr><tr><td>Information Systems Management</td><td>169</td><td>.28</td><td>2.66</td><td>3.1</td><td>68.9</td></tr><tr><td>Journal of Computer IS</td><td>137</td><td>.23</td><td>2.66</td><td>3.20</td><td>132.8</td></tr><tr><td>DATA BASE for Advances in IS</td><td>94</td><td>.16</td><td>2.64</td><td>3.31</td><td>248.3</td></tr><tr><td></td><td></td><td>Correlation coefficient</td><td>0.55</td><td>0.78</td><td>0.50</td></tr><tr><td></td><td></td><td>p-Value</td><td>0.10</td><td>0.01</td><td>0.08</td></tr></table>

## 5. Conclusion and future research

## 5.1. Limitations of the study

The approach of classifying the journals and extending the set of AIS journals has certain limitations. The initial set of journals may be crucial. We began with the AIS journal set. Fortunately, the empirical citation data clearly validates this set as a close-knit group of journals and therefore as a suitable starting point. Our findings are based on total citation numbers collated until 2012. A full study could provide a time-series perspective of citation behavior to track any changes over the years. An analysis beginning with a larger set of journals (JExp) is provided in Appendix 2. The results are similar, with no change in the set of IS journals.

Many scholars have criticized the limitations and misuse of JCR’s impact factors as a basis for evaluating journal influence and research papers (e.g., [1,2,18]). These factors include journal size, the measurement window, and the year-to-year impact variability [1]. However, journal citations are objective numbers. To reduce the impact of the measurement window, this study considered raw citation numbers for articles since the journal began publication until 2012. We did not exclusively consider citation numbers for a certain period of time (e.g., 2007–2012). However, we do agree with Laband and Piete [21] that impact variability may be an issue when collecting citations over the years. New journals or journals excluded from the JCR report may suffer from smaller or zero citations compared with the long-established JCR journals. Additionally, the data are exclusively obtained from JCR.

Citation analysis using our approach is a simple and effective means of identifying citation patterns across journals. Previous citation studies employed different approaches to citation analysis. For example Pieters and Baumgartner [26] used log-multiplicative models. This type of model combines the strength of ‘multidimensional scaling’ (geometrical representation) and log-linear analysis (tests of model adequacy). However, although both multidimensional scaling and log-linear analysis have advantages, they also have a disadvantage. The advantage of using multidimensional scaling is that it facilitates the interpretation of multiple relationships between journals, particularly when very large citation networks are explored. In our case, the set of journals is not particularly large and the need for multiple relationships is not a major concern. However, although a log-linear model enables tests of model adequacy, it requires parameters for each pair of journals in the sample, which substantially complicates the interpretation of the results if numerous journals are analyzed. The in-degree centrality index is also a simple but powerful means of identifying prestigious IS journals. The number of citations flowing to a journal does provide a holistic view of the impact of that journal on other journals. Nevertheless, our method purely focused on the citation behavior between journals. In a multidisciplinary analysis, the disciplinary characteristics of each journal could be a relevant factor.

Using this method, a journal that is more specialized may be excluded from the set of IS journals because the percentage citation is likely to be lower. One example is Decision Support Systems. Many more studies applying this method to various disciplines will be needed to identify its limitations and advantages.

## 5.2. Future research

Having identified the set of IS journals (JExp), we can extend this research by making more detailed comparisons with more recent studies. Older lists (from the 1980s and 1990s) may be more difficult to compare because IS research and publications have changed considerably over time. For example, Chan et al. [6] used citations from articles from a conference (i.e., International Conference on Information Systems (ICIS)) to identify journals that are heavily cited by ICIS articles. A detailed comparison can be made to identify similarities or differences between citations by IS journals and citations by ICIS articles. A preliminary analysis reveals substantial differences, as the second- and third-mostcited journals by ICIS are not in the list of pure IS journals.

Fisher et al. [11] published three sets of journals (level A, level B, and premium professional) based on other published rankings and a follow-up discussion among IS scholars. Preliminary analysis of the ‘‘level A’’ journals reveals strong agreement with the pure IS journals identified in this study. There are 10 ‘‘level A’’ journals: Decision Sciences, Decision Support Systems, European Journal of Information Systems, Information Systems Journal, Information Systems Research, Information & Management, Journal of the Association for Information Systems, Journal of Management Information Systems, Management Science, and MIS Quarterly. Of this set of 10 journals, 6 are on the J8 list, 1 is from the additional journals in the expanded JExp list, and 2 are outside the JExp list but have quite high %-citation values from J8 (6.2% and 7.3%). There is an ‘odd’ journal (Management Science) with below 1% of its citations referring to the J8 set of journals. This demonstrates that the citation method employed here can also be used to identify ‘odd’ journals within a group of journals, i.e., journals that have limited citation relationships with other journals in the group.

This study has demonstrated that network centrality values correlate with perceptions of journal importance and impact factors. Further research could be conducted on the applicability of centrality values as a measure of journal importance, for example, by comparing network centrality values with other measures of journal importance, such as the eigenvalue and h-index [29]. This study uses a simple centrality measure of degree centrality. A combination of centrality measures and other factors was used by Lowry et al. [23], who identified three top journals (MIS Quarterly, Information Systems Research, and Journal of Management Information Systems) that are identical to the top three identified in this study (as reported in Table 5). The lower journals differ somewhat between our study and theirs because of different criteria in selecting and ranking the journals.

## 6. Conclusion

This study proposes and illustrates a process for analyzing citation behavior among journals to identify journals within a discipline. This method is applied to identify core journals in the information systems discipline. The analysis provides general empirical support for the set of eight AIS journals identified by senior AIS scholars. Each of these journals has substantial citations to journals within the set. However, the analysis also reveals that a number of core information systems journals, identified based on their citation behavior, were ignored by AIS. The analysis identifies five additional journals that are pure information systems journals, i.e., each has higher percentage of citationsto theAIS set of journals than thelowest percentageof the AIS set of journals. The results should be of interest to the information systems community. For example, AIS could use our findings as an empirical validation of their journal selection. The citation data also indicate that there is a core information systems discipline, despite the field often being perceived as multi-disciplinary. The information systems journals cite more heavily among themselves than from individual journals in other disciplines.

The set of journals we obtained is further analyzed using their centrality values. The analysis indicates that the perception of a journal is strongly linked to citations to that journal from other pure-IS journals. That is, author citation behavior is strongly linked to perceptions of journal prestige. However, perception of a journal is not strongly linked to its citations to other pure-IS journals. This method uses data readily available from JCR. It is a more efficient method compared to article-level citations. For example, Katerattanakul and Han [20] used article-level citations to compare European journals with American journals. They found that European journals have fewer citations compared to the top American journals. This finding is similar to the findings from our journal-level citation analysis.

The process can be applied to identify journals in other disciplines, such as marketing or finance. For example, instead of beginning with the AIS set of journals, a similar effort for the marketing discipline could begin with a generally agreed set of core marketing publications. The initial core set can be identified based on published classifications. If a commonly agreed core set of journals cannot be identified, it may be plausible to adopt the alternative of beginning with a large set of journals and then eliminating journals based on their percentage citations in this group. Cross-discipline citation is another important research problem that is difficult to solve [22]. Identifying journals within a discipline, as we have done in this study, is a basic foundation for a cross-discipline citation study. The process can also be used to refine the journal classification system currently used by Web of Science.

## Appendix 1. Analysis with self-citation data

Because the study concerns the citation relationship between journals, the main analysis excluded self-citations, as they do not represent relationships with another journal. However, self-citation is important when we consider citations to IS journals because selfcitations are also citations to IS journals once the journal is classified as an IS journal. To provide readers with a more detailed understanding, this appendix reports the results when self-citations are counted.

The table below reports the %-citations of the journals within J8, including self-citations. If we use the cutoff of 13.5%, then only 3 additional journals will be added to the list of pure IS journals. These are Information & Management (19.3%), DATA BASE for Advances in Information Systems (13.8%) and Journal of Global Information Management (13.1%, which is very close to the cutoff) (Table A1).

Table A1  
Citations of AIS set of 8 journals.

<table><tr><td>Citing journal</td><td>To all journals</td><td>To J8 journals (include self-citation)</td><td>%-Citation</td></tr><tr><td>ISR</td><td>4568</td><td>616</td><td>13.5</td></tr><tr><td>MISQ</td><td>4822</td><td>860</td><td>17.8</td></tr><tr><td>JMIS</td><td>2156</td><td>445</td><td>20.6</td></tr><tr><td>JIT</td><td>1696</td><td>326</td><td>19.2</td></tr><tr><td>ISJ</td><td>1243</td><td>265</td><td>21.3</td></tr><tr><td>JSIS</td><td>1909</td><td>450</td><td>23.6</td></tr><tr><td>EJIS</td><td>3037</td><td>694</td><td>22.9</td></tr><tr><td>JAIS</td><td>2228</td><td>540</td><td>24.2</td></tr></table>

## Appendix 2. Analysis with a larger initial set of journals

To estimate whether there would be any significant change in the set of IS journals based on the initial set of journals, we repeat our analysis using the 13 journals (JExp) as the initial set instead of J8. The resulting set of IS journals remains the same. No other journals have %-citation values above 9.5% (Table A2).

Table A2  
Citations of the set of 13 journals

<table><tr><td>Citing journal</td><td>To all journals</td><td>To JExp journals (exclude self-citation)</td><td>%-Citation</td></tr><tr><td> $ISR^a$ </td><td>4568</td><td>433</td><td>9.5</td></tr><tr><td> $MISQ^a$ </td><td>4822</td><td>480</td><td>10.0</td></tr><tr><td> $JMIS^a$ </td><td>2156</td><td>321</td><td>14.9</td></tr><tr><td> $JIT^a$ </td><td>1696</td><td>278</td><td>16.4</td></tr><tr><td> $ISJ^a$ </td><td>1243</td><td>216</td><td>17.4</td></tr><tr><td> $JSIS^a$ </td><td>1909</td><td>337</td><td>17.7</td></tr><tr><td> $EJIS^a$ </td><td>3037</td><td>605</td><td>19.9</td></tr><tr><td> $JAIS^a$ </td><td>2228</td><td>508</td><td>22.8</td></tr><tr><td>IM</td><td>920</td><td>190</td><td>20.6</td></tr><tr><td>JCIS</td><td>924</td><td>137</td><td>14.8</td></tr><tr><td>JGIM</td><td>1163</td><td>220</td><td>18.9</td></tr><tr><td>DBAIS</td><td>564</td><td>94</td><td>16.7</td></tr><tr><td>ISM</td><td>1165</td><td>163</td><td>14.0</td></tr></table>

<sup>a</sup> Journals in the original set of 8 AIS journals.

Table A3  
Correlation of in-degree centrality with impact factors.

<table><tr><td>JExp journal</td><td>In-degree citations</td><td>In-degree centrality</td><td>Impact factor</td><td>5-year impact factor</td></tr><tr><td>MIS Quarterly</td><td>1488</td><td>1.00</td><td>4.659</td><td>7.474</td></tr><tr><td>Information Systems Research</td><td>727</td><td>.49</td><td>2.010</td><td>3.638</td></tr><tr><td>Journal of Management IS</td><td>471</td><td>.31</td><td>1.262</td><td>2.780</td></tr><tr><td>Information &amp; Management</td><td>269</td><td>.18</td><td>1.663</td><td>3.178</td></tr><tr><td>European Journal of IS</td><td>268</td><td>.18</td><td>1.558</td><td>2.422</td></tr><tr><td>Journal of the Association for IS</td><td>188</td><td>.12</td><td>1.048</td><td>2.766</td></tr><tr><td>Journal of Information Technology</td><td>156</td><td>.10</td><td>3.352</td><td>3.801</td></tr><tr><td>Information Systems Journal</td><td>139</td><td>.09</td><td>1.381</td><td>2.376</td></tr><tr><td>Journal of Strategic IS</td><td>111</td><td>.07</td><td>1.500</td><td>2.433</td></tr><tr><td>DATA BASE for Advances in IS</td><td>66</td><td>.04</td><td>0.341</td><td>-</td></tr><tr><td>Journal of Computer IS</td><td>39</td><td>.03</td><td>0.495</td><td>0.767</td></tr><tr><td>Information Systems Management</td><td>39</td><td>.03</td><td>0.352</td><td>0.750</td></tr><tr><td>Journal of Global IM</td><td>27</td><td>.02</td><td>0.452</td><td>1.179</td></tr><tr><td></td><td></td><td rowspan="2">Correlation coefficient p-Value</td><td>0.735</td><td>0.866</td></tr><tr><td></td><td></td><td>0.001</td><td>0.001</td></tr></table>

## Appendix 3. Correlation between centrality values and impact factors

A further correlation analysis of the centrality values for the extended set of journals with their impact factors in Journal Citation Report 2012 is reported below. As expected, the in-degree centrality is highly correlated with the impact factor and the 5- year impact factor because the impact factor is a special measure of incoming citations. The out-degree centrality is not significantly correlated with the impact factors (Table A3).

## References

[1] M. Amin, M. Mabe, Impact factors: use and abuse, Perspect. Publ. 1, 2000, pp. 1–6.

[2] J.A. Baum, Free-riding on power laws: questioning the validity of the impact factor as a measure of research quality in organization studies, Organization 18, 2011, pp. 449–466.

[3] P. Bharati, P. Tarasewich, Global perceptions of journals publishing e-commerce research, Commun. ACM 45, 2002, pp. 21–26.

[4] S.P. Borgatti, M.G. Everett, J.C. Johnson, Analyzing Social Networks, SAGE Pub lications Limited London UK 2013.

[5] L.D. Brown, J.C. Gardner, Using citation analysis to assess the impact of journals and articles in contemporary accounting research (CAR), J. Account. Res. 23, 1985 pp. 84–109.

[6] H.C. Chan, H.W. Kim, W.C. Tan, Information systems citation patterns from International Conference on Information Systems articles, J. Am. Soc. Inform Sci. Technol. 57, 2006, pp. 1263–1274.

[7] B.R. Cooper, D. Blair, M. Pao, Communicating MIS research: a citation study of journal influence, Inform. Process. Manag. 29, 1993, pp. 113–127.

[8] M.J. Culnan, E.B. Swanson, Research in management information systems, 1980– 1984: points of work and reference, MIS Q. 10 (3), 1986, pp. 289–302.

[10] E.R. Doke, R.H. Luke, Perceived quality of CIS/MIS journals among faculty: publishing hierarchies, J. Comput. Inform. Syst. 2, 1987, pp. 30–33.

[11] J. Fisher, G. Shanks, J. Lamp, A ranking list for information systems journals, Aust. J. Inform. Syst. 14, 2007, pp. 5–18.

[12] G.A. Forgionne, R. Kohli, A multiple criteria assessment of decision technology system journal quality, Inform. Manag. 38, 2001, pp. 421–435.

[13] L.C. Freeman, Centrality in social networks conceptual clarification, Soc. Netw. 1 (3), 1979, pp. 215–239.

[14] M.L. Gillenson, J.D. Stutz, Academic issues in MIS: journals and books, MIS Q. 15, 1991, pp. 447–452.

[15] S. Hamilton, B. Ives, Knowledge utilization among MIS researchers, MIS Q. 6, 1982, pp. 220–235.

[16] D.L. Hansen, B. Shneiderman, M.A. Smith, Analyzing Social Media Networks with NodeXL: Insights from a Connected World, Morgan Kaufmann, USA, 2010.

[17] B. Hardgrave, K. Walstrom, Forums for MIS scholars, Commun. ACM 40, 1997, pp. 119-124

[18] S.P. Harter, T.E. Nisonger, ISI’s impact factor as misnomer: a proposed new measure to assess journal impact, J. Am. Soc. Inform. Sci. 48, 1997, pp. 1146-1148

[19] C.W. Holsapple, L.E. Johson, H. Manakyan, J. Tanner, Business computing research journals: a normalized citation analysis, J. Manag. Inform. Syst. 11, 1994, pp. 131–140.

[20] P. Katerattanakul, B. Han, Are European IS journals under-rated? An answer based on citation analysis Eur. J. Inform. Syst. 12, 2003, pp. 60–71.

[21] D.N. Laband, M.J. Piette, The relative impacts of economics journals: 1970–1990, J. Econ. Lit. 32, 1994, pp. 640–666

[22] P.B. Lowry, D. Romans, A. Curtis, Global journal prestige and supporting disciplines: a scientometric study of information systems journals I. Assoc, Inform Syst. 5, 2004, pp. 29–80.

[23] P.B. Lowry. G.D. Moody. I. Gaskin. D.F. Galleta. S.J. Humpherys. I.B. Barlow. D.W. Wilsion. Evaluaing journal quality and the Association for Information Systems senior scholars’ journal basket via bibliometic measures: do expert journal assessments add value? MIS Q. 37, 2013, pp. 993–1021.

[24] N.A. Mylonopoulos, V. Theoharakis, Global perceptions of IS journals: where is the best IS research published? Commun. ACM 44, 2001, pp. 29–33.

[25] K. Peffers, Y. Tang, Identifying and evaluating the universe of outlets for information systems research: ranking the journals, J. Inform. Technol. Theory Appl. 5, 2003, pp. 63–84.

[26] R. Pieters, H. Baumgartner, Who talks to whom? Intra and interdisciplinary communication of economics journals J. Econ. Lit. 40, 2002, pp. 483–509.

[27] G. Polites, R.T. Watson, Using social network analysis to analyze relationships among IS journals, J. Assoc. Inform. Syst. 10, 2009, pp. 595–636.

[28] R.K. Rainer, M.D. Miller, Examining differences across journal rankings, Commun. ACM 48, 2005, pp. 91–94.

[29] D. Straub, C. Anderson, Journal quality and citations: common metrics and considerations about their use, MIS Q. 2010, pp. iii–xii.

[30] D.R. Vogel, J.C. Wetherbe, MIS research: a profile of leading journals and universities, Data Base 16, 1984, pp. 3–14.

[31] K. Walstrom, B. Hardgrave, R. Wilson, Forums for management information system scholars, Commun. ACM 38, 1995, pp. 93–107.

[32] K.A. Walstrom, B.C. Hardgrave, Forums for information systems scholars: III, Inform. Manag. 39, 2001, pp. 117–124.

[33] S. Walczak, A re-evaluation of information systems publications forums, J. Comput. Inform. Syst. 40, 1999, pp. 88–97.

[34] M. Whitman, A.R. Hendrickson, A.M. Townsend, Academic rewards for teaching, research and service: data and discourse, Inform. Syst. Res. 10, 1999, pp. 99–109.

![](/api/attachments/BHTZJBD8/fulltext/images/f4bda335ee50104c19787884d9c7592ff5cce1b1deea2b7c3cf2fa19e80279fa.jpg)

![](/api/attachments/BHTZJBD8/fulltext/images/46112ef3a8a773c24353cc1340d355de9743c3204f56fd139408029bc710fa08.jpg)  
Hock Chuan Chan is an associate professor in the Department of Information Systems at the National University of Singapore. He works on information systems and human computer interaction. He was a program committee member, track co-chair, or program co-chair for a number of conferences, such as ICIS, PACIS and HCI/MIS Workshop. He is on the editorial board of AIS Transactions on Human-Computer Interaction, Journal of Database Management and Journal of Electronic Commerce Research. He was an associate editor for MIS Quarterly.

![](/api/attachments/BHTZJBD8/fulltext/images/5ed5ba4c77260010b866fa59d4493c459bb77d91cf5d85a952930591ae3504b6.jpg)

Varsha Guness is a graduate from the Department of Information Systems at the National University of Singapore and a Masters student from the University College Dublin Business School. Varsha currently works as a Human Resources Professional in the Capital Market Industry. She has a strong appetite for both Human Resources Management and IT and she currently oversees the Human Resources Information System, Talent Acquisition, Learning and Development and the Performance Management processes of a financial software consulting firm.

Hee-Woong Kim is Underwood Distinguish Professor in the Graduate School of Information at Yonsei University, Seoul Korea. Before joining Yonsei University, he was a faculty member at the National University of Singapore after spending several years as a senior IS consultant in the banking industry. He has served on the editorial boards of the Journal of the Association for Information Systems and IEEE Transactions on Engineering Management. His research work has been published in the IEEE Transactions on Engineering Management, Information Systems Research, Journal of the Association for Information Systems, Journal of Management Information Systems, Journal of Retailing, and MIS Quarterly.
