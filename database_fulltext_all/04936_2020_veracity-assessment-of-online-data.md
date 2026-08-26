---
otero_id: 4936
otero_key: "5H5EH52Z"
title: "Veracity assessment of online data"
authors: "Marianela García Lozano; Joel Brynielsson; Ulrik Franke; Magnus Rosell; Edward Tjörnhammar; Stefan Varga; Vladimir Vlassov"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113132"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

Veracity assessment of online data

Decision Support Systems

Marianela García Lozano, Joel Brynielsson, Ulrik Franke, Magnus Rosell, Edward Tjörnhammar, Stefan Varga, Vladimir Vlassov

![](/api/attachments/5H5EH52Z/fulltext/images/5b5eb977fa7503b1840b21101782080befb1c54a913a8c50730759361e9a0b55.jpg)

PII: S0167-9236(19)30161-7

DOI: https://doi.org/10.1016/j.dss.2019.113132

Reference: DECSUP 113132

To appear in: Decision Support Systems

Received date: 6 May 2019

Revised date: 16 July 2019

Accepted date: 16 August 2019

Please cite this article as: M. García Lozano, J. Brynielsson, U. Franke, et al., Veracity assessment of online data, Decision Support Systems (2019), https://doi.org/10.1016/ j.dss.2019.113132

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Published by Elsevier.

# Veracity assessment of online data

Marianela García Lozano<sup>a,b,</sup>∗, Joel Brynielsson<sup>a,b</sup>, Ulrik Franke<sup>c</sup>, Magnus Rosell<sup>a</sup>, Edward Tjörnhammar<sup>a,b</sup>, Stefan Varga<sup>b,d</sup>, Vladimir Vlassov<sup>b</sup>

<sup>a</sup>FOI Swedish Defence Research Agency, SE-164 90 Stockholm, Sweden <sup>b</sup>KTH Royal Institute of Technology, SE-100 44 Stockholm, Sweden <sup>c</sup>RISE Research Institutes of Sweden, P.O. Box 1263, SE-164 29 Kista, Sweden <sup>d</sup>Swedish Armed Forces Headquarters, SE-107 85 Stockholm, Sweden

## Abstract

Fake news, malicious rumors, fabricated reviews, generated images and videos, are today spread at an unprecedented rate, making the task of manually assessing data veracity for decision-making purposes a daunting task. Hence, it is urgent to explore possibilities to perform automatic veracity assessment. In this paper we review the literature in search for methods and techniques representing state of the art with regard to computerized veracity assessment. We study what others have done within the area of veracity assessment, especially targeted towards social media and open source data, to understand research trends and determine needs for future research.

The most common veracity assessment method among the studied set of papers is to perform text analysis using supervised learning. Regarding methods for machine learning much has happened in the last couple of years related to the advancements made in deep learning. However, very few papers make use of these advancements. Also, the papers in general tend to have a narrow scope, as they focus on solving a small task with only one type of data from one main source. The overall veracity assessment problem is complex, requiring a combination of data sources, data types, indicators, and methods. Only a few papers take on such a broad scope, thus, demonstrating the relative immaturity of the veracity assessment domain.

Keywords: veracity assessment, credibility, data quality, online data, social media, fake news

## 1. Introduction

As the internet has become a significant source of information for many, the need to assess the veracity of statements to, e.g., identify the spreading of false information, is apparent. Since individuals, companies, organizations, etc.—i.e., almost anyone—can write and post anything on the web, the information is often incomplete, ambiguous, contradicting, biased, or wrong. Further, due to the large amounts of heterogeneous information and the velocity with which it is created, it quickly becomes unfeasible to manually assess its veracity. A decision support system is only as good as its underlying data. The question of data veracity especially comes to mind whenever data retrieved from social media and other open sources is utilized. Hence, automatic, i.e., computerized, methods and tools capable of processing and assessing large amounts of data are needed.

The terms veracity and veracity assessment deserve a few words of introduction. The concept of veracity was introduced and became widely used among computer scientists after it, in 2012, was proposed as the fourth “V” [18, 91, 96] (the other ones being Volume, Variety, and Velocity) of big data [57]. In a blog post Snow [96] argues that trusted data needed to be defined separately in the era of big data, with its generally easy access to large volumes of heterogeneous data. Snow [96] states that “I believe that the definition of trusted data depends on the way you are using the data and applying it to your business.” Furthermore, veracity is presented as a concept that “deals with uncertain or imprecise data” which is an important property to take into account when data is analyzed and ultimately used for decision-making.

In a cursory overview of different veracity definitions in dictionaries, see Figure 1, one can observe proposals in which aspects of accuracy, credibility, truthfulness and quality can be used to delimit the term. These aspects represent several different but equally valid views of veracity that are interrelated. Hence, we note that it is hard to define such a broad term a in a succinct manner.

In the big data domain, data scientists and researchers have tried to give more precise descriptions and/or definitions of the veracity concept. Some proposals are in line with the dictionary definitions of Figure 1, while others take an approach of using corresponding negated terms, or both. An IBM report from 2012 describes veracity as “data uncertainty,” referring to the ability of “managing the reliability and predictability of inherently imprecise data types” [91]. Another IBM report from the same year, states that veracity has to do with managing “data in doubt” and relates it to “uncertainty due to data inconsistency, incompleteness, ambiguities, and deception” [18]. In the corresponding presentation the author also gives what could be interpreted as a definition of veracity, i.e., “truthful-

## veracity

![](/api/attachments/5H5EH52Z/fulltext/images/8e491cf49198044cda7ed0acc112f82a4ad3f68301f841da49797fd60d24f8b6.jpg)  
Figure 1: English online dictionary definitions of veracity as of November 2018.

ness, accuracy or precision, correctness.” There are many more examples; Lukoianova and Rubin [68] propose a veracity framework with three main veracity dimensions outlined by “objectivity, truthfulness, credibility and their opposites,” and Ramachandramurthy et al. [83] state that veracity “focuses on Information Quality (IQ).” It is worth pointing out that many of the veracity aspects such as data quality, truth, credibility, and trustfulness assessment, were not new and had before the big data inclusion in 2012 been addressed by researchers in related settings, e.g., decision support and information systems [2, 28, 70, 77, 104].

Another related veracity assessment concept is the indicator; an indicator is a predefined phenomenon of interest that may, or may not, be present in the data. The occurrences of one or several indicators can be used to facilitate the veracity assessment process. The indicators may also affect the confidence in an assessment positively or negatively. Indicators can also in themselves be assessed with regard to veracity. Whether a specific approach targets a single indicator or solves the whole veracity assessment problem is in many cases context-dependent: determining user credibility can for example both be a purpose in itself and be thought of as a veracity assessment indicator.

In sum, despite many researchers’ efforts, we assert that there is no prevalent generally agreed upon definition of veracity in academia. In this paper we refrain from adding yet another definition, but simply use a list of terms that are often mentioned in conjunction with veracity related to big data. They include truth, trust, uncertainty, credibility, reliability, noisy, anomalous, imprecise, and quality. As will be discussed in Section 2, such terms were used in the search strings employed in the literature study presented herein. We have also chosen to include studies of approaches, methods and algorithms related to indicators that may help with veracity assessment of data.

## 1.1. Purpose and problem statement

The purpose of this paper is to review the approaches, methods, algorithms, and tools which are used or proposed by the research community for automatic veracity assessment (VA) of open source data<sup>1</sup>, thereby obtaining a view of the state of the art for this domain. By open source data we refer to information published online such as social media posts, blog posts, forum entries, newspaper articles, etc., whether on the shallow or the deep web. Hence, the research question to be studied is the following:

Which approaches, methods, algorithms, and tools are used or proposed for automatic veracity assessment of open source data?

## 1.2. Outline

The remainder of this paper is structured as follows. Section 2 describes the chosen methodology and our choices in the execution of it. Section 3 contains the results of the undertaken systematic literature survey. This is followed by a synthesis and gap analysis discussion of the obtained results in Section 4, while the last section sums up the work and presents conclusions.

## 2. Review methodology

We address the research question in Section 1 by conducting a systematic literature review (SLR). An SLR aims to study scientific literature in an unbiased and reproducible way, aiming to find all existing works that fit the set criteria. Reasons for including or excluding studies are explicitly stated and agreed upon before searching for relevant studies. In this SLR the guidelines proposed by Kitchenham and Charters [52] were followed, which are briefly outlined in the following section.

## 2.1. SLR methodology

The first step in a systematic literature review is to formulate a main research question together with inclusion and exclusion criteria. The research question should embrace the purpose of the review and the inclusion and exclusion criteria help focus the scope of the research that is included in the survey. To reliably assess papers in a consistent manner, a review protocol along with instructions to the reviewers is created.

The next step is to design and plan the search strategy in the form of key terms combined into suitable search strings which are applied to relevant databases. This is preferably done with the aid of an expert librarian.

Once results have been gathered, the inclusion and exclusion criteria are applied, filtering and narrowing down the final set of papers to review. This is an iterative process, starting by looking only at the title, keywords and authors, then reading the abstract, and in the final iteration reading the full text to decide on whether to include the paper.

In Sections 2.2–2.5 the application of the SLR methodology in the present study is described.

## 2.2. Search strategy

Based on the purpose and objectives of the survey and our previous knowledge of research within the domain, the following set of keywords was used as a basis for a search conducted by a professional librarian: veracity, credibility, assessment, social media, open source data, rumors, and fake news.

We expanded the set of keywords with related terms and synonyms which were primarily gathered by analysis of the dictionary definitions (see Figure 1) and Google searches. With the aid of expertise within library search methodology and online libraries we finally obtained a set of search questions, see Table 1, which were then applied to the list of online databases, see Figure 2. The list of search strings is not an exhaustive list of keyword combinations since that would only inflate the amount of results without adding much to the findings. The search string list is rather based on a trial and error process looking for coverage and relevance.

The number of hits each database generated using the search strings can be seen in Figure 2. Note that not all of the inclusion and exclusion criteria have been applied at this stage. The total number of hits was 5047. Since i) some papers are indexed by multiple databases, and ii) different search strings sometimes triggered the same papers, this number contains duplicates.

## 2.3. Inclusion and exclusion criteria

The list of inclusion and exclusion criteria used to filter the search results are:

