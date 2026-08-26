---
otero_id: 3138
otero_key: "R398KKEW"
title: "Quality Assessment of Peer-Produced Content in Knowledge Repositories using Development and Coordination Activities"
authors: "Srikar Velichety; Sudha Ram; Jesse Bockstedt"
year: "2019"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2019.1598692"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Quality Assessment of Peer-Produced Content in Knowledge Repositories using Development and Coordination Activities

Srikar Velichety, Sudha Ram & Jesse Bockstedt

To cite this article: Srikar Velichety, Sudha Ram & Jesse Bockstedt (2019) Quality Assessment of Peer-Produced Content in Knowledge Repositories using Development and Coordination Activities, Journal of Management Information Systems, 36:2, 478-512, DOI: 10.1080/07421222.2019.1598692

To link to this article: https://doi.org/10.1080/07421222.2019.1598692

![](/api/attachments/R398KKEW/fulltext/images/bbd1246baa1989e26db245588699ebdfc2e3a04fa73f700223ce25b1a6b8d02d.jpg)

View supplementary material

![](/api/attachments/R398KKEW/fulltext/images/ee1e3571ab7e74143b75b398361d71e9c43ab3e3f0ff9f779c024a47519a6bbc.jpg)

Published online: 14 Jun 2019.

![](/api/attachments/R398KKEW/fulltext/images/36142fbdd65e471eb29f0d9f9be071f58212938e0c969316ca92be7cdc3d3a4b.jpg)

ubmit your article to this journal

![](/api/attachments/R398KKEW/fulltext/images/3857e787db52d3693021d1705b7e6b61c26fed3b95a1905c2495b6a2d9c430b8.jpg)

Article views: 131

![](/api/attachments/R398KKEW/fulltext/images/869c0f3d3683177e7ad4759fcfe03459920bf7461668f63c507ac35a18ae0320.jpg)

View Crossmark data

# Quality Assessment of Peer-Produced Content in Knowledge Repositories using Development and Coordination Activities

SRIKAR VELICHETY, SUDHA RAM, AND JESSE BOCKSTEDT

SRIKAR VELICHETY (svlchety@memphis.edu; corresponding author) is an Assistant Professor of Business Information and Technology at the Fogelman College of Business and Economics at the University of Memphis. He received his Ph.D. in Management Information Systems from the Eller College of Management, University of Arizona. Dr. Velichety’s research interests lie in social media and social networks, user-generated content, and predictive analytics.

SUDHA RAM (ram@eller.arizona.edu) is Anheuser-Busch Endowed Professor of MIS, Entrepreneurship and Innovation in the Eller College of Management, and director of the INSITE: Center for Business Intelligence and Analytics at the University of Arizona. She received her Ph.D. from the University of Illinois at Urbana-Champaign. Dr. Ram’s research focuses on business intelligence, large scale networks, data mining, and Big Data analytics, using such methods as machine learning, statistical approaches, ontologies, and conceptual modeling. Dr. Ram has published more than 200 articles in such journals as Information Systems Research, Management Science, MIS Quarterly, Journal of Management Information Systems, IEEE Transactions on Knowledge and Data Engineering, and Communications of the ACM.

JESSE BOCKSTEDT (bockstedt@emory.edu) is an associate professor of Information Systems and Operations Management in the Goizueta Business School at Emory University. He received his Ph.D. from Carlson School of Management at the University of Minnesota. He studies user behavior and economic issues in environments that rely on information technology. His research has appeared in a variety of journals, including Information Systems Research, MIS Quarterly, Journal of Management Information Systems, Journal of Operations Management, and Production and Operations Management.

ABSTRACT: We develop a method to assess the quality of peer-produced content in knowledge repositories using their development and coordination histories. We also develop a process to identify relevant features for quality assessment models and algorithms for processing datasets in large-scale knowledge repositories. Models using these features, on English language Wikipedia articles, outperform existing methods for quality assessment. We achieve an overall accuracy of 81 percent which is a 7 percent improvement over existing models. In addition, our features improve the precision and recall of each class up to 9 percent and 17 percent respectively. Finally, our models are robust to ten-fold cross validation and techniques used for classification. Overall, our research provides a comprehensive design science framework for both identifying and efficiently extracting features related to development and coordination activities and assessing quality using these features. We also provide details of potential implementation of a quality assessment system for knowledge repositories.

KEY WORDS AND PHRASES: knowledge repositories, Wikipedia, peer-produced content, design science, big data analytics, predictive analytics.

## Introduction

Knowledge repositories on the internet have increased in popularity since the emergence of the social web. Leveraging the model of peer-production, these repositories not only provide freely accessible content but also an opportunity for anyone to edit and improve that content [71]. Wiki-based knowledge repositories (that leverage a model of peer-production) have proven to be the most popular and successful [9], both in public and private/organizational contexts. Among all these repositories, Wikipedia is an epitome of success.

Research studies have determined that the quality of articles on Wikipedia is comparable to those of Encyclopaedia Britannica [26], and indeed Wikipedia put the latter out of business [11]. This world’s largest open source knowledge repository to date has impacted a variety of social and economic contexts including court cases [16], flu forecasting [8], financial markets [81], and more recently assisted in fighting fake news on community video platforms such as YouTube [13]. Inspired by the success of Wikipedia, today there are more than fifty services on the Internet that host free access web-collections spanning a diverse range of topics such as science, TV Shows, sports, technology, fiction, and events to name a few [27].

Despite the much-celebrated success of these knowledge repositories, there is still a debate about the quality of information in these collections and how it is assessed. For example, Wikipedia introduced a quality rating system for its articles where grades are assigned to specific articles using a peer-review system. The standard four quality grades in order from highest to lowest are Featured (FA),<sup>1</sup> Good (GA),<sup>2</sup> B,<sup>3</sup> and C<sup>4</sup>. (There is also a grade A, but it is assigned only to articles related to war and military.) Articles are assigned a “Start/Stub” status when they are created and should at least be “substantially developed” (minimum of 350 words) to be considered for a “C” grade. As of October 2018, a mere 0.1 percent of the nearly six million articles in the English language version of Wikipedia have “Featured” status, which means the article is well written, structured and reliable. Moreover, only seven percent of all articles on Wikipedia have ever received a grade through the peer-review system.

Assigning quality grades to articles using this system is a time consuming and human intensive process where each article needs to be reviewed, often by multiple editors, as per the published quality criteria. Moreover, manual reviews are subject to human biases in judgement [27, 30]. Also, this process needs to be repeated whenever the content or the quality assessment criteria are updated [18, 77]. Considering that currently every second there are ten edits on an average to Wikipedia articles, it is impossible to scale this manual peer-review system to all articles on Wikipedia, let alone all of the peer-produced knowledge repositories [30, 42]. Because of this scalability issue with the present manual peer-review system, many articles on Wikipedia that deserve one of the four quality grades are not get assigned one.

The past few years have seen an increasing interest in the development of scalable quality assessment methods for content in peer-production communities [10, 12, 18, 27, 30, 42, 46, 47, 52, 66, 68, 69, 77, 79, 80]. More specifically, there is increasing evidence for the use of features related to coordination of content development efforts (i.e., discussion pages [33, 59, 60, 67, 75]), for quality assessment. However, most of the recent studies in this area have used simple metrics such as the number of comments, participating editors, and number of threads as proxies for coordination activity [40, 41]. Given that editors participate across different threads and contribute to discussions about different article development activities at various points of time [44, 75], we believe that a set of much richer and comprehensive features derived from the discussion page can be used to improve our ability to accurately predict article quality. In addition, there is limited understanding of the relationship between the activities of the editors, who participate in both development and coordination, and article quality [40]. Moreover, there has been a limited amount of work using a combination of development and coordination features (i.e., different types of collaboration features) for automating quality assessment in peer-produced content [18, 23, 43, 66, 80]. Finally, much of the prior work aims at either differentiating Featured articles from the rest or at differentiating Featured and Good articles from the rest instead of assigning one of the four quality grades. When we put all of this together, two important research questions arise: (1) What features of coordination (discussion) are useful in assessing article quality? (2) What is the relationship between coordination (discussion) and development (editing) activities of the contributors who participate in both and how does this relationship contribute to assessing article quality? Answering these two questions will help in the development of more accurate quality assessment strategies for peer-produced content in knowledge repositories. It will also enable the design and implementation of automated quality assessment tools that overcome the scalability problems associated with the present peer-review method.

In this research, we use the nominal process model for design science research proposed by Peffers et al. [55] to answer our questions and provide a scalable quality assessment method, with Wikipedia as the focal context. We leverage the knowledge about not just the way an article is written and presented (which are the only features used at present to judge the quality), but also the way the article was developed (i.e., editing and the way the development efforts were coordinated, e.g., discussions). The combination of and relationship between these two sets of features allow us to develop a robust quality assessment method. We also leverage the complete population of graded English language Wikipedia articles instead of a stratified random sample to harness the power of big data analytics in identifying a set of relevant features that lead to high performing predictive models [2, 5, 20, 38]. In doing so, we provide a method for quality assessment and a process for identifying relevant features, which includes algorithms for extracting edit and discussion histories from large-scale knowledge repositories (both open and organizational). Our results demonstrate significant improvements over existing approaches to quality assessment in peer-produced knowledge repositories. We also discuss the details of the architecture and implementation of an automated quality assessment system that leverages results of this research. Our research also contributes to the application of big data, which is defined as large scale datasets that are too big, complex and variegated to be handled by traditional computational infrastructure such as personal computers, spreadsheets, and relational databases [72], in developing novel artifacts for description and prediction using design science research [1, 2, 21, 37, 83].

## Previous Work

Research on developing methods for quality assessment of peer-produced content in knowledge repositories can be broadly divided into three categories based on the features used.

The first category uses features related to the content and structure of the article. Blumenstock [10] showed that a simple count of the number of words in the article can differentiate featured articles from the rest. Building on this work, Lipka and Stein [47] measured the writing style of the article, using unique trigram representations, and found it to be more effective than edit history in identifying featured articles. Similarly, Hasan Dalip et al. [27] found that textual indicators related to length, style, and structure were most relevant in classifying articles into different quality grades. More recently, Dang and Ignat [18] used a combination of content and structure based features to classify articles into four quality grades and found substantial increases in both accuracy and information gain over the existing approaches.

The second category uses features related to edits and contributors. Stvilia et al. [66] used seven different metrics, calculated using the article and edit characteristics, to separate featured articles from random articles. They found that all these metrics differentiated featured articles from random articles. Along similar lines, Suzuki and

Yoshikawa [69] proposed metrics for edit and contributor quality using the edit longevity and found that these metrics differentiate Featured (FA) articles from Good (GA) articles. Wöhner and Peters [79] proposed life cycle metrics based on edit longevity and found that these can differentiate high quality (Featured and Good) articles from low quality ones. In a similar piece of work, Suzuki [68] proposed a h-index measure, that assigns a quality score to the editor using his edits to other pages on Wikipedia, and found that it outperforms existing peer review methods for quality assessment. Finally, Hu et al. [30] proposed three different models for article quality assessment using the interaction between articles and contributors. They found that a model that uses the probability of an article being partially reviewed by a contributor, in addition to the contributions, gives the best results.

