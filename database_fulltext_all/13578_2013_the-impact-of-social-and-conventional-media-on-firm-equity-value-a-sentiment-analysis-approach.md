---
otero_id: 13578
otero_key: "PS9RFPJ8"
title: "The impact of social and conventional media on firm equity value: A sentiment analysis approach"
authors: "Yang Yu; Wenjing Duan; Qing Cao"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.028"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The impact of social and conventional media on <sup>fi</sup>rm equity value: A sentiment analysis approach

Yang Yu <sup>a</sup>, Wenjing Duan <sup>b,</sup>⁎, Qing Cao <sup>a</sup>

<sup>a</sup> Texas Tech University, United States

<sup>b</sup> The George Washington University, United States

## a r t i c l e i n f o

Available online 30 December 2012

Keywords: Sentiment analysis Social media Conventional media Firm equity value

## a b s t r a c t

This study aims to investigate the effect of social media and conventional media, their relative importance, and their interrelatedness on short term <sup>fi</sup>rm stock market performances. We use a novel and large-scale dataset that features daily media content across various conventional media and social media outlets for 824 public traded <sup>fi</sup>rms across 6 industries. Social media outlets include blogs, forums, and Twitter. Conventional media includes major newspapers, television broadcasting companies, and business magazines. We apply the advanced sentiment analysis technique that goes beyond the number of mentions (counts) to analyze the overall sentiment of each media resource toward a speci<sup>fi</sup>c company on the daily basis. We use stock return and risk as the indicators of companies' short-term performances. Our <sup>fi</sup>ndings suggest that overall social media has a stronger relationship with <sup>fi</sup>rm stock performance than conventional media while social and conventional media have a strong interaction effect on stock performance. More interestingly, we <sup>fi</sup>nd that the impact of different types of social media varies signi<sup>fi</sup>cantly. Different types of social media also interrelate with conventional media to in<sup>fl</sup>uence stock movement in various directions and degrees. Our study is among the <sup>fi</sup>rst to examine the effect of multiple sources of social media along with the effect of conventional media and to investigate their relative importance and their interrelatedness. Our <sup>fi</sup>ndings suggest the importance for <sup>fi</sup>rms to differentiate and leverage the unique impact of various sources of media outlets in implementing their social media marketing strategies.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The Internet has enabled an increasing amount of user-generated content (UGC) that potentially becomes the primary source of information for both consumers and businesses. The past decade has witnessed a dramatic change of the media landscape with digital social media channels (e.g., blogs, online forums, and social networking sites) for word-of-mouth (WOM) supplementing traditional media channels (e.g., newspapers, television, and magazines). The rise of UGC on the Internet has fueled a fast-growing market in personal opinions [1]. More and more businesses and top executives are recognizing social media as an incredibly rich vein for gaining a better understanding of the online discussions and market opportunities, and for gaining feedback and evaluations of their own and their competitors' products and performances, the market structure, and the overall competitive landscape [27,40].

With the increasing availability of social media data sources, the recent years have seen an emergence of academic and industrial research that taps into these data sources. However, the utilization of these data sources remains in an early stage and outcomes are often mixed [17,27]. The major challenges are the inherent dif<sup>fi</sup>culties of tracking and quantifying the overwhelmingly large amount and unstructured set of data. A large body of extant research uses the quantitative summaries of UGC, such as overall valence and volume of user review ratings, to represent the users' opinions [6,8–10,16,24]. However, recent research suggests that it is important to extract the multifaceted textual content in UGC, which highlights the need to delve deeper into the content of the online discussions [1,13,35]. In addition, the vast majority of previous studies focus purely on the effect of online UGC and social media, without considering their interactions with conventional medial sources [37].

In this study, we aim to investigate the effect of social media and conventional media, their relative importance, and their interrelatedness on <sup>fi</sup>rm performances. Our choice of stock market performance as the outcome variable has the following bene<sup>fi</sup>ts. First, stock market performance measures the shareholder value, and is the ultimate concern of the company, which has been increasingly used in Marketing and IS studies [5,25,36]. Second, in contrast to sales and pro<sup>fi</sup>ts data, which are not easily available at a daily level, stock market performance is readily available at this level, allowing for more granular analysis. Third, social media content is updated rapidly and spreads virally, which can provide the real-time <sup>fi</sup>rst-hand information to the investor. Thus social media can provide the timely evaluation of <sup>fi</sup>rms' performance, which allow the investors not only to follow consumers' sentiment but also to predict their future business values [25].

We use a novel and large-scale dataset that features daily media content across various conventional media and social media outlets for 824 public traded <sup>fi</sup>rms across 6 industries. To properly capture both longitudinal and cross-sectional properties of our data set, we apply <sup>fi</sup>xed-effects panel data estimators. There are several important differences between the current paper and previous studies. First, unlike most of the previous studies, our research focuses not on product reviews and ratings, but on less structured media content. Second, we apply more advanced sentiment analysis technique that go beyond the number of mentions (counts) and the simple and discrete classi-<sup>fi</sup>cation of positive and negative for media discussion. Third, we extract and analyze the overall sentiment toward a speci<sup>fi</sup>c <sup>fi</sup>rm on a daily basis for a large range of <sup>fi</sup>rms across various industries, whereas most of the earlier studies focus either on one product, one <sup>fi</sup>rm, or one site. Fourth, we are among the <sup>fi</sup>rst to examine the effect of multiple sources of social media along with the effect of conventional media, investigate their relative importance and their interrelatedness. Fifth, the panel data we use in this study are particularly bene-<sup>fi</sup>cial in media research as they not only allow us to study the intertemporal behavior and performance of <sup>fi</sup>rms, but they also enable us to control for the unobserved <sup>fi</sup>rm-level heterogeneity and seasonal factors [20].

The paper proceeds as follows. Related work is reviewed and discussed to provide the theoretical background and foundation for our study in Section 2. We then describe the data, measurement, and provide detailed discussion on sentiment analysis procedures in Section 3. In Section 4, we formulate the econometrics models and present the estimation results. Finally, we conclude the paper by discussing study implications and suggesting future research directions.

## 2. Literature review

While the number and types of information resources continue to grow exponentially, human beings start to face the dif<sup>fi</sup>culty of transforming the wealth of information to knowledge for more effective use [3]. Especially, social media has been exploded as a category of online discourse where people create content, share and discuss in communication network. Social media is changing people's way of life dramatically because of its high speed connections, ease of use and great credibility. From a business and marketing perspective, we notice that the media landscape has dramatically changed in the recent years, with traditional media (e.g., newspapers, magazines, and television) now supplemented or replaced by social media (e.g., blogs, microblogs, and online forums). In contrast to content provided by traditional media sources, social media content tend to be more “human being” oriented. For example, in a blog post, an author argues against the traditional source news from her perspective and readers can join the discussion and propose their own views freely. Despite author or social group bias, such content is still often considered to be more credible and trustworthy by people than traditional sources of information [2]. With an increasing amount of user-generated content (UGC) on the social media, more and more businesses and top executives are recognizing social media as an incredibly rich vein for gaining a better understanding of the online discussion and market opportunities, and for gaining feedback and evaluations of their own and their competitors' products and performances, the market structure and the overall competitive landscape [27,40].

The object of an information system is bridging the gap between the continuous growing information and effectively converting information into knowledge. As for information processing capabilities, the challenges of a current information system are two-fold: suf<sup>fi</sup>cient accuracy and high ef<sup>fi</sup>ciency. Narrowing this down to UGC research, the major challenges are the dif<sup>fi</sup>culties to track and quantify the overwhelmingly large amount and unstructured set of data. Recent years have seen an emergence of academic and industrial research that taps into UGC. A large body of extant research uses the quantitative summaries of UGC, such as overall valence and volume of user review ratings, to represent the users' opinions [6,8–10,16]. However, the utilization of these data sources still remains in an early stage and outcomes are often mixed [17,27]. To the best of our knowledge, most of previous studies have only used the numeric data such as count or number of stars, without incorporating semantic information contained in the text. Recent research suggests that it is important to extract the multifaceted textual content in UGC, which highlights the need to delve deeper into the content of the online discussions [1,13,35]. In addition, it is still not well understood with respect to the relative impacts of different media types on marketing performance (e.g., sales), and how marketing performance in<sup>fl</sup>uences word of mouth (WOM). Furthermore, the vast majority of previous studies focus purely on the effect of online UGC and social media, without considering their interactions with conventional media sources [37].