```txt
Nr Search string
1 “assessment*” AND (“credibility” OR “veracity”) AND “social media”
2 “assessment*” AND “credibility” AND (“fake news” OR “misinformation”）
3 “assessment*” AND “fake news” AND “open source data”
4 “assessment*” AND (“lie*” OR “truth*”) AND “social media”
5 “assessment*” AND (“rumor*” OR “rumour*”）
6 “assessment*” AND “open source data” AND “social media”
7 “credibility” AND (“facebook” OR “twitter”) AND (“fake news” OR “misinformation”）
8 “credibility” AND “social media” AND (“fake news” OR “misinformation”）
9 (“credibility” OR “veracity”) AND “open source data”
10 “fake news” AND (“misinformation*” OR “reliability” OR “truth*”) AND “social media”
11 “misinformation” AND (“instagram” OR “snapchat”）
12 “open source data” AND “social media”
13 “validate*” AND (“facebook” OR “twitter”) AND “fake news”
14 “validate*” AND (“facebook” OR “twitter”) AND “misinformation”
15 “veracity” AND (“facebook” OR “fake news” OR “twitter” OR “misinformation”）
16 “veracity” AND (“rumor*” OR “rumour*”) AND “social media”
17 “veracity” AND (“lie*” OR “truth*”)
```  
Table 1: Search strings.

1. Only papers related to automatic/computerized approaches, methods, algorithms and tools are included.

2. Only papers using or discussing open source data are included.

3. Only assessment studies with the purpose of assessing veracity or some related aspect are included. That is, research related to, e.g., the veracity phenomenon as such is excluded.

4. Only research published between 2013–2017 is included, which provides a cut-off criterion and at the same time provides a recent view of the methodologies in use.

5. Research published in any other language than English (British and American spelling) is excluded, i.e., only work available to the wider research audience is included.

Due to the automatic filtering possibilities inherent in the databases, criteria number four and five were used in the searches. Some non-English results were still obtained, but eliminated later in the process.

![](/api/attachments/5H5EH52Z/fulltext/images/e67a8822d4fd8de7f6d4625ac04971f6d0cdfcd7b5ae95f63f164d8e72eee971.jpg)  
Figure 2: Paper selection and review process.

## 2.4. Study selection process

The database searches were conducted in February 2018, and in the subsequent months the filtering and reviewing process took place. The literature selection consisted of an iterative funnel-like process, see Figure 2, where the search results were screened based on the SLR method according to Section 2.1. With the inclusion and exclusion criteria at hand, filtering of the data base results was done based on title, keywords, and authors, resulting in a total of 346 papers left. In the following iteration we read the abstracts and were able to remove 159 more papers, leaving us with 187 papers. The last filtering iteration was based on a cursory glance at the full papers, resulting in a set of 112 papers. This final set of papers were read and reviewed in full. On closer inspection, however, five more papers were removed from the final set due to non-complacency with the inclusion-exclusion criteria.

## 2.5. Review protocol and objectives

Based on the main research question and purpose of the study, a review protocol which was used by all reviewers to analyze the chosen papers was developed (see Appendix A for the full protocol). The research question part of the review protocol is further divided into six groups: approaches, methods, algorithms, tools, data, and miscellaneous questions about issues indirectly related to the main research question. This division was done to provide a good basis for analysis of the papers and synthesis of the results.

## 3. Results

Out of the 107 papers that were reviewed there is a clear trend in the publication year. The majority of the papers, i.e., 65%, are published in the last two years of the explored time range, i.e., between 2016 and 2017, as can be seen in Figure 3a. The majority of the papers are also published by authors affiliated with a university or institute, and about a quarter of the papers have a mixture of affiliations, e.g., university with company or university and institute, see Figure 3b. The one country which most authors have as affiliation is USA with participation in 37 of the publications, see Figure 3c. China, which was the runner up country, has representation in 15 papers. Grouping the country affiliation in geographical regions, the most productive region is Europe with participation in 50 of the publications, i.e., almost half of the examined papers, see Figure 3d.

## 3.1. Approaches

As discussed in Section 1, veracity assessment often, but not always, makes use of indicators as a basis for making the end assessment, and in many cases it is context-dependent whether a specific approach targets a single indicator or solves the whole veracity assessment problem: determining user credibility can for example both be a purpose in itself and be thought of as an indicator [1]. With this precaution in mind it is still interesting to note that the investigated papers can be roughly divided into two broad equally sized categories dependent on their focus: about half of the papers set out to perform the veracity assessment directly [37, 48, 84, 62, 5], whilst the other half of the papers have a clear focus on the indicators (in themselves or as a means of performing the overarching veracity assessment) [61, 88, 3, 56, 6].

![](/api/attachments/5H5EH52Z/fulltext/images/5f3dae7e78e196486cfc9f8e271d505243171d25c642c11a0f4c1dc7daed93a1.jpg)  
(a) Publication year.

![](/api/attachments/5H5EH52Z/fulltext/images/ba389ea6ba3e55d1808bd2f8eb4bdf01228f6cf8a40432738f0b2cb3da2a912f.jpg)  
(b) Affiliation.

![](/api/attachments/5H5EH52Z/fulltext/images/ca83b309b45215935307d8ecb2df760daaa07cc1c39126f1db2c4f48a024e52c.jpg)  
(c) Countries.

![](/api/attachments/5H5EH52Z/fulltext/images/f11537aebd6cf6ca3e55c33aa7084767467b47863adaffb1ed1f5b0bcf63bead.jpg)  
(d) Geographical region.  
Figure 3: Reviewed paper statistics.

Two main indicator “dimensions” can be discerned. The first indicator dimension is related to the data origin, with indicators derived from, i) message content, ii) meta data, and iii) external sources. Focusing on approaches used for solely looking at the actual message content itself, indicators for sentiment/affect and opinion/stance are the predominant ones [25, 36]. The ingenuity when it comes to the aforementioned external sources is large, including, e.g., crowd sourcing (letting own users tag the tweet) [89], and could give rise to further division into several dimensions of external sources.

The other indicator dimension can be related to some underlying modeling aspect where the algorithm developer starts with an idea of some aspect that can be used for veracity assessment and tries to model this aspect to confirm or disprove the veracity. One example of this modeling dimension is coordinated behavior where, e.g., many users exhibiting similar behavior could be used as an indicator [1]. The indicators used typically relate to the assumptions being made regarding the intended end user application, e.g., the availability of databases for verifying claims [125, 90, 82, 85], whether additional messages can be used for comparison, etc. As a consequence, many interesting examples of special cases that can only be used in a specific context exist. For example, facts related to soccer games can be used to make good assessments specifically related to soccer claims [44], and meta data concerning geographical positioning can be combined with knowledge regarding traffic patterns [23] and points of interest [6] to improve the veracity assessment in infrastructure contexts.

In the papers/approaches making use of indicators, the motivations for the choice of indicators can be divided in three about equally sized categories: i) related work is used to motivate the indicator(s), e.g., [122, 16, 58], ii) a convincing argument based on intuition is provided, e.g., [1, 85, 14], or iii) the paper serves in itself to investigate and motivate the indicator(s) used, e.g., [6, 78, 64].

Concerning quantification and presentation of the veracity assessment result, the typical veracity assessment approach calculates a probability to be used for presenting some kind of discrete result depending on the application at hand. In most cases a binary yes/no answer is calculated, e.g., [126, 118, 42], but in some cases the probability measure is used for more fine-grained quantification on a scale [35] and sometimes there are more than two classes to be distinguished between [37, 62]. The few exceptions that stand out include cases where the algorithm design necessitates alternative quantification methods where, e.g., a relative score is calculated and used for ranking different alternatives [78], and cases with alternative means of presentation using, e.g., heat maps [127].

All but a few papers present some kind of a more or less scientific evaluation of the result. Depending on the foreseen application and focus, these evaluation efforts typically target i) the invented method and/or algorithm, ii) the assessment itself, iii) the data, and iv) the end user application. Although much related to the application and focus, it is still interesting to note that roughly two thirds of the evaluation efforts relate to the presented method/algorithm [42, 46, 93], while the rest of the evaluations, i.e., one third, are directed towards the veracity assessment itself [125, 45, 95]. Some papers include evaluations of several aspects, a handful of the papers evaluate the data [62, 25, 126, 17, 40, 92], and yet a few papers include evaluations related to the envisioned end user application where things such as tool usability is included [35].

## 3.2. Methods

This section seeks to epitomize the methods used for automated veracity assessments. The results obtained in the literature review revealed that not all articles actually describe a complete process for this. There are exemples of vague or imprecise research questions, and articles where only parts of the process are adressed, e.g., the algorithms or the process of calculating some score. Others describe inventions or methods to create training data. There are also other literature reviews. In sum, it is difficult to present general characteristics describing the most common methods due to this diversity. Out of the articles that describe semi-automatic and automatic veracity assessment procedures in some detail, however, which constitute the majority of the articles, there are some general steps that can be discerned. First, there is the data aquisition phase, in which a data set is typically downloaded according to some criterion. Second, there is a pre-processing stage in which the data is arranged, and possibly classified. Third, extraction of features that are needed for the following calculations commences. Fourth, some algorithm is used to calculate workable numeric values. Finally, some classifier that determines the final assessment is invoked.

Most papers present one or more explicitly stated research questions, e.g., differences between rumors and counter-rumors [16], exploiting topology properties to assess whether a Weibo post is a rumor or not [118], automatic detection of relevance in social networks [25], etc. Somewhat surprising, quite a few papers lack explicitly stated traditional research questions. However, for many of these papers plausible ulterior research questions and purposes can often be inferred by analyzing the used methods and approaches. Yet in some papers, original research questions are hard to discern or absent. As previously discussed in Section 1, the selected sample of research papers demonstrate a lack of consensus regarding the definition of crucial terms, such as credibility, truthfulness, and veracity. This, what can be called term inexactitude, in the context of the research challenges presented here, contributes to muddle the clarity and precision of the posed research questions.

The main aim of our structured literature review is to evaluate articles that seek to determine veracity or a comparable property of a statement in an automated fashion (see Section 1). Hence, we have contributions that seek to determine credibility [61, 73, 75], truthfulness [49, 121, 40], rumors [97, 116, 86], and geolocation [87, 122, 71, 30].

A range of papers do not examine veracity per se, but rather develop methods for doing so. On this meta-level authors have developed algorithms [24, 1], novel inventions [125, 35], or created training data (sets) suitable for further research [123, 71], and for example, an approach to combine relevance and credibility scores into a single value [63]. Another category contains the secondary research articles constituting of literature reviews, though with slightly different scopes, [43, 86, 33].

The majority of the papers propose methods that are semi-automatic, that is: some part of the process requires manual intervention, e.g., the downloading of data, labeling, the determination of thresholds, result assessments, etc. [38, 60, 16]. In a second category, some articles claim to produce fully automated veracity assessments [98, 85, 27]. A third category do not claim to perform automatic veracity assessments, but the proposed solutions were judged by the authors of this paper to be fully automated with limited additional work, e.g., [101, 90].