The third category uses network-based approaches to derive features related to interactions among edits and contributors. Brandes et al. [12] found the structural network characteristics of the interaction network among editors to be highly correlated to article quality. Wu et al. [80] used the motif counts of the edit network around an article and found it to be effective in classifying articles on the basis of quality. However, Hasan Dalip et al. [27] found that citation network characteristics are not useful predictors for article quality. Li et al. [46] complemented the features of article-editor network with measures of editor contribution to build weighted models for quality assessment. Recently, de La Robertie et al. [42] used the co-edit graphs of individuals (using the editing activity) and found that good articles are a result of grouping of expert users. More recently, Liu and Ram [49] defined and quantified three types of social capital (i.e., Internal Bonding, External Bridging, and Functional Diversity) and found that each of them had a significant impact on the quality of articles. They also found that internal bonding interacts positively with external bridging to produce higher quality articles.

To our knowledge, no known research thus far has looked at how features related to various aspects of coordination of development efforts (i.e., discussions and the relationship between coordination and development efforts, such as editing, can be used to assess article quality). Liu and Ram [48] developed a three step approach to identify the roles of editors, measure their collaboration on edits and quantify the impact of this collaboration on article quality. However, their approach does not consider the coordination of development efforts (i.e., discussions). Since discussions represent the volume and nature of efforts in coordinating various content development activities, we posit that the comprehensive set of features derived here can add significant value to quality assessment. Also, the relationship between edits and discussions represents how article development and coordination activities are related and hence can also provide appropriate features for quality assessment. Thus, we propose to use a combination of these two feature sets to assess the quality of peer-produced content in knowledge repositories.

## Research and Design Process

Peffers et al. [55] proposed a nominal process model for design science research that has seven stages: identifying the problem and motivation, defining the objectives of the solution, design and development, demonstration, evaluation, and communication. Figure 1 maps the steps in our research to this process.

The problem we aim to address with our research is to efficiently assess the quality of peer-produced content in knowledge repositories using features related to content, collaboration, and the relationship between different types of collaboration such as development and coordination. The objective is to provide a method for quality assessment and a process for identifying relevant features which includes algorithms for dealing with edit and discussion histories in large-scale knowledge repositories in a computationally efficient way.

Hevner et al. [28, p. 77] define artifacts as “constructs, models, methods, instantiations or properties of technical, social and or informational sources.” To address this research problem and meet our objectives, we create an artifact that is a combination of the method used for quality assessment of peer-produced content in knowledge repositories, and the process used to identify relevant features in a computationally efficient way from large-scale edit and discussion history data. The motivation for our proposed method is grounded in the results of prior research, which say that quality of peer-produced content is a function of knowledge from multiple types of collaboration (development (edits) and coordination (discussion) activities) and the relationships among them supplemented with the properties of the content [34, 35, 36]. Our process starts with an initial set of features based on prior research and leverages large-scale analytics and algorithms on multiple types of data (i.e., big data) to identify additional robust sets of relevant features. The design phase in this research has broadly three sub-phases.

The first sub-phase involves feature engineering to identify an initial set of features related to article development and coordination. Shmueli [62] posits that the choice of features in a prediction model is dependent on the quality of association between the predictors and the response, data quality, and their exante availability at the time of prediction. In this approach, we start with an initial set of discussion features based on existing work and knowledge about how discussion pages are used and what article characteristics are used for quality assessment.

![](/api/attachments/R398KKEW/fulltext/images/aed87246b9ebf46806b60ad2066468a219f0ef9c386f3b21be16c43095dba961.jpg)  
Figure 1. Design Process Model

The second sub-phase involves feature engineering and analysis to understand if there is any link between various discussion characteristics and quality. In other words, this sub-phase answers the question: “What features of coordination (discussion) are useful in assessing article quality?” In this sub-phase, we use features from the first sub-phase and analyze their relationship to article quality. As a result, we identified additional features that have a significant association with article quality and develop algorithms to extract them. Here, we also develop a combined machine learning and human encoding technique to comprehensively extract topics from large-scale textual data (details of which are provided in Appendix A).

The third sub-phase involves an analysis to understand the link between the collaborative patterns of editors, who participate in both discussions and editing, and article quality. In other words, this sub-phase answers the question: “What is the relationship between coordination (discussion) and development (editing) activities of the contributors who participate in both and how does this relationship contribute to assessing article quality?” Here, using customized metrics, we extract the different roles that editors play in different types of discussions and editing. Considering the large dataset (i.e., the entire Wikipedia corpus), we develop and implement a scalable map-reduce algorithm [19].<sup>5</sup> We also learn how editors in these roles collaborate and quantify the proportion of edits and discussions of certain type performed by a role [48]. We then discover how this collaboration is associated with article quality. The goal of these two phases is to identify appropriate features that provide inputs to the quality assessment model.

In the demonstration phase of the design process model (Figure 1), we leverage features identified in the design phase to build models for assessing article quality. We describe the details of the machine learning algorithms used to build quality assessment models and the various metrics used for evaluating them. We also describe the statistical methods used for deriving the standard errors and the confidence intervals.

In the evaluation phase, we compare performance of our models with models that use: (a) only the article development (edit) characteristics, (b) only the coordination (discussion) characteristics, and (c) a combination of the two. We test the robustness of the identified features to the choice of the dataset and the technique used for classification. In addition, we quantify the value each of these features adds to the overall quality assessment. Finally, we also analyze and describe the real-world implications of these results in terms of assigning correct quality grades to peerproduced content.

Finally, in the communication phase, building on the results from evaluation, we describe how this research can be used to implement a system for automated quality assessment of peer-produced content in knowledge repositories. We provide the technical specifications for the system, the computational complexity for each of the involved tasks and the estimated time required for completing these activities.

## Data Description

We use a dataset of all articles from the entire English language version of Wikipedia as of November 2014. Wikipedia provides an $\mathrm { A P I } ^ { 6 }$ that allowed us to also download the discussion pages and edit history of these articles. As of November 2014, English Wikipedia had 4.7 million articles. Since our goal is to predict quality, we use the complete corpus of articles for English Wikipedia that have received one of the standard four quality grades (i.e., FA, GA, B, and C). Using such a large dataset reveals patterns that are representative of true underlying relationships in the data that can in turn be leveraged to build high performing models [4, 20, 38, 39]. We do not consider articles that belong to A-class as most of them are related to topics on war and military and, hence, may cause a bias in the sample [48]. We also eliminate articles in the Start/Stub class because most of them either do not have any comments or have very few comments on their discussion pages [44]. Moreover, many of them were written by a single editor. For the articles in the standard four quality grades, we consider the discussions until the point of time the article was first submitted for review for a quality grade. Together, we had 67,390 articles with one of the four assigned grades.

Existing studies [7, 35, 40] have shown that article ratings from external raters and the Wikipedia quality ratings are significantly correlated (Spearman’ rho = .54, p < .001). Also, there are no available statistics on how many articles would have received one of the four quality grades but did not get one because of scalability issues with the peer-review process and hence we do not use any article that does not have an assigned grade. In addition, considering the growing popularity of Wikipedia over the past decade fueled by the increasing quality of content on the knowledge repository [11, 13, 16, 26], we believe that these quality ratings, though not guaranteed to be completely objective and neutral, are reliable indicators of article quality. Furthermore, using the labels derived from Wikipedia’s own peer review process, in developing our models, is appropriate given our goal is to automate the existing quality assessment process. Table 1 provides the descriptive statistics of the complete dataset, which was close to 2TB after cleaning.

Table 1. Descriptive Statistics of our Dataset

<table><tr><td></td><td>FA</td><td>GA</td><td>B</td><td>C</td></tr><tr><td colspan="5">Discussion Page Characteristics</td></tr><tr><td>Number of Articles in the Corpus</td><td>3968</td><td>18213</td><td>55613</td><td>88915</td></tr><tr><td>Number of Articles with at least one comment on discussion page</td><td>3772</td><td>15978</td><td>34782</td><td>53217</td></tr><tr><td>Number of Articles with at least once comment before submitting for review</td><td>2716</td><td>10816</td><td>22238</td><td>31620</td></tr><tr><td>Number of Articles with at least five contributors</td><td>867</td><td>2584</td><td>4297</td><td>5826</td></tr><tr><td>Number of Comments</td><td>99411</td><td>157768</td><td>295704</td><td>364646</td></tr><tr><td>Number of Threads</td><td>32778</td><td>48330</td><td>112060</td><td>143271</td></tr><tr><td>Number of Unique editors</td><td>20377</td><td>32884</td><td>69069</td><td>88742</td></tr><tr><td>Number of Signed Comments</td><td>92528</td><td>145140</td><td>262763</td><td>319039</td></tr><tr><td>Number of Anonymous comments</td><td>6883</td><td>12628</td><td>32941</td><td>45607</td></tr><tr><td>Average Length of the Comment (Words)</td><td>51.21</td><td>45.82</td><td>54.43</td><td>53.29</td></tr><tr><td>Average Length of the Comment (Characters)</td><td>254.00</td><td>228.69</td><td>273.77</td><td>268.91</td></tr><tr><td>Average Depth per article</td><td>1.95</td><td>2.19</td><td>1.04</td><td>0.95</td></tr><tr><td colspan="5">Article Characteristics</td></tr><tr><td>Average No of Edits</td><td>440.89</td><td>309.95</td><td>393.14</td><td>363.27</td></tr><tr><td>Average No of Contributors</td><td>224.12</td><td>135.60</td><td>213.51</td><td>180.57</td></tr><tr><td>Average No of Anonymous Contributors</td><td>304.96</td><td>186.60</td><td>282.90</td><td>222.25</td></tr><tr><td>Average Images</td><td>87.76</td><td>48.56</td><td>64.42</td><td>44.93</td></tr><tr><td>Average Internal References</td><td>850.53</td><td>642.65</td><td>862.17</td><td>701.94</td></tr><tr><td>Average External References</td><td>294.25</td><td>227.29</td><td>266.15</td><td>197.11</td></tr><tr><td>Average Information Presentation</td><td>6.22</td><td>5.85</td><td>6.38</td><td>6.08</td></tr><tr><td>Average Reading Complexity</td><td>19.45</td><td>20.09</td><td>21.16</td><td>21.72</td></tr><tr><td>Average Article Length</td><td>5127.79</td><td>3181.09</td><td>3552.54</td><td>2736.54</td></tr><tr><td>Average Age (days)</td><td>1384.97</td><td>1268.50</td><td>1177.57</td><td>1631.55</td></tr></table>

## Design: Feature Engineering, Data Analysis, and Algorithms

In this section, we describe the process we used to identify various features for our models. We also describe the data analysis used to identify additional features. We have three sub-phases in design: (1) feature engineering for initial set of discussion, article, and editor experience features; (2) feature engineering and analysis for identifying additional discussion features; and (3) feature engineering for identifying the relationship between discussions and editing. The purpose is to identify a comprehensive set of features that encompass development, coordination and the relationship between the two, to assess article quality.

