---
otero_id: 20451
otero_key: "3DK65U8T"
title: "A social investing approach for portfolio recommendation"
authors: "Yung-Ming Li; Lien-Fa Lin; Chin-Yu Hsieh; Bo-Syun Huang"
year: "2021"
journal: "Information & Management"
doi: "10.1016/j.im.2021.103536"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A social investing approach for portfolio recommendation

![](/api/attachments/3DK65U8T/fulltext/images/b7d8432da3f6d61df6eb5769721aa1a480bdcea49ea6a54efcd723d5bf13e936.jpg)

Yung-Ming Li <sup>a,\*</sup>, Lien-Fa Lin <sup>b</sup>, Chin-Yu Hsieh <sup>a</sup>, Bo-Syun Huang a

<sup>a</sup> Institute of Information Management, National Yang Ming Chiao Tung University, Hsinchu, 300, Taiwan

<sup>b</sup> Department of Digital Media Design, Asia University, Taichung, 413, Taiwan

## A R T I C L E I N F O

Keywords: Social network Text mining Investment portfolio creation Collective intelligence Decision support system

## A B S T R A C T

Presently, people use social media at a greater rate to share their personal investment experiences. This plentiful user-generated data source has been promisingly used by investors for portfolio creation. A new type of investing platform that allows investors to copy the portfolios of experienced investors has grown dramatically. In this research, we propose a collective intelligence mechanism that can extract and consolidate the opinions expressed over the social investing platform and generate appropriate portfolios by analyzing other investors’ knowledge, authority, and opinions toward the investment target. The experimental results obtained based on the social investing platform eToro.com reveal that the portfolio recommended by the proposed mechanism outperforms the market index and other benchmark approaches in various financial performance aspects.

## 1. Introduction

In the past, people invested their unused cash at central banks and hoped to receive a small amount of interest in return. But now, the central banks charge a fee with negative interest rates, instead [12]. From the European Central Bank to Japan’s central bank, a negative interest rate policy has become a trend around the world. Hence, people tend to secure their money in investments instead of savings. However. although the annual return of the S&P 500 Index averaged 9.85% for the recent twenty years, the average equity fund investors only earned a market return of 5.19%. Investor behavior is sometimes illogical and often based on emotions [5]. This does not lead to wise decisions on long-term investments.

Two main behaviors cause investors to earn below average market returns. First, buying high. A study reveals that when the stock market goes up, investors put more money into it. And when it goes down, they pull money out. This irrational behavior causes an investor’s market return to be substantially less than historical stock market returns [14]. Second, overreacting. This problem is that human reaction to good news or bad news is to overreact [13]. This emotional reaction causes illogical investment decisions. The avoidance of irrational financial decisions is an essential issue – whether in the study of behavioral finance [4,16] or in the development of decision technology.

Owing to the rapid development of Web 2.0 technologies, more people are using social networking platforms to express their personal experiences. A new type of social platform that focuses on investing activities has recently grown dramatically because of the global investing environment. A social investing platform makes it possible for users to build portfolios based on the experience and knowledge shared by other credible investors. As a result, novice investors can easily become involved in investing activities through a social investing plat form. A Nielsen Global Online Consumer Survey indicated that 70% of people trust the online reviews posted by strangers [43]. Online reviews have become a new and useful source of information that allows investors to analyze people’s opinions and find a good investment port folio planning strategy.

The opinions that are aggregated from the large crowd have equal o superior quality to those contributed by experts in the domain. A study by the MIT Media Lab at the Massachusetts Institute of Technology found that crowd-sourced investment boosted returns [34] The study found that returns were increased more than 10% compared to those who traded without guidance from the social network and 4% higher than for those who only followed the highest-performing gurus. In addition, there is already a new kind of exchange-traded fund (ETF) based on the vote of crowds which is called the wisdom exchange-traded fund (WIZE). It aims to use the wisdom of the crowd for investing in stocks by analyzing public sentiment extracted from an iPhone app. The CrowdInvest Wisdom Index was down 0.56% on its first anniversary (ending January 7, 2016); however, during the same time frame, the S&P 500 was down 2.04%.

Traditional investment methods can be generalized into three types: self-learning, finding a financial consultant, and social discussion.

Despite the method used, investors have to study and build an invest ment portfolio. Portfolio building can be divided into three parts: designing the portfolio, making investments, and maintaining the portfolio. Investors require much time for all of this work. A new in vestment approach—a copy and paste strategy to follow experienced investors in the social investing platform—has presently become a trend. For example, eToro.com is a popular social investing platform that is simple and easy to use. On November 5, 2015, eToro merged its OpenBook social investing platform and their WebTrader trading plat form to be a brand-new portfolio management platform, packed with all the trading tools for investors to manage their trading portfolio. Through the WebTrader, users could view live rates, change trade settings, and edit stop-loss and take-profit orders. OpenBook was a social platform containing a community of 4.5 million traders. With OpenBook’s social infrastructure, an investor can connect with other experienced investors in the eToro network and acquire their collective wisdom [6].

However, there is too much information and discussion displayed on a social investing platform. Although users can see the reviews of each trader on eToro, it is too difficult for the beginner to understand and choose suitable stocks from several investment targets. An investor who follows popular investors cannot certainly make a benefit, as even highperformance investors sometimes still have irrational behaviors when making a decision. Although a social investing platform can help in vestors to follow other investors’ actions, the selection of the investing targets requires careful evaluation. Hence, in this research, we aim to build collective intelligence to create stock portfolios by analyzing the opinions and discussions of investors expressed on the social investing platform. With the support of the proposed mechanism, an investor does not have to spend much time to understand financial knowledge or to read in depth a huge amount of reviews.

There is a broad range of investment decision support systems, ranging from providing better informational insights for an investor to very specific actionable investment support. However, few investment decision support systems analyze the crowd reviews contributed by in vestors on a social investing platform to derive investment decisions; even though research indicates that valuable insights can be expected. In this research, we propose a stock portfolio recommendation mechanism based on the collective intelligence extracted from the social investing platform. With the recommended portfolio, we can make good use of asset allocation and reduce the damage. Even when some of the in vestment targets are pessimistic, the decision-making support can still help people make a profit. The proposed mechanism is capable of sup porting investors as they build a promising investment portfolio. In vestors with little financial knowledge can receive helpful decision support and avoid irrational behaviors.

The remainder of this paper is organized as follows: Section 2 dis cusses the literature related to our research. Section 3 presents the sys tem framework of the proposed social intelligence mechanism for stock recommendation. Section 4 describes the data collection, processing, and experiments. Section 5 demonstrates and evaluates the experi mental results. Finally, Section 6 summarizes the research contributions and discusses the research limitations and future work.

## 2. Related literature

## 2.1. Collective intelligence in finance

There are already many enterprises that use the wisdom of crowds to provide a reliable source for business strategies [8]. Nowadays, even stock trading strategies can be constructed based on collective wisdom Avery et al. [3] studied the predictive power of the wisdom of crowds by analyzing 2.5 million stock picks. They studied whether the stocks ranked higher by the system that performed better than lower ranked stocks and found that community predictions provide effective result [10]. Research conducted by Hill and Ready–Campbell [21] analyzed CAPS data and found evidence that a portfolio based on the wisdom of crowds performs better than the market index (S&P 500).

Literature also indicates that the data of investment platforms can be effectively used to predict stock trends. For example, research by Eickhoff and Muntermann [15] found that the investor opinions expressed in social media can predict future stock returns and earn surprises. Antweiler and Frank [2] studied the effect of more than 1.5 million messages posted on Yahoo! Finance and found evidence that the wisdom of crowds can be used to predict stock market trading volume, volatility, and even returns. Bollen et al. [10] investigated whether measurements of collective mood states derived from Twitter messages were correlated to the value of the Dow Jones Industrial Average (DJIA) and found an accuracy of 86.7% in predicting the daily up and down changes in the closing values of the DJIA and a reduction of the mean average percentage error (MAPE) by more than 6%. Motivated by these studies, we aim to derive collective intelligence from the social investing platform to create investment portfolios for different risk preference types of investors. The way we extract the financial collective intelli gence is based on the analysis of collective mood states derived from the posts contributed by the investors on the target investment forum of the investment platform.

## 2.2. DSS for investment

