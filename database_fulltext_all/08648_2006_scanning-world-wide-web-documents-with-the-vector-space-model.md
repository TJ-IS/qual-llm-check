---
otero_id: 8648
otero_key: "SNCKCZSG"
title: "Scanning World Wide Web documents with the vector space model"
authors: "Cheryl Aasheim; Gary J. Koehler"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.03.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Scanning World Wide Web documents with the vector space model

Cheryl Aasheim <sup>a,T</sup>, Gary J. Koehler <sup>b,1</sup>

<sup>a</sup>Department of Information Technology, PO Box 8150, Georgia Southern University, Statesboro, GA 30460-8150, United States <sup>b</sup>Department of Decision and Information Sciences, Warrington College of Business Administration, 351 STZ, PO Box 117169, University of Florida, Gainesville, FL 32611, United States

Available online 26 April 2005

## Abstract

The vector space model used in Information Retrieval is combined with discriminant analysis to provide an automated WWW environment scanning system to detect signals of interest to an organization. The vector space model converts text-based information to numerical vectors that are then used in discriminant analysis. We illustrate the methodology using news articles pertaining to a predefined randomly selected set of stocks to test whether they provide predictive signals on whether the stock’s return will increase or decrease relative to the market in the target period following the report or whether the stock’s trading volume will increase or decrease.

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Multivariate statistics; Discriminant analysis; Environmental scanning; Decision support systems; Vector space model; Text classification

## 1. Introduction

The ability to convert data to information that can be used in decision-making is critical to an organization’s survival. Organizing and analyzing the vast quantities of data available to an organization, both internally and externally, is a challenging and sometimes impossible task. The process of obtaining and using information from an organization’s external environment to assist in decision-making is called environmental scanning [1,6]. Many studies support that environmental scanning improves an organization’s performance [10,12,28,31,32,35,40,41,46]. Information is available to an organization in many formats and from many sources, including text-based documents available on the World Wide Web (WWW). Organizations can glean valuable information from sources such as chat rooms, message boards and news documents given the capability to do so. However, many organizations do not currently have an automated system in place to collect and analyze the text-based documents available from the aforementioned sources.

As a step towards developing such a system, the purpose of this study is to develop a process to scan large amounts of text-based data collected from the

WWW for signals of interest in an automated fashion. In addition, we conducted an empirical assessment of the results produced by the process we developed. Many areas of research were combined to develop this process including the vector space model (VSM) introduced by Salton [38], linear discriminant analysis, environmental scanning [1] and text classification methods (for examples see Refs. [2,7,8,20,25,26,30,45]). A brief review of each of the areas of research is provided.

## 2. Background

The process of collecting and using information from an organization’s environment to assist management in making decisions is called environmental scanning [1,6,24]. The first person to develop a categorization for the search methods organizations use to scan the environment was Aguilar [1]. His categories are undirected viewing, conditioned viewing, informal search and formal search. The literature on environmental scanning that appeared prior to 2002 is summarized in Choo [5]. The literature is organized into the following categories: (1) situational dimensions: the effect of perceived environmental uncertainty, organizational strategy and scanning strategy, managerial traits: unanswered questions, (2) information needs: the focus of environmental scanning, (3) information seeking: source usage and preferences, (4) information seeking: scanning methods and (5) information use: strategic planning and enhanced organizational learning. Choo [5] claims that, based on the literature, the amount of scanning activity depends on the organization’s perception of how uncertain the environment is. He also claims that there is a link between organizational strategy and the sophistication and scope of scanning, scanning improves the performance of an organization, managers tend to rely on informal, personal sources for information, although, they use a variety of sources [5]. Choo [5] also introduces a general framework for managing the staggering amount of information available on the World Wide Web.

Many research studies have found a connection between scanning activity and organizational performance [10,12,28,31,32,35,40,41,45]. Additionally, the amount of information available via the World Wide

Web is immense. <sup>b</sup>Companies of all shapes and sizes are finding that the Internet provides new opportunities for competitive advantage.<sup>Q</sup> [9,pp,40–43] Pawar and Sharda [33] caution that collecting information unsystematically via the Internet can be expensive and time consuming. They claim that an Internet-based scanning system can render advantages including the timeliness, low-cost and abundance of the information available, but can also have disadvantages such as high search costs. Drucker [13] alleges that the growth of information technology has had minimal to no impact on making strategic decisions. Other researchers support this allegation by noting some of the shortcomings of the quantity and quality of information. For example, Denton [11] states that organizations are drowning in the amount of information available to them and claims that organizations should use the Internet to focus on critical information to make decision-making easier. Consequently, a webbased scanning system used to organize and classify information available on the Internet via primarily text-based web pages in an automated manner with minimal search costs to aide an organization in decision-making is needed.