New research applying text-mining (TM) and natural language processing (NLP) techniques was developed to help people <sup>fi</sup>nd business intelligence from free-form data; however, these methods lack strength in detecting people's opinion [15]. In the past decades, both industry and academia have been trying to <sup>fi</sup>nd effective methods and tools to extract opinion-oriented information automatically from unstructured data [31]. Sentiment analysis (SA) has evolved from TM and NLP, but aims to determine the sentiment of a speaker or a writer with respect to some speci<sup>fi</sup>c topics [23]. More recently, SA has greatly assisted decision makers in extracting opinions from unstructured human-authored documents [31], which can be applied in various areas. It reduces the need for reading huge amount of documents to extract business opinions on a variety of topics. There are three main reasons to choose SA as a research approach. 1) It converts large unstructured content into a form that allows for speci<sup>fi</sup>c predictions about particular outcomes, without institute market mechanisms. 2) It builds models to aggregate the opinions of the collective population and gains useful insights into group behavior to predict future trends. 3) It applies gathered information on how people react to particular objects and then design marketing and advertising campaigns.

Existing SA approaches are either based on linguistic resources or machine learning. SA based on linguistic resources is centered on predetermined lists of positive and negative words. The polarity of language depends on the frequency of different types of words appearing in the document. However, this approach involves a number of linguistic techniques that are not always robust and are often quite labor intensive [34]. The other machine learning based approach relies on a computer's ability to automatically learn the language used for expressing sentiment regardless of how “good” or “normal” the language is. However, the computer needs to have some information to learn from (called a training corpus or documents) and the more documents the computer learns the better. In the case of SA, the training corpus is always a set of example documents annotated by humans. Once the computer has learned from the examples, it can apply the acquired knowledge to new documents (a holdout corpus) and then classify them into sentiment categories.

There are two main streams of research in SA domain. One stream has focused on sentiment polarity and the other has focused on features detection. Most of previous SA research focuses on UGC such as product reviews or online comments. Also, we notice that most of the prior works prefer to explore the performance of a single product only. Gruhl et al. [18] show how to predict spikes in book sales via analyzing the correlation between blog and review mentions and performance. Joshi et al. [19] mine on text and metadata features to predict the earning of movies. In addition, signi<sup>fi</sup>cant progress has been made in sentiment tracking techniques that extract indicators of public mood directly from social media content such as blog content and in particular large-scale Twitter feeds [14,24,26,29]. In this research, we extract sentiment signals from both conventional and social media and calculate the sentiment polarity of each document for different <sup>fi</sup>rms based on SA techniques.

## 3. Data, measures, and sentiment analysis

## 3.1. Conventional media and social media data

We randomly select 824 companies and create a unique dataset. As shown in Table 1, this dataset covers six industries including pharmaceutical, retail, software, savings institutions, health care, and hotel. Table 1 shows the summary of the 824 companies.

We obtain the <sup>fi</sup>nancial-statement and <sup>fi</sup>nancial-market data for the 824 companies from COMPUSTAT and the Center of Research in Security Prices (CRSP) that was recorded from July 1st to September 30th, 2011. We use these data to construct measures of abnormal returns and cumulative abnormal returns (please see more discussion in the next section). Subsequently, we obtained a collection of blog, forum, news and micro blog (e.g., Twitter) content for those three months (from 2011/07/01 to 2011/09/30) related to the 824 companies (Table 2). A web crawler was created to download blogs, forums, and news web pages automatically. Due to the large variety of data source, the web pages have different layouts, different formatting markups, and different hidden advertisements. As such it is the main challenge for automatic text extraction, and a customized HTML parser based on Python was designed and imported as a “noise” <sup>fi</sup>lter to remove the irrelevant information such as sidebars, advertisements, header, footer, and then to identify useful and clean text paragraphs from large chunks of HTML code. The underlying mechanism of this <sup>fi</sup>lter is rather simple, which is to use information about the density of text vs. HTML tags to <sup>fi</sup>gure out if a line of text is worth outputting. Different with a common html parser, the main advantage of this <sup>fi</sup>lter is that it can be applied to an arbitrary html code regardless of the page layout or the noise tags used. For each blog post, forum post, and news article, we obtained the title, date, author, source domain, and the main content. For each Tweet, we obtain Twitter username, the date–time of the submission (GMT+0), submission type (Tweet or Retweet), and the text content of Tweet which is by design limited to 140 characters. In order to avoid spam messages and other advertising tweets, we <sup>fi</sup>lter tweets that include URLs only. Table 2 summarizes the four media data resources.

We employ an automated SA technique to explore the sentence-level sentiment polarity and to obtain a sentiment measure for each company in a given day. The detail of such SA analysis will be discussed in Section 3.2. The sentiment matrix is then derived to show sentiment from each media source (a score from −1 to 1), a score of 1 (−1) means this media source has the most positive (negative) view for the company. For example, in a given day, a company may have a score of 0.8 from the conventional news and a score of 0.3 from the social media, which would imply that traditional media has more positive sentiment towards the company than social media does.

For one document d, either a blog or a forum post, the overall sentiment score is calculated by the following formula:

$$
S _ {d} = \frac {N _ {p d} - N _ {n d}}{N _ {p d} + N _ {n d}}\tag{1}
$$

## Table 1

Summary of company characteristics.

<table><tr><td>Industry</td><td>N</td></tr><tr><td>Pharmaceutical preparation manufacturing</td><td>156</td></tr><tr><td>Retail trade</td><td>190</td></tr><tr><td>Software publishers</td><td>155</td></tr><tr><td>Savings institutions</td><td>146</td></tr><tr><td>Accommodation and food services, travel arrangement and reservation services and tour operators</td><td>82</td></tr><tr><td>Health care and social assistance, direct health and medical insurance carriers</td><td>95</td></tr><tr><td>Total</td><td>824</td></tr></table>

where $N _ { p d }$ denotes the number of positive sentences in document d and $N _ { p d }$ denotes the number of negative sentences in document d. Previous studies use ternary classi<sup>fi</sup>cation to represent sentiment polarity, positive, negative, and neutral [30]. We only use positive and negative labels in this study due to two main reasons. The <sup>fi</sup>rst reason is that a sentence that includes subjective expressions always implies either positive or negative feelings. Neutral has a fairly vague range, which is much less accurate to identify. The second consideration is from the methodological (e.g., machine learning) perspective. There are no mature sentiment repertoires yet available to ef<sup>fi</sup>ciently and accurately identify neutral sentiment.

One routine step in SA is to train the machine to allows computers to evolve behaviors based on empirical data such as an external knowledge repository. In our procedure, we train the sentiment classi<sup>fi</sup>cation system by the Cornell movie-review dataset<sup>1</sup>. We then compute the accuracy of the classi<sup>fi</sup>er on the test set and use the F-measure to evaluate the performance based on precision and recall.

The F-measure is calculated as:

$$
\mathrm{F-measure} = \frac {2 * \text { Precision } * \text { Recall }}{\text { Precision } + \text { Recall }}\tag{2}
$$

where

$$
\text { Precision } = \mathrm{TP} / (\mathrm{TP} + \mathrm{FP}) \quad \text { and } \quad \text { Recall } = \mathrm{TP} / (\mathrm{TP} + \mathrm{FN}).\tag{3}
$$

In Eq. (3), TP is the number of true positive, TN is the number of true negatives, FP is the number of false positives, and FN is the number of false negatives.

The proposed positive–negative classi<sup>fi</sup>cation algorithm can automatically classify polarity with 79% accuracy and 0.86 F-measure on the test set. On average, accuracy of binary sentiment classi<sup>fi</sup>cation is around 80% [4].

## 3.2. Sentiment analysis

We employ an automated sentiment analysis technique to explore the document-level polarity and to gain a sentiment score for the company in a given day. Sentiment analysis is the computational detection and study of opinions, sentiments, emotions, and subjectivities in text [22,23,30].