Phase 1: Feature Engineering for Initial Set of Features

Here, we describe how we identify the initial set of discussion page features for the first sub-phase of our design. Figure 2 shows a sample discussion page for a Wikipedia article titled “The Great Auk.”

![](/api/attachments/R398KKEW/fulltext/images/3c723149e46b7ad87c24908288cea54130052ca76ea885c89380cdaa3e0f4133.jpg)  
Figure 2. Sample Discussion Page

We can observe that there are various editors participating in these discussions. We can also observe that there are discussions regarding various aspects of article development by different editors at different points in time. Finally, we can observe that people reply to each other’s comments, thus participating in various aspects of article development. These discussion pages are not idiosyncratic to Wikipedia and are an integral part of any knowledge repository based on Wiki technology (online or offline, open or organizational).

Based on these observations, which indicate that there are volume, structural, temporal, and topical aspects in discussions and drawing on previous work on discussion pages [33, 41, 44, 60], we defined and extracted three categories of features in this first design phase.

1. General features that measure the activity on a discussion page [34, 40].

2. Structural Features that represent and quantify the comment-reply chains, temporal nature, and extent of participation in discussions.

3. Textual features that represent the types of topics discussed and the tone (sentiment) of discussions.

Kittur and Kraut [40] used the number of edits on a discussion page as a measure of explicit coordination. Kane [33] used the total number of editors in both the edit and discussion pages as well as their contributions to both the edits and comments (measured using the number of comments) as a measure of volume of activity. Here, we quantify the discussion activity using four measures: number of discussion threads, number of comments, number of editors, and total discussion time (calculated from the time the first comment was posted to the time the last comment was posted before the article was submitted for review). Together, we use these four features to represent and quantify the general activity on discussion pages.

Next, we turn our attention to the structure of discussions. An examination of discussion pages reveals that most discussions are organized by threads and that discussion threads have heterogeneity in depth (i.e., varying levels of comment and reply chains, different response times, and different comment lengths). Arazy and Croitoru [6] showed how corporate wikis become inactive after a period of time and how user satisfaction leads to sustained participation. Based on this, we believe that volume of user participation in discussions across different periods in article development could possibly be used to assess its quality. Thus, we incorporate a measure to represent the temporal nature of discussion.

Finally, we can observe that there are different aspects of article development being discussed, namely, adding and deleting content, adding references, images and multimedia content, font and formatting issues, and so forth. We label these characteristics as textual activities.

Since wiki-based knowledge repositories rely on collaborative and peerproduced content, it is intuitive that high quality articles are likely to have more threads, comments, and editors than the low-quality ones. Similarly, high quality articles should be expected to have more depth in their discussions, faster response time for comments and queries, better comment readability, and a variety of topics being discussed as compared to low quality ones. A summary of the discussion characteristics is provided in Table 2. (Note that subscript i denotes an article in our sample.) The sentiment analysis was conducted using Harvard – IV dictionary [24].

Features were also derived from the article content. These features were identified from a comprehensive survey of previous literature on different article characteristics that can possibly predict quality [10, 48, 59]. These are at present the primary characteristics used by reviewers on Wikipedia to judge the quality of articles. Hence, a model for assessing article quality based on these features serves as a baseline for comparing with our proposed model. Description of these features is provided in Table 3. The extraction details are provided in Appendix B (Figures 10 and 11).

In addition, we derived several features related to the edit experience of contributors. These are shown in Table 4.

## Phase 2: Analysis and Feature Engineering of the Relationship between Discussion Characteristics and Quality

In this sub-phase of design, we examine the distributions of features (Table 2) to understand if there are any clear patterns/differences among articles in different quality grades. This also helps identify potential new features that we might have missed. In short, we answer the question: “What features of the coordination (discussion) are useful in assessing article quality?” Since we use the complete population of articles instead of a stratified sample, we posit that the patterns revealed here are representative of the true underlying relationships [20, 38, 39]. For the number of comments, threads, contributors, and anonymous contributors, we found that higher grade articles in general tend to have higher values (Figure 13 in Appendix C). We also found that higher quality articles tend to have a greater variety of aspects of article development discussed than the lower quality articles (Figure 14 in Appendix C).

Table 2. Discussion Page Activity Based Features

<table><tr><td colspan="2">General Features</td></tr><tr><td>No of  $Threads_i$ </td><td>Total number of discussions threads.</td></tr><tr><td>No of  $Comments_i$ </td><td>Total number of Comments in the discussion page.</td></tr><tr><td>No of  $Editors_i$ </td><td>Total number of unique editors who have commented.</td></tr><tr><td>No of Anonymous  $Editors_i$ </td><td>Total number of anonymous editors.</td></tr><tr><td> $Discussion\_Period_i$ </td><td>Total time elapsed between the first and last comments for the article.</td></tr><tr><td colspan="2">Structural Features</td></tr><tr><td> $Avg\_Depth_i$ </td><td>Average Depth of the Discussion Threads (Details in Appendix B – Figure 12 for the algorithm used).</td></tr><tr><td> $Avg\_Reading\_Complexity\_Comments_i$ </td><td>Average Automated Readability Index [65] calculated as 4.71×(letters/words) + 0.5×(words/sentences) - 21.43</td></tr><tr><td> $Avg\_Time\_Gap_i$ </td><td>Average Time gap between a comment and a reply across all the discussion threads.</td></tr><tr><td> $User\_Participation_i^t$ </td><td>Number of users who have participated in the discussion in a period t ∈ {1,2,3......50}. We divide the whole discussion period into 50 equal periods and calculate the number of users in each period for each article.</td></tr><tr><td> $Comments_i^t$ </td><td>Number of comments in a discussion period t ∈ {1, 2, 3......50}</td></tr><tr><td> $Gini\_Index_i$ </td><td>The Gini Index of the number of comments by the editors. This measures the inequality of user contribution across different types of comments.</td></tr><tr><td colspan="2">Text Features</td></tr><tr><td> $Avg\_Pos\_Sentiment_i$ </td><td>Average positive sentiment across all the comments in the article</td></tr><tr><td> $Avg\_Neg\_Sentiment_i$ </td><td>Average Negative sentiment across all the comments in the article</td></tr><tr><td> $Topic\_CommentX_i$ </td><td>Percentage of comments of type X in the article. The Topics of the comments are shown in Table 11 in Appendix A.</td></tr></table>

Table 3. Article Features

<table><tr><td>Feature</td><td>Description</td></tr><tr><td>Article_Lengthi</td><td>No of Words in the article.</td></tr><tr><td>Article_Agei</td><td>No of Days elapsed between the first edit to the article and the day on which it was submitted for review.</td></tr><tr><td>Contributorsi</td><td>No of Unique editors to the article.</td></tr><tr><td>Anonymous_Contributorsi</td><td>No of Anonymous contributors to the article.</td></tr><tr><td>Editsi</td><td>No of Edits made to the article.</td></tr><tr><td>Imagesi</td><td>No of Images.</td></tr><tr><td>Internal_Referencesi</td><td>No of References to other Wikipedia articles</td></tr><tr><td>External_Referencesi</td><td>No of External References to other websites and articles.</td></tr><tr><td>Information_Presentationi</td><td>Measure of level of detail reached in the article calculated as the maximum section depth reached.</td></tr><tr><td>Reading_Complexity_Articlei</td><td>Automated Readability Index calculated as 4.71*(letters/words) + 0.5*(words/sentences) - 21.43</td></tr></table>

Table 4 Edit Experience Features

<table><tr><td>Feature</td><td>Description</td></tr><tr><td> $Avg\_Article\_Experience_i$ </td><td>Average number of articles edited by all contributors before editing the focal article i.</td></tr><tr><td> $Avg\_Edit\_Experience_i$ </td><td>Average number of edits made by all contributors before editing the focal article i.</td></tr><tr><td> $Avg\_FA\_Article\_Experience_i$ </td><td>Average number of Featured (FA) articles edited before editing the focal article.</td></tr><tr><td> $Avg\_GA\_Article\_Experience_i$ </td><td>Average number of Good (GA) articles edited before editing the focal article.</td></tr><tr><td> $Avg\_B\_Article\_Experience_i$ </td><td>Average number of B articles edited before editing the focal article.</td></tr><tr><td> $Avg\_C\_Article\_Experience_i$ </td><td>Average number of C articles edited before editing the focal article.</td></tr><tr><td> $Avg\_FA\_Edit\_Experience_i$ </td><td>Average number of edits to Featured (FA) articles before editing the focal article.</td></tr><tr><td> $Avg\_GA\_Edit\_Experience_i$ </td><td>Average number of edits to Good (GA) articles before editing the focal article.</td></tr><tr><td> $Avg\_B\_Edit\_Experience_i$ </td><td>Average number of edits to B articles before editing the focal article.</td></tr><tr><td> $Avg\_C\_Edit\_Experience_i$ </td><td>Average number of edits to C articles before editing the focal article.</td></tr></table>

Another interesting finding was that the user participation, measured by the number of users participating in different development periods, was high in Featured (FA) and Good (GA) articles throughout the discussion period. In Figure 3, we divided the total discussion period into 50 equal periods and calculated the average number of users, who participated in discussions, in each period across all the articles. Similarly, we also found that Featured (FA) and Good (GA) articles tend to have more comments across different periods as shown in Figure 4. Based on these observations, we use the average number of topics, the average number of comments and active users across the article development period as additional predictors for article quality.

![](/api/attachments/R398KKEW/fulltext/images/025b607cc1fdf5ec74bf5630cad0c36d3f1fb48c869aea540c6bc10670e8331d.jpg)  
Figure 3. Period Wise User Participation Activity

Finally, we also found that within an article, features like depth across different threads, average time difference between a comment and its reply, positive and negative sentiment and reading complexity varied widely. Figures 5 and 6 show the variation in time difference and maximum depth across various threads for the article “7 World Trade Center,” which belongs to the FA-class. The Y-axis in these two figures shows the thread titles while the X-axis shows the Average Time Difference and Maximum Depth, respectively. Based on this observation, we use both the average and the skewness (measured as the ratio of median to mean) for these features as predictors. The idea here is that articles with higher quality grades tend to have more negatively skewed depth (skewed to the left) or positive sentiment (i.e., more threads with higher depths and more comments with strong positive sentiment) and more positively skewed time difference (skewed to the right) or negative sentiment (i.e., more replies with lesser response time and more comments with lesser negative sentiment).

![](/api/attachments/R398KKEW/fulltext/images/0f7cc1d773667aaf19f089d9ee1ad62735147d3f7591e5dea2f731f3a6b6fbd1.jpg)  
Figure 4. Period Wise Comments

![](/api/attachments/R398KKEW/fulltext/images/8065ee207433c419916d894e095708b781cb365e4c073b3b77038c20f4d39254.jpg)  
Figure 5. Average Time Difference Distribution

