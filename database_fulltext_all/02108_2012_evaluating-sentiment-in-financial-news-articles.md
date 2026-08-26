---
otero_id: 2108
otero_key: "EKJYJCUG"
title: "Evaluating sentiment in financial news articles"
authors: "Robert P. Schumaker; Yulei Zhang; Chun-Neng Huang; Hsinchun Chen"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.03.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Evaluating sentiment in <sup>fi</sup>nancial news articles

Robert P. Schumaker <sup>a,</sup>⁎, Yulei Zhang <sup>b</sup>, Chun-Neng Huang <sup>c</sup>, Hsinchun Chen

<sup>a</sup> Management Information Systems, Central Connecticut State University, New Britain, CT 06050, USA

<sup>b</sup> The W.A. Franke College of Business, Northern Arizona University, Flagstaff, AZ 86011, USA

<sup>c</sup> Microsoft Corporation, Bellevue, WA 98006, USA

<sup>d</sup> Artificial Intelligence Lab, Department of Management Information Systems, The University of Arizona, Tucson, AZ 85721, USA

## a r t i c l e i n f o

Article history: Received 30 August 2010 Received in revised form 24 May 2011 Accepted 4 March 2012 Available online 16 March 2012

Keywords: Business intelligence Text mining Financial prediction Sentiment analysis

## a b s t r a c t

Can the choice of words and tone used by the authors of financial news articles correlate to measurable stock price movements? If so can the magnitude of price movement be predicted using these same variables? We investigate these questions using the Arizona Financial Text (AZFinText) system, a <sup>fi</sup>nancial news article prediction system, and pair it with a sentiment analysis tool. Through our analysis, we found that subjective news articles were easier to predict in price direction (59.0% versus 50.0% of chance alone) and using a simple trading engine, subjective articles garnered a 3.30% return. Looking further into the role of author tone in <sup>fi</sup>nancial news articles, we found that articles with a negative sentiment were easiest to predict in price direction (50.9% versus 50.0% of chance alone) and a 3.04% trading return. Investigating negative sentiment further, we found that our system was able to predict price decreases in articles of a positive sentiment 53.5% of the time, and price increases in articles of a negative sentiment 52.4% of the time. We believe that perhaps this result can be attributable to market traders behaving in a contrarian manner, e.g., see good news, sell; see bad news, buy.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Predicting stock market behavior has always had a certain appeal to researchers. While numerous attempts have been made, the dif<sup>fi</sup>- culty has always centered around the inability to model the behaviors of human traders. Worse yet, behavioral patterns are constantly changing, making accurate predictions quite dif<sup>fi</sup>cult. To further add to this uncertainty, there are two entirely opposed philosophies of stock market research; fundamental and technical analysis techniques [33]. Fundamentalists seek to leverage a security's relative data, ratios and earnings, while technicians analyze charts and modeling techniques based on historical trading volume and pricing. The basic problem becomes does price history matter?

Within the past several years, the role of computers in stock prediction has increased dramatically. Many of these systems have simply followed the trend of automating existing fundamental and/or technical strategies with the goal of achieving better returns than human traders by removing the elements of emotion and bias from trading [15]. The downside of these types of systems is that they lack intuition and will continue to execute trades even after unfavorable news events, such as losing a costly court battle. In order to work effectively, these systems require news events to be translated into numeric data before appropriate decisions can be made. This problem introduces serious lag-time into decisions and in some cases human analysts must override trades.

Even with the addition of <sup>fi</sup>nancial news in a quantitative trading system, other important features of the article may be missing. The addition of author sentiment in stock price prediction could improve accuracy [6] and reduce risk [20]. By automatically recognizing not only the terms used in the <sup>fi</sup>nancial news article, but also the emotional cues used by the author and re<sup>fl</sup>ected by their choice of words, we plan to implement a machine learning approach that can learn historical price movements using these features and build a price prediction model in which future news articles could be instantly evaluated.

Our motivation is to build and test such an artifact with an emphasis on the sentiment and author tone features incorporated within a <sup>fi</sup>nancial news article. By evaluating the intricacies of article sentiment and author tone, we seek to discover the role author sentiment can play in price prediction.

This paper is arranged as follows. Section 2 provides an overview of literature concerning Stock Market prediction, textual representations and sentiment analysis techniques. Section 3 develops our research questions. Section 4 describes our approach to the problem and introduces the Arizona Financial Text (AZFinText) system. Section 5 gives an overview of our experimental design. Section 6 provides results of our experimental <sup>fi</sup>ndings and a discourse of their impact on stock price prediction. Section 7 presents our conclusions and a brief discussion of future research directions.

## 2. Literature review

There are two theories that have had a signi<sup>fi</sup>cant impact on market prediction, Ef<sup>fi</sup>cient Market Hypothesis (EMH) and Random Walk Theory (RWT). In EMH, the price of a security is a re<sup>fl</sup>ection of complete market information and when new information is introduced, the market instantly adjusts the stock price to re<sup>fl</sup>ect it [10]. From EMH theory, it is believed that markets are ef<sup>fi</sup>cient and that price corrections occur instantly, making price prediction from market data impossible.

RWT is similar to EMH where all information is embedded in the current price and cannot be practically used for future prediction. This theory slightly differs from EMH in that under RWT, short-term price movements are viewed as indistinguishable from random activity [22]. It is believed that this short-term random activity produces unpredictable near-term price movements and thus the market's nondeterministic nature makes it impossible to consistently outperform it.

