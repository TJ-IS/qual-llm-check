---
otero_id: 21115
otero_key: "XJNW7TXK"
title: "Enriching Web taxonomies through subject categorization of query terms from search engine logs"
authors: "Shui-Lung Chuang; Lee-Feng Chien"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00099-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Enriching Web taxonomies through subject categorization of query terms from search engine logs

Shui-Lung Chuang\*, Lee-Feng Chien

Institute of Information Science, Academia Sinica, Taipei 115, Taiwan

## Abstract

In this paper, we propose a query-categorization approach to facilitating the engineering process of constructing Web taxonomies. One primary step in taxonomy construction is to acquire the domain-specific terminology terms and the mapping between the subjects and these terms. We introduce a technique for categorizing Web query terms from the logs of on-line search services into a predefined subject taxonomy based on their supposed popular search interests. The obtained experimental results show our technique’s effectiveness in reducing the workload of human indexers in constructing Web taxonomies and also show its usefulness in various Web information retrieval applications. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Information retrieval; Query categorization; Log analysis

## 1. Introduction

It is, undoubtedly, very valuable to put a huge amount of data into a well-organized taxonomy to help users perform many activities, such as searching for specific information and performing decision-making tasks. Hence, in recent years, many efforts have focused on facilitating the engineering process of taxonomy construction, e.g., the acquisition of subjects, the establishment of a subject hierarchy, the discovering of conceptual relationships, etc. [5,11, 13,14]. One primary step in this construction process is to acquire the domain-specific terminology terms and the mapping between the subjects and these terms.

The most common taxonomies available on the Web are the large directories used to organize Web sites (such as the one at Yahoo!). In order to enable such well-categorized resources to be easily processed by human indexers and retrieved by software programs (such as Internet search services), many domain-specific terms for each category and their relationships, e.g., synonym and hypernym/hyponym relationships, are required. However, most of the significant terms for Web information retrieval (IR) applications are proper nouns and new terms [19], both of which are hard to find in traditional handbuild knowledge bases, such as WordNet [10]. Manually collecting and organizing such term vocabularies for Web applications is neither practical nor costeffective due to problems related to information updating, time consumption, and scalability. Thus, some automatic or computer-aided mechanisms are needed to make this process more efficient and adaptable.

![](/api/attachments/XJNW7TXK/fulltext/images/a15194c8a20ea3399bb5f11090cdb37f8c57c13e4be14caaecb04ad376053f4e.jpg)  
Fig. 1. An example of subject taxonomy with query terms.

Some of the excellent sources for obtaining Web significant terms are the query logs of on-line search services. In this work, we are interested in organizing such query terms<sup>1</sup> into a broader subject taxonomy (e.g., Fig. 1), where deeper analysis of domain-specific terminology and further discovery of term relationships can be performed under each subject domain. This can serve as a step toward enriching Web taxonomies. Thus, in this paper, our problem is as follows: If there already exists a predefined subject taxonomy, how can we place any given query terms into proper categories? For example, the appropriate category for the query term ‘‘Real Player’’ may be Computer/ Company or Computer/Software Download.

To our knowledge, few reports in the literature have focused on the Web query term categorization problem. Recently, some document-based approaches to acquiring domain-specific semantic lexicons or to enriching the existing ontologies have been proposed [1,6,17]. Our work differs from these works in that we adopt the query logs as the terminology source, thus avoiding term segmentation and extraction problems commonly faced in document-based approaches. Some researches on term clustering are to a certain degree related to our research, such as the works on latent semantics, SVD, term relationship analysis, etc. [9,15,18]. Most of them have dealt with the automatic clustering of controlled indexed terms into clusters and with using them to assist IR systems in the query expansion process so as to improve the precision and recall ratios. There have been some works on terminology analysis for Web IR [2,4] and a similar work on the clustering of Web queries [3], in which a collection of user transactions from an Internet search engine are mined to discover clusters of similar queries. The clustered queries could then be used for term suggestion to help users form their own search requests. Our research differs from these works in that we try to structure each unknown query term into appropriate and meaningful subject categories, and provide possible corresponding subject domains for each unknown term.

To instantiate our research, the logs from three different search engines in different time periods were collected. Human efforts were applied to analyze these logs, and a two-level subject taxonomy with 14 major categories and 100 subcategories was constructed to express the popular search subject areas. Also, about 20 K of high-frequency query terms was categorized properly by human experts. This working environment then served as the basis for exploring use of the automatic query-term categorization approach.

Since a query term is too short to contain enough information in itself for automatic categorization, retrieved documents from real-world search engines are used in our approach to supplement the features of the candidate query term. Then, a classification method based on a term feature vector and a modified inner-product similarity measure is applied to this query term categorization task. Several experiments have been conducted to evaluate the performance of this approach. The top 1 inclusion rate, i.e., the rate of obtaining the top one category containing the most appropriate categories assigned by human indexers, could reach 49.83%, and the top 5 inclusion rate could reach 78.64%. The obtained experimental results show that this approach is efficient in dealing with large numbers of queries and is adaptable to the dynamic Web environment. We believe that this approach will be also useful in the various Web IR applications aforementioned. An obvious application is that of collecting sufficient query terms for some sensitive resources, such as adults and drugs related materials, to improve the ability of a search engine to filter out sensitive queries.

In the rest of this paper, we will first introduce the classification method used to categorize query terms into a subject taxonomy. Next, the working environment in which we carried out the research will be introduced. This includes the query logs and the taxonomy we used in our experiments. Then, the conducted experiments and their results will be presented. Finally, we will discuss some possible applications and give a conclusion.

## 2. The query categorization problem