![](/api/attachments/R398KKEW/fulltext/images/79226266e355c6a68cfebb0ff4e92efa28f400f23e69955f33ff7ea719c2f473.jpg)  
Figure 6. Maximum Depth Distribution

To conclude, the results of this design sub-phase point to interesting and significant differences across all the general, structural, and textual characteristics of discussions in articles of different quality grades while suggesting additional features for quality assessment (Table 13 in Appendix C has additional confirmatory analyses of these features). Therefore, we have good initial support to use these as features for assessing article quality.

## Phase 3: Analysis and Feature Engineering of Discussion-Edit Relationship

Since editors who participate in discussions can also edit the article and vice-versa, we examined the relationship between the actions of common editors (i.e., who participate in both coordination and development activities for an article), and article quality. We use a three-step process to do so. The purpose of these three steps is to identify features, which quantify the relationship between editing and discussions, such that they can be used as inputs for quality assessment. In short, we answer the question: “What is the relationship between coordination (discussion) and development (editing) activities of the contributors who participate in both and how does this relationship contribute to assessing article quality?”

In step 1, we defined metrics to quantify the percentage of editors who participate in both discussions and edits (called common editors) and compare it with those who participate only in either one of these activities. To examine if articles that have similar participation patterns in editing and discussions have the same quality, we group articles based on the defined participation metrics. This step essentially answers the questions: “How many editors (out of all the editors to an article) participate in both discussions and editing (i.e., common editors,)? and How many participate in only one of the two activities and what is the relationship of this participation activity to article quality?” In step 2, having identified the common editors, we cluster them based on their actions and label the roles they play based on Liu and Ram [48]. In short, this step answers the question: “What roles do the common editors play in discussion pages and in article editing?” In step 3, we examine the collaborative patterns among these common editors playing different roles. (In saying collaboration here, we mean how editors assuming different roles [identified from step 2] perform different actions [the nine types of discussions and the nine types of edits] across the article [48].) Here, we use the definition of collaboration as “the ability to integrate talents of dispersed individuals on various tasks to produce optimal output” [71, p.18]). This step answers the question: “How do the common editors for an article, who perform different roles in editing and discussions, collaborate across various types of discussions and edits and what is the relationship between this collaboration and article quality?”

## Step 1: Analysis of Percentages of Common Editors

In this step, we define metrics to analyze the participation patterns of contributors across article editing activities and discussions. We use $\boldsymbol { \mathrm { P } } = \{ p _ { I } , p _ { 2 } , p _ { 3 } . . . p _ { n } \}$ to represent the set of Wikipedia articles in our dataset. For any given article p $\in \mathrm { \bf ~ P }$ in our data set, we identify the set of editors who participate in discussions $\mathrm { D } _ { \mathrm { p } } = \{ d _ { I } , ~ d _ { 2 } , ~ d _ { 3 } , . . . d _ { m } \}$ and the set of those who participate in editing $\mathrm { E _ { p } } \ =$ $\{ e _ { I } , e _ { 2 } , e _ { 3 } , . . . e _ { n } \}$ . Using the information on these sets, we define the following three metrics.

$$
\text { Edit   Contributor   Ratio } _ {p} = \frac {n (D _ {p} \cap E _ {p})}{n (D _ {p})}
$$

$$
\text { Discussion   Contributor   Ratio } _ {p} = \frac {n (D _ {p} \cap E _ {p})}{n (E _ {p})}
$$

$$
\text { Edit   Discussion   Ratio } _ {p} = \frac {n (E _ {p} \backslash D _ {p})}{n (D _ {p} \backslash E _ {p})}
$$

where n(X) denotes the cardinality of the set ${ \mathrm { X } } ;$ n(X∩Y) denotes the cardinality of the elements that are common to sets X and ${ \mathrm { Y } } ;$ and n(X\Y) denotes the cardinality of elements that only belong to set X but not Y.

Edit Contributor Ratio measures the percentage of editors in discussion pages who also edited the article while Discussion Contributor Ratio measures the percentage of editors of the article who also participated in discussions. These two metrics are like precision and recall [32] used in information retrieval. Edit Discussion Ratio measures ratio of the cardinalities of the sets of users who participate only in editing to those who participate only in discussions.

To segment the articles based on similarity in these three ratios, we use these three metrics as input dimensions to a repeated K-means clustering algorithm. We found that the optimal number of clusters was three using standard techniques (discussed in Appendix B). The mean values for each of the components of the input vector in each of the three clusters is shown in Table 5.

Table 5. Discussion Edit Relationship Clusters

<table><tr><td></td><td>Cluster -1</td><td>Cluster - 2</td><td>Cluster - 3</td></tr><tr><td>Edit Contributor Ratio</td><td>0.05</td><td>0.99</td><td>0.54</td></tr><tr><td>Discussion Contributor Ratio</td><td>0</td><td>0.03</td><td>0.02</td></tr><tr><td>Edit Discussion Ratio</td><td>75.41</td><td>3.02</td><td>105.85</td></tr></table>

Articles in Cluster-1 have low values of Edit Contributor Ratio and zero value for Discussion Contributor Ratio. It shows that in these articles, editors who participate in discussion do not participate in editing and vice-versa. Also, the Edit Discussion Ratio is very high indicating that there are many more editors who participate in editing than in discussions. In contrast, clusters 2 and 3 have significantly higher values of Edit Contributor Ratio and marginally higher values for Discussion Contributor Ratio indicating that a substantial percentage of editors who participate in discussions also edit the article while only a small percentage of editors who participate in editing also participate in discussions. One the other hand, cluster-2 has low values of Edit Discussion Ratio while cluster-3 has very high values. We found that approximately 80 percent of Featured (FA) and Good (GA) articles belonged to clusters 2 and 3, which had higher percentages of discussion editors also participating in article editing activity as compared to cluster-1. In general, B and C class articles tend to have lower values for Edit Contributor Ratio, meaning fewer editors who participate in discussions also edit the article. Finally, clusters 2 and 3 had either very high or very low values for Edit Discussion Ratio while cluster-1 had a moderate value. This shows that higher quality articles tend to have either very high or very low values for the number of editors participating only in editing as compared to that of editors participating only in discussions. This clean delineation of articles into clusters based on these metrics suggests that they may be useful as inputs for assessing article quality.

## Step 2: Analysis of Discussion-Edit Patterns and Roles

In the previous step, we identified the percentage of editors who participate in both editing and discussions (i.e., common editors). Here, we identify the different roles that these common editors play. The purpose is to identify groups of contributors who participate in similar kinds of discussion topics and perform similar types of edits (i.e., similar actions). Following Liu and Ram [48], we identified nine common edit types as shown in Table 6 (The nine types of discussions are shown in Appendix A – Table 11).

Table 6. Types of Edits

<table><tr><td>Type of Action</td><td>Explanation</td></tr><tr><td>Sentence Insertion</td><td>Insertion of a Sentence</td></tr><tr><td>Sentence Modification</td><td>Modification or rewording of an existing sentence</td></tr><tr><td>Sentence Deletion</td><td>Deletion of a Sentence</td></tr><tr><td>Link Insertion</td><td>Linking a word to an existing article on Wikipedia.</td></tr><tr><td>Link Modification</td><td>Modification of an existing link (can be the change of an URL or the name of the link).</td></tr><tr><td>Link Deletion</td><td>Deletion of an existing link.</td></tr><tr><td>Reference Insertion</td><td>Adding reference to an article outside Wikipedia.</td></tr><tr><td>Reference Modification</td><td>Modification of an existing reference.</td></tr><tr><td>Reference Deletion</td><td>Deletion of a reference.</td></tr></table>

Our approach to identifying these edit types and examples are provided in Appendix A. Since the volumes of edits, discussions, and editors are large in our dataset, we developed and implemented a scalable map-reduce algorithm to extract the actions of editors (described in Appendix B). This algorithm reduced the execution time by nearly 95 percent when compared to the case where we do not use either the Hadoop infrastructure [64], a distributed computational infrastructure for processing large variety of datasets, or the map-reduce algorithm. The output of this algorithm is an 18-component vector (nine each for discussions and edits) with each component representing the percentage of actions of each type performed by a common editor (Refer to equation 9 in Appendix B).

Using the edit and discussion actions for each common editor $d e _ { k p } \in \mathrm { D } _ { \mathfrak { p } } \cap \mathrm { E } _ { \mathfrak { p } }$ and for each article $p \in \mathrm { P }$ as the input, we again used the repeated K-means clustering on these vectors to identify groups of contributors whose actions are similar on both edits and discussions. We found that the optimal number of clusters was nine (using the criteria mentioned in Appendix B). Table 7 provides a comprehensive description of the clusters.

Cluster-5 (Internal content justifiers) forms the largest percentage of common editors. These editors primarily work on providing references to other Wikipedia articles and discuss about article content in the discussion pages. Cluster-6 (Comprehensive content justifiers) comes next in terms of the number of common editors. These editors provide links to articles both within and outside Wikipedia but only participate in discussions related to article content. Together these two types of editors form 46 percent of common editors. In general, the pattern observed across all the clusters is that common editors primarily concentrate on links and references as far as article edits are concerned. However, editors in cluster-8 which forms the third largest group, participate in a variety of discussions in addition to editing links and references. Interestingly, this also happens to be the only cluster where editors discuss a variety of aspects of article development. Finally, there are a small percentage of editors in cluster-2 who control the discussions and make sure that they are going properly. Previous research [76] showed how Wikipedia solves the Internet’s biggest problem, of spreading hatred in discourses, using practices that promote an orderly debate. Cluster 2 provides evidence of this behavior.

Table 7. Common Editor Role Playing Clustering Details

<table><tr><td>Cluster Number</td><td>Size</td><td>Description of actions by Editors</td><td>Role Label</td></tr><tr><td>1</td><td>7915 (10.9 percent)</td><td>Mostly perform Adding and Deleting links. Also perform Adding and deleting references to some extent. Discussions mostly center on font and formatting issues. Also talk a little bit about links and references.</td><td>Content Shapers</td></tr><tr><td>2</td><td>67(0.09 percent)</td><td>Perform Deleting and modifying links to a large extent. Also perform adding, deleting and modifying references to some extent. In discussions, they just summarize the discussions i.e., control them.</td><td>Discussion Controllers</td></tr><tr><td>3</td><td>3106(4.2 percent)</td><td>Perform adding, deleting and modifying links. Talk mostly about images and multimedia content.</td><td>Link and Multimedia Managers</td></tr><tr><td>4</td><td>7835(10.8 percent)</td><td>Edit References and talk about references only.</td><td>Reference managers</td></tr><tr><td>5</td><td>16895(23.3 percent)</td><td>Edit Links but participate only in discussions related to content.</td><td>Internal Content Justifiers</td></tr><tr><td>6</td><td>16453(22.7 percent)</td><td>Edit Links and References but participate only in discussions related to content.</td><td>Comprehensive Content Justifiers</td></tr><tr><td>7</td><td>3411(4.7 percent)</td><td>Edit Links and References but participate in only appreciating others for their efforts.</td><td>Aficionados</td></tr><tr><td>8</td><td>12676 (17.49 percent)</td><td>Edit Links and References and participate in a wide variety of discussions.</td><td>All around content justifiers</td></tr><tr><td>9</td><td>4094(5.6 percent)</td><td>Edit Links and References and acknowledge making changes to those.</td><td>Link and Reference Managers</td></tr></table>