A decision support system (DSS) is a computer-based information system that supports business or investment decision-making. Kuo et al. [26] proposed an intelligent stock trading decision support system with a good buy-sell performance through the integration of a genetic algo rithm based on a fuzzy neural network and an artificial neural network. Luo et al. [32] developed a multi-agent decision support system, which was proven to be a viable solution for distributed problem solving and for stock trading. Financial decision support systems could also be used to solve the portfolio selection problem with techniques such as a genetic algorithm. Hargreaves et al. [20] developed a stock portfolio se lection method by using neural network and logistic regression approaches for data mining and proved that the proposed method per forms better than the market index in the healthcare and financial category with 18% and 1%, respectively. Chan et al. [11] examined monthly returns following the public news and found a strong drift after bad news. Kim et al. [24] used a method of mining text opinions to analyze news to predict rises and falls in the KOSPI (Korea Composite Stock Price Index). They found that the result extracted from their system is very useful in predicting stock market movements. Various ap proaches for investment portfolio recommendation have been developed by analyzing different types of data sources, such as market information [30], company financial information [39], and news/re views [15]. In this study, we use the text mining technique and collective intelligence as the base of the decision support system. We use the social investment approach to make investment portfolio recommendations by deriving collective intelligence from the social investing platform, and by analyzing investment activities and posts of important investors. The proposed mechanism is built to derive useful information from the shared posts and help an investor to solve the portfolio selection problem.

## 2.3. Text mining techniques

The implementation architecture of text mining could be divided into three parts: market data collection, preprocessing, and a machine learning algorithm [47]. Preprocessing is the most important part and directly affects the effectiveness of the mining result. It contains three steps: feature selection, dimensionality reduction, and feature repre sentation [30]. One of the biggest obstacles in preprocessing is feature selection, where a subset of relevant features for building accurate prediction models are to be selected [44]. The most general method is known as the ‘‘bag-of-words’’ which breaks down the text of the review into many single words and uses each of them as a feature [46]. Another technique known as Latent Dirichlet Allocation (LDA) is less frequently used, but interesting; it is a generative statistical model that allows sets of observations to be explained by unobserved groups that explain why some parts of the data are similar [9].

In machine learning, if the number of features is too large, it may cause some problems, such as overfitting and slow processing speed, which may decrease the efficiency of machine learning algorithms [36] Dimensionality reduction, which reduces the number of features, can avoid these questions. The goal of variable selection is threefold: to improve the predictive performance of predictors, provide faster and more cost-effective predictors, and better understand the underlying process of generating data [19]. There are other steps in dimensionality reduction: stemming and the removal of punctuation, numbers, and stop words [17]. After determining the minimum number of features, the feature representation step aims to transfer the features into a numeric value to use for further analysis. The most common technique is Bool ean; it uses two numbers like 0 and 1 to represent the absence or pres ence of a feature in the sentence [27]. There is another very popular technique, namely the term frequency-inverse document frequency (TF-IDF), which is a numerical statistical approach that is intended to reflect how important a word is to a document in a collection or corpus [1]. In this research, we implement the common steps in text mining approaches to analyze the posts of investors. All these posts will be analyzed by the preprocessing task which contains the following steps: feature selection, dimensionality reduction, and feature representations.

## 2.4. Sentiment analysis

Recently, sentiment analysis has been used in the data mining area as a technique for improving prediction accuracy. This technique is also known in the field of text mining as opinion mining or review mining [45]. For example, Reyes and Paolo [38] collected the reviews from Amazon and used sentiment analysis and opinion mining techniques for purchase decision-making [18,38]. These decisions are usually valuable because the opinions expressed by the crowd are less likely to be biased and can be the basis for stock market prediction [15].

In the area of stock market prediction, there is an important issue, which is to classify the posts into positive sentiment, negative sentiment, or neutral/irrelevant sentiment [35]. With the application of sentiment analysis, the prediction results will be more useful. Gu et al. [18] used comments posted on Yahoo! Finance’s discussion board to predict the returns of stocks based on sentiment analysis and found approximately a 4% increase in returns over one month. Mittal and Goel [28] found that stock market prediction is available by aggregating millions of tweets posted on Twitter and got a 75.56% accuracy. As the above studies suggest, we suggest that positive opinions will reflect optimistically on future stock performance. In this research, we use the opinion mining approach to derive public mood for the specific investment targets.

## 3. The system framework

We developed a decision support mechanism for investment port folio recommendation that uses collective intelligence extracted from a social investing platform. The proposed mechanism can find and aggregate the experience and knowledge of credible investors to generate investment strategy and improve the performance of average equity fund investment. Specifically, it can be used to help investors who are beginners in the field of finance and lack specialized knowledge. The process flow of our proposed mechanism is shown in Fig. 1 and detailed as follows:

Step 1, when searching the investment targets, investors should make a decision based on their own risk preference. An investor is asked to reveal his/her preference. Investors’ preferences will be classified into three groups (risk taker, risk neutral, and risk averter).

![](/api/attachments/3DK65U8T/fulltext/images/eb72de22ff8ea3ac4e54c557487a2c3f12af02b7973f56052362ed4aa7efb60e.jpg)  
Fig. 1. The processes of our proposed mechanism.

Step 2, the system extracts collective intelligence from the investors posts and historical data on the social investing platform. We analyze the features, sentiment, knowledge, and authority of the extracted posts related to investment targets.

Step 3, the system integrates various evaluation scores of all the posts regarding each investment target and constructs different types of investment portfolios. The recommended portfolio list will contain top-ranked stocks.

Step 4, customized portfolios are created for the investors in accor dance with their risk preference. A requesting investor could use the recommended portfolio for decision-making support and provide feedback reviews to the social investing platform.

The system framework is depicted in Fig. 2. There are six main modules in the system that are described as follows:

(1) Feature Dictionary Construction Module: We collected all of the posts on each investment target (e.g., stock) from eToro.com as the data for further analysis. After that, we constructed a feature dictionary to arrange important words from these reviews. The feature dictionary will be used to evaluate the knowledge rele vance of a post.

(2) Sentiment Analysis Module: This module is used to analyze public opinions regarding the investment targets. Investors usually use subjective words (e.g., good, perfect, bad, and terrible) to express their emotions in comments. Sentiment analysis is used in this module to understand whether they are optimistic or pessimistic about the stock.

(3) Knowledge Analysis Module: This module is used to analyze the credibility of investors by evaluating the relevance of their knowledge to the investment target according to the transaction history of the post’s writer and the intensity of keywords included in the post. The module considers two factors; domain score and keyword score – to measure the knowledge relevance of each investor. The reviewing investors who get higher scores have higher knowledge credibility regarding this investment target.

![](/api/attachments/3DK65U8T/fulltext/images/501caaa9730f8580af7c2151785f703d466a9f75bbe9a3c76a301f22e62ee064.jpg)  
Fig. 2. The System Framework.

(4) Influencer Analysis Module: The reviewers’ degree of authority can also be used to measure the credibility of each investor. We analyze the relationship between investors and identify those who have more influence than others [25]. This module considers two common social factors (celebrity score and rating score) to measure a reviewer’s authority. The reviewing investors who get higher scores have higher credibility of authority regarding this investment target.

(5) Financial Statement Analysis Module: In this module, we consid ered important financial indexes of a company to evaluate the value of the investment target, including profitability analysis, operating ability analysis, capital structure analysis, and liquidity analysis.

(6) Investment Portfolio Construction Module: By aggregating the opinions collected from reviews, we will recommend a reliable investment portfolio to help users make a decision. In this mod ule, each user’s risk preference will be considered to generate a customized recommendation list.

## 3.1. Feature dictionary construction module

This module can be divided into two parts; the first part is to extract data from the social investing platform and the second part is feature selection. An example of the feature dictionary is shown in Fig. 3. It contains the ranked features that represent important words.

Data Extraction: This study first extracts all the posts from the forum of each investment target on the social investing platform. To reduce the complexity of the analysis, we only analyzed the posts written in En glish. Therefore, in this phrase, the main task is to filter out non-English posts because the website could be registered by people around the world.