Furthermore, the ability to scrutinize the decisions of traders and uncover trading behavior on the scale of a market exchange is an extremely dif<sup>fi</sup>cult task. To lessen this problem and test the impact of both fundamental and technical trading strategies, LeBaron created an arti<sup>fi</sup>cial stock market of simulated traders whose trading decisions could be manipulated and dissected [18]. LeBaron accomplished this by introducing new pieces of information into the market and adjusted the amount of decision time between when an individual trader would receive new information and then act upon it. It was discovered that traders with longer waiting times formed fundamental strategies, relying more heavily on company-speci<sup>fi</sup>c performance data, while those with shorter waiting times developed technical strategies, such as timing trades to base their trading decisions upon. This study led to a more important contribution by <sup>fi</sup>nding that a lag period existed between the time information is introduced and when the market would correct itself. This apparent delay in market behavior helped to dismiss the instantaneous market correction theories and lent support to the idea that markets could be forecast for short durations of time following the introduction of new information. To follow up on establishing limits to this predictive window, Gidofalvi discovered that there exists a twenty minute window of opportunity before and after a <sup>fi</sup>nancial news article is released [12]. It is within this window that weak prediction of a stock price is possible. It is further believed that this period occurs for several reasons. The predictability of price 20 min before an article is released is believed to account for the activity of insider traders whereas the 20 min following an article release is the result of reprinting and posting delays that exist across web media, where some traders may receive their information later than others [13].

## 2.1. Financial news articles

Markets thrive on new information and this data is constantly streaming. While many information types can move a stock price, e.g., rumors, eavesdropping and scandals; <sup>fi</sup>nancial news articles are considered to be a more stable and trustworthy source. Many studies rooted in the Information Retrieval (IR) methodologies have examined the use of textual news articles. While most are interested in studying the relationships between articles in a pure IR point of view, few focus on the domain of <sup>fi</sup>nancial text as it relates to quanti<sup>fi</sup>able stock market data. In Cecchini's work, he examined the role that <sup>fi</sup>nancial text may play in predicting corporate fraud or bankruptcy [4]. He did this by looking at the terms used in corporate 10K reporting and linked it to historical <sup>fi</sup>nancial results. Through this pairing of text and quantitative activity, Cecchini was able to predict bankruptcy 83.9% of the time and fraud with 82.0% accuracy.

In a different type of study, Ma examined the textual role that <sup>fi</sup>nancial news articles may play in determining levels of company cooperation and connectedness among one another [21]. This study constructed a social network of companies mentioned in <sup>fi</sup>nancial news articles and built links between co-mentioned organizations. The strength of the links can provide an idea of the amount of connectedness between companies.

The act of correlating <sup>fi</sup>nancial news articles to a quanti<sup>fi</sup>able price movement is a dif<sup>fi</sup>cult task, even when the information within a <sup>fi</sup>- nancial news article can have a visible impact on price [12,17,25,43]. However, <sup>fi</sup>nancial news articles are not the sole determiner of price movement. Sudden price movements can still occur from other sources, such as large unexpected trades [3].

The <sup>fi</sup>rst challenge of a textual <sup>fi</sup>nancial prediction system is to manage the large amounts of textual information that exist for securities. This material can include required reports such as periodic SEC <sup>fi</sup>lings, press releases and <sup>fi</sup>nancial news articles reporting both unexpected events and routine news alike. These textual documents can then be parsed using Natural Language Processing (NLP) techniques to identify speci<sup>fi</sup>c article terms or phrases most likely to cause dramatic share price changes. Terms such as “factory exploded” or “workers strike” may indicate a price plunge in the near future. By automating this process, machines can map <sup>fi</sup>nancial text terms to discrete price movements and identify arbitrage opportunities faster than a human counterpart. This leads to the next logical step where a purpose-built quantitative system could also be put in charge of executing immediate trades based on textual data.

Thus the process of obtaining timely <sup>fi</sup>nancial documents from reputable Web sources is a critical step. There are a variety of <sup>fi</sup>nancial news aggregation sites that provide this service. One of these sites is Comtex which offers real-time <sup>fi</sup>nancial news in a subscription format. Another source is PRNewsWire, which offers free real-time and subscriptionbased services. Yahoo! Finance is a third such source and is a compilation of 45 different news sources including the Associated Press, Financial Times and PRNewsWire among others. This source provides a variety of perspectives and timely news stories regarding <sup>fi</sup>nancial markets.

## 2.2. Textual representation

Once <sup>fi</sup>nancial news articles have been gathered they need to be represented in machine-friendly form. There are multiple techniques available, the <sup>fi</sup>rst of which is to tokenize the article and use each token as a feature. However, this technique is both noisy and has scalability issues from rarely used features. Furthermore, some repetitive features can detract from a prediction algorithm's accuracy. Features such as “http:” or semantically empty stopwords only add to the scalability overhead. There are a variety of ways to combat these problems which will be discussed throughout this section. The most popular way to represent text is to isolate particular features in an article, such as writing style, parts of speech or even author sentiment.

## 2.2.1. Writing style

Writing style analysis is a useful representation in document comparisons where the goal is to identify an unknown author amidst a corpus of known authors. Techniques include measures of similarity between documents and focusing on word choice and syntax usage [1].

## 2.2.2. Parts of speech

