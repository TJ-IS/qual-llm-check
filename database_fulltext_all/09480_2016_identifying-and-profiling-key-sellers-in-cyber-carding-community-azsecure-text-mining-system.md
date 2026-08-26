---
otero_id: 9480
otero_key: "97S7NYM7"
title: "Identifying and Profiling Key Sellers in Cyber Carding Community: AZSecure Text Mining System"
authors: "Weifeng Li; Hsinchun Chen; Jay F. Nunamaker"
year: "2016"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2016.1267528"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Identifying and Profiling Key Sellers in Cyber Carding Community: AZSecure Text Mining System

Weifeng Li, Hsinchun Chen & Jay F. Nunamaker Jr.

To cite this article: Weifeng Li, Hsinchun Chen & Jay F. Nunamaker Jr. (2016) Identifying and Profiling Key Sellers in Cyber Carding Community: AZSecure Text Mining System, Journal of Management Information Systems, 33:4, 1059-1086, DOI: 10.1080/07421222.2016.1267528

To link to this article: http://dx.doi.org/10.1080/07421222.2016.1267528

![](/api/attachments/97S7NYM7/fulltext/images/35deaba24cd34df33b455de6bc2552674055e3c80206b1e243fc5f927202142a.jpg)

Published online: 10 Feb 2017.

![](/api/attachments/97S7NYM7/fulltext/images/55c74a376d770b86afb4df74c90a08efe7facf37dcf1f3c9c6c4047138bd7ad1.jpg)

Submit your article to this journal

![](/api/attachments/97S7NYM7/fulltext/images/55fb9a18430ebc3d156c1c4a4df728cc491eaddb356937ff2050eb4159e86838.jpg)

Article views: 25

![](/api/attachments/97S7NYM7/fulltext/images/f2c9e853e8c9fc6df23f25b30a5d526d7cc2269e1a759009129451e860c15d7a.jpg)

View related articles

![](/api/attachments/97S7NYM7/fulltext/images/207d50283912b233f63074de56a99aa47686480ee1ef5e56033cd60b14c82b83.jpg)

View Crossmark data

# Identifying and Profiling Key Sellers in Cyber Carding Community: AZSecure Text Mining System

WEIFENG LI, HSINCHUN CHEN, AND JAY F. NUNAMAKER JR.

WEIFENG LI (weifengli@email.arizona.edu; corresponding author) is a doctoral student in the Department of Management Information Systems and a research associate in the Artificial Intelligence Lab at the University of Arizona. His research interests include social media analytics, natural language processing, machine learning, and security informatics. His work has appeared in various conferences and workshops, including International Conference on Information Systems, Workshop on Information Technology and Systems, and the IEEE Conference on Intelligence and Security Informatics.

HSINCHUN CHEN (hchen@eller.arizona.edu) is University of Arizona Regents Professor and Thomas R. Brown Chair in Management and Technology in the Management Information Systems Department at the Eller College of Management. He joined the National Science Foundation (NSF) as program director of the Smart and Connected Health Program in September 2014. He received his Ph.D. in information systems from New York University. He is director of the Artificial Intelligence Lab where he developed the COPLINK system, which has been cited as a national model for public safety information sharing and analysis, and has been adopted in more than 3,500 law enforcement and intelligence agencies. He is the author or editor of 20 books, 25 book chapters, 280 journal papers, and 150 refereed conference articles covering digital library, data/ text/web mining, business analytics, security informatics, and health informatics. He is editor in chief of Security Informatics. He has received over 90 grants totaling more than \$40 million in research funding from the NSF, National Institutes of Health, National Library of Medicine, Department of Defense, Department of Justice, Central Intelligence Agency, Department of Homeland Security, and other agencies.

JAY F. NUNAMAKER JR. (jnunamaker@cmi.arizona.edu) is Regents and Soldwedel Professor of MIS, Computer Science and Communication and director of the Center for the Management of Information and the National Center for Border Security and Immigration at the University of Arizona. He received his Ph.D. in operations research and systems engineering from Case Institute of Technology. He has held a professional engineer’s license since 1965. He was inducted into the Design Science Hall of Fame and received the LEO Award for Lifetime Achievement from the Association for Information Systems. He was featured in the July 1997 issue of Forbes Magazine on technology as one of eight key innovators in information technology. He specializes in the fields of system analysis and design, collaboration technology, and deception detection. The commercial product GroupSystems ThinkTank, based on his research, is often referred to as the gold standard for structured collaboration systems. He founded the MIS Department at the University of Arizona in 1974 and served as department head for 18 years.

ABSTRACT: The past few years have witnessed millions of credit/debit cards flowing through the underground economy and ultimately causing significant financial loss. Examining key underground economy sellers has both practical and academic significance for cybercrime forensics and criminology research. Drawing on social media analytics, we have developed the AZSecure text mining system for identifying and profiling key sellers. The system identifies sellers using sentiment analysis of customer reviews and profiles sellers using topic modeling of advertisements. We evaluated the AZSecure system on eight international underground economy forums. The system significantly outperformed all benchmark machine-learning methods on identifying advertisement threads, classifying customer review sentiments, and profiling seller characteristics, with an average F-measure of about 80 percent to 90 percent. In our case study, we identified the famous carder, Rescator, who was affiliated with the Target breach, and captured important seller characteristics in terms of product type, payment options, and contact channels. Our research leverages social media analytics to probe into the underground economy in order to help law enforcement target key sellers and prevent future fraud. It also contributes to our understanding of the use of information technology in detecting deception in online systems.

KEY WORDS AND PHRASES: carding community, cybersecurity, deep learning, fraud detection, online deception, social media analytics, topic modeling, underground economy.

Carding is the deceptive process of stealing, reselling, and ultimately using large volumes of payment information to commit fraud [40]. Carding has increasingly caused significant economic and societal loss. The number of confirmed carding incidents went from 14 in 2004 to 1,367 in 2013 [50]. Hundreds of millions of carding victims have been exposed to potential financial fraud. For instance, over 40 million credit/debit cards were leaked from Target in 2013; one-third of American households were affected by the leak of 83 million accounts at JPMorgan Chase in August 2014; and 56 million payment card records were stolen from Home Depot in 2014. In 2015, Carbanak, a carding advanced persistent threat (APT), is reported to have caused over 100 banks to suffer losses up to \$1 billion [26]. Although carding involves a sequence of sophisticated deceptive processes, the international online underground economy has commoditized carding activities by providing a platform for exchanging cardingrelated products and services worldwide [23]. Specifically, the underground economy, which is often housed on carding forums, allows carders to easily advertise or acquire attacking malwares and stolen cards [19, 21]. Consequently, the underground economy has put card owners at greater risk of financial fraud.

Lately, the identification and profiling of key underground economy sellers has gained increasing traction in both academia and law enforcement [41]. Peretti [40] argued that “prosecuting and punishing” key sellers is a key solution to data breaches [p. 407]. Holt [21] called for law enforcement to “target” key sellers that are “reputable and trustworthy” and “gather information in order to develop cases” [p. 175]. The recent arrest and conviction of several key sellers has rescued millions of cards from further dissemination and prevented myriad cases of potential financial fraud [48, 49]. However, the identification of key sellers in the underground economy has been challenging, considering a number of deceptive sellers who do not provide buyers with promised products and services [20]. While many English linguistic cues have been found to detect deception [18], the multilingual nature of the international underground economy poses great challenges to the application of these techniques. As underground economy forums allow buyers to comment on their purchase experience, we are motivated to make use of the customer reviews to tell deceptive sellers apart. Furthermore, little has been done to profile key sellers in terms of their specialties, which inspires us to capture sellers’ characteristics from their advertisements.

Using a design science approach [37], we propose a text mining-based system for identifying and profiling the key sellers from the carding forums. Our system is capable of effectively ranking sellers based on their quality and extracting sellers’ characteristics. The proposed system uses two types of textual traces in carding forums—advertisements and customer reviews. While advertisements reflect major seller characteristics, including product or service descriptions, payment options, and contact, customer reviews reveal seller quality. The system leverages (1) deep learning-based sentiment analysis to evaluate seller quality based on customer reviews, and (2) topic modeling to profile sellers based on their advertisements. To the best of our knowledge, our system is the first to contribute to carding crime forensics by providing a means for large-scale cyber surveillance on carders and thereby alleviating law enforcement investigation efforts.

## Literature Review

We provide a review of prior work from the following related research areas to form the basis of our study.

## Underground Economy

The underground economy [20] is a vast international online black market for exchanging crime-related products and services, including vulnerabilities, malware, stolen data, host services, cash-out services, and spammers, to name only a few. Carders actively participate in the online underground economy to acquire tools or services for the malicious activities [23]. Sellers’ participation in the carding forums as well as their interactions with buyers have resulted in two critical textual traces: advertisements and customer reviews.

## Advertisements

Sellers rely heavily on advertisements as the major way of promoting products or services [17, 40]. Advertisements usually contain a thorough description of a product or service, the accepted payment options along with the prices, and the contact channels [17]. The advertisement is a reflection of the seller’s characteristics, from which we can profile the seller. For example, by categorizing the advertisement threads, we can determine the products or services in which the carder specializes. Advertisements (as shown in Figure 1) are relatively easy to distinguish from other forum posts for three reasons. First, the advertisements from the same seller use similar language and descriptions across forums [22]. This is because the seller posts the same advertisement multiple times to reach potential customers. To expedite this process, many sellers employ spamming scripts to automate advertisement posting [16, 17]. Second, the advertisements for the same product or service contain the same set of lexicons referring to a certain product or service feature, payment option, or contact channel. Third, advertisements all have an aesthetic appearance that regular posts usually do not have. To attract customers, advertisements often use capitalization, multicolored text, ASCII flares, and repeated sales pitches across multiple lines [17].