Because of the deep-hierarchical structures of realworld taxonomies, it is natural to hierarchically classify query terms into such taxonomies. That is, we first classify queries into top-level categories, and then for each category, we classify queries into its subcategories. Thus, the categorization of queries into a taxonomy is decomposed into a set of simpler problems, one at each node in the hierarchy, such that we only need to classify queries into a small set of categories. In the rest of this section, we will only discuss our approach to categorizing query terms into a set of categories.

Query categorization is defined as the problem of automatically assigning predefined categories to query terms according to the terms’ supposed search interests or information needs. More formally, let C be a predefined taxonomy, and let $V = \{ w _ { 1 } , w _ { 2 } , . . . , w _ { n } \}$ be the set of all query terms that have been categorized into C properly.<sup>2</sup> Query categorization is used to determine a category set $C ( t ) \subseteq C$ for a given unknown query term tgV, so each $c { \in } C ( t )$ is considered as a possible category t is related to.

## 2.1. Classification model

A canonical way to an automatic classification<sup>3</sup> problem is to represent each candidate as a feature vector in which each dimension of the vector represents a candidate’s attribute and its value indicates the candidate’s quantity/quality for that attribute. Then, a classifier is constructed as a function that maps such an input feature vector to a numerical value indicating the confidence that the input candidate belongs to a class. The final class(es) can then be determined by means of some criteria, such as a predefined threshold value or some experimentally learned parameters. Thus, a classification problem can be solved by determining the proper features to be used and defining a classifier function to rank target classes.

Since a query term, usually containing one to two words in English [19] or two to three characters in Chinese [7], is too short to convey enough information in itself, some extra useful information is required to assist in the determination of corresponding categories. In our considered problem, a query term is a string submitted to a search engine to express a certain search request(s). Although the user’s original search interest for a query term is hard to judge, the retrieved documents are believed to contain helpful information about the unknown query term. Collecting the required documents for each candidate query term can be easily performed by submitting the query string to on-line search engines. Thus, we assume that there exists virtually a document collection D, i.e., documents indexed by search engines, and we let $D _ { t }$ denote the set of documents that can be retrieved by query term t.

## 2.2. Extracting features from retrieved documents

It is helpful to understand the process a human indexer uses to determine the corresponding subjects of a given query term that is beyond his/her knowledge. From our observations, a human indexer may refer to the subject terms that occur in the documents retrieved by the candidate term when the subjects of the retrieved documents are hard to judge. Determining the subject(s) of the unknown term is then done based on the subjects of the subject terms in the retrieved documents. The proposed approach is, therefore, designed to simulate such human behavior.

The basic idea of our approach is to represent the feature vector of the candidate query term t by using the term features extracted from $t ^ { \ast } \mathrm { s }$ retrieved document set $D _ { t } .$ The feature space is defined by the precategorized query term vocabulary set $V ,$ in which each term has already been associated with proper category information. This approach is very similar to classifying a document based on the composed key terms in a conventional document classification process, or to tagging the part of speech for a word with its co-occurring neighboring words in linguistic analysis. Below, we will propose a ranking scheme used to estimate the confidence of a query term t belonging to a category c.

## 2.3. Tf –df-based category ranking

The approach employed in our work is to use term frequency (tf) and document frequency (df) information to give a weighted value for each occurring feature term. The intuition behind using the tf factor is that the degree that query term t belongs to category c is determined by whether there are many feature terms appearing in $D _ { t }$ with category c and by the number of times these feature terms appear. Also, feature terms appearing in more retrieved documents are assumed to be more relevant to $t ,$ which motivates use of the df factor. The formula is defined in the following.

Let $n _ { w }$ be the number of documents in $D _ { t }$ in which the feature term $w \in V$ appears, and let $f _ { w }$ be the raw frequency of term w in $D _ { t }$ (i.e., the sum of the number of times the term w occurs in the text of each document $d _ { i } { \in } D _ { t } )$ . The ranking function based on tf–df information is given by

$$
R (t, c) = \sum_ {w \in W _ {t, c}} \frac {f _ {w}}{\max _ {k \in W _ {t}} f _ {k}} \log \left(n _ {w} + 1\right),\tag{1}
$$

where $W _ { t }$ is the complete set of feature terms in $D _ { t }$ and $W _ { t , c }$ is the set of those feature terms related to category c. Computing the maximum frequency over all feature terms is only done to beautify and make more reasonable the formula, and it does not have any effect if we only use the formula to rank a set of categories based on the same document set $D _ { t } .$ A count of one is added to $n _ { w }$ to avoid a logarithm value of zero.

## 3. The overall approach and working environment

In this section, we will describe the environment in which the research was carried out. The diagram depicted in Fig. 2 shows the overall concept of the proposed approach, which is composed of three computational processes: query term log analysis, relevant document retrieval, and subject categorization. The function of query term log analysis, which will be further described in the following paragraphs, is to obtain the subject taxonomy and the categorized term set through analysis of search-engine logs. The relevant document retrieval process is performed to retrieve the most relevant document sets by working together with the search process of real-world engines. As we described above, this step is used to gather the features for each candidate query term. Finally, the categorization method described in the previous section is applied to determine the appropriate subject categories for each query term. Fig. 3 shows the detailed algorithmic procedure of the whole hierarchical categorization process, which recursively applies the categorization algorithm to the n, specified by the user, most possible candidate categories at each layer and, finally, returns the top-ranked n categories.

![](/api/attachments/XJNW7TXK/fulltext/images/5b38261bba1e65c7a4db614d0841c4e84437d80640fdd7a0b0164c9e6070292e.jpg)  
Fig. 2. An abstract diagram showing the concept behind the proposed approach.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
SubjectCategorize(t, C, V, D, n)
t: the unknown query term
C: the set of subject categories
V: the set of feature terms
 $D_{t}$ : the highly ranked Web document set retrieved by term t