To accomplish the goal of mining opinions, the sentiment analysis involves two consecutive tasks: detecting which text segments (e.g., sentences) contain sentiment signals, and determining the polarity and even the strength of that sentiment [30]. Thus, the main purpose of SA is to determine the sentiment of a speaker or a writer on speci<sup>fi</sup>c topics. The use of sentiment analysis and related approaches has gained great popularity in the past decade due to several factors, including the advance of machine learning methods in natural language processing and information retrieval, the availability of large and rich datasets for machine learning algorithms to be trained on, and the development of many commercial intelligence applications [7,30,38,39].

In this study, we apply the Naïve Bayes (NB) algorithm to conduct sentiment analysis. NB is a simple but effective classi<sup>fi</sup>er that has been used in numerous information processing techniques such as image recognition, NLP, information retrieval, etc., based on the open-source Natural Language Toolkit (NLTK) [11,21,28,32].

The underlying theorem for Naïve Bayesian text classi<sup>fi</sup>cation is the Bayes Rule:

$$
P (A | B) = \frac {(P (B | A) * P (A))}{P (B)}.\tag{4}
$$

The Bayes Rule enables the calculation of the likelihood of event A given that B has happened. This is used in text classi<sup>fi</sup>cation to determine the probability that a document B is of type A just by looking at the frequencies of words in the document. In our classi<sup>fi</sup>cation task, we use the Bayes Rule in updating the probability of event A (frequencies of words or terms) happening given that we've observed B (positive or negative sentiment).

Table 2  
Four types of media data.

<table><tr><td>Content category</td><td>Data source</td><td>Data source description</td><td># of content</td></tr><tr><td>Blog</td><td>Google Blogs</td><td>Google Blog Search provides fresh, relevant search results from millions of feed-enabled blogs. Users can search for blogs or blog posts, and can narrow their searches by dates and more.</td><td>11,369</td></tr><tr><td>Forum</td><td>BoardReader</td><td>BoardReader is developed to address the shortcomings of current search engine technology to accurately find and display information contained on the Web&#x27;s forums and message boards. It uses proprietary software that allows users to search multiple message boards simultaneously, allowing users to share information in a truly global sense.</td><td>13,091</td></tr><tr><td>Micro blog</td><td>Twitter</td><td>Twitter, a micro blogging service, has emerged as a new medium in the spotlight through recent events, such as the death of Steve Jobs and the Libyan uprising. Twitter users follow others or are followed. Unlike most online social networking sites, such as Facebook or MySpace, the relationship of following and being followed requires no reciprocation. A user can follow any other user, and the user being followed need not follow back. A common practice of responding to a tweet has evolved into a well-defined markup culture: RT stands for retweet, &#x27;@&#x27; followed by a user identifier addresses the user, and &#x27;#&#x27; followed by a word represents a hashtag. This well-defined markup vocabulary combined with a strict limit of 140 characters per posting conveniences users with brevity in expression.</td><td>24,505</td></tr><tr><td>Conventional News</td><td>Google News</td><td>Google News is a computer-generated news site that aggregates headlines from news sources worldwide. In this research, we choose 10 big news sources as conventional media sources. There are ABC News, New York Times, Reuters, USA Today, Fox News, Wall Street Journal, Washington Post, CNN, The Economist and Forbes.</td><td>3782</td></tr></table>

For the purposes of text classi<sup>fi</sup>cation, the Bayes Rule is used to determine the category a document falls into by determining the most probable category. That is, given this document with these words in it, which category does it fall into? A category is represented by a collection of words and their frequencies while the frequency is the number of times that each word has been seen in the documents used to train the classi<sup>fi</sup>er. Suppose there are n categories $C _ { 0 }$ to $C _ { ( n - 1 ) }$ (in our case, here are only two categories, positive or negative). Determining which category a document D is mostly associated with means calculating the probability that document D is in category $C _ { i } ,$ written $P ( C _ { i } | D )$ for each category $C _ { i }$

Then we can calculate $P ( C _ { i } | D )$ by computing:

$$
(C _ {i} | D) = \frac {(P (D | C _ {i})) (P (C _ {i}))}{(P (D))}.\tag{5}
$$

P(C |D) is the probability that document D is in category $C _ { i } ;$ that is, the probability that given the set of words in D, they appear in category $C _ { i } . P ( D | C _ { i } )$ is the probability that for a given category $C _ { i } ,$ the words in D appear in that category. $P ( C _ { i } )$ is the probability of a given category; that is, the probability of a document being in category $C _ { i }$ without considering its contents. $P ( D )$ is the probability of that speci<sup>fi</sup>c document occurring. To calculate which category D should go in, we need to calculate $P ( C _ { i } | D )$ for each of the categories and <sup>fi</sup>nd the largest probability. Because each of those calculations involves the unknown but <sup>fi</sup>xed value $P ( D )$ , we just ignore it and calculate:

$$
P (C _ {i} | D) = P (D | C _ {i}) * P (C _ {i}).\tag{6}
$$

P(D) can also be safely ignored because you are interested in the relative, not absolute, values of $P ( C _ { i } | D )$ , and $P ( D )$ simply acts as a scaling factor on $P ( C _ { i } | D )$ . D is split into the set of words in the document, called $W _ { 0 }$ through $W _ { m - 1 }$ . To calculate P(D|C ), we need to know the likelihood that each word appears in $C _ { i }$ <sup>fi</sup>rst. Assume that words appear independently from other words (which is clearly not true for most languages) and $P ( D | C _ { i } )$ is the simple product of the probabilities for each word:

$$
P (D | C _ {i}) = P \left(W _ {0} | C _ {i}\right) * P \left(W _ {1} | C _ {i}\right) * \dots * P \left(W _ {m - 1} | C _ {i}\right).\tag{7}
$$

For any category, $P ( W _ { j } | C _ { i } )$ is calculated as the number of times $W _ { j }$ appears in $C _ { i }$ divided by the total number of words in $C _ { i } , P ( C _ { i } )$ is calculated as the total number of words in $C _ { i }$ divided by the total number of words in all the categories put together. Hence, $P ( C _ { i } | D )$ is:

$$
P (W _ {0} | C _ {i}) * P (W _ {1} | C _ {i}) * \ldots * P (W _ {m - 1} | C _ {i}) * P (C _ {i}).\tag{8}
$$

Then we pick the highest probability category as the label of docu ment D.

A common criticism of Naïve Bayesian text classi<sup>fi</sup>ers is that they make the naïve assumption that words are independent of each other and are, therefore, less accurate than a more complex model. There are many more complex text classi<sup>fi</sup>cation techniques, such as Support Vector Machines, K-nearest Neighbor, and so on. In practice, Naïve Bayesian classi<sup>fi</sup>ers often perform well, and the current state of sentiment analysis indicates that they work very well for sentiment polarity classi<sup>fi</sup>cation [4,31].

## 3.3. Data and measures for firm financial value

We obtain <sup>fi</sup>nancial-statement and <sup>fi</sup>nancial-market data from COMPUSTAT and the Center of Research in Security Prices (CRSP). We use these data to construct measures of abnormal returns and cumulative abnormal returns. Fama and French [12] present a time-series model of the evolution of excess security returns (relative to a risk-free rate) as a function of excess market returns, a high-minus-low marketto-book ratio factor, and a small-minus-big market capitalization factor. The Fama and French four factor model is therefore often used as the benchmark model to generate normal returns. This model extends the market model with the returns on a “size” portfolio (SMB), a “value” portfolio (HML) and a “momentum” portfolio (UMD). Fama–Frenchmomentum four-factor model is:

$$
R _ {j t} = \alpha_ {j} + \beta_ {j} R _ {m t} + s _ {j} \mathrm{SMB} _ {t} + h _ {j} \mathrm{HML} _ {t} + u _ {j} \mathrm{UMD} _ {t} + \int_ {j t}\tag{9}
$$