One of the main goals of environmental scanning is to detect various signals. For example, is the economy going up or down in the next period? Is a competitor planning to introduce a new product in the next period? And so on. As stated in the introduction, the purpose of this paper is to define an automated process that takes large amounts of text data from the Internet and produces signals of interest.

Numerous methods are available acquiring knowledge from data. However, all such methods have several assumptions. In choosing a particular hypothesis space and knowledge representation language (e.g., decision trees, discriminant functions, neural nets, etc.) consideration must be given to the type of independent and dependent variables (nominal, ordinal, etc.) and a variety of other conditions. In this paper, we begin with text-based data and want to produce a categorical signal. Frequently, decision trees (see Ref. [36]) are used to represent rules that provide a classification. They scale well for large data sets, have been used successfully in many areas, but are not well suited for text-based attributes primarily due to the large number of independent variables (a variable for each word). Financial applications, pattern recognition and a host of other applications have had success using neural nets (e.g., [14]) as a classification mechanism. However, neural nets are generally hard to train especially with large amounts of data and even harder to interpret. Alternatively, linear discriminant analysis [15] is a method that does scale well for large data sets, but can only handle linear combinations of real-valued independent variables. Since most methods of analyzing textual data start by converting documents to vectors of realvalued attributes, we see a good match between document representation and the discriminant analysis classification method. Therefore, we begin with a discussion of methods used to convert text to realvalued attributes.

Text classification is a method to categorize each document in a document collection based on a predefined set of categories. Algorithms have been written for classifying text, examples include CON-STRUE [20], DTree [25], NaiveBayes [25], SWAP-1 [2], Nnets [46], Rocchio [26], k-NN [20] and support vector machines (SVM) introduced by Vapnik et al. [43,8]. The process developed in this paper uses the VSM [38] to represent documents in accordance with the most popular text categorization algorithm, Rocchio [26], and with support vector machines [43,8].

In text categorization, one must first decide how to represent the documents. One solution to the document representation problem is the VSM, introduced by Salton [38]. The VSM represents documents and users’ queries with vectors, providing a quantitative approach to the problem of document representation. Documents are converted to vectors by converting each word in the document to its corresponding word stem and by using the frequency of each word stem, or another similar measure, in the document as the corresponding element in the vector used to represent that document.

Once the document representation problem has been solved, the next problem is deciding on a method of categorizing the documents. Categorizing documents via linear discriminant analysis (LDA) is a natural extension of using the linear representation of documents provided by the VSM. This is the method of categorization we use in the process developed in this paper. Although the document representation problem is in accordance with Rocchio [26], the method of categorization is different. Rocchio categorizes documents based on their similarity to a prototype vector developed for each predefined category of documents.

A method of classification using LDA introduced by Fisher [15] is based on computing one or more linear discriminant functions from a training set of documents. Each document in the collection is classified according to its score in the discriminant function. The discriminant function chosen is the one that best partitions the set of documents according to some criterion, such as minimizing the number of misclassifications [22]. The original Fisher method starts with various assumptions including multivariate normality [27,37]. Although departures often are not detrimental [19], many other methods for determining LDAs are available. Mathematical programming methods were introduced to solve the LDA problem due such assumptions made in calculating Fisher’s linear discriminant function [15]. More recently, support vector machines have been introduced by Vapnik [43]. These also use mathematical programming but derive their objective from statistical learning theory.

Combining the aforementioned areas of research, we develop a process to scan, analyze and classify the content of news articles about an organization to detect and/or predict changes in the trading volume of the organization’s stock or changes in the organization’s stock returns. There have been several recent studies in the financial literature relating news and stock returns. Chan [4] studies the patterns for a set of stocks with public news releases (new stocks) versus a set of stocks with similar monthly returns without news releases (no-news stocks). He finds that there is a major difference in the return patterns for news versus no-news stocks. In a paper by Huberman and Regev [21], the events surrounding an in-depth news story in The New York Times on Sunday, May 3, 1998, concerning a breakthrough in cancer research by Entremed Inc. (ENMD) are examined. After the story, the stock price of ENMD increased by 330% from Friday–close to Monday–close and the price of stocks in the biotechnology sector also increased significantly. Interestingly, the scientific breakthrough discussed in the story had already been published in Nature and in other sources in the press five months prior to the article in the Times, with a much milder reaction with respect to stock price and no spillover to the rest of the biotechnology sector.