![](/api/attachments/97S7NYM7/fulltext/images/2f225e3c7725bdc71c92390edffccf213a8df552a0c6527df504916372c6cab1.jpg)  
Figure 1. Illustration of Underground Economy. In the Screenshot, Rescator is Promoting His Dump Shop by Listing the Prices, Highlighting the Dumps, and So On

## Customer Reviews

Because heterogeneous deception sensors [38] are lacking in computer-mediated communications, deception is pervasive in online social media [15]. It is especially so in the carding forums due to the absence of stringent regulations and the asymmetry of information [20]. Customer reviews serve as a crucial mechanism for building trust between buyers and sellers [22, 23, 24, 42]. Buyers leave comments regarding their experiences with the sellers or the products and services beneath the advertisement post [21]. These comments may, in turn, improve prospective buyers’ perceptions of the seller [25]. Exploratory research has found that customer reviews are critical for prospective buyers in assessing the seller quality [22, 32]. Therefore, sellers rely on positive comments to gain reputation, trust, and credibility [42]. For investigators, customer reviews collectively reflect the seller quality. Computational analysis of customer reviews would allow us to assess the sellers based on their quality and identify key sellers.

Since underground economies are hosted on carding forums [16, 17], we can leverage social media analytics to analyze textual traces in underground economy forums. Consequently, we review selected prior hacker social media analytics literature.

## Hacker Social Media Analytics

We review research investigating hacker communities using hacker social media data and social media analytics techniques. The review of prior research is organized using a taxonomy of four dimensions (Table 1): research objective, data source, analysis approach, and features. In particular, textual features include attributes derived from the message body that has semantic meaning [43]; and structural features include attributes from communication mechanisms, such as the number of posts, number of replies, and friendship connections [30].

## Research Objectives

Three major themes of objectives can be identified in past research. The first theme is the general exploration of the hacker community for enriching our understanding of the hacker community [21, 23, 39, 42, 53, 56]. Prior researchers are interested in exploring the operational mechanisms of hacker communities [53] and social norms [42]. The second theme is the analysis of hacker organizations [24, 31, 55]. This line of research mainly tests the generalizability of criminal organization theory in the context of online hacker communities. The third, emerging theme focuses on investigation of key hackers based on their reputation [2, 54]. This line of research relates to the identification of key sellers; however, there is a lack of evidence supporting the correlation between reputation scores and the seller quality.

## Data Sources

There are two major sources of data: social network services data and hacker community data. Social network services data have been used to investigate hacker social organizations [24]. For example, Holt and Strumsky [24] experimented on LiveJournal, a Russiabased social network service, to build a social network characterizing key hacker interactions. As hackers increasingly congregate in dedicated hacker communities to share hacking knowledge and experiences, find collaborators, and acquire malware, there has been a trend to examine hacker community data [33]. For example, Yip et al. [53] showed that forum-based underground economy had its unique operational mechanisms to sustain the black market. Following this stream of work, our research focuses on the forum-based underground economy where most advertisements and customer reviews reside.

Table 1. A Taxonomy of Prior Hacker Social Media Analytics Research

<table><tr><td rowspan="2">Study</td><td rowspan="2">Objective</td><td rowspan="2">Data</td><td colspan="2">Analysis</td><td colspan="2">Feature</td></tr><tr><td>Method</td><td>Manual</td><td>Textual</td><td>Structural</td></tr><tr><td>Benjamin et al. [9]</td><td>Identifying evidence of potential threats</td><td>HCD</td><td>IR</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Odabas et al. [39]</td><td>Theorizing and analyzing the underground economy</td><td>HCD</td><td>CA</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Zhang et al. [55]</td><td>Classifying hackers</td><td>HCD</td><td>CA</td><td>No</td><td>Yes</td><td>No</td></tr><tr><td>Abbasi et al. [2]</td><td>Identifying expert hackers and their specialties</td><td>HCD</td><td>SNA</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Lau et al. [29]</td><td>Mining cybercriminal network</td><td>SNS, HCD</td><td>LDA</td><td>No</td><td>Yes</td><td>No</td></tr><tr><td>Zhang and Li [54]</td><td>Identifying Characters of reputable hackers</td><td>HCD</td><td>SNA</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>Yip et al. [53]</td><td>Understanding forum-based underground economy mechanisms</td><td>HCD</td><td>CA, SNA</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Holt [21]</td><td>Examining social dynamics in cybercrime markets</td><td>HCD</td><td>CA</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Holt et al. [24]</td><td>Exploring Russian hacker social networks</td><td>SNS</td><td>SNA</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>Wang et al. [51]</td><td>Correlation between hacker discussions and attacks</td><td>HCD, VDB</td><td>LR</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>Zhao et al. [56]</td><td>Identifying adversaries</td><td>SNS</td><td>MB</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>Motoyama et al. [36]</td><td>Characterizing underground forums</td><td>HCD</td><td>SNA</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>Chu et al. [13]</td><td>Examining the creation and sale of malwares</td><td>HCD</td><td>CA</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Holt and Lampke [23]</td><td>Examining the nature of stolen data markets</td><td>HCD</td><td>CA</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Lu et al. [31]</td><td>Studying hacker community organization</td><td>SD</td><td>SNA</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Radianti [42]</td><td>Examining hacker social behavior leading to black market continuity</td><td>HCD</td><td>CA</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td colspan="7">Notes: CA = content analysis; CR = Cox Regression; HCD = hacker community data; IR = information retrieval; LDA = latent Dirichlet allocation; LR = linear regression; MB = model building; SD = secondary data; SNA = social network analysis; SNS = social network services; VDB = vulnerability database.</td></tr></table>

## Analysis Techniques

Three types of social media analytics techniques have been used: social network analysis, regression analysis, and content analysis. Widely adopted in hacker organization research, social network analysis has characterized the properties of hacker networks with centrality measures [2, 24, 31, 36, 54]. Yip et al. [53] further compared hacker networks to canonical social network models (e.g., preferential attachment) and discovered the uniqueness of the hacker networks. Regression analysis has been mostly leveraged to test the generalizability of theories in hacker communities. For example, Wang et al. [51] studied the relationship between the volume of cyber attacks and the number of attack-related threads. Content analysis employed grounded-theory methodology by manually examining hacker community texts [9, 39]. The findings include the operation mechanism [21, 53], black market dynamics [13, 23], and social behavior [42]. The biggest drawback of these studies has been the lack of scalability and consistency. The automation of content analysis, including text classification and topic modeling, is needed in light of the large and diverse international hacker community. Text classification techniques, such as Maximum Entropy classifier, have helped group similar documents together in many research contexts [34]. Topic modeling techniques, such as latent Dirichlet allocation, can automatically explore underlying topics from hacker community discussions.

## Features

Both textual features and structural features have been used. While structural features are useful in representing communication activities [44], textural features are informative in carrying semantics of the communication [1]. One major shortcoming of past textual feature analysis has been scalability. In contrast to hundreds of thousands of records that structural feature analysis could handle, prior textual feature analysis has been able to process only several hundred records through manual coding. On the other hand, many significant insights regarding hacker communities, such as the underground economy dynamics [13, 23, 39] and hacker behaviors [42], were first discovered by analyzing textual features (i.e., content analysis). The lack of scalability undermines the significance of the findings and the generalizability of the method. While prior studies leveraging textual features have demonstrated their potential in capturing rich hacker semantics, there is a need for interpreting the semantics of textual features on a large scale. Another drawback of past textual feature analysis is language barrier. The international hacker community has members speaking languages from all over the world; however, most of the past research focuses only on English [2, 55]. A language barrier is a big challenge for textual feature analysis on international hacker communities because multilingual textual analysis techniques are lacking. It is important to handle the multilingual problem either by developing language-specific textual analysis techniques or by using a reliable machine translator.

To summarize, several major conclusions can be drawn from the prior literature. First, focusing on key hackers has become an emerging direction for understanding hacker communities. Second, there is a trend to use hacker community data as hackers increasingly congregate in hacker communities. Third, significant findings from textual feature analysis necessitate a scalable method for content analysis that can interpret the semantics in hacker discussions.

## Text Mining for Content Analysis

We further review two promising types of text mining techniques that could automate content analysis: sentiment analysis and topic modeling. Sentiment analysis can quantify customer reviews to measure seller quality, while topic modeling can profile sellers based on their seller characteristics inherent in advertisements.

## Sentiment Analysis

Sentiment analysis is a class of text mining techniques for determining the subjective information of a text. Sentiment analysis has been applied to a variety of usergenerated content (UGC) contexts to inform business intelligence (BI). For example, Lau et al. [28] applied sentiment analysis to financial news to inform decision support for mergers and acquisitions; Bollen et al. [11] performed sentiment analysis on Twitter to predict stock prices; Aggarwal and Singh [4] tested the influence of the sentiment of blog posts on venture capitalists’ decision-making process; Archak et al. [7] demonstrated that the sentiment of product reviews is a determinant of consumers’ purchase decisions. Among all UGC contexts, online customer reviews have served as the most popular research testbed [47]. This validates our intention to apply sentiment analysis to the underground economy customer reviews.