n: the number of target categories

1: for all  $c \in C$  do
2:    $W_{t,c} \leftarrow \emptyset$ 
3: for all  $w \in V \land w$  appears in  $D_{t}$  do
4:    calculate  $f_{w}$  (term frequency) and  $n_{w}$  (document frequency)
5:    $W_{t,c} \leftarrow W_{t,c} \cup \{w\}$  where c is the category w belongs to
6: for all  $c \in C$  do
7:    $R(t, c) \leftarrow \sum_{w \in W_{t,c}} \frac{f_{w}}{\max_{k \in W_{t}} f_{k}} \log(n_{w} + 1)$ 
8:  $C' \leftarrow \emptyset$ 
9: for all c in top n categories with highest  $R(t, c)$  do
10:    if c is a leaf node then
11:    $C' \leftarrow C' \cup \{c\}$ 
12:    else {c has children}
13:    $C' \leftarrow C' \cup \textbf{SubjectCategorize}(t, \{\textbf{children of } c\}, V, D_{t}, n)$ 
14: return top-ranked n categories in  $C'$  according to the decreasing order of  $R(t, c)$
</div>

Fig. 3. An algorithmic procedure describing the hierarchical categorization process.

In the following paragraphs, we will describe in detail query term log analysis. This includes the logs we obtained from real search engines and the taxonomy we constructed for our experiment. Also, highfrequency query terms are manually analyzed and categorized into proper categories. We are interested in categorizing high-frequency query terms into popular search subject categories because these query terms are considered relatively stable foremost data for analyzing users’ search interests or information needs. The obtained categorized query terms can then be treated as the basis for experimental evaluation.

## 3.1. Analysis of three log data sets

To instantiate the research, three query logs from the Dreamer<sup>4</sup> (D-1998), $\mathrm { G A I S } ^ { 5 }$ (G-1999), and Openfind<sup>6</sup> (O-2000) search engines in Taiwan were collected as the basis for our analysis. The query logs contain a series of request entries, and each entry contains a query term, the IP address of the machine that sent the request, the corresponding timestamp, etc. Since we were only interested in the query terms themselves in our research, only the query-term parts of the logs were extracted.

Each query term in the logs was preprocessed by mapping the characters in its English part to lowercase, converting a sequence of spaces to only one, and removing the spaces between Chinese characters. Furthermore, we removed those queries with only one byte or one Chinese character. No further processing was performed. To avoid significant preprocessing of query logs is to underscore the nature of the queries submitted by users.

Table 1 shows these three data sets based on the collection time periods, the counts of distinct query terms, the total query frequencies, and some basic statistics. In our research design, we focused on analyzing D-1998 and let G-1999 and O-2000 be cross-reference sets.

## 3.2. Structuring a subject taxonomy

To advance our study of the considered problem, we structured a popular subject taxonomy, a hierarchy of popular subject categories, to describe the subjects of users’ search interests. As mentioned before, we are interested in the subjects the query terms correspond to. Instead of adopting the hierarchical structure commonly found in Web directories, such as Yahoo!, or in the classification schemes in library communities, such as the Dewey Decimal system, we used a bottom-up methodology by quickly reviewing the top 5000 query terms from D-1998 and then constructing the hierarchy based mainly on the analysis of human observations. The intention and information requests of each query term were estimated by several people with substantial experience surfing the Internet. Finally, a two-level hierarchical structure, consisting of 14 major categories together with 100 subcategories, was developed. Fig. 1 depicts a fragment of the whole taxonomy. The reason for structuring the taxonomy using such an approach was that we wanted it to reflect precisely the search interests in terms of locality of space and culture under which the queries were made.

Table 1 Statistics of three log data set

<table><tr><td>Data set name</td><td>D-1998</td><td>G-1999</td><td> $O-2000^a$ </td></tr><tr><td>Year</td><td>1998</td><td>1999</td><td>2000</td></tr><tr><td>Period</td><td>3 months</td><td>2 weeks</td><td>12 months</td></tr><tr><td>Number of distinct queries</td><td>228,566</td><td>114,182</td><td>3011</td></tr><tr><td>Number of total queries</td><td>2,184,256</td><td>475,564</td><td>2,493,211</td></tr></table>

a O-2000 collected the top 1000 query terms of each month in 2000, so it only contains 3011 distinct queries.

## 3.3. Manually categorizing high-frequency terms

Similar to the approach used to structure the taxonomy, categorization of high-frequency terms was performed manually by five Library and Information Science students together with a professional reference librarian for 3 months. These people had substantial experience surfing the Internet. In the whole process, each query term was examined, and the corresponding categories were determined according to subjective estimation of the information requests of the users who issued the query. For example, the query term ‘‘Microsoft’’ was categorized as an instance of the Company subcategory included in the major Computer category. Since it is very likely that a query term can have multiple information requests from different users, besides one major category, a secondary category was also assigned to each term if necessary for the purpose of crossreferencing. In this manual categorization process, a total of 18,017 terms with the highest frequencies from D-1998 were categorized properly. Though this set only represented 8% of the distinct queries, they totally formed 81% of the search requests in the test logs.

Admittedly, human classification is subjective even if there is interceder agreement between human indexers. However, in our study, the human analysts were involved mainly in classifying seed terms into appropriate subject categories. If there was an adequate number of feature terms in each category, we believe that the distortion caused by a few instances of invalid human categorization in fact would not seriously affect the accuracy of the auto-categorization approach.

## 3.4. Collecting retrieved documents