In addition, there have been several related articles in the text classification literature using text classification methods to predict stock price movements. Wuthrich et al. [47] used news sources on the web collected over a 6-month period containing information on stock, currency and bond markets as well as financial analysis to predict daily movements (go up more than 0.5%, go down more than 0.5% or remain steady) of five stock indices. They considered the frequency of keyword tuples determined by domain experts to be influential in moving stock markets to predict changes in the stock indices. This study achieved an average accuracy of 46%, significantly better than chance, which would only achieve 33% accuracy. Lavrenko et al. [23] developed a system that makes recommendations on news stories likely to affect market behavior by correlation of the content of news stories with trends in financial time series. The authors measured their performance by developing a trading strategy simulation that demonstrates that a trader could do significantly better than random in terms of cumulative profit by using the story recommendations made by the system. Thomas and Sycara [42] use maximum entropy text classification combined with a genetic algorithm for learning simple rules to mine web bulletin board postings to predict changes in returns on stocks with enough text to analyze. The authors also developed a trading strategy with small excess returns for stocks with a large number of postings. Gidofalvi [17] used a na<sup>R</sup>ve Bayesian text classifier to predict changes in stock prices based on news articles. The predictive power obtained in this study was low. Mettermayer [29] developed a system to predict stock price trends using press releases published immediately prior to the change in return. The system preprocesses the text in the press release, sorts the press releases into predefined categories and then determines appropriate trading strategies. The strategies significantly outperform a trader randomly buying and shorting stocks.

There have also been articles related to classifying documents on the Web. Boley et al. [3] use a new clustering technique based on graph partitioning to discover document similarities. The authors’ technique does not require pre-specified distance measures, performs well in high dimensional spaces and performs well compared to other traditional clustering algorithms. Wei and Lee [44] combine information extraction and text categorization techniques to develop an information extraction-based event detection technique. The authors use their technique to perform event detection on online news documents. They find that their technique improves the effectiveness of event detection as compared to traditional feature-based event detection techniques.

## 3. Research framework

There are four steps involved in the process: (1) collecting the documents, (2) document representation via the vector space model, (3) using two-group linear discriminant analysis for classification of a training set of documents and (4) classifying new documents using the discriminant function in (3) and testing the hypotheses. A detailed description of each of these steps is provided in the Data Analysis section.

When using LDA as a classification technique, two research questions are commonly asked:

RQ1: How well does the process classify or group the training set of documents based on a categorical variable?

RQ2: Does the process predict the correct classification better than random guessing?

## We hypothesize that

Hypothesis 1. The process will classify the training set of documents better than chance.

Hypothesis 2. The process will predict classification for new documents better than random guessing.

The application setting for empirically testing these hypotheses is the stock market. We collect news articles about publicly traded companies to detect and/ or predict changes in the trading volume of the organization’s stock or changes in the organization’s stock returns.

## 4. Data analysis: the process

A more detailed description of the steps described in the previous section is provided here.

## 4.1. Document collection and preparation

The first step involves automating the collection of web documents. Documents were collected for close to 1 year. A computer program in Java was written that automatically collects potentially relevant documents from previously identified web sites. The documents are news articles pertaining to a predefined randomly selected set of stocks. The program visits each of these sites on a daily basis and collects news articles related to specific stocks on the list of stocks. The start and stop dates for collecting articles were the same for all stocks. The html documents are stored locally in files. Each document for each stock can be classified into one of two groups using the current stock return or trading volume as the classification mechanism. By the first classification mechanism, news documents appearing before stock returns increase (decrease) relative to the market return are classified as $\pi _ { 1 } ( \pi _ { 2 } )$ , where the market return is measured by the S and P500 Index. Alternatively, news documents appearing before trading volume of a stock increases (decreases) are classified as $\pi _ { 1 } ( \pi _ { 2 } )$ . The intuition is the contents of the news documents signal an increase or decrease in stock returns relative to the market or signal a change in trading volume.