The application fields in which statements of veracity were to be examined include, most commonly, the news production business. Much interest was shown for potential or established news outlets that produce or distribute news [105]. More specifically, some aim to judge newsworthiness (i.e., newsworthy events) [13], while others try to distinguish actual news items from informal chat [25]. Other application fields include health related information [126], and politics [14]. A few papers include geospatial information [6, 122, 30] as an indicator.

About a dozen papers seek to study phenomena such as rumors and hoaxes from different perspectives, e.g., [56, 16, 11]. Again, the notion of term inexactitude that we previously mentioned, apply to terms such as rumors and hoaxes as well—neither of which are consistently defined. This means that what is treated like a hoax in one paper, can be labelled as a rumor in another.

The majority of the proposed approaches that were found in this review use Twitter as source data. However, most of the methods are judged to be versatile enough to also use other data source types, e.g., [98, 66, 120].

In general, detection and propagation methods are studied. Some want to detect and determine whether an item is or is likely to become a rumor, e.g., [118, 42, 97, 124]. Others seek to track how rumors or misinformation spread, e.g., [64, 127, 121]. Some have a more peripheral interest, such as the interplay between rumors and counter-rumors, e.g., [16], as well as the detection of users who spread rumors, e.g., [85, 20]. With regard to hoaxes, some want to examine misinformation in the form of hoaxes [56].

## 3.3. Algorithms

Almost half of the papers report using machine learning (ML), e.g., [37, 36, 85] (see Figure 4a). Of these the clear majority use supervised machine learning, e.g., [44, 16, 51], of which a smaller number use some variant of semi-supervised methods, e.g., [34, 60, 10], and only very few use unsupervised methods, e.g., [120, 119, 94]. Of the other half of the papers, some present methods that are not based on machine learning, some are surveys, and some describe data or user behaviors. A large number of different algorithms are used, and some papers try several, or use a combination of several algorithms to achieve their end result, e.g., [48, 8, 3]. Some papers develop specific algorithms for the problem, e.g., [123, 6, 117], while others use well known algorithms (as part of their method), such as support vector machines, e.g., [66], Naïve Bayes, e.g., [118], Random Forests, e.g., [12], clustering algorithms, e.g., [49], methods for logistic regression, e.g., [5], etc.

![](/api/attachments/5H5EH52Z/fulltext/images/ce8c5b8a62ca19d3d163e5de7373330e35d708273055d51e8d42222d64c8fe20.jpg)  
(a) Machine learning (ML).

![](/api/attachments/5H5EH52Z/fulltext/images/e1463860336b035d50c96e57465654326c9b058e4ec7c63f835ea0dfec77a047.jpg)  
(b) Online or offline algorithm?  
Figure 4: Algorithm statistics.

About two fifths of the papers claim that their algorithms work online, e.g., [5, 11, 119], see Figure 4b. Another two fifths describe algorithms that only work offline, e.g., [16, 120, 32]. The last fifth of the papers contain surveys, descriptions of data, or of user behavior, e.g., [127, 29, 100].

For evaluating the methods almost half of the papers use a measure based on the confusion matrix between the result of the algorithm and a known categorization, such as precision, recall, f-measure, etc., e.g., [88, 125, 79]. There are many other measures used for evaluation, and if we count them all almost 70% of the papers make some kind of evaluation, e.g., [124, 94, 106]. Of these, 55% of the papers use machine learning, e.g., [3, 16, 39], which also means that 80% of the machine learning papers make some kind of evaluation.

## 3.4. Tools

This section gives an overview of the tools employed for veracity assessment by the authors of the studied papers. Around 45% of the papers report the details of all, or parts of, the used tools. Some of the reviewed papers do, however, not implement anything since they are of a visionary, methodological or survey type. The rest of the papers contain no or very sparse information on the used tools. The reported tools and libraries that are in the studied literature belong to a few subfields of data science, information management and artificial intelligence, namely, natural language processing (NLP), machine learning and big data analytics, i.e., large-scale data processing. The use of tools and libraries from different sub-fields is motivated by the tasks and corresponding steps in veracity assessment, e.g., linguistic analysis of textual data, data collection, and network analysis. Common NLP tools used in the reviewed papers are i) the Natural Language Toolkit (NLTK) [67], ii) Stanford CoreNLP [69], iii) the Stanford dependency parser [21], iv) TweeboParser, a Twitter dependency parser [53], v) the Linguistic Inquiry and Word Count (LIWC) [80], and vi) semantic similarity word vectors like Stanford GloVe [81] and Word2Vec [72].

Rather many of the studied papers, e.g., [103, 32, 55, 30], report the use of Twitter APIs from its developer platform. In particular, the Search API and the Account Activity API, for collecting tweets, finding historic tweets, and obtaining user account statistics, are used. Other examples of tools used in the papers for processing tweets are i) Apache Flume [108], used for streaming tweets from the Twitter API based on a predefined set of keywords [4, 78], ii) Apache Spark [111], a distributed/cluster computing solution used to process tweets [30], iii) networkx [112], a Python library for creating and manipulating complex networks, e.g., used to construct tweet propagation graphs [103], iv) NeuroLab [113], a neural network library for Python used by, e.g., [32], v) scikitlearn [114], ML tools/library in Python used by, e.g., [39, 27], vi) Apache Hadoop [109], a framework for distributed processing of large data sets across clusters of computers, e.g., [13, 22], and vii) Apache Hive [110], a data warehouse software project built on top of Apache Hadoop for provid ing data query and analysis using SQL used by, e.g., [4].

Almost 18% of the papers state that they use open source tools, but the real number is probably much higher since a majority of the papers provide no or little information of used tools and implementation details, see Figure 5.

![](/api/attachments/5H5EH52Z/fulltext/images/bf73d45da73d04c98d835682587a3f123a14e044ecead545450cdc4551e00000.jpg)  
Figure 5: Nature of used and developed software.

Only around one tenth of the papers have made their tooling publicly available, usually through a web-link, e.g., [92, 74, 50]. Thus, the majority do not provide any details.

## 3.5. Data

An overwhelming majority of the research approaches include mining text of some form, see Figure 6a. Text data types range from i) microblogs, e.g., [6, 13], i.e., short status updates on open social networks, and ii) short texts, e.g., [5, 61, 102], i.e., under 500 words, to iii) long texts, e.g., [82, 92, 60], i.e., more than 500 words. Graph data is the second most common data type. The “not applicable” class consists primarily of exploratory surveys, e.g., [86, 100], books, e.g., [33, 9], and visionary papers, e.g., [29].

![](/api/attachments/5H5EH52Z/fulltext/images/a1c8570a357c8bc3798986a209b54ced2bf5b2ecb90b651715e30855c8af747f.jpg)  
(a) Types of data.

![](/api/attachments/5H5EH52Z/fulltext/images/6d0cd64fa0ea2b94b2794f5ff9169cccec753d160b33c944ff084c8604023dba.jpg)  
(b) Data sources used in two or more papers.  
Figure 6: Types of data, and data sources.

Mining veracity assessments themselves, e.g., [125, 38], for veracity assessment is more common than algorithms which process images, e.g., [46, 38], geospatial data, e.g., [122, 87, 31], generic data (any kind of data), e.g., [1, 24], and keyword based approaches, e.g., [95, 74]. Waveform mining, e.g., sound and optical data, in any form, is completely absent in the approaches presented in the studied papers.

As for the data sources, the vast majority of the papers rely on microblogging services such as Twitter [90, 23, 35, 46, 11, 32] and Weibo [118, 49, 105, 34] (see Figure 6b). Relying on news agencies is more common among papers where the authors are affiliated with China than other countries [47, 105]. Using “fact baseline” sources such as Wikipedia and DBpedia [94, 93, 17] or news agencies [10, 105, 25], is as commonly relied upon as review sites such as Dianping [102], TripAdvisor [5], or Yelp [27, 26]. Geospatial sources, such as FourSquare [122] or GIS services as well as image sources like Instagram [115], are only used by a handful of papers.

As depicted in Figure 7, almost two thirds of the papers use their own collected authentic data, e.g., [54, 41, 102], whereas one fourth rely on already collected known data sets, e.g., [74, 5]. One fifth of the papers lack details regarding their data set acquisition process, e.g., [117, 99, 43]. A few papers rely on synthetic data, e.g., [94, 8, 106], as part of the data acquisition process, and sometimes also combine the approach by using either authentic or known data sets. Only one paper combined the usage of authentic data and known data [65].

![](/api/attachments/5H5EH52Z/fulltext/images/6b737ae3a003c2c31e9db258d24251a71ee242b032482caa510ba4d0670b840a.jpg)  
Figure 7: Data acquisition process.

One out of five papers indicate how to access the data sets, mostly as web URLs, e.g., [37]. The most common way among these papers is to share the data sets via GitHub, e.g., [127, 12, 50]. Otherwise we were unable to find any commonalities between papers with regards to data set sharing services: one used Dropbox [47], some used plain web servers, e.g., [37, 56], and one explicitly stated that the data set was available upon request [13].

One of the review protocol questions investigated the possibility for data set reuse, and specifically whether the available data can be used for veracity assessment benchmarking. The criteria for whether the data set is benchmarkable is i) if the data is publicly available, and ii) if there is a suitable performance metric target with regards to veracity or an indicator. One in six papers contain enough details regarding their data sets for them to be usable as benchmark data, e.g., [62, 5, 93, 27, 50].

As previously mentioned in Section 3.4, a common data source is Twitter. The data gathering is mostly done using the Twitter streaming API, which is used for collecting microblog posts and annotating them with meta data. The second most popular data gathering method is web crawling and scraping, e.g., [37, 43, 26, 115].

Regarding the data selection criteria, the most common approach is keyword based, e.g., [4, 54, 32, 115], whilst automatically mining keywords for data acquisition is not that common, e.g., [127]. Many papers select data based on time frame ranges, rather than topics, e.g., [48, 84, 23, 49].

Regarding data use, the papers mainly focus on content and to a lesser extent on meta data and social graph structures. Popular features include (where applicable) number of replies, “retweets,” number of connections, number of positive/negative words, entity frequency, and word class percentages.