To collect the retrieved document set $D _ { t }$ for each query term $t ,$ we adopted Google<sup>7</sup> Chinese as the back-end engine. Each query term was submitted to Google, and then up to 100 search result entries were collected. The title and description of each entry were extracted as the representation of the corresponding document. In the final result, only 107 queries among 18,017 total queries had no retrieved documents.

Table 2  
Coverage comparison between D-1998 and G-1999

<table><tr><td>G-1999/D-1998</td><td>Top 1000</td><td>Top 20,000</td></tr><tr><td>Top 1000</td><td>583</td><td>914</td></tr><tr><td>Top 20,000</td><td>977</td><td>9709</td></tr><tr><td>All</td><td>992</td><td>14,721</td></tr></table>

## 3.5. Core term extraction

Many search requests are affected by ephemeral trends in querying, such as searches related to a newly released movie released or some specific events happening during the year. This situation really interests us. To determine the effects of time locality, query terms from D-1998 were matched and filtered using the G-1999 log to make a comparison of coverage. Table 2 shows the coverage comparison of query terms between the two data sets: D-1998 and G-1999. This table shows that 14,721 terms, nearly 77%, (the lower-right cell in the table) of D-1998’s top 20,000 query terms still existed in G-1999’s 2- week randomly selected log, which indicates that many core or important information requests were not much affected by time and were worthy of further study.

To obtain seed feature terms, query terms without the effects of time, so-called ‘‘core terms,’’ are extracted based on whether or not the terms occur in both of the query logs. Except for some proper nouns like names of famous Web sites and people, an interesting finding was that core terms like ‘‘movie,’’ ‘‘baseball,’’ or ‘‘flight ticket’’ were found to mostly be subject terms. These core terms are considered to be more comprehensive and are often used by Web users to represent popular search interests and also by Web authors to indicate the key subjects of Web documents. Using core terms as features in the categorization process is believed to be more effective than just using common words.

## 4. Experiment

To assess the performance of the proposed approach, two tests using the data from D-1998 and O-2000 were conducted, respectively. The former was used to test the accuracy of the categorization approach compared with that of human analysis, and the latter was used to test the sustainability of different term sets like core terms or high-frequency terms as the feature set used for categorization.

The first test was performed to evaluate the performance achieved in categorizing the test query terms into our predefined two-level taxonomy with 14 major categories and 100 subcategories. The 9709 core terms were taken as the feature term set V. To ensure stability of the achieved performance, 20 test sets of query terms were prepared, each of which contained 1000 randomly selected noncore terms. The experiment was conducted using these 20 test term sets, and the performance achieved was the average of the results of these 20 trials. In addition, in order to reveal the effects of size variation of the core term set used as the feature set for categorization, we ran the experiment with different core term sets: the top 100, 200, . . ., 900, 1000, 2000, . . ., 9000, and 9709 terms from the seed feature term set, in accordance with the frequency of the core terms.

Some of the obtained correct rates are shown in Table 3, and the overall accuracy curve is depicted in Fig. 4, where top n means the highly ranked n candidate categories that contained the appropriate category. Also, Table 4 shows a set of randomly selected English query terms from our test sets (note that our query terms contain both Chinese and English queries) along with their human-assigned categories and machine-suggested top five categories. Note that

Table 3  
Top 1 – 5 inclusion rates with various core term sets used as the feature sets

<table><tr><td></td><td>100</td><td>300</td><td>500</td><td>1000</td><td>3000</td><td>5000</td><td>7000</td><td>9000</td><td>9709</td></tr><tr><td colspan="10">(A) Inclusion rates for the top-level 14 categories</td></tr><tr><td>1</td><td>36.80</td><td>46.70</td><td>48.20</td><td>51.90</td><td>55.40</td><td>59.50</td><td>60.00</td><td>59.90</td><td>60.20</td></tr><tr><td>2</td><td>48.10</td><td>62.20</td><td>61.80</td><td>67.40</td><td>72.60</td><td>76.60</td><td>77.30</td><td>78.00</td><td>77.90</td></tr><tr><td>3</td><td>53.50</td><td>68.70</td><td>70.50</td><td>74.60</td><td>82.40</td><td>84.40</td><td>84.60</td><td>85.40</td><td>85.70</td></tr><tr><td>4</td><td>56.60</td><td>73.60</td><td>75.90</td><td>81.60</td><td>87.10</td><td>88.90</td><td>89.20</td><td>89.60</td><td>89.50</td></tr><tr><td>5</td><td>57.90</td><td>79.00</td><td>80.20</td><td>86.80</td><td>90.80</td><td>90.90</td><td>91.30</td><td>91.60</td><td>91.70</td></tr><tr><td colspan="10">(B) Inclusion rates for the second-level 100 categories</td></tr><tr><td>1</td><td>24.98</td><td>36.30</td><td>38.79</td><td>43.67</td><td>46.77</td><td>48.77</td><td>49.40</td><td>49.57</td><td>49.83</td></tr><tr><td>2</td><td>31.00</td><td>46.12</td><td>49.49</td><td>55.40</td><td>61.51</td><td>63.87</td><td>64.58</td><td>65.26</td><td>65.55</td></tr><tr><td>3</td><td>33.28</td><td>50.23</td><td>54.29</td><td>60.91</td><td>67.82</td><td>70.28</td><td>71.36</td><td>72.09</td><td>72.34</td></tr><tr><td>4</td><td>34.83</td><td>53.39</td><td>57.44</td><td>64.73</td><td>71.62</td><td>73.78</td><td>74.70</td><td>75.78</td><td>75.87</td></tr><tr><td>5</td><td>36.06</td><td>55.58</td><td>59.76</td><td>67.34</td><td>74.50</td><td>76.67</td><td>77.42</td><td>78.47</td><td>78.64</td></tr></table>

