---
otero_id: 19790
otero_key: "6FUH5BCB"
title: "Job satisfaction and employee turnover determinants in Fortune 50 companies: Insights from employee reviews from Indeed.com"
authors: "Bishal Sainju; Chris Hartwell; John Edwards"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113582"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Job satisfaction and employee turnover determinants in Fortune 50 companies: Insights from employee reviews from Indeed.com

Bishal Sainju <sup>a</sup>, Chris Hartwell <sup>b</sup>, John Edwards

<sup>a</sup> Dept. of Computer Science, Utah State University, Logan, UT, United States of America

<sup>b</sup> John M. Huntsman School of Business, Utah State University, Logan, UT, United States of America

## A R T I C L E I N F O

Keywords: Topic modeling Data mining Latent Dirichlet allocation Employee satisfaction

## A B S T R A C T

An important aspect of human resource management is understanding employees’ values, motivations, and factors of satisfaction. Relationships between employee satisfaction, values, positivity and negativity, employee retention, and industry allow human resource managers to make decisions on employee recruitment techniques and budgets, employee retention efforts, and even company image initiatives. Traditional methods for identi fying employee values, job satisfaction, and linkages to important company outcomes are through employee entrance/exit surveys, annual evaluations, and informal interactions. In recent years, companies and researchers have begun to take advantage of the increasing ubiquity of online reviews, including unstructured text responses. In this paper we explore 682.176 emplovee reviews of Fortune 50 companies from Indeed.com using Structural Topic Modeling (STM) to identify salient aspects in employee reviews and automatically infer latent topics that are salient factors related to employee satisfaction. We compare these topics with the five facets of the Job Descriptive Index (JDI) that are traditionally used to measure job satisfaction among human resource experts. We conduct further analysis comparing comments of current vs. former employees. Results suggests that management may be an important salient factor in employee satisfaction and turnover, as it is consistently mentioned by current and former employees in both positive and the negative comments. Similarly, monetary benefits are mentioned as a negative by former employees, but as a positive for current employees. Furthermore, we examine topic differences by industry sector and find that retail emplovees frequently mention Pay and Benefits and Length of Breaks, whereas technology sector employees were more concerned with Work-Life Balance. Our results can be used to support company behavioral management decision makers to conceive and evaluate initiatives intended to enhance employee satisfaction. Furthermore, our techniques, including the visualization of topic composition and quality, are generalizable to any setting that uses topic discovery from unstructured text, such as customer reviews, social media posts, and critic reviews, especially when comparing topics across entities.

## 1. Introduction

Employee job satisfaction is one of the most researched topics in management literature, and is an important human factor affecting a company’s operating effectiveness and financial performance. Thus, it is important to understand and analyze these satisfaction aspects well to inform effective organizational decision making. While examination of job satisfaction has a long history in the literature, measurement of job satisfaction tends to be limited to employee surveys, often administered by organizational representatives or academic researchers. This project moves beyond traditional means of employee surveys and instead looks at proactive employee comments. This research uses online employee review comments found on Indeed.com (hereafter referred to as Indeed) to extract latent satisfaction categories in order to better understand salient factors affecting employee job satisfaction. Some implications for retention and turnover are suggested by contrasting such factors be tween current and former employees, and comparisons by industry are also discussed. This paper also discusses novel topic visualizations that aid in evaluation and interpretation of latent topics.

## 1.1. Motivation

The primary motivation for this research is the plethora of oppor tunities that online review sites like Indeed provide for the companies to discover new and latent satisfaction aspects that companies can utilize in order to make important decisions that direct effective use of human capital and positively impact organizational outcomes.

Traditional methods for measuring job satisfaction, like question naires and surveys, provide limited capabilities as the user provides their opinions on a limited set of topics typically developed and delivered by the employer. However, an online platform like Indeed contains millions of free-form employee reviews that can be analyzed to extract unre stricted critique on a variety of topics, which may allow for a truer gauge of employee job satisfaction.

Also, with increasing computational resources, topic modeling al gorithms like Structural Topic Modeling (STM) can be leveraged to mine large corpora of textual data. Thus, thousands of employee reviews can be analyzed with relative ease.

In addition to studying salient job satisfaction factors, the focus of this research extends to employee retention and turnover, motivated by a desire to better understand factors that may influence employee retention and turnover and perhaps lessen the costly consequences that turnover incurs to the firms. The availability of first-hand online infor mation from both current and former employees likely provides useful information that helps employers better understand some of the salient factors that influence employee retention (positive feedback from cur rent employees) and turnover (negative feedback from former employees).

Also, we further investigate the sector-wise and company-wise topic differentiation on both positive and negative feedback, thus demon strating to employers one way to evaluate and analyze their company’s comparative satisfaction aspects in a sleek and discrete manner. This could help companies compare different satisfaction facets with competition within their industry sector, and provide perspective on what factors may enhance their employees’ satisfaction and reduce turnover, in turn driving company performance.

## 1.2. Contribution

In this paper we make the following contributions:

• We use STM to mine latent job satisfaction topics in the large corpus of employee reviews (Section 4.1).

• We present a visualization that allows analysts to quickly grasp the composition and quality of a topic and compare composition and quality across topics (Sections 4.1.1–4.1.2).

• We draw upon and compare against the most ubiquitous job satis faction framework, the Job Descriptive Index (JDI) [30], but also discover novel job satisfaction aspects that provide additional breadth and depth to the concept of job satisfaction (Section 4.1.3).

• We present a visualization that allows a person to clearly distinguish between positive and negative salient factors related to dissatisfac tion and satisfaction, and also distinguish between former and cur rent employees on satisfaction factors, allowing a conceptual understanding of what drives employee turnover (Section 4.1.4).

• Finally, we implement a method to compare and analyze company wise and sector-wise topic contributions, thus providing compari sons across sectors and within each sector’s companies, regarding common positive and negative job satisfaction facets (Section 4.2).

## 2. Background & related work

## 2.1. Employee job satisfaction and job descriptive index (JDI)

Employee job satisfaction is defined as the “positive emotional state resulting from the appraisal of one’s job or job experience” (p. 1304)

[19]. Job satisfaction is an important correlate of individual employee performance [10,12], employee turnover [29], and organizational suc cess $[ 6 , 2 0 ]$ . Early job satisfaction research suggested a wide variety of methods for gathering job satisfaction data, such as questionnaires, in terviews, rank order studies, sentence completion tests, and critical incident techniques [5]. However, in a vast majority of job satisfaction research, employee surveys have been the main method used to evaluate job satisfaction [11,14,33]. Of these, the Job Descriptive Index (JDI) is the most common measure, and has demonstrated adequate reliability and validity [14]. The JDI comprises five facets, including satisfaction with: coworkers, the work itself, pay, opportunities for promotion, and supervision. While these facets have shown good independence [28], some research has shown that job satisfaction may be more complex, and breaking job satisfaction into more than five dimensions may be appropriate [35]. Thus, the JDI and other facet-level measures of job satisfaction may omit important variables that play an important role in overall job satisfaction [27].