where $R _ { j t }$ is the rate of return of the common stock of the $j ^ { t h }$ <sup>fi</sup>rm on day t; $R _ { m t }$ is the rate of return of a market index on day t; SMB is the average return on small market-capitalization portfolios minus the average return on three large market-capitalization portfolios; HML is the average return on two high book-to-market equity portfolios minus the average return on two low book-to-market equity portfolios; $\mathrm { U M D } _ { t }$ is the average return on two high prior return portfolios minus the average return on two low prior return portfolios. $j t$ is a random variable that, by construction, must have an expected value of zero, and is assumed to be uncorrelated with $R _ { m t }$ , uncorrelated with $R _ { k t }$ for $k \neq j ,$ , not autocorrelated, and homoskedastic. $\beta _ { j }$ is a parameter that measures the sensitivity of $R _ { j t }$ to the excess return on the market index; $s _ { j }$ measures the sensitivity of $R _ { j t }$ to the difference between small and large capitalization stock returns; $h _ { j }$ measures the sensitivity of $R _ { j t }$ to the difference between value and growth stock returns; and $u _ { j }$ measures the sensitivity of $R _ { j t }$ to the difference between high prior return stock returns and low prior return stock returns. Thus, we de<sup>fi</sup>ne the abnormal return $( A R _ { j t } )$ (or prediction error) from the common stock of the $j ^ { t h }$ <sup>fi</sup>rm on day t as:

$$
A R _ {j t} = R _ {j t} - \left(\hat {\alpha} _ {j} + \hat {\beta} _ {j} R _ {m t} + \hat {s} _ {j} \mathrm{SMB} _ {t} + \hat {h} _ {j} \mathrm{HML} _ {t} + \hat {u} _ {j} \mathrm{UMD} _ {t}\right)\tag{10}
$$

where the coef<sup>fi</sup>cients $\hat { \alpha } _ { j } , \hat { \beta } _ { j } , \hat { s } _ { j } , \hat { h } _ { j }$ and $\hat { u } _ { j }$ are ordinary least squares estimates of $\cdot \alpha _ { j } , \beta _ { j } , s _ { j } , h _ { j }$ and $u _ { j } .$ The idiosyncratic risk $( I R _ { j t } )$ is the standard deviation of the model residuals.

## 4. Econometric modeling and estimation results

We estimate two equations, where endogenous variables are <sup>fi</sup>rm equity value (return and risk), using the <sup>fi</sup>xed-effects panel data estimation technique. To control for any company idiosyncratic factors that could in-<sup>fl</sup>uence stock return and risk, such as company size, industry characteristics, and others, we include company <sup>fi</sup>xed effects in the model by adding company-speci<sup>fi</sup>c dummy variables. The company-speci<sup>fi</sup>c <sup>fi</sup>xed effects capture the idiosyncratic and time-constant unobserved characteristics associated with each company in our data. The advantage of <sup>fi</sup>xed effects estimation is that it controls for intrinsic company characteristics, which inherently affect stock movement. In addition, <sup>fi</sup>xed effects estimation also allows the error term to be arbitrarily correlated with other explanatory variables, thus making the estimation results more robust. Table 3 describes the variable name and measures. Table 4 shows the descriptive statistics.

The two equations are speci<sup>fi</sup>ed as follows:

$$
A R _ {i t} = \alpha_ {r} + X _ {i, t - 1} ^ {m} \beta_ {r} ^ {m} + X _ {i, t - 1} ^ {n} \beta_ {r} ^ {n} + \mu_ {i} + \varepsilon_ {i t}\tag{11}
$$

$$
I R _ {i t} = \alpha_ {s} + X _ {i, t - 1} ^ {m} \beta_ {s} ^ {m} + X _ {i, t - 1} ^ {n} \beta_ {s} ^ {n} + \rho_ {i} + \sigma_ {i t}.\tag{12}
$$

Eq. (11) uses the abnormal return $( A R _ { i t } )$ as the dependent variable, and Eq. (12) uses the idiosyncratic risk $( I R _ { i t } )$ as the dependent variable. Let $i { = } 1 , . . . , N$ index the companies, $t { = } 1 , . . . , T$ index the time (day), $X _ { i , t - 1 } ^ { m }$ is a vector of one-day lagged independent variables including all three social media (blog, forum, and Twitter) metrics, and $X _ { i , t - 1 } ^ { n }$ is a vector of one-day lagged independent variables of conventional news media metrics. µ and $\rho _ { i }$ denote the company-speci<sup>fi</sup>c <sup>fi</sup>xed effects that capture the idiosyncratic characteristics associated with each company.

Table 5 shows the <sup>fi</sup>xed-effect estimation results using the total volume or sentiment of social and conventional media as the independent variables. In Model (a1), only total number of social media counts has a signi<sup>fi</sup>cant positive relationship with risk, but not with return. In Model $\left( \mathsf { a } 2 \right)$ , the interaction term of the social and conventional media counts is added. It is shown that the interaction term has a marginally negative relationship with return, but a highly negative signi<sup>fi</sup>cant relationship with risk. Considering that the social media volume is signi<sup>fi</sup>cantly larger than conventional media, this result suggests that the volume of social and conventional media complements with each other to reduce the uncertainty associated with the stock prices. In Model (a3) and (a4), we <sup>fi</sup>nd that the social media sentiment has a strong positive relationship with stock risk, indicating that the overall sentiment of social media channels may increase the <sup>fl</sup>uctuation of the stock market. The interaction term of the social and conventional media sentiment does not show a signi<sup>fi</sup>cant relationship with either return or risk. Results in Table 5 demonstrate that overall social media metrics has a strong relationship with risk, which indicates that the information instilled from various social media channels may contribute to the uncertainty of the market. In addition, we notice that the impact of count and sentiment may have different directions, which suggest the importance of delving into the textual content mentioned in the media. Furthermore, it seems the impact is more salient with risk than return. This may be due to the short term span of the dataset and one-day lagged independent variable setting. Previous research indicates that stock market may need some time to respond to the social media information [25].

Description of key variables.

<table><tr><td>Variable</td><td>Description and measure</td></tr><tr><td> $AR_{it}$ </td><td>The abnormal return of the stock price for company  $i$  at day  $t$ .</td></tr><tr><td> $IR_{it}$ </td><td>The idiosyncratic risk of the stock price for company  $i$  at day  $t$ .</td></tr><tr><td> $BLOG_POS_NUM_{it}$ </td><td>The number of positive sentiment blogs for company  $i$  at day  $t$ .</td></tr><tr><td> $BLOG_NEG_NUM_{it}$ </td><td>The number of negative sentiment blogs for company  $i$  at day  $t$ .</td></tr><tr><td> $BLOG_NUM_{it}$ </td><td>Total number of mentions in blogs for company  $i$  at day  $t$ .</td></tr><tr><td> $BLOG_SENTI_{it}$ </td><td>Overall sentiment in blogs for company  $i$  at day  $t$ .</td></tr><tr><td> $FORUM_POS_NUM_{it}$ </td><td>The number of positive sentiment forums for company  $i$  at day  $t$ .</td></tr><tr><td> $FORUM_NEG_NUM_{it}$ </td><td>The number of negative sentiment forums for company  $i$  at day  $t$ .</td></tr><tr><td> $FORUM_NUM_{it}$ </td><td>Total number of mentions in forums for company  $i$  at day  $t$ .</td></tr><tr><td> $FORUM_SENTI_{it}$ </td><td>Overall sentiment in forums for company  $i$  at day  $t$ .</td></tr><tr><td> $TWEET_POS_NUM_{it}$ </td><td>The number of positive sentiment Tweets for company  $i$  at day  $t$ .</td></tr><tr><td> $TWEET_NEG_NUM_{it}$ </td><td>The number of negative sentiment Tweets for company  $i$  at day  $t$ .</td></tr><tr><td> $TWEET_NUM_{it}$ </td><td>Total number of mentions in Tweets for company  $i$  at day  $t$ .</td></tr><tr><td> $TWEET_SENTI_{it}$ </td><td>Overall sentiment in Tweets for company  $i$  at day  $t$ .</td></tr><tr><td> $NEWS_POS_NUM_{it}$ </td><td>The number of positive sentiment news for company  $i$  at day  $t$ .</td></tr><tr><td> $NEWS_NEG_NUM_{it}$ </td><td>The number of negative sentiment news for company  $i$  at day  $t$ .</td></tr><tr><td> $NEWS_NUM_{it}$ </td><td>Total number of mentions in news for company  $i$  at day  $t$ .</td></tr><tr><td> $NEWS_SENTI_{it}$ </td><td>Overall sentiment in news for company  $i$  at day  $t$ .</td></tr><tr><td> $MEDIA_NUM_{it}$ </td><td>Total number of mentions in social media for company  $i$  at day  $t$ .</td></tr><tr><td> $NEWS_SENTI_{it}$ </td><td>Overall sentiment in social media for company  $i$  at day  $t$ .</td></tr></table>