The majority of the papers do not include any specific statistical analysis or amendments related to skewed data. The minority cases consist of the papers for which the proposed method could work on multi-sourced data under non-independent identically distributed assumptions, e.g., [84], makes skewness adjustments, e.g., [93], or performs data exploration as part of the evaluation [54]. The most common assumption concerning the data is that it has the right membership, i.e., that it belongs to a rumor/event, e.g., [105, 3, 86, 15], is a review, e.g., [101], or concerns the topic, e.g., [55, 39, 50]. It should also be noted that papers without any explicitly mentioned assumptions regarding data distribution might still have implicit assumptions. Similarly, the methods proposed in most papers rely on the data exhibiting a specific shape, i.e., that entries contain certain strict features or value ranges, e.g., [36, 87, 10, 106, 55], albeit not being explicit about it. Some papers also rely upon the veracity of features of a data point being inherently correct, e.g., have correct geographical information [6, 71], or have assigned credibility scores [64].

## 3.6. Miscellaneous

As previously discussed in Sections 1 and 3.2 there is a term inexactitude and breadth present regarding the definitions of central terms such as veracity and its closest concepts, i.e., credibility, truth, quality, etc. The results show that only a handful of the papers analyzed offer explicit definitions of veracity or veracity assessment. Thus, the following definition is given by Jamil et al. [43], in turn based on Bennett-Woods [7]: “Data veracity refers to principles of truth-telling, and it is grounding in respect for persons and the concept of autonomy.” Bodnar et al. [11] give a two-fold definition in passing: “veracity referring to the accuracy and truthfulness of the data as well as the ability of the data to predict trends.” Robin et al. [87] equate veracity with truthfulness: “Veracity refers to the degree of truthfulness associated with a data set,” as does Debattista et al. [22]: “conformity with truth or facts.” Wang et al. [105] also remark very briefly: “veracity (trustworthiness of various data).”

Conroy et al. [19] implicitly define veracity by how it is compromised: “Veracity is compromised by the occurrence of intentional deceptions.” A similar approach is taken by Bhattacharjee et al. [10], stating that “[t]he objective of a news veracity detection system is to identify various types of potentially misleading or false information.”

A few other papers give operationalizations intended only for the paper itself, such as “[t]he probability of a tweet to be a counter-rumor is referred as tweet veracity in this paper” [16].

However, most papers do not define veracity or veracity assessment. Instead they introduce, define, or discuss other related terms and concepts. Examples include deception, e.g., [99], misinformation, e.g., [54, 64], credibility, e.g., [101, 25, 73, 39, 50], reliability, e.g., [121], believability, e.g., [32, 25, 100], trust and trustworthiness, e.g., [1, 32, 10, 35], truthfulness, e.g., [94, 121], and truth discovery, e.g., [31, 8]. Again, some give operationalizations intended only for the particular paper, such as a “rumor is defined as any information posted on Twitter, that many people believe to be true, but it contrasts with the news tweets from the verified news channels” [42].

Turning to legal and ethical issues of automated veracity assessment, these are absent in all but a single paper. Webb et al. [107] alone discuss ethical issues as a prominent part (Section 4) of their effort to define a research agenda on the governance and regulation of social media. However, they do not discuss ethics directly related to veracity assessment. No paper discusses legal issues.

Assessing the relevance of the papers to the main research question, as introduced in Section 1, most of the papers read are of high or medium relevance, as is to be expected given the selection process and search strategy as outlined in Section 2.1. However, some papers are assessed to be of low relevance.

As expected, the breadth of the scientific contributions made in the reviewed papers is significant. Even though the papers all address some aspect of veracity assessment of online data, the ranges of methods, algorithms, tools, data, etc., are substantial. Nevertheless, a “typical” paper i) proposes some kind of method or algorithm that is either entirely novel or more commonly an addition or improvement to an existing one, ii) applies it to some interesting data, and iii) evaluates the results. However, as the papers apply their methods to investigate interesting phenomena, they sometimes also make positive social science contributions, e.g., about the characteristics of Wikipedia hoaxes [56], about differences between true and false health rumors [126], and about the interplay between fake news promoters and grass-roots responses [92]. Another kind of contribution found, as previously described in Section 3.5, is the introduction of data sets subsequently made available to the research community, e.g., [85, 73, 50]. Unfortunately, another not too uncommon deviation from the typical paper structure outlined above is that the evaluation is missing, very narrow, or flawed in some other

way.

A large majority of the papers contain primary research contributions. In addition, a handful of secondary research contributions, i.e., literature reviews, were included [86, 43, 33, 100, 22, 99, 19, 107]. Furthermore, some papers are best characterized as positional, i.e., discussing interesting ideas for future research rather than making full contributions in their own right.

Unsurprisingly, the large majority of papers are directed towards the scientific community, mostly that consisting of computer scientists. When a particular application or interest group is mentioned, journalism (including both the supply-side of journalists writing news articles and the demand-side of consumers reading them) is the most common [40, 97, 66, 65, 19]. Other perspectives include marketing [5], e-commerce [117], medicine [75], social network moderation [48, 47], and the mili tary [59].

## 4. Synthesis and discussion

In this section we synthesize and discuss the results presented in Section 3. The section consists of four subsections containing discussions on i) approaches and methods, ii) algorithms, tools, and data, iii) gaps, and iv) validity and reliability.

## 4.1. Approaches and methods

Looking at the descriptions of indicators, methods, and definitions (mostly implicit) of veracity used in the papers, three broad categories of veracity operationalizations can be discerned: i) implicit features, ii) explicit fact checking, and iii) appeal to authority.

The implicit features approach is by far the most common. Roughly, the idea is that claims that are (in some sense) non-veridical differ from claims that are veridical in other, non-veracity, properties. Such properties include stylometric text features such as length and wordings [37, 56, 82], URL features such as link densities [56] or domain names [97], temporal distributions [92, 117, 103], (social network) distribution patterns [1, 92, 117], and user account features [89, 97].

The explicit fact checking approach is rare, but a few examples were found [94, 59]. The idea is to compare a claim made to an existing body of knowledge so as to determine if it is veridical. Typically this involves representing the claim as a subject-predicate-object triple, and then using graph-methods to compare it to existing knowledge triples.

The appeal to authority approach, in its most crude form, is also rare. The idea is that a claim is veridical if it is claimed by an authoritative source. For example, a photo can be trusted if shared by a trusted source 30 minutes after the event [115], and a claim can be considered veridical if supported by the majority [76] or by verified news channels [42].

It should be noted that the mentioned three approaches are often combined to achieve better results. For example, a moderate appeal to authority is often blended into the implicit features approach by, e.g., including some PageRank-like features among the other implicit features considered [41, 54, 82].

## 4.2. Algorithms, tools, and data

That most papers that are concerned with machine learning have used supervised methods is not a surprise. Veracity estimation is a very difficult task and the veracity is probably in many cases dependent on factors external to what is available to the algorithm. Therefore, in most situations the results of these algorithms should be subject to manual consideration. In such scenarios unsupervised methods could prove quite useful as a complement, and provide the human with more information.

It is remarkable that two fifths of the papers describe algorithms/methods that work online, considering how complex veracity assessment is. It should probably be understood that these online algorithms, i.e., algorithms that work with streaming data, scale well over processing cores. On the other hand, methods that do not work online (two fifths of the papers) can potentially work in some kind of batch version, although this may require extra resources to update knowledge over the entire data set.

There seems to be a big problem with reproducibility in veracity assessment research. Many papers do not share source code, models, and data. This can be in the form of missing URLs, due to updated web pages and absent servers, or even underspecified details in the paper. Some authors rely on known data sets and software, but fail to disclose versioning constraints or what parts were used. None of the papers provide DOI links to point out the research materials used or to publish trained models.

The main data source in many papers is Twitter. Hence, it is unsurprising that many of the reviewed papers are text oriented. The majority of the tooling is adapted thereafter and is mostly focused on different types of linguistic analysis, supervised machine learning, and big data analytics.

One would expect many proposals to contain intricate computations relying on diverse data sources and data type sets. However, a majority of the papers have a narrow focus using only one data source and/or data type for a specific algorithm, which can be seen as an indication of the immaturity of the field. Only a handful of papers use, or are adapted for, multiple sources, which in many cases would be necessary in a real application, see, e.g., [10, 74, 105].

## 4.3. Gap analysis

A gap analysis based on the obtained results and synthesis is presented in this section. The identified gaps summarize the main challenges that have been identified through the systematic literature review.

Multiple sources and data types. Of the analyzed papers very few approaches or methods are adapted to handle multiple sources and/or data types. Since one of the pillars of source criticism or information evaluation is the comparison of information from multiple sources and data types, this should also by extension be a criterion for future automatic veracity assessment systems. One could argue that sources like Twitter and other microblogs are in essence multiple sources since the expressed opinions come from various individuals. However, the format is limited and the expressed opinions/information to a very low degree come from authoritative sources. Also, even though other data types such as links, images, sound, and video, are sometimes embedded, very few of the approaches make full use of these additional data types.

Common definitions of core terminology. As discussed in the introduction of this paper, there is no common definition of the core terminology related to veracity or veracity assessment. The analysis of the selected papers showed that the lack of consensus is also present in related terms, e.g., credibility, rumor, and source, making it cumbersome for the research community to compare results and follow the state of the art within the domain.

Reproducibility. Another challenge which was identified in the synthesis is the difficulty of reproducing obtained results. Lack of details or accessibility to data sets, code, and used tools, make reproducing results difficult if not impossible.

Data sets suitable for benchmarking. One of the identified gaps is the limitation of suitable data sets with which the research community can compare results and follow the development of methods.

Deep learning and transfer learning. Machine learning has, with recent years’ reemergence of deep learning, made giant leaps and has had unprecedented success in a number of fields. However, the use of deep learning techniques in the evaluated paper set is very low, and a research gap is clearly present. This is also related to the previous point—the lack of suitable data sets—which further limits effective use of machine learning.

Scalable online methods and data. Many of the used approaches and methods are theoretically scalable or applicable in an online setting. However, the majority of the reviewed papers results come from experiments which have not focused on scalability or streaming data. For a realistic open source data veracity assessment application, these two aspects (scalability and ability to handle streamed data) are probably crucial.

## 4.4. Validity and reliability

The main strength of validity of the present study is the rigor and transparency of the method employed, adhering to the guidelines of Kitchenham and Charters [52]. In practice, this means that all papers reviewed were selected from databases of renowned peer-reviewed sources, and match explicit inclusion criteria, as listed in Section 2. Thus, the selected papers should comprise a representative selection of the research done in the veracity assessment community.

A moderate threat to validity relates to vocabulary and search strings—the queries listed in Table 1 reflect a Western bias in terms of services (e.g., Facebook, Twitter, Instagram) and language (English). Still, this threat should not be exaggerated—the vast majority of high-impact computer science research is published in English regardless of origin (as is also suggested by the diverse distribution of countries and geographical regions in Figure 3), and the services mentioned in the queries are truly global, even though there are countries where they are barely used.