## Step 3: Identifying Collaboration Patterns

In this step, we investigate how editors assuming different roles (in edits and discussions) implicitly collaborate on Wikipedia articles and how information about that collaboration can be used to assess article quality. For example, there may be articles where content justifiers are involved in a major set of discussions and perform most edits. We identify collaboration patterns among editors assuming different roles by again using clustering to group articles based on roles and actions performed by common editors to these articles (Details in Appendix B). Articles in which editors were involved in similar actions for editing and discussions are grouped together. Table 8 shows the details of each of the collaboration patterns in the clusters.

We found that the collaboration patterns and article quality are significantly correlated (Kendall’s Tau $- \updownarrow = 0 . 4 9 { \mathrm { ~ } } { \mathrm { p } } < 0 . 0 1$ , Spearman’s rho $= 0 . 5 3 \ \mathrm { p } < 0 . 0 1 )$ . In clusters 2 and 3, all-around content justifiers and comprehensive content justifiers dominated both edits and discussions which were associated with higher quality. For example, these two clusters together accounted for 55.73 percent of Featured (FA) articles and 48.25 percent of Good (GA) articles. Clusters 4 and 5, where people participated in only single type of discussions and where there were almost no discussions related to suggestions for improvement, were in general found to contain articles of lower quality. In general, lower quality articles (B and C Classes) were found to have a minimal amount of collaboration across the different roles we identified in the previous step (Table 7). These clear differences lead to the conclusion that the collaborative pattern among editors in an article is a possibe good predictor of overall article quality.

To summarize, in this final sub-phase of our design, we use editing and discussion behavior and collaboration characteristics to identify four additional features for our model to predict article quality. We name these four features the bridge characteristics (Edit Contributor Ratio, Discussion Contributor Ratio, Edit Discussion Ratio and Collaboration Cluster) since they bridge the discussion and article characteristics. We did not include the cluster memberships from step 2 since they are at the level of an editor. We need to aggregate them to the level of an article for prediction (which is what we did in step 3 by quantifying how the different roles collaborated and the relationship between this collaboration and article quality). The next step is to use these bridge characteristics along with the discussion characteristics identified in the previous two design sub-phases to build our model for assessing and predicting article quality.

Table 8. Common Editor Collaboration Clusters

<table><tr><td>Cluster Number</td><td>Number of Articles</td><td>Description</td></tr><tr><td>1</td><td>4315(14.29 percent)</td><td>Reference Managers dominate on all the article related actions. Internal and Comprehensive content justifiers dominate content related comments. Link and Multimedia managers for Images and Multimedia and Reference Managers for Sources and References.</td></tr><tr><td>2</td><td>7066(23.41 percent)</td><td>All round content justifiers dominate all types of edits and discussions.</td></tr><tr><td>3</td><td>7201(23.86 percent)</td><td>Comprehensive content justifiers dominate all types of edits and discussions.</td></tr><tr><td>4</td><td>7888(26.13 percent)</td><td>Internal Content justifiers dominate all types of edits and discussions. But this cluster has almost no discussions related to Clarifications and Suggestions for content improvement.</td></tr><tr><td>5</td><td>2177(7.21 percent)</td><td>Link and Reference Managers dominates all types of edits and discussions except those related to content where there are comprehensive content justifiers. Almost no comments related to suggestions for improvement.</td></tr><tr><td>6</td><td>3880(12.85 percent)</td><td>Content Shapers dominates all types of edits and discussions except those related to content which is by Comprehensive content justifiers. Hardly any comments related to content clarification and suggestions for improvement.</td></tr><tr><td>7</td><td>1967(6.51 percent)</td><td>Comprehensive content justifiers dominate all types of edits and discussions. Comprehensive content justifiers dominate acknowledgement and content.</td></tr></table>

## Demonstration and Evaluation: Predictive Modeling

As shown in the prior section, we found that articles in the given four quality grades differ significantly on almost all the features identified in all the three sub-phases of design. We therefore leverage these features to assess quality. Here the purpose is to implement and evaluate how well the identified discussion and bridge characteristics perform to identify articles in each of the four different quality grades (FA, GA, B, and C) correctly. We also quantify the contribution of each of these features towards quality assessment and their robustness to the choice of dataset and the technique used. We therefore build multi-class prediction models. The outcome of our models has four possible values: FA, GA, B, and C. We tested a variety of classification techniques including logistic regression, C5.0, Adaboost, Random Forests, and Bayesian networks, and found that C 5.0 gives the best results in this case. We used a standard ten-fold cross validation approach to prevent overfitting. To reduce the upward bias associated with cross validation [22], we use bootstrapping with 1000 samples on the training datasets to estimate the standard errors. We also used hyper parameter optimization, tree pruning, and boosting approaches with confidence-based voting to improve the accuracy of the models.

To evaluate the performance of our model, we utilized common metrics in machine learning: Overall Accuracy, Precision, Recall, and the F-Measure.

Overall Accuracy measures the total number of articles for which the model predicted the correct outcome:

$$
\text { Overall   Accuracy } = \frac {\text { No   of   Correctly   Classified   Instances }}{\text { Total   Instances }} * 1 0 0\tag{1}
$$

Class-wise precision measures the number of instances that were predicted correctly within an outcome class:

$$
\text { Precision   (For   FA   Articles) } = \frac {\text { No   of   Correctly   classified   instances   of   FA   articles }}{\text { No   of   instances   classified   as   FA }} * 1 0 0\tag{2}
$$

Class-wise recall measures the coverage of the classifier for that class:

$$
\text { Recall   (For   FA   Articles) } = \frac {\text { No   of   Correctly   classified   instances   of   FA   Articles }}{\text { Total   instances   of   FA   articles }} * 1 0 0\tag{3}
$$

F-measure is the harmonic mean of precision and recall:

$$
\mathrm{F} - \text { Measure } = \frac {2 * \text { Precision } * \text { Recall }}{\text { Precision } + \text { Recall }} * 1 0 0\tag{4}
$$

The results of multi-class prediction are shown in Table 9. The values in the parenthesis show the standard deviations for these metrics. C 5.0 outperformed other models on all evaluation metrics.

Considering that the baseline accuracy is 46.9 percent (percentage of C-Class articles in the sample), each of the general, structural and textual characteristics improves the overall accuracy between 6 and 8 percent. Also, a combination of these (i.e., all the discussion characteristics identified in our first sub-phase of design) results in a 12 percent increase in overall accuracy and 15 percent increase in class wise recall suggesting that discussion features can help us identify precisely, a wider variety of articles in each of the quality grades. A combination of article and discussion features results in a 2.79 percent increase in overall accuracy and between 1 and 8 percent increases in class wise recall (with 4-6 percent increases in class wise precision) again suggesting the utility of discussion features in correctly identifying a wider variety of articles within each grade. Finally, bridge characteristics help us achieve an 81.03 percent overall accuracy, which is a 6.53 percent improvement over using just the article characteristics (and a 9.16 percent improvement over using the edit experience characteristics), and 4-17 percent increase in class wise recall values validating the utility of both these characteristics in being able to classify into one of the four different grades. In addition, all these models have very low values of standard deviations across the evaluation metrics indicating the robustness of the features in classifying articles into one of the four grades and the utility of using large samples to identify these features. Overall, these models validate the utility of discussion and bridge features in improving the process of assigning grades.

Table 9. Results Multiclass Classification

<table><tr><td rowspan="2">Features Used</td><td colspan="2">Area under  $Curve^8$ </td><td colspan="4">Precision</td><td colspan="4">Recall</td><td colspan="4">F-Measure</td></tr><tr><td>Overall Accuracy</td><td>(FA vs Rest)</td><td>FA</td><td>GA</td><td>B</td><td>C</td><td>FA</td><td>GA</td><td>B</td><td>C</td><td>FA</td><td>GA</td><td>B</td><td>C</td></tr><tr><td>Article</td><td>74.5(0.159)</td><td>96.1(0.0)</td><td>87.01(0.862)</td><td>78.68(0.294)</td><td>72.43(0.338)</td><td>74.15(0.181)</td><td>45.88(0.761)</td><td>63.93(0.517)</td><td>66.18(0.216)</td><td>86.4(0.248)</td><td>60.08(2.19)</td><td>70.54(3.61)</td><td>69.16(3.12)</td><td>79.81(3.38)</td></tr><tr><td>Editor Experience</td><td>71.87(0.145)</td><td>96.49(0.0491)</td><td>74.24(0.743)</td><td>74.41(0.355)</td><td>72.07(0.235)</td><td>70.97(0.104)</td><td>58.71(0.671)</td><td>73.93(0.561)</td><td>49.66(0.168)</td><td>86.56(0.194)</td><td>65.56(4.137)</td><td>74.16(4.078)</td><td>58.8(4.353)</td><td>77.99(3.869)</td></tr><tr><td>Only General</td><td>53.51(0.364)</td><td>71.2(0.0)</td><td>71.9(1.25)</td><td>57.51(0.63)</td><td>55.82(0.432)</td><td>52.63(0.063)</td><td>9.61(0.124)</td><td>32.66(0.569)</td><td>17.78(0.529)</td><td>89.5(0.651)</td><td>16.95(0.151)</td><td>41.66(3.79)</td><td>26.96(2.56)</td><td>66.29(2.26)</td></tr><tr><td>Only Structural</td><td>52.75(0.187)</td><td>87.5(0.0)</td><td>75.75(1.12)</td><td>69.01(0.5)</td><td>54.02(0.708)</td><td>51.31(0.084)</td><td>10.24(0.05)</td><td>26.68(0.391)</td><td>12.45(0.319)</td><td>93.7(0.284)</td><td>18.04(0.143)</td><td>38.48(3.06)</td><td>20.23(0.88)</td><td>66.29(2.05)</td></tr><tr><td>Only Textual</td><td>52.47(0.234)</td><td>61.5(0.002)</td><td>69.53(0.892)</td><td>56.07(0.871)</td><td>58.08(0.485)</td><td>51.49(0.04)</td><td>9.24(0.11)</td><td>27.19(0.199)</td><td>14(0.196)</td><td>91.9(0.163)</td><td>16.31(0.442)</td><td>36.62(2.309)</td><td>22.56(2.15)</td><td>65.99(2.04)</td></tr><tr><td>Bridge</td><td>49.92(0.229)</td><td>85.7(0.002)</td><td>50(0.0)</td><td>48(0.77)</td><td>50(1.12)</td><td>51.26(0.0962)</td><td>10.5(0)</td><td>88.59(0.909)</td><td>1.17(0.464)</td><td>30.14(0.419)</td><td>17.35(0.0)</td><td>62.26(0.0)</td><td>2.28(0.0)</td><td>37.96(0.0)</td></tr><tr><td>Discussion Page (General, Structural and Textual)</td><td>58.05(0.115)</td><td>90.2(0.253)</td><td>72.72(1.38)</td><td>70.6(0.675)</td><td>62(0.341)</td><td>55.5(0.122)</td><td>25.81(0.184)</td><td>45.2(1.086)</td><td>22.34(0.5104)</td><td>90.3(0.683)</td><td>38.09(0.513)</td><td>55.11(3.19)</td><td>32.84(2.15)</td><td>68.75(2.12)</td></tr><tr><td>Both Article and Discussion Page</td><td>77.29(0.150)</td><td>85(0.0211)</td><td>91.35(0.874)</td><td>83.29(0.615)</td><td>75.96(0.161)</td><td>75.95(0.214)</td><td>51.13(0.675)</td><td>71.98(1.15)</td><td>67.76(0.222)</td><td>90(0.277)</td><td>65.56(2.97)</td><td>77.22(3.74)</td><td>71.62(3.34)</td><td>82.36(3.58)</td></tr><tr><td>Article+</td><td>81.03(0.224)</td><td>78.4(0.019)</td><td>93.11(1.269)</td><td>87.38(0.437)</td><td>80.54(0.392)</td><td>78.98(0.170)</td><td>62.66(0.459)</td><td>78.75(0.935)</td><td>71.44(0.263)</td><td>90.1(0.354)</td><td>74.91(2.99)</td><td>82.84(3.401)</td><td>75.72(3.36)</td><td>84.19(3.608)</td></tr><tr><td>Discussion +Bridge</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Considering that the English language Wikipedia has close to six million articles today, a 6.53 percent increase in overall accuracy on an average, with a standard deviation of 0.224 percent results in anywhere between 351,140 to 432,120 more articles being assigned the correct grade (when you assume normal distribution for accuracies and take three standard deviations around the mean). In addition, when you look into the current statistics of articles that belong to different quality grades on Wikipedia: (a) a 16.78 percent increase in recall for FA-articles translates to 1085 more FA-articles being assigned the correct grade; (b) a 14.82 percent increase in recall for GA-articles translates to 4628 more GA-articles being assigned the correct grade; (c) a 5.26 percent increase in recall for B-articles translates to 6357 more B-articles being assigned the correct grade; and (d) a 3.7 percent increase in recall for C-articles translates to 10290 more C-articles being assigned the correct grade.