We then extend our analysis in Table 5 to examine the impact of each individual media metrics. Table 6 shows the results of using number of mentions (count) of each media metrics. Model (b1) shows that number of blog mentions has a marginal negative effect on return but a signi<sup>fi</sup>cantly positive effect on risk. Number of forum mentions has a negative effect on return. Number of tweets has a signi<sup>fi</sup>cantly positive effect on risk. Model (b2) adds the interaction terms between social and conventional media mentions, only the interaction terms of forum and news mentions, and Twitter and news mentions, have a marginally negative effect on return. Risk, nevertheless, seems to be signi<sup>fi</sup>cantly in<sup>fl</sup>uenced by most variables. Besides number of blog mentions and tweets, number of conventional news mentions is also found to be positively and signi<sup>fi</sup>cantly correlated with risk. The interaction terms of forum and news mentions, and Twitter and news mentions, have a negative relationship with risk. Consistent with the results in Table $5 ,$ results in Table 6 suggest that the sheer volume of social media may help conventional media to reduce the risk, though the social media volume itself may increase the risk. Again, the return of the stock price seems to be only marginally affected.

Summary statistics of the daily data.

<table><tr><td>Variable</td><td>N</td><td>Mean</td><td>Median</td><td>Std. Dev.</td><td>Min.</td><td>Max.</td></tr><tr><td>AR</td><td>50,611</td><td>-0.0002</td><td>-0.0005</td><td>0.04</td><td>-0.61</td><td>1.36</td></tr><tr><td>IR</td><td>50,611</td><td>0.03</td><td>0.02</td><td>0.02</td><td>0.01</td><td>0.14</td></tr><tr><td>BLOG_POS_NUM</td><td>50,611</td><td>0.25</td><td>0.00</td><td>0.97</td><td>0.00</td><td>42.00</td></tr><tr><td>BLOG_NEG_NUM</td><td>50,611</td><td>0.01</td><td>0.00</td><td>0.08</td><td>0.00</td><td>4.00</td></tr><tr><td>BLOG_NUM</td><td>50,611</td><td>0.44</td><td>0.00</td><td>1.64</td><td>0.00</td><td>76.00</td></tr><tr><td>BLOG_SENTI</td><td>50,611</td><td>0.24</td><td>0.00</td><td>0.96</td><td>-2.00</td><td>42.00</td></tr><tr><td>FORUM_POS_NUM</td><td>50,611</td><td>0.56</td><td>0.00</td><td>2.00</td><td>0.00</td><td>64.00</td></tr><tr><td>FORUM_NEG_NUM</td><td>50,611</td><td>0.00</td><td>0.00</td><td>0.06</td><td>0.00</td><td>3.00</td></tr><tr><td>FORUM_NUM</td><td>50,611</td><td>1.23</td><td>0.00</td><td>3.80</td><td>0.00</td><td>109.00</td></tr><tr><td>FORUM_SENTI</td><td>50,611</td><td>0.55</td><td>0.00</td><td>2.00</td><td>-1.00</td><td>64.00</td></tr><tr><td>TWEET_POS_NUM</td><td>50,611</td><td>0.11</td><td>0.00</td><td>0.82</td><td>0.00</td><td>77.00</td></tr><tr><td>TWEET_NEG_NUM</td><td>50,611</td><td>0.40</td><td>0.00</td><td>1.97</td><td>0.00</td><td>227.00</td></tr><tr><td>TWEET_NUM</td><td>50,611</td><td>3.17</td><td>0.00</td><td>9.37</td><td>0.00</td><td>573.00</td></tr><tr><td>TWEET_SENTI</td><td>50,611</td><td>-0.29</td><td>0.00</td><td>1.76</td><td>-150.00</td><td>52.00</td></tr><tr><td>NEWS_POS_NUM</td><td>50,611</td><td>0.05</td><td>0.00</td><td>0.24</td><td>0.00</td><td>5.00</td></tr><tr><td>NEWS_NEG_NUM</td><td>50,611</td><td>0.00</td><td>0.00</td><td>0.07</td><td>0.00</td><td>2.00</td></tr><tr><td>NEWS_NUM</td><td>50,611</td><td>0.08</td><td>0.00</td><td>0.33</td><td>0.00</td><td>6.00</td></tr><tr><td>NEWS_SENTI</td><td>50,611</td><td>0.04</td><td>0.00</td><td>0.24</td><td>-2.00</td><td>5.00</td></tr><tr><td>MEDIA_NUM</td><td>50,611</td><td>4.84</td><td>0.00</td><td>10.99</td><td>0.00</td><td>573.00</td></tr><tr><td>NEWS_SENTI</td><td>50,611</td><td>0.51</td><td>0.00</td><td>2.80</td><td>-150.00</td><td>67.00</td></tr></table>

\*\*\* $\mathrm { p } < . 0 1 .$

Table 6  
Table 5  
Fixed effects estimation results for overall social media and news.

<table><tr><td rowspan="2">Variable</td><td>Coefficient (Std. Err.)</td><td>Coefficient (Std. Err.)</td><td>Coefficient (Std. Err.)</td><td>Coefficient (Std. Err.)</td></tr><tr><td>Model (a1)</td><td>Model (a2)</td><td>Model (a3)</td><td>Model (a4)</td></tr><tr><td colspan="5">Return equation: with abnormal return  $AR_{it}$  as dependent variable</td></tr><tr><td>Constant</td><td>-.0002 (.0002)</td><td>-.0003 (.0002)</td><td>-.0002 (.0002)</td><td>-.0003 (.0002)</td></tr><tr><td> $NEWS\_NUM_{i,t-1}$ </td><td>.0002 (.0005)</td><td>.001 (.001)</td><td></td><td></td></tr><tr><td> $MEDIA\_NUM_{i,t-1}$ </td><td>9.43e-06 (.00002)</td><td>.00003 (.00002)</td><td></td><td></td></tr><tr><td> $NEWS\_SENTI_{i,t-1}$ </td><td></td><td></td><td>.00003 (.0006)</td><td>.001 (.001)</td></tr><tr><td> $MEDIA\_SENTI_{i,t-1}$ </td><td></td><td></td><td>.00002 (.00002)</td><td>.00003 (.00002)</td></tr><tr><td> $NEWS\_NUM_{i,t-1} * MEDIA\_NUM_{i,t-1}$ </td><td></td><td>-.00004 (.00002)*</td><td></td><td></td></tr><tr><td> $NEWS\_SENTI_{i,t-1} * MEDIA\_SENTI_{i,t-1}$ </td><td></td><td></td><td></td><td></td></tr><tr><td colspan="5">Risk equation: with idiosyncratic risk  $IR_{it}$  as dependent variable</td></tr><tr><td>Constant</td><td>.03 (9.97e-06)</td><td>.03 (.00001)</td><td>.03 (9.75e-06)</td><td>.03 (9.88e-06)</td></tr><tr><td> $NEWS\_NUM_{i,t-1}$ </td><td>.00004 (.00003)**</td><td>.0001 (.00004)***</td><td></td><td></td></tr><tr><td> $MEDIA\_NUM_{i,t-1}$ </td><td>8.36e-06 (9.4e-07)***</td><td>1.00e-05 (1.06e-06)***</td><td></td><td></td></tr><tr><td> $NEWS\_SENTI_{i,t-1}$ </td><td></td><td></td><td>.00003 (.00003)</td><td>.00005 (.00004)</td></tr><tr><td> $MEDIA\_SENTI_{i,t-1}$ </td><td></td><td></td><td>7.92e-06 (1.35e-06)***</td><td>8.50e-06 (1.44e-06)***</td></tr><tr><td> $NEWS\_NUM_{i,t-1} * MEDIA\_NUM_{i,t-1}$ </td><td></td><td>-4.46e-06 (1.31e-06)***</td><td></td><td></td></tr><tr><td> $NEWS\_SENTI_{i,t-1} * MEDIA\_SENTI_{i,t-1}$ </td><td></td><td></td><td></td><td>-2.55e-06 (2.21e-06)</td></tr><tr><td>N=49,807 Group=824</td><td></td><td></td><td></td><td></td></tr></table>