A small threat to validity is that there is a bias in the review protocol towards computer science in general and machine learning in particular. Social science terms and methods are not similarly reflected. However, this largely reflects a legitimate delimitation of the research questions, and the residual threat to validity is minor.

A moderate threat to reliability is related to the review protocol, where some questions, notably in part 2 in the protocol (see Appendix A), can be interpreted in different ways. Though every effort was made to ensure reviewer agreement on these questions, conclusions should be interpreted in light of this risk.

## 5. Conclusions

The main purpose of this paper has been to investigate which approaches, methods, algorithms, and tools that are used or proposed for automatic veracity assessment of open source data, which is important to consider should the data be used for decision-making in itself or as part of a decision support system. The purpose was also to see how far the research community has progressed since the introduction of veracity (assessment) in big data back in 2012. Using a structured literature review method, papers have been identified, selected and evaluated following a predefined assessment protocol. The protocol was constructed for the purpose of analyzing the research literature targeting veracity assessment of heterogeneous and unstructured open source data, including social media.

One of the things revealed in the results is that in the years that have passed since the inception of veracity in big data, researchers have not reached consensus on a veracity (assessment) definition. Despite this, there is some convergence in the methods used to assess veracity. Three main veracity assessment research approaches were found. The implicit features approach hypothesizes that nonveridical statements differ from veridical statements not only concerning the actual claim but also in other aspects that can be used for assessment. Next, the explicit fact checking approach makes use of external data to evaluate a claim in relation to existing knowledge. Finally, the appeal to authority approach stipulates that a claim can be trusted if it is also claimed or can be verified by an authoritative source. Legal and ethical aspects have unfortunately been discussed to a very low degree. A reproducibility problem can also be seen where many papers are lacking in data gathering details, data sets are not publicly available, and details regarding toolsets and implementation are sparse.

The identified gaps in the current literature mainly consist of i) a general lack of approaches and methods adapted to multiple sources and data types, ii) a lack of consensus in the definitions of core terms, iii) reproducibility challenges, iv) very few available data sets suitable for benchmarking purposes, v) low use of recent advancements made in machine learning, and vi) a lack of research efforts targeting scalable solutions for managing streaming data.

## Acknowledgments

We gratefully acknowledge the help obtained from the librarian Alexis Wiklund, for performing the initial database literature searches. This work was supported by the Swedish Armed Forces.

## References

[1] Abbasi, M.-A., & Liu, H. (2013). Measuring user credibility in social media. In A. M. Greenberg, W. G. Kennedy, & N. D. Bos (Eds.), Social Computing, Behavioral-Cultural Modeling and Prediction (pp. 441–448). Berlin, Heidelberg: Springer Berlin Heidelberg. doi:10.1007/978-3-642-37210-0\_48.

[2] Abdul-Rahman, A., & Hailes, S. (2000). Supporting trust in virtual communities. In Proceedings of the 33rd annual Hawaii international conference on system sciences (pp. 9–pp). IEEE.

[3] Aker, A., Zubiaga, A., Bontcheva, K., Kolliakou, A., Procter, R., & Liakata, M. (2017). Stance classification in outof-domain rumours: A case study around mental health disorders. In G. L. Ciampaglia, A. Mashhadi, & T. Yasseri (Eds.), Social Informatics (pp. 53–64). Cham: Springer International Publishing.

[4] Ashwin, K. T., Kammarpally, P., & George, K. (2016). Veracity of information in twitter data: A case study. In 2016 International Conference on Big Data and Smart Computing (BigComp) (pp. 129–136). doi:10.1109/BIGCOMP.2016.7425811.

[5] Ball, L., & Elworthy, J. (2014). Fake or real? the computational detection of online deceptive text. Journal of Marketing Analytics, 2, 187–201. doi:10.1057/jma.2014.15.

[6] Bendler, J., Wagner, S., Brandt, T., & Neumann, D. (2014). Taming uncertainty in big data. Business & Information Systems Engineering, 6, 279–288. doi:10.1007/s12599-014-0342-4.

[7] Bennett-Woods, D. (2005). Ethics at a glance. Regis University.

[8] Berti-Equille, L. (2015). Data veracity estimation with ensembling truth discovery methods. In 2015 IEEE International Conference on Big Data (Big Data) (pp. 2628–2636). doi:10.1109/BigData.2015.7364062.

[9] Berti-Equille, L., & Borge-Holthoefer, J. (2015). Veracity of data: From truth discovery computation algorithms to models of misinformation dynamics. Synthesis Lectures on Data Management, 7, 1–155.

[10] Bhattacharjee, S. D., Talukder, A., & Balantrapu, B. V. (2017). Active learning based news veracity detection with feature weighting and deep-shallow fusion. In 2017 IEEE International Conference on Big Data (Big Data) (pp. 556–565). doi:10.1109/BigData.2017.8257971.

[11] Bodnar, T., Tucker, C., Hopkinson, K., & BilÃl’n, S. G. (2014). Increasing the veracity of event detection on social media networks through user trust modeling. In 2014 IEEE International Conference on Big Data (Big Data) (pp. 636–643). doi:10.1109/BigData.2014.7004286.

[12] Buntain, C., & Golbeck, J. (2017). Automatically identifying fake news in popular twitter threads. In 2017 IEEE International Conference on Smart Cloud (SmartCloud) (pp. 208–215). doi:10.1109/SmartCloud.2017.40.

[13] Castillo, C., Mendoza, M., & Poblete, B. (2013). Predicting information credibility in time-sensitive social media. Internet Research, 23, 560–588. doi:10.1108/IntR-05-2012-0095.

[14] Chang, C., Zhang, Y., Szabo, C., & Sheng, Q. Z. (2016). Extreme user and political rumor detection on twitter. In J. Li, X. Li, S. Wang, J. Li, & Q. Z. Sheng (Eds.), Advanced Data Mining and Applications (pp. 751–763). Cham: Springer International Publishing. doi:10.1007/978-3-319-49586-6\_54.

[15] Cheng, O. K., & Lau, R. Y. (2014). A multi-perspective methodology for detecting low-quality contents in social media. In 2014 International Conference on Advanced ICT (ICAICTE-2014). Citeseer.

[16] Chua, A. Y., & Banerjee, S. (2017). A study of tweet veracity to separate rumours from counter-rumours. In Proceedings of the 8th International Conference on Social Media & Society (p. 4). ACM.

[17] Ciampaglia, G. L., Shiralkar, P., Rocha, L. M., Bollen, J., Menczer, F., & Flammini, A. (2015). Computational Fact Checking from Knowledge Networks. PLOS ONE, 10, 1–13. doi:10.1371/journal.pone.0128193.

[18] Claverie-Berge, I. (2012). Solutions big data IBM. Presentation slides.

[19] Conroy, N. J., Rubin, V. L., & Chen, Y. (2015). Automatic deception detection: Methods for finding fake news. In Proceedings of the 78th ASIS&T Annual Meeting: Information Science with Impact: Research in and for the Community ASIST ’15 (pp. 82:1–82:4). Silver Springs, MD: American Society for Information Science. URL: http://dl.acm.org/citation.cfm?id=2857070.2857152.

[20] Dang, A., Smit, M., Mohammad, A., Minghim, R., & Milios, E. E. (2016). Toward understanding how users respond to rumours in social media. 2016 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining (ASONAM), (pp. 777–784). doi:10.1109/ASONAM.2016.7752326.

[21] De Marneffe, M.-C., MacCartney, B., Manning, C. D. et al. (2006). Generating typed dependency parses from phrase structure parses. In Lrec (pp. 449–454). volume 6.

[22] Debattista, J., Lange, C., Scerri, S., & Auer, S. (2015). Linked ’big’ data: Towards a manifold increase in big data value and veracity. 2015 IEEE/ACM 2nd International Symposium on Big Data Computing (BDC), (pp. 92–98). doi:10.1109/BDC.2015.34.

[23] Elias, D., Nadler, F., Cornwell, I., Grant-Muller, S., & Heinrich, T. (2016). UNIETD – assessment of third party data as information source for drivers and road operators. Transportation Research Procedia, 14, 2035–2043. doi:10.1016/j.trpro.2016.05.171.

[24] Fang, X. S., Sheng, Q. Z., Wang, X., & Ngu, A. H. (2017). Value veracity estimation for multi-truth objects via a graph-based approach. In Proceedings of the 26th International Conference on World Wide Web Companion WWW ’17 Companion (pp. 777–778). Republic and Canton of Geneva, Switzerland: International World Wide Web Conferences Steering Committee. doi:10.1145/3041021.3054212.

[25] Figueira, A., Sandim, M., & Fortuna, P. (2016). An approach to relevancy detection: Contributions to the automatic detection of relevance in social networks. In Á. Rocha, A. M. Correia, H. Adeli, L. P. Reis, & M. Mendonça Teixeira (Eds.), New Advances in Information Systems and Technologies (pp. 89–99). Cham: Springer International Publishing.

[26] Fontanarava, J., Pasi, G., & Viviani, M. (2017). An ensemble method for the credibility assessment of user-generated content. In Proceedings of the International Conference on Web Intelligence WI ’17 (pp. 863–868). New York, NY: ACM. doi:10.1145/3106426.3106464.

[27] Fontanarava, J., Pasi, G., & Viviani, M. (2017). Feature analysis for fake review detection through supervised classification. In 2017 IEEE International Conference on Data Science and Advanced Analytics (DSAA) (pp. 658– 666). doi:10.1109/DSAA.2017.51.

[28] Gambetta, D. et al. (2000). Can we trust trust. Trust: Making and breaking cooperative relations, 13, 213–237.

[29] García Lozano, M., Franke, U., Rosell, M., & Vlassov, V. (2015). Towards Automatic Veracity Assessment of Open Source Information. In 2015 IEEE International Congress on Big Data (pp. 199–206). doi:10.1109/BigDataCongress.2015.36.

[30] García Lozano, M., Schreiber, J., & Brynielsson, J. (2017). Tracking geographical locations using a geo-aware topic model for analyzing social media data. Decision Support Systems, 99, 18 – 29. doi:10.1016/j.dss.2017.05.006. Location Analytics and Decision Support.

[31] Garcia-Ulloa, D. A., Xiong, L., & Sunderam, V. (2017). Truth discovery for spatio-temporal events from crowdsourced data. Proc. VLDB Endow., 10, 1562–1573. doi:10.14778/3137628.3137662.

[32] Giasemidis, G., Singleton, C., Agrafiotis, I., Nurse, J. R. C., Pilgrim, A., Willis, C., & Greetham, D. V. (2016). Determining the veracity of rumours on twitter. In E. Spiro, & Y.-Y. Ahn (Eds.), Social Informatics (pp. 185–205). Cham: Springer International Publishing