We calculated the contribution of each of the features toward increasing the overall accuracy of the model (i.e., the features that result in at least a one percent increase in prediction accuracy). To do so, we iteratively construct and test two models: one containing all the features and one containing all features except one (i.e., leave-one-out). Then on the testing set, we calculate the difference between the overall accuracies of these models as a representation of the importance of that feature. The results are shown below in Table 10 in the descending order of feature importance. All the numbers are in percentages.

We found that 24 out of the 29 proposed new features had a non-zero impact on predictive accuracy with at least a one percent increase. All the four bridge characteristics were found to increase the accuracy at least by three percent. We found that the average depth of the discussions had the highest impact on predictive accuracy. Our initial analysis showed that while Good (GA) articles have a greater depth than Featured (FA) articles, the skewness of depth across different threads in an article is more positive in the case of Featured (FA) articles. Put together, these results show that depth of discussions on article development and coordination activities plays an important role in determining quality. Comments related to clarification on article content had the second biggest impact on predictive accuracy. We also found that articles whose editors acted as all around content justifiers and comprehensive content justifiers (both of whom primarily concentrate on links and references in editing and who participate in a variety of discussions) were found to be of higher quality. This suggests that articles in which editors concentrate on clarifying the article content and perform edits that justify the content tend to be of higher quality. Anonymous contributor count, contributor count, and comment count were the next three important variables, and this result was expected and consistent with what has been found in our analysis in the first sub-phase of our design. Overall, considering the size of the present-day English language Wikipedia, even a 1 percent increase in accuracy translates to 60,000 more articles being classified into the correct grade, while a 14 percent increase translates to 840,000. To conclude, addition of each of the identified features, to quality assessment models, contributes substantially to solving the problem of assigning accurate quality grades for peer-produced content.

Table 10. Feature Importance (Overall Accuracy Improvements)

<table><tr><td>Feature</td><td>Importance (percent)</td></tr><tr><td>Average Depth</td><td>14.00</td></tr><tr><td>Clarification Comments</td><td>11.00</td></tr><tr><td>Anonymous Contributor Count</td><td>10.00</td></tr><tr><td>Contributor Count</td><td>9.00</td></tr><tr><td>Gini Index of Contributions</td><td>7.00</td></tr><tr><td>Comment Count</td><td>7.00</td></tr><tr><td>Suggestion Comments</td><td>6.00</td></tr><tr><td>Discussion Period</td><td>6.00</td></tr><tr><td>Thread Count</td><td>5.00</td></tr><tr><td>Positive Sentiment Skewness</td><td>5.00</td></tr><tr><td>Discussion Contributor Ratio*</td><td>4.00</td></tr><tr><td>Collaboration Cluster*</td><td>4.00</td></tr><tr><td>Summary Comments</td><td>4.00</td></tr><tr><td>Mean Positive Sentiment</td><td>3.00</td></tr><tr><td>Edit Contributor Ratio*</td><td>3.00</td></tr><tr><td>Edit Discussion Ratio*</td><td>3.00</td></tr><tr><td>Acknowledgement Comments</td><td>2.00</td></tr><tr><td>References Comments</td><td>2.00</td></tr><tr><td>Format Comments</td><td>2.00</td></tr><tr><td>Images and Multimedia Comments</td><td>2.00</td></tr><tr><td>Reading Complexity Skewness</td><td>1.00</td></tr><tr><td>Depth Skewness</td><td>1.00</td></tr><tr><td>Average Time Gap</td><td>1.00</td></tr><tr><td>Content Comments</td><td>1.00</td></tr></table>

Note: \* represents the bridge characteristics.

We also found that the same technique (C 5.0) gives the best results on smaller stratified samples of data but the accuracies become much lower, indicating the utility of using larger training samples for better performance. This validates the robustness of our results to the choice of data set and technique. Leveraging these results, we discuss the architecture and implementation of a system, and its technical details, specifications, and computational complexity, for automated quality assessment.

## Communication: System Architecture and Implementation for Automated Quality Assessment

Figure 7 shows the architecture of the proposed system for automated quality assessment. Broadly, the system has two layers (i.e., the Data and Infrastructure Layer and the Modeling and Evaluation Layer).

The data and infrastructure layer takes care of collecting and cleaning data and providing the required infrastructure for analyzing this data and building the prediction models. Based on the infrastructure we used in this research, we recommend a standard six node Cloudera Hadoop cluster [61] for the big data infrastructure. The textual data is stored in HIVE [73] while the numerical and temporal data are stored in relational database tables in MySQL [51]. When we deploy our map-reduce algorithm (presented in Appendix B), the run time reduces by approximately 95 percent when compared to the case where we do not use either the algorithm or the computational infrastructure. With the ever decreasing cost of computing power accompanied with the increasing ease of implementation and use of big data related computational infrastructure [59, 70], we posit that this infrastructure can be easily procured and configured with minimal efforts by organizations that use a model of peer-production for their knowledge repositories.

![](/api/attachments/R398KKEW/fulltext/images/5b47a771605af0db4bc7d809feb9ed01e65fed6263fdd4d6e2f4af50602e66bd.jpg)  
Figure 7. System Architecture for Automated Quality Assessment

The modeling and evaluation layer leverages the identified features to assign grades for articles. This layer will also have functions to evaluate the models and derive the importance of each of the features. These steps can be implemented using open source software packages like R [31] and Python [74] (as we did in this research), which have in-built libraries for all the supervised and unsupervised machine learning tasks. Since the system already has a big data infrastructure component (Hadoop Ecosystem) that readily integrates with open source tools, it can be leveraged for modeling and evaluation purposes. Overall, the algorithms and the code for data collection, cleaning and feature extraction we developed for this research can be directly imported to an automated quality assessment system. The interfaces (pipelines) that connect various components of this research for a production ready environment need to be developed.

Considering the extremely large size of knowledge repositories such as Wikipedia and the need to frequently assess quality as content is continually updated [18, 77], models can be built and evaluated using this infrastructure in an efficient way. When we account for the time it takes to download the Wikipedia edit and discussion history, clean it and extract the features, we estimate the total time for completion of all the activities, which lead to quality grade assignment for all the articles, to be less than four days. In other words, when this system is implemented with the given specifications, it is possible to assess the quality of all articles at least once a week (on a knowledge repository that is as big as the present-day English language version of Wikipedia). Thus, this system would fit the present and future needs for frequent quality assessment of peer-produced content in large-scale knowledge repositories [18, 77].

## Conclusion, Contributions, Implications, and Limitations

In this research, we developed a method to assess the quality of peer-produced content in knowledge repositories using a design science approach. We also described a process to identify features related to coordination and development of content in knowledge repositories and computationally efficient algorithms to extract these features from internet-scale data. To our knowledge, this is the first known work to leverage the complete population of graded English language Wikipedia articles to identify a robust set of features for quality assessment. Our results showed that articles that belong to different quality grades differ significantly on almost all the discussion characteristics we identified. We discovered that articles in which all around content justifiers and comprehensive content justifiers dominated both discussions and edits were found to be of higher quality. Our approach significantly outperforms the existing method for quality assessment of peer-produced content in knowledge repositories. We reduced the error rate of the existing quality assessment method by more than 25 percent. Considering that the decision tree classifier (C 5.0) gave the best results in our case, our results also have higher interpretability than approaches that use other machine learning methods (such as KNN, SVM, Random Forest, etc.). In doing so, our work has three major contributions.

First, our research contributes to the work on assessing quality of content in knowledge repositories. We identified a comprehensive, rich set of features related to coordination of development activities, which represent the temporal, structural, volume, and topical aspects of discussions, which are significantly predictive of article quality. We found that these features add value to quality assessment by not only providing more accurate and precise predictions but also by covering a larger percentage of articles in each grade. We also found that when combined with bridge characteristics, they increase the overall accuracy by 6.53 percent over the baseline model that uses just the article characteristics. Finally, we found that our results are robust to the choice of data and technique and that using larger samples substantially increases the performance of the models. In doing so, we provided architecture and implementation details of the system to automate quality assessment of content in peer-produced internet-scale knowledge repositories (Figure 7). Given the exponential growth of articles in knowledge repositories over past few years [27, 30], it has become almost impossible to have a system where humans read and evaluate the quality of every piece of content without being subject to biases. Our research significantly improves the previous work done on quality assessment [10, 12, 18, 27, 46, 66, 77, 80] by not only providing an efficient scalable method for quality assessment but also by providing a rich set of features and algorithms to extract these features from largescale knowledge repositories.