From a methodological perspective, there are generally two types of approaches: machine-learning–based and dictionary-based. Machine-learning–based techniques train classifiers based on a set of predefined features extracted from the text. Commonly used classifiers include support vector machine (SVM) and naive Bayes (NB). Dictionary-based techniques rely on sentiment dictionaries incorporated with scoring rules to determine the sentiment scores in text. The sentiment dictionary includes mappings of words to sentiment scores, while the scoring rules guide the calculation of the sentiment score from the constituent words in the text. An emerging sentiment analysis technique that has outperformed existing methods is deep learning.

Deep-learning–based sentiment analysis is a hybrid approach with both machinelearning–based properties and dictionary-based properties [12, 46].

Deep-learning–based sentiment analysis includes two building blocks: word vectorization and recursive neural network (RNN) [46]. Word vectorization builds a word-vector language model to represent each word as a low-dimensional continuous-valued sentiment vector. RNN composites word sentiment vectors into sentence sentiment vectors using the parse trees of sentences, where words are the leaves and the phrases are the vertexes. Starting from the bottom subtree, RNN recursively computes the parent sentiment vectors from its children sentiment vectors. The root sentiment vector represents the sentiment score of the entire sentence. At each subtree, child vectors, $\xrightarrow [ { c _ { 1 } } ] { }$ and $\overrightarrow { c _ { 2 } }$ , are composited into the parent vector, ${ \vec { p } } ,$ using the equation: ${ \vec { p } } = \operatorname { t a n h } \left( W \left[ { \frac { { \overrightarrow { c _ { 1 } } } } { { \overrightarrow { c _ { 2 } } } } } \right] \right)$ . In this equation, <sup>W</sup> is the compositionality matrix that contains weights for compositing child vectors and tanh introduces nonlinearity into RNN to ensure model complexity. The deeplearning–based method proves to outperform state-of-the-art sentiment models by 5 percent and reaches 85 percent accuracy [46].

## Topic Modeling

Topic modeling refers to a class of statistical techniques for discovering the underlying topics from a corpus [10]. Latent Dirichlet allocation (LDA) is a prominent technique widely used as automated content analysis on social media data. LDA characterizes each document in the corpus as a mixture of topics, which are distributions over words with certain words having high probability [10]. While all the documents share the same set of topics, each document has different weights for the topics. Markov chain Monte Carlo (MCMC) sampling methods are often used to fit the LDA model. While LDA has gained increasing appreciation as a legitimate content analysis method, little research has leveraged this technique for hacker community analysis. Therefore, we turn to studies using LDA for business intelligence (BI), a discipline to which cyber-security intelligence belongs. We thus review and summarize prior studies from five perspectives: data, problem type, preprocessing procedure, topic interpretation, and evaluation method.

First, social media data have been widely modeled using LDA, including electronic communication [52], enterprise blogging posts [45], search engine queries [3], and stock recommendations [6]. Second, LDA can solve both confirmatory problems and exploratory problems. Confirmatory problems seek to match the inferred LDA topics against a predefined set of topics from the research context. For example, Singh et al. [45] used LDA to categorize enterprise blogs to determine whether they were workrelated, managerial, or technical; Bao and Datta [8] applied LDA to discover the predefined risk types concealed in 10-K forms. Exploratory problems seek to decompose the collection of documents into a list of themes. For instance, Aral et al. [5] decomposed a collection of stock recommendations to inform the analysis of buyers choices; Abhishek et al. [3] leveraged the output topics to interpret the semantics of the words; and Wu [52] measured the information diversity based on output topics. Third, the preprocessing procedure is widely performed [5, 10]. It usually includes removing annotations, tokenizing the sentences, lemmatizing terms, removing stop words, and so on. Fourth, it is a common practice to qualitatively interpret the topics from the distributions over the vocabulary. In particular, the distribution over the vocabulary is difficult for humans to conceive and interpret because of its massiveness. The most commonly adopted procedure is to infer the topic based on its top key words [5, 8, 45]. Fifth, as an unsupervised learning model, LDA lacks robust external validation methods for evaluating its results, so most studies evaluate their LDA models using internal validation [5, 45]. The major internal validation method is perplexity, a language modeling evaluation metric [8, 10]. Perplexity is a measure of the topic model’s ability to predict unobserved documents. However, as an internal validation metric, the perplexity value has been used to compare different models, but it cannot measure how close the model is to perfect classification.

## Research Gaps and Questions

Based on the review of prior literature on underground economy and hacker social media analytics, we present two research gaps.

First, prior research rarely approaches the underground economy through the lens of its participants, especially the key sellers. Most underground economy studies have instead focused on the social-economic features of the underground economy. However, key sellers play pivotal roles in cyber carding crimes and thus are critical for cyber forensics. The identification and profiling of key sellers can potentially provide actionable intelligence to law enforcement, and consequently, reduce potential financial fraud.

Second, few studies have systematically developed advanced text mining techniques to textual features in the underground economy. Moreover, we are not aware of any prior application of advanced text mining techniques, such as sentiment analysis and topic modeling, to carding forum discussions. Texts, such as advertisements and customer reviews, have shown great potential for revealing seller quality and characteristics in prior literature. There is a need for techniques that can handle the rich textual features in carding forums.

To address these research gaps, this study seeks to answer the following questions:

● How can we develop a scalable text mining-based system for identifying and profiling key sellers from the underground economy forums?

● How effective is it to leverage advanced text mining techniques to (1) identify key sellers using deep-learning–based sentiment analysis of customer reviews, and (2) profile key sellers using topic modeling of advertisements?

## Research Design

We propose the development of a text mining-based system called AZSecure for identifying and profiling key sellers based on advertisements and customer reviews in the underground economy. In particular, the system seeks to (1) identify key sellers using deep-learning–based sentiment analysis of customer reviews, and (2) profile key sellers using topic modeling of advertisements. We aim to compare our proposed system and techniques against popular benchmark techniques, including support vector machine, naive Bayes, k-Nearest Neighbour (kNN), and N-gram models. The evaluation will assess the effectiveness of our system for the identification and profiling of key sellers. We also present a case study to further demonstrate the utility and applicability of our proposed system in a real cyber forensics setting.

## Overview

We present the AZSecure system (Figure 2) for identifying and profiling the top sellers in the underground economy. The system contains two steps—the collection step and the analytics step. The collection step extracts advertisements and groups them based on the product and service type. The collection step has two components: thread crawling and thread classification. Thread crawling identifies underground economy-related threads from a comprehensive collection of a carding forum. Thread classification determines whether they are advertisement threads or not, and if so, what product or service they are promoting. The analytics step analyzes the advertisements and associated customer reviews to evaluate and profile the seller. This step has two components: seller rating and top seller profiling. The seller rating evaluates seller quality based on customer reviews. Top seller profiling extracts seller characteristics from advertisements. As discussed in the literature review, the scope of the research focuses on two groups of sellers—malware sellers and stolen data sellers. Nonetheless, our system can generalize to the sellers with other specialties. In the reminder of this section, we elaborate on each component in the system.

![](/api/attachments/97S7NYM7/fulltext/images/2ff95d42d07d7b05f0666ae7e626ab6cb86a56692d867a53331af2a11bbba201.jpg)  
Figure 2. The AZSecure Text Mining Research System

## Thread Crawling

The thread crawling component aims to generate an inclusive subset of undergroundeconomy–related threads and rule out irrelevant threads, thereby allowing the computation-intensive thread classification component to run more efficiently. If a carding forum user is involved in the underground economy, the user must have either (1) joined a thread containing underground economy keywords, or (2) joined a thread containing other users involved in the underground economy. Based on this intuition, we can find an inclusive subset of underground-economy–related threads by following users involved in threads containing underground-economy key words. The snowball sampling approach has been used in previous exploratory cyber-security research to collect the discussions from underground economy [22]. Inspired by this technique, we use a breadth-first search-based snowball method to retrieve potentially relevant threads (Algorithm 1).

```txt
Algorithm 1. Thread Crawling Using Snowball Sampling

Input: Ω={all threads}; X={all users}; Φ={underground economy-related keywords}
Output: X*={underground economy-related users}; Θ={thread|thread.author ∈ X*}
X* := {x|x.thread ∈ Θ};
collect all the threads that contains underground economy-related keywords
Θq := {θ|θ ∈ Ω, θ.contains(φ ∈ Φ)}; //Θq is the queue of threads to be examined
Θc := {}; //Θc is the thread history that keeps track of the traversed threads
while Θq is not empty do
    Get the next thread in collection θ := Θq.head;
    if θ ∈ Θc then continue; //skip if the thread has been traversed
    Θc.add(θ); //add the thread to be examined into the thread history
    find the users in the threads Y := {y|y ∈ X, yinvolveθ};
    for each y ∈ Y do
    if y∉X* then
    add the user to the underground economy-related user collection X*.add(y);
    add other threads the user posted to the task queue Θq.add({θ|θ.author = y});
collect the threads of underground economy-related users
    Θ = {thread|thread ∈ Ωandthread.author ∈ X*};
return X*, Θ;
```

Starting with a set of seeding underground economy key words, we first retrieve the threads containing these key words and the users in these threads. These users then become new seeds to find more threads that are relevant. This iterative process stops until all threads by hacker forum users interested in the underground economy are collected [14].