The second step in the procedure involves cleaning the html documents. Cleaning the documents involves removing html tags and words in a stopword list [16]. A stopword list consists of words that are very frequent in the English language and do not have discriminatory meaning, such as the words <sup>b</sup>the<sup>Q</sup> and <sup>b</sup>of.<sup>Q</sup> As the words in the stopword lists are very frequent in document collections, they do not help distinguish documents from one another and may be removed from the document collection. Cleaning the documents involves running a Java program. Additionally, documents are stemmed, the process of replacing words with their word stems, using the Porter stemming algorithm [34].

Once the documents have been cleaned and stemmed, they are indexed. <sup>b</sup>The process of constructing document surrogates by assigning identifiers to text items is known as indexing<sup>Q</sup> [39,p,275]. The idea behind indexing is to find the set of n index terms that best represent the documents in the collection. The method of indexing chosen determines how the documents will be represented in vector format. Indexing is accomplished by computing term weights for each term in the document after cleaning and only keeping the terms with a weight above a threshold value. One common method of producing a set of index terms is to choose terms that are good at discriminating between documents in the collection. Terms that are good discriminators are not necessarily the terms that occur the most frequently in the collection. For example, if the term <sup>b</sup>computer<sup>Q</sup> is a high-frequency word in a document collection, but also occurs in every document in the collection then <sup>b</sup>computer<sup>Q</sup> would not be a good candidate for an index term as it does not discriminate between documents. A common measure used to calculate term weights is to multiply the term frequency by the inverse document frequency. The inverse document frequency is given by

$$
\log (k / d f _ {i})\tag{1}
$$

where k is the number of documents in the collection and $d f _ { i }$ is the number of documents that contain term i. Note that the inverse document frequency includes the inverse of the ratio of the number of documents containing a given term to the total number of documents in the collection.

Indexing is accomplished via running a series of three Java programs. The first creates a master list of terms in the entire document collection for each stock. The second computes the inverse document frequency of each term in the document collection, only including terms that occur five or more times in the entire document collection. Finally, each document is represented numerically by counting the term frequency for each distinct stem in the document and multiplying by the corresponding inverse document frequency for that term.

## 4.2. Document representation

For each stock, the k articles collected are used to determine if the text or terms in the article indicate whether the stock’s return will increase or decrease relative to the market in the target period following the report or whether the stock’s trading volume will increase or decrease. Once the articles or documents are collected, a set of n index terms needs to be determined. The index terms are chosen according to the description of indexing documents in the previous section. Let

$$
t _ {1}, \dots , t _ {n} \text { for } t _ {i} \in \mathfrak {R} ^ {n}\tag{2}
$$

be the vectors corresponding to the n index terms. The term vectors form a vector space. When the terms are linearly independent, the dimensionality of the vector space is n. With full dimensionality, each document can be written as a linear combination of term vectors. Articles or documents are represented by vectors, $d _ { r } .$ For the collection of k documents or news articles for each stock, an $n \times k$ document by term matrix D can be constructed with the document vectors where each column of the document matrix corresponds to a document vector $d _ { r } .$ The elements of $d _ { r }$ are the term weights, $a _ { i , r } ,$ when the terms are orthonormal, which can be confirmed by

$$
t _ {i} ^ {\prime} d _ {r} = a _ {i, r}.\tag{3}
$$

The $\boldsymbol { a } _ { i , r } \mathbf { \bar { s } }$ are determined by the indexing operation on the document collection.

## 4.3. Document classification: LDA

After the documents have been indexed, they are in vector format. Next, their classification, $\pi _ { 1 }$ or $\pi _ { 2 } ,$ , was determined. The first classification method involves measuring stock returns relative to the market. Let $r _ { i }$ be the rate of return of stock i and $r _ { m }$ be the rate of return of the market as measured by the S and P500 Index. A stock’s performance relative to the market is measured by computing the difference between the stock’s rate of return $r _ { i }$ and the market’s rate of return $r _ { m }$ . News documents appearing a day before $r _ { i } - r _ { m } { \ge } 0$ are classified as $\pi _ { 1 }$ and documents appearing a day before $r _ { i } - r _ { m } < 0$ are classified as $\pi _ { 2 }$

The second method of classification is based on trading volume. News documents appearing a day before an increase in a stock’s trading volume as compared to the previous day’s trading volume are classified as $\pi _ { 1 }$ and documents appearing a day before a decrease or no change in trading volume are classified as $\pi _ { 2 }$