The horizontal rows indicate the sizes of the core term sets used for categorization, and the vertical columns list the obtained inclusion rates for the top 1 – 5 candidate categories.

![](/api/attachments/XJNW7TXK/fulltext/images/0dbacc1e855ca88d1d41f9e676cf96758065a13654ccb86b39cd3730fffb5b87.jpg)  
Fig. 4. Top 1 – 5 inclusion rates with the core term set for second-level categories.

the top five categories are shown in the order of their R values, i.e., the one on the left-hand side has a larger R value than the one on the right-hand side does.

Even with the simple tf –df ranking scheme, the performance seems to be acceptable. Considering only the top 1 categorization result for second-level categories, the average top 1 inclusion rate, i.e., the rate of the obtained top one category containing the most appropriate categories assigned by human indexers, is 49.83%. If we consider the performance of the top five categories, the inclusion rate can reach 78.64%. The achieved performance is assumed nearly compet-

Table 4 An example of query terms with their top five suggested categories

<table><tr><td>Query term</td><td>Corr. cat.</td><td>Suggested five cat.</td><td>Major category</td><td>/ Sub-category</td><td>: ID</td></tr><tr><td>real player</td><td>cd,cn</td><td>cd cn mn ch pc</td><td>Art&amp;Humanities</td><td>/ Art</td><td>: aa</td></tr><tr><td>star trek</td><td>en</td><td>ei gg en cd ds</td><td>Business&amp;Finance</td><td>/ Bank</td><td>: bb</td></tr><tr><td>michael jackson</td><td>ei</td><td>em cd tl en cn</td><td></td><td>/ Information</td><td>: bf</td></tr><tr><td>tennis</td><td>fs</td><td>fs e3 cd ds gg</td><td>Computer&amp;Network</td><td>/ Money</td><td>: bm</td></tr><tr><td>case tool</td><td>cd</td><td>ch ds cd e3 ks</td><td></td><td>/ Telcom</td><td>: bn</td></tr><tr><td>erotica</td><td>ss</td><td>cn ss mn cd cs</td><td></td><td>/ Download</td><td>: cd</td></tr><tr><td>meg ryan</td><td>ei</td><td>en cn cd em cp</td><td></td><td>/ Group</td><td>: cg</td></tr><tr><td>i phone</td><td>cd,cn</td><td>cd lp tl cn e3</td><td></td><td>/ Hardware</td><td>: ch</td></tr><tr><td>quarkxpress</td><td>cd</td><td>cd kb cg aa mn</td><td>Education</td><td>/ Network</td><td>: cn</td></tr><tr><td>doom2</td><td>gg</td><td>cn cd gg ds cb</td><td>Entertainment</td><td>/ Picture</td><td>: cp</td></tr><tr><td>australia</td><td>tf</td><td>tl tf cd cn ds</td><td></td><td>/ Search Engine</td><td>: cs</td></tr><tr><td>fishing</td><td>fs</td><td>tl cn e3 fs cd</td><td></td><td>/ Group</td><td>: dg</td></tr><tr><td>chinatrust</td><td>bb</td><td>bm tl tf bb cn</td><td>Recreation&amp;Chat</td><td>/ School</td><td>: ds</td></tr><tr><td>geocity</td><td>cn</td><td>cn cd mn cs ds</td><td></td><td>/ MP3</td><td>: e3</td></tr><tr><td>motorora</td><td>lp,bn</td><td>cn lp bn dt cd</td><td>Game</td><td>/ Individual</td><td>: ei</td></tr><tr><td>age of empires</td><td>gg</td><td>gg cd cn ch cg</td><td></td><td>/ Music</td><td>: em</td></tr><tr><td>photo shop</td><td>cd</td><td>cd cp dt cn kb</td><td>Shopping</td><td>/ Movie</td><td>: en</td></tr><tr><td>airplane</td><td>tp</td><td>tp bf cn cd mn</td><td>News&amp;Media</td><td>/ News</td><td>: mn</td></tr><tr><td>cafe</td><td>le</td><td>le cn mn cd em</td><td>Adult</td><td>/ Sex</td><td>: ss</td></tr><tr><td>nokia8810</td><td>lp</td><td>cn cd lp ds ls</td><td>Travel</td><td>/ Local</td><td>: tl</td></tr><tr><td></td><td></td><td></td><td>Travel</td><td>/ Plane</td><td>: tp</td></tr></table>

itive with that of human indexers. Human indexers normally assign one or two categories for each test query term due to the difficulties involved in complete analysis. It is worth noting that although many of the top five categories are not exactly the same as the categories assigned by human indexers, some of them are still related to the human-assigned categories and cannot simply be considered as miscategorized. For example, the query ‘‘michael jackson’’ shown in Table 4 was assigned to Entertainment/Individual by humans. Although this human-assigned category does not appear in the machine-suggested top five categories, the suggested category Entertainment/Music is surely related, and the category Computer/Download may also be considered related because someone may want to download the singer’s music files. Therefore, the suggested top categories are found to be rather helpful in many respects; for example, they can be used by human indexers to reexamine the correctness of their assigned categories.

Our second test was conducted to compare the sustainability of various feature term sets for categorization. We used O-2000 as our test set, which had a 2-year lag compared to the feature term set from D-1998 in the first test. Among the total of 3011 distinct query terms, 1265 terms were not found in the term set that had been categorized. These unlabeled query terms were then categorized by the human indexers as described in the previous section, and the result was treated as the testing set. To compare the effects of various feature sets, we adopted four feature sets selected based on D-1998: core terms (coreterm), high-frequency terms (freqterm), terms randomly selected from among high-frequency terms (freqrand), and terms randomly selected from among 18,017 categorized terms without considering their frequencies (baseline). The experiment was conducted in the same way as the first one was.