## Thread Classification

We use thread classification to identify advertisements for malware and stolen data from the crawled threads. The Maximum Entropy classifier (MaxEnt) has shown excellent performance in multiclass classification over other text classifiers due to its advanced feature selection technique [34]. MaxEnt learns the likelihood of each textual pattern’s systematic appearance in a certain class. In MaxEnt, each feature <sup>f</sup>i <sup>pattern</sup>; <sup>class</sup> represents the relationship between a certain textual pattern and a certain class, and the feature weight $\theta _ { i }$ represents the likelihood of the textual pattern’s systematic presence in the class. Further, the conditional probability of the textual data uses the entropy model: $p ( c l a s s \vert d a t a ) \propto \exp ( \sum _ { i } \theta _ { i } f _ { i } )$ . By maximizing this entropy, MaxEnt weights the

relevance of each textual patterns under each class. Therefore, MaxEnt allows us to emphasize certain features that are strongly related to a certain class and accommodate the dependencies among the features. In addition to the rankingbased feature selection that is inherent to MaxEnt, we incorporate three categories of knowledge-based features informed by prior literature [16, 17]: topical features, highlight features, and hyperlink features (Table 2). Topical features are textual features that semantically relate to underground economy topics. Monetary lexicons are a major type of underground economy topical feature. Domain-specific lexicons are words that reflect the product or service type of the advertisements. Lexical measures capture the fact that advertisements are usually longer than regular discussions where detailed descriptions are rarely needed. Highlight features are the layout details that depict the decoration of the advertisements, including page layout, multicolor texts, and font style (e.g., bold, italic). Hyperlink features capture the contact channels of these sellers including the external links and e-mail addresses.

Table 2. Features for Thread Classification

<table><tr><td>Category</td><td>Cue</td><td>Example</td><td>Type</td></tr><tr><td rowspan="3">Topical</td><td>Monetary lexicons</td><td>“$,” “Ruble,” “wmz”</td><td>Malware, Carding, Other products or services</td></tr><tr><td>Domain-specific lexicons</td><td>“cc,” “program,” “v1.0,” “shop”</td><td>Malware, Carding, Other products or services</td></tr><tr><td>Lexical measures</td><td>Length of the thread</td><td>Malware, Carding, Other products or services, Irrelevant</td></tr><tr><td rowspan="3">Highlight</td><td>Layout</td><td>“”</td><td>Malware, Carding</td></tr><tr><td>Color</td><td>“#FF0000”</td><td>Malware, Carding</td></tr><tr><td>Font style</td><td>“”</td><td>Malware, Carding</td></tr><tr><td rowspan="2">Hyperlink</td><td>External URLs</td><td>“shop: http://octavian.su”</td><td>Carding</td></tr><tr><td>E-mail</td><td>“@”</td><td>Malware, Carding</td></tr></table>

## Seller Rating

We measure the seller quality by quantifying customer reviews [17, 21]. As mentioned in the literature review, the review comments replying to an advertisement thread is a major channel for prospective buyers to evaluate the quality of a seller [7]. Sentiment analysis techniques have been used to evaluate the subjective information of the customer reviews. Therefore, we use the sentiment analysis score as a measure of a buyer’s evaluation of the seller quality. The seller rating component processes customer reviews through four steps: machine translation, word vectorization, recursive neural network, and score aggregation. We present our seller rating component in Algorithm 2.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2. Seller Rating Algorithm