In a parts of speech representation, articles are represented by particular syntactic subsets, such as nouns or verbs. The most popular of which is the Bag of Words (BOW) approach which has been used extensively in textual <sup>fi</sup>nancial research [12,17]. This approach is similar to tokenization, except that stopwords such as conjunctions and declaratives are removed from the representation. Better versions of BOW will also employ some form of stemming where predicates are stripped and the root term representation remains. However, the BOW approach still has noise-related issues associated with infrequent terms as well as problems of scalability. An improved representational system is Noun Phrases which retains only the nouns and noun phrases from a document and can adequately represent important article concepts [35]. As a result, this technique uses fewer terms leading to better article scaling. A third representational technique is Named Entities, which is an extension of Noun Phrases. It functions by selecting the proper nouns of an article that fall within well-de<sup>fi</sup>ned categories. This process uses a semantic lexical hierarchy [30] as well as a syntactic/semantic tagging process [23] to assign candidate terms to pre-de<sup>fi</sup>ned categories. Named Entities allows for better generalization of previously unseen terms and does not possess the scalability problems associated with a semantics-only approach. A fourth representational technique is Proper Nouns. This method functions as an intermediary between Noun Phrases and Named Entities. Proper Nouns is a subset of Noun Phrases by selecting speci<sup>fi</sup>c nouns and a superset of Named Entities without the constraint of pre-de<sup>fi</sup>ned categories. In a comparison study using these four representational techniques, it was found that the Proper Noun representation was more effective in representing <sup>fi</sup>nancial news articles [29].

## 2.2.3. Author sentiment

In general, sentiment analysis is concerned with the analysis of direction-based text and attempts to determine whether the text is objective or subjective, as well as whether the subjective parts contain either positive or negative sentiments. This classi<sup>fi</sup>cation into positive and negative sentiments is a common two-class problem [26,36]. Additional variations include classifying sentiments as opinionated/ subjective or factual/objective [39]. Some studies have attempted to classify emotions, including happiness, sadness, anger, horror, etc., instead of sentiments [14,24,31].

Building upon these sentiment and tonal classi<sup>fi</sup>cations, [19] developed an SVM clustering technique which found that popular chat forum topics all shared certain sentiment values and that it was possible to predict future topical hotspots based on their similarity to the sentiment characteristics. While our research does not investigate topical similarity, the same underlying methods can be used to derive stock price movement, or online product sales, such as <sup>fi</sup>nancial press releases and <sup>fi</sup>nancial news [8,9,34], or user generated content [2,7,11]. From these investigations, it was discovered that negative sentiment may be predictive of future downward moves in <sup>fi</sup>rm value [34] and that positive and negative polarities in <sup>fi</sup>nancial news are consistent with human judgment [9] and have an impact on <sup>fi</sup>rm performance [7,8,11].

One well-known and tested tool to measure an article's sentiment is OpinionFinder. This tool aims to identify subjective sentences and classify them as either positive or negative sentiments [40]. It was developed by Wiebe's group based on a series of publications, such as the subjective sentence classi<sup>fi</sup>er [28,38], and the polarity classi<sup>fi</sup>er [41]. It also has relatively good performance compared against the MPQA Opinion Corpus, with an accuracy of 74%, subjective precision of 78.4%, subjective recall of 73.2% and a subjective F-measure of 75.7% as compared to baseline accuracy of 55.3%.

## 2.3. Machine representation

Machine learning algorithms are unable to process raw text or sentiment representations and require an additional layer of representation. One popular method is to represent article terms in binary where the term is either present or not in a given article [16]. This binary solution is typically implemented using a massive matrix where articles comprise one axis and the other axis is all of the terms in the corpora and other article-speci<sup>fi</sup>c features. It leads to large but sparse matrices where the number of represented terms throughout the dataset will greatly outnumber the number of terms used in an individual article.

Once <sup>fi</sup>nancial news articles have been represented, learning algorithms can then begin to identify patterns of behavior and build prediction models from them. One commonly accepted method, Support Vector Regression (SVR), is a regression equivalent of Support Vector Machines (SVM) but without the aspect of classi<sup>fi</sup>cation [37]. Like SVM, SVR attempts to minimize its <sup>fi</sup>tting error while maximizing its goal function by <sup>fi</sup>tting a regression estimate through a multidimensional hyperplane. This method is also well-suited to handling textual input in binary and has been used in similar <sup>fi</sup>nancial news studies [29,32].

## 3. Research questions

From these gaps, we have formulated several research questions. The <sup>fi</sup>rst of which is:

• Does Objectivity/Subjectivity impact news article prediction?

While we know from the literature that the tone of an article can correlate to future price direction, can the addition of objectivity and subjectivity provide improved discrete prediction?

As a follow-up to this question, we also ask:

• Does Positive/Negative Subjectivity impact news article prediction?

From the literature, we know that the subjectivity of an article will impact the share price in the same direction over the long term, but shorter periods of time have not been examined and could perhaps lead to interesting results.

## 4. System design

In order to evaluate our research questions, we designed the AZFinText system. Fig. 1 illustrates the basic design.

From the AZFinText system design in Fig. 1, there are several major components to describe in detail. The <sup>fi</sup>rst component is Numerical Data that gathers stock price data in one minute increments from a commercially available stock price database. The second component is Textual Analysis. This component gathers <sup>fi</sup>nancial news articles from Yahoo! Finance and represents them by their proper nouns as well as by the sentiment of the article. This module further limits extracted features to three or more occurrences in any document, which cuts down the noise from rarely used terms [16].

Once data is gathered, AZFinText makes price predictions, 20 min after the news article has been released, for each <sup>fi</sup>nancial news article. This 20 min period was selected because it follows the research of Gidofalvi who observed a twenty minute window of weak predictability [12]. From prior empirical testing, it was found that including the proper noun representation and the stock price at the time the news article was released, provided AZFinText with superior predictive performance compared to other textual representations and different pieces of price information [29].