The results are shown in Fig. 5. The baseline set obviously had the poorest performance. The coreterm set and freqterm set achieved comparable results. While the freqterm set outperformed the freqrand set, the figure shows that the total frequencies (ranks)

of the feature terms greatly influenced the performance. Although the experimental results do not strongly support our previous assumption that core terms perform better than frequency terms in the categorization process, it can be assumed that better performance would be achieved if longer time lags were considered.

![](/api/attachments/XJNW7TXK/fulltext/images/383431d545eb5b08f428d593e9f55c983f061ccff73e8072d8ca109c6e5d7ebe.jpg)  
Fig. 5. Top 1 inclusion rates for four different feature term sets.

## 4.1. Discussion

One of the factors that causes the robustness of the proposed approach to increase is the representative and coverage of the core terms as the basic feature terms in this categorization task. These core terms were extracted based on adequate logs and human effort. It is worth noting that the top 1 inclusion rate could reach 24.98% only using the top 100 core terms as the feature set, compared with a rate of 7.92% obtained using 100 randomly selected feature core terms (cf. Fig. 5). This reveals that these top core terms might represent some major search interests, and that they are effective features for categorizing query terms into certain categories. In fact, Fig. 4 shows that a small set of precategorized core terms, e.g., 1000–3000, was useful for achieving an acceptable performance. This number is much smaller than the total number of query terms. However, there were weaknesses in our initial study.

One of the factors that may weaken our approach is the weak representation of corresponding retrieved documents for test query terms. We represent each document using only the title and description extracted from the top 100 search results from search engines. The titles are normally useful. However, the descriptions are usually autogenerated by the search engines and, thus, are often not precise or meaningful. One possible alternative way is to use the document contents or the anchor texts of that page, which are texts associated with links that point to that page. If this kind of representation is used, it will be necessary to run a Web crawler to download the corresponding pages. This requires lots of band width and storage space, so this approach is not suitable under most environments. In addition, due to the hypertext design principle, the web page content may also be not representative enough. Anchor texts are sometimes precise descriptions for a page, but they are usually short and must be interpreted in their context. Thus, using anchor texts as the representation of a document may make it too narrow for obtaining a sufficient feature term set.

One other reason is the ambiguous nature of terms. As we have mentioned, query terms are usually very short. This means that some terms have multiple information requests. Comparing the performance of top 3 or 5 with that of top 1, there is obvious improvement. This shows that our approach to multicategorization is still effective. However, determining how many categories should be chosen has not yet been explored.

Analyzing the instances of erroneous categorization of query terms by the machine for each subject category, it is noted that some categories tend to have more ambiguous or annoying terms than others, such as the Computer and Network category. These terms usually have little discrimination value for categorization and prevent correct category assignment for each term. For example, many Web documents contain some computer-related terms like ‘‘search,’’ ‘‘Web,’’ and ‘‘homepage;’’ hence, it is very likely that query terms containing these feature terms in their retrieved documents will be assigned to the Computer and Network category. In other words, these annoying terms act like stop words and need to be filtered out from the feature term set to prevent inappropriate categorization.

Furthermore, each category poses different problems that need to be solved. For example, personal name identification techniques are useful for dealing with the Entertainment/Individual subcategory since query terms belonging to this category are mostly personal names. Considering the sample query terms ‘‘michael jackson’’ and ‘‘meg ryan’’ listed in Table 4, they were not correctly categorized into the Entertainment/Individual category. However, they are really suggested into related Entertainment subcategories.

In addition, some other factors may affect the correctness of category assignment and need to be further studied, such as the relevance and numbers of the retrieved documents, and the sufficiency of the surrogates of these documents as described in the previous paragraphs. Also, as a task of categorization into hierarchical taxonomies, there are still many approaches that need to be explored to better utilize the hierarchical structure, such as that of applying deeper analysis of terms to terms and of terms to subjects to determine flexible features for each interior node in the taxonomy [12].

The experimental results are promising that various new terms given by users can be categorized automatically or semiautomatically if high categorization accuracy is required. To make our approach adaptive, we only need to apply human effort periodically to examine whether the initial feature terms are appropriate or not and perform updating if necessary. Using this human –machine integrated approach, terms can be categorized properly.

## 5. Discussion of possible applications

Our term categorization approach for real-world query terms may be useful in some applications.

## 5.1. Live thesaurus construction

Query term categorization serves as a first step in the construction of a thesaurus for Web search. For query terms categorized in the same classes, more accurate relationships between terms such as abbreviations, synonyms, related terms, broader terms, narrow terms, and translations might be further discovered. Such thesaurus information can be very useful in some applications, such as term suggestion for interactive Web search [8].

Our work provides a good beginning for constructing such a Web thesaurus. Through the term categorization process, terms can be grouped into several meaningful subject categories. With subject information of each term, some kind of term suggestion can be performed. Furthermore, if we think a category is still too rough to convey a strong relationship between terms, we can apply some clustering techniques to terms in the same category. This will reduce the size of the term set for the clustering algorithm and, of course, enable it to more efficiently and reliably find really relevant terms without disturbance from other irrelevant terms.

## 5.2. Sensitive query filtering

To prevent commercial search engines from providing inappropriate information to certain users like children, it is necessary to have a query term filter for filtering out sensitive query terms, such as pornography-related terms. The query term filter problem is similar to the search term categorization problem: the problem is to determine whether a given term can be categorized as porn-related or not. Our approach directly provides a possible solution to this problem. Table 5 shows some other statistics of the categorization with the first-level 14 major categories from our previous experiment described in Section 4. Recall that the experiment was conducted 20 times on 1000 randomly selected terms of each time for a total of 20,000 trials. Each table cell shows, for one category, the recall rate, the rate of terms in that category being correctly categorized, and the precision rate, the rate of terms categorized in that category really belonging to that category. The results show that the proposed method can be applied to query term filtering within such categories as Adult, Computer, etc. The proposed approach is useful for collecting users’ query terms in these domains. Combined with final examination by humans, a collection of query terms can be incrementally updated. A real-world query term filter for filtering out pornography-related terms for Web image search has been successfully developed, and more than 20,000 sensitive query terms have been collected using the proposed approach.