Feature Selection: After extracting the posts, we used the data to build the dictionary. The most common technique used is “bag-of-words” which breaks the text into words and considers each of the words as a feature. However, it would cause a noise problem as it contains too many meaningless words. So, we use stop-word removal and stemming to filter the features. Stop-word removal involves removing meaningless words such as $" { \bf a } , " \ \mathrm { \bf " } { \bf i } { \bf s } , "$ and “of.” Stemming refers to the process of identifying the root of a certain word. For example, happy and happiness stand for the same opinion. The two words should be considered as the same feature. Finally, we used POS (part of speech) tagging to record the part of speech of each feature and used the TF-IDF method to analyze the importance of each feature keyword. The feature dictionary includes the keywords of high importance measured by their TF-IDF scores.

## 3.2. Sentiment analysis module

This module aims to aggregate public opinions to predict the trend of stocks. Investors usually use opinion words (e.g., good, nice, bad, terrible) to express their thinking about future prediction. The investment target with more positive comments would have better performance in the future. To infer the investors’ emotions on an in vestment target, we used sentimental analysis to recognize the words as positive, negative, or neutral. The experiment process includes two phrases:

![](/api/attachments/3DK65U8T/fulltext/images/05d3591bb074a278724d00bde02d91f3e6b8da28ffb0f983d15f59e8c1d2b3f5.jpg)  
Fig. 3. The structure of the feature dictionary.

Sentiment recognition: In this step, we recognized the sentimental polarity of the opinion words. We used the data of Loughran and McDonald Sentiment Word Lists to determine the polarity of each word [33]. It is a repository of accounting and finance words containing 85, 132 words that are already classified into three groups (positive, nega tive, and uncertainly). The most common technique is to mark the positive opinion word as 1, negative as -1, and neutral as 0.

Sentiment measurement: In this step, we measured the sentiment po larity of a post. After marking the sentiment polarity of each word, we used this data to evaluate the sentiment score of each post. We first calculated the ratio of the number of positive words minus the number of negative words in each sentence and then summed up all the scores of all the sentences in the post as the financial sentiment:

$$
f i n a n c i a l \_ s t e n t i m e n t (p _ {i}) = \sum_ {s e p _ {i}} \frac {\sum_ {P _ {i} e s} S T (P _ {i}) + \sum_ {N _ {j} e s} S T (N _ {j})}{T o t a l n u m b e r o f w o r d s i n s e n t e n c e s}\tag{1}
$$

where $P _ { i }$ is a positive word $( S T ( P _ { i } ) = 1 )$ and $N _ { j }$ is a negative word $( S T ( N _ { j } ) ~ = ~ - ~ 1 )$ in a sentence.

Moreover, we used Textblob, a python package used for natural language processing, to calculate the review sentiment based on the collected reviews. Finally, the average of these two types of sentiment as the final sentiment score of each post was obtained as

$$
\text { SentimentScore } (p _ {i}) = \frac {\text { financial\_stentiment } (p _ {i}) + \text { review\_sentiment } (p _ {i})}{2}\tag{2}
$$

## 3.3. Knowledge analysis module

The main purpose of this module is to evaluate the credibility of posts according to the professional level of authors. This study considers two factors: domain score and keyword score to measure the knowledge degree.

## 3.3.1. Domain score

When people usually spend more time on interesting topics and accumulate more experience, they have more knowledge in the specific domain than other traders. We can speculate each investor’s investment preference by analyzing his/her historical trading records. If an investor usually concentrates on some investment topic, it indicates that this investor is interested in such an investment category. Fig. 4 indicates a partial category tree constructed from eToro.com. It classifies the in vestment targets into different groups.

This study calculates the ratio of historical trading for the investment target category made by an investor. The domain score of a user u for an investment target t is measured as

$$
D S (u _ {i}, t) = \frac {\sum_ {r _ {t} \in T _ {i}} c (r _ {t})}{| T _ {i} |}\tag{3}
$$

where $T _ { i }$ indicates the set of transactions by user $u _ { i } ,$ , t stands for the in vestment target, and c(r ) represents the quantity of each trading r belonging to the category of investment target t. For example, suppose the analysis target is “Stocks”, and if the user $u _ { i }$ has performed transactions for a total of 10 times, 2 for Technology, 3 for Healthcare, 1 for Gold, and 4 for SPX500, then the domain score of u for Stocks will be 0.5 $\left( { \frac { 2 + 3 } { 1 0 } } = 0 . 5 \right)$

![](/api/attachments/3DK65U8T/fulltext/images/8b13c89dd28f660402247eec3eb2bdb68034e71c5d4f24b28d12c9a47e427866.jpg)  
Fig. 4. The tree structure of preference category.

## 3.3.2. Keyword score

A common way to determine the knowledge degree of a reviewer is to count how many posts a reviewing investor contributed in the target category; but this may have some problems. For example, when an investor writes many posts in the target category, but those posts are full of meaningless sentences, the counting approach would be unsuitable for evaluating the degree of a person’s expertise. Hence, our mechanism analyzes the content of posts instead. If a post includes many sentences containing the keywords, the post would be more important [31]. The knowledge score of u for t can be measured as:

$$
K S (u _ {i}, t) = \frac {\left| \left\{s \mid s \epsilon \phi_ {i , t} , \exists k \epsilon s , F \right\} \right|}{\left| \phi_ {i , t} \right|}\tag{4}
$$

where $\phi _ { i , t }$ contains all the sentences related to t in the posts written by u ; s is a sentence in this post; and F stands for the set of keywords in the feature dictionary. The numerator of Eq. (4) is the number of sentences that contain feature keywords in the post.

## 3.4. Influencer analysis module

The degree of investors’ influence can also be used to measure the value of their posts. This module uses two factors; celebrity score and rating score – to measure an investor’s authority and influence.

## 3.4.1. Celebrity score

This factor is used to measure the degree of credibility of investors by computing their social relationships. The more social relationships that have been built with other people, the greater the investor’s influence power. We used the following social links to calculate the celebrity degree.

Explicit link: Explicit link represents the direct relationship between two investors. In most of the social platforms, people can use the “follow” function to receive the latest news of the person they are following. Even though both links of out-degree (follow people) and indegree (been followed) can be recognized, out-degree is easily manip ulated by man-made ways. Thus, this research only adopts in-degree to calculate the explicit link. The celebrity in the explicit link of an investor is measured as:

$$
E L (u _ {i}) = \frac {f _ {i} - \min (\varnothing_ {f})}{\max (\varnothing_ {f}) - \min (\varnothing_ {f})} * (n e w \_ m a x - n e w \_ m i n) + n e w \_ m i n\tag{5}
$$

where $f _ { i }$ stands for the number of followers that the user u has and $\varnothing _ { f }$ represents the set of followers of each user. New max and new min are the new intervals of $E L ( u _ { i } )$ ). The value should be normalized to be in the interval between 0 and 1.

Implicit link: Implicit link means there is an indirect relationship between two investors. If they participate in the same activity, it could be recognized that they have an implicit link from this activity. If a person commented on the post, there is a relationship between the author and the person who wrote the comment. When a post receives many comments, it indicates that the post contains useful information or some of the keywords attract other investors’ attention. The celebrity in the implicit link of an investor is measured as

$$
I L (u _ {i}) = \frac {c _ {i} - m i n (\emptyset_ {c})}{m a x (\emptyset_ {c}) - m i n (\emptyset_ {c})} * (n e w \_ m a x - n e w \_ m i n) + n e w \_ m i n\tag{6}
$$

where $c _ { i }$ stands for the number of comments that the user u receives in his/her post and $\varnothing _ { c }$ represents the set of comments in each post.

By combining explicit links and implicit links that construct the relationship network, we can evaluate the celebrity score of an investor as:

$$
C S (u _ {i}) = \alpha * E L (u _ {i}) + (1 - \alpha) * I L (u _ {i})\tag{7}
$$

## 3.4.2. Rating score

Most of the social platforms provide the rating mechanism for eval uating each article. For example, users can choose 1 to 5 stars to represent their favorite degree. Another common way for evaluating whether an article is good or bad is by the quantity of “likes.” However, the evaluation of experts may have more value than that of the public [25]. Therefore, rating scores of experts should get higher weight. Eq. (8) is used to calculate the rating score of an investor, which considers the importance of the other investors who pressed the “like” button. The importance is measured by an investor’s profit ratio.

$$
R S (u _ {i}) = \frac {\sum_ {u _ {k} \in \theta_ {l}} \pi_ {u _ {k}}}{| \theta_ {l} |}\tag{8}
$$

where $\theta _ { l }$ means that the set of users who “likes” the posts investor u published. And we use profit ratio $\pi _ { u _ { k } }$ as the index to evaluate the expert degree of user u .

## 3.5. Financial statement analysis module

The financial statements are formal records of a company’s financial activities. In this module, we analyze important financial indexes of a company to evaluate the Financial Statement Score (FSS) of the in vestment target, including profitability analysis, operating ability anal ysis, capital structure analysis, and liquidity analysis [39].

Profitability: Profitability is an indicator that evaluates the ability to earn money by the companies. This indicator shows the ability of the companies which use their assets to create profits. In our study, we used two ratios to evaluate the probability of the company:

Return on Total Assets Ratio (ROTA): This ratio is used to measure the efficiency of a company to generate earning.

Earnings Per Share (EPS): The EPS indicator is the monetary value of earnings per share for a company’s common stock.

Operating Ability: The ability of operating performance is an indicator based on the ratio of items on the balance sheet. It can evaluate the efficiency of assets used by a company and help us to understand the ability of business management. In our study, we used four indicators to evaluate the ability of operating performance:

Receivables Turnover Ratio (RTR): The RTR indicator is an activity ratio that measures how efficiently a company uses its assets.

Inventory Turnover (IT): The IT indicator measures the number of times an inventory is sold or used in a year.

Capital Structure: In financial terminology, capital structure is the way a corporation finances its assets through some equity and debt. It shows the degree of dependence on debt by the company. In our study, we considered two indicators to evaluate the capital structure:

Debt Asset Ratio (DAR): The DAR indicator indicates the percentage of assets of a company that are formed through debt. The higher the ratio, the greater is the risk in company operation.

Long Term Funds to Fixed Assets (LTFFA): The LTFFA indicator is a ratio to measure whether a company properly use their funds. It is calculated by dividing its long-term funds by total net fixed assets of a company.