At the Model Building stage, we partitioned the data into three models. The <sup>fi</sup>rst of which is the AZFinText system without sentiment information. This model only incorporates the proper nouns of the article and the price of the stock at the time the article was released. The second model of Tone is AZFinText plus three sentiment features of objective, subjective and neutral. We then used the OpinionFinder tool to make a determination of the overall tone of the article, i.e., is the article more objective or more subjective. In cases of a tie between objective and subjective, the article was marked neutral. The third model of Polarity is AZFinText plus three subjective sub-features of positive, negative and neutral. Even though an article may be marked as objective, we felt that the minority subjective aspects may make a valuable contribution to price prediction and should certainly be tested. As an example of the subjective and objective aspects of the OpinionFinder tool, we present two <sup>fi</sup>- nancial news articles, one marked subjective and the other objective.

Article marked SubjectiveBaby Talk at Coach by Alyce Lomax (Dec. 5, 2005)I have to admit: I chuckled in amazement when I saw that Coach (NYSE: COH) offers a line of baby products. I had a hard time dealing with the thought of tiny Coach purses, tiny Coach leather gloves and other miniaturized Coach wares. (And given the Coach brand name, it's guaranteed that all of this tiny stuff will bear grown-up price tags.)Coach certainly does offer cashmere mittens, blankets, and teddy bears for infants and babies. However, the vast majority of the product line includes leather photo albums enamel frames and of course what might be seen as a must-have for the well-heeled Mom a Coach baby bag. When it comes to designer apparel and accouterments for a baby I would imagine that lots of us would most certainly blink an eye at say the Coach pom-pom cap for baby that costs \$98 (as do the mittens mentioned above). The product line includes a \$398 diaper-and-associated-baby-necessities bag, a \$58 teddy bear, and last but not least, a \$48 key fob. (Ahem!)Many moms certainly go for less expensive baby gear — Target (NYSE: TGT) or Gap's (NYSE: GPS) Old Navy are big destinations for parents who juggle the needs of a newborn in a more frugal manner. I know many moms who are of the opinion that spending too much money on gear is silly when baby grows out of everything quite soon enough. (Not to mention, infants certainly don t distinguish according to brand — if they did, parents would be in big trouble!) Regardless, though there are plenty of people who prefer luxury or aspirational brands — Coach is a popular one as is Tiffany (NYSE: TIF).It may have seemed silly to me at <sup>fi</sup>rst blush, but Coach has been doing quite well as an investment over the years, having successfully attracted a cross-section of shoppers in different income brackets many of whom see the brand as an affordable luxury. Meanwhile it is the holiday season when doting grandparents and other family members are gearing up to <sup>fi</sup>nd the perfect gift for special little someones everywhere. Coach for baby might seem like madness to some of us — but it seems more than likely there's great method to the madness as the holidays approach. (Credit: Motley Fool)

![](/api/attachments/EKJYJCUG/fulltext/images/fe4a0ff7792f47472b89a28d1b902eb9608369e7261fbc27ed25befab8b96731.jpg)  
Fig. 1. The AZFinText system.

Article marked ObjectiveProcter increase in price products pays off (Nov. 1, 2005)Procter & Gamble Co.'s quarterly pro<sup>fi</sup>t rose 4.5% the company announced Tuesday after price increases and new product additions. Net income in the <sup>fi</sup>rst quarter at Procter increased to \$2.03 billion or 77 cents a share on a sales gain of 7.6%.Procter raised prices on Pampers diapers and Cascade dishwashing detergent and sales of new products such as Tide with Febreze scent increased. The company was trying to recover cost increases of raw materials including oil and resin. Procter was forecast to earn 76 cents a share according to the average estimate of 12 analysts surveyed by Thomson Financial.Procter is adding health and beauty items to grab market share from Kimberly-Clark Corp. The company had announced earlier this year increases on Ivory soap Cascade dishwashing detergent and Gain laundry detergent to try to recover some of the higher costs of raw materials including resin. So far the majority of the company's price increases have been accepted by retail and passed on to the end consumer Christopher Ferrara an analyst at Merrill Lynch amp; Co. in New York wrote in a report.

Procter also expanded sales in China and other developing markets which account for about 23% of Procter's annual revenue. Cincinnati-based Procter & Gamble (NYSE: PG) has a product lineup that includes Crest toothpaste and Pampers diapers. (Credit: Cincinnati Business Courier)For the machine learning algorithm we chose to implement the SVR Sequential Minimal Optimization [27] function through Weka [42]. This function allows discrete numeric prediction instead of classi<sup>fi</sup>cation. We selected a linear kernel and ten-fold cross-validation. A similar prediction method was employed in the forecasting of future contracts [32].AZFinText is then trained on the data and performs price predictions for each <sup>fi</sup>- nancial news article encountered. Evaluations are then made regarding the effect of predicted stock price in terms of the models generated.

## 5. Experimental design

For the experiment, we selected a consecutive <sup>fi</sup>ve week period of time to serve as our experimental baseline. This period of research was from Oct. 26, 2005 to Nov. 28, 2005 and incorporates twentythree trading days. The <sup>fi</sup>ve-week period of study was selected because it gathered a comparable number of articles to prior studies: 6602 for Mittermayer [25] and 5500 for Gidofalvi [12]. We also observe that the <sup>fi</sup>ve-week period chosen did not have unusual market conditions and was a good testbed for our evaluation. In order to identify the companies with the most likelihood of having quality <sup>fi</sup>nancial news, we limited our scope of activity to only those companies listed in the S&P 500 as of Oct. 3, 2005. Articles gathered during this period were restricted to occur between the hours of 10:30am and 3:40pm. Even though trading starts at 9:30am, we felt it important to reduce the impact of overnight news on stock prices and selected a period of 1 h to allow these prices to adjust. The 3:40pm cut-off was selected to disallow any +20 minute stock predictions to occur after market hours. A further constraint to reduce the effects of confounding variables was introduced where two articles on the same company cannot exist within 20 min of each other or both will be discarded. The above processes <sup>fi</sup>ltered the 9211 candidate news articles gathered during this period to 2802, where the majority of discarded articles occurred outside of market hours. Similarly, 10,259,042 per-minute stock quotations were gathered during this period. This large testbed of time-tagged articles and <sup>fi</sup>ne-grain stock quotations allow us to perform a systematic evaluation.

AZFinText's predictions were then analyzed against a three metric evaluation of Closeness, Directional Accuracy and a simple Trading Engine. Closeness, or how close AZFinText's predicted +20 min value was to the actual +20 min price, is measured in terms of Mean Squared Error (MSE) where MSE=(1/n)Σ(Predicted−Actual)<sup>2</sup> [5]. Directional Accuracy is simply how often AZFinText was correct in predicting the price direction of the +20 min stock [12]. For a Trading Engine, AZFin-Text utilized a modi<sup>fi</sup>ed version of Lavrenko's Trading Engine [17] that examines the percentage return of the stock. When a stock demonstrates an expected movement exceeding 1%, then \$1000 worth of that stock is either bought or shorted and then disposed of after 20 min. This modi<sup>fi</sup>ed version differs slightly from Lavrenko's original design, where Lavrenko traded in blocks of \$10,000 instead of \$1000. We further assume zero transaction costs, consistent with Lavrenko.

An example of AZFinText in operation is shown in Fig. 2.

The <sup>fi</sup>rst task is to extract <sup>fi</sup>nancial news articles. The entire corpus of <sup>fi</sup>nancial news articles is represented by their Proper Nouns in binary. If a particular Proper Noun feature is present in the article, that feature is given a 1, else a 0 and then stored in the database. Similarly, each <sup>fi</sup>nancial news article is evaluated by OpinionFinder to identify its overall tone and polarity. In tandem, stock quotations gathered on a per minute basis and stored. To build a model, we <sup>fi</sup>rst pair together the representational Proper Nouns and stock quotation at the time the article was released, for each <sup>fi</sup>nancial news article. Then, depending upon the particular model that is tested, data is aggregated and passed to our machine learning component for training and testing. Stock price predictions are then made for each <sup>fi</sup>nancial news article and passed along to the evaluation instruments.

From the example above, AZFinText derived a prediction price of \$15.945 which is greater than 1% of the stock price at the time the article was released, \$15.65. Our trading engine makes a trade and sells 20 min later, for a trade return of \$23.64 or 2.36%.

## 6. Experimental results

To answer our <sup>fi</sup>rst research question of does Objectivity/Subjectivity impact news article prediction, we tested AZFinText (Baseline), against Tone (AZFinText plus binary representations of objective, subjective and neutral). We further broke apart Tone into individual Objective, Subjective and Neutral components to further investigate Tone's impact, as shown in Table 1.

Tone performed poorly against Baseline in all three metrics. Although it may seem that the addition of sentiment variables harmed AZFinText's predictive capability, when Tone was sub-divided into its three constituent parts of Objective, Subjective and Neutral, it became apparent that several of Tone's components were depressing its overall score. Objective articles were performing poorly in Directional Accuracy versus Baseline (49.5% to 50.4% respectively) and Neutral articles had poorer Trading Returns versus Baseline (0.42% to 2.41% respectively). By contrast, Subjective articles performed better with 59.0% Directional Accuracy and a 3.30% Trading Return. From these results, Baseline, which did not include any sentiment analysis in its model, had the best Closeness score of 0.0516 while subjective articles had the best Directional Accuracy (59.0%) and Trading Return (3.30%). This would imply that the author's use of subjectivity in <sup>fi</sup>nancial news articles demonstrated marked price movement immediately following article release. These results were all signi<sup>fi</sup>cant as all values versus Baseline's values had p-valuesb0.05. Digging further into the subjective trading returns, of the 61 opportunities to trade, there were 10 instances where AZFinText executed a trade for an average return of \$3.30 (standard deviation of \$7.92). The maximum return was \$390 and the minimum was 60.

To answer our second research question of does Positive/Negative subjectivity impact news article prediction, we tested AZFinText (Baseline) against Polarity, which was AZFinText plus the binary representations of positive, negative and neutral. We further broke apart Polarity into its constituent components of Positive, Negative and Neutral to further investigate Polarity's impact, as shown in Table 2.

Polarity performed poorly versus Baseline in all three metrics (0.0556 to 0.0516 in Closeness, 49.4% to 50.4% in Directional Accuracy and 2.29% to 2.41% in Trading Returns). We suspect that the addition of the polarity variables was detrimental to AZFinText's predictions. However, by breaking apart Polarity into its component pieces, interesting results occurred. As shown in Table 2, Baseline again performed best in measures of Closeness (0.0516). Negative subjective articles performed best in both Directional Accuracy (50.9%) and Trading Returns (3.04%). We believe that this may be a psychological re<sup>fl</sup>ection of market dynamics because negative emotions can have a larger and more lasting impact than positive or neutral ones. These results were all signi<sup>fi</sup>cant as all values versus Baseline's values had p-valuesb0.05 except for Positive Closeness, which was statistically equivalent to Baseline. Looking closer at the negative polarity results, of the 1077 opportunities to execute a trade, AZFinText traded in 82 of them for an average return of \$3.04 (standard deviation of \$22.30). The maximum return was \$610 and the minimum was −\$250.

![](/api/attachments/EKJYJCUG/fulltext/images/6ccdee810ffe9f995ead6b7018a09ae54308a84aa4bad57cdab389b145a7d74d.jpg)  
Fig. 2. AZFinText textual example.

Table 1  
Article tone results (all p-values versus baseline b 0.05).

<table><tr><td></td><td>Baseline</td><td>Tone</td><td>Objective</td><td>Subjective</td><td>Neutral</td></tr><tr><td># Articles</td><td>2802</td><td>2802</td><td>2662</td><td>61</td><td>79</td></tr><tr><td>Closeness</td><td>0.0516</td><td>0.0565</td><td>0.0544</td><td>0.103</td><td>0.0930</td></tr><tr><td>Direction</td><td>50.4%</td><td>49.8%</td><td>49.5%</td><td>59.0%</td><td>53.2%</td></tr><tr><td>Trading</td><td>2.41%</td><td>2.00%</td><td>2.03%</td><td>3.30%</td><td>0.42%</td></tr></table>

To pursue why negative articles were easier to predict, we looked at the three component pieces of Polarity (Positive, Negative and Neutral) in terms of AZFinText's ability to correctly predict price direction, as shown in Table 3.

From this table, AZFinText worked best at predicting downswings of price in Positive Polarity articles (53.5%) and price upswings on both Negative and Neutral Polarity articles (52.4% and 49.5% respectively). All pvaluesb0.05. AZFinText exhibited seemingly counter-intuitive results where positive articles were easier to predict price decreases whereas negative and neutral articles were easier to predict price increases. We believe that perhaps this result can be attributable to market traders behaving in a contrarian manner, e.g., see good news, sell… see bad news, buy.

An example of this contrarian behavior is shown in the following PRNewsWire article, Goodyear, Tire Industry Association Join Forces on Certification, in which Goodyear describes their training certi<sup>fi</sup>cation program.

The industry-<sup>fi</sup>rst collaboration between a tire company and the international industry trade association includes two one-day seminars in 48 cities next year. Tire technicians from the Goodyear Dunlop and Kelly dealer network as well as Wingfoot Commercial Tire Centers are eligible for the Goodyear/TIA joint certi<sup>fi</sup>cation. Steve McClellan Goodyear's vice president of commercial tire systems said the customized training combines TIA's commercial tire service program and Goodyear's hands-on experience. TIA's certi<sup>fi</sup>cation process offers technicians valuable information that will help them perform their jobs better and with more care particularly as we embark on an aggressive campaign to expand our service business through a strong network of tire servicing outlets. McClellan said Goodyear seeks to improve its service business revenue which is more stable than cyclical commercial tire sales. Knowledgeable tire technicians across more than 2000 commercial tire centers will deliver unrivaled service to our customers in their quest to lower costs. The service equation becomes a win-win for Goodyear and its dealer network. Al Cohn manager of strategic initiatives for Goodyear's commercial tire systems said dealer training is a major initiative. Our vision is to do more than just manufacture quality tires. We want to create business solutions that are measurable, repeatable and sustainable. That means helping dealers to work with <sup>fl</sup>eets to manage their tire costs from original equipment to replacement and retreads and delivering service and value along the way. In addition the course exceeds OSHA training requirements for improved safety awareness. And that's why Goodyear/ TIA technician certi<sup>fi</sup>cation makes sense. Through this collaboration the training provides a competitive advantage for independent dealers to grow their tire and service business, he said. Goodyear/TIA certi<sup>fi</sup>cation also may reduce dealer workers compensation costs, Cohn added. Goodyear commercial tire systems offer complete products and services to the trucking industry including a full range of original equipment and replacement tires. In addition the company's cradle-tograve tire and service network includes retreading tire management tools and business solutions for tomorrow's trucking <sup>fl</sup>eets. For more information on Goodyear's line of commercial tires, go to http:// www.goodyear.com/truck.

Table 2  
Article polarity results (all p-values versus baseline b 0.05 except positive closeness).

<table><tr><td></td><td>Baseline</td><td>Polarity</td><td>Positive</td><td>Negative</td><td>Neutral</td></tr><tr><td># Articles</td><td>2802</td><td>2802</td><td>619</td><td>1077</td><td>1106</td></tr><tr><td>Closeness</td><td>0.0516</td><td>0.0556</td><td>0.0521</td><td>0.0576</td><td>0.0557</td></tr><tr><td>Direction</td><td>50.4%</td><td>49.4%</td><td>50.1%</td><td>50.9%</td><td>47.6%</td></tr><tr><td>Trading</td><td>2.41%</td><td>2.29%</td><td>1.73%</td><td>3.04%</td><td>1.98%</td></tr></table>

Table 3  
Article polarity versus directional accuracy (all p-valuesb 0.05)

<table><tr><td>Correct predictions</td><td>Positive</td><td>Negative</td><td>Neutral</td></tr><tr><td>Upswings</td><td>46.0%</td><td>52.4%</td><td>49.5%</td></tr><tr><td>Downswings</td><td>53.5%</td><td>49.1%</td><td>46.0%</td></tr></table>

This article is a rather normal public relations piece that was marked with positive polarity and had a stock price of \$15.39 when released. AZFinText predicted the +20 min stock price to decline to \$15.136 and Goodyear's actual +20 min stock price was \$15.22, a clear decline. Since the price was stable prior to article release, it would appear contrarian trading was taking place. While it could be possible that some external event occurred simultaneously that forced the price downward, AZFinText found a statistically suf<sup>fi</sup>cient number of these declines occurring that if this trend were noticed by the company, they may have done far better managing their share price to not release any news articles during this time, positive or otherwise.

## 7. Conclusions

From our investigation we found several interesting results. The <sup>fi</sup>rst of which was that AZFinText was best able to predict Subjective articles in Directional Accuracy (59.0% to 50.4%) and Trading Returns (3.30% to 2.41%), but not Closeness (0.103 versus 0.0516). We felt that the subjectivity of the articles may have had an impact on trading behavior. The second notable result was that AZFinText was best able to predict Negative Subjective articles in Directional Accuracy (50.9% to 50.4%) and Trading Returns (3.04% to 2.41%), but not Closeness (0.0576 versus 0.0516). We believe that these results are attributable to investors reacting more strongly to negative articles, which further adds to the ideas of [9]. The third notable result was that AZFinText found evidence of Contrarian trading activity. AZFinText was better able to predict downswings in Positive articles (53.5%) and upswings in Negative and Neutral articles (52.4% and 49.5% respectively). This stands in contrast to the work of [34] whom observed that negative sentiments should be indicative of downward price movement. It is possible that this work and that of Tetlock observed differing snapshots of market trading activity that led to differing results. Clearly more research is needed to determine the full extent of market trading behavior on mechanized prediction.

We would also suggest several future directions for this area of research. The <sup>fi</sup>rst of which is to investigate the role of verbs and adverbs as a textual representation method. Perhaps this representational scheme will lead to better predictivity than Proper Nouns alone. It would be bene<sup>fi</sup>cial in future studies to draw comparisons between various textual representations. The second future direction would be to investigate other machine learning techniques. While SVR has proven itself in the textual <sup>fi</sup>nancial domain, perhaps other techniques could identify different types of hidden market patterns. The third future direction would be to explore the role of negation in the OpinionFinder tool and its impact on price direction. While OpinionFinder has satisfactory accuracy at 74%, an unaccounted for negation could introduce a small amount of noise into the results. It would be important to determine its overall impact before constructing a real-time trading system.

## References

[1] A. Abbasi, H. Chen, Writeprints: a stylometric approach to identify-level identi<sup>fi</sup>- cation and similarity detection in cyberspace, ACM Transactions on Information Systems 26 (2) (2008).

[2] W. Antweiler, M. Frank, Is all that talk just noise? The information content of internet stock message boards, Journal of Finance 59 (3) (2004) 1259–1294.

[3] C. Camerer, K. Weigelt, Information mirages in experimental asset markets, Journal of Business 64 (4) (1991) 463–493.

[4] M. Cecchini, H. Aytug, et al., Making words work: using <sup>fi</sup>nancial text as a predictor of <sup>fi</sup>nancial events, Decision Support Systems (2010), doi:10.1016/j.dss.2010.07.012.

[5] V. Cho, B. Wuthrich, et al., Text processing for classi<sup>fi</sup>cation, Journal of Computational Intelligence in Finance 7 (2) (1999).

[6] S. Das, The <sup>fi</sup>nance web: internet information and markets, IEEE Intelligent Systems 25 (2) (2010).

[7] S. Das, M. Chen, Yahoo! for Amazon: sentiment extraction from small talk on the web, Management Science 53 (9) (2007) 1375–1388.

[8] A. Davis, J. Piger, et al., Beyond the numbers: an analysis of optimistic and pessimistic language in earnings press releases, Technical Report, Federal Reserve Bank of St. Louis, 2006.

[9] A. Devitt, K. Ahmad, Sentiment Polarity Identi<sup>fi</sup>cation in Financial News: A Cohesion-Based Approach, Association of Computational Linguistics, Prague, Czech Republic, 2007.

[10] E. Fama, The behavior of stock market prices, Journal of Business 38 (1) (1964) 34–106.

[11] A. Ghose, P. Ipeirotis, et al., Opinion Mining Using Econometrics: A Case Study on Reputation Systems, Association of Computational Linguistics, Prague, Czech Republic, 2007.

[12] G. Gidofalvi, Using News Articles to Predict Stock Price Movements, Department of Computer Science and Engineering, University of California, San Diego, 2001.

[13] G. Gidofalvi, C. Elkan, Using news articles to predict stock price movements, Technical Report, Department of Computer Science and Engineering, University of California, San Diego, 2003.

[14] G. Grefenstette, Y. Qu, et al., Coupling niche browsers and affect analysis for an opinion mining application, 7th International Conference on “Recherche d'Information Assistee par Ordinateur”, Avignon, France, 2004.

[15] Z. Jelveh, How a computer knows what many managers don't, The New York Times, 2006.

[16] T. Joachims, Text categorization with support vector machines: learning with many relevant features, European Conference on Machine Learning, Chemnitz, Germany, 1998.

[17] V. Lavrenko, M. Schmill, et al., Language models for <sup>fi</sup>nancial news recommendation, International Conference on Information and Knowledge Management, Washington, DC, 2000.

[18] B. LeBaron, W.B. Arthur, et al., Time series properties of an arti<sup>fi</sup>cial stock market, Journal of Economic Dynamics and Control 23 (9–10) (1999) 1487–1516.

[19] N. Li, D.D. Wu, Using text mining and sentiment analysis for online forums hotspot detection, Decision Support Systems 48 (2009) 354–368.

[20] H.-M. Lu, H. Chen, Financial text mining: supporting decision making using Web 2.0 content, IEEE Intelligent Systems 25 (2) (2010).

[21] Z. Ma, O. Sheng, et al., Discovering company revenue relations from news: a network approach, Decision Support Systems 47 (2009) 408–414.

[22] B.G. Malkiel, A Random Walk Down Wall Street, W.W. Norton & Company Ltd., New York, 1973.

[23] D.M. McDonald, H. Chen, et al., Transforming open-source documents to terror networks: the Arizona terrornet, American Association for Arti<sup>fi</sup>cial Intelligence Conference Spring Symposia, Stanford, CA, 2005.

[24] G. Mishne, Experiments with Mood Classi<sup>fi</sup>cation in Blog Posts, SIGIR, Salvador, Brazil, 2005.

[25] M. Mittermayer, Forecasting intraday stock price trends with text mining techniques, Hawaii International Conference on System Sciences, Kailua-Kona, HI, 2004.

[26] B. Pang, L. Lee, et al., Thumbs up?: Sentiment Classi<sup>fi</sup>cation Using Machine Learning Techniques, Association for Computational Linguistics, Philadelphia, PA, 2002.

[27] J.C. Platt, Fast training of support vector machines using sequential minimal optimization, in: B. Scholkopf, C. Burges, A. Smola (Eds.), Advances in Kernel Methods: Support Vector Learning, MIT Press, Cambridge, MA, 1999, pp. 185–208.

[28] E. Riloff, J. Wiebe, Learning extraction patterns for subjective expressions, Conference on Empirical Methods in Natural Language Processing, Sapporo, Japan, 2003.

[29] R.P. Schumaker, H. Chen, Textual analysis of stock market prediction using breaking <sup>fi</sup>nancial news: the AZFinText system, ACM Transactions on Information Systems 27 (2) (2009).

[30] S. Sekine, C. Nobata, De<sup>fi</sup>nition, dictionaries and tagger for extended named entity hierarchy Language Resources and Evaluation Conference Lisbon, Portugal 2004

[31] P. Subasic, A. Huettner, Affect analysis of text using fuzzy semantic typing, IEEE Transactions on Fuzzy Systems 9 (4) (2001) 483–496.

[32] F. Tay, L. Cao, Application of support vector machines in <sup>fi</sup>nancial time series forecasting, Omega 29 (2001) 309–317.

[33] Technical Analysis, The Trader's Glossary of Technical Terms and TopicsRetrieved Mar. 15, 2005, 2005, from, http://www.traders.com2005.

[34] P. Tetlock, Giving content to investor sentiment: the role of media in the stock market, Journal of Finance 62 (3) (2007) 1139–1168.

[35] K.M. Tolle, H. Chen, Comparing noun phrasing techniques for use with medical digital library tools, JASIS 51 (4) (2000) 352–370.

[36] P.D. Turney, Thumbs up or thumbs down? Semantic orientation applied to unsupervised classi<sup>fi</sup>cation of reviews, Association for Computational Linguistics (ACL'02), Philadelphia, PA, 2002.

[37] V. Vapnik, The Nature of Statistical Learning Theory, Springer, New York, 1995.

[38] J. Wiebe, E. Riloff, Creating subjective and objective sentence classi<sup>fi</sup>ers from unannotated texts, Sixth International Conference on Intelligent Text Processing and Computational Linguistics, Mexico City, Mexico, 2005.

[39] J. Wiebe, T. Wilson, et al., Learning subjective language, Computational Linguistics 30 (3) (2004) 277–308.

[40] T. Wilson, P. Hoffmann, et al., OpinionFinder: a system for subjectivity analysis, Human Language Technology Conference, Vancouver, Canada, 2005.

[41] T. Wilson, J. Wiebe, et al., Recognizing contextual polarity in phrase-level sentiment analysis, Conference on Human Language Technology and Empirical Methods in Natural Language Processing, Vancouver, Canada, 2005.

[42] I.H. Witten, F. Eibe, Data Mining: Practical Machine Learning Tools and Techniques, Morgan Kaufmann, San Francisco, 2005.

[43] B. Wuthrich, V. Cho, et al., Daily stock market forecast from textual web data, IEEE International Conference on Systems, Man, and Cybernetics, San Diego, CA, 1998.

![](/api/attachments/EKJYJCUG/fulltext/images/0b989b44891ed2d9961bdd16c7279dbf5dc8306ba3dd01d809abc4dd7210cfc4.jpg)  
Dr. Robert P. Schumaker is an Associate Professor of Management Information Systems (MIS) at Central Connecticut State University. He received his undergraduate degree in Civil Engineering from the University of Cincinnati, an MBA degree in Management and International Business from the University of Akron and his Ph.D. degree in Management from The University of Arizona. His interests include Stock Price Prediction, Natural Language systems and Textual Analysis techniques

![](/api/attachments/EKJYJCUG/fulltext/images/d22f465f70101c3b20a3b598dcd6bc264bb785be191218cac47f8106d85824cf.jpg)  
Dr. Yulei Zhang is an Assistant Professor of Computer Information Systems (CIS) at The W.A. Franke College of Business at Northern Arizona University. His research interests include data mining and bioinformatics.

![](/api/attachments/EKJYJCUG/fulltext/images/0d0f87f35bca4a41d691d87123f327350f1055f25c9cabda5662f8dc67e37aa8.jpg)

Mr. Chun-Neng Huang is a Software Design Engineer in Test (SDET) at Microsoft. He obtained his B.S.M degree from National Chiao Tung University in Management Science in 2001, an MBA from National Sun Yat-Sen University in 2003 and a Master's in Management Information Systems (MIS) from the University of Arizona in 2011. His research interests include data mining and text mining.

![](/api/attachments/EKJYJCUG/fulltext/images/229e8e0b9c8268c06ecb766bd15ff75960ae398be7a8b12bd4e08c4e11061fb6.jpg)

Dr. Hsinchun Chen is McClelland Professor of Management Information Systems at the University of Arizona and Andersen Consulting Professor of the Year (1999). He received the B.S. degree from the National Chiao-Tung University in Taiwan, the MBA from the SUNY Buffalo, and the Ph.D. degree in Information Systems from New York University. He is author of seven books and more than 120 SCI journal articles covering intelligence analysis, data/text/web mining, digital library, knowledge management, medical informatics, and Web computing.