## 5.3. Observation of Web users’ search interests [16]

Information about the needs of Web users is valuable for enhancing the effectiveness of search engines and Web content organization. The query term logs of search engines are considered to be the most useful data for monitoring users’ information needs and search interests. With our approach to subject categorization of query terms, it is a straightforward task to construct an automatic system for Web search engines or digital library systems to monitor changes in users search requests, including the distribution of users search subject categories, and the frequencies of the query terms in each category. To show this idea more clearly, the distribution of information requests of some subject categories from the analysis of D-1998’s log is depicted in Fig. 6. Among the 14 major categories, the Computer category has the highest percentage of queries, 19.9%, followed by Adult at 16.9%, Entertainment at 9.8%, and so on. Each major category is also decomposed by related subcategories. Obviously, an up-to-date distribution of the information needs corresponding to each subject category can be easily obtained using our approach.

Table 5  
Recall/precision statistics of categorization with the first-level 14 major categories

<table><tr><td></td><td>Humanities</td><td>Business</td><td>Computer</td><td>Education</td><td>Entertainment</td><td>Chat</td><td>Game</td></tr><tr><td>Top 1</td><td>43.41/70.10</td><td>70.38/62.41</td><td>80.11/53.29</td><td>72.28/76.48</td><td>55.36/75.86</td><td>57.35/63.71</td><td>65.51/77.07</td></tr><tr><td>Top 3</td><td>71.26/40.39</td><td>91.81/28.15</td><td>96.07/22.35</td><td>92.16/43.06</td><td>80.44/46.61</td><td>85.60/30.81</td><td>87.69/51.66</td></tr><tr><td></td><td>Health</td><td>Science</td><td>Shopping</td><td>Media</td><td>Society</td><td>Adult</td><td>Travel</td></tr><tr><td>Top 1</td><td>70.07/77.22</td><td>43.10/43.43</td><td>60.60/60.95</td><td>54.74/49.87</td><td>41.21/78.75</td><td>51.26/81.02</td><td>74.51/56.63</td></tr><tr><td>Top 3</td><td>86.98/54.41</td><td>74.20/12.07</td><td>91.45/21.58</td><td>83.03/20.86</td><td>78.17/38.61</td><td>75.92/65.49</td><td>90.40/21.53</td></tr></table>

![](/api/attachments/XJNW7TXK/fulltext/images/99c20c0d1b9f7216e6261a4494151cde37a387b491348a29c82327035d8a411b.jpg)  
Fig. 6. An illustration of an information request distribution for some subject categories.

## 5.4. Web page classification/filtering

The problem of classifying Web pages is undoubtedly very important in today’s Web environment, and it also presents a big challenge to the traditional text classification approaches. When we consider the determination of the class of a document made by a human being, we can obviously observe that the determination of the target class is usually dependent on only a few dominate key terms. When conventional machine learning approaches are applied to some corpora, the effect of such key terms may been decreased by other unrelated terms. This phenomenon is more obvious in the Web page environment. Imagine the difficulty of classifying a company’s front page containing only a few images or animations. In such a case, the traditional term-based approach can only depend on the page title or anchor texts from other pages pointing to the candidate page. Such contents are usually very brief, and only one or two key terms can be used to determine the class of the pages. Search logs provide us with a good source of vocabularies used in Internet communities. By associating each term with some subject information using our approach, we may be able to form these query terms into a good feature set for classifying Web pages. Because this is surely an another big problem and much work needs to be done, we only point out this idea here.

## 6. Conclusion remarks

In this paper, we have presented an approach to categorizing query terms that are obtained from on-line search engine logs into broader subject categories of taxonomies for use in Web applications. The approach successfully integrates human and machine efforts. First, a set of high-frequency core query terms along with their subject information can be determined by human experts. With this seed core term set, an automatic categorization process can be developed for categorizing each newly given query term. The experimental results show that various new terms given by users can be categorized automatically, and this gives that that our approach can be applied as a good beginning for constructing Web taxonomies or for enriching existing ones using query terms. Other applications that can benefit from our work have also been pointed out.

## References

[1] E. Agirre, O. Ansa, E. Hovy, D. Martinez, Enriching Very Large Ontologies using the www, ECAI 2000, Workshop on Ontology Learning, Berlin, Germany.

[2] P.G. Anick, S. Tipirneni, The paraphrase search assistant: terminological feedback for interactive information seeking, Proceedings of the 22nd ACM International Conference on Research and Development in Information Retrieval (SIGIR’99), Berkeley, USA, August 15 – 19, 1999, ACM Press, New York, USA, 1999, pp. 153 – 159.

[3] D. Beeferman, A. Berger, Agglomerative clustering of a search engine query log, Proceedings of the Sixth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Boston, MA, USA, August 20 – 23, 2000, ACM Press, New York, USA, 2000, pp. 407 – 416.

[4] P. Bruza, R. McArthur, S. Dennis, Interactive internet search: keyword, directory and query reformulation mechanisms compared, Proceedings of the 23th ACM International Conference on Research and Development in Information Retrieval (SIGIR’2000), Athens, Greece, July 24 – 28, 2000, ACM Press, New York, USA, 2000, pp. 280 – 287.