Liquidity: The purpose of liquidity analysis is to help us to understand the ability of working capital creation of a company and short-term debt paying ability. It is an important indicator to evaluate the effectiveness of the assumption going concern. In this study, we use the current ratio and quick ratio to analyze the liquidity of a company:

Current Ratio (CR): The CR indicator is a ratio that is used to measure the liquidity of a company. It measures the ability of a company to pay short-term and long-term liabilities.

Quick Ratio (QR): The QR indicator is a ratio that is used to measure indicator of the short-term liquidity of a company. It measures the ability of a company to meet its short-term liabilities with its liquid assets.

We calculated the financial statement score by aggregating these eight indicators. This score shows the robustness of the operating com pany. The financial statement score is calculated as Eq. (9) and the value is normalized to the interval between 0 and 1.

FS<sup>′</sup><sub>j</sub> j∈n Financial statement score 8

$$
\text { where } n \in \{\text { ROTA }, \text { EPS }, R T R, I T, D A R, L T F F A, C R, Q R \}\tag{9}
$$

post $p _ { i } .$ Besides, to handle the temporal effects of sentiments, we used the basic power function to obtain the time decay rate (td(∙)) for a specific time as follows:

$$
t d \left(d _ {p}\right) = \theta^ {- \left(\frac {d _ {c} - d _ {p}}{3 0}\right)}\tag{12}
$$

where $d _ { c }$ notes the current date, $d _ { p }$ denotes the post date of p $\cdot \frac { d _ { c } - d _ { p } } { 3 0 }$ is used to estimate the difference of months between d and $d _ { p } { } _ { : }$ , and the variable θ is a constant parameter of the time decay function. We obtained different decay effects by adjusting the value of θ. The value of θ can be determined by sequential tests and practical experience. Hence, we calculated the important score of each post on the investment target and the value was normalized to the interval between 0 and 1:

$$
\begin{array}{l} \text { PostImportance } (p _ {i}, t) = t d \big (d _ {p _ {i}} \big) * S e n t i m e n t S c o r e (p _ {i}) * (\alpha D S (A u (p _ {i}), t) + \beta K S (A u (p _ {i}), t) + \gamma C S (A u (p _ {i})) + \delta R S (A u (p _ {i}))) * F S S (t) \\ t \in \Phi = \{\text { All   investment   targets   discussed   in   post } p _ {i} \} \end{array}\tag{13}
$$

## 3.6. Investment portfolio construction module

The more optimistic the comment on the specific target, the higher the opportunity that the target would perform better in the future. Therefore, we used sentiment analysis and incorporated authority and knowledge analysis to build the list of recommendation stocks as the investment portfolio. The list of recommendations is further customized in accordance with each investor’s risk preference.

## 3.6.1. User preference consideration

This study assumes that the risk preference of investors is of three types (risk taker, risk neutral, and risk averter). Therefore, we divided the stocks into three groups to match the risk preference. Specifically, we used beta analysis to evaluate each stock’s risk. Beta is one of the important measures of equity market volatility, and an index that shows the relationship of stocks to the financial market. For example, if beta of equity is more than 1, it represents that the investment target will outperform the market when the market is going up and underperform when the market is going down. Beta could be a measure of risk: the higher the beta of a company, the higher the expected return should be to compensate for the excess risk caused by volatility. Eq. (10) is used to calculate the beta of each stock.

$$
B e t a _ {i} = \frac {\text { Covariance } (r _ {i} , r _ {m})}{\text { Varience } (r _ {m})}\tag{10}
$$

It is calculated by the covariance between the return $r _ { i }$ of the stock and the return $r _ { m }$ of the market index divided by the variance of the market index (over a period of three years). Finally, we separated the interval of beta value into three sections as used in Eq. (11).