Note: standard errors in parentheses.  
Company dummies (<sup>fi</sup>xed effects for each of the 824 companies) used in estimating the model are not reported.  
\*\*\* $\mathrm { p } < . 0 1 .$  
\*\* $\mathsf { p } { < } . 0 5 .$  
\* $\mathsf { p } \ll . 1 0 .$

Table 7 shows the estimation results using sentiment measures for each individual media. Results in Model (b3) is consistent with that in Model (b1), that blog sentiment has a positive impact but forum sentiment has a negative impact on return. Both blog and Twitter sentiment are also found to have a positive effect on risk. Interestingly, as shown in Model (b4), it seems the interaction term between Twitter and news sentiment has a signi<sup>fi</sup>cant negative effect on returns, but none of the interaction terms has a signi<sup>fi</sup>cant effect on risk. Considering results in Tables 6 and 7 together, social media metrics seem to have a much stronger impact than conventional news metrics, yet social media and conventional news media do have a joint effect on the market. The effect also seems to be stronger on risk than return, and the volume of the in<sup>fl</sup>uence is more salient than the sentiment. Moreover, each social medial metrics, as well as its interaction with conventional media metrics, has a varied impact on risk and return.

Lastly, we examine the count of positive and negative count of media mentions on stock performance to get more insights on the effect at a more granular level. Table 8 shows the results. Positive blog posts have a strong positive impact on return, and negative forum posts have a strong negative impact on return. The results provide a better explanation for results shown in Tables 6 and 7, which suggest that the majority of blog posts may be positive comments on companies and products, while forum posts may have more negative discussions. For the risk equation, we <sup>fi</sup>nd positive blog posts also contribute to the <sup>fl</sup>uctuation of the market. Interestingly, both positive and negative tweets have positive relationships with the risk. This is also consistent with the results in

Fixed effects estimation results for volume of individual social media and news.

<table><tr><td rowspan="2">Variable</td><td>Coefficient (Std. Err.)</td><td>Coefficient (Std. Err.)</td></tr><tr><td>Model (b1)</td><td>Model (b2)</td></tr><tr><td colspan="3">Return equation: with abnormal return  $AR_{it}$  as dependent variable</td></tr><tr><td>Constant</td><td>-.0002 (.0002)</td><td>-.0003 (.0001)</td></tr><tr><td> $BLOG\_NUM_{i,t-1}$ </td><td>.0002 (.0001)*</td><td>.0002 (.0001)</td></tr><tr><td> $FORUM\_NUM_{i,t-1}$ </td><td>-.0001 (.00004)**</td><td>-.0001 (.00005)</td></tr><tr><td> $TWEET\_NUM_{i,t-1}$ </td><td>.00002 (.00002)</td><td>.00004 (.00002)</td></tr><tr><td> $NEWS\_NUM_{i,t-1}$ </td><td>.0002 (.0005)</td><td>.001 (.001)</td></tr><tr><td> $BLOG\_NUM_{i,t-1}*NEWS\_NUM_{i,t-1}$ </td><td></td><td>.00003(.0002)</td></tr><tr><td> $FORUM\_NUM_{i,t-1}*NEWS\_NUM_{i,t-1}$ </td><td></td><td>-.0002 (.0001)*</td></tr><tr><td> $TWEET\_NUM_{i,t-1}*NEWS\_NUM_{i,t-1}$ </td><td></td><td>-.00004 (.00003)*</td></tr><tr><td colspan="3">Risk equation: with idiosyncratic risk  $IR_{it}$  as dependent variable</td></tr><tr><td>Constant</td><td>.03 (.00001)</td><td>.03 (.00001)</td></tr><tr><td> $BLOG\_NUM_{i,t-1}$ </td><td>.00002 (6.56e-06)***</td><td>.00002 (6.93e-06)***</td></tr><tr><td> $FORUM\_NUM_{i,t-1}$ </td><td>-2.48e-06 (2.44e-06)</td><td>-8.36e-07 (2.60e-06)</td></tr><tr><td> $TWEET\_NUM_{i,t-1}$ </td><td>9.4e-06 (1.06e-06)***</td><td>.00001 (1.21e-06)***</td></tr><tr><td> $NEWS\_NUM_{i,t-1}$ </td><td>.00003 (.00003)</td><td>.0001 (.00004)***</td></tr><tr><td> $BLOG\_NUM_{i,t-1}*NEWS\_NUM_{i,t-1}$ </td><td></td><td>-7.66e-06 (.00001)</td></tr><tr><td> $FORUM\_NUM_{i,t-1}*NEWS\_NUM_{i,t-1}$ </td><td></td><td>-8.80e-06 (5.15e-06)*</td></tr><tr><td> $TWEET\_NUM_{i,t-1}*NEWS\_NUM_{i,t-1}$ </td><td></td><td>-4.59e-06 (1.41e-06)***</td></tr><tr><td colspan="3">N=49,807 Group=824</td></tr></table>

Note: standard errors in parentheses.  
\*\* $\mathsf { p } { < } . 0 5 .$  
Company dummies (<sup>fi</sup>xed effects for each of the 862 companies) used in estimating the model are not reported.  
\* pb.10.

Table 7  
Fixed effects estimation results for sentiment of individual social media and news

<table><tr><td rowspan="2">Variable</td><td>Coefficient (Std. Err.)</td><td>Coefficient (Std. Err.)</td></tr><tr><td>Model (b3)</td><td>Model (b4)</td></tr><tr><td colspan="3">Return equation: with abnormal return  $AR_{it}$  as dependent variable</td></tr><tr><td>Constant</td><td>-.0002 (.0002)</td><td>-.0003 (.0002)</td></tr><tr><td> $BLOG\_SENTI_{i,t-1}$ </td><td>.0002 (.0001)**</td><td>.0002 (.0001)**</td></tr><tr><td> $FORUM\_SENTI_{i,t-1}$ </td><td>-.00007 (.00004)*</td><td>-.00004 (.00005)</td></tr><tr><td> $TWEET\_SENTI_{i,t-1}$ </td><td>.00004 (.00003)</td><td>.00005 (.00003)*</td></tr><tr><td> $NEWS\_SENTI_{i,t-1}$ </td><td>.0001 (.0005)</td><td>.001 (.0006)*</td></tr><tr><td> $BLOG\_SENTI_{i,t-1}*NEWS\_SENTI_{i,t-1}$ </td><td></td><td>-.00004(.0002)</td></tr><tr><td> $FORUM\_SENTI_{i,t-1}*NEWS\_SENTI_{i,t-1}$ </td><td></td><td>-.00007 (.00005)</td></tr><tr><td> $TWEET\_SENTI_{i,t-1}*NEWS\_SENTI_{i,t-1}$ </td><td></td><td>-.0002 (.0001)**</td></tr><tr><td colspan="3">Risk equation: with idiosyncratic risk  $IR_{it}$  as dependent variable</td></tr><tr><td>Constant</td><td>-.03 (.001)</td><td>-.03 (.001)</td></tr><tr><td> $BLOG\_SENTI_{i,t-1}$ </td><td>.00003 (6.68e-6)***</td><td>.00003 (7.03e-6)***</td></tr><tr><td> $FORUM\_SENTI_{i,t-1}$ </td><td>-2.97e-06 (2.51e-06)</td><td>-1.57e-06 (2.65e-06)</td></tr><tr><td> $TWEET\_SENTI_{i,t-1}$ </td><td>.00001 (1.70e-06)***</td><td>.00001 (1.83e-06)***</td></tr><tr><td> $NEWS\_SENTI_{i,t-1}$ </td><td>.00002 (.00003)</td><td>.0001 (.00004)*</td></tr><tr><td> $BLOG\_SENTI_{i,t-1}*NEWS\_SENTI_{i,t-1}$ </td><td></td><td>-.00001(.00001)</td></tr><tr><td> $FORUM\_SENTI_{i,t-1}*NEWS\_SENTI_{i,t-1}$ </td><td></td><td>-1.15e-06 (2.57e-06)</td></tr><tr><td> $TWEET\_SENTI_{i,t-1}*NEWS\_SENTI_{i,t-1}$ </td><td></td><td>-8.85e-06 (5.41e-06)</td></tr><tr><td colspan="3">N = 49,807 Group = 824</td></tr></table>