[5] R. Byrd, Y. Ravin, Identifying and extracting relations in text, Proceedings of the Fourth International Conference on Application of Natural Language to Information Systems (NLDB’99), Austria, June 17– 19, 1999.

[6] L.-F. Chien, Pat-tree-based adaptive keyphrase extraction for intelligent Chinese information retrieval, Information Processing & Management 35 (1999) 501 – 521.

[7] L.-F. Chien, H.-T. Pu, Important issues on Chinese information retrieval, Computational Linguistics and Chinese Language Processing 1 (1) (1996) 205– 221.

[8] S.-L. Chuang, H.-T. Pu, W.-H. Lu, L.-F. Chien, Autoconstruction of a live thesaurus from search term logs for interactive web search, Proceedings of the 23rd Annual International ACM SIGIR Conference on Research and Develop ment in Information Retrieval (SIGIR2000), Athens, Greece, July 24– 28, 2000, ACM Press, New York, USA, 2000, pp. 334– 336.

[9] S. Deerwester, S.T. Dumais, G.W. Furnas, T.K. Landauer, R.A. Harshman, Indexing by latent semantic analysis, Journal of the American Society for Information Science 41 (6) (1990) 391 – 407.

[10] C. Fellbaum, Wordnet: An Electronic Lexical Database, MIT Press, Cambridge, 1998.

[11] U. Hahn, K. Schnattinger, Towards text knowledge engineering, Proceedings of the 15th National Conference on Artificial Intelligence (AAAI’98), Madison, Wisconsin, USA, July 26 – 30, 1998, AAAI Press, Menlo Park, California, USA, 1998, pp. 524 – 531.

[12] D. Koller, M. Sahami, Hierarchically classifying documents using very few words, Proceedings of the Fourteenth International Conference on Machine Learning (ML’97), Nashville,

Tennessee, USA, July 6 – 12, 1997, Morgan Kaufmann, San Francisco, USA, 1997, pp. 170– 178.

[13] A. Maedche, S. Staab, Discovering conceptual relations from text, Proceedings of the 14th European Conference on Artificial Intelligence (ECAI-2000), Berlin, Germany, August 20 – 25, 2000.

[14] A. Maedche, S. Staab, Mining ontologies from text, Proceedings of the 12th International Conference on Knowledge Engineering and Knowledge Management (EKAW-2000), Juanles-Pins, French Riviera, France, October 2 – 6, 2000, Springer-Verlag, Heidelberg, Germany, 2000.

[15] R. Mandala, T. Tokunaga, H. Tanaka, Combining multiple evidence from different types of thesaurus for query expansion, Proceedings of the 22nd ACM International Conference on Research and Development in Information Retrieval (SIGIR’99), Berkeley, USA, August 15 – 19, 1999, ACM Press, New York, USA, 1999, pp. 191 – 197.

[16] H.-T. Pu, S.-L. Chuang, Auto-categorization of search terms toward understanding web users’ information needs, Proceedings of the 3rd International Conference of Asian Digital Library (ICADL2000), Seoul, Korea, December 6– 8, 2000.

[17] E. Riloff, J. Shepherd, A corpus-based approach for building semantic lexicons, Proceedings of the Second Conference on Empirical Methods in Natural Language Processing, Providence, Rhode Island, USA, August 1– 2, 1997.

[18] M. Sanderson, B. Croft, Deriving concept hierarchies from text, Proceedings of the 22nd ACM International Conference on Research and Development in Information Retrieval (SIGIR’99) (1999) pp. 206– 213.

[19] C. Silverstein, M. Henzinger, H. Marais, M. Moricz, Analysis of a very large altavista query log, DEC SRC Technical Note, 1998.

![](/api/attachments/XJNW7TXK/fulltext/images/96c6f51632350060f98ec0ecbdc6453597553215754b5401110beffcd7bc8235.jpg)

Shui-Lung Chuang is a research assistant at the Institute of Information Science, Academia Sinica, Taiwan, for his military service since October 1999. He received his BS and MS degrees in Computer Science and Information Engineering from the National Taiwan University in 1997 and 1999, respectively. His master thesis was on information extraction from Web resources, and won the Best Thesis Award from ACM Taipei Chapter in 1999.

Currently, his research interests include Web information retrieval and mining, knowledge acquisition and organization, text classification, and intelligent agent.

![](/api/attachments/XJNW7TXK/fulltext/images/54f713c6d639c922ca2cd506b38d74a348936de8b8896b3cd16899efad5c77a9.jpg)

Lee-Feng Chien received his Computer Science PhD at the National Taiwan University in 1991. Since 1993, Dr. Chien joined in the Institute of Information Science, Academia Sinica, and is currently an associate research fellow of the Institute. Dr. Chien’s research interests include information retrieval, Web mining, spoken language processing, and natural language processing. In these areas, he has published over 100 technical articles in scien-

tific journals and conference proceedings such as IEEE Trans SAP, Computational Linguistics, JASIS, IP&M, ACM SIGIR, ICASSP, COLING, ACL, WWW, etc. Dr. Chien is currently an associate editor of ACM Transaction on Asian Language Information Processing. Besides, he usually served as a committee member in international conferences, such as a PC member of ACM-SIGIR’99, 00, 01, IRAL’97 00, ICCPOL’95 99, and the PC chair of the 1999 International Workshop on Information Retrieval with Asian Languages (IRAL’99). He was a co-recipient of the 1998 ACM SIGIR Best Poster Presentation Award for Late-breaking Research in Melbourne and a co-adviser of the recipient of the 1999 ISCSLP Best Student Paper Award in Singapore. He was also the owner of the 1997 K.T. Li Award by ACM Taipei Chapter for his contribution in Chinese Information Retrieval.