In addition to the potential for excluding important variables that factor into job satisfaction, there are other drawbacks to the JDI and similar measures. These types of survey methods have limited valida tion, are restricted to a relatively small set of topics/questions, and demonstrate large amounts of method and error variance [3,14]. Perhaps most problematic is that these surveys do not attempt to identify omitted factors that may influence job satisfaction by gauging em ployees’ independent thoughts. Instead, employees only provide ratings on the previously developed survey items. Finally, although employees are often told their survey responses are anonymous, their answers may still be biased by social desirability based on fears of repercussions when the survey is developed, delivered, and/or sponsored by their employer [23].

Job sites like Glassdoor.com and Indeed.com provide outlets for em ployees to proactively express their opinions about their current and former jobs anonymously and in an open-ended fashion, thus allowing employees’ opinions to cover a wide range of subjects, rather than a restricted set of topics. This allows the employees to express a much broader and unfiltered opinion of their employers. One more advantage that these platforms have is that employees who have left the company can also leave their comments, thus potentially highlighting dissatis faction factors that may have caused them to leave their previous employer. Online satisfaction ratings have demonstrated good construct validity in prior research [16].

Indeed allows employees to provide overall satisfaction ratings, which gives a general view of their job experience with the company. Users can also rate in 5 different dimensions: i) Work-Life Balance, ii) Compensation / Benefits, iii) Job Security / Advancement, iv) Man agement, and v) Culture, thus allowing further depth. Some of these five factors are similar to the facets of the JDI [30], such as satisfaction with pay, opportunities for promotion, and supervision. Finally, Indeed users can provide specific comments about the pros and cons of their current and former jobs. These free-form comments provide insights about what employees see as the most salient positive and negative aspects of their jobs, and our research focuses on these comments in an attempt to use clustering and job modeling techniques to identify positive and negative factors of job satisfaction, and to see whether the emerging clusters match the dimensions of the JDI.

We separately consider (and compare) employees’ free-form com ments regarding the pros and cons of their employment, because the salient factors in job satisfaction may not necessarily be the same salient factors in job dissatisfaction [1,4,7,8]. Because users self-identify as current or former employees, we also examine what aspects may relate to retention (the pros identified by current employees) and turnover (the cons identified by former employees). This is in line with previous research, which has demonstrated that job satisfaction is a salient factor influencing turnover [9,15,22,29,32]. Finally, we analyze the data by company and industry to examine whether salient pros and cons vary by industry.

## 2.2. Topic modeling

Topic modeling is a type of statistical modeling for discovering the abstract “topics” that occur in a collection of documents. A document can be a part of multiple topics, similar to fuzzy clustering (soft clus tering), in which each data point belongs to more than one cluster with some membership probability.

The Structural Topic Model (STM) [26] is a general framework for topic modeling with document-level covariate information. The cova riates can improve inference and qualitative interpretability and are allowed to affect topical prevalence, topical content or both. STM is basically an extension of LDA, incorporating the additional information about the structure of the corpus into the model by altering the prior distributions to partially pool information among similar documents.

STM provides a general way to incorporate corpus structure or document metadata into standard topic model. In our case, the docu ment metadata is Employee Status (whether the review was written by a current or former employee). Using STM we can observe how topical prevalence varies on the basis of co-variate information by inclusion of interest into the prior distributions for document-topic proportions and topic-word distributions. For example, using STM, we can observe what topics “Former Employees” are talking about most versus what topic “Current Employees” are talking about.

STM looks for patterns of co-occurences and makes guesses about sets of themes. Passing through each document it first randomly assigns probability of a document containing particular theme (“topic”) among various topics and then iterates to improve the classification of the probability of document belonging to one of these hypothetical topics. At the end, we get topic-term and document-topic distribution matrices.

1. Document-Topic Distribution: A probability matrix that gives us the probability value of any particular topic belonging to a particular document. For a given document, the probability over all topics sums to 1.

2. Topic-Term Distribution: A probability matrix that gives us the prob ability of a particular term belonging to a particular topic, defining a topic. The probability of all terms for a topic sums to 1.

## 2.3. Related work

Several studies have applied text mining approaches to online employee reviews. Luo et al. [20] used Glassdoor’s employee reviews to build a model which found the correlation between employee satisfac tion and company performance. Lee and Kang [18] performed topic modeling using LDA by adopting n-gram technique on the employee reviews obtained from Glassdoor.com. They then conducted dominance analysis to examine the relative importance of job factors. They found that culture and value, and senior management had the highest influence on both retention and turnover groups. Similarly, Jung and Suh [13] used LDA to extract job satisfaction factors from jobplanet.co.kr. They then measured sentiment and importance of each job satisfaction factor at industry, company, group, and chronological levels, using the domi nance and correspondence analysis. They found that Senior Management and Benefit and Compensation had the highest importance on overall job satisfaction. Stamolampros et al. [31] used 297,933 online employee reviews from US tourism and hospitality firms to study the determinants of job satisfaction and emplovee turnover. They found that leadershir and cultural values are better predictors of high employee satisfaction, while career progression is a critical predictor of employee turnover.

In our work we first perform comprehensive text analysis to extract latent satisfaction factors, and distinguish these factors between former and current employees, providing a basis to infer employee turnover factors. Prior works had only used LDA, which does not support cova riates, as a means to extract satisfaction factors. In our research we distinguish between factors dominant in former versus current em ployees by employing STM. Similarly, we also identify what factors are dominant across which sector and which company in that sector contributed to such dominance, which helps us compare topics across companies and sectors to a degree not achieved in prior work.

## 3. Data and methods

## 3.1. Data collection