Note: standard errors in parentheses.  
Company dummies (<sup>fi</sup>xed effects for each of the 824 companies) used in estimating the model are not reported.  
\*\*\* $\mathsf { p } \ll . 0 1 .$  
\*\* $\mathsf { \bar { p } } < . 0 5 .$  
⁎ pb.10.

Tables 6 and 7 that both volume and sentiment of Twitter posts are signi<sup>fi</sup>cantly positively related to risk. Only negative news mentions are found to have a marginally positive signi<sup>fi</sup>cant relationship with risk.

## 5. Discussion and conclusion

The effect of social media and conventional media, their relative importance, and their interrelatedness on short term <sup>fi</sup>rm stock market performances (e.g., return and risk) is of interest to academics, standard-

Fixed effects estimation results for sentiment of individual social media and news.

<table><tr><td rowspan="2">Variable</td><td>Coefficient (Std. Err.)</td></tr><tr><td>Model (c1)</td></tr><tr><td colspan="2">Return equation: with abnormal return  $AR_{it}$  as dependent variable</td></tr><tr><td>Constant</td><td>-.0003 (.0002)</td></tr><tr><td> $BLOG\_POS\_NUM_{i,t-1}$ </td><td>.0002 (.0001)**</td></tr><tr><td> $BLOG\_NEG\_NUM_{i,t-1}$ </td><td>-.00004 (.002)</td></tr><tr><td> $FORUM\_POS\_NUM_{i,t-1}$ </td><td>-.00004 (.00004)</td></tr><tr><td> $FORUM\_NEG\_NUM_{i,t-1}$ </td><td>-.003 (.001)***</td></tr><tr><td> $TWEET\_POS\_NUM_{i,t-1}$ </td><td>.00003 (.00003)</td></tr><tr><td> $TWEET\_NEG\_NUM_{i,t-1}$ </td><td>.00003 (.00005)</td></tr><tr><td> $NEWS\_POS\_NUM_{i,t-1}$ </td><td>.0002 (.0005)</td></tr><tr><td> $NEWS\_NEG\_NUM_{i,t-1}$ </td><td>.003 (.002)</td></tr><tr><td colspan="2">Risk equation: with idiosyncratic risk  $IR_{it}$  as dependent variable</td></tr><tr><td>Constant</td><td>.03 (.001)</td></tr><tr><td> $BLOG\_POS\_NUM_{i,t-1}$ </td><td>.00002 (6.75e-06)***</td></tr><tr><td> $BLOG\_NEG\_NUM_{i,t-1}$ </td><td>.0001 (.0001)</td></tr><tr><td> $FORUM\_POS\_NUM_{i,t-1}$ </td><td>-2.71e-06 (2.56e-06)</td></tr><tr><td> $FORUM\_NEG\_NUM_{i,t-1}$ </td><td>.00002 (.00005)</td></tr><tr><td> $TWEET\_POS\_NUM_{i,t-1}$ </td><td>.00001 (1.47e-06)***</td></tr><tr><td> $TWEET\_NEG\_NUM_{i,t-1}$ </td><td>9.62e-06 (2.86e-06)***</td></tr><tr><td> $NEWS\_POS\_NUM_{i,t-1}$ </td><td>.00002 (.00003)</td></tr><tr><td> $NEWS\_NEG\_NUM_{i,t-1}$ </td><td>.0002 (.0001)*</td></tr><tr><td colspan="2">N = 49,807 Group = 824</td></tr></table>

Note: standard errors in parentheses.  
Company dummies (<sup>fi</sup>xed effects for each of the 824 companies) used in estimating the model are not reported.

$$
\mathrm{p} <  . 0 1.
$$

setters and <sup>fi</sup>rms. In this study, we use both social media and conventional data to empirically evaluate the effect. With a sample of 52,746 messages from 824 <sup>fi</sup>rms from various social media and conventional media sources, we cover six industries including pharmaceutical, retail, software, savings institutions, health care, and hotel. Our <sup>fi</sup>ndings add to the literature on media's impact on <sup>fi</sup>rm stock performances. Speci<sup>fi</sup>cally, we show that overall social media sentiment has a stronger impact on <sup>fi</sup>rm stock performance than conventional media, while social and conventional media have a strong interaction effect on stock performance. These results highlight the importance of social media and conventional media (in a less degree) on <sup>fi</sup>rm stock performance and uncover the moderating relationship between these two types of media sources. Next, we examine whether the effect of social media on <sup>fi</sup>rm stock performance varies depending on social media type (e.g., blogs, Twitter, and forums). Specifically, using sentiment measures for each individual media, we <sup>fi</sup>nd that blog sentiment has a positive impact while forum sentiment has a negative impact on return. Additionally, both blog and Twitter sentiment are found to have a positive effect on risk. Further, we <sup>fi</sup>nd that the interaction effect between Twitter and news sentiment has a signi<sup>fi</sup>cant negative effect on returns and but not a signi<sup>fi</sup>cant effect on risk. Lastly, we examine the count of positive and negative count of media messages on stock performance to gather insights on the effect at a more detailed level. We document that positive blog posts have a strong positive impact on return while negative forum posts have a strong negative impact on return. We conjecture that blog messages contain more positive contents while forum messages are more negative oriented. Thus, better social media research may be associated with the quality in information availability and information processing.

In summary, our results do not suggest that textual analysis of various media sources will resolve, to paraphrase Roll [33], our profession's modest ability to explain stock returns. Our results, however, suggest that textual analysis can contribute to our ability to understand the impact of information from stock returns, and even if sentiment in media sometimes does not directly cause returns it might be an ef<sup>fi</sup>cient way for analysts to capture other sources of information. Another limitation lies in that we examine the overall media sentiment rather than being business domain (e.g., accounting or <sup>fi</sup>nance) speci<sup>fi</sup>c. We suggest that <sup>fi</sup>nancial and business intelligence researchers be cautious when relying on word classi<sup>fi</sup>cation schemes derived outside the domain of business usage. Applying non-business word lists to accounting and <sup>fi</sup>nance topics can lead to a high misclassi<sup>fi</sup>cation rate and spurious correlations.

Nevertheless, the study opens up avenues for future research that could examine media effects on <sup>fi</sup>rm stock performance applying speci<sup>fi</sup>c accounting or <sup>fi</sup>nance domain knowledge. Another area for future study is to explore the tone of the messages in various media sources and the extent of sentiment among the general public as compared to the sentiment among more sophisticated media practitioners such as analysts.

## References

[1] N. Archak, A. Ghose, P.G. Ipeirotis, Deriving the pricing power of product features by mining consumer reviews, Management Science 57 (8) (2011) 1485–1509.

[2] B. Bickart, R.M. Schindler, Internet forums as in<sup>fl</sup>uential sources of consumer information, Journal of Interactive Marketing 15 (3) (2001) 31–40.

[3] Q. Cao, W. Duan, Q. Gan, Exploring determinants of voting for the “helpfulness” of online user reviews: a text mining approach, Decision Support Systems 50 (2) (2011) 511–521.

[4] Q. Cao, M.A. Thompson, Y. Yu, Sentiment analysis in decision sciences research: an illustration to IT governance, Decision Support Systems 54 (2) (2013) 1010–1015.

[5] H. Chen, P. De, Y.J. Hu, B.H. Hwang, Customers as Advisors: The Role of Social Media in Financial Markets, 2012. Available at SSRN 1807265

[6] J.A. Chevalier, D. Mayzlin, The effect of word of mouth on sales: online book reviews, National Bureau of Economic Research, 2003.

[7] S.R. Das, M.Y. Chen, Yahoo! for Amazon: sentiment extraction from small talk on the web, Management Science 53 (9) (2007) 1375–1388.

[8] W. Duan, B. Gu, A. Whinston, Informational cascades and software adoption on the Internet: an empirical investigation, MIS Quarterly 33 (1) (2009) 23–48.

[9] W. Duan, B. Gu, A.B. Whinston, Do online reviews matter?—an empirical investigation of panel data, Decision Support Systems 45 (4) (2008) 1007–1016.

[10] W. Duan, B. Gu, A.B. Whinston, The dynamics of online word-of-mouth and product sales—an empirical investigation of the movie industry, Journal of Retailing 84 (2) (2008) 233–242