Input: x=seller to be rated,  $\Theta = \{\theta|\theta$  is the advertisement of x},  $\Omega = \{\Omega_i|\Omega_i = \{\omega|\omega\text{ replies to } \theta_i\}$ , W=compositionality matrix.

Output:  $\Gamma = \{\gamma_i|\gamma_i$  is the rating for  $\theta_i\}$ , r=overall rating of the seller

for each advertisement  $\theta_i \in \Theta$  do

find the set of replies for the advertisement  $\Omega_i$ ;

for each reply  $\omega \in \Omega_i$  do

if  $\omega$  is not in English then

    $\omega := \text{translate}(\omega)$ ;

break  $\omega$  into a collection of sentences,  $S = \{s_1, s_2, \ldots, s_n\}$ 

for each sentence  $s_j \in S$  do

    $s_j := word\_vectorization(s_j|SentiTreebank)$ ;

    T := binary_parse_tree(s_j);

    Q := queue({root nodes of bottom subtrees in T});

while Q is not empty do

    n := thefirstnodeinQ;

    composite the parent vector  $\overrightarrow{p_n} := \tanh\left(W\left[\frac{\overrightarrow{p_{c1}}}{\overrightarrow{p_{c2}}}\right]\right)$ , c1 and c2 are children of n.

if the sibling of n has a sentiment vector then

    add the parent of n to Q;

    calculate the rating of the reply  $\gamma_{ij} := largest(\overrightarrow{p_{root}})$ ;

    calculate the rating of the advertisement  $\gamma_i := \sum \gamma_{ij}$ 

    calculate the rating of the seller r = average( $\Gamma$ )

return sellers and their ratings  $\Gamma$ , r;
</div>

We highlight the major steps in the seller rating component as follows: the thread content is automatically translated from the original language to English via Google Translate because much of the content is multilingual, which is incompatible with deep-learning–based sentiment analysis. This step first segments the content sentence by sentence, then detects the language of the original sentence, and finally translates the sentence to English. Then, each word is vectorized into a fivedimensional sentiment vector using SentiTreeBank, a word vector dictionary trained on customer reviews [46]. Each dimension represents an ordered sentiment degree, with the first dimension being the most negative and the fifth dimension being the most positive. The value of each dimension reflects the probability of being the corresponding sentiment degree. Next, the recursive neural network step parses the sentence into a binary tree and composites sentiment vectors recursively. From the bottom of the tree, we recursively combine the two child sentiment vectors into a single parent sentiment vector for each subtree. We evaluate the sentiment by averaging the probability of the root node sentiment vector over the sentiment spectrum. Finally, the sentiment-averaging step averages the post-level sentiment scores for each advertisement and further averages the advertisement level sentiment scores for each seller.

## Top Seller Profiling

As suggested by prior literature [17], we profile the top sellers in terms of seller characteristics, including product/service, payment options, and contact channels. Based on the intuition that the relationships among topics, documents, and words are similar to seller characteristics, sellers, and advertisements, we derive our top seller profiling component from latent Dirichlet allocation (LDA) to extract seller characteristics. In particular, we build the seller characteristic model based on the following assumptions: (1) the advertisement is represented with a collection of words; (2) the characteristic is treated as a distribution over words; (3) the seller is portrayed by the collection of advertisements; and (4) the seller is characterized by a mixture of characteristics, in which we are interested. We define the corresponding generative process in Algorithm 3 accordingly:

## Algorithm 3. Top Seller Advertisement Generative Process

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Step 1. For each seller s, choose seller characteristics proportion  $\boldsymbol{\theta}_{s}\sim\text{Dirichlet}(\alpha)$ , where  $\boldsymbol{\theta}_{s}=(\theta_{s1},\ldots,\theta_{sT})$  with  $\theta_{st}$  being the probability of seller s having characteristics t and  $\alpha$  is the hyperprior parameter.
Step 2. For each characteristic z, choose seller characteristic  $\varphi_{z}\tilde{\text{Dirichlet}}(\beta)$ , where  $\varphi_{z}=(\varphi_{z1},\ldots,\varphi_{zW})$  with  $\varphi_{zw}$  being the probability of word w in characteristic z and  $\beta$  is the hyperprior parameter.
Step 3. For each word w in that the advertisements of seller s,
a. Choose a characteristic  $z_{w}\tilde{\text{Multinomial}}(\boldsymbol{\theta}_{s})$ .
b. Choose the word  $w_{s}\tilde{\text{Multinomial}}(\boldsymbol{\varphi}_{z})$
</div>

This process depicts the imaginary process through which the advertisements were generated. Following McCallum and Mallet [35], we fit our model using collapsed Gibbs sampling. Based on the fitted seller characteristic model, we first interpret each characteristic with the top key words, then extract the posterior seller characteristic proportion $p ( \theta _ { s } | w )$ , and finally profile the seller with the major characteristics. We summarize the major steps of top seller profiling component in Algorithm 4.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 4. Top Seller Profiling Algorithm

Input:  $D = \{d_s | d_s$  is the collection of advertisements of top seller s

Output:  $C = \{C_s | C_s$  isthecharacteristicsofsellers

for each seller s do

    preprocess  $d_s$  using unigram model  $d_s = \text{preprocess}(d_s)$ 

fit the seller characteristic model to D using collapsed Gibbs sampling

for each characteristic z do

    pick the top-k words to interpret seller characteristic  $\varphi_z$ 

for each seller s do

    extract the posterior seller characteristic proportion  $p(\theta_s | w)$ 

    pick the top-p seller characteristics  $\varphi_z$ 

    use the interpreted characteristics to profile the seller  $C_s = \{\varphi_z \text{interpretation}\}$ 

return C
</div>

## Evaluation

To evaluate the key technical components in our proposed system, three experiments were conducted by comparing against several benchmark methods.

## Testbed

The experiments and case study were conducted across the research testbed encompassing eight forum-based underground economies (Table 3). Due to the sensitivity of the underground economy, we censored the forum names. Forums 5 through 8 were recommended by our cyber-security expert who examined the same forums in prior studies. Forums 1 through 4 were found via following the web links posted by users in the four aforementioned forums. All the forums are then validated by our cybersecurity expert to ensure data integrity. A majority of these forums are Russian carding forums because East European hackers are heavily involved in cyber carding. These carding forums are often equipped with sophisticated anticrawling measures. To collect them, we leveraged multiple countersecurity measures, including automated authentication, cookie installation, concealing request origin, and so forth. Most of these forums are longitudinal in nature, with thousands of members and tens of thousands of posts and threads. All metadata are extracted, including thread title, original post content, user, date, post sequence, and so on.

Table 3. Summary of the Carding Forums

<table><tr><td>Forum</td><td>Date range</td><td>Members</td><td>Threads</td><td>Posts</td><td>Language</td></tr><tr><td>1</td><td>1/1/2003–8/29/2015</td><td>35,406</td><td>90,520</td><td>622,560</td><td>Russian</td></tr><tr><td>2</td><td>12/17/2010–6/23/2015</td><td>4,168</td><td>14,228</td><td>23,094</td><td>English</td></tr><tr><td>3</td><td>6/2/2007–11/17/2015</td><td>27,607</td><td>70,302</td><td>679,893</td><td>English/Russian</td></tr><tr><td>4</td><td>8/7/2013–3/11/2016</td><td>4,972</td><td>4,834</td><td>38,335</td><td>English</td></tr><tr><td>5</td><td>7/20/2002–1/3/2015</td><td>13,572</td><td>49,617</td><td>395,530</td><td>Russian</td></tr><tr><td>6</td><td>4/15/2009–9/4/2015</td><td>3,818</td><td>12,869</td><td>43,073</td><td>Russian</td></tr><tr><td>7</td><td>2/26/2005–9/3/2015</td><td>7,761</td><td>16,194</td><td>157,106</td><td>Russian</td></tr><tr><td>8</td><td>6/13/2007–9/3/2015</td><td>4,850</td><td>48,947</td><td>62,316</td><td>Russian</td></tr></table>

## Experiment 1: Thread Classification

## Experimental Setup

The objective of the first experiment was to assess the effectiveness of the proposed thread classification technique and the benchmark techniques in determining the type of advertisement threads. Each thread was to be classified into four groups: malware advertisement, stolen data advertisement, other advertisement, and nonadvertisement. The first two groups of advertisement threads would lead us to malware sellers and stolen data sellers. One thousand threads were randomly chosen and manually categorized into the aforementioned four groups. The benchmark methods consisted of state-of-the-art text classifiers, including SVM, NB, and k-NN. All the benchmark methods used the best parameter combinations optimized on the research testbed to allow the best comparison against the proposed thread classification. Both our proposed thread classification technique and the benchmark methods were trained on the holistic feature set. Finally, all methods were evaluated using a fivefold cross-validation setting to avoid overfitting. Standard evaluation metrics including precision, recall, and the F-measure were used: precision measures the correctness of the identified instances matching its true class; recall measures the completeness of the identified instances with respect to the desired category; and the F-measure assesses the overall performance by calculating the harmonic mean of precision and recall. Testing set results from each fold were aggregated to test the statistical significance of the techniques’ performance.

## Results

Table 4 shows the experimental results for categorizing malware and stolen data advertisements. The proposed MaxEnt-based method had the best performance, with an F-measure of 69.17 percent in categorizing malware advertisements and an F-measure of 84.88 percent in categorizing stolen data advertisements. Furthermore, our proposed method reached 90.20 percent on precision in categorizing malware advertisements and 97.33 percent on precision in categorizing stolen data advertisements, suggesting that most of the extracted advertisements were correct hits. In terms of the benchmark methods, SVM had the best overall performance. SVM achieved 49.13 percent on the F-measure in categorizing malware advertisements and 77.22 percent on the F-measure in categorizing stolen data advertisements. Overall, our proposed MaxEnt-based thread classifier outperformed the best benchmark method by 20.04 percent on the F-measure in classifying malware advertisements and 7.66 percent in classifying stolen data advertisements.

Table 4. Thread Classification Performance (%)

<table><tr><td rowspan="2">Techniques</td><td colspan="3">Malware</td><td colspan="3">Stolen data</td></tr><tr><td>Precision</td><td>Recall</td><td>F-measure</td><td>Precision</td><td>Recall</td><td>F-measure</td></tr><tr><td>MaxEnt</td><td>90.20</td><td>56.10</td><td>69.17</td><td>97.33</td><td>75.26</td><td>84.88</td></tr><tr><td>NB</td><td>37.01</td><td>57.32</td><td>44.98</td><td>58.45</td><td>85.57</td><td>69.46</td></tr><tr><td>SVM</td><td>87.50</td><td>34.15</td><td>49.13</td><td>100.00</td><td>62.89</td><td>77.22</td></tr><tr><td>kNN</td><td>41.56</td><td>39.02</td><td>40.25</td><td>64.86</td><td>74.23</td><td>69.23</td></tr></table>

Table 5. P-Values for Pairwise t-tests on Precision, Recall, and the F-Measure for MaxEnt-based Method over the Benchmark Methods

<table><tr><td rowspan="2"></td><td>MaxEnt vs. NB</td><td>MaxEnt vs. SVM</td><td>MaxEnt vs. kNN</td><td>MaxEnt vs. NB</td><td>MaxEnt vs. SVM</td><td>MaxEnt vs. kNN</td></tr><tr><td colspan="3">Malware (H1a)</td><td colspan="3">Stolen data (H1b)</td></tr><tr><td>Precision</td><td>&lt; 0.001***</td><td>0.1309</td><td>&lt; 0.001***</td><td>&lt; 0.001***</td><td>0.176</td><td>&lt; 0.001***</td></tr><tr><td>Recall</td><td>0.1785</td><td>0.0082**</td><td>0.0170*</td><td>0.074</td><td>0.0221*</td><td>0.5114</td></tr><tr><td>F-</td><td></td><td>measure</td><td>&lt; 0.001***</td><td>0.0141*</td><td>&lt; 0.001***</td><td>&lt; 0.001***</td></tr><tr><td>0.0441*</td><td>0.0033**</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Notes: Asterisks represent significance level: \*: p < 0.05, \*\*: p < 0.01, \*\*\*: p < 0.001.

Table 5 shows the p-values for the pairwise t-test conducted on the classification evaluation for both malware advertisements and stolen data advertisements. In extracting malware advertisements, the MaxEnt-based thread classifier significantly outperformed the benchmark methods on most experimental metrics. Specifically, it significantly outperformed all the benchmark methods on recall and the F-measure and it significantly outperformed NB and kNN on precision. In extracting stolen data advertisements, our proposed method significantly outperformed all the benchmark methods on the F-measure, NB and kNN on precision, and NB and SVM on recall.

## Discussion

In Experiment 1, we assessed the system’s effectiveness in identifying the malware sellers and stolen data sellers. There are several interesting findings. First, the overall performance for identifying the malware sellers was not as good as that for identifying the stolen data sellers. We believe that the variation of malware advertisement content might be the cause. In the case of malware advertisements, less text was observed in malware advertisements probably because malware writers wanted to prevent imitation and potential competition. Therefore, the amount of text was insufficient for the classifiers to effectively discriminate. Second, SVM achieved the highest on precision and lowest on recall in classifying stolen data advertisements. This suggests that SVM suffered overfitting: SVM failed to identify many stolen data advertisements but what SVM captured was mostly correct. On the other hand, our proposed method is capable of balancing between precision and recall, resulting in a higher F-measure. Third, we notice that MaxEnt performed far better than the benchmark methods. This is attributed to MaxEnt’s advanced feature selection technique, which emphasizes the most relevant features to each class. To demonstrate this point, we examined the impact of N-gram features on the overall performance (Figure 3). When given the unigram feature set, the overall performance of MaxEnt is comparable to SVM. As we introduced more features by allowing for higher-order N-gram features, MaxEnt was able to consistently select the most relevant features compared whereas NB and SVM suffered from overfitting.

![](/api/attachments/97S7NYM7/fulltext/images/f26e766abf9be467fbfb57fd70fccda50ac3360e03ecb57e9d7cc498ddee02b4.jpg)  
(a)

![](/api/attachments/97S7NYM7/fulltext/images/df6b4967ac805859c1ce8a361ec27b46972d93b8e52148902fa6deb609dbfe08.jpg)  
(b)  
Figure 3. Impact of N-gram Features on the Overall Thread Classification Performance: (a) Malware Advertisements Classification; (b) Stolen Data Advertisements Classification

## Experiment 2: Seller Rating

## Experimental Setup

The objective of the second experiment was to assess the efficacy of our proposed seller rating technique, RNN, and the benchmark methods in determining the sentiment orientation of customer reviews. The customer reviews were to be classified into either a positive sentiment or a negative sentiment. Four hundred customer reviews were randomly chosen and manually categorized into the two sentiment orientations. The benchmark methods consisted of both machine-learning–based techniques, including SVM and NB, and the dictionary-based technique, the well-known SentiWordNet (SWN). SVM and NB were trained on the feature set containing N-grams and part-of-speech (POS) tags. Similarly, we optimize the benchmark methods to allow best possible comparison. Similar to Experiment 1, all methods were tested using a fivefold cross-validation setting to avoid overfitting. We also use precision, recall, and the F-measure for evaluation.

## Results

Table 6 shows the experimental results for determining the sentiment orientation of customer reviews. The proposed deep-learning–based seller rating technique (RNN) generally outperformed all the benchmark methods, with 96.12 percent on the F-measure in determining positive review comments and 90.14 percent on the F-measure in determining negative review comments. In terms of the benchmark methods, the best F-measure for positive sentiment was 93.31 percent by SVM and the best F-measure for negative sentiment was 82.91 percent by NB. Overall, our proposed deep-learning–based seller rating technique outperformed the best benchmark method by 2.81 percent in positive reviews and 7.23 percent in negative reviews. Table 7 shows the p-values for the pairwise t-test for the experiment evaluating RNN against baseline methods. RNN significantly outperformed the benchmark methods on most experimental metrics. In particular, RNN significantly outperformed all the benchmark methods on the F-measure. RNN also significantly outperformed SVM on precision and NB and SWN on recall.

Table 6. Seller Rating Performance (%)

<table><tr><td rowspan="2">Techniques</td><td colspan="3">Positive sentiment</td><td colspan="3">Negative sentiment</td></tr><tr><td>Precision</td><td>Recall</td><td>F-measure</td><td>Precision</td><td>Recall</td><td>F-measure</td></tr><tr><td>RNN</td><td>94.20</td><td>98.11</td><td>96.12</td><td>95.05</td><td>85.71</td><td>90.14</td></tr><tr><td>NB</td><td>94.12</td><td>90.57</td><td>92.31</td><td>79.51</td><td>86.61</td><td>82.91</td></tr><tr><td>SVM</td><td>89.58</td><td>97.36</td><td>93.31</td><td>92.13</td><td>73.21</td><td>81.59</td></tr><tr><td>SWN</td><td>93.40</td><td>63.45</td><td>75.57</td><td>48.29</td><td>88.39</td><td>62.46</td></tr></table>

Notes: Bolded numbers are the best performance.

Table 7. P-Values for Pairwise t-tests on Precision, Recall, and the F-Measure for Deep Learning-based Method over the Benchmark Methods

<table><tr><td rowspan="2"></td><td colspan="3">H2</td></tr><tr><td>RNN &gt; NB</td><td>RNN &gt; SVM</td><td>RNN &gt; SWN</td></tr><tr><td>Precision</td><td>0.9866</td><td>0.0124*</td><td>0.399</td></tr><tr><td>Recall</td><td>&lt; 0.001***</td><td>0.4927</td><td>&lt; 0.001***</td></tr><tr><td>F-measure</td><td>0.0016**</td><td>0.00582**</td><td>&lt; 0.001***</td></tr></table>

## Discussion

In Experiment 2, we assessed the system’s efficacy in determining the sentiment orientations (i.e., positive or negative) from customer reviews. The overall performance on our testbed was better than on previous testbeds, such as blog [4] and product reviews [7]. This is because texts on the aforementioned testbeds had relatively vague sentiment orientations, while much of the feedback in our testbed was made up of comments with clear sentiment terms, such as “good,” “good seller,” or “invalid.” To evade the investigation, Russian hackers tend to leave brief review comments with simple terms, such as “прекрасный” (“prekrasnyy” meaning “excellent”), “отличный” (“otlichnyy” meaning “great”), and “теряю деньги” (“teryayu den’gi” meaning “lost money”), which significantly lowered the translation difficulty caused by ambiguity. Google Translate has thus reduced its negative side effect to the minimum. The machine-learning–based techniques had better overall performance (i.e., the F-measure) than the dictionary-based approach. The reason is that machine-learning– based techniques had the ability to learn new patterns from data, while the scoring rules in the dictionary-based technique were predefined and may not apply to our testbed. Overall, our proposed technique is effective in evaluating customer reviews and further rating the sellers.

## Experiment 3: Top Seller Profiling

## Experimental Setup

The objective of the third experiment was to assess the effectiveness of the proposed LDA-based top seller profiling technique and the benchmark methods in modeling seller advertisements. The most typical evaluation for topic models is perplexity, which measures the model’s ability to predict unobserved documents [8, 10]. In particular, a good model learned on the training set should give better prediction on the testing set. Better models have lower perplexity, suggesting less uncertainty about the unobserved document. Perplexity given test data <sup>D</sup> was computed as follows:

$$
\text { Perplexity } (D) = \exp \left(- \sum_ {d = 1} ^ {D} \log p (\boldsymbol {w} _ {d}) / \sum_ {d = 1} ^ {D} N (d)\right),
$$

where $p ( w _ { d } )$ is the probability of document <sup>d</sup> and $N ( d )$ is the length of document <sup>d</sup>. We compared our proposed model against the benchmark methods, including unigram, bigram, and trigram models. All techniques were run using a tenfold cross-validation setting. Our LDA-based top seller profiling technique was parameterized with 1,500 iterations of collapsed Gibbs sampling and 100 seller characteristics. Hyperparameters were set to $a = 0 . 0 1$ and β= 0.5 as suggested in Blei [10]. Benchmark N-grams models were trained with commonly adopted Good–Turing smoothing.

Table 8. Comparison of Models on Holdout Perplexity

<table><tr><td></td><td>Unigram</td><td>Bigram</td><td>Trigram</td><td>LDA</td></tr><tr><td>Mean</td><td>19,250.02</td><td>4,388.08</td><td>3,682.49</td><td>1,968.08</td></tr><tr><td>Std. dev.</td><td>2,119.24</td><td>653.05</td><td>684.41</td><td>306.07</td></tr><tr><td>p-value</td><td>&lt; 0.001***</td><td>&lt; 0.001***</td><td>&lt; 0.001***</td><td>—</td></tr></table>

Notes: Asterisks represent significance level: \*: p < 0.05, \*\*: p < 0.01, \*\*\*: p < 0.001.

## Results

Table 8 shows the experimental results and t-test results. The proposed LDA-based seller profiling technique outperformed all the benchmark methods. It achieved the lowest perplexity (1,968.08), suggesting strong certainty in modeling unobserved documents (i.e., sellers). In contrast, the unigram model performed poorly with a perplexity of 19,250.02. Results from the paired t-tests suggested that our proposed LDA-based top seller profiling technique significantly outperformed all the benchmark methods.

## Discussion

In the experiment, the LDA-based top seller profiling technique had the best performance. LDA was effective in modeling seller advertisements. It outperformed the benchmark methods, N-grams models, because it assumes characteristics as distributions of words, and sellers as distributions of characteristics while N-grams models only profile sellers with frequent words. The perplexity value of our proposed model was comparable to Blei’s [10], suggesting a plausible model. The unigram model was much worse than the others due to its independence assumption.

## Case Study: The Cyber-Forensics Setting

To demonstrate the value of our system, we conducted a case study to examine the application of our system in a real cyber-forensics setting. In particular, we show how we address the following questions when working with real carding communities: Who created the malware used to conduct the cyber carding crime? And who sold the stolen card data? What are the characteristics of top sellers in the carding community? We chose the top three forums (in terms of members and activities) in our research testbed as the case study data set. Each forum was processed individually so that we could compare the results across forums and further assess the generalizability of the system.

Table 9. Top 3 Best/Worst Malware and Stolen Data Sellers for Each Forum

<table><tr><td rowspan="3">Rank</td><td colspan="4">Top 3 Best</td><td colspan="4">Top 3 Worst</td></tr><tr><td colspan="2">Malware</td><td colspan="2">Stolen data</td><td colspan="2">Malware</td><td colspan="2">Stolen Data</td></tr><tr><td>User</td><td>Score</td><td>User</td><td>Score</td><td>User</td><td>Score</td><td>User</td><td>Score</td></tr><tr><td colspan="9">Forum 1</td></tr><tr><td>1</td><td>L**G</td><td>5</td><td>I**]</td><td>3.6</td><td>N**g</td><td>1.8</td><td>I**s</td><td>2.3</td></tr><tr><td>2</td><td>V**U</td><td>4.5</td><td>A**s</td><td>3.5</td><td>K**a</td><td>2</td><td>P**A</td><td>2.3</td></tr><tr><td>3</td><td>G**l</td><td>4</td><td>D**R»</td><td>3.4</td><td>D**i</td><td>2</td><td>S**8</td><td>2.4</td></tr><tr><td colspan="9">Forum 3</td></tr><tr><td>1</td><td>H**l</td><td>4</td><td>Rescator</td><td>4.4</td><td>N**0</td><td>2</td><td>F**4</td><td>1.3</td></tr><tr><td>2</td><td>B**t</td><td>4</td><td>F**x</td><td>4</td><td>1**4</td><td>2</td><td>S**3</td><td>1.3</td></tr><tr><td>3</td><td>S**r</td><td>4</td><td>R**c</td><td>4</td><td>M**D</td><td>2</td><td>L**u</td><td>1.3</td></tr><tr><td colspan="9">Forum 5</td></tr><tr><td>1</td><td>P**t</td><td>5</td><td>B**r</td><td>4</td><td>R**t</td><td>1.5</td><td>R**y</td><td>1</td></tr><tr><td>2</td><td>D**n</td><td>4</td><td>B**1</td><td>4</td><td>W**0</td><td>1.6</td><td>M**n</td><td>1</td></tr><tr><td>3</td><td>D**f</td><td>4</td><td>S**c</td><td>4</td><td>G**n</td><td>2</td><td>J**a</td><td>2</td></tr></table>

Notes: Asterisks are used to anonymize seller screen names. Bolded entries are key sellers who we provide more details on.

## Key Seller Identification

We used the seller rating component in our system to identify the key sellers. The three best-rated sellers and the three worst-rated sellers for three of the forums are listed in Table 9. Seller screen names are anonymized partially to avoid possible complication.

Three findings can be drawn from comparing these malware and stolen data sellers for all three forums. First, some forums had better-rated sellers than others. For example, stolen data sellers in Forum 1 were not as highly rated as those in the other two forums. Stolen data sellers in Forum 3 were the most highly rated among the three forums. Second, malware sellers generally tended to have higher ratings than the stolen data sellers for all three forums. This phenomenon is attributable to the property of the goods they are selling. The quality of malware is easier to determine than that of carding information. It is not easy for carders to guarantee the validity of each carding record due to the banking industry’s remedial actions. Third, all three forums had equally fraudulent malware sellers and stolen data sellers. This means that although different measures of regulation had been enforced in each forum, fraudulent sellers existed universally across these underground economies.

## Top Seller Profiling

The top seller profiling component was trained on malware and stolen data advertisements separately. As a common practice from prior literature [5, 8, 45], the top

Table 10. Top Seller Characteristics of Rescator

<table><tr><td>#</td><td>Top key words</td><td>Interpretation</td></tr><tr><td>5</td><td>shop, wmz, icq, webmoney, price, dump,</td><td>Product: CCs, dumps (valid, verified);</td></tr><tr><td>6</td><td>валид (valid), чекер (checker), карты (cards), баланс (balance), карт (cards)</td><td>Payment: wmz, webmoney, bitcoin, lesspay;</td></tr><tr><td>8</td><td>shop, good, CCs, bases, update, cards, bitcoin, webmoney, validity, lesspay</td><td>Contact: shop, register, deposit, e-mail, icq, jabber</td></tr><tr><td>11</td><td>dollars, dumps, deposit, payment, sell, online, verified</td><td></td></tr><tr><td>16</td><td>e-mail, shop, register, icq, account, jabber,</td><td></td></tr></table>

10 seller characteristics were reviewed for each seller and the top key words were extracted to interpret each characteristic. The resulting seller characteristics were categorized into a taxonomy comprising three topical groups: product or service type, payment options, and contact channels. Our example relates to one of the top carding sellers, Rescator from Forum 3, who was famous for distributing stolen data from the Target breach [27]. Table 10 shows the top 5 seller characteristics of Rescator. Based on the top key words from each seller characteristic, we profiled this particular seller from product or service type, payment options, and contact channels: Rescator sold mostly CC (credit card) and dumps (card magnetic strip) through the shop that required deposit and registration or email/icq/jabber and accepts mainly webmoney, Bitcoin, and lesspay. To verify the findings from top seller profiling regarding Rescator, we compared the profile against the seller’s advertisement in the forum. We show the essence of the advertisement in Figure 4a. The findings from the original advertisement generally matched our profiling. Furthermore, we were able to find Rescator’s shop through the link in the advertisement (Figure 4b), where we found millions of stolen payment cards for sale.

![](/api/attachments/97S7NYM7/fulltext/images/c3e447bbf06648cbeedd615d8373ddd4cf372aad9042067b9d222f86a1a05749.jpg)  
Figure 4. Illustration of Seller Characteristics: (a) Seller Characteristics Reflected from Rescator’s Advertisement; (b) Rescator’s Carding Shop

## Conclusions

In this study, we proposed the AZSecure text mining-based system for identifying and profiling top sellers in the underground economy. Three experiments were performed to evaluate the efficacy of our system in identifying threads of relevance, classifying customer feedback sentiment, and profiling seller characteristics. Our proposed system outperformed the benchmark methods, reaching an average F-measure of about 80 percent to 90 percent. A case study was provided to illustrate the utility and applicability of our proposed system in a real cyberforensics setting. We identified the best-rated and the least-reputable malware sellers and stolen data sellers in three carding forums, discovered both similarities and differences between malware sellers and stolen data sellers and across different forums, and delivered an accurate profile for the famous carder, Rescator.

The contribution of our research is manifold. First, we proposed to study the underground economy through the new lens of its participants, especially the key sellers. Key sellers play a pivotal role in cyber carding crime by providing the critical criminal activities. Knowing the key sellers and observing their behaviors enriches our understanding of the underground economy and may allow us to further contain potential crimes. Second, we developed advanced text mining techniques to analyze multilingual textual traces in the underground economy. As hackers increasingly congregate in the hacker communities, the question of how to use hacker community data to inform cyber-security intelligence remains open [33]. Our research gives an example of leveraging social media analytics to probe into the underground economy in order to target key sellers and possibly prevent future fraud. Third, we developed a novel system capable of identifying and profiling key international underground economy sellers and conducted experiments to evaluate its effectiveness. A holistic feature set and advanced text mining techniques were leveraged to help identify and profile key sellers from carding forum discussions. Experiments demonstrated the effectiveness of our proposed system as compared with benchmark methods. Fourth, we built a hacker community data set encompassing eight major carding forums. As the firsthand carding community data, this data set would benefit researchers in their academic exploration and practitioners in their crime investigation.

Future directions for this research are suggested as follows. First, we will consider distinguishing the authenticity of the customer reviews. We treated each review equally, assuming that customer feedback was a true reflection of the reality. This may not be true, if feedback manipulation exists. Second, we will investigate the correlation between price or reputation and seller quality. For example, does a high-quality seller necessarily benefit from higher prices and a better reputation? Third, we will also further study buyers’ advertisements, where buyers are asking for a specific product or service. These advertisements are also valuable for understanding carder behavior. Fourth, we intend to develop language-specific sentiment analysis that allows us to better capture the semantics of the text in East European languages, especially Russian.

Acknowledgments: This work was supported in part by the National Science Foundation under Grant no. SES-1314631 and DUE-1303362.

## REFERENCES

1. Abbasi, A.; Chen, H.; and Nunamaker, J.F. Jr. Stylometric identification in electronic markets: Scalability and robustness. Journal of Management Information Systems, 25, 1 (2008), 49–78.

2. Abbasi, A.; Li, W.; Benjamin, V.; Hu, S.; and Chen, H. Descriptive analytics: Investigating expert cybercriminals in web forums. In M. den Hengst, M. Israël, and D. Zeng (eds.). Proceedings of the IEEE Joint Intelligence and Security Informatics Conference. The Hague: IEEE, 2014, pp. 56–63.

3. Abhishek, V.; Gong, J.; and Li, B. Examining the impact of contextual ambiguity on search advertising keyword performance: A topic model approach. Available at SSRN: https://ssrn.com/abstract=2404081 or http://dx.doi.org/10.2139/ssrn.2404081

4. Aggarwal, R., and Singh, H.H. Differential influence of blogs across different stages of decision making: The case of venture capitalists. MIS Quarterly, 37, 4 (2013), 1093–1112.

5. Aral, S.; Ipeirotis, P.; and Taylor, S. Content and context: Identifying the impact of qualitative information on consumer choice. (March 12, 2011). Available at SSRN: https:// ssrn.com/abstract=1784376 or http://dx.doi.org/10.2139/ssrn.1784376

6. Aral, S., and Walker, D. Creating social contagion through viral product design: A randomized trial of peer influence in networks. Management Science, 57, 9 (2011), 1623–1639.

7. Archak, N.; Ghose, A.; and Ipeirotis, P.G. Deriving the pricing power of product features by mining consumer reviews. Management Science, 57, 8 (2011), 1485–1509.

8. Bao, Y., and Datta, A. Simultaneously discovering and quantifying risk types from textual risk disclosures. Management Science, 60, 6 (2014), 1371–1391.

9. Benjamin, V.A.; Li, W.; Holt, T.J.; and Chen, H. Exploring threats and vulnerabilities in hacker web forums, IRC and carding shops. In Proceedings of IEEE International Conference on Intelligence and Security Informatics. Baltimore, MD, 2015, pp. 85–90.

10. Blei, D.M. Probabilistic topic models. Communications of the ACM, 55, 4 (2012), 77–84.

11. Bollen, J.; Mao, H.; and Zeng, X. Twitter mood predicts the stock market. Journal of Computational Science, 2, 1 (2011), 1–8.

12. Chen, D.; Socher, R.; Manning, C.D.; and Ng, A.Y. Learning new facts from knowledge bases with neural tensor networks and semantic word vectors (March 16, 2013). Available at arXiv: https://arxiv.org/abs/1301.3618.

13. Chu, B.; Holt, T.J.; and Ahn, G.J. Examining the Creation, Distribution, and Function of Malware On Line. 2010. Available at: www.ncjrs.gov/App/Publications/abstract.aspx?ID=252143

14. Chung, W.; Chen, H.; and Nunamaker, J.F. Jr. A visual framework for knowledge discovery on the web: An empirical study of business intelligence exploration. Journal of Management Information Systems, 21, 4 (2005), 57–84.

15. Derrick, D.C.; Meservy, T.O.; Jenkins, J.L.; Burgoon, J.K.; and Nunamaker, J.F. Jr. Detecting deceptive chat-based communication using typing behavior and message cues. ACM Transactions on Management Information Systems, 4, 2 (2013), 1–21.

16. Fallmann, H.; Wondracek, G.; and Platzer, C. Covertly probing underground economy marketplaces. In C. Kreibich and M. Jahnke (eds.). Detection of Intrusions and Malware, and Vulnerability Assessment. DIMVA 2010. Lecture Notes in Computer Science, vol 6201. Bonn: Springer, 2010, pp. 101–110.

17. Fossi, M.; Johnson, E.; Turner, D. et al. Symantec report on the underground economy. Journal of Financial Services Technology, 3, 1 (2009), 77–82.

18. Fuller, C.M.; Biros, D.P.; Burgoon, J.; and Nunamaker, J.F. Jr. An examination and validation of linguistic constructs for studying high-stakes deception. Group Decision and Negotiation, 22, 1 (2013), 117–134.

19. Graaf, D. De; Shosha, A.; and Gladyshev, P. BREDOLAB: Shopping in the cybercrime underworld. In M. Rogers and K.C. Seigfried-Spellar (eds.). Digital Forensics and Cyber Crime. ICDF2C 2012. Lecture Notes of the Institute for Computer Sciences, Social

Informatics and Telecommunications Engineering, vol 114. Lafayette: Springer, 2012, pp. 302–313.

20. Herley, C., and Florêncio, D. Nobody sells gold for the price of silver: Dishonesty, uncertainty and the underground economy. In T. Moore, D. Pym, and C. Ioannidis (eds.). Economics of Information Security and Privacy. Boston: Springer, 2010, pp. 33–53.

21. Holt, T.J. Examining the forces shaping cybercrime markets online. Social Science Computer Review, 31, 2 (September 2012), 165–177.

22. Holt, T.J. Exploring the social organisation and structure of stolen data markets. Global Crime, 14, 2–3 (2013), 155–174.

23. Holt, T.J., and Lampke, E. Exploring stolen data markets online: Products and market forces. Criminal Justice Studies, 23, 1 (2010), 33–50.

24. Holt, T.J.; Strumsky, D.; Smirnova, O.; and Kilger, M. Examining the social networks of malware writers and hackers. International Journal of Cyber Criminology, 6, 1 (2012), 891–903.

25. Jensen, M.L.; Averbeck, J.M.; Zhang, Z.; and Wright, K.B. Credibility of anonymous online product reviews: A language expectancy perspective. Journal of Management Information Systems, 30, 1 (2013), 293–324.

26. Kaspersky Lab. Carbanak APT: The great bank robbery. Securelist, 2015. https:// securelist.com/files/2015/02/Carbanak\_APT\_eng.pdf.

27. Krebs, B. The Target breach, by the numbers. KrebsonSecurity, 2014. http://krebsonse curity.com/2014/05/the-target-breach-by-the-numbers/.

28. Lau, R.Y.K.; Liao, S.S.Y.; Wong, K.F.; and Chiu, D.K.W. Web 2.0 environmental scanning and adaptive decision support for business mergers and acquisitions. MIS Quarterly, 36, 4 (2012), 1239–1268.

29. Lau, R.Y.K.; Xia, Y.; and Ye, Y. A probabilistic generative model for mining cybercriminal networks from online social media. Computational Intelligence Magazine, IEEE, 9, 1 (2014), 31–43.

30. Li, X.; Chen, H.; Zhang, Z.; Li, J.; and Nunamaker Jr., J.F. Managing knowledge in light of its evolution process: An empirical study on citation network-based patent classification. Journal of Management Information Systems, 26, 1 (2009), 129–154.

31. Lu, Y.; Polgar, M.; Luo, X.; and Cao, Y. Social network analysis of a criminal hacker community. Journal of Computer Information Systems, 51, 2 (2010), 31–41.

32. Ma, X.; Khansa, L.; Deng, Y.; and Kim, S.S. Impact of prior reviews on the subsequent review process in reputation systems. Journal of Management Information Systems, 30, 3 (2013), 279–310.

33. Mahmood, M.A.; Siponen, M.; Straub, D.; and Rao, H.R. Moving toward black hat research in information systems security: An editorial introduction to the special issue. MIS Quarterly, 34, 3 (2010), 431–433.

34. Manning, C.D., and Klein, D. Optimization, Maxent Models, and Conditional Estimation without Magic. In Proceedings of the 2003 Conference of the North American Chapter of the Association for Computational Linguistics on Human Language Technology: Tutorials,Volume 5. Edmonton, Canada: Association for Computational Linguistics, 2003, pp. 8–8.

35. McCallum, A.K. Mallet: A machine learning for language toolkit. (2002). Available at: http://mallet.cs.umass.edu.

36. Motoyama, M.; McCoy, D.; Levchenko, K.; Savage, S.; and Voelker, G.M. An analysis of underground forums. In Proceedings of the 2011 ACM SIGCOMM Conference on Internet Measurement Conference. New York: ACM Press, 2011, pp. 71–80.

37. Nunamaker, J.F. Jr.; Chen, M.; and Purdin, T.D.M. System development in information systems research. Journal of Management Information Systems, 7, 5 (1990), 89–106.

38. Nunamaker, J.F. Jr.; Derrick, D.C.; Elkins, A.C.; Burgoon, J.K.; and Patton, M.W. Embodied conversational agent-based kiosk for automated interviewing. Journal of Management Information Systems, 28, 1 (2011), 17–48.

39. Odabas, M.; Breiger, R.; and Holt, T.J. Toward an economic sociology of online hacker communities. In Twenty-Seventh Annual Meeting. London, England: Society for the Advancement of Socio-Economics. 2015.

40. Peretti, K. Data breaches: What the underground world of carding reveals. Santa Clara Computer and High Tech. L.J., 25 (2008), 375–413.

41. Png, I.P.L., and Wang, Q.-H. Information security: Facilitating user precautions vis-à- vis enforcement against attackers. Journal of Management Information Systems, 26, 2 (September 2009), 97–121.

42. Radianti, J. A study of a social behavior inside the online black markets. In R. Savola, M. Takesue, R. Falk, and M. Popescu (eds.). 2010 Fourth International Conference on Emerging Security Information, Systems and Technologies. Venice: IEEE, 2010, pp. 189–194.

43. Romano, N.C. Jr.; Donovan, C.; Chen, H.; and Nunamaker Jr., J.F. A methodology for analyzing web-based qualitative data. Journal of Management Information Systems, 19, 4 (2003), 213–246.

44. Sack, W. Conversation map: An interface for very-large-scale conversations. Journal of Management Information Systems, 17, 3 (2000), 73–92.

45. Singh, P.V.; Sahoo, N.; and Mukhopadhyay, T. How to attract and retain readers in enterprise blogging? Information Systems Research, 25, 1 (March 2014), 35–52.

46. Socher, R.; Perelygin, A.; Wu, J.Y. et al. Recursive deep models for semantic compositionality over a sentiment treebank. In D. Yarowsky, T. Baldwin, A. Korhonen, K. Livescu, and S. Bethard (eds.). Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP), Seattle, Washington, 2013, pp. 1631–1642.

47. Taboada, M.; Brooke, J.; and Tofiloski, M. Lexicon-based methods for sentiment analysis. Computational Linguistics, 37, 2 (2011), 267–307.

48. United States Department of Homeland Security. U.S. Secret Service arrests one of the world’s most prolific traffickers of stolen financial information. 2014. Available at: https:// www.dhs.gov/news/2014/07/07/us-secret-service-arrests-one-worlds-most-prolific-traffick ers-stolen-financial

49. United States Department of Justice. Five indicted in New Jersey for largest known data breach conspiracy. 2013. Available at: https://www.justice.gov/opa/pr/five-indictednew-jersey-largest-known-data-breach-conspiracy

50. Verizon and Verizon Business. 2014 Data breach investigations report. Verizon Business Journal (2014), 1–60.

51. Wang, Q.; Yue, W.; and Hui, K. Do hacker forums contribute to security attacks? In M. J. Shaw, D. Zhang, and W.T. Yue (eds.). E-Life: Web-Enabled Convergence of Commerce, Work, and Social Life, Lecture Notes in Business Information Processing, vol 108. Shanghai: Springer, 2011, pp. 143–152.

52. Wu, L. Social network effects on productivity and job security: Evidence from the adoption of a social networking tool. Information Systems Research, 24, 1 (2013), 30–51.

53. Yip, M.; Shadbolt, N.; and Webber, C. Why forums? An empirical analysis into the facilitating factors of carding forums. In H. Davis, H. Halpin, and A. Pentland (eds.). Proceedings of the 5th Annual ACM Web Science, Paris, France, 2013, pp. 453–462.

54. Zhang, X., and Li, C. Survival analysis on hacker forums. In K.R. Lang and W.T. Yue. (eds.). SIGBPS Workshop on Business Processes and Service, Milan, Italy, 2013, pp. 106–110.

55. Zhang, X.; Tsang, A.; Yue, W.T.; and Chau, M. The classification of hackers by knowledge exchange behaviors. Information Systems Frontiers, 17, 6 (2015), 1239–1251.

56. Zhao, Z.; Ahn, G.; Hu, H.; and Mahi, D. SocialImpact: Systematic analysis of underground social dynamics. In S. Foresti, M. Yung, and F. Martinelli (eds.). Computer Security – ESORICS 2012. ESORICS 2012. Lecture Notes in Computer Science, vol 7459. Pisa: Springer, 2012, pp. 877–894.