[33] Ginsca, A. L., Popescu, A., Lupu, M. et al. (2015). Credibility in information retrieval. Foundations and Trends R in Information Retrieval, 9, 355–475.

[34] Guo, Q., Huang, W. W., Huang, K., & Liu, X. (2016). Information credibility: A probabilistic graphical model for identifying credible influenza posts on social media. In X. Zheng, D. D. Zeng, H. Chen, & S. J. Leischow (Eds.), Smart Health (pp. 131–142). Cham: Springer International Publishing. doi:10.1007/978-3-319-29175-8\_12.

[35] Gupta, A., Kumaraguru, P., Castillo, C., & Meier, P. (2014). Tweetcred: Real-time credibility assessment of content on twitter. In L. M. Aiello, & D. McFarland (Eds.), Social Informatics (pp. 228–243). Cham: Springer International Publishing.

[36] Hardalov, M., Koychev, I., & Nakov, P. (2016). In search of credible news. In C. Dichev, & G. Agre (Eds.), Artificial Intelligence: Methodology, Systems, and Applications (pp. 172–180). Cham: Springer International Publishing.

[37] Igawa, R. A., Jr, S. B., Paulo, K. C. S., Kido, G. S., Guido, R. C., Júnior, M. L. P., & da Silva, I. N. (2016). Account classification in online social networks with LBCA and wavelets. Information Sciences, 332, 72–83. doi:10.1016/j.ins.2015.10.039.

[38] Ionescu, B., Popescu, A., Lupu, M., Gînsca, A. L., Boteanu, B., & Müller, H. (2015). Div150cred: A social image ˘ retrieval result diversification with user tagging credibility dataset. In Proceedings of the 6th ACM Multimedia Systems Conference MMSys ’15 (pp. 207–212). New York, NY: ACM. doi:10.1145/2713168.2713192.

[39] Ito, J., Song, J., Toda, H., Koike, Y., & Oyama, S. (2015). Assessment of tweet credibility with lda features. In Proceedings of the 24th International Conference on World Wide Web (pp. 953–958). ACM.

[40] Jaho, E., Tzoannos, E., Papadopoulos, A., & Sarris, N. (2014). Alethiometer: A framework for assessing trustworthiness and content validity in social media. In Proceedings of the 23rd International Conference on World Wide Web WWW ’14 Companion (pp. 749–752). New York, NY: ACM. doi:10.1145/2567948.2579324.

[41] Jain, P., & Singh, V. (2016). Credrank: Evaluating tweet credibility during high impact events. In 2016 2nd International Conference on Contemporary Computing and Informatics (IC3I) (pp. 553–557). doi:10.1109/IC3I.2016.7918025.

[42] Jain, S., Sharma, V., & Kaushal, R. (2016). Towards automated real-time detection of misinformation on twitter. In 2016 International Conference on Advances in Computing, Communications and Informatics (ICACCI) (pp. 2015– 2020). doi:10.1109/ICACCI.2016.7732347.

[43] Jamil, N. B. C. E. ., Ishak, I. B., Sidi, F., Affendey, L. S., & Mamat, A. (2015). A systematic review on the profiling of digital news portal for big data veracity. Procedia Computer Science, 72, 390 – 397. doi:10.1016/j.procs.2015.12.154. The Third Information Systems International Conference 2015.

[44] Janssen, B., Habib, M., & van Keulen, M. (2017). Truth assessment of objective facts extracted from tweets: A case study on world cup 2014 game facts. In Proceedings of the 13th International Conference on Web Information Systems and Technologies (pp. 187–195). volume 1. doi:10.5220/0006185101870195.

[45] Jeong, S., Noh, G., Oh, H., & Kim, C.-k. (2016). Follow spam detection based on cascaded social information. Inf. Sci., 369, 481–499. doi:10.1016/j.ins.2016.07.033.

[46] Jin, Z., Cao, J., Guo, H., Zhang, Y., & Luo, J. (). Multimodal Fusion with Recurrent Neural Networks for Rumor Detection on Microblogs. In Proceedings of the 2017 ACM on Multimedia Conference MM ’17 (pp. 795–816). ACM. doi:10.1145/3123266.3123454.

[47] Jin, Z., Cao, J., Jiang, Y. G., & Zhang, Y. (2014). News credibility evaluation on microblog with a hierarchical propagation model. In 2014 IEEE International Conference on Data Mining (pp. 230–239).

doi:10.1109/ICDM.2014.91.

[48] Jin, Z., Cao, J., Zhang, Y., & Luo, J. (2016). News Verification by Exploiting Conflicting Social Viewpoints in Microblogs. In AAAI (pp. 2972–2978).

[49] Jin, Z., Cao, J., Zhang, Y., Zhou, J., & Tian, Q. (2017). Novel visual and statistical image features for microblogs news verification. IEEE Transactions on Multimedia, 19, 598–608. doi:10.1109/TMM.2016.2617078.

[50] Kakol, M., Nielek, R., & Wierzbicki, A. (2017). Understanding and predicting web content credibility using the content credibility corpus. Inf. Process. Manage., 53, 1043–1061.

[51] Kim, Y. A., & Ahmad, M. A. (2013). Trust, distrust and lack of confidence of users in online social media-sharing communities. Know.-Based Syst., 37, 438–450. doi:10.1016/j.knosys.2012.09.002.

[52] Kitchenham, B. A., & Charters, S. M. (2007). Guidelines for Performing Systematic Literature Reviews in Software Engineering, Version 2.3. Technical Report EBSE-2007-01 Keele University and Durham University United Kingdom.

[53] Kong, L., Schneider, N., Swayamdipta, S., Bhatia, A., Dyer, C., & Smith, N. A. (2014). A dependency parser for tweets. In Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP) (pp. 1001–1012).

[54] Kumar, K. P. K., & Geethakumari, G. (2014). Detecting misinformation in online social networks using cognitive psychology. Human-centric Computing and Information Sciences, 4, 14. doi:10.1186/s13673-014-0014-x.

[55] Kumar, K. P. K., Srivastava, A., & Geethakumari, G. (2016). A psychometric analysis of information propagation in online social networks using latent trait theory. Computing, 98, 583–607. doi:10.1007/s00607-015-0472-7.

[56] Kumar, S., West, R., & Leskovec, J. (2016). Disinformation on the web: Impact, characteristics, and detection of wikipedia hoaxes. In Proceedings of the 25th International Conference on World Wide Web WWW ’16 (pp. 591–602). Republic and Canton of Geneva, Switzerland: International World Wide Web Conferences Steering Committee. doi:10.1145/2872427.2883085.

[57] Laney, D. (2001). 3d data management: Controlling data volume, velocity and variety. META group research note, 6, 1.

[58] Lendvai, P., Reichel, U. D., & Declerck, T. (2016). Factuality drift assessment by lexical markers in resolved rumors. In Proceedings of the 1st International Workshop on Semantic Change & Evolving Semantics.

[59] Levchuk, G., & Blasch, E. (2015). Probabilistic graphical models for multi-source fusion from text sources. In 2015 IEEE Symposium on Computational Intelligence for Security and Defense Applications (CISDA) (pp. 1–10). doi:10.1109/CISDA.2015.7208640.

[60] Levchuk, G., & Shabarekh, C. (2017). Using soft-hard fusion for misinformation detection and pattern of life analysis in OSINT. In T. P. Hanratty, & J. Llinas (Eds.), Proceedings of SPIE Vol. 10207, Next-Generation Analyst V. Bellingham, WA: SPIE. doi:10.1117/12.2263546.

[61] Li, R., & Suh, A. (2015). Factors influencing information credibility on social media platforms: Evidence from facebook pages. Procedia Computer Science, 72, 314–328. doi:10.1016/j.procs.2015.12.146.

[62] Lim, W. Y., Lee, M. L., & Hsu, W. (2017). iFACT: An interactive framework to assess claims from tweets. In Proceedings of the 2017 ACM on Conference on Information and Knowledge Management CIKM ’17 (pp. 787– 796). New York, NY: ACM. doi:10.1145/3132847.3132995.

[63] Lioma, C., Simonsen, J. G., & Larsen, B. (2017). Evaluation measures for relevance and credibility in ranked lists.

In Proceedings of the ACM SIGIR International Conference on Theory of Information Retrieval ICTIR ’17 (pp. 91–98). New York, NY: ACM. doi:10.1145/3121050.3121072.

[64] Litou, I., Kalogeraki, V., Katakis, I., & Gunopulos, D. (2017). Efficient and timely misinformation blocking under varying cost constraints. Online Social Networks and Media, 2, 19 – 31. doi:10.1016/j.osnem.2017.07.001.

[65] Liu, X., Li, Q., Nourbakhsh, A., Fang, R., Thomas, M., Anderson, K., Kociuba, R., Vedder, M., Pomerville, S., Wudali, R., Martin, R., Duprey, J., Vachher, A., Keenan, W., & Shah, S. (2016). Reuters tracer: A large scale system of detecting and verifying real-time news events from twitter. In Proceedings of the 25th ACM International on Conference on Information and Knowledge Management CIKM ’16 (pp. 207–216). New York, NY: ACM. doi:10.1145/2983323.2983363.

[66] Liu, X., Nourbakhsh, A., Li, Q., Shah, S., Martin, R., & Duprey, J. (2017). Reuters tracer: Toward automated news production using large scale social media data. In 2017 IEEE International Conference on Big Data (Big Data) (pp. 1483–1493). doi:10.1109/BigData.2017.8258082.

[67] Loper, E., & Bird, S. (2002). Nltk: the natural language toolkit. arXiv preprint cs/0205028, .

[68] Lukoianova, T., & Rubin, V. L. (2013). Veracity roadmap: Is big data objective, truthful and credible? Advances In Classification Research Online, 24, 1.

[69] Manning, C., Surdeanu, M., Bauer, J., Finkel, J., Bethard, S., & McClosky, D. (2014). The stanford corenlp natural language processing toolkit. In Proceedings of 52nd annual meeting of the association for computational linguistics: system demonstrations (pp. 55–60).

[70] Marsh, S. P. (1994). Formalising trust as a computational concept. Ph.D. thesis University of Stirling Stirling, United Kingdom.

[71] Middleton, S. E., & Krivcovs, V. (2016). Geoparsing and geosemantics for social media: spatio-temporal grounding of content propagating rumours to support trust and veracity analysis during breaking news. ACM Transactions on Information Systems, 34, 1–27. URL: https://eprints.soton.ac.uk/390820/.