After classification, each document is in a form that can be analyzed via discriminant analysis. The set of independent variables for the discriminant procedure is given by the set of index terms and the dependent variable is either classification based on return or trading volume. Each document is an observation in the discriminant procedure. Discriminant analysis is performed in two steps using SAS. First, a forward stepwise discriminant procedure [18] is employed with the significance level, set at 15%, of an F test from an analysis of covariance used as the selection criteria for a variable to enter the model. The maximum number of entering variables in the stepwise discriminant procedure is set to the total number of documents in the collection for a given stock divided by four to insure a four to one observation to variable ratio. Next, Fisher’s [15] linear discriminant model is determined by calculating the linear discriminant coefficients, w, using the variables that entered the model via the stepwise procedure and calculating the cutting score, z.

Once the discriminant function is determined, the validity of the discriminant model will be checked via a holdout sample. Documents in the holdout sample will be used to predict whether stock returns will increase or decrease relative to the market or whether trading volume will increase or decrease. The values of z and w computed in the discriminant procedure will be updated periodically according to the newly collected data.

## 4.4. Testing the hypotheses

The document collection is divided into an 80% training sample and a 20% holdout sample. The training sample consisted of documents collected in the first 80% of the dates used for data collection and holdout sample consisted of the remaining 20% of the dates. Classification matrices provided in the SAS output for the training and the holdout samples are examined. To assess external validity of the model statistical significance for the holdout sample classification matrix is determined via Press’s Q using a Chi-square distribution with one degree of freedom for two-group classification. Press’s Q is given by