Indeed claims to be “the 1 job site in the world with over 25 million unique visitors every month” (https://www.indeed.com/about). With its easy-to-use user interface and extensive features, it has become one of the best platforms for the employees to express their opinions regarding the companies that they work for (current employees) or that they previously worked for (former employees). At 320 million, Indeed has a substantial number of employee reviews available.

For this study, we focused on Indeed’s employee reviews of Fortune 50 companies, with permission from Indeed to gather and analyze the data. The Fortune 500 (https://fortune.com/fortune500) is an annual list compiled and published by Fortune magazine that ranks the 500 largest United States corporations by total revenue for their respective fiscal years. The list includes publicly held companies, along with pri vately held companies for which revenues are publicly available. In this study, only Fortune 50 companies were used in order to keep data analysis manageable for this initial investigation.

## 3.2. Data preprocessing

We gathered the following information from Indeed: “Review Title”, “Reviewer Job Status”, “Review Text”, “Pros Text”, “Cons Text”, and “Ratings” - both overall ratings and the five sub-ratings Work-Life Bal ance, Benefits, Job Advancement, Management, and Culture. Because this study is concerned with understanding the salient positive and negative aspects related to job satisfaction, we focused on the “Pros Text” and “Cons Text” in our analyses. We gathered 344,573 pro reviews and 330,544 con reviews for a total of 675,117 reviews. For each of the Fortune 50 companies, the following steps were taken for both the positive (pro) feedback and negative (con) feedback (see Fig. 1 for an example of processing):

1. Data Cleaning: Data cleaning was done to remove the URL, @ men tions, hashtags, punctuation marks, and letter repititions.

2. Upper to Lowercase: Each of the terms was lowercased.

3. Tokenization: Each of the documents (reviews) was tokenized.

4. Stop Word Removal: Stop words were removed from each of the documents.

<table><tr><td>Review_Text</td><td>Processed_Texts</td><td>Tokenized_Texts</td></tr><tr><td>Free drinks, paid time, overtime</td><td>drink free overtim paid time free_drink paid_t...</td><td>[drink, free, overtim, paid, time, free_drink,...</td></tr><tr><td>On your own, flexible, can keep job even worki...</td><td>flexibl month time flexibl_time</td><td>[flexibl, month, time, flexibl_time]</td></tr><tr><td>Amazing health benefits, Ot, prizes during cer...</td><td>amaz benefit health ot prize time health_benefit</td><td>[amaz, benefit, health, ot, prize, time, healt...</td></tr></table>

Fig. 1. Text preprocessing.

5. Stemming: Stemming was done on each of the tokens using the Porter Stemmer algorithm.

6. N-Gram Creation and Addition: Bigrams and Trigrams were generated using words that appeared together and added to the document.

7. Stop Word Removal: Stop words were again removed after the text had been stemmed and bigrams and trigrams generated.

8. Pruning: Terms that did not appear in the top 1000 unigrams, top 500 bigrams, or top 300 trigrams for each company were removed.

We randomly sampled 1000 reviews from each company for both the positive (pro) and the negative (con) feedback, so that companies with the largest volume of reviews (e.g., Walmart) would not dominate the results. For companies with fewer than 1000 reviews, we used all available reviews. The fewest reviews for a single company was 125. All reviews from each company were merged to form two large groups, one for the positive text and one for negative text. After this, each of the documents that had less than 3 terms were removed, and modeling was done on the remaining data. Thus, of the 1000 original reviews for each company, some documents didn’t have enough terms and were discarded.

## 3.3. Topic modeling

Fig. 2 shows various steps of the proposed model, which consists of Data Collection and Data Pre-processing (discussed in Sections 3.1 and 3.2, respectively), Topic Modeling (discussed in this section), and Topic Evaluation (discussed in 3.4).

The main purpose of Topic Modeling in our research analysis is to discover the most widely expressed topics in the employee reviews across Fortune 50 companies. This method of discovering latent topics in the employee reviews helps us discover latent topics that might not have been previously considered using other methods. The traditional method of figuring out which metrics best influence employee satis faction is limited because surveys and questionnaires rely on fixed sets of dimensions to quantify employee satisfaction. Indeed also provides em ployees dimensions that can be quantitatively rated (and an overall rating), but the employees are also able to express their reviews in freeform text as they choose.

In addition to analyzing these free-form comments, we take an additional step to compare and contrast differences between former employees and current employees, thus reflecting upon possible salient factors related to employee turnover in Fortune 50 companies. To un derstand the salient factors that may influence employees to remain at or leave a company, we introduce a covariate of Employee Status (Former vs. Current), using the STM package in the R programming language.

For STM, various metrics like Semantic Coherence, Exclusivity, and Held-Out Likelihood were used to evaluate the most efficient number of topics to model our dataset.

![](/api/attachments/6FUH5BCB/fulltext/images/9085b3008608d0499a26d2aff4ae22108a4d289ff1ef5634cb54334444aa5a22.jpg)  
Fig. 2. Proposed methodology.

We also processed the document-topic and topic-term probability matrices, which were the output from our model, to analyze industry wise topic proportion and, in each industry, company-wise topic contribution, which helps us compare topic distributions across various industries and companies.

## 3.4. Topic evaluation

The two topic quality evaluation metrics that will be used in this paper are topic coherence and exclusivity, each discussed individually below.

## 3.4.1. Topic coherence

Semantic coherence is a criterion developed by Minmo and col leagues [21] and is closely related to pointwise mutual information [17]. It is maximized when the most probable words in a given topic frequently co-occur together. Minmo et al. [21] shows that semantic coherence correlates well with the human judgment of topic quality. Formally, let $D ( \nu _ { i } , \nu _ { j } )$ be the number of times that words v and v appear together in a document. The semantic coherence for topic k is given in [26] as

$$
C _ {k} = \sum_ {i = 2} ^ {M} \sum_ {j = 1} ^ {i - 1} \log \left(\frac {D (v _ {i} , v _ {j}) + 1}{D (v _ {j})}\right)\tag{1}
$$

where, M is the M most probable words in topic k, and we set this value to 30 in our analysis.

High semantic coherence can be easily obtained by having a few topics dominated by very common words [25]. Thus, other metrics need to be taken into consideration for evaluating various topic models.

Since these scores are log probabilities, they are negative. Large negative values indicate words that don’t co-occur often; values closer to zero indicate that words tend to co-occur more often. For each model, an overall coherence score is calculated by calculating the topic coherence for each topic individually and then averaging these values.

## 3.4.2. Exclusivity

There are various ways to identify the theme of a topic. However, the most general way of defining a topic’s core concept is using the words with the highest probabilities. However, it is not always sufficient that the most probable terms in a topic are the best definer of a topic, as the terms may commonly occur in the corpus, and commonly occur in other topics as well. So it is also important to understand whether the most probable terms in the topic in question are relatively exclusive to that particular topic only, and not common in other topics.

Exclusivity is the measure of the extent to which the top words for a topic do not appear as top words in other topics – i.e., the extent to which its top words are” exclusive” to a given topic. The value is essentially the average, over each top word, of the probability of that word in the topic divided by the sum of the probabilities of that word in all topics. The FREX metric [2] is used to measure the exclusivity in a way that balances word frequency. FREX is the weighted harmonic mean of the word’s rank in terms of exclusivity and frequency, and is given in [26] as:

$$
\mathrm{FREX} _ {k, v} = \left(\frac {\omega}{\operatorname{ECDF} \left(\beta_ {k , v} / \sum_ {j = 1} ^ {K} \beta_ {j , v}\right)} + \frac {1 - \omega}{\operatorname{ECDF} \left(\beta_ {k , v}\right)}\right) ^ {- 1}\tag{2}
$$

where ECDF is the empirical CDF, ω is the weight which is set to.7 to favor exclusivity, k ∈ K is the $k ^ { \mathrm { { t h } } }$ topic, v is the word under consideration and β is the topic word distribution for this topic.

The cumulative distribution function (CDF) of a real-valued random variable X, evaluated at x, is the probability that X will take a value less than or equal to x. Whereas, empirical cumulative distribution function (ECDF) is the probability distribution obtained from the sampled dataset of the sample, instead of the population.

Both term frequency and term exclusivity are informative: nonexclusive words are less likely to carry topic-specific content, while infrequent words occur too rarely to form the semantic core of a topic.

Topic coherence and exclusivity are both calculated for each topic of a model and then averaged over all the topics to get the score for the model. Models with higher exclusivity and semantic coherence are generally preferred.

## 4. Results

We had an average of 6891 pro reviews, and 6610 con reviews of each company. Walmart had the highest number of reviews of 159,328, while Berkshire Hathaway had the lowest number of reviews of 125. The top 10 lowest number of reviews is shown in Fig. 3a. Most of the com panies had more than 1000 reviews (pro and con combined).

After preprocessing the dataset, we tokenized each review, and only those documents that had more than 3 tokens in it were retained, which reduced our total review document size from 675,117 to 215,452. The top 10 lowest number of reviews after preprocessing is in Fig. 3b.

Most of the companies still had a substantial number of reviews. Overall, there were 107,954 pro documents, and 107,498 con docu ments. We then sampled 1000 pro and 1000 con reviews from each of the Fortune 50 companies (using all reviews for companies with less than 1000 reviews), so as to distribute the effect of one company over powering our topic model. The pro dataset had 33,624 reviews while the con dataset had 32,988 reviews. Review length distributions in Fig. 4 show that the large majority of preprocessed reviews had fewer than 10 tokens. The lengthiest topic is 72 tokens long after preprocessing.

## 4.1. Structural topic modeling (STM)

To observe the effect of the covariate (in our case Job Status being the covariate), STM was applied on both pro and con reviews separately, as well as on pro and con reviews combined.

Model selection was done using the diagnostic plot as shown in Fig. 5 using various evaluation metrics discussed earlier in Section 3.4. We used Eq. (2) to compute the semantic coherence of the model, with M (the M most probable words in topic k) set as 30. Comprehensive diagnosis with various diagnosis metrics are shown in Appendix A. A 16- topic model for pro and 17-topic model for con were chosen qualitatively using the elbow method: in both the pro and con cases, increase in ex clusivity and decrease in coherence start leveling off at around 16 or 17 topics. The resulting models are presented in Figs. 6 and 7 for pros and cons respectively.

Num Reviews of Companies (Ascending)  
![](/api/attachments/6FUH5BCB/fulltext/images/aee152868b7254baa1f827e3d2e6f58700b499932b214e794d02fed5262ca5fb.jpg)  
(a) Before Preprocessing

## 4.1.1. Pros

The stacked barplot in Fig. 6 indicates the dominance of specific terms within each topic. In other words, each bar in the plot for each topic is a composite of multiple terms, the size of each term bar repre sents the probability of the term being in a particular topic. For example, Topic 3 is dominated by the “pay” and “benefit” terms, which together account for nearly 60% of the probability. Hence, with this graph, we can easily observe what a particular topic is about by analyzing the term probabilities. We have included the top 10 terms for each topic, as these dominant terms are most likely to most clearly convey the topic mean ing. The rest of the terms in each topic are grouped together and designated as “others”. We qualitatively established a.5 threshold as a cutoff to help differentiate topic quality. If the top 10 terms compose a total of more than.5 probability, these terms dominate a majority of the topic, and the topic is likely to be strongly interpretable. If the ten topics do not sum to at least.5 probability, the topic should be viewed with some caution, and may be considered weaker. Because of the balance between exclusivity and coherence, terms can appear in multiple topics. In most cases, these duplicate terms appear with very low probability and are in the “others” grouping. But, in some cases, terms can appear with reasonably high probability in multiple topics, such as the term lunch appearing in topics 5 and 6. Duplicate terms are cross-topic terms that may be advantageous to study because, in practice, addressing a single cross-topic term may result in positive effects across more than one area.

Looking at the bar plots for pro in Fig. 6 identifies that 13 of the 16 topics (81.25%) are above the.5 threshold. Some clearly defined topics come out from this analysis. For the pro model, topics like: Fun people (Topic 1), Monetary benefits (Topic 3), Friendly co-workers (Topic 4), Free

Num Reviews of Companies after Preprocessing (Top 10 Lowest)  
![](/api/attachments/6FUH5BCB/fulltext/images/2e4f550c4ddbba62fe53f42c659e04b5e493faf5735a30e51be53ba869921d3e.jpg)  
(b) After Preprocessing  
Fig. 3. Total number of reviews in each company.

Decision Support Systems xxx (xxxx) xxx

![](/api/attachments/6FUH5BCB/fulltext/images/86cee30b5896eaa9b20ef5391846d459800c19526f72d62b4947ef322827e202.jpg)  
(a) Pro

![](/api/attachments/6FUH5BCB/fulltext/images/556d6ae42009d0aaab568e0e35b76141beaeab0d89e48e2feb097683ba90d6b2.jpg)  
(b) Con  
Fig. 4. Document length distribution.

![](/api/attachments/6FUH5BCB/fulltext/images/6e4dfd99ea7327e8abc5a80050f2966252c76f9a52ee6a100199b75743a44ccc.jpg)  
Diagnostic Plot (Pro-STM

![](/api/attachments/6FUH5BCB/fulltext/images/327fff9361f6f9fa3bb73581be60be10e5e23db02e3f5a835ed5d66de32583a4.jpg)  
(a) Pro  
Diagnostic Plot (Con-STM

![](/api/attachments/6FUH5BCB/fulltext/images/0f552c39de993e3dcdfc9c1c7cb97f08ea4ef5b7cace76e38b8d14966d6fdd87.jpg)

![](/api/attachments/6FUH5BCB/fulltext/images/d30c2d3ab4efbc45cf14bb11be2de90c459260e9eb9799c9ba79af1376c0b6e0.jpg)  
(b) Con  
Fig. 5. Diagnosis of topic quality for different numbers of topics using STM.

lunch (Topic 5), Sufficient breaks (Topic 6), Paid time off (Topic 10), and Flexible schedule (Topic 16) emerge. Some topics comprise two interre lated sub-topics, such as Management & work environment (Topic 7), Free food & work-life balance (Topic 8), Work teams & work-life balance (Topic 12), and Health insurance & fast-paced work (Topic 15). Using the.5 threshold, topics 2, 9, and 14 are the relatively weak topics.

4.1.2. Cons

Fig. 7 highlights the negative comments made by employees about various aspects, such as Poor work-life balance (Topic 1), Poor manage ment (Topic 2), Stressful environment (Topic 8), Lack of advancement (Topic 9), Short breaks (Topic 14), Work schedule (Topic 15), and Low pay (Topic 16). As with the pro topics, some of the con topics also cover two interrelated sub-topics. These include Customers & work-life balance (Topic 7) and Hard work & low pay (Topic 10). Compared to the “pro” model, there are many lower quality topics, as only eight of 17 topics (47%) are above the.5 threshold with the top ten terms.

![](/api/attachments/6FUH5BCB/fulltext/images/3fd41bce060a1d2a81780f4407d05796b0677e315f9e2488ae554b75aedd2199.jpg)  
Fig. 6. Top 10 terms across each topics (Pro) using STM. The dotted line indicates 50% probability.

![](/api/attachments/6FUH5BCB/fulltext/images/41a6d96b8926cd4ce023727da0b14d18ee7565c20772cff26a4342a36362fb34.jpg)  
Fig. 7. Top 10 terms across each topics (Con) using STM. The dotted line indicates 50% probability.

Our visualizations in Figs. 6 and 7 follow the validation approach of Munzer [24], which splits validation into four levels: domain, abstrac tion, encoding, and algorithm, of which the first three apply in this case. We claim that domain is valid, as the chart addresses topic quality. Abstraction is reliable: topics’ term probabilities are partitions of unity and thus can be visualized using stacked bar charts with identical heights for each topic. Encoding is also reliable because the terms are categorical attributes and the color hue channel is both expressive and highly effective [24,34]. Similar arguments justify Figs. 9-11.

## 4.1.3. Comparison with JDI

Overall, we obtained many cohesive, unique topics from the STM model. In comparison with prior job satisfaction research, our topic encompass all five JDI facets, even highlighting potentially important sub-topics. Our computer-generated topics also include some important considerations that are not specifically captured in the JDI. The com parison between the JDI and STM topics (both pros and cons) are shown in Table 1.

Satisfaction with coworkers was demonstrated by topics focused on fun (or difficult) people, nice coworkers, and work teams. Satisfaction with the work itself was mainly manifest in topics regarding breaks, work pace, work schedules, and stress. Satisfaction with pay was broadened to also include benefits (both general and specific), including free food, employee discounts, and health insurance. Satisfaction with opportu nities for promotion came across in nearly identical terms (i.e., training, development, growth, advancement). Finally, Satisfaction with superviso

## Table 1

Topic Comparison with JDI facets. Topics in bold are higher quality, with the top 10 words accounting for at least 50% of the probability.

<table><tr><td>Job descriptive index facets</td><td>Corresponding Indeed.com Categories (Pro)</td><td>Corresponding Indeed.com Categories (Con)</td></tr><tr><td>Satisfaction with Coworkers</td><td>Pro1: Fun PeoplePro4: Friendly co-workersPro12(a): Work teams</td><td>Con12: Difficult people</td></tr><tr><td>Satisfaction with the Work Itself</td><td>Pro6: Sufficient breaksPro15(b): Fast-paced workPro16: Flexible schedule</td><td>Con6: Short lunch breaksCon7(a): CustomersCon8: High stressCon10(a): Hard workCon11: Changing scheduleCon13: Fast-paced/ overtimeCon14: Short breaksCon15: Work schedule (hours/shift)</td></tr><tr><td>Satisfaction with Pay</td><td>Pro2: Benefits (e.g, cafeteria, gym, tuition reimbursement)Pro3: Monetary benefitsPro5: Free lunchPro8(a): Free foodPro10: Paid time offPro11: Employee discountsPro13: PayPro15(a): Health insurance</td><td>Con5: Time benefitsCon10(b): Low payCon16: Low pay</td></tr><tr><td>Satisfaction with Opportunities for Promotion</td><td>Pro9: Training and development Pro14: Growth opportunities</td><td>Con9: Lack of advancement</td></tr><tr><td>Satisfaction with Supervisor</td><td>Pro7(a): Management</td><td>Con2: Poor management</td></tr><tr><td>Facets not specifically covered in the JDI</td><td>Pro7(b): Work environmentPro8(b): Work-life balancePro12(b): Work-life balance</td><td>Con1: Poor work-life balanceCon3: Business environmentCon4: Poor cultureCon7(b): Work-life balance</td></tr></table>

was highlighted in topics focused on management (both good and bad). One interesting thing to note is the sheer number of topics. While most JDI facets are relatively balanced when looking at pro and con topics, Satisfaction with pay has many more pro topics (eight) than con topics (three). This may highlight the importance of pay and benefits as a salient factor in employees’ positive perceptions. On the other hand, Satisfaction with the work itself has many more con topics (nine) than pro topics (three), which may indicate that negative aspects of the work (short breaks, changing schedules, forced overtime, etc.) may be demotivating and difficult for many employees.

## 4.1.4. Covariate effect (effect of job status on topic distribution)

Fig. 8 provides a graphical depiction of the topic distribution be tween former and current employee. The x-axis is the slope of a linear regression line in a correlation between former/current status and probability of a given topic. The dotted line is the zero effect, and the topics that are close to this line are the topics that do not differ signifi cantly in frequency between former and current employees. The farther a topic falls on the right side, the more it was mentioned by current employees (in comparison to former employees). Similarly, the farther a topic falls on the left side, the more it was mentioned by former em ployees (in comparison to current employees). Note from the magnitude of values between pros and cons that the effect of employee status on which topics are discussed is stronger among pro comments.

Fig. 8a shows that current employees were more often satisfied with Friendly co-workers, Paid time off, and Flexible schedules than former employees, while former employees were more often satisfied with Work-life balance, Free lunch, and Monetary benefits. When it comes to the negative aspect of the job, Fig. 8b shows that current employees were more dissatisfied by aspects like Lack of advancement opportunity and Low pay than former employees. Former employees were more dissatisfied than current employees by factors such as Poor management and Benefits.

## 4.2. Company-wise and sector-wise analysis

Using topics discovered by STM, we qualitatively paired similar pro and con topics and visualized their probabilities across companies and industry sector. Each company’s industry sector was taken directly from the Fortune 500 website. On the right-hand side of Fig. 9, we compare similar pro and con topics from previous analyses that can both be interpreted as focused on Pay. For example, while numerous pro and con topics mention compensation and/or benefits, topics pro13 and con16 are most comparable and focused directly on compensation, as both have “pay” as their strongest contributor. Thus, we compare these topics in Fig. 9, and similar comparisons are made in Fig. 10(length of breaks) and Fig. 11 (work-life balance).

On the left of the figure, we see the distributions of a given topic among companies and sectors. For example, in Fig. 9 we see that about 2% of all appearances of the “pro/Pay” topic in our data are in reviews of McKesson, and over 6% of all “con/Pay” topic appearances are accounted for by three companies in the Financials sector. For clarity, we show only the top three companies contributing to a particular topic for each sector. Sectors with fewer than three companies in the Fortune 50 list are not included. There are two bars for each sector, the blue one indicating topic proportion from the pro comments, and the red one indicating topic proportion from the con comments. Companies are ar ranged in descending order of the topic proportion from bottom to top. Percentages in the figures do not sum to 100% because (a) we have limited our analyses to those sectors with three or more companies, and (b) we have limited our visualization to the top three companies in each sector for each topic. For this analysis we have chosen three common and comparable topics on both pro and con reviews: Pay, Length of break and Work-life balance. This is done as an illustration of how the infor mation can be analyzed and visualized to provide decision-making in formation for companies.

Fig. 9 shows that the Retail sector talks the most about the Pay, on both the positive and negative sides. Employees from Costco, Amazon, and Lowe’s appear to be the most satisfied with the Pay within the Retail sector, while employees from Home Depot, Walmart, and Target appear to be the most dissatisfied with Pay. We see that employees from Apple, Dell, and IBM talk more about Pay, both positively and negatively, than other companies in the Technology sector.

![](/api/attachments/6FUH5BCB/fulltext/images/fd4221fc47f3a9df6789afa0124925713b5b879ae290607367a615fb564a5270.jpg)  
(a) Pro

![](/api/attachments/6FUH5BCB/fulltext/images/583286009aa9d8b9c6c74c33368fd6bf3e34e7d7a9f46f19bab7022721685090.jpg)  
(b) Con

Fig. 8. Marginal effects of employee status (former to current) for the topic distribution of (a) positive and (b) negative aspects of the review text. Numbers in the bracket represent the topic number in corresponding stm model (pro/con) in Figs. 6 and 7.  
![](/api/attachments/6FUH5BCB/fulltext/images/25b3fff196360db49bd811dd3ad3ecd8ef49baf2d516a9d5fdd7a8dbae2c255c.jpg)  
Fig. 9. Sector-wise and company-wise topic distribution for “Pay” topics.

Like the previous figure, Fig. 10 demonstrates that Length of break is a salient factor for employees in the Retail sector, especially compared to employees in other industry sectors. Technology and Telecommunica tions employees seem particularly unconcerned with the Length of break. In Retail, employees from Walmart appear most satisfied with the length of their breaks, while Amazon employees appear the most dissatisfied. Similarly, CVS Health in the Health care sector, and Valero Energy in the

Energy sector appear relatively dissatisfied with break length.

Finally, Fig. 11 shows that Technology sector employees seem the most satisfied by the Work-life balance, led by companies like IBM and Dell. However, there is also dissatisfaction, due to companies like Microsoft and Intel. This analysis also provides insight into what em ployees in the different sectors may care most about. Retail sector em ployees talk mostly about Pay and benefit and Length of break while Technology and Financial sector employees are more interested in Work life balance. This suggests that Retail employers may benefit from focusing more on Pay and benefit and Length of break, while Technology and Financial sector employers may consider Work-life balance issues more in their employee satisfaction initiatives.

![](/api/attachments/6FUH5BCB/fulltext/images/de2a46e337d198ff728f6965212552cc78717edebc8ba539865ce4ee50f09bfa.jpg)  
Fig. 10. Sector-wise and company-wise topic distribution for “Length of break” topics.

![](/api/attachments/6FUH5BCB/fulltext/images/1de7fc0b530ba3fcbbd7b4dc9c8759cfb060ed07bd20b7d3fcf8367b5699a601.jpg)  
Fig. 11. Sector-wise and company-wise topic distribution for “Work-life balance” topics.

## 5. Discussion

In this paper, we present novel approaches for leveraging open source reviews on Indeed.com to extract latent (hidden) satisfaction aspects of the employees in Fortune 50 companies, using STM. We have analyzed salient positive and negative factors for all employees, while also analyzing and comparing factors between current and former employees.

## 5.1. Contributions

Many identified topics were similar to the JDI facets, albeit often more specific. Thus, this project highlights the factors in a particular facet that may contribute most strongly to employee satisfaction or dissatisfaction. For example: Fun People, Friendly Co-workers and Team work were some of the salient aspects that contributed for the satisfac tion of employee with co-workers, while Difficult People dissatisfied them. This information breaks down specific focus areas within the common JDI facets of employee satisfaction, giving decision makers more specific information to allow more a more targeted approach to improving or sustaining employee satisfaction. In the above example, the information could be used to focus hiring on applicants that will effectively work with and positively interact with others. It could also be used to design the work environment to allow more positive employee interactions.

Free food and Sufficient lunch breaks were some of the salient factors that were most commonly identified by employees, which is somewhat surprising since little prior research focuses on these specific factors. We specifically highlight these factors because of their frequent mention in the reviews that we analyzed. This could imply that if the companies focused more on these aspects, they may see gains in employee satis faction. These results also suggest that these specific topics deserve more attention in academic research.

By analyzing sector-wise topic distributions, results indicate that the Work-life balance topic may apply more heavily in Technology and Financial sectors, and Pay may apply more in the Retail industry, indi cating the relative interests of employees in those sectors. In addition, we found that Length of break is also identified frequently by employees in the Retail sector. These results indicate that pay and breaks may be highly salient for retail employees, while employees in other sectors are more focused on other factors, such as personal satisfaction of a job and maintaining positive work-life balance.

Our visualization of topic composition (Figs. 6 and 7), along with our probability-based measure of topic quality (see the 50% threshold in the figures) are generalizable to topic discovery from unstructured text in settings including customer reviews, critic reviews, and social media comments. Our company-wise and sector-wise topic distribution ana lyses are also applicable to these settings, especially when topics need to be compared across attributes. Examples beyond human resource management include targeted advertising for social media platforms, product recommender systems, and critical review aggregation services. And finally, the visualization of topic composition (again, Figs. 6 and 7) can be a way to gain additional intuition into traditional measures of topic quality (e.g. coherence and exclusivity), possibly leading to inno vation in topic quality measurements.

In this paper we have presented two classes of research findings. The first are results from our analysis of Indeed reviews and their application to systems that support decisions in human behavioral management. These results are important in supporting, as mentioned above, decisions in human resource management. We emphasize that our data-driven approach discovers important, latent principles on which to base de cisions. These principles are an important research finding in that they largely support and extend understanding of the Job Descriptive Index (JDI), which, in contrast to a data-driven approach, was developed in an industrial-organizational psychology setting.

The second class of research finding is our methods themselves. Document-level covariates of the reviews (Section 3.3), our novel topic visualizations (Figs. 6-11), and our accumulated probability threshold topic quality measure (Sections 4.1.1 and 4.1.2) are all methods that can be generalized to decision support systems in settings beyond behavioral

## Appendix A. Diagnosis (STM)

management.

## 5.2. Limitations

While this research provides a number of important contributions, in terms of both practical decision making and research methods, it is not without limitations. First, in order to keep the data manageable, we focused this research on reviews from Fortune 50 companies. While the data collected resulted in over 200,000 data points, the generalizability of the salient factors identified by these employees is unknown. Further research should consider expanding data collection to all companies in the Fortune 500, and comparing results with that of mid- and small-sized companies not found on the Fortune 500(e.g., mid- and small-sized companies).

A second limitation is that we are unable to fully understand or empirically test the impact of these salient factors on job behaviors. We theorize that the salient positive categories identified by current em ployees would have a strong positive influence on job satisfaction, employee engagement, and organizational commitment. Similarly, we suggest that the salient negative categories identified by former em ployees are likely drivers that led them to leave the company. However, this study does not allow us to make direct causal implications. Future work should examine the predictive validity of our identified salient factors in driving actual employee behaviors, particularly factors that are more specific than, or altogether different from, the variables typi cally used to measure job satisfaction and employee turnover.

## 5.3. Future work

This research opens the door to new areas of study, some of which were described in the previous section. In addition, analyzing direct correspondence of employee satisfaction factors to positive organiza tional outcomes (e.g., revenue, profits, turnover ratios) could be a fruitful avenue for future research. Further investigation could be done to find the difference in the satisfaction needs between employers in low performing companies and high performing companies. Similarly, other algorithms like hierarchical clustering and other variants of STM can be used to compare resulting models and topics. Finally, job satisfaction research may benefit from drilling down to understand what specific components drive satisfaction of the five general facets, and the JDI may benefit from updating to include other relevant job satisfaction facets like Work-life balance).

## CRediT authorship contribution statement

Bishal Sainju: Conceptualization, Methodology, Software, Data curation, Writing - original draft, Writing - review & editing. Chris Hartwell: Conceptualization, Writing - original draft, Writing - review & editing. John Edwards: Conceptualization, Supervision, Writing - original draft, Writing - review & editing.

![](/api/attachments/6FUH5BCB/fulltext/images/4413ebb4bcaf2b7facd129ad4567b7b87c635c464cbda8174933053320f1e534.jpg)

![](/api/attachments/6FUH5BCB/fulltext/images/7886d217a4c600485ea6c7fec6680ecb21d22032b00daa5b6dedf0ce4493a179.jpg)

![](/api/attachments/6FUH5BCB/fulltext/images/1c4b3787a4a63c04c60f328db2a2600161d1b985b46938b91b70c3b54d28c6d2.jpg)

![](/api/attachments/6FUH5BCB/fulltext/images/7bc274fa58c505c491599fb45cdce7ddc1a0a324f2550315e7c13c79ea61a2ce.jpg)

![](/api/attachments/6FUH5BCB/fulltext/images/b4ca03711acdb1ce98ef21ad2d0b58bf6640e76fd9e1aba797ca34cc1673a132.jpg)  
Fig. A.12. Diagnosis of topic quality for different numbers of topics using STM for pro.

![](/api/attachments/6FUH5BCB/fulltext/images/0281028af72ef870a846a7fe3ac2f1f84d6080a646a5e977e7924e204858d20b.jpg)

![](/api/attachments/6FUH5BCB/fulltext/images/5ca65e918f0f201994e433a8e6a15b68f50f6d70753c16897d53650a07f92347.jpg)

![](/api/attachments/6FUH5BCB/fulltext/images/2fed6401e2e50561d33ccd853c4b71d19b7d343c6d3451ca056df28e401cd674.jpg)

![](/api/attachments/6FUH5BCB/fulltext/images/71002e6aeb7e767cafd5c907fdd2fe1734593f85d2ee1b52164e65b268b4bff5.jpg)

![](/api/attachments/6FUH5BCB/fulltext/images/6ce6ed11f560528456c1d9288b87bf62f1a1de6b4a6f2504a2d3319cb92c33d2.jpg)

Fig. A.13. Diagnosis of topic quality for different numbers of topics using STM for con.  
![](/api/attachments/6FUH5BCB/fulltext/images/91958dcec5f0f74f2d1c465bec12b9d19d3c9e844af2caec15e6a84abb99f9b4.jpg)

## References

[1] Seymour Adler, Self-esteem and causal attributions for job satisfaction and dissatisfaction, J. Appl. Psychol. 65 (3) (1980) 327.

[2] Jonathan M. Bischof, Edoardo M. Airoldi, Summarizing topical content with word International Conference on Machine Learning, ICML’12, Omnipress, Madison, WI, USA 2012 pp. 9-16 JSBN 9781450312851

[3] M. Ronald Buckley, Shawn M. Carraher, Joseph A. Cote, Measurement issues concerning the use of inventories of job satisfaction, Educ. Psychol. Meas. 52 (3) (1992) 529–543.

[4] Marvin D. Dunnette, John P. Campbell, Milton D. Hakel, Factors contributing to job satisfaction and job dissatisfaction in six occupational groups, Org. Behav. Hum. Perform, 2 (2) (1967) 143–174

![](/api/attachments/6FUH5BCB/fulltext/images/d0654381404c3b2f6c6bdf8a36622eaea9cda28754b560cfd92a8d3c6e87e567.jpg)

[5] Glenn P. Fournet. M.K. Distefano Jr., Margaret W. Prver. Job satisfaction: issues

[6] James K. Harter, Frank L. Schmidt, Theodore L. Hayes, Business-unit-leve relationship between employee satisfaction, employee engagement, and business outcomes: a meta-analysis, J. Appl, Psychol, 87 (2) (2002) 268.

[7] Frederick Herzberg, One more time: how do you motivate employees? Harv. Bus. Rev. 65 (5) (1987).

[8] Frederick Herzberg, Bernard Mausner, Barbara Bloch Snyderman, Motivation to Work, Wiley, 1959.

[9] Peter W. Hom, Fanny Caranikas-Walker, Gregory E. Prussia, Rodger W. Griffeth, A meta-analytical structural equations analysis of a model of employee turnover, J. Appl, Psychol, 77 (6) (1992) 890.

[10] Michelle T. Jaffaldano. Paul M. Muchinsky. Job satisfaction and job performance: a meta-analysis, Psychol, Bull, 97 (2) (1985) 251.

[11] Timothy A. Judge, Job satisfaction: Research and practice, in: Industrial and Organizational Psychology: Linking Theory with Practice. 2000.

[12] Timothy A. Judge, Carl J. Thoresen, Joyce E. Bono, Gregory K. Patton, The job satisfaction-job performance relationship: a qualitative and quantitative review. Psychol. Bull. 127 (3) (2001) 376.

[13] Yeonjae Jung, Yongmoo Suh, Mining the voice of employees: a text mining approach to identifying and analyzing job satisfaction factors from online employee reviews, Decis. Support. Syst. 123 (06 2019) 113074, https://doi.org/ 10.1016/i.dss.2019.113074

[14] Angelo J. Kinicki, Frances M. McKee-Ryan, Chester A. Schriesheim, Kenneth P. Carson, Assessing the construct validity of the job descriptive index: a review and meta-analysis, J. Appl. Psychol. 87 (1) (2002) 14.

[15] Eric G. Lambert, Nancy Lynne Hogan, Shannon M. Barton, The impact of job satisfaction on turnover intent: a test of a structural measurement model using a

[16] Richard N. Landers, Robert C. Brusso, Elena M. Auer, Crowdsourcing job satisfaction data: examining the construct validity of glassdoor. com ratings, Personnel Assess. Decision. 5 (3) (2019) 6.

[17] Jey Han Lau, David Newman, Timothy Baldwin, Machine reading tea leaves: Automatically evaluating topic coherence and topic model quality, in: Proceedings of the 14th Conference of the European Chapter of the Association for Computational Linguistics, Association for Computational Linguistics, Gothenburg, Sweden. April 2014. pp. 530–539. https://doi,org/10.3115/v1/E14-1056. URI https://www.aclweb.org/anthology/E14-1056

[18] Jongseo Lee, Juyoung Kang, A study on job satisfaction factors in retention and turnover groups using dominance analysis and lda topic modeling with employee reviews on glassdoor.com, in: ICIS, 2017.

[19] Edwin A. Locke. The nature and causes of job satisfaction, in: Handbook ot Industrial and Organizational Psychology, 1976.

[20] Ning Luo, Yilu Zhou, John Shon, Emplovee satisfaction and corporate performance Mining emplovee reviews on glassdoor.com, in: ICIS. 2016

[21] David Mimno, Hanna M. Wallach. Edmund Talley, Miriam Leenders. Andrew McCallum, Optimizing semantic coherence in topic models, in: Proceedings of the Conference on Empirical Methods in Natural Language Processing, EMNLP ‘11, Association for Computational Linguistics, USA, 2011, pn. 262–272 JSBN 9781937284114

[22] William H. Mobley, Intermediate linkages in the relationship between job satisfaction and emplovee turnover. J. Appl. Psychol. 62 (2) (1977) 237.

[23] Robert H. Moorman, Philip M. Podsakoff, A meta-analytic review and empirical test of the potential confounding effects of social desirability response sets in organizational behaviour research, J. Occup. Organ. Psychol. 65 (2) (1992) 131–149.

[24] Tamara Munzner, Visualization Analysis and Design, CRC press, 2014.

[25] Margaret E. Roberts, Brandon M. Stewart, Dustin Tingley, Christopher Lucas, Jetson Leder-Luis, Shana Kushner Gadarian, Bethany Albertson, David G. Rand, Structural topic models for open-ended survey responses, Am. J. Polit. Sci. 58 (4) (2014) 1064–1082, https://doi.org/10.1111/ajps.12103. URL, https://onlinelibra ry.wiley.com/doi/abs/10.1111/ajps.12103.

[26] Margaret E. Roberts, Brandon M. Stewart, Dustin Tingley, stm: an R package for structural topic models, J. Stat. Softw. 91 (2) (2019) 1–40, https://doi.org 10.18637/iss.v091.i02.

[27] Vida Scarpello, John P. Campbell, Job satisfaction: are all the parts there? Pers. Psychol. 36 (3) (1983) 577–600.

[28] Benjamin Schneider, H. Peter Dachler, A note on the stability of the job descriptive index, J. Appl. Psychol. 63 (5) (1978) 650.

[29] Parbudyal Singh, Natasha Loncar, Pay satisfaction, job satisfaction and turnover intent, Relations industrielles/industrial relation 65 (3) (2010) 470–490.

[30] Patricia Cain Smith, Lorne M. Kendall, Charles L. Hulin, The Measurement of Satisfaction in work and Retirement: A strategy for the study of attitudes, Rand McNally, 1969.

[31] Panagiotis Stamolampros, Nikos Korfiatis, Konstantinos Chalvatzis Dimitrios Buhalis, Job satisfaction and employee turnover determinants in high contact services: insights from employees’online reviews, Tour. Manag. 75 (2019) 04, https://doi.org/10.1016/j.tourman.2019.04.030.

[32] Robert P. Tett, John P. Meyer, Job satisfaction, organizational commitment, turnover intention, and turnover: path analyses based on meta-analytic findings Pers. Psychol. 46 (2) (1993) 259–293.

[33] N. Van Saane, Judith K. Sluiter, J.H.A.M. Verbeek, M.H.W. Frings-Dresen, Reliability and validity of instruments measuring job satisfaction—a systematic review, Occup. Med. 53 (3) (2003) 191–200.

[34] Colin Ware, Information Visualization: Perception for Design, Morgan Kaufmann, 2019.

[35] Samuel J. Yeager. Dimensionality of the job descriptive index. Acad, Manag, J. 24 (1) (1981) 205–212

Bishal Sainju is a Masters student in Computer Science at Utah State University. His current research interests include text mining, topic discovery, and decision support systems.

Chris Hartwell is an Assistant Professor of Management in the Huntsman School of Business at Utah State University. He received his PhD from Purdue University. Dr. Hartwell has more than eight years of professional work experience in the field of human resources with such varied organizations as the United States Senate, Kelly Services, and the Society for Human Resource Management (SHRM). He has been a certified Profes sional in Human Resources (PHR) through the HR Certification Institute since 2009.

John Edwards is an Assistant Professor of Computer Science at Utah State University. He received his PhD from The University of Texas at Austin. He has ten years experience as a software engineer in graphics and visualization. His current research interests include data science, data visualization, and simulation.