[72] Mikolov, T., Sutskever, I., Chen, K., Corrado, G. S., & Dean, J. (2013). Distributed representations of words and phrases and their compositionality. In Advances in neural information processing systems (pp. 3111–3119).

[73] Mitra, T., & Gilbert, E. (2015). CREDBANK: A large-scale social media corpus with associated credibility annotations. In Proceedings of the Ninth International Conference on Web and Social Media, ICWSM 2015, University of Oxford, Oxford, UK, May 26-29, 2015 (pp. 258–267). URL: http://www.aaai.org/ocs/index.php/ICWSM/ICWSM15/paper/view/10582.

[74] Mitra, T., Wright, G. P., & Gilbert, E. (2017). A parsimonious language model of social media credibility across disparate events. In Proceedings of the 2017 ACM Conference on Computer Supported Cooperative Work and Social Computing (pp. 126–145). New York, NY: ACM. doi:10.1145/2998181.2998351.

[75] Mukherjee, S., Weikum, G., & Danescu-Niculescu-Mizil, C. (2014). People on Drugs: Credibility of User Statements in Health Communities. In Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining KDD ’14 (pp. 65–74). New York, New York: ACM. doi:10.1145/2623330.2623714.

[76] Namihira, Y., Segawa, N., Ikegami, Y., Kawai, K., Kawabe, T., & Tsuruta, S. (2013). High precision credibilit analysis of information on twitter. In 2013 International Conference on Signal-Image Technology Internet-Based

Systems (pp. 909–915). doi:10.1109/SITIS.2013.148.

[77] O’Leary, D. E. (2011). Blog mining-review and extensions:âAIJfrom each according to his opinionâ <sup>˘</sup> A<sup>˘ ˙</sup>I. Decision Support Systems, 51, 821–830.

[78] Paryani, J., T.K., A. K., & George, K. M. (2017). Entropy-based model for estimating veracity of topics from tweets. In N. T. Nguyen, G. A. Papadopoulos, P. J˛edrzejowicz, B. Trawinski, & G. Vossen ´ (Eds.), Computational Collective Intelligence (pp. 417–427). Cham: Springer International Publishing. doi:10.1007/978-3-319-67077-5\_40.

[79] Pasternack, J., & Roth, D. (2013). Latent Credibility Analysis. In Proceedings of the 22Nd International Conference on World Wide Web WWW ’13 (pp. 1009–1020). Rio de Janeiro, Brazil: ACM. doi:10.1145/2488388.2488476.

[80] Pennebaker, J. W., Francis, M. E., & Booth, R. J. (2001). Linguistic inquiry and word count: Liwc 2001. Mahway: Lawrence Erlbaum Associates, 71, 2001.

[81] Pennington, J., Socher, R., & Manning, C. (2014). Glove: Global vectors for word representation. In Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP) (pp. 1532–1543).

[82] Popat, K., Mukherjee, S., Strötgen, J., & Weikum, G. (2016). Credibility assessment of textual claims on the web. In Proceedings of the 25th ACM International on Conference on Information and Knowledge Management CIKM ’16 (pp. 2173–2178). New York, NY: ACM. doi:10.1145/2983323.2983661.

[83] Ramachandramurthy, S., Subramaniam, S., & Ramasamy, C. (2015). Distilling big data: refining quality information in the era of yottabytes. The Scientific World Journal, 2015.

[84] Rao, P., Katib, A., Kamhoua, C., Kwiat, K., & Njilla, L. (). Probabilistic Inference on Twitter Data to Discover Suspicious Users and Malicious Content. In 2016 IEEE International Conference on Computer and Information Technology (CIT) (pp. 407–414). doi:10.1109/CIT.2016.29.

[85] Rath, B., Gao, W., Ma, J., & Srivastava, J. (2017). From retweet to believability: Utilizing trust to identify rumor spreaders on twitter. In Proceedings of the 2017 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining 2017 ASONAM ’17 (pp. 179–186). New York, NY: ACM. doi:10.1145/3110025.3110121.

[86] Reuter, C., Kaufhold, M.-A., & Steinfort, R. (2017). Rumors, fake news and social bots in conflicts and emergencies: Towards a model for believability in social media. In Proceedings of the 14th ISCRAM Conference – Albi, France.

[87] Robin, L., Mark, B., Philip, C., & Martin, C. (2016). From big noise to big data: Toward the verification of large data sets for understanding regional retail flows. Geographical Analysis, 48, 59–81. doi:10.1111/gean.12081.

[88] Ros, S. P., Canelles, A. P., Pérez, M. G., Mármol, F. G., & Pérez, G. M. (2015). Chasing Offensive Conduct in Social Networks: A Reputation-Based Practical Approach for Frisber. ACM Transactions on Internet Technology, 15, 1–20. doi:10.1145/2797139.

[89] Saez-Trumper, D. (2014). Fake tweet buster: A webtool to identify users promoting fake news ontwitter. In Proceedings of the 25th ACM Conference on Hypertext and Social Media HT ’14 (pp. 316–317). New York, NY: ACM. doi:10.1145/2631775.2631786.

[90] Sampson, J., Morstatter, F., Wu, L., & Liu, H. (2016). Leveraging the implicit structure within social media for emergent rumor detection. In Proceedings of the 25th ACM International on Conference on Information and Knowledge Management CIKM ’16 (pp. 2377–2382). New York, NY: ACM. doi:10.1145/2983323.2983697.

[91] Schroeck, M., Shockley, R., Smart, J., Romero-Morales, D., & Tufano, P. (2012). Analytics: The real-world use of big data. IBM Global Business Services, 12, 1–20. URL: https://public.dhe.ibm.com/common/ssi/ecm/gb/en/gbe03519usen/global-business-services-globa

[92] Shao, C., Ciampaglia, G. L., Flammini, A., & Menczer, F. (2016). Hoaxy: A platform for tracking online misinformation. In Proceedings of the 25th International Conference Companion on World Wide Web WWW ’16 Companion (pp. 745–750). Republic and Canton of Geneva, Switzerland: International World Wide Web Conferences Steering Committee. doi:10.1145/2872518.2890098.

[93] Shi, B., & Weninger, T. (2016). Discriminative predicate path mining for fact checking in knowledge graphs. Knowledge-Based Systems, 104, 123 – 133. doi:10.1016/j.knosys.2016.04.015.

[94] Shiralkar, P., Flammini, A., Menczer, F., & Ciampaglia, G. L. (2017). Finding streams in knowledge graphs to support fact checking. In 2017 IEEE International Conference on Data Mining (ICDM) (pp. 859–864). doi:10.1109/ICDM.2017.105.

[95] Sirivianos, M., Kim, K., Gan, J. W., & Yang, X. (2014). Leveraging social feedback to verify online identity claims. ACM Trans. Web, 8, 9:1–9:38. doi:10.1145/2543711.

[96] Snow, D. (2012). Adding a 4th V to BIG data - veracity. URL: http://dsnowondb2.blogspot.se/2012/07/adding-4th-v-to-big-data-veracity.html.

[97] Tolo¸si, L., Tagarev, A., & Georgiev, G. (2016). An analysis of event-agnostic features for rumour classification in Twitter. In Proceedings of the Tenth International AAAI Conference on Web and Social Media (pp. 151–158). URL: https://www.aaai.org/ocs/index.php/ICWSM/ICWSM16/paper/view/13197/12859.

[98] Torky, M., Baberse, R., Ibrahim, R., Hassanien, A. E., Schaefer, G., Korovin, I., & Zhu, S. Y. (2016). Credibility investigation of newsworthy tweets using a visualising petri net model. In 2016 IEEE International Conference on Systems, Man, and Cybernetics (SMC) (pp. 003894–003898). doi:10.1109/SMC.2016.7844842.

[99] Vartapetiance, A., & Gillam, L. (2014). Deception detection: dependable or defective? Social Network Analysis and Mining, 4, 166. doi:10.1007/s13278-014-0166-8.

[100] Viviani, M., & Pasi, G. (2017). Credibility in social media: opinions, news, and health information – a survey. Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 7.

[101] Viviani, M., & Pasi, G. (2017). A multi-criteria decision making approach for the assessment of information credibility in social media. In A. Petrosino, V. Loia, & W. Pedrycz (Eds.), Fuzzy Logic and Soft Computing Applications (pp. 197–207). Cham: Springer International Publishing.

[102] Viviani, M., & Pasi, G. (2017). Quantifier guided aggregation for the veracity assessment of online reviews. International Journal of Intelligent Systems, 32, 481–501.

[103] Vosoughi, S., Mohsenvand, M. N., & Roy, D. (2017). Rumor gauge: Predicting the veracity of rumors on twitter. ACM Trans. Knowl. Discov. Data, 11, 50:1–50:36. doi:10.1145/3070644.

[104] Wang, R. Y., & Strong, D. M. (1996). Beyond accuracy: What data quality means to data consumers. Journal of management information systems, 12, 5–33.

[105] Wang, X., Luo, X., & Liu, H. (2015). Measuring the veracity of web event via uncertainty. Journal of Systems and Software, 102, 226 – 236. doi:10.1016/j.jss.2014.07.023.

[106] Wang, X., Sheng, Q. Z., Fang, X. S., Li, X., Xu, X., & Yao, L. (2015). Approximate truth discovery via problem scale reduction. In Proceedings of the 24th ACM International on Conference on Information and Knowledge

Management (pp. 503–512). ACM.

[107] Webb, H., Burnap, P., Procter, R., Rana, O., Stahl, B. C., Williams, M., Housley, W., Edwards, A., & Jirotka, M. (2016). Digital wildfires: Propagation, verification, regulation, and responsible innovation. ACM Trans. Inf. Syst., 34, 15:1–15:23. doi:10.1145/2893478.

[108] Website (Visited 2018). Apache flume. URL: https://flume.apache.org/.

[109] Website (Visited 2018). Apache hadoop. URL: https://hadoop.apache.org/.

[110] Website (Visited 2018). Apache hive. URL: https://hive.apache.org/.

[111] Website (Visited 2018). Apache spark. URL: https://spark.apache.org/.

[112] Website (Visited 2018). Networkx. URL: https://networkx.github.io/.

[113] Website (Visited 2018). Neurolab. URL: https://pythonhosted.org/neurolab/.

[114] Website (Visited 2018). scikit-learn. URL: https://scikit-learn.org/stable/index.html.

[115] Wiegand, S., & Middleton, S. E. (2016). Veracity and velocity of social media content during breaking news: Analysis of november 2015 paris shootings. In Proceedings of the 25th International Conference Companion on World Wide Web WWW ’16 Companion (pp. 751–756). Republic and Canton of Geneva, Switzerland: International World Wide Web Conferences Steering Committee. doi:10.1145/2872518.2890095.