Second, we contribute to the literature on design science in big data analytics, by leveraging analytics on large-scale diverse and fine grained datasets to extract insights that lead to high accuracy models [14, 15, 21, 25, 37, 45, 50, 54, 83]. We provided a method and a process for quality assessment of peer-produced content in large-scale knowledge repositories. We demonstrated how to use data-driven methods that start with an initial set of features and employ big data analytics to identify additional features for the model. We also defined several features that quantify the relationship between various collaborative activities in knowledge repositories (i.e., bridge characteristics). Finally, we developed a scalable map-reduce algorithm that can be used to efficiently extract the editor actions in peer-produced content. In doing so, we provide a process, a set of features and the relevant algorithms that can not only be replicated to identify relevant and robust features for quality assessment in other peer-produced content communities but also be deployed directly for quality assessment in knowledge repositories. In areas where there is lack of appropriate social science and economic theory but large population sized datasets are available [56, 62, 63], insights from performing analytics, similar to the ones done in this research, can provide a robust set of features that can be used to build high accuracy models. Recent examples in literature used big data analytics to provide solutions to realworld problems. Zhou et al. [83] developed a singular value decomposition-based semantic keyword similarity method to quantify customer agility using large-scale customer review texts and product release notes. In a similar piece of work, Dong et al. [21] use systemic functional linguistics theory to propose a framework that leverages data from financial social media platforms to assess the risk of corporate fraud. Along the same lines, Kitchens et al. [37] leverage relationship marketing theory to build a framework for identifying and evaluating various sources of big data and enable agile deployment of advanced customer analytics. Winter [78] emphasized the need for maximizing relevance as well as rigor in IS design research. Abbasi et al. [2, p. xvii] argued that one of the opportunities for big data in design science research is “leveraging volume and variety to develop novel artifacts for prediction or description,” Our work in this research is a step forward in both these directions.

Finally, we contribute to the literature on analyzing datasets much richer, larger, and comprehensive than those examined in traditional information systems and marketing literature. We developed and evaluated a method to efficiently extract topics from a large corpus of text by combining machine learning and human encoding approaches (details in Appendix A). Given that 80 percent of the data produced in the world today is in the form of text [29], techniques for both cleaning and mining text effectively have become more important than ever before. Agrawal et al. [4] describe tasks where machines and human beings are good at and how collaboration between the two can be leveraged to improve the efficiency and scalability of existing methods. Our contributions from this work can be scaled and applied to mining large corpuses of text in other contexts such as product reviews in e-commerce, posts on LinkedIn and Facebook, tweets, and so forth. With the ever increasing availability of rich datasets for Information Systems researchers [3, 25, 50, 57, 59, 82] and the ease of setting up the required computational infrastructure, we believe that this work paves way for conducting more studies using big data analytics. Such research can lead to the construction of more domain specific artifacts for identifying relevant features and building automated systems.

We acknowledge that there are limitations with this research in the sense that our features and models were built only on graded articles. This is because of the absence of any statistics on how many articles on Wikipedia would have received one of the four quality grades but did not get one because of the scalability issues with the peer-review process. However, we made sure that the articles in our sample encompass all the topics<sup>9</sup> on the complete English language version of Wikipedia. Moreover, considering that our features were identified on the complete population of graded articles, and that they are robust to the choice of the technique used for classification, we believe that our results have a great potential for generalizability [4, 20, 38, 39]. Also, considering the evidence for increasing popularity of Wikipedia articles over the past decade [8, 11, 16, 81], we believe that the insights derived here can be transferred not only to the non-graded articles on Wikipedia but also to other knowledge repositories using transfer learning approaches such as transductive learning [53] and Eigen Transfer [17].

## NOTES

1. http://en.wikipedia.org/wiki/Wikipedia:Featured\_article\_criteria

2. http://en.wikipedia.org/wiki/Wikipedia:Good\_article\_criteria

3. http://en.wikipedia.org/wiki/Wikipedia:Version\_1.0\_Editorial\_Team/Assessment/ B-Class\_criteria

4. http://en.wikipedia.org/wiki/Template:Grading\_scheme

5. Map-reduce is a computational framework that performs a large-scale computational processing job by splitting it into multiple smaller jobs and combines the output of these jobs while coordinating them in a timely manner to extract editor actions (Details are in Appendix B).

6. https://www.mediawiki.org/wiki/API:Main\_page

7. We also used the standard measures of skewness used in statistics and found that the results of our predictive modeling were not sensitive to the choice of the measures. We therefore picked the ratio of median to mean since it is much simpler to interpret. The results of predictive modeling using the other two measures are shown in Tables 14 and 15 in Appendix C.

8. AUC values are used only in Binary Classification. All other columns are for evaluating multi-class classification which is the primary focus of our evaluation. We used AUC’s only to demonstrate the power of our features in differentiating highest quality articles (FA) from the rest.

9. https://en.wikipedia.org/wiki/Wikipedia:1,000\_core\_topics

## ORCID

Srikar Velichety http://orcid.org/0000-0001-9849-3509

Sudha Ram http://orcid.org/0000-0001-6053-1311

Jesse Bockstedt http://orcid.org/0000-0002-4274-9744

## REFERENCES

1. Abbasi, A.; and Chen, H. CyberGate: A design framework and system for text analysis of computer-mediated communication. MIS Quarterly, 32, 4 (2008), 811–837.

2. Abbasi, A.; Sarker, S.; and Chiang, R.H. Big data research in information systems: Toward an inclusive research agenda. Journal of the Association for Information Systems, 17, 2 (2016), pp. i–xxxii.

3. Agarwal, R., and Dhar, V. (2014) Editorial—Big data, Data Science, and Analytics: The opportunity and challenge for is research. Information Systems Research 25(3):443–448

4. Agrawal, A.; Gans, J.; and Goldfarb, A. Prediction machines: The simple economics of artificial intelligence. Harvard Business Press, Boston, MA, USA, 2018.

5. Anderson, C. The end of theory: The data deluge makes the scientific method obsolete. Wired Magazine, 16, 7 (2008), 1–3.

6. Arazy, O.; and Croitoru, A. The sustainability of corporate wikis: A time-series analysis of activity patterns. ACM Transactions on Management Information Systems (TMIS), 1, 1 (2010), 6.

7. Arazy, O.; and Nov, O. Determinants of Wikipedia quality: The roles of global and local contribution inequality. In Proceedings of the 2010 ACM Conference on Computer Supported Cooperative Work. 2010, pp. 233–236. Savannah, Georgia, USA: ACM Publishers.

8. Hickman et al. How Wikipedia Data Is Revolutionizing Flu Forecasting. MIT Technology Review, 2014. Accessed on June 29, 2015: http://www.technologyreview.com/ view/532246/how-wikipedia-data-is-revolutionizing-flu-forecasting/.

9. Best Knowledge Management Software | 2018 Reviews of the Most Popular Systems. Accessed on November 20, 2018: https://www.capterra.com/knowledge-managementsoftware/.

10. Blumenstock, J.E. Size matters: Word count as a measure of quality on Wikipedia. In Proceedings of the 17th International Conference on World Wide Web, 2008, pp. 1095–1096. Beijing, China: ACM Publications.

11. Bosman, J. After 244 years, Encyclopaedia Britannica stops the presses. The New York Times, 13, (2012), 1–3.

12. Brandes, U.; Kenis, P.; Lerner, J.; and van Raaij, D. Network analysis of collaboration structure in Wikipedia. In Proceedings of the 18th International Conference on World Wide Web. New York, NY, USA: ACM, 2009, pp. 731–740.

13. Brown, D. YouTube uses Wikipedia to fight fake news. The Times, 2018, pp. 1–3. Accessed on March 24, 2018 : https://www.thetimes.co.uk/article/youtube-fights-fake-newswith-wikipedia-frkpc8nm2.

14. Brynjolfsson, E.; Geva, T.; and Reichman, S. Crowd-Squared: Amplifying the Predictive Power of Search Trend Data. MIS Quarterly, 40, 4 (2015), 941–962.

15. Chau, M.; and Xu, J. Business intelligence in blogs: Understanding consumer interactions and communities. MIS Quarterly, 36, 4 (2012), 1189–1216.

16. Cohen, N. Courts turn to wikipedia, but selectively. The New York Times, 29, (2007).

17. Dai, W.; Jin, O.; Xue, G.-R.; Yang, Q.; and Yu, Y. Eigentransfer: A unified framework for transfer learning. In Proceedings of the 26th Annual International Conference on Machine Learning. Montreal, Canada: ACM, 2009, pp. 193–200.

18. Dang, Q.-V.; and Ignat, C.-L. Measuring quality of collaboratively edited documents: The case of Wikipedia. In Proceedings of the 2016 IEEE 2nd International Conference on Collaboration and Internet Computing (CIC). Pittsburgh, USA: IEEE, 2016, pp. 266–275.

19. Dean, J.; and Ghemawat, S. MapReduce: Simplified data processing on large clusters. Communications of the ACM, 51, 1 (2008), 107–113.

20. Dhar, V. Data science and prediction. Communications of the ACM, 56, 12 (2013), 64–73.

21. Dong, W.; Liao, S.; and Zhang, Z. Leveraging financial social media data for corporate fraud detection. Journal of Management Information Systems, 35, 2 (2018), 461–487.

22. Efron, B.; and Tibshirani, R. Improvements on cross-validation: The 632+ bootstrap method. Journal of the American Statistical Association, 92, 438 (1997), 548–560.

23. Ferschke, O.; Daxenberger, J.; and Gurevych, I. A survey of NLP methods and resources for analyzing the collaborative writing process in Wikipedia. In The People’s Web Meets NLP. Berlin, Heidelberg: Springer, 2013, pp. 121–160.

24. General Inquirer Categories. Accesed on March 18, 2018: http://www.wjh.harvard. edu/\~inquirer/homecat.htm.

25. Geva, T.; Oestreicher-Singer, G.; Efron, N.; and Shimshoni, Y. Using forum and search data for sales prediction of high-involvement products. MIS Quarterly, 41, 1 (2017), 65–82.

26. Giles, J. Internet encyclopaedias go head to head. Nature, 438, 7070 (2005), 900–901.

27. Hasan Dalip, D.; André Gonçalves, M.; Cristo, M.; and Calado, P. Automatic quality assessment of content created collaboratively by web communities: A case study of wikipedia. In Proceedings of the 9th ACM/IEEE-CS Joint Conference on Digital Libraries. Austin, TX, USA: ACM, 2009, pp. 295–304.

28. Hevner, A.; March, S.T.; Park, J.; and Ram, S. Design science research in information systems. MIS quarterly, 28, 1 (2004), 75–105.

29. Holzinger, A.; Stocker, C.; Ofner, B.; Prohaska, G.; Brabenetz, A.; and Hofmann-Wellenhof, R. Combining HCI, natural language processing, and knowledge discoverypotential of IBM Content Analytics as an assistive technology in the biomedical field. In Human-Computer Interaction and Knowledge Discovery in Complex, Unstructured, Big Data. Berlin, Heidelberg: Springer, 2013, pp. 13–24.