$$
\text { Press's } Q = \frac {(N - n K) ^ {2}}{N (K - 1)}\tag{4}
$$

where N is the total sample size, n is the number of correctly classified observations and K is the number of groups [18]. Press’s Q is a measure of the classification power of a discriminant function as compared to classification done completely by chance [18].

The internal validity of the linear discriminant model is checked by examining the classification matrix for the training set and by examining the classification matrix determined via a jackknife crossvalidation procedure. The proportional chance criterion [18] is calculated for both classification matrices. The proportional chance criterion is

$$
p _ {c} = p ^ {2} + (1 - p) ^ {2}\tag{5}
$$

where $p$ is the proportion of group 1 documents in the training set. The proportional chance criterion is compared to the hit ratio, $p _ { h } .$ , defined as the proportion of documents that are classified correctly by the discriminant model. If the hit ratio is statistically significantly larger than the proportional chance criterion according to the z-statistic

$$
z = \frac {(p _ {h} - p _ {c})}{\sqrt {\frac {p _ {c} (1 - p _ {c})}{N}}}\tag{6}
$$

then the classification by the jackknife cross-validation is statistically better than chance.

Testing the training set and the cross-validation classification matrices via the proportional chance criterion addresses research question one (RQ1). Testing the holdout sample addresses research question two (RQ2).

## 5. Results

There were 186 stocks in the original data set. Stocks with 200 articles or less were not considered as they did not average more than one article per day (in fact, many of these 186 had as few as 20 articles). This provided a sample of 96 stocks remaining in the analysis. Additionally, stocks that did not trade on all days that data were collected were removed from the list of stocks for analysis, leaving 93 stocks. The average training set had 974 news articles (observations or vectors), the average holdout sample had 195 and the average number of word stems (variables) in the training set was 5217.

Table 1 summarizes the results for the training set of documents. The results presented in this table are related to research question one (RQ1). The average hit ratio for the classification matrix with classification based on stock returns, defined as the percent of correctly classified documents in the collection, is 92.11%. Using the z-statistic based on the proportional chance criterion, 100% of the stocks have a classification matrix with correct classification that is significant at 1%. The average hit ratio for the jackknife cross-validation classification matrix with classification based on stock returns is 89.06%. The zstatistic for the jackknife cross-validation classification matrix for 100% of the stocks is significant at 1%. The average hit ratio for the classification matrix with classification based on changes in volume is 91.68%. Using the z-statistic based on the proportional chance criterion, 100% of the stocks have a classification matrix with correct classification that is significant at 1%. The average hit ratio for the jackknife crossvalidation classification matrix with classification based on changes in trading volume is 88.68%. Using the z-statistic based on the proportional chance criterion, 100% of the stocks have a leave-one-out cross-validation classification matrix with correct classification that is significant at 1%. Based on the evidence provided, the linear discriminant function does very well in classifying the training set of documents. Based on the results presented in Table 1 for the proportional chance criterion, the process classifies the training set of documents better than chance, supporting Hypothesis 1.

Table 1  
Summary of training set results

<table><tr><td colspan="2">Classification mechanism</td><td>Average hit ratio (%)</td><td>Proportional chance criterion (%)</td></tr><tr><td rowspan="2">Stock returns</td><td>Classification matrix</td><td>92.11</td><td>100</td></tr><tr><td>Leave-one-out cross-validation matrix</td><td>89.06</td><td>100</td></tr><tr><td rowspan="2">Trading volume</td><td>Classification matrix</td><td>91.66</td><td>100</td></tr><tr><td>Leave-one-out cross-validation matrix</td><td>88.68</td><td>100</td></tr></table>

Table 2 provides a summary of the results for the 20% holdout sample. The results presented in this table are related to research question two (RQ2). The average hit ratio, the percent of correctly classified documents in the holdout sample, for classification based on stock returns is 50.25%. Using Press’s Q, 16 out of 93 stocks have a holdout classification matrix with correct classification that is significant at 10%. The average hit ratio for classification based on changes in trading volume is 49.67%. Using Press’s Q, 16 out of 93 stocks have a holdout classification matrix with correct classification that is significant at 10%. Based on the number of stocks that have a significant holdout classification matrix, the methodology does a fairly good job of classification of the holdout sample for both classification mechanisms.

Table 2  
Summary of holdout sample results

<table><tr><td colspan="2">Classification mechanism</td><td>Average hit ratio (%)</td><td>Press&#x27;s Q (out of 93)</td></tr><tr><td>Stock returns</td><td>Classification matrix</td><td>50.25</td><td>16</td></tr><tr><td>Trading volume</td><td>Classification matrix</td><td>49.67</td><td>16</td></tr></table>

The second research question addresses how well the linear discriminant function derived from the training set of documents does on classifying the 20% holdout sample. Specifically, does the linear discriminant function predict the correct classification in the holdout sample better than random guessing? To address this question, each document in the holdout sample is classified according to the linear discriminant function and Press’s Q is computed based on the number of correctly classified documents, the total number of documents and the number of classification groups using a Chi-square distribution with one degree of freedom for two-group classification. Using return as the classification mechanism, 16 out of 93 or 17.20% of the stocks had holdout classification matrices that were statistically significant at 10%. Using volume as the classification mechanism, the result is exactly the same. In 16 out of 93 stocks, the process does predict classification for new documents better than random guessing, supporting Hypothesis 2 for those cases. The 16 stocks that were significant for returns were not the same as those for volume. Therefore, the methodology does a fairly good job of classification of the holdout sample for both classification mechanisms.

## 6. Discussion, implications of findings and future work

The environmental scanning methodology developed in this paper is automated, well founded and useful to an organization. The methodology has great versatility as shown by the ease of incorporating a variety of independent variables, the capability of handling large document collections with a large number of terms and the adaptability to a variety of applications. The methodology is validated empirically. The training set has excellent classification results for both classification mechanisms, with 100% of the stocks’ training classification matrices and leave-one-out classification matrices having statistical significance using either volume or return as the classification mechanism. The predictive capability of the linear discriminant function, calculated using the training set for both classification mechanisms, shows great promise with 17% (16 out of 93) of the stocks having holdout classification matrices with statistical significance.

The authors believe that the results can be improved in several ways in future work. From a statistical standpoint, the observation to variable ratio is low (4:1). Hair et al. [18] suggest an ideal ratio of (20:1) with a practical ratio of at least (5:1). The low observation to variable ratio as well as the performance drop from the training set to the test set suggests that the data set is suffering from overfitting, a limitation of our study. A future study is to explore the effects of increasing the observation to variable ratio. To ameliorate the problems that arise with departures from the assumptions made in the Fisher approach to the discriminant analysis problem, a linear programming or SVM approach could be used. A procedure to update the discriminant function computed from the training set needs to be added, as the classification of the holdout sample becomes known. Variables can be added to account for the nature and reliability of the news source and to represent the recent performance of the stock. To improve the results based on classification using changes in trading volume, the level of trading volume can be used as the classification mechanism as opposed to changes in trading volume. This change is consistent with what is done in the financial literature. To determine whether our method of text classification performs well, a future study is needed to compare the performance of our method to other methods such as Na<sup>R</sup>ve Bayes or SVMs. In addition, a field study is needed to determine whether our method outperforms humans reading the same articles.

Based on the predictive capability for 16 out of 93 stocks in the holdout sample when using stock returns as the classification mechanism, a profitable daily trading strategy for these stocks could be implemented. Additionally, the predictive capability of the results shows a link between news and stock returns. However, since only 16 out of 93 showed sufficient predictive capability, generalization error and overfitting are probably indicated. Two approaches will be used in the future to address these issues. First, larger training sets will be used. Fortunately, this is easy to attain for most stocks. Second, statistical learning theory (see Vapnik [43]) with the related support vector machine approach for finding linear discriminant functions will be used since these methods directly minimize bounds on the generalization error.

The predictive capability for the 16 stocks as well as the training set classification accuracy for all 93 stocks illustrates that there is a link between news and subsequent trading volume. This link between news and subsequent trading volume is consistent with financial literature. In this study, classification is based on daily changes in trading volume, as opposed to levels of trading activity or turnover ratio, the measurement typically used in financial studies. Based on the results of this study, an interesting application would be to determine which terms signal a decrease in trading activity and which signal an increase.

## References

[1] F.J. Aguilar, Scanning the Business Environment, Macmillan, New York, 1967.

[2] C. Apte, F. Damerau, S. Weiss, Towards language independent automated learning of text categorization models, Proceedings of the 17th Annual ACM/SIGIR Conference, 1994.

[3] D. Boley, M. Gini, R. Gross, E. Han, K. Hastings, G. Karypis, V. Kumar, B. Mobasher, J. Moore, Partitioning-based clustering for web document categorization, Decision Support Systems 27 (1999).

[4] W.S. Chan, Stock price reaction to news and no-news: drift and reversal after headlines, Journal of Financial Economics 70 (2) (2003).

[5] C.W. Choo, Information Management for the Intelligent Organization: the Art of Scanning the Environment, Information Today, Inc., Medford, 2002.

[6] C.W. Choo, E. Auster, Scanning the business environment: acquisition and use of information by managers, in: M.E.

Williams (Ed.), Annual Review of Information Science and Technology, Learned Information, Inc., Medford, 1993.

[7] W.W. Cohen, Y. Singer, Context-sensitive learning methods for text categorization, SIGIR ’96: Proceedings of the 19th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, 1996.

[8] C. Cortes, V. Vapnik, Support-vector networks, Machine Learning 20 (1995).

[9] M.J. Cronin, What’s my motivation? Why businesses are turning to the internet, Internet World (1993 (November/ December)).

[10] R.L. Daft, J. Sormunen, D. Parks, Chief executive scanning, environmental characteristics, and company performance: an empirical study, Strategic Management Journal 9 (2) (1988).

[11] D.K. Denton, Better decisions with less information, Industrial Management 43 (2001).

[12] M.J. Dollinger, Environmental boundary spanning and information processing effects on organizational performance, Academy of Management Journal 27 (2) (1984).

[13] P.E. Drucker, The Next Information Revolution, Forbes, 1998 (August 24).

[14] L. Fausett, Fundamentals of Neural Networks, Prentice Hall, New York, 1994.

[15] R.A. Fisher, The use of multiple measurements in taxonomic problems, Annals of Eugenics 7 (1936).

[16] W.B. Frakes, R. Baeza-Yates, Information Retrieval Data Structures and Algorithms, Prentice Hall, Englewood Cliffs, NJ, 1992.

[17] G. Gifdofalvi, Using News Articles to Predict Stock Price Movements, URL: http://www.cs.ucsd.edu/users/elkan/ 254spring01/gidofalvirep.pdf (2001).

[18] J.F. Hair, R.E. Anderson, R.L. Tatham, W.C. Black, Multivariate Data Analysis, Prentice Hall, Inc., Upper Saddle River, 1998.

[19] D.J. Hand, Discrimination and Classification, John Wiley & Sons, New York, 1981.

[20] P.J. Hayes, S.P. Weinstein, Construe/tis: a system for content-based indexing of a database of new stories, Second Annual Conference on Applications of Artificial Intelligence, 1990.

[21] G. Huberman, T. Regev, Contagious speculation and a cure for cancer: a non-event that made stock prices soar, Journal of Finance 56 (2001).

[22] G.J. Koehler, S.S. Erenguc, Minimizing misclassifications in linear discriminant analysis, Decision Sciences 2 (1990).

[23] V. Lavrenko, M. Schmill, D. Lawrie, P. Ogilvie, D. Jensen, J. Allan, Language models for financial news recommendation, Proceedings of the 9th International Conference on Information and Knowledge Management, 2000.

[24] R. Lester, J. Waters, Environmental Scanning and Business Strategy, British Library, Research and Development Department, London, 1989.

[25] D.D. Lewis, M. Ringuette, Comparison of two learning algorithms for text categorization, Proceedings of the Third Annual Symposium on Document Analysis and Information Retrieval, 1994.

[26] D.D. Lewis, R.E. Schapire, J.P. Callan, R. Papka, Training algorithms for linear text classifiers, Proceedings of the 19th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, 1996.

[27] O.L. Mangasarian, Linear and nonlinear separation of patterns by linear programming, Operations Research 13 (1965).

[28] D. Miller, P.H. Friesen, Strategy-making in context: ten empirical archetypes, Journal of Management Studies 14 (3) (1977).

[29] M.A. Mittermayer, Forecasting intraday stock price trends with text mining techniques, Proceedings of the 37th Annual Hawaii International Conference on System Sciences, 2004.

[30] I. Moulinier, G. Raskins, J. Ganascia, Text categorization: a symbolic approach, Proceedings of the Fifth Annual Symposium on Document Analysis and Information Retrieval, 1996.

[31] M.F. Murphy, Environmental scanning: a case study in higher education (Doctoral dissertation, University of Georgia), 1987.

[32] K.E. Newgren, A.A. Rasher, M.E. LaRoe, An empirical investigation of the relationship between environmental assessment and corporate performance, Proceedings of the 44th Annual Meeting of the Academy of Management, 1984.

[33] B. Pawar, R. Sharda, Obtaining business intelligence on the internet, Long Range Planning 30 (1997).

[34] M.F. Porter, An algorithm for suffix stripping, Program 14 (3) (1980).

[35] J.G. Ptaszynski, Ed Quest as an organizational development activity: evaluating the benefits of environmental scanning (Doctoral dissertation, The University of North Carolina at Chapel Hill, 1989).

[36] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kauffman, 1993.

[37] J.B. Rosen, Pattern separation by convex programming, Journal of Mathematical Analysis and Applications 10 (1965).

[38] G. Salton, Automatic Information Organization and Retrieval, McGraw-Hill Book Company, New York, 1968.

[39] G. Salton, Automatic Text Processing, Addison-Wesley Publishing Company, Inc., Reading, 1989.

[40] R. Subramanian, N. Fernandes, E. Harper, Environmental scanning in U.S. companies: their nature and their relationship to performance, Management International Review 33 (3) (1993).

[41] R. Subramanian, K. Kumar, C. Yauger, The scanning of task environments in hospitals: an empirical study, Journal of Applied Business Research 10 (4) (1994).

[42] J.D. Thomas, K. Sycara, Integrating genetic algorithms and text learning for financial prediction, in: A.A. Freitas, W. Hart, N. Krasnogor, J. Smith (Eds.), Data Mining with Evolutionary Algorithms, Technical Report WS-99-06, 2000.

[43] V.N. Vapnik, The Nature of Statistical Learning Theory, Springer, New York, 1995.

[44] C. Wei, Y. Lee, Event detection from online news documents for supporting environmental scanning, Decision Support Systems 36 (2004).

[45] J.J. West, Environmental scanning, and their effect upon firm performance: an exploratory study of the food service industry (Doctoral dissertation, Virginia Polytechnic Institute and State University), 1988.

[46] E. Wiener, J.O. Pedersen, A.S. Weigend, A neural network approach to topic spotting, Proceedings of the Fourth Annual Symposium on Document analysis and Information Retrieval, 1995.

[47] B. Wuthrich, V. Cho, S. Leung, D. Permunetilleke, K. Sankaran, J. Zhang, W. Lam, Daily stock market forecast from textual web data, IEEE International SMC Conference, 1998, pp. 2720 – 2725.

In August of 2002, Cheryl Aasheim received her Doctor of Philosophy in Decision and Information Sciences from the University of Florida. She is currently an Assistant Professor at Georgia Southern University in the College of Information Technology. Her current research interests are in the areas of information retrieval and data mining.

Gary J. Koehler has held academic positions at Northwestern University, Purdue University and at the University of Florida where he is the John B. Higdon Eminent Scholar and Professor of Decision and Information Sciences in the Warrington School of Business at the University of Florida. He has published in Decision Support Systems, Management Science, the Journal on Computing, Evolutionary Computation, Operations Research, Decision Sciences and others. He is on the editorial boards of Decision Science, Decision Support Systems, Information Technology and Management and several other journals. His current research interests are related to data mining.