[116] Xie, B., Wang, Y., Chen, C., & Xiang, Y. (2016). Gatekeeping Behavior Analysis for Information Credibility Assessment on Weibo. In J. Chen, V. Piuri, C. Su, & M. Yung (Eds.), Network and System Security (pp. 483–496). Cham: Springer International Publishing.

[117] Yan, S.-R., Zheng, X.-L., Wang, Y., Song, W. W., & Zhang, W.-Y. (2015). A graph-based comprehensive reputation model: Exploiting the social context of opinions to enhance trust in social commerce. Information Sciences, 318, 51–72. doi:10.1016/j.ins.2014.09.036.

[118] Yang, Y., Niu, K., & He, Z. (2015). Exploiting the topology property of social network for rumor detection. In 2015 12th International Joint Conference on Computer Science and Software Engineering (JCSSE) (pp. 41–46). doi:10.1109/JCSSE.2015.7219767.

[119] Yao, S., Amin, M. T., Su, L., Hu, S., Li, S., Wang, S., Zhao, Y., Abdelzaher, T., Kaplan, L., Aggarwal, C., & Yener, A. (2016). Recursive ground truth estimator for social data streams. In 2016 15th ACM/IEEE International Conference on Information Processing in Sensor Networks (IPSN) (pp. 1–12). doi:10.1109/IPSN.2016.7460719.

[120] Yao, S., Hu, S., Li, S., Zhao, Y., Su, L., Kaplan, L., Yener, A., & Abdelzaher, T. (2016). On source dependency models for reliable social sensing: Algorithms and fundamental error bounds. In 2016 IEEE 36th International Conference on Distributed Computing Systems (ICDCS) (pp. 467–476). doi:10.1109/ICDCS.2016.75.

[121] Zhang, D. Y., Han, R., Wang, D., & Huang, C. (2016). On robust truth discovery in sparse social media sensing. In 2016 IEEE International Conference on Big Data (Big Data) (pp. 1076–1081). doi:10.1109/BigData.2016.7840710.

[122] Zhao, B., & Sui, D. Z. (2017). True lies in geospatial big data: detecting location spoofing in social media. Annals of GIS, 23, 1–14. doi:10.1080/19475683.2017.1280536.

[123] Zhao, L., Hua, T., Lu, C.-T., & Chen, R. (2016). A topic-focused trust model for twitter. Computer Communications, 76, 1–11.

[124] Zhao, Z., Resnick, P., & Mei, Q. (2015). Enquiring minds: Early detection of rumors in social media from enquiry posts. In Proceedings of the 24th International Conference on World Wide Web (pp. 1395–1405). International

World Wide Web Conferences Steering Committee.

[125] Zhi, S., Sun, Y., Liu, J., Zhang, C., & Han, J. (2017). Claimverif: A real-time claim verification system using the web and fact databases. In Proceedings of the 2017 ACM on Conference on Information and Knowledge Management CIKM ’17 (pp. 2555–2558). New York, NY: ACM. doi:10.1145/3132847.3133182.

[126] Zili, Z., Ziqiong, Z., & Hengyun, L. (2015). Predictors of the authenticity of internet health rumours. Health Information & Libraries Journal, 32, 195–205. doi:10.1111/hir.12115.

[127] Zubiaga, A., Liakata, M., Procter, R., Wong Sak Hoi, G., & Tolmie, P. (2016). Analysing how people orient to and spread rumours in social media by looking at conversational threads. PLoS ONE, 11, e0150989. doi:10.1371/journal.pone.0150989.

## Appendix A. Review protocol

This section contains the review protocol used by the authors to analyze the selected papers.

1. General information

(a) Internal ID

(b) Title

(c) Authors

(d) Abstract

(e) Publication year (actual publication date, i.e., not the “online first” date)

(f) Author background (affiliated to company, university, government institution, a mixture)

(g) Countries (i.e., author affiliation countries)

(h) BibTeX reference (including the fields “doi” and/or “url”)

## 2. Research questions

(a) Approaches

i. What aspect of VA does the approach target, i.e., do the authors try to assess trustworthiness, credibility, formal correctness, explicit lies, bot vs. human, etc.?

ii. Do the authors try to extract/mine an indicator related to VA or do they try to determine VA directly?

iii. Which indicator(s) do the authors target (e.g., stance, geographical location, social network)?

iv. Do the authors motivate the choice of indicator? If so, how?

v. How is the VA or indicator quantified (a scale, a confidence interval, a binary response, a heatmap color, etc.)?

vi. What is evaluated, e.g., the assessment itself, the method, the data, etc.?

## (b) Methods

i. Are there one or more distinct research questions? If yes, what is it/what are they?

ii. Method: describe the procedural VA steps taken in chronological order

iii. Is the VA method fully automated or semi-automatic (requiring manual intervention)? If semi-automatic, what intervention(s) are required?

iv. Is the method (apparently) applicable for different data sources?

## (c) Algorithms

i. Which algorithms do they employ (mention only the algorithms directly involved in the VA or related task)?

ii. Is the algorithm(s) based on an ML method? If so, what type (supervised, unsupervised, reinforcement, etc.)?

iii. Do the algorithms handle online or offline data (streams)?

iv. What quality assessment measure(s) is used (precision, accuracy, entropy, etc.)?

## (d) Tools

i. Which tools do the authors employ?

ii. Have the tools been developed by the authors themselves or have they used proprietary software, open source, etc.?

iii. Has their code/tool been made publicly available (if yes, how)?

## (e) Data

i. Which data types (tweet, picture, sound, article, long/short text, etc.)?

ii. Which data sources (Twitter, Facebook, Wikipedia, RSS, blog posts, etc.)?

iii. Which data sets are used (gathered by themselves, a known data set, synthetic, authentic)?

iv. If gathered (produced) by the researchers, has the data been made available? If so, where?

v. If the data was collected or produced by the researchers, how was it done?

vi. Is the data usable for benchmarking?

vii. What were the data selection criteria (keywords, time frame, accounts, etc.)?

viii. Which parts of the data do they use in the VA, e.g., do they use content, meta data, network data, feature types, etc.?

ix. Are there any particular assumptions made regarding the data or its distribution (if yes, which)?

(f) Miscellaneous

i. Does the paper give a definition of veracity and/or veracity assessment? If so, what is the definition? (copy/paste from the paper)

ii. Does the paper discuss ethical issues related to automatic veracity assessment? If yes, which?

iii. Does the paper discuss legal aspects related to automatic veracity assessment? If yes, which?

iv. Relevance to main research question (high, medium, low)?

v. Summary of statements (contributions) made in the article

vi. Type of paper (primary, secondary, tertiary, other)

vii. Perspective/interest group

## 3. The paper (qualitative assessment)

(a) Strengths of the paper

(b) Weaknessess of the paper

(c) Subjective assessment/reflection (state of the art or not, worth reading or not, etc.)

## Author biography

Marianela García Lozano is a senior scientist at the Swedish Defence Research Agency (FOI) since 2001. Her research interests include information and knowledge modeling, veracity assessment, software development in distributed systems, web mining, machine learning, and natural language processing. Marianela received her M.Sc. degree in Computer Science and Engineering in 2003 and her Licentiate degree in Electronic and Computer Systems in 2010 from the Royal Institute of Technology (KTH). Marianela’s Licentiate thesis is on the topic of distributed systems.

## Highlights

Three main veracity assessment research directions found, i.e., utilizing implicit features, employing explicit fact checking, and the appeal to authority method.

<sub>•</sub> The studied papers in general tend to be narrow as they focus on solving a small task with only one type of data from one main source.

The most common approach to veracity assessment is to perform text analysis using supervised learning.

Important identified research gaps include reproducibility challenges, low use of recent advancements made in machine learning, and a lack of efforts targeting online data streams.

<sub>•</sub> The veracity assessment domain is still relatively immature.

## veracity

\- the quality of being true, honest, or accurate

https://dictionary.cambridge.org

\- i) conformity with truth or fact; accuracy, ii) devotion to the truth; truthfulness, iii) power of conveying or perceiving truth, iv) something true.

https://www.merriam-webster.com

\- i) habitual observance of truth in speech or statement; truthfulness, ii) conformity to truth or fact; accuracy, iii) correctness or accuracy, as of the senses or of a scientific instrument.

https://www.dictionary.com

\- unwillingness to tell lies

https://www.vocabulary.com

![](/api/attachments/5H5EH52Z/fulltext/images/c4776de6c9c9b55729a6a4c0d76ca3e7fd29605049c120216d1e7acdb7609508.jpg)

![](/api/attachments/5H5EH52Z/fulltext/images/d3c0645221ed1227c79e5c8e98e9cbe20942b7291e44893e69a84b7216aff3fc.jpg)

(a) Publication year.  
![](/api/attachments/5H5EH52Z/fulltext/images/1a7412d1102abf10d9c800c5f99cf8ebfa64d68063805fbac636186208a6eac6.jpg)  
(c) Countries.

![](/api/attachments/5H5EH52Z/fulltext/images/42e870054688ac8cd46e92db174b34ec3b0e9c5c2fdbcb1c0cb76264e064186e.jpg)

(b) Affiliation.  
![](/api/attachments/5H5EH52Z/fulltext/images/c1594fe1707673fec04522f55cedc8da90ba5a3425347094fc94cef4060865c8.jpg)  
(d) Geographical region.

![](/api/attachments/5H5EH52Z/fulltext/images/14d758bd09ee47b50e1ba41ebd9782e78bd7956cb099a5664c7afbc17123623b.jpg)  
(a) Machine learning (ML).

![](/api/attachments/5H5EH52Z/fulltext/images/b002444aef2c37a1aff8c3435929c2f13befe7acc9cea7c04dcb9892506f607a.jpg)  
(b) Online or offline algorithm?  
Figure 4

![](/api/attachments/5H5EH52Z/fulltext/images/cd676e7032e1fecc83d8c576c9a91d5a7f46bdf97e9bca4ff5237d032c457f3a.jpg)  
Figure 5

![](/api/attachments/5H5EH52Z/fulltext/images/72e44808f9b33f7c9ec2128cf518a2ff0b8c842c96b4611656af3dcd3b5e76c9.jpg)  
(a) Types of data.

![](/api/attachments/5H5EH52Z/fulltext/images/090019f4ed8118468c304bc709eba5fd038c902370182557f90d8825809b6f47.jpg)  
(b) Data sources used in two or more papers.

![](/api/attachments/5H5EH52Z/fulltext/images/21bf2991226b40057aeb1fb0cf2f14873b1d2f05d4634d14683962d49f9746ea.jpg)  
Figure 7