[11] G. Escudero, L. Marquez, G. Rigau, Naive Bayes and Exemplar-based Approaches to Word Sense Disambiguation Revisited, 2000, arXiv preprint cs/0007011.

[12] E.F. Fama, K.R. French, Common risk factors in the returns on stocks and bonds, Journal of <sup>fi</sup>nancial economics 33 (1) (1993) 3–56.

[13] A. Ghose, S.P. Han, An empirical analysis of user content generation and usage behavior on the mobile Internet, Management Science 57 (9) (2011) 1671–1691.

[14] E. Gilbert, K. Karahalios, C. Sandvig, The network in the garden: designing social media for rural life, American Behavioral Scientist 53 (9) (2010) 1367–1388.

[15] N. Godbole, M. Srinivasaiah, S. Skiena, Large-scale sentiment analysis for news and blogs, Proceedings of the International Conference on Weblogs and Social Media (ICWSM), 2007.

[16] D. Godes, D. Mayzlin, Using online conversations to study word-of-mouth communication, Marketing Science 23 (4) (2004) 545–560

[17] D. Godes, D. Mayzlin, Y. Chen, S. Das, C. Dellarocas, B. Pfeiffer, B. Libai, S. Sen, M. Shi, P. Verlegh, The <sup>fi</sup>rm's management of social interactions, Marketing Letters 16 (3) (2005) 415–428.

[18] D. Gruhl, R. Guha, R. Kumar, J. Novak, A. Tomkins, The predictive power of online chatter. Proceedings of the eleventh ACM SIGKDD international conference on Knowledge discovery in data mining, ACM, 2005, pp. 78–87.

[19] M. Joshi, D. Das, K. Gimpel, N.A. Smith, Movie reviews and revenues: an experiment in text regression, Human Language Technologies: The 2010 Annual Conference of the North American Chapter of the Association for Computational Linguistics, Association for Computational Linguistics, 2010, pp. 293–296.

[20] E. Kyriazidou, Estimation of dynamic panel data sample selection models, Review of Economic Studies 68 (3) (2001) 543–572.

[21] D. Lewis, Naive (Bayes) at forty: the independence assumption in information retrieval, Machine Learning (1998) 4–15, ECML-98.

[22] N. Li, D.D. Wu, Using text mining and sentiment analysis for online forums hotspot detection and forecast, Decision Support Systems 48 (2) (2010) 354–368.

[23] B. Liu, Sentiment analysis and subjectivity, Handbook of Natural Language Processing (2010) 627–666.

[24] Y. Liu, X. Huang, A. An, X. Yu, ARSA: a sentiment-aware model for predicting sales performance using blogs, Proceedings of the 30th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, 2007, pp. 607–614.

[25] X. Luo, J. Zhang, W. Duan, Social media and <sup>fi</sup>rm equity value, information systems research, (forthcoming).

[26] G. Mishne N. Glance Leave a reply: an analysis of weblog comments Third Annual Workshop on the Weblogging Ecosystem, 2006.

[27] O. Netzer, R. Feldman, J. Goldenberg, M. Fresko, Mine your own business: market-structure surveillance through text mining, Marketing Science 31 (3) (2012) 521–543.

[28] K. Nigam, R. Ghani, Analyzing the effectiveness and applicability of co-training, Proceedings of the Ninth International Conference on Information and Knowledge Management, ACM, 2000, pp. 86–93.

[29] A. Pak, P. Paroubek, Twitter based system: using Twitter for disambiguating sentiment ambiguous adjectives, Proceedings of the 5th International Workshop on Semantic Evaluation, Association for Computational Linguistics, 2010, pp. 436–439.

[30] B. Pang, L. Lee, A sentimental education: sentiment analysis using subjectivity summarization based on minimum cuts, Proceedings of the 42nd Annual Meeting on Association for Computational Linguistics, Association for Computational Linguistics, 2004, p. 271.

[31] B. Pang, L. Lee, Opinion Mining and Sentiment Analysis, 2008, (Now Pub)

[32] T. Pedersen, A simple approach to building ensembles of Naive Bayesian classi-<sup>fi</sup>ers for word sense disambiguation, Proceedings of the 1st North American chapter of the Association for Computational Linguistics conference, Association for Computational Linguistics, 2000, pp. 63–69.

[33] R. Roll, R2, Journal of Finance 43 (2) (1988) 541–566.

[34] J.C. Short, T.B. Palmer, The application of DICTION to content analysis research in strategic management, Organizational Research Methods 11 (4) (2008) 727–752.

[35] G.P. Sonnier, L. McAlister, O.J. Rutz, A dynamic model of the effect of online communications on firm sales, Marketing Science 30 (4) (2011) 702–716

[36] S. Srinivasan, D. Hanssens, Marketing and <sup>fi</sup>rm value: metrics, methods, <sup>fi</sup>ndings, and future directions, Boston U. School of Management Research Paper No. 20o9-6 2008

[37] A. Stephen, J. Galak, The Complementary Roles of Traditional and Social Media Publicity in Driving Marketing Performance, 2010.

[38] S. Tong, D. Koller, Support vector machine active learning with applications to text classi<sup>fi</sup>cation, Journal of Machine Learning Research 2 (2002) 45–66.

[39] P.D. Turney, Thumbs up or thumbs down?: semantic orientation applied to unsupervised classi<sup>fi</sup>cation of reviews, Proceedings of the 40th Annual Meeting on Association for Computational Linguistics, Association for Computational Linguistics, 2002, pp. 417–424.

[40] A. Wright, Mining the Web for feelings, not facts, New York Times 24 (2009).

![](/api/attachments/PS9RFPJ8/fulltext/images/cd311ba60538b9405ffae42d6b538761b6bc8ec48820bd5b76ada2c37fffa225.jpg)

Yang Yu is currently an MIS Ph.D. candidate in the Rawls College of Business at Texas Tech University. Yang also holds a Management Science and Engineering Ph.D. from the School of Economics and Management at Beijing University of Aeronautics & Astronautics. Yang's research interests include social media, business intelligence, IT security and supply chain information systems. He has published papers in journals such as Decision Support Systems, Information Systems and E-Business Management. He has been awarded the Best Interdisciplinary Research Award at the Decision Sciences Institute Conference (DSI), 2012.

![](/api/attachments/PS9RFPJ8/fulltext/images/4ed0d38386c59b2585afb6f340e693929a49ba341708c67adf0114e29e5b48c3.jpg)

Wenjing Duan, Associate Professor of Information Systems & Technology Management, received her Ph.D. in Information Systems from University of Texas at Austin in 2006. Wenjing's research interests glide the intersections between Information Systems, Economics, and Marketing. Among her primary research interests are the social and economic impact of online consumer-generated content and social media, online commu nities and online social network, information systems and marketing, and healthcare and IT. Wenjing has published in MIS Quarterly, Information Systems Research, Communications of ACM, Journal of Retailing, Decision Support Systems, among others. She is also the recipient of the Emerald Management Reviews Citations of Excellence Awards, NET Institute Research Grant, and serves on the Editorial Board of the Decision

Support Systems. For more details, see http://home.gwu.edu/\~wduan/.

![](/api/attachments/PS9RFPJ8/fulltext/images/1418e757c54aca46ab325f65f8dd9336f5d397b0a322dddc70300e49ed6c2b1f.jpg)

Dr. Qing Cao is the Jerry Rawls Professor of Management Information Systems at the Rawls College of Business, Texas Tech University. He holds a Ph.D. from the College of Business Administration at the University of Nebraska (2001). His research interests include IT governance, supply chain information management, strategic alignment, and business intelligence. Dr. Cao was the recipient of the University of Missouri-Kansas City Trustee's Faculty Research Award (2005). Dr. Cao has received the 2012 Chancellor's Council Distinguished Research Award at Texas Tech University. He is also a recipient of the Best Interdisciplinary Research Award at the 43rd Annual Decision Sciences Institute (DSI) Conference 2012. Dr. Cao has published more than 42 research papers in top business journals such as Journal of Operations Management, Decision Sciences, Decision Support Systems, Communications of ACM. International Iournal of Production Research. European Journal of Operational Research, among many others. Dr. Cao also served as the Associ ate Program Chair at the Decision Sciences Institute (DSI) Annual Meeting in 2008.