$$
S t o c k T y p e = \left\{ \begin{array}{c} h i g h r i s k, i f B e t a > 1. 2 5 \\ n o r m a l r i s k, i f 1. 2 5 \geq B e t a \geq 0. 7 5 \\ l o w r i s k, i f B e t r a <   0. 7 5 \end{array} \right.\tag{11}
$$

The stock type will be used to classify the recommendation list of stocks. For example, if a user is a risk taker, the high-risk stock will get a higher weight in the system to match the recommendation list to each user’s risk preference.

## 3.6.2. Investment portfolio formation

We collected all the posts on the social investing platform and used sentimental analysis to evaluate the sentiment polarity of each post. Then, we used authority and knowledge analysis on a post’s author to evaluate the credibility of each post. Denote Au(p ) as the author of a where $\alpha , \beta , \gamma ,$ , and δ are different weights of the factors generated by the principal component analysis (PCA). The promising score of an invest ment target is computed by averaging the importance score of all posts on this investment target.

Finally, we customized the stock portfolio by each investor’s risk preference. For a risk taker, investing in high-risk stock would have a higher will. He/she may have little interest in low-risk stock. So, we weighed the stock’s score by the psychological factor in accordance with the investing preference as given in Table 1. Finally, the stocks with a higher total score is chosen as the recommendation target.

## 4. Experiments

In this section, we describe the experiment processes used to verify the proposed mechanism. This research chooses eToro.com as the experiment platform, in which the investment targets are divided into five categories: stocks, indices, commodities, currencies, and ETFs. Stocks can be further divided into six groups: technology, consumer goods, services, financial, healthcare, and basic materials. Each target has a forum for investors to publish their opinions. We computed the overall sentiment polarity and used four features (domain score, keyword score, celebrity score, and rating score) to evaluate the importance of each post related to the investment target. The promising score of an investment target is computed by aggregating the impor tance scores of all posts on this investment target. Finally, we custom ized our recommendation list by considering a user’s risk preference.

## 4.1. Data collection, preprocessing and feature extraction

Data collection: This study chose stocks as the analyses targets because they contain multiple categories and have more posts than other investment targets. We collected review data from December 2016 to March 2017 and gathered a total of 927 posts. The information extracted from the posts include the name of each writer, post content, review likes, reviewers, and the writer’s profile.

Table 1  
The weight of constructing different recommendation lists.

<table><tr><td>Portfolio Type</td><td>High risk stock</td><td>Normal risk stock</td><td>Low risk stock</td></tr><tr><td>Low risk portfolio</td><td>0.6</td><td>0.8</td><td>1.0</td></tr><tr><td>High risk portfolio</td><td>1.0</td><td>0.8</td><td>0.6</td></tr><tr><td>Normal risk portfolio</td><td>1.0</td><td>1.0</td><td>1.0</td></tr></table>

Table 2  
The example of stop words from python package.

<table><tr><td>Stop words</td><td>&#x27;a&#x27;, &#x27;about&#x27;, &#x27;above&#x27;, &#x27;after&#x27;, &#x27;again&#x27;, &#x27;against&#x27;, &#x27;all&#x27;, &#x27;am&#x27;, &#x27;an&#x27;, &#x27;and&#x27;, &#x27;any&#x27;, &#x27;are&#x27;, &quot;aren&#x27;t&quot;, &#x27;as&#x27;, &#x27;at&#x27;, &#x27;be&#x27;, &#x27;because&#x27;, &#x27;been&#x27;, &#x27;before&#x27;, &#x27;being&#x27;, &#x27;below&#x27;, &#x27;between&#x27;, &#x27;both&#x27;, &#x27;but&#x27;, &#x27;by&#x27;, &quot;can&#x27;t&quot;, &#x27;cannot&#x27;</td></tr></table>

Table 3  
The result of POS tagging.

<table><tr><td>The sentence</td><td>After tagging</td></tr><tr><td>updat portfolio react less way expect usdzar gone rel well today fix littl earn green</td><td>(&#x27;updat&#x27;, &#x27;JJ&#x27;), (&#x27;portfolio&#x27;, &#x27;NN&#x27;), (&#x27;react&#x27;, &#x27;NN&#x27;), (&#x27;less&#x27;, &#x27;JJR&#x27;), (&#x27;way&#x27;, &#x27;NN&#x27;), (&#x27;expect&#x27;, &#x27;VBP&#x27;), (&#x27;usdzar&#x27;, &#x27;JJ&#x27;), (&#x27;gone&#x27;, &#x27;VBN&#x27;), (&#x27;rel&#x27;, &#x27;NN&#x27;), (&#x27;well&#x27;, &#x27;RB&#x27;), (&#x27;today&#x27;, &#x27;NN&#x27;), (&#x27;fix&#x27;, &#x27;VBP&#x27;), (&#x27;littl&#x27;, &#x27;NN&#x27;), (&#x27;earn&#x27;, &#x27;VBP&#x27;), (&#x27;green&#x27;, &#x27;JJ&#x27;)</td></tr></table>

Preprocessing: The content of each post contains some meaningles words, such as stop words and punctuation. We first removed punctu ation in the post and used the natural language toolkit [7] to split the sentence into words. Next, we removed the common stop words. Ex amples of stop words are given in Table 2.

Finally, we used the Porter stemming algorithm [37] to recognize words with the same meaning, but use different types as one word. After these steps, we joined the processing words into a new sentence and used Textblob (a Python library for processing textual data) to recognize the part of speech in the sentence. The tagged format is shown in Table 3:

“NN” is a word that is tagged as a noun, “JJ” stands for an adjective, and “RB” for an adverb. This study acquires the part of speech to detect the keywords’ tag for evaluating the distribution of the opinion words. There were 29,060 sentences from which 58,863 nouns, 33,569 adjec tives, and 23,533 adverbs were abstracted to be analyzed.

Feature extraction: After the preprocessing phase, we created new sentences and used TF-IDF to analyze the importance of each word. The TF-IDF method is used to recognize the important words of a document in a collection or corpus. In this study, we used it to find the keywords in the documents. We aggregated all the scores of the same word appearing in different documents as the importance score of each word. Based on the ranked scores, we found 3453 words and chose the top 500 words a the feature keywords in the public posts, as shown in Table 4.

## 4.2. Sentiment classification and analysis

For identifying the sentiment of a sentence, we require a benchmark to recognize the word’s sentiment polarity. In this section, we use the Loughran and McDonald Sentiment Word Lists [33] as our repository. We first use the new sentence which has been preprocessed and compare the words in the sentence with the Sentiment Word Lists. If the word matches, the positive attribute would be marked as +1. The negative words would be represented as -1. The words that belong to uncertainty would be recognized as 0. We then evaluated the sentiment polarity of the sentence by calculating the quantity of the positive words and negative words. If there are more positive words than negative words, the sentence would be recognized as positive and the score would be the ratio of positive or negative words to all words.

To improve the accuracy of sentiment polarity, we combined Text blob to do the sentiment analysis. Textblob uses movie review as the training data and uses the NaiveBayes algorithm to calculate the probability of the word that appears in the positive or negative document. The final sentiment score of each post is the average score of what was computed from our method (financial sentiment) and the Textblob method (review sentiment).

Table 4  
The dictionary of keywords.

<table><tr><td>Rank</td><td>Word</td><td>POS</td><td>Score</td></tr><tr><td>1</td><td>Report</td><td>NN</td><td>44.383687552029</td></tr><tr><td>2</td><td>Content</td><td>NN</td><td>44.277374036979</td></tr><tr><td>3</td><td>Flag</td><td>NN</td><td>44.272374097952</td></tr></table>

## 4.3. Knowledge and influencer analysis

Domain Score: If an investor has more historical trading in a category, then the investor has more experience and knowledge in the domain. eToro.com has organized their investment targets into a tree structure and we acquired the classification for our analysis. We thus have a threetier tree structure and 128 classifications for further analysis.

Keyword Score: Another approach to determine an investor’s knowledge degree is to calculate the importance of his/her posts. We established the feature dictionary that includes 500 chosen keywords based on their TF-IDF scores. A post that includes more sentences with keywords gets a higher score.

Celebrity Score: We used the celebrity score as an index to measure a post’s authority, which computes the explicit and implicit links con structed in eToro.com. The explicit links represent the direct relation ship between users, whereas implicit links stand for the indirect correlation of two users. If a person commented on the post, then there is an implicit link between the author and the person who wrote the comment.

Rating score: We used the rating score as the second index to measure a post’s authority. Because we can find the historical performance of each investor on the social investing platform, this study uses their profit ratio as the performance to evaluate the authority degree of each user who presses the “like” button. The higher the rating score of a post, the more influence the post has on other investors. A part of the posts’ score list is shown in Table 5.

## 4.4. Financial statement analysis

We used financial indicators to evaluate the financial statement score of the investment target, including profitability analysis (ROTA and EPS), operating ability analysis (RTR and IT), capital structure analysis (DAT, LTFFA), and liquidity analysis (CR and QR). A part of the financial statement score is given in Table 6. The related financial statement data comes from the largest financial and accounting database – the WRDS database.

## 4.5. Risk preference

We used beta value to evaluate the stock’s risk and to match the risk preference of each investor. Here, we used Apple as an example and the S&P 500 as our market index. To extract the historical price of the stock and market, we used the Yahoo finance package from which the data was collected. A small snippet of the data is shown in Table 7.

We collected the data on Apple stock from 2014/03/01 to 2017/03/ 01, which contains a total of 755 trading days. To calculate the daily return for the beta formula, we only needed the Adj Close column that represents the close price for the stock in a day. We acquired the S&P 500 data as the market index during the same period. We also retrieved two more columns of information, the market index daily return $r ,$ and the performance of Apple. Eq. (14) calculates the daily return of Apple. The final data format is listed in Table 8. Eq. (15) calculates the beta value of Apple stock based on the S&P 500 market index.

$$
A A P L \% = \left(\text {Close\_price\_today} - \text {Close\_price\_yesterday}\right) / \text {Close\_price\_yesterday} \tag{14}
$$

$$
B e t a = C o v (A A P L \% 1: 7 5 4, S \& P 5 0 0 \% 1: 7 5 4) / V A R (S \& P 5 0 0 \% 1: 7 5 4)\tag{15}
$$

Finally, we obtained the beta value of Apple stock as 1.44, which belongs to the high-risk stock and is suitable for the risk neutral investors.

Table 5  
Part of posts’ score list.

<table><tr><td>Post</td><td>Domain score</td><td>Keyword score</td><td>Celebrity score</td><td>Rating score</td></tr><tr><td>1</td><td>0.329082682023</td><td>0.401639344262</td><td>0.00758653390232</td><td>0.166666666666</td></tr><tr><td>2</td><td>0.765322912381</td><td>0.189873417721</td><td>0.10078544853245</td><td>0.194444444444</td></tr><tr><td>3</td><td>0.309851912793</td><td>0.217647058823</td><td>0.06438047277237</td><td>0.305555555555</td></tr></table>

Table 6  
Part of the financial statement score.

<table><tr><td>Stock Symbol</td><td>Corporation Name</td><td>ROTA</td><td>EPS</td><td>RTR</td><td>IT</td><td>DAR</td><td>LTFFA</td><td>CR</td><td>QR</td><td>FSS Score</td></tr><tr><td>Mu</td><td>Micron Technology</td><td>0.325</td><td>0.229</td><td>0.297</td><td>0.413</td><td>0.023</td><td>0.186</td><td>0.830</td><td>0.915</td><td>0.402</td></tr><tr><td>Wdc</td><td>Western Digital Corporation</td><td>0.896</td><td>0.341</td><td>0.464</td><td>0.513</td><td>0.285</td><td>0.302</td><td>0.143</td><td>0.139</td><td>0.385</td></tr><tr><td>Baba</td><td>Alibaba</td><td>0.567</td><td>0.464</td><td>0.486</td><td>0.613</td><td>0.113</td><td>0.362</td><td>0.227</td><td>0.155</td><td>0.373</td></tr><tr><td>Appl</td><td>Apple</td><td>0.944</td><td>0.206</td><td>0.341</td><td>0.444</td><td>0.203</td><td>0.418</td><td>0.205</td><td>0.026</td><td>0.349</td></tr><tr><td>Fb</td><td>Facebook</td><td>0.328</td><td>0.260</td><td>0.335</td><td>0.926</td><td>0.056</td><td>0.327</td><td>0.240</td><td>0.239</td><td>0.339</td></tr></table>

Table 7  
Snippet data of Apple stock.

<table><tr><td>Date</td><td>Open</td><td>High</td><td>Low</td><td>Close</td><td>Volume</td><td>Adj Close</td></tr><tr><td>2017/3/1</td><td>137.89</td><td>140.15</td><td>137.60</td><td>139.79</td><td>36414600</td><td>139.79</td></tr><tr><td>2017/2/28</td><td>137.08</td><td>137.44</td><td>136.70</td><td>136.99</td><td>23482900</td><td>136.99</td></tr><tr><td>2017/2/27</td><td>137.14</td><td>137.44</td><td>136.28</td><td>136.93</td><td>20257400</td><td>136.93</td></tr></table>

Table 8  
The snippet data used to evaluate the beta of apple stock.

<table><tr><td>Date</td><td>AAPL</td><td>S&amp;P 500</td><td>AAPL%</td><td>S&amp;P 500%</td></tr><tr><td>2017/3/1</td><td>139.79</td><td>2395.96</td><td>0.020439</td><td>0.013674</td></tr><tr><td>2017/2/28</td><td>136.99</td><td>2363.64</td><td>0.000438</td><td>-0.00257</td></tr><tr><td>2017/2/27</td><td>136.93</td><td>2369.73</td><td>0.001976</td><td>0.00101</td></tr></table>

Table 9  
Principal component analysis.

<table><tr><td>Component</td><td>Total</td><td>% of Variance</td><td>Cumulative %</td></tr><tr><td>Domain Score</td><td>0.477</td><td>20.384</td><td>20.384</td></tr><tr><td>Keyword Score</td><td>0.308</td><td>13.162</td><td>33.547</td></tr><tr><td>Celebrity Score</td><td>0.795</td><td>33.974</td><td>67.521</td></tr><tr><td>Rating Score</td><td>0.760</td><td>32.478</td><td>100</td></tr></table>

## 4.6. Recommendation list

To incorporate the four factors that were used to evaluate the cred ibility of a post, we determined the weight combination by using the principal component analysis [23]. The total variance explained is shown in Table 9. The greater percentage of a factor means this factor has more variance explanation.

Finally, with the obtained criteria weights, we aggregated the scores of all posts on each stock as the final grade of this stock. The recom mendation lists created with respect to an investor’s risk preference are shown in Tables 10–12.

Table 10  
Recommendation list of normal risk portfolio.

<table><tr><td>Rank</td><td>Stock Symbol</td><td>Post Importance</td></tr><tr><td>1</td><td>Mu</td><td>1</td></tr><tr><td>2</td><td>Wdc</td><td>0.826</td></tr><tr><td>3</td><td>Baba</td><td>0.774</td></tr></table>

Table 11  
Recommendation list of low risk portfolio.

<table><tr><td>Rank</td><td>Stock Symbol</td><td>Post Importance</td></tr><tr><td>1</td><td>Baba</td><td>0.774</td></tr><tr><td>2</td><td>Wdc</td><td>0.660</td></tr><tr><td>3</td><td>FB</td><td>0.537</td></tr></table>

Table 12  
Recommendation list of high risk portfolio.

<table><tr><td>Rank</td><td>Stock Symbol</td><td>Post Importance</td></tr><tr><td>1</td><td>Mu</td><td>1</td></tr><tr><td>2</td><td>Wdc</td><td>0.660</td></tr><tr><td>3</td><td>Appl</td><td>0.577</td></tr></table>

## 5. Results and evaluation

In the experiment, we traded for thirty days and observed the change in daily return. We chose the S&P 500 as the market index for com parison of the performance of the portfolio. The S&P 500 is an American stock market index based on the market capitalizations of 500 large companies. Compared to the Dow Jones Industrial Average Index, the S&P 500 index contains more companies such that risk is more dispersed and can more accurately reflect the market changes. As recent works analyzing reviews for stock market prediction mainly include the review sentiment analysis approach [40], knowledge approach [29], and au thority approach [21], we used them as the representative benchmark approaches for method comparison. The recommendation approaches used for comparison are listed as follows: (1) no-filter recommendation (2) knowledge-based recommendation (research domain analysis and article keyword analysis) (3) authority-based recommendation (user celebrity analysis and review rating analysis) and (4) collective intelli gence recommendation (the proposed CIR approach including research domain analysis, article keyword analysis, user celebrity analysis, and review rating analysis).

Table 13  
Percentage value change for each approach.

<table><tr><td>Approach</td><td>Portfolio Return</td><td>S&amp;P 500</td></tr><tr><td>no-filter</td><td>-27.550%</td><td>-0.806%</td></tr><tr><td>knowledge-based</td><td>16.180%</td><td>-0.806%</td></tr><tr><td>authority-based</td><td>2.168%</td><td>-0.806%</td></tr><tr><td>CIR</td><td>30.369%</td><td>-0.806%</td></tr></table>

![](/api/attachments/3DK65U8T/fulltext/images/8ce8b036ba61d7a1e4ce914862361fbf89528d448f0eeb8758453688ac82247e.jpg)  
Fig. 5. The daily stock return by each approach.

![](/api/attachments/3DK65U8T/fulltext/images/3f6e9c53ecca4364d3b9be12f6d831ff7bf61c699b5c6b91f273f1e86171cf40.jpg)  
Fig. 6. The daily stock return by no-filter approach.

![](/api/attachments/3DK65U8T/fulltext/images/c89d3e975d28714aa25e90fd16ef7cc5478bfbdf6a68fa4f1ba6ada5ae5c7200.jpg)  
Fig. 7. The daily stock return by knowledge-based approach.

![](/api/attachments/3DK65U8T/fulltext/images/8975e343ea82b3493596c7d84ea279bc21a73f449eeb062ed9c1df1dc3d5d5cf.jpg)  
Fig. 8. The daily stock return by authority-based approach.

## 5.1. Portfolio evaluation

In this section, we measured the performance of each portfolio by three measures. The first measure, which is the most common method, compares the portfolio return fluctuation with the market index to observe the performance during the trading period. The second measure is to calculate the Treynor ratio of each portfolio. The third one is to calculate the Jensen ratio of each portfolio.

![](/api/attachments/3DK65U8T/fulltext/images/dd45f948a3087fd5dae3007ad8bdd426608d3f6a2b3b113208bc422cd1481854.jpg)  
Fig. 9. The daily portfolio return by CIR approach.

## 5.1.1. Portfolio evaluation by daily returns

Table 13 summarizes the results of the percentage change in the returns by different approaches. We observed that our CIR mechanism outperforms the S&P 500 index and other approaches.

As represented in Figs. 5–9, if we only consider the sentiment po larity of each post to recommend the stock, the performance would be terrible and even worse than the market index. The portfolio created by the knowledge-based approach has stable growth and finally received a 16.180% return, which is better than the authority-based approach. The performance of the authority-based recommendation approach is worse than the knowledge-based approach with a return of 2.168% and is a little better than the market index. More domain knowledge reflects that the investors are the experts in the corresponding field and are likely to share better insights on how to make an investment strategy. The returns of the portfolio constructed by our proposed mechanism exhibit a growing trend and outperform those portfolios suggested by the market index and other benchmark approaches during the trading period.

## 5.1.2. Portfolio evaluation by Treynor measure

Jack L. Treynor was the first person to propose a measure of portfolio performance that combines both risk and return [42]. The Treynor measure, also known as the reward-to-volatility ratio, is used to calcu late the excess return between the portfolio and risk-free asset divided by the beta of the portfolio. Beta is a numeric value that measures the fluctuations of a stock to changes in the overall stock market. In other words, it is an index that shows the relationship of investment target to the financial market.

The Treynor ratio can be defined as Eq. (16).

$$
\text { Treynor   ratio } = \frac {\left(\text { Portfolio   Return } - \text { Risk   Free   Rate }\right)}{\text { Beta }}\tag{16}
$$

The ratio represents the portfolio’s return per unit risk. When the value of the Treynor ratio is high, it is an indication that an investor has generated high returns on each of the market risks he has taken. In this research, we chose the average annual return on treasury bills as the risk-free rate. Fig. 10 depicts the Treynor ratios of portfolios generated by different approaches. We can find that the no-filter approach has the worst performance and our CIR mechanism is much better than all of the other approaches.

![](/api/attachments/3DK65U8T/fulltext/images/0ea221e925d3cdde851bb88c094dca999b0f01f1380a6c17cfe2672a5fa9c53c.jpg)  
Fig. 10. Treynor ratio of each approach.

## 5.1.3. Portfolio evaluation by Jensen measure

The Jensen measure is named after its creator, Michael C. Jensen. It calculates the excess return that a portfolio generates over its expected return [22]. The measure of return is also known as alpha. It can be defined as Eq. (17).

Jensen ratio = Portfolio Return − Benchmark Portfolio Return

(17)

where the benchmark portfolio return is defined as Eq. (18).

$$
\begin{array}{r l} \text { Benchmark   Return } & = \text { Risk   Free   Return } + \text { Beta } \\ & * (\text { Return   of   Market } - \text { Risk   Free   Return }) \end{array}\tag{18}
$$

Usually, investors hope to get a high return with a minimum amount of risk. Jensen’s alpha is important to investors because they consider not only the total return of a security or portfolio, but also the amount of risk involved in achieving that return. If the actual return is higher than the predicted return, the security or portfolio is said to have a positive alpha (or an abnormal return). Investors are always looking for oppor tunities in which the investment portfolio can have a positive alpha. From Fig. 11, we find that the no-filter approach still has the worst performance. In addition to that, our CIR mechanism has a positive ratio, while other approaches have negative ones.

## 5.2. Customized recommendation list

In this section, we customized stock portfolios in accordance with each user's risk preference. For risk takers, the score of high-risk stock was multiplied by 1, low-risk stock by 0.6, and normal risk stock by 0.8. For risk averters, the score of high-risk stock was multiplied by 0.6, while the low-risk stock was multiplied by 1. For risk neutral investors, the score of each stock remained the same because they can accept all kinds of stocks. The performance of the portfolio for risk averters is given in Table 14 and Fig. 12. The performance of the portfolio for risk takers is shown in Table 15 and Fig. 13. Finally, Table 16 and Fig. 14 represents the performance of the portfolio for risk neutral investors.

From the results of these three types of investors, our proposed CIR mechanism has better performance than all other approaches on all of the performance measures, that is, the return, Treynor ratio, and Jen sen’s alpha. Particularly, the performance of the portfolio recommended by our mechanism is the best for risk neutral investors.

## 6. Discussion and conclusion

We are facing an era of negative interest rates on deposits around the world. To make a profit and for the proper usage of idle funds, people

![](/api/attachments/3DK65U8T/fulltext/images/ea2803f4a3595b1345303c87d42ba0ef60ccc5de34d3dfc87558ffc2b754a377.jpg)  
Fig. 11. of each approach.

Table 14  
Recommendation lists of low risk portfolio.

<table><tr><td>Measure</td><td>no-filter</td><td>knowledge-based</td><td>authority-based</td><td>CIR</td></tr><tr><td>Return</td><td>-30.092%</td><td>15.830%</td><td>-7.360%</td><td>17.233%</td></tr><tr><td>Treynor</td><td>-97.629%</td><td>-5.072%</td><td>-53.291%</td><td>-4.384%</td></tr><tr><td>Jensen</td><td>-47.007%</td><td>-1.298%</td><td>-24.896%</td><td>-0.269%</td></tr></table>

![](/api/attachments/3DK65U8T/fulltext/images/4be69746952e813018312d85f0c50bf3cdc84bb5753cce23ce5f5a7b2e5bd3ab.jpg)  
Fig. 12. Recommendation performance of low-risk portfolio.

Table 15  
Recommendation lists of high-risk portfolio.

<table><tr><td>Measure</td><td>no-filter</td><td>knowledge-based</td><td>authority-based</td><td>CIR</td></tr><tr><td>Return</td><td>3.549%</td><td>12.329%</td><td>29.255%</td><td>29.255%</td></tr><tr><td>Treynor</td><td>-12.029%</td><td>-6.946%</td><td>5.896%</td><td>5.896%</td></tr><tr><td>Jensen</td><td>-16.875%</td><td>-7.870%</td><td>9.290%</td><td>9.290%</td></tr></table>

![](/api/attachments/3DK65U8T/fulltext/images/6f99793d617bcb07038ce5d20b208dde6a2a5b797994ef7377cd2071c0cecff7.jpg)  
Fig. 13. Recommendation performance of high-risk portfolio.

Table 16  
Recommendation lists of normal risk portfolio.

<table><tr><td>Measure</td><td>no-filter</td><td>knowledge-based</td><td>authority-based</td><td>CIR</td></tr><tr><td>Return</td><td>-27.550%</td><td>16.180%</td><td>2.168%</td><td>30.369%</td></tr><tr><td>Treynor</td><td>-63.400%</td><td>-7.492%</td><td>-16.056%</td><td>5.607%</td></tr><tr><td>Jensen</td><td>-45.995%</td><td>-2.949%</td><td>-17.593%</td><td>11.164%</td></tr></table>

tend to invest. How to find a profitable target from numerous investment targets is a crucial problem. This research proposes a portfolio recom mendation mechanism based on the collective intelligence extracted from a social investing platform, which can create an investment port folio to support an investor’s decision making. Specifically, we extracted all the posts from the investing forums to construct the feature dictionary. Then we evaluated the credibility of the posts from four key per spectives (the domain, keyword, celebrity, and rating aspects of the reviewing investors). We incorporated the analyses of sentimental po larity and these four indexes on the posts to evaluate investment targets (e.g., stocks) and construct the recommendation portfolio list of stocks that are highly ranked.

![](/api/attachments/3DK65U8T/fulltext/images/a64746d5c1b016f179ba85228f4ec1ef3b843ef185cfbeb8ac773b4d550f30b8.jpg)  
Fig. 14. Recommendation performance of normal risk portfolio

In the experiment, we evaluated and compared our mechanism with different benchmark approaches based on the performance on returns, the Treynor measure, and the Jensen measure. Our mechanism kept outperforming the other benchmark approaches during the trading period in all three measures. We also generated customized recom mendation lists and proved that the portfolio created by our proposed mechanism for each kind of investor with different risk preferences re mains the best. The proposed recommendation mechanism can help investors save time in selecting investment targets, which requires dealing with innumerable data records and receiving more profitable returns.

## 6.1. Research contributions

The contributions of this research are as follows. First, from the system development perspective, we built a decision support system for investment support that is based on the collective intelligence extracted from social investing platforms. However, no investment decision sup port system uses the reviews of investors from social investing platforms to derive investment decisions. Unlike the general reviewers, they made actual investment trades on the social investing platform (eToro) and their investment performances are tractable. Driving the portfolio based on the social investing approach (“copy and paste” prior expert in vestors' investment targets) is a new and practical investment approach. According to our experimental results, we found that our proposed system can generate a more profitable return. Second, from the perspective of data source, as the investors on the social investing platform likely have studied related public information, learned private information, and conducted analytics on the investment targets before they make an investment trade, their investment performance and re views reveal valuable information which is not achievable from the approaches discussed in prior studies. Third, from the methodological perspective, we consider the characteristics of posts, investors, and in vestment targets (companies) and use knowledge domain, article keyword, user celebrity, review rating, and financial index as criteria to evaluate the credibility of the posts relevant to a stock. Our system which combines these five indexes performs better than other bench: mark approaches. Fourth, from the practical perspective, while existing social trading platforms such as eToro provide a space for investors to express their opinions on the investment target, it is too hard for a beginner to recognize the detailed insights expressed in the review. Our mechanism can effectively process the numerous data and construct a recommendation list to help a beginner to make a decision. Lastly, from the financial perspective, our mechanism can avoid irrational behavior because the portfolio is created based on collective intelligence that is extracted from the platform’s reviews over a period; it is less affected by the temporary bump of the market. Moreover, it also reduces the risk of an investment strategy because the recommendation list is constructed by using the collective wisdom from a large number of credible investors.

## 6.2. Research limitations

There are some limitations to this research, which are listed as fol lows. First, we mainly used reviews acquired from eToro.com because of its clear structure of investment target classification. There are several social investment platforms, such as scutify.com or stocktwits.com that target investors with different properties. Second, in this research, we mainly considered the technology stocks as our investing targets because there are more reviews on technology stock than for other categories. We can provide a more diversified recommendation list if more cate gories of stocks are analyzed. Third, this research classifies the users into three groups (risk taker, risk neutral, and risk averter) in accordance with the risk preference of each investor. We did not take the basic profile (e.g., income, job, age) into account, which could be an impor tant factor when creating the customized portfolio recommendation. Fourth, we collected the experiment data at a fixed time to develop the recommendation list as the simulated investment portfolio. We can update the data every day and construct new lists to adjust the strategy during a period of thirty trading days.

## 6.3. Future works

There are several articles that can be further studied. First, in thi research, we mainly used TF-IDF to select the features. There are other text-mining techniques, such as information gain (IG), chi-square sta tistics (CHI), document frequency (DF), and accuracy balanced (Acc2), which could be used and compared to further improve the performance. Second, although the performance of the portfolio generated from our mechanism is superior to other approaches, some machine learning al gorithms, such as support vector machine (SVM), logistic regression, and decision rules of trees, can be incorporated to further enhance the per formance. Third, with the advancement of technology, people tend to use mobile devices to make a transaction. Stock investors with high performance expectancy are likely to have increased intention to use mobile stock trading [41]. We can extend the research to construct mobile stock trading systems with an advanced stock analysis to support investors when they are determining appropriate trading strategies. Finally, the correlation between the community opinions and the trend of stock prices could be further investigated. Investigating the insights as to whether the bump caused people to post a comment or the community opinions made the stock price fluctuate helps to improve the perfor mance of portfolio recommendations.

## CRediT authorship contribution statement

Yung-Ming Li: Methodology, Formal analysis, Investigation, Data curation, Writing – review & editing, Visualization, Supervision. Lien-Fa Lin: Conceptualization, Methodology, Formal analysis, Investigation, Validation. Chin-Yu Hsieh: Conceptualization, Formal analysis, Inves tigation, Validation. Bo-Syun Huang: Conceptualization, Investigation, Validation, Resources, Data curation.

## Acknowledgements

This research was supported by the Ministry of Technology and Science, Taiwan under grant MOST 107-2410-H-009 -026 -MY3.

## References

[11 A. Aizawa, An information-theoretic perspective of tf-idf measures, Inf, Process. Manag. 39 (1) (2003) 45–65

[2] W. Antweiler, M.Z. Frank, Is all that talk just noise? The information content of internet stock message boards, J. Financ. 59 (3) (2004) 1259–1294.

[3] C. Avery, J.A. Chevalier, R.J. Zeckhauser, The "CAPS" prediction system and stock market returns, Rey, Financ, 20 (4) (2016) 1363–1381.

[4] N. Barberis, R. Thaler, A survey of behavioral finance, Handb. Econ. Financ. 1 (2003) 1053–1128.

[5] G.S. Becker, Irrational behavior and economic theory, J. Polit. Econ. 70 (1) (1962) 1–13.

[6] E.S.C. Berger, M. Wenzel, V. Wohlgemuth, Imitation-related performance outcomes in social trading: a configurational approach, J. Bus. Res. 89 (2018) 322–327.

[7] S. Bird, NLTK: the natural language toolkit, in: Proceedings of the 6th COLING/ACL on Interactive presentation sessions, 2006, pp. 69–72.

[8] D.C. Brabham, Crowdsourcing as a model for problem solving: an introduction and cases, Convergence 14 (1) (2008) 75–90.

[9] T. Brandt, J. Bendler, D. Neumann, Social media analytics and value creation in urban smart tourism ecosystems, Inf. Manag. 54 (6) (2017) 703–713.

[10] J. Bollen, H. Mao, X. Zeng, Twitter mood predicts the stock market, J. Comput. Sci. 2 (1) (2011) 1–8.

[11] W.S. Chan, Stock price reaction to news and no-news: drift and reversal after

[12] C. Chandrasekhar, Negative interest rates, Econ. Political Weekly 52 (12) (2017) 53.

[13] K. Daniel, D. Hirshleifer, A. Subrahmanyam, Investor psychology and security market under-and overreactions, J. Financ. 53 (6) (1998) 1839–1885.

[14] JB. DeLong. A. Shleifer. L.H. Summers. RJ. Waldmann. Noise trader risk in financial markets, J. Polit. Econ, 98 (4) (1990) 703–738.

[15] M. Eickhoff. J. Muntermann. Stock analysts ys. the crowd: mutual prediction and the drivers of crowd wisdom, Inf, Manag, 53 (7) (2016) 835–845.

[16] E.F. Fama. Market efficiency. long-term returns, and behavioral finance. J. Financ Econ, 49 (3) (1998) 283–306

[17] G.P.C. Fung, J.X. Yu, W. Lam, Stock prediction: integrating text mining approach using real-time news, in: Proceedings of the IEEE International Conference on Computational Intelligence for Financial Engineering, 2003, pp. 395–402.

[18] B. Gu, P. Konana, A. Liu, B. Rajagopalan, J. Gsh, Predictive value of stock message board sentiments, McCombs Research Paper No. IROM-11-06, 2006, Available at https://SSRN:https://ssrn.com/abstract=966498.

[19] I. Guvon, A. Elisseeff, An introduction to variable and feature selection, J. Mach. Lear, Res, 3 (2003) 1157–1182

[20] C.A. Hargreaves, P. Dixit, A. Solanki, Stock portfolio selection using data mining approach, IOSR J. Eng. 3 (11) (2013) 42–48.

[21] S. Hill, N. Ready-Campbell, Expert stock picker: the wisdom of (experts in) crowds

[22] M.C. Jensen, The performance of mutual funds in the period 1945–1964, J. Financ. 23 (2) (1968) 389–416.

[23] I. Jolliffe, Principal Component Analysis, Wiley Online Library, 2002.

[24] Y. Kim, S.R. Jeong, I. Ghani, Text opinion mining to analyze news for stock market prediction, Int. J. Adv. Soft Comput. Appl 6 (1) (2014).

[25] C. Kiss, M. Bichler, Identification of influencers – measuring influence in customer networks, Decis. Support Syst. 46 (1) (2008) 233–253.

[26] R.J. Kuo, C. Chen, Y. Hwang, An intelligent stock trading decision support system through integration of genetic algorithm based fuzzy neural network and artificial neural network, Fuzzy Sets Syst. 118 (1) (2001) 21–45.

[27] A. Mahajan, L. Dey, S.M. Haque, Mining financial news for major events and their impacts on the market, in: Proceedings of JEEE/WIC/ACM International

Conference on Web Intelligence and Intelligent Agent Technology, Sydney, NSW, Australia, 2008, pp. 423–426.

[28] A. Mittal, A. Goel, Stock prediction using twitter sentiment analysis. Project Report, Standford, 2011. https://pdfs.semanticscholar.org/4ecc/55e1c3ff1cee 41f21e5b0a3b22c58d04c9d6.pdf.

[29] K. Nam, N. Seong, Financial news-based stock movement prediction using causality analysis of influence in the Korean stock market, Decis. Support Syst. 117 (2019)

[30] A.K. Nassirtoussi, S. Aghabozorgi, T.Y. Wah, D.C.L Ngo, Text mining for marke prediction: a systematic review. Expert Syst. Appl. 41 (16) (2014) 7653–7670.

[31] J. Liu, Y. Cao, C.Y. Lin, Y. Huang, M. Zhou, Low-quality product review detection in opinion summarization, in: Proceedings of the Joint Conference on Empirica Methods in Natural Language Processing and Computational Natural Language Learning, Prague, Czech Republic, 2007, pp. 334–342.

[32] Y. Luo, K. Liu, D.N. Davis, A multi-agent decision support system for stock trading, IEEE Netw. 16 (1) (2002) 20–27.

[33] T. Loughran, B. McDonald, Textual analysis in accounting and finance: a survey, J. Account. Res. 54 (4) (2016) 1187–1230.

[34] W. Pan, Y. Altshuler, A. Pentland, Decoding social influence and the wisdom of the crowd in financial trading network. Paper presented at the privacy, security, risk and trust (PASSAT), in: Proceedings of the International Conference on Privacy, Security, Risk and Trust and International Confernece on Social Computing, 2012, pp. 203–209.

[35] B. Pang, L. Lee, S. Vaithyanathan, Thumbs up?: Sentiment classification using machine learning techniques, in: Proceedings of the Conference on Empirical Methods in Natural Language Processing, 2002, pp. 79–86

[36] V. Pestov, Is the k-NN classifier in high dimensions affected by the curse o dimensionality? Comput. Math. Appl. 65 (10) (2013) 1427–1437.

[37] M. Porter, The Porter stemming algorithm, http://www.tartarus.org/martin/Porte rStemmer/index.html

[38] A. Reyes, P. Rosso, Making objective decisions from subjective data: detecting irony in customer reviews, Decis, Support Syst, 53 (4) (2012) 754–760

[39] D. Schniederjans, E.S. Cao, M. Schniederjans, Enhancing financial performance with social media: an impression management perspective, Decis. Support Syst. 55 (4) (2013) 911–918.

[40] Y. Sun, X. Liu, G. Chen, Y. Hao, Z. Zhang, How mood affects the stock market: empirical evidence from microblogs, Inf. Manag. 57 (5) (2020), 103181.

[41] Y.M. Tai, Y.C. Ku, Will stock investors use mobile stock trading? A benefit-risk assessment based on a modified UTAUT model, J. Electron. Commer. Res. 14 (1) (2013) 67–84.

[42] J.L. Treynor, How to rate management of investment funds, Harv. Bus. Rev. 43 (1) (1965) 63–75.

[43] N. Wire, Global advertising: consumers trust real friends and virtual strangers the most.2009.Accessed:26-03-2021 https://www.nielsen.com/us/en/insights/artic le/2009/global-advertising-consumers-trust-real-friends-and-virtual-strangers-themost/.

[44] Y. Yang, J.O. Pedersen, A comparative study on feature selection in tex categorization, in: Proceedings of the Fourteenth International Conference on Machine Learning, 1997, pp. 412–420. July.

[45] J.P. Zagal, N. Tomuro, A. Shepitsen, Natural language processing in game studies research: an overview, Simul. Gaming 43 (3) (2012) 356–373

[46] Y. Zhang, R. Jin, Z.H. Zhou, Understanding bag-of-words model: a statistical framework, Int. J. Mach. Lear. Cyber. 1 (1-4) (2010) 43–52.

[47] H.M. Zolbanin. D. Behrooz, D. Dursun, H.Z. Amir. Data analytics for the sustainable use of resources in hospitals: predicting the length of stay for patients with chronic diseases, Inf. Manag. (2020), 103282.

Yung-Ming Li is a Professor at the Institute of Information Management, National Yang Ming Chiao Tung University in Taiwan. He received his Ph.D. in Information Systems from the University of Washington. His research interests include network science. Internet economics. and business intelligence. His research has appeared in JEEE/ACM Transactions on Networking, INFORMS Journal on Computing, Production and Operations Management, Decision Sciences, International Journal of Electronic Commerce, Infor mation and Management, Decision Support Systems, European Journal of Operational Research, International Conference on Information Systems (ICIS), Workshop on Infor mation Technology and Systems (WITS), among others.

Lienfa Lin is an Associate Professor at the Department of Digital Media Design, Asia University in Taiwan. He received Ph.D. degree in Information Management from National Chiao Tung University. His research interests include electronic commerce, mobile computing, and social computing. His research has appeared in Decision Support Systems, International Journal of Electronic Commerce, and Information and Management

Chin-Yu Hsieh received his Ph.D. student at the Institute of Information Management, National Yang Ming Chiao Tung University in Taiwan. His research interests includ artificial intelligence and electronic ecommerce.

Bo-Syun Huang received his M.S. degree from the Institute of Information Management, National Chiao Tung University in Taiwan and B.S. degree in Information Management from the National Central University. Taiwan. His research interests focus on electronic commerce and financial computing.