30. Hu, M.; Lim, E.-P.; Sun, A.; Lauw, H.W.; and Vuong, B.-Q. Measuring article quality in wikipedia: models and evaluation. In Proceedings of the Sixteenth ACM Conference on Conference on Information and Knowledge Management. Lisbon, Portugal: ACM, 2007, pp. 243–252.

31. Ihaka, R.; and Gentleman, R. R. A language for data analysis and graphics. Journal of Computational and Graphical Statistics, 5, 3 (1996), 299–314.

32. Järvelin, K.; and Kekäläinen, J. IR evaluation methods for retrieving highly relevant documents. In Proceedings of the 23rd Annual International ACM SIGIR Conference on Research and Development in Information Retrieval. New York, NY: ACM, 2000, pp. 41–48.

33. Kane, G.C. A multimethod study of information quality in wiki collaboration. ACM Transactions on Management Information Systems (TMIS), 2, 1 (2011), 4.

34. Kane, G.C.; Johnson, J.; and Majchrzak, A. Emergent life cycle: The tension between knowledge change and knowledge retention in open online coproduction communities. Management Science, 60, 12 (2014), 3026–3048.

35. Kane, G.C.; and Ransbotham, S. Research Note—Content and collaboration: An affiliation network approach to information quality in online peer production communities. Information Systems Research, 27, 2 (2016), 424–439.

36. Kane, G.C.; and Ransbotham, S. Content as community regulator: The recursive relationship between consumption and contribution in open collaboration communities. Organization Science, 27, 5 (2016), 1258–1274.

37. Kitchens, B.; Dobolyi, D.; Li, J.; and Abbasi, A. Advanced customer analytics: Strategic value through integration of relationship-oriented big data. Journal of Management Information Systems, 35, 2 (2018), 540–574.

38. Kitchin, R. Big Data, new epistemologies and paradigm shifts. Big Data & Society, 1, 1 (2014), 2053951714528481.

39. Kitchin, R. The data revolution: Big data, open data, data infrastructures and their consequences. London, UK :Sage, 2014.

40. Kittur, A.; and Kraut, R.E. Harnessing the wisdom of crowds in Wikipedia: Quality through coordination. In Proceedings of the 2008 ACM Conference on Computer Supported Cooperative Work. 2008, pp. 37–46, San Diego, California, USA.

41. Kittur, A.; Suh, B.; Pendleton, B.A.; and Chi, E.H. He says, she says: Conflict and coordination in Wikipedia. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. 2007, pp. 453–462. San Jose, California, USA: ACM Publishers.

42. de La Robertie, B.; Pitarch, Y.; and Teste, O. Measuring article quality in Wikipedia using the collaboration network. In Proceedings of the 2015 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining (ASONAM). New York, NY, USA: IEEE, 2015, pp. 464–471.

43. Laniado, D.; and Tasso, R. Co-authorship 2.0: Patterns of collaboration in Wikipedia. In Proceedings of the 22nd ACM Conference on Hypertext and Hypermedia. 2011, pp. 201–210. Eindhoven, The Netherlands: ACM Publishers.

44. Laniado, D.; Tasso, R.; Volkovich, Y.; and Kaltenbrunner, A. When the Wikipedians talk: Network and tree structure of Wikipedia discussion pages. In Proceedings of the 5<sup>th</sup> AAAI International Conference on Weblogs and Social Media. 2011, pp. 177–184. Barcelona, Spain: AAAI Publishers.

45. Lash, M.T.; and Zhao, K. Early predictions of movie success: The who, what, and when of profitability. Journal of Management Information Systems, 33, 3 (2016), 874–903.

46. Li, X.; Tang, J.; Wang, T.; Luo, Z.; and De Rijke, M. Automatically assessing Wikipedia article quality by exploiting article–editor networks. In European Conference on Information Retrieval. Springer, Vienna, Austria, 2015, pp. 574–580.

47. Lipka, N.; and Stein, B. Identifying featured articles in Wikipedia: Writing style matters. In Proceedings of the 19th International Conference on World Wide Web. ACM, Raleigh, North Carolina, USA, 2010, pp. 1147–1148.

48. Liu, J.; and Ram, S. Who does what: Collaboration patterns in the Wikipedia and their impact on article quality. ACM Transactions on Management Information Systems (TMIS), 2, 2 (2011), 11.

49. Liu, J.; and Ram, S. Using big data and network analysis to understand Wikipedia article quality. Data & Knowledge Engineering, 115, (2018), 80–93.

50. Martens, D.; Provost, F.; Clark, J.; and de Fortuny, E.J. Mining massive fine-grained behavior data to improve predictive analytics. MIS Quarterly, 40, 4 (2016), 869–888.

51. MySQL, A.B. MySQL database server. http://www. mysql. com (accessed/1/2000), (2004).

52. ORES - MediaWiki. https://www.mediawiki.org/wiki/ORES.

53. Pan, S.J.; and Yang, Q. A survey on transfer learning. IEEE Transactions on Knowledge and Data Engineering, 22, 10 (2010), 1345–1359.

54. Park, S.-H.; Huh, S.-Y.; Oh, W.; and Han, S.P. A social network-based inference model for validating customer profile data. MIS Quarterly, 36, 4 (2012), 1217–1237.

55. Peffers, K.; Tuunanen, T.; Rothenberger, M.A.; and Chatterjee, S. A design science research methodology for information systems research. Journal of Management Information Systems, 24, 3 (2007), 45–77.

56. Provost, F.; and Fawcett, T. Data science and its relationship to big data and data-driven decision making. Big Data, 1, 1 (2013), 51–59.

57. Provost, F.; Martens, D.; and Murray, A. Finding similar mobile consumers with a privacy-friendly geosocial design. Information Systems Research, 26, 2 (2015), 243–265.

58. Ransbotham, S.; and Kane, G.C. Membership turnover and collaboration success in online communities: Explaining rises and falls from grace in Wikipedia. MIS Quarterly, 35, 3 (2011), 613–627.

59. Ransbotham, S.; Kane, G.C.; and Lurie, N.H. Network characteristics and the value of collaborative user-generated content. Marketing Science, 31, 3 (2012), 387–405.

60. Schneider, J.; Passant, A.; and Breslin, J.G. Understanding and improving Wikipedia article discussion spaces. In Proceedings of the 2011 ACM Symposium on Applied Computing. Taichung, Taiwan: ACM, 2011, pp. 808–813.

61. Shahverdiev, J. Cloudera cluster with 6 nodes and 1 master(HDFS MapReduse) | Unixmen. Accessed date on January 01, 2018 https://www.unixmen.com/cloudera-clusterwith-6-nodes-and-1-masterhdfs-mapreduse/.

62. Shmueli, G. To explain or to predict? Statistical Science, 25, 3 (2010), 289–310.

63. Shmueli, G.; and Koppius, O.R. Predictive analytics in information systems research. MIS Quarterly, 35, 3 (2011), 553–572.

64. Shvachko, K.; Kuang, H.; Radia, S.; and Chansler, R. The hadoop distributed file system. In Proceedings of the 2010 IEEE 26<sup>th</sup> Symposium on Mass Storage Systems and Technologies (MSST), 2010, pp. 1–10.

65. Smith, E.A.; and Senter, R.J. Automated readability index. Cincinnati, Ohio, USA: Cincinnati University Ohio, 1967.

66. Stvilia, B.; Twidale, M.B.; Smith, L.C.; and Gasser, L. Assessing information quality of a community-based encyclopedia. In Proceedings of the International Conference on Information Quality. 2005, pp. 1–12. Cambridge, USA.

67. Stvilia, B.; Twidale, M.B.; Smith, L.C.; and Gasser, L. Information quality work organization in Wikipedia. Journal of the American Society for Information Science and Technology, 59, 6 (2008), 983–1001.

68. Suzuki, Y. Quality assessment of Wikipedia articles using h-index. Journal of Information Processing, 23, 1 (2015), 22–30.

69. Suzuki, Y.; and Yoshikawa, M. Assessing quality score of Wikipedia article using mutual evaluation of editors and texts. In Proceedings of the 22nd ACM International Conference on Information & Knowledge Management. ACM, San Francisco, California, USA, 2013, pp. 1727–1732.

70. Tambe, P. Big data investment, skills, and firm value. Management Science, 60, 6 (2014), 1452–1469.

71. Tapscott, D.; and Williams, A.D. Wikinomics: How mass collaboration changes everything. Penguin, New York, NY, USA, 2008.

72. The Importance of “Big Data”: A Definition. Accessed on January 01, 2018: https:// www.gartner.com/doc/2057415/importance-big-data-definition.

73. Thusoo, A.; Sarma, J.S.; Jain, N.; et al. Hive: A warehousing solution over a map-reduce framework. Proceedings of the VLDB Endowment, 2, 2 (2009), 1626-1629.

74. Van Rossum, G. Python Programming Language. In USENIX Annual Technical Conference. 2007, pp. 36. Santa Clara, California, USA: ACM Publishers.

75. Viegas, F.B.; Wattenberg, M.; Kriss, J.; and Van Ham, F. Talk before you type: Coordination in Wikipedia. In Proceedings of the 40th Annual Hawaii International Conference on System Sciences. 2007, pp. 1–10. Waikoloa, HI, USA: IEEE Publishers.

76. Wikipedia is fixing one of the Internet’s biggest flaws - The Washington Post. Accessed on October 25, 2016: https://www.washingtonpost.com/news/wonk/wp/2016/10/ 25/somethings-terribly-wrong-with-the-internet-and-wikipedia-might-be-able-to-fix-it/.

77. Wang, S.; and Iwaihara, M. Quality evaluation of Wikipedia articles through edit history and editor groups. Web Technologies and Applications, 6612, (2011), 188-199.

78. Winter, R. Design science research in Europe. European Journal of Information Systems, 17, 5 (2008), 470–475.

79. Wöhner, T.; and Peters, R. Assessing the quality of Wikipedia articles with lifecycle based metrics. In Proceedings of the 5th International Symposium on Wikis and Open Collaboration. ACM, Orlando, Florida, 2009, pp. 1–10.

80. Wu, G.; Harrigan, M.; and Cunningham, P. Classifying Wikipedia articles using network motif counts and ratios. In Proceedings of the Eighth Annual International Symposium on Wikis and Open Collaboration. ACM, Linz, Austria, 2012, pp. 1–10.

81. Xu, S.X.; and Zhang, X.M. Impact of Wikipedia on market information environment: Evidence on management disclosure and investor reaction. MIS Quarterly, 37, 4 (2013), 1043–1068.

82. Zhang, K.; Bhattacharyya, S.; and Ram, S. Large-scale network analysis for online social brand advertising. MIS Quarterly, 40, 4 (2016), 849–868.

83. Zhou, S.; Qiao, Z.; Du, Q.; Wang, G.A.; Fan, W.; and Yan, X. Measuring customer agility from online reviews using big data text analytics. Journal of Management Information Systems, 35, 2 (2018), 510–539.
